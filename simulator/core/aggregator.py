class Aggregator:
    @staticmethod
    def update_room(room, tick_duration=0.1):
        # 1. Initialize Deltas (Rate of change per second)
        deltas = {"temperature": 0.0, "illuminance": 0.0, "humidity": 0.0, "air_quality": 0.0}
        
        # 2. Sum influence of all ACTIVE devices
        for device in room.devices:
            if device.is_on:
                # Example: AC reduces temp and humidity
                # These coefficients come from the paper's Appendix P
                for var, impact in device.impact_factors.items():
                    deltas[var] += impact * device.intensity_multiplier

        # 3. Apply changes to room state (scaled by tick duration)
        for var in room.state:
            room.state[var] += deltas[var] * tick_duration

