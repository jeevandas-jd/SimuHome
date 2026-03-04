from __future__ import annotations

import json
import os
import random
from typing import Any, Dict, List, Optional, Tuple, Union


REGISTRY_PATH = os.path.join(
    os.path.dirname(__file__),
    "targets_registry.json",
)


THERMOSTAT_SYSTEM_MODE_LABELS = {
    0x00: "off",  
    0x01: "auto",  
    0x03: "cooling",
    0x04: "heating",
}


MEDIA_PLAYBACK_STATE_LABELS = {
    0: "playing",  
    1: "paused",  
    2: "not playing",  
    3: "buffering",  
}


WINDOW_COVERING_SAFETY_LABELS = {0: "safe"}


OPERATIONAL_STATE_LABELS = {
    0x00: "stopped",  
    0x01: "running",  
    0x02: "paused",  
    0x03: "error",  
}


RVC_OPERATIONAL_STATE_LABELS = {
    0x00: "stopped",  
    0x01: "running",  
    0x02: "paused",  
    0x03: "error",  
    0x40: "seeking charger",  
    0x41: "charging",  
    0x42: "docked",
}


WASHER_MODE_LABELS = {
    0: "normal",  
    1: "delicate",  
    2: "heavy",  
    3: "whites",  
    4: "quick normal",  
    5: "heavy whites",  
}


DRYNESS_LEVEL_LABELS = {
    0: "low",  
    1: "normal",  
    2: "extra",  
    3: "max",  
}


