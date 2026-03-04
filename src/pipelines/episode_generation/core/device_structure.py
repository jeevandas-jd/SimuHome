from __future__ import annotations

from typing import List, MutableMapping, Tuple

from src.simulator.application.device_factory import create_device

ReadonlyAttribute = Tuple[int, str, str]


def _endpoint_sort_key(value: object) -> tuple[int, str]:
    try:
        return (0, f"{int(value):08d}")
    except Exception:
        return (1, str(value))


def _to_endpoint_id(value: object) -> int:
    try:
        return int(value)
    except Exception:
        return 1


def get_device_readonly_attributes(
    device_type: str,
    *,
    cache: MutableMapping[str, List[ReadonlyAttribute]] | None = None,
) -> List[ReadonlyAttribute]:
    key = str(device_type)
    if cache is not None and key in cache:
        return list(cache[key])

    structure = create_device(
        device_type=key, device_id=f"__template_{key}"
    ).get_structure()
    endpoints = structure.get("endpoints") or {}

    readonly: List[ReadonlyAttribute] = []
    for endpoint_id, endpoint_data in sorted(
        endpoints.items(), key=lambda item: _endpoint_sort_key(item[0])
    ):
        clusters = (endpoint_data or {}).get("clusters") or {}
        for cluster_id, cluster_data in sorted(
            clusters.items(), key=lambda item: str(item[0])
        ):
            attributes = (cluster_data or {}).get("attributes") or {}
            for attribute_id, attribute_meta in sorted(
                attributes.items(), key=lambda item: str(item[0])
            ):
                if bool((attribute_meta or {}).get("readonly", False)):
                    readonly.append(
                        (
                            _to_endpoint_id(endpoint_id),
                            str(cluster_id),
                            str(attribute_id),
                        )
                    )

    if cache is not None:
        cache[key] = list(readonly)
    return readonly


__all__ = ["get_device_readonly_attributes", "ReadonlyAttribute"]
