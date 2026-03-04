from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.rvc_clean_mode import RVCCleanModeCluster
from src.simulator.domain.clusters.rvc_operational_state import (
    OperationalState,
    RVCOperationalStateCluster,
)
from src.simulator.domain.clusters.rvc_run_mode import ModeTag, RVCRunModeCluster
from src.simulator.domain.devices.base import Device


class RVC(Device):
    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "rvc",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="RVC",
                product_id=3,
            ),
        )

        run_mode = RVCRunModeCluster()
        _ = self.add_cluster(1, run_mode)
        self.run_mode = run_mode

        operational_state = RVCOperationalStateCluster()
        _ = self.add_cluster(1, operational_state)
        self.operational_state = operational_state

        clean_mode = RVCCleanModeCluster()
        _ = self.add_cluster(1, clean_mode)
        self.clean_mode = clean_mode

        self.run_mode.set_device_reference(self)
        self.clean_mode.set_device_reference(self)
        self.operational_state.set_device_reference(self)

    def set_run_mode_idle(self) -> None:
        current_mode = self.run_mode.attributes.get("CurrentMode")
        if isinstance(current_mode, int) and self.run_mode.is_idle_mode(current_mode):
            return

        supported_modes = self.run_mode.attributes.get("SupportedModes")
        if not isinstance(supported_modes, list):
            return

        for mode_entry in supported_modes:
            if not isinstance(mode_entry, dict):
                continue
            mode_value = mode_entry.get("Mode")
            if not isinstance(mode_value, int):
                continue

            tags = mode_entry.get("ModeTags")
            if not isinstance(tags, list):
                continue

            if int(ModeTag.IDLE) in [int(tag) for tag in tags if isinstance(tag, int)]:
                self.run_mode.attributes["CurrentMode"] = mode_value
                return

    def on_run_mode_changed(self, old_mode: int, new_mode: int) -> None:
        _ = old_mode
        if self.run_mode.is_idle_mode(new_mode):
            current_state = self.operational_state.attributes.get("OperationalState")
            if current_state in (int(OperationalState.RUNNING), int(OperationalState.PAUSED)):
                self.operational_state.begin_seek_charger()
            else:
                self.operational_state.stop_operation()
            return

        if self.run_mode.mode_has_tag(new_mode, ModeTag.MAPPING):
            self.operational_state.start_operation("Mapping")
        else:
            self.operational_state.start_operation("Cleaning")

    def on_clean_mode_changed(self, old_mode: int | None, new_mode: int) -> None:
        _ = (old_mode, new_mode)

    def on_time_tick(self) -> None:
        self.operational_state.on_time_tick(tick_interval=self.tick_interval)