def load_registry(path: Optional[str] = None) -> Dict[str, Any]:
    target_path = path or REGISTRY_PATH
    with open(target_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _auto_template_from_clusters(*, state_flat: Dict[str, Any]) -> Dict[str, Any]:
    
    targets: List[Dict[str, Any]] = []

    def has_attr(p: str) -> bool:
        return p in state_flat

    if has_attr("1.OnOff.OnOff"):
        targets.append(
            {"attribute": "1.OnOff.OnOff", "value": True, "value_type": "bool"}
        )

    if has_attr("1.LevelControl.CurrentLevel"):
        targets.append(
            {
                "attribute": "1.LevelControl.CurrentLevel",
                "sampling": {
                    "type": "range",
                    "range": {"min": 10, "max": 100, "step": 10},
                    "exclude_current": True,
                },
                "value_type": "percent",
            }
        )

    if has_attr("1.FanControl.PercentSetting") or has_attr(
        "1.FanControl.PercentCurrent"
    ):
        targets.append(
            {
                "attribute": "1.FanControl.PercentSetting",
                "sampling": {
                    "type": "bins",
                    "values": [30, 40, 50, 60, 70, 80],
                    "exclude_current": True,
                },
                "value_type": "percent",
            }
        )

    
    if has_attr("1.MediaPlayback.CurrentState"):
        targets.append(
            {
                "attribute": "1.MediaPlayback.CurrentState",
                "value": 0,
                "value_type": "enum",
            }
        )
    elif has_attr("1.MediaPlayback.PlaybackState"):
        targets.append(
            {
                "attribute": "1.MediaPlayback.PlaybackState",
                "value": 0,
                "value_type": "enum",
            }
        )

    return {"targets": targets} if targets else {"targets": []}


def _default_variant_from_auto(
    device_type: str, state_flat: Dict[str, Any]
) -> List[Dict[str, Any]]:
    _ = device_type
    auto = _auto_template_from_clusters(state_flat=state_flat)
    targets = auto.get("targets", [])
    if not targets:
        return []
    return [
        {
            "id": "default",
            "requires": [],
            "targets": targets,
            "prefer_change": True,
        }
    ]


def get_targets_template(
    *,
    registry: Dict[str, Any],
    device_type: str,
    state_flat: Dict[str, Any],
) -> List[Dict[str, Any]]:
    entry = (registry or {}).get("templates", {}).get(device_type)
    if isinstance(entry, list):
        return entry
    return _default_variant_from_auto(device_type=device_type, state_flat=state_flat)


def _pick_from_bins(
    rng: random.Random, values: List[int], current: Optional[int]
) -> Optional[int]:
    if not values:
        return None
    candidates = list(values)
    if isinstance(current, int) and current in candidates and len(candidates) > 1:
        candidates = [v for v in candidates if v != current]
    if not candidates:
        return None
    return rng.choice(candidates)


def _pick_from_range(
    rng: random.Random, spec: Dict[str, Any], current: Optional[int]
) -> Optional[int]:
    r = spec or {}
    lo = int(r.get("min", 0))
    hi = int(r.get("max", 100))
    step = int(r.get("step", 1))
    if lo > hi or step <= 0:
        return None
    values = list(range(lo, hi + 1, step))
    if len(values) == 0:
        return None
    if isinstance(current, int) and current in values and len(values) > 1:
        values = [v for v in values if v != current]
    return rng.choice(values)


def _read_current(
    state_flat: Dict[str, Any], attribute: Optional[str]
) -> Optional[int]:
    if not isinstance(attribute, str):
        return None
    v = state_flat.get(attribute)
    return v if isinstance(v, int) else None


def _sample_from_list(
    *,
    rng: random.Random,
    state_flat: Dict[str, Any],
    source_path: str,
    pick_field: str,
    exclude_value: Optional[Any] = None,
    return_meta: bool = False,
) -> Union[Optional[Any], Tuple[Optional[Any], Optional[Any]]]:
    
    source = state_flat.get(source_path)
    candidates: List[Any] = []
    candidates_meta: List[Any] = []

    if isinstance(source, list):
        for item in source:
            try:
                if pick_field in (None, "__self__"):
                    val = item
                elif isinstance(item, dict):
                    val = item.get(pick_field)
                else:
                    val = getattr(item, pick_field)
            except Exception:
                val = None
            if val is not None:
                candidates.append(val)
                candidates_meta.append(item)

    if exclude_value is not None and len(candidates) > 1:
        filtered_candidates = []
        filtered_meta = []
        for i, v in enumerate(candidates):
            if v != exclude_value:
                filtered_candidates.append(v)
                filtered_meta.append(candidates_meta[i])
        candidates = filtered_candidates
        candidates_meta = filtered_meta

    if not candidates:
        return (None, None) if return_meta else None

    selected_idx = rng.randint(0, len(candidates) - 1)
    selected_value = candidates[selected_idx]
    selected_meta = candidates_meta[selected_idx]

    if return_meta:
        return (selected_value, selected_meta)
    else:
        return selected_value


def _extract_label_from_meta(
    meta: Optional[Any], fields: Optional[List[str]] = None
) -> Optional[str]:
    
    if not isinstance(meta, dict):
        return None

    fields = fields or ["label", "name", "displayName", "title", "Identifier"]
    for field in fields:
        value = meta.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _generate_dynamic_description(
    attribute: str,
    value: Any,
    meta: Optional[Any] = None,
    value_type: Optional[str] = None,
) -> Optional[str]:
    

    if attribute.endswith("OnOff.OnOff"):
        return "on" if value else "off"

    if attribute.endswith("LevelControl.CurrentLevel"):
        if isinstance(value, int):
            return f"level {value}"
        return "level"

    if attribute.endswith("FanControl.PercentSetting") or attribute.endswith(
        "FanControl.PercentCurrent"
    ):
        if isinstance(value, int):
            return f"fan {value}%"
        return "fan"

    if "Temperature" in attribute and (
        "Setpoint" in attribute or "LocalTemperature" in attribute
    ):
        if isinstance(value, (int, float)):
            return f"temp {value / 100:.1f}°C"
        return "temperature"

    if "WindowCovering.TargetPositionLiftPercent100ths" in attribute:
        if isinstance(value, int):
            if value == 0:
                return "fully open"
            elif value == 10000:
                return "fully closed"
            else:
                percentage = value / 100
                return f"{percentage}% closed"
        return "position"

    if "WindowCovering.SafetyStatus" in attribute:
        return "safe" if value == 0 else "unsafe"

    
    if "Thermostat.SystemMode" in attribute:
        return THERMOSTAT_SYSTEM_MODE_LABELS.get(value)

    
    if "MediaPlayback.CurrentState" in attribute:
        return MEDIA_PLAYBACK_STATE_LABELS.get(value)

    
    if "WindowCovering.SafetyStatus" in attribute:
        return WINDOW_COVERING_SAFETY_LABELS.get(
            value, "unsafe" if value != 0 else None
        )

    
    if attribute.endswith("OperationalState.OperationalState"):
        return OPERATIONAL_STATE_LABELS.get(value)

    
    if "RVCOperationalState" in attribute:
        return RVC_OPERATIONAL_STATE_LABELS.get(value)

    
    if attribute.endswith("LaundryWasherMode.CurrentMode"):
        label = _extract_label_from_meta(meta)
        if label:
            return label.lower()
        return WASHER_MODE_LABELS.get(value)

    
    if attribute.endswith("LaundryDryerControls.SelectedDrynessLevel"):
        return DRYNESS_LEVEL_LABELS.get(value)

    if "Channel.CurrentChannel" in attribute:
        label = _extract_label_from_meta(meta, ["Name", "CallSign", "Identifier"])
        if label:
            return label
        return f"ch {value}" if value else None

    if meta and isinstance(meta, dict):
        label = _extract_label_from_meta(meta)
        if label:
            return label.lower()

    return None


def build_target_assert(
    *,
    device_type: str,
    state_flat: Dict[str, Any],
    registry: Optional[Dict[str, Any]] = None,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    
    rng = random.Random(seed)
    variants = get_targets_template(
        registry=registry or {}, device_type=device_type, state_flat=state_flat
    )
    candidates: List[Dict[str, Any]] = []
    for v in variants:
        requires = v.get("requires", [])
        satisfied = True
        for req in requires:
            r_attr: Optional[str] = req.get("attribute")
            expected = req.get("value")
            if r_attr is None or state_flat.get(r_attr) != expected:
                satisfied = False
                break
        if satisfied:
            candidates.append(v)
    chosen = (
        rng.choice(candidates)
        if candidates
        else (variants[0] if variants else {"targets": []})
    )

    asserts_out: List[Dict[str, Any]] = []

    for t in chosen.get("targets", []):
        attr: Optional[str] = t.get("attribute")
        vtype: Optional[str] = t.get("value_type")

        original_desc = t.get("description")

        if "value" in t:
            result = {"attribute": attr, "value": t["value"], "value_type": vtype}
            if original_desc:
                result["description"] = original_desc
            asserts_out.append(result)
            continue

        sampling = t.get("sampling") or {}
        exclude_current = bool(sampling.get("exclude_current"))
        val: Optional[int] = None
        meta: Optional[Any] = None
        stype = sampling.get("type")

        if stype in ("bins", "enum"):
            values: List[int] = list(sampling.get("values", []))
            current: Optional[int] = (
                _read_current(state_flat, attr) if exclude_current else None
            )
            val = _pick_from_bins(rng, values, current)
        elif stype == "range":
            spec = sampling.get("range") or {}
            current: Optional[int] = (
                _read_current(state_flat, attr) if exclude_current else None
            )
            val = _pick_from_range(rng, spec, current)
        elif stype == "from_list":
            source = sampling.get("source")
            pick_field = sampling.get("pick_field")
            exclude_path = sampling.get("exclude_path")
            exclude_val = state_flat.get(exclude_path) if exclude_path else None
            if isinstance(source, str) and isinstance(pick_field, str):
                sampled = _sample_from_list(
                    rng=rng,
                    state_flat=state_flat,
                    source_path=source,
                    pick_field=pick_field,
                    exclude_value=exclude_val,
                    return_meta=True,
                )
                if isinstance(sampled, tuple):
                    val, meta = sampled

        if val is None:
            cur = _read_current(state_flat, attr)
            if isinstance(cur, int):
                val = cur
            elif stype in ("bins", "enum"):
                values = list((sampling.get("values") or []))
                val = values[0] if values else 50
            elif stype == "range":
                spec = sampling.get("range") or {}
                lo = spec.get("min")
                hi = spec.get("max")
                step = spec.get("step", 1)
                try:
                    lo_i = int(lo) if lo is not None else 0
                    hi_i = int(hi) if hi is not None else 100
                    step_i = int(step) if step is not None else 1
                    mid = (lo_i + hi_i) // 2
                    
                    if step_i > 1:
                        mid = lo_i + ((mid - lo_i) // step_i) * step_i
                    val = mid
                except Exception:
                    val = 50
            elif stype == "from_list":
                val = state_flat.get(attr) if attr else None
            else:
                val = 50

        desc = original_desc
        if not desc and isinstance(attr, str):
            desc = _generate_dynamic_description(
                attr,
                val,
                meta,
                vtype if isinstance(vtype, str) else None,
            )

        result = {"attribute": attr, "value": val, "value_type": vtype}
        if desc:
            result["description"] = desc
        asserts_out.append(result)

    return asserts_out


__all__ = [
    "load_registry",
    "get_targets_template",
    "build_target_assert",
]
