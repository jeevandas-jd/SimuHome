from typing import List, Optional, Dict, Any, Set
from enum import IntEnum

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode


class PowerTopologyFeature(IntEnum):
    

    NODE_TOPOLOGY = 0x01
    TREE_TOPOLOGY = 0x02
    SET_TOPOLOGY = 0x04
    DYNAMIC_POWER_FLOW = 0x08


class PowerTopologyCluster(Cluster):
    

    CLUSTER_ID = 0x009C
    CLUSTER_NAME = "PowerTopology"
    CLUSTER_REVISION = 1


    FEATURE_NODE = PowerTopologyFeature.NODE_TOPOLOGY
    FEATURE_TREE = PowerTopologyFeature.TREE_TOPOLOGY
    FEATURE_SET = PowerTopologyFeature.SET_TOPOLOGY
    FEATURE_DYPF = PowerTopologyFeature.DYNAMIC_POWER_FLOW


    ATTR_AVAILABLE_ENDPOINTS = 0x0000
    ATTR_ACTIVE_ENDPOINTS = 0x0001


    MAX_ENDPOINTS = 20

    def __init__(
        self, features: PowerTopologyFeature = PowerTopologyFeature.NODE_TOPOLOGY
    ):
        
        super().__init__(self.CLUSTER_NAME)

        self.features = features
        self._validate_feature_combination()


        self.attributes = {
            "ClusterRevision": self.CLUSTER_REVISION,
            "FeatureMap": self.features.value,
        }


        if self.has_feature(self.FEATURE_SET):
            self.attributes[self.ATTR_AVAILABLE_ENDPOINTS] = []
            self.readonly_attributes.add(self.ATTR_AVAILABLE_ENDPOINTS)

        if self.has_feature(self.FEATURE_DYPF):
            self.attributes[self.ATTR_ACTIVE_ENDPOINTS] = []


        if not hasattr(self, 'readonly_attributes'):
            self.readonly_attributes = set()


        self.commands = {}


        self._power_relationships: Dict[int, Set[int]] = (
            {}
        )
        self._power_flow_direction: Dict[int, str] = (
            {}
        )

    def _validate_feature_combination(self):
        
        has_node = self.has_feature(self.FEATURE_NODE)
        has_tree = self.has_feature(self.FEATURE_TREE)
        has_set = self.has_feature(self.FEATURE_SET)
        has_dypf = self.has_feature(self.FEATURE_DYPF)


        illegal_combinations = [

            (
                has_dypf and not has_set,
                "DynamicPowerFlow feature requires SetTopology feature",
            ),

            (
                has_node and has_tree,
                "NodeTopology and TreeTopology features are mutually exclusive",
            ),
            (
                has_node and has_set,
                "NodeTopology and SetTopology features are mutually exclusive",
            ),
            (
                has_tree and has_set,
                "TreeTopology and SetTopology features are mutually exclusive",
            ),

            (
                not has_node and not has_tree and not has_set,
                "At least one topology feature is required",
            ),
        ]

        for is_illegal, message in illegal_combinations:
            if is_illegal:
                raise ValueError(
                    f"Illegal Power Topology feature combination: {message}"
                )

    def has_feature(self, feature: PowerTopologyFeature) -> bool:
        
        return bool(self.features & feature)

    def get_available_endpoints(self) -> List[int]:
        
        if not self.has_feature(self.FEATURE_SET):
            return []
        return self.attributes.get(self.ATTR_AVAILABLE_ENDPOINTS, [])

    def set_available_endpoints(self, endpoints: List[int]) -> Result:
        
        if not self.has_feature(self.FEATURE_SET):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND,
                "AvailableEndpoints attribute requires SetTopology feature",
            )

        if len(endpoints) > self.MAX_ENDPOINTS:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Too many endpoints specified (max {self.MAX_ENDPOINTS})",
            )


        if len(set(endpoints)) != len(endpoints):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Duplicate endpoint IDs not allowed"
            )


        self.attributes[self.ATTR_AVAILABLE_ENDPOINTS] = endpoints.copy()


        if self.has_feature(self.FEATURE_DYPF):
            active = self.attributes.get(self.ATTR_ACTIVE_ENDPOINTS, [])

            new_active = [ep for ep in active if ep in endpoints]
            if len(new_active) != len(active):
                self.attributes[self.ATTR_ACTIVE_ENDPOINTS] = new_active

        return Result.ok({"available_endpoints": endpoints})

    def get_active_endpoints(self) -> List[int]:
        
        if not self.has_feature(self.FEATURE_DYPF):
            return []
        return self.attributes.get(self.ATTR_ACTIVE_ENDPOINTS, [])

    def set_active_endpoints(self, endpoints: List[int]) -> Result:
        
        if not self.has_feature(self.FEATURE_DYPF):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND,
                "ActiveEndpoints attribute requires DynamicPowerFlow feature",
            )


        if self.has_feature(self.FEATURE_SET):
            available = self.get_available_endpoints()
            invalid_endpoints = [ep for ep in endpoints if ep not in available]
            if invalid_endpoints:
                return Result.fail(
                    ErrorCode.INVALID_ARGUMENT,
                    f"Active endpoints must be subset of available endpoints. Invalid: {invalid_endpoints}",
                )

        if len(endpoints) > self.MAX_ENDPOINTS:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Too many endpoints specified (max {self.MAX_ENDPOINTS})",
            )


        if len(set(endpoints)) != len(endpoints):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Duplicate endpoint IDs not allowed"
            )


        self.attributes[self.ATTR_ACTIVE_ENDPOINTS] = endpoints.copy()

        return Result.ok({"active_endpoints": endpoints})

    def add_power_relationship(
        self, endpoint_id: int, connected_endpoints: List[int], direction: str = "both"
    ) -> Result:
        
        if direction not in ["provider", "consumer", "both"]:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, f"Invalid power flow direction: {direction}"
            )

        self._power_relationships[endpoint_id] = set(connected_endpoints)
        self._power_flow_direction[endpoint_id] = direction

        return Result.ok(
            {
                "endpoint_id": endpoint_id,
                "connected_endpoints": connected_endpoints,
                "direction": direction,
            }
        )

    def remove_power_relationship(self, endpoint_id: int) -> Result:
        
        if endpoint_id in self._power_relationships:
            del self._power_relationships[endpoint_id]

        if endpoint_id in self._power_flow_direction:
            del self._power_flow_direction[endpoint_id]

        return Result.ok({"removed_endpoint": endpoint_id})

    def get_power_relationships(
        self, endpoint_id: Optional[int] = None
    ) -> Dict[str, Any]:
        
        if endpoint_id is not None:
            return {
                "endpoint_id": endpoint_id,
                "connected_endpoints": list(
                    self._power_relationships.get(endpoint_id, set())
                ),
                "direction": self._power_flow_direction.get(endpoint_id, "unknown"),
            }
        else:
            return {
                "all_relationships": {
                    str(ep_id): {
                        "connected_endpoints": list(connected),
                        "direction": self._power_flow_direction.get(ep_id, "unknown"),
                    }
                    for ep_id, connected in self._power_relationships.items()
                }
            }

    def validate_topology_constraints(self) -> Result:
        
        errors = []


        if self.has_feature(self.FEATURE_NODE):


            pass


        if self.has_feature(self.FEATURE_TREE):


            pass


        if self.has_feature(self.FEATURE_SET):
            available = self.get_available_endpoints()
            if not available:
                errors.append(
                    "SetTopology feature requires at least one available endpoint"
                )


        if self.has_feature(self.FEATURE_DYPF):
            if not self.has_feature(self.FEATURE_SET):
                errors.append("DynamicPowerFlow feature requires SetTopology feature")
            else:
                active = self.get_active_endpoints()
                available = self.get_available_endpoints()
                invalid_active = [ep for ep in active if ep not in available]
                if invalid_active:
                    errors.append(
                        f"Active endpoints not in available list: {invalid_active}"
                    )

        if errors:
            return Result.fail(
                ErrorCode.CONSTRAINT_ERROR,
                "Topology validation failed",
                {"errors": errors},
            )

        return Result.ok({"topology_valid": True})

    def get_topology_summary(self) -> Dict[str, Any]:
        
        summary = {
            "cluster_id": self.CLUSTER_ID,
            "cluster_name": self.CLUSTER_NAME,
            "revision": self.CLUSTER_REVISION,
            "features": {
                "node_topology": self.has_feature(self.FEATURE_NODE),
                "tree_topology": self.has_feature(self.FEATURE_TREE),
                "set_topology": self.has_feature(self.FEATURE_SET),
                "dynamic_power_flow": self.has_feature(self.FEATURE_DYPF),
            },
            "attributes": {},
        }

        if self.has_feature(self.FEATURE_SET):
            summary["attributes"][
                "available_endpoints"
            ] = self.get_available_endpoints()

        if self.has_feature(self.FEATURE_DYPF):
            summary["attributes"]["active_endpoints"] = self.get_active_endpoints()

        summary["power_relationships"] = self.get_power_relationships()

        return summary

    def read_attribute(self, attribute_id: str) -> Result:
        
        if attribute_id in self.attributes:
            return Result.ok(self.attributes[attribute_id])
        return Result.fail(
            ErrorCode.ATTRIBUTE_NOT_FOUND, f"Attribute {attribute_id} not found"
        )

    def write_attribute(self, attribute_id: str, value: Any) -> Result:
        

        if attribute_id in self.readonly_attributes:
            return Result.fail(
                ErrorCode.READ_ONLY, f"Attribute {attribute_id} is read-only"
            )


        if attribute_id == self.ATTR_AVAILABLE_ENDPOINTS:
            return self.set_available_endpoints(value)
        elif attribute_id == self.ATTR_ACTIVE_ENDPOINTS:
            return self.set_active_endpoints(value)
        elif attribute_id in self.attributes:
            self.attributes[attribute_id] = value
            return Result.ok(value)
        else:
            return Result.fail(
                ErrorCode.ATTRIBUTE_NOT_FOUND, f"Attribute {attribute_id} not found"
            )

    def __str__(self) -> str:
        
        feature_names = []
        if self.has_feature(self.FEATURE_NODE):
            feature_names.append("NODE")
        if self.has_feature(self.FEATURE_TREE):
            feature_names.append("TREE")
        if self.has_feature(self.FEATURE_SET):
            feature_names.append("SET")
        if self.has_feature(self.FEATURE_DYPF):
            feature_names.append("DYPF")

        features_str = "|".join(feature_names) if feature_names else "NONE"

        endpoint_info = ""
        if self.has_feature(self.FEATURE_SET):
            available_count = len(self.get_available_endpoints())
            endpoint_info += f", Available: {available_count}"

        if self.has_feature(self.FEATURE_DYPF):
            active_count = len(self.get_active_endpoints())
            endpoint_info += f", Active: {active_count}"

        return f"PowerTopologyCluster(Features: {features_str}{endpoint_info})"
