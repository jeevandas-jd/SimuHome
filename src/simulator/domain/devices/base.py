from enum import Enum
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from typing import Any, Optional, Dict


class Device:
    def __init__(
        self,
        device_id: str,
        device_type: str,
        basic_information_cluster: BasicInformationCluster,
    ):
        self.device_id = device_id
        self.device_type = device_type
        self.tick_interval = 0.1
        self.endpoints: dict[int, dict[str, Cluster]] = {0: {}}
        self.endpoints[0][basic_information_cluster.cluster_id] = basic_information_cluster

    @property
    def is_time_aware(self) -> bool:
        
        for endpoint_id, cluster_ids in self.endpoints.items():
            for cluster in cluster_ids.values():
                if hasattr(cluster, "on_time_tick"):
                    return True
        return False

    def has_batch_blocking_tick_work(self) -> bool:
        for cluster_ids in self.endpoints.values():
            for cluster in cluster_ids.values():
                tick_handler = getattr(cluster, "on_time_tick", None)
                if not callable(tick_handler):
                    continue

                block_predicate = getattr(cluster, "blocks_exact_batch_advance", None)
                if callable(block_predicate):
                    try:
                        if bool(block_predicate()):
                            return True
                        continue
                    except Exception:
                        return True

                return True

        return False

    def set_tick_interval(self, interval: float):
        
        self.tick_interval = interval

    def on_time_tick(self):
        
        for endpoint_id, cluster_ids in self.endpoints.items():
            for cluster in cluster_ids.values():
                tick_handler = getattr(cluster, "on_time_tick", None)
                if callable(tick_handler):
                    tick_handler()

    def add_endpoint(self, endpoint_id: int) -> Result:
        if endpoint_id not in self.endpoints:
            self.endpoints[endpoint_id] = {}
            return Result.ok({"endpoint_id": endpoint_id, "created": True})
        return Result.ok({"endpoint_id": endpoint_id, "created": False})

    def add_cluster(self, endpoint_id: int, cluster: Cluster) -> Result:
        
        if endpoint_id not in self.endpoints:
            self.endpoints[endpoint_id] = {}
        already = cluster.cluster_id in self.endpoints[endpoint_id]
        self.endpoints[endpoint_id][cluster.cluster_id] = cluster
        return Result.ok(
            {
                "endpoint_id": endpoint_id,
                "cluster_id": cluster.cluster_id,
                "replaced": already,
            }
        )

    def execute_command(self, endpoint_id, cluster_id, command_id, **args) -> Result:
        
        if endpoint_id not in self.endpoints:
            return ResultBuilder.endpoint_not_found(endpoint_id)
        if cluster_id not in self.endpoints[endpoint_id]:
            return ResultBuilder.cluster_not_found(cluster_id)
        cluster = self.endpoints[endpoint_id][cluster_id]
        return cluster.execute_command(command_id, **args)

    def write_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str, value: Any
    ) -> Result:
        
        if endpoint_id not in self.endpoints:
            return ResultBuilder.endpoint_not_found(endpoint_id)
        if cluster_id not in self.endpoints[endpoint_id]:
            return ResultBuilder.cluster_not_found(cluster_id)
        cluster = self.endpoints[endpoint_id][cluster_id]
        return cluster.write_attribute(attribute_id, value)

    def get_structure(self) -> Dict[str, Any]:

        structure: Dict[str, Any] = {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "endpoints": {},
        }
        for endpoint_id, clusters in self.endpoints.items():
            structure["endpoints"][endpoint_id] = {
                "clusters": {
                    cluster_id: cluster.get_structure()
                    for cluster_id, cluster in clusters.items()
                }
            }
        return self._to_jsonable(structure)

    def get_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str
    ) -> Optional[Any]:
        
        if endpoint_id not in self.endpoints:
            return None
        if cluster_id in self.endpoints[endpoint_id]:
            value = self.endpoints[endpoint_id][cluster_id].attributes.get(attribute_id)

            if cluster_id == "OperationalState" and attribute_id == "CurrentPhase":
                phase_list = self.endpoints[endpoint_id][cluster_id].attributes.get(
                    "PhaseList"
                )
                if (
                    isinstance(value, int)
                    and phase_list
                    and 0 <= value < len(phase_list)
                ):
                    return phase_list[value]
            return value
        return None

    def get_all_attributes(self) -> Dict[str, Any]:
        
        all_attrs: Dict[str, Any] = {}
        for endpoint_id, clusters in self.endpoints.items():
            for cluster_id, cluster in clusters.items():
                for attr_id, attr_value in cluster.attributes.items():
                    flattened_key = f"{endpoint_id}.{cluster_id}.{attr_id}"
                    all_attrs[flattened_key] = attr_value
        return all_attrs

    def _is_readonly_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str
    ) -> bool:
        
        cluster = self.get_cluster(endpoint_id, cluster_id)
        if cluster and hasattr(cluster, "readonly_attributes"):
            return attribute_id in cluster.readonly_attributes
        return False

    def get_cluster(self, endpoint_id: int, cluster_id: str) -> Optional[Cluster]:
        
        if endpoint_id in self.endpoints and cluster_id in self.endpoints[endpoint_id]:
            return self.endpoints[endpoint_id][cluster_id]
        return None

    @staticmethod
    def _parse_attribute_path(attr_path: str) -> tuple[int, str, str]:
        parts = attr_path.split(".")
        if len(parts) != 3:
            raise ValueError(f"Invalid attribute path format: {attr_path}")

        endpoint_id = int(parts[0])
        cluster_id = parts[1]
        attribute_id = parts[2]
        return endpoint_id, cluster_id, attribute_id

    def initialize_attributes(self, attr_config: Dict[str, Any]) -> Result:
        
        failed_attributes = []
        for attr_path, value in attr_config.items():
            try:
                endpoint_id, cluster_id, attribute_id = self._parse_attribute_path(attr_path)

                if endpoint_id not in self.endpoints:
                    failed_attributes.append(f"{attr_path} (endpoint not found)")
                    continue

                if cluster_id not in self.endpoints[endpoint_id]:
                    failed_attributes.append(f"{attr_path} (cluster not found)")
                    continue

                cluster = self.endpoints[endpoint_id][cluster_id]
                cluster.attributes[attribute_id] = value

            except Exception as e:
                failed_attributes.append(f"{attr_path} ({str(e)})")

        if failed_attributes:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Some attributes failed to initialize",
                f"Failed attributes: {', '.join(failed_attributes)}",
            )

        return Result.ok({"initialized_attributes": len(attr_config)})

    @staticmethod
    def _to_jsonable(o: Any):
        if isinstance(o, Enum):

            return o.name
        if isinstance(o, dict):
            return {
                Device._to_jsonable(k): Device._to_jsonable(v) for k, v in o.items()
            }
        if isinstance(o, (list, tuple)):
            return [Device._to_jsonable(x) for x in o]
        if isinstance(o, set):
            return [Device._to_jsonable(x) for x in sorted(o, key=lambda x: str(x))]

        if hasattr(o, "to_dict") and callable(getattr(o, "to_dict")):
            return Device._to_jsonable(o.to_dict())
        return o
