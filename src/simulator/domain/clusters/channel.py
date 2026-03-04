from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, List
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


class ChannelType(IntEnum):
    SATELLITE = 0
    CABLE = 1
    TERRESTRIAL = 2
    OTT = 3


class LineupInfoType(IntEnum):
    

    MSO = 0


class StatusEnum(IntEnum):
    

    SUCCESS = 0
    MULTIPLE_MATCHES = 1
    NO_MATCHES = 2


@dataclass
class LineupInfoStruct:
    OperatorName: str
    LineupName: str
    PostalCode: str
    LineupInfoType: LineupInfoType


@dataclass
class Channel:
    MajorNumber: int
    MinorNumber: int
    Name: str
    CallSign: str
    AffiliateCallSign: str
    Identifier: str
    Type: ChannelType


class ChannelCluster(Cluster):
    

    def __init__(self, default_channels: List[Channel]):
        super().__init__(cluster_id="Channel")

        self.attributes = {
            "ChannelList": default_channels,
            "Lineup": LineupInfoStruct(
                OperatorName="Comcast",
                LineupName="Comcast King County",
                PostalCode="98052",
                LineupInfoType=LineupInfoType.MSO,
            ),
            "CurrentChannel": default_channels[0],
        }


        self.readonly_attributes = {"ChannelList", "Lineup"}


        self._previous_channel = None

        self.commands = {
            "ChangeChannel": self._change_channel,
            "ChangeChannelByNumber": self._change_channel_by_number,
            "SkipChannel": self._skip_channel,
        }

    def _change_channel(self, match: str) -> Result:
        

        if not isinstance(match, str):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for ChangeChannel command",
                f"Expected 'match' parameter as string, got {type(match).__name__}. "
                f'Usage: ChangeChannel(match="channel_name_or_number")',
            )

        if not match.strip():
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                "Empty channel identifier provided",
                "The 'match' parameter cannot be empty. Provide a channel name, number, or identifier.",
            )

        try:
            channel_list: List[Channel] = self.attributes.get("ChannelList", [])
            if not channel_list:
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR, "No channels available"
                )

            match_lower = match.lower().strip()

            priority_fields = [
                "Identifier",
                "AffiliateCallSign",
                "CallSign",
                "Name",
                "Number",
            ]
            matches: Dict[str, List[Channel]] = {field: [] for field in priority_fields}

            for channel in channel_list:
                channel_number = f"{channel.MajorNumber}.{channel.MinorNumber}"

                field_values = {
                    "Identifier": channel.Identifier,
                    "AffiliateCallSign": channel.AffiliateCallSign,
                    "CallSign": channel.CallSign,
                    "Name": channel.Name,
                    "Number": channel_number,
                }

                for field in priority_fields:
                    if field_values[field].lower() == match_lower:
                        matches[field].append(channel)

            for field in priority_fields:
                found_channels = matches[field]
                if len(found_channels) > 1:
                    response_data = {
                        "Status": StatusEnum.MULTIPLE_MATCHES,
                        "Data": found_channels,
                    }
                    return Result.fail(
                        ErrorCode.COMMAND_EXECUTION_ERROR,
                        "Multiple matches found",
                        str(response_data),
                    )

                if len(found_channels) == 1:
                    target_channel = found_channels[0]

                    self._previous_channel = self.attributes.get("CurrentChannel")
                    self.attributes["CurrentChannel"] = target_channel
                    response_data = {
                        "Status": StatusEnum.SUCCESS,
                        "Data": f"Changed to {target_channel.Name} (Channel {target_channel.MajorNumber}.{target_channel.MinorNumber})",
                    }
                    return Result.ok(response_data)

            response_data = {
                "Status": StatusEnum.NO_MATCHES,
                "Data": f"No channel found matching '{match}'",
            }
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                "No matches found",
                str(response_data),
            )

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to change channel", str(e)
            )

    def _change_channel_by_number(
        self, major_number: int, minor_number: int = 0
    ) -> Result:
        

        if not isinstance(major_number, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for ChangeChannelByNumber command",
                f"Expected 'major_number' as int, got {type(major_number).__name__}. "
                f"Usage: ChangeChannelByNumber(major_number=13, minor_number=1)",
            )

        if not isinstance(minor_number, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for ChangeChannelByNumber command",
                f"Expected 'minor_number' as int, got {type(minor_number).__name__}. "
                f"Usage: ChangeChannelByNumber(major_number=13, minor_number=1)",
            )

        if major_number < 0 or minor_number < 0:
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                "Invalid channel number",
                f"Channel numbers must be non-negative. Got major={major_number}, minor={minor_number}",
            )

        try:
            channel_list: List[Channel] = self.attributes.get("ChannelList", [])
            target_channel = None
            for channel in channel_list:
                if (
                    channel.MajorNumber == major_number
                    and channel.MinorNumber == minor_number
                ):
                    target_channel = channel
                    break

            if target_channel is None:
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR,
                    f"Channel {major_number}.{minor_number} not found",
                )


            self._previous_channel = self.attributes.get("CurrentChannel")
            self.attributes["CurrentChannel"] = target_channel
            return Result.ok(
                f"Changed to channel {major_number}.{minor_number} ({target_channel.Name})"
            )

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to change channel", str(e)
            )

    def _skip_channel(self, count: int = 1) -> Result:
        

        if not isinstance(count, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for SkipChannel command",
                f"Expected 'count' as int, got {type(count).__name__}. "
                f"Usage: SkipChannel(count=1) for next channel or SkipChannel(count=-1) for previous",
            )

        try:
            channel_list = self.attributes.get("ChannelList", [])
            current_channel = self.attributes.get("CurrentChannel")

            if not channel_list:
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR, "No channels available"
                )

            if current_channel is None:
                self.attributes["CurrentChannel"] = channel_list[0]
                return Result.ok(f"Set to first channel: {channel_list[0].Name}")

            current_index = -1
            for i, channel in enumerate(channel_list):
                if channel.Identifier == current_channel.Identifier:
                    current_index = i
                    break

            if current_index == -1:
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR,
                    "Current channel not found in list",
                )

            new_index = (current_index + count) % len(channel_list)
            new_channel = channel_list[new_index]


            self._previous_channel = self.attributes.get("CurrentChannel")
            self.attributes["CurrentChannel"] = new_channel
            return Result.ok(f"Skipped to channel: {new_channel.Name}")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to skip channel", str(e)
            )

    def __str__(self):
        
        current_channel = self.attributes.get("CurrentChannel")
        channel_name = current_channel.Name if current_channel else "None"
        channel_count = len(self.attributes.get("ChannelList", []))

        return (
            f"ChannelCluster("
            f"CurrentChannel={channel_name}, "
            f"ChannelCount={channel_count}, "
            f"Lineup={self.attributes.get('Lineup', 'Unknown')})"
        )
