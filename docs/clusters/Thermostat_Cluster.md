
# 4.3 Thermostat Cluster

This cluster provides an interface to the functionality of a thermostat.
Optional temperature,
humidity and occupancy
sensors
Dehumidification
notification
Heating / cooling Heating / cooling device
control panel (e.g. indoor air handler)
Thermostat
Dehumidification
C S S
Thermostat
C S S C
Fan control
user interface
configuration
Thermostat
C S C
notification configuration
Configuration
tool
C S
= Client = Server
Note: Device names are examples for illustration purposes only
Figure 15. Example Usage of the Thermostat and Related Clusters"

## Units of Temperature
Temperatures within this cluster are represented by types using units of degree Celsius.
The temperature data type used throughout this cluster is defined in the Derived Data Types section
of the Data Model.
The following temperature-related data types are also defined in and used throughout this cluster:
• TemperatureDifference
• SignedTemperature
• UnsignedTemperature
While temperature values MUST be transferred over the air using these types, this does not limit
how Thermostats may display or store temperature values. Thermostats which display temperature
values SHOULD follow the recommendations in Conversion of Temperature Values for Display.
Calculations with temperature attributes
Where calculations or comparisons are performed, attribute values must be
CAUTION
converted to a common type. In many cases, it is not sufficient to simply use the
integer representation as the scaling from °C to integer value differs.

## Setpoint Limits
There are a number of attributes which impose limits on setpoint values. This imposes constraints
which MUST be maintained by any mechanism which modifies a limit or setpoint. Individual
attribute descriptions detail the actions to be taken should a conflict arise while modifying the
value.
User configurable limits must be within device limits:
<= <= <=
• AbsMinHeatSetpointLimit   MinHeatSetpointLimit   MaxHeatSetpointLimit   AbsMaxHeat
SetpointLimit
<= <= <=
• AbsMinCoolSetpointLimit   MinCoolSetpointLimit   MaxCoolSetpointLimit   AbsMaxCoolSet
pointLimit
Setpoints must be within user configurable limits:
<= <=
• MinHeatSetpointLimit   OccupiedHeatingSetpoint   MaxHeatSetpointLimit
<= <=
• MinCoolSetpointLimit   OccupiedCoolingSetpoint   MaxCoolSetpointLimit
<= <=
• MinHeatSetpointLimit   UnoccupiedHeatingSetpoint   MaxHeatSetpointLimit
<= <=
• MinCoolSetpointLimit   UnoccupiedCoolingSetpoint   MaxCoolSetpointLimit
If, and only if, the AUTO feature is supported, a deadband must be maintained between Heating
and Cooling setpoints and limits:
<=
• AbsMinHeatSetpointLimit   (AbsMinCoolSetpointLimit - MinSetpointDeadBand)
<=
• AbsMaxHeatSetpointLimit   (AbsMaxCoolSetpointLimit - MinSetpointDeadBand)
<=
• MinHeatSetpointLimit   (MinCoolSetpointLimit - MinSetpointDeadBand)
<=
• MaxHeatSetpointLimit   (MaxCoolSetpointLimit - MinSetpointDeadBand)
<=
• OccupiedHeatingSetpoint   (OccupiedCoolingSetpoint - MinSetpointDeadBand)
<=
• UnoccupiedHeatingSetpoint   (UnoccupiedCoolingSetpoint - MinSetpointDeadBand)

## Dependencies
If the Alarms server cluster is supported on the same endpoint then the Alarms functionality is
enabled and the AlarmMask attribute SHALL be supported.
For remote temperature sensing, the Temperature Measurement client cluster MAY be included on
the same endpoint.
For occupancy sensing, the Occupancy Sensing client cluster MAY be included on the same end
point.

## Data Types
4.3.8.1. TemperatureDifference Type
This data type is derived from int16 and represents a temperature difference with a resolution of
0.01°C.
• value = (temperature in °C) x 100
• -4°C ⇒ -400
• 123.45°C ⇒ 12345
The full (non-null) range of -327.67°C to 327.67°C may be used.
4.3.8.2. SignedTemperature Type
This data type is derived from int8 and represents a temperature from -12.7°C to 12.7°C with a reso
lution of 0.1°C.
• value = (temperature in °C) x 10
• -4°C ⇒ -40
• 12.3°C ⇒ 123
This type is employed where compactness of representation is important and where the resolution
and range are still satisfactory.
4.3.8.3. UnsignedTemperature Type
This data type is derived from uint8 and represents a temperature from 0°C to 25.5°C with a resolu
tion of 0.1°C.
• value = (temperature in °C) x 10
• 4°C ⇒ 40
• 12.3°C ⇒ 123
This type is employed where compactness of representation is important and where the resolution
and range are still satisfactory.
4.3.8.4. ACErrorCodeBitmap Type
This data type is derived from map32.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a data element named "CompressorFail," which is associated with the bit '0'. This element indicates a "Compressor Failure or Refrigerant Leakage." According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that supports the Thermostat Cluster. There are no conditions or dependencies affecting its inclusion, underscoring its essential role in monitoring and reporting compressor-related issues within the thermostat system.

* In the Thermostat Cluster's Data Types section, the table entry describes a data element named "RoomSensorFail," which is represented by the bit '1'. This element indicates a "Room Temperature Sensor Failure." The conformance rule for this element is marked as 'M', meaning it is mandatory. This implies that the "RoomSensorFail" feature must always be implemented and supported in any device or system that conforms to the Matter specification for the Thermostat Cluster. There are no conditions or exceptions; it is a required component of the specification.

* In the Thermostat Cluster's Data Types section, the table row describes a data element named "OutdoorSensorFail," which is associated with bit 2. This element indicates a failure in the outdoor temperature sensor. The conformance rule for "OutdoorSensorFail" is marked as "M," which means it is a mandatory element. This implies that the "OutdoorSensorFail" feature must always be implemented and supported in any device or application utilizing the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster's Data Types, the table row describes a feature named "CoilSensorFail," which is represented by bit 3. This feature indicates an "Indoor Coil Temperature Sensor Failure." According to the conformance rule specified as "M," this feature is mandatory. This means that the "CoilSensorFail" element must always be implemented and supported in any device or application that adheres to the Matter specification for the Thermostat Cluster. There are no conditions or exceptions; it is a required component of the system.

* In the Thermostat Cluster, under the Data Types section, there is an entry for a data type named 'FanFail', which is represented by bit '4'. This data type indicates a 'Fan Failure' condition. The conformance rule for 'FanFail' is marked as 'M', which stands for Mandatory. This means that the 'FanFail' data type is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.8.5. AlarmCodeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a data element named "Initialization," which is associated with the bit value '0'. This element indicates an "Initialization failure," meaning the device did not successfully complete its initialization process during power-up. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Initialization" element is always required to be implemented in any device that supports the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster's Data Types, the table row describes a feature named "Hardware," which is associated with a bit value of '1' and summarizes a "Hardware failure." The conformance rule for this feature is marked as 'M,' indicating that it is Mandatory. This means that the "Hardware" feature must always be implemented and supported in any device or application that adheres to the Matter specification for the Thermostat Cluster. There are no conditions or exceptions; the presence of this feature is required without any dependencies or optionality.

* In the context of the Thermostat Cluster's Data Types, the table entry for 'SelfCalibration' with a bit value of '2' indicates a feature related to self-calibration failure. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'SelfCalibration' feature is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or exceptions; this feature must be included to ensure compliance with the standard.

4.3.8.6. HVACSystemTypeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, the entry for 'CoolingStage' represents a data type that indicates the stage of cooling being used by the HVAC system. The 'Bit' field specifies the bit range '1..0', which suggests that this data type is represented using two bits. The 'Conformance' field is marked as 'M', meaning that the 'CoolingStage' data type is mandatory. This implies that it is a required element within the Thermostat Cluster and must be implemented in any device or system that conforms to this specification. There are no conditions or exceptions; it is always required.

* In the Thermostat Cluster's Data Types section, the table row describes an element named "HeatingStage," which is represented by bits 3 and 2. This element indicates the stage of heating that the HVAC system is currently using. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that supports the Thermostat Cluster. There are no conditions or dependencies affecting its requirement; it must be present in all relevant implementations.

* In the Thermostat Cluster, under the Data Types section, the entry for 'HeatingIsHeatPump' with a bit value of '4' indicates whether the heating type is a Heat Pump. The conformance rule for this entry is 'M', which means that this element is mandatory. Therefore, the 'HeatingIsHeatPump' attribute must always be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions. This ensures that the capability to identify if the heating type is a Heat Pump is consistently available across all implementations of the Thermostat Cluster.

* The table row pertains to the Thermostat Cluster within the Data Types section, specifically focusing on a feature named "HeatingUsesFuel." This feature is represented by bit 5 and is summarized as indicating whether the HVAC system uses fuel. The conformance rule for this feature is marked as "M," which stands for Mandatory. This means that the "HeatingUsesFuel" feature is always required to be implemented in any device or system that conforms to the Matter specification for the Thermostat Cluster. There are no conditions or dependencies that alter this requirement; it is a fundamental and non-negotiable aspect of the specification.

4.3.8.6.1. CoolingStage Bits
These bits SHALL indicate what stage of cooling the HVAC system is using.
• 00 = Cool Stage 1
• 01 = Cool Stage 2
• 10 = Cool Stage 3
• 11 = Reserved
4.3.8.6.2. HeatingStage Bits
These bits SHALL indicate what stage of heating the HVAC system is using.
• 00 = Heat Stage 1
• 01 = Heat Stage 2
• 10 = Heat Stage 3
• 11 = Reserved
4.3.8.6.3. HeatingIsHeatPump Bit
This bit SHALL indicate whether the HVAC system is conventional or a heat pump.
• 0 = Conventional
• 1 = Heat Pump
4.3.8.6.4. HeatingUsesFuel Bit
This bit SHALL indicate whether the HVAC system uses fuel.
• 0 = Does not use fuel
• 1 = Uses fuel
4.3.8.7. OccupancyBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, the table row describes a data element named 'Occupied', which is associated with the bit '0'. This element serves to indicate the occupancy state. According to the conformance rule 'M', this element is classified as Mandatory. This means that the 'Occupied' data element is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.8.7.1. Occupied Bit
If this bit is set, it SHALL indicate the occupied state else if the bit if not set, it SHALL indicate the
unoccupied state.
4.3.8.8. PresetTypeFeaturesBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes a feature named "Automatic," which is associated with bit '0'. This feature indicates that a preset may be automatically activated by the thermostat. The conformance rule for this feature is marked as 'M', meaning it is Mandatory. This implies that the "Automatic" feature is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, the entry for 'SupportsNames' with a bit value of '1' indicates that this feature allows presets to support user-provided names. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'SupportsNames' feature is always required to be implemented in any device or system that conforms to the Matter specification for the Thermostat Cluster. There are no conditions or exceptions; it must be supported in all cases.

4.3.8.9. ProgrammingOperationModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a feature named "ScheduleActive," which is associated with bit '0'. This feature is summarized as enabling any programmed weekly schedule configurations, essentially indicating whether the thermostat is in schedule programming mode. The conformance rule for "ScheduleActive" is marked as 'M', which stands for Mandatory. This means that the "ScheduleActive" feature is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, the entry for 'AutoRecovery' with a bit value of '1' represents a feature related to the auto/recovery mode of the thermostat. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the 'AutoRecovery' feature is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting this requirement, making it an essential part of the cluster's functionality.

* In the Thermostat Cluster, under the Data Types section, the table row describes a feature named "Economy," which is associated with bit '2' and summarized as "Economy/EnergyStar mode." The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that the "Economy" feature is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.8.10. RelayStateBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, there is an entry for a data type with the bit value '0', named 'Heat', which is summarized as 'Heat Stage On'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Heat' data type must always be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, the table row entry for the 'Bit' labeled '1' is named 'Cool' and summarized as 'Cool Stage On'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Cool Stage On' feature is always required to be implemented in any device or application that supports the Thermostat Cluster. There are no conditions or exceptions; this feature must be included as part of the standard functionality.

* In the context of the Thermostat Cluster's Data Types, the table row describes a data element with the name "Fan" and a summary indicating "Fan Stage On," associated with bit position 2. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Fan" element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies that affect its requirement status; it must be included in all cases.

* In the Thermostat Cluster's Data Types section, the table row describes a data element named "HeatStage2," which corresponds to bit 3 and is summarized as "Heat 2nd Stage On." The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "HeatStage2" element is always required to be implemented in any device or system that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, the table row describes a data element named 'CoolStage2', which is represented by bit '4' and summarized as 'Cool 2nd Stage On'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'CoolStage2' element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement; it must be present in all cases.

* In the context of the Thermostat Cluster's Data Types, the table entry for 'Bit' 5, named 'FanStage2', represents a data element indicating that the second stage of the fan is on. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'FanStage2' element is always required to be implemented in any device or system that conforms to this part of the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental and non-negotiable aspect of the specification for the Thermostat Cluster.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data element named 'FanStage3', which is represented by bit 6. The summary indicates that this element signifies when the third stage of the fan is on. The conformance rule for 'FanStage3' is marked as 'M', meaning that this element is mandatory. This implies that the 'FanStage3' data element must always be implemented and supported in any device or application that conforms to this section of the Matter specification. There are no conditions or exceptions; its inclusion is required without any dependencies or optionality.

4.3.8.11. RemoteSensingBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data element named "LocalTemperature," which is represented by the bit '0'. This element refers to the calculated local temperature that is derived from a remote node. According to the conformance rule specified as 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Thermostat Cluster. There are no conditions or dependencies affecting its requirement; it must be present in all implementations.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the entry for 'OutdoorTemperature' at bit position '1' indicates that this data type represents the outdoor temperature, which is derived from a remote node. The 'Conformance' field is marked as 'desc', meaning that the conformance requirements for this element are too complex to be captured by a simple tag or expression. Instead, the specific conditions and rules governing its implementation are detailed elsewhere in the documentation. This suggests that understanding when and how 'OutdoorTemperature' should be implemented requires consulting additional descriptive information beyond the basic conformance tags and expressions.

* In the Thermostat Cluster's Data Types section, the table row describes a data element named "Occupancy," which is represented by bit '2'. The summary indicates that this element is used to derive occupancy information from a remote node. The conformance rule for this element is specified as "OCC." According to the Matter Conformance Interpretation Guide, this means that the "Occupancy" element is mandatory if the feature code "OCC" is supported by the device. If the device does not support the "OCC" feature, the conformance rule does not apply, and the element is not required.

4.3.8.11.1. OutdoorTemperature Bit
This bit SHALL be supported if the OutdoorTemperature attribute is supported.
4.3.8.12. ScheduleTypeFeaturesBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, within the Data Types section, the entry for 'SupportsPresets' at bit position '0' indicates a feature that allows the thermostat to support presets. The conformance rule '[PRES].b+' specifies that this feature is optional if the condition 'PRES' is true. The use of brackets around 'PRES' indicates that the feature is not mandatory but becomes optional when the 'PRES' condition is met. The '.b+' suffix suggests that this condition is related to a bitfield, implying that the presence of this feature depends on a specific bit being set within a broader context of conditions related to 'PRES'.

* In the Thermostat Cluster's Data Types section, the entry for 'SupportsSetpoints' with a bit value of '1' indicates a feature related to the thermostat's ability to support setpoints. The 'Conformance' field is marked as 'O.b+', which suggests that this feature is Optional. The notation 'O.b+' typically indicates that the feature is optional and may have additional conditions or notes described elsewhere in the documentation. In essence, while the 'SupportsSetpoints' feature is not required by default, there may be further details or conditions that could influence its implementation, which are documented beyond the basic conformance tag.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named "SupportsNames," which is associated with bit 2 and summarized as supporting user-provided names. The conformance rule for this element is marked as "O," indicating that it is optional. This means that the inclusion of the "SupportsNames" feature is not required and does not depend on any other features or conditions. Devices implementing the Thermostat Cluster can choose to support this feature, but they are not obligated to do so according to the Matter specification.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a feature named 'SupportsOff', which is associated with bit '3'. This feature indicates whether the thermostat supports transitioning to the 'SystemModeOff' state. According to the conformance rule 'O', the 'SupportsOff' feature is optional. This means that while it is not required for the implementation of the Thermostat Cluster, it can be included at the discretion of the developer or manufacturer without any dependencies or conditions.

4.3.8.12.1. SupportsPresets Bit
This bit SHALL indicate that any ScheduleStruct with a SystemMode field whose value matches the
SystemMode field on the encompassing ScheduleTypeStruct supports specifying presets on Sched
uleTransitionStructs contained in its Transitions field.
4.3.8.12.2. SupportsSetpoints Bit
This bit SHALL indicate that any ScheduleStruct with a SystemMode field whose value matches the
SystemMode field on the encompassing ScheduleTypeStruct supports specifying setpoints on Sched
uleTransitionStructs contained in its Transitions field.
4.3.8.12.3. SupportsNames Bit
This bit SHALL indicate that any ScheduleStruct with a SystemMode field whose value matches the
SystemMode field on the encompassing ScheduleTypeStruct supports setting the value of the Name
field.
4.3.8.12.4. SupportsOff Bit
This bit SHALL indicate that any ScheduleStruct with a SystemMode field whose value matches the
SystemMode field on the encompassing ScheduleTypeStruct supports setting its SystemMode field
to Off.
4.3.8.13. ScheduleDayOfWeekBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row entry describes a data element named "Sunday," which is represented by the bit '0'. The summary also identifies it as "Sunday." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Sunday" data element is always required to be implemented in any device or system that conforms to this part of the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental and non-negotiable part of the specification for the Thermostat Cluster.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named "Monday," which is represented by the bit value '1'. The summary also identifies this element as "Monday." According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Thermostat Cluster. There are no conditions or dependencies affecting this requirement, indicating that the presence of the "Monday" element is essential and non-negotiable within this specification.

* In the Thermostat Cluster's Data Types section, the table row describes an element named "Tuesday," which is represented by the bit value '2'. The summary simply reiterates the name as "Tuesday." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Tuesday" element is always required to be implemented in any device or application that uses the Thermostat Cluster according to the Matter specification. There are no conditions or exceptions; it must be included in all cases.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data element named "Wednesday" associated with bit 3. The summary also labels it as "Wednesday." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Wednesday" element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status; it must be included in all cases.

* In the context of the Thermostat Cluster, under the Data Types section, the table row describes an element named "Thursday," which is associated with bit 4. The summary simply reiterates the name as "Thursday." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Thursday" element is always required to be implemented in any device or application that supports this part of the Thermostat Cluster specification. There are no conditions or exceptions; it must be included as specified.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data element named "Friday," associated with bit 5. The summary also identifies it as "Friday." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Friday" data element is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named "Saturday," which is represented by the bit value '6'. The summary also labels it as "Saturday." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Saturday" element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or exceptions; it must be included in all relevant implementations.

* In the Thermostat Cluster, under the Data Types section, there is an entry for a data type named 'Away', which is represented by bit '7'. This data type is summarized as 'Away or Vacation', indicating its purpose is to denote when the thermostat is set to an 'Away' or 'Vacation' mode. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Away' data type is a required element in the Thermostat Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

4.3.8.14. ScheduleModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, within the Data Types section, the table row describes a feature called 'HeatSetpointPresent', which is associated with the bit '0'. This feature is summarized as 'Adjust Heat Setpoint'. According to the conformance rule 'M', this element is mandatory, meaning that it is always required to be implemented in any device or application that supports the Thermostat Cluster. There are no conditions or dependencies affecting its requirement; it must be present in all cases.

* In the Thermostat Cluster, under the Data Types section, the table row describes an element named "CoolSetpointPresent" with a bit value of '1'. This element is summarized as "Adjust Cool Setpoint," indicating its role in managing the cooling setpoint of a thermostat. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "CoolSetpointPresent" element is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.8.15. ACCapacityFormatEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes a data type named "BTUh," which stands for "British Thermal Unit per Hour" and is represented by the value '0'. The conformance rule for this data type is 'O', indicating that it is optional. This means that the inclusion of the BTUh data type in a device's implementation is not required and does not depend on any other features or conditions. Devices can choose to support this data type, but it is not mandatory for compliance with the Matter specification in this context.

4.3.8.16. ACCompressorTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes an entry with the value '0', named 'Unknown', which summarizes an 'Unknown compressor type'. The conformance rule for this entry is 'O', indicating that this element is optional. This means that the inclusion of this data type is not required and there are no dependencies or conditions that mandate its presence. Devices implementing the Thermostat Cluster can choose to support this 'Unknown' compressor type, but they are not obligated to do so according to the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the name 'T1', which has a value of '1' and a summary indicating that it represents a maximum working ambient temperature of 43 °C. The conformance rule for this entry is 'O', which means that this element is optional. It is not required for implementation and has no dependencies on other features or conditions. This allows implementers the flexibility to include or exclude this data type based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the name 'T2', which represents a data type with a value of '2' and a summary indicating it pertains to a maximum working ambient temperature of 35 °C. The conformance rule for this entry is 'O', which means that this data type is optional. It is not required for implementation and has no dependencies on other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this data type based on their specific needs or preferences.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named 'T3', which has a value of '3' and represents the maximum working ambient temperature of 52 °C. The conformance rule for this element is 'O', indicating that it is optional. This means that the inclusion of the 'T3' element is not required and does not depend on any other features or conditions within the Matter specification. Devices implementing the Thermostat Cluster can choose to support this element, but they are not obligated to do so.

4.3.8.17. ACLouverPositionEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes an entry with the 'Name' "Closed" and a 'Value' of "1", which is summarized as "Fully Closed". The 'Conformance' for this entry is marked as "O", indicating that the "Closed" data type is optional. This means that while it is not required for implementation, it can be included without any dependencies or conditions. Devices or systems implementing the Thermostat Cluster may choose to support this data type, but they are not obligated to do so according to the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '2', named 'Open', which has a summary of 'Fully Open'. The conformance rule for this entry is 'O', indicating that it is optional. This means that the 'Open' data type is not required to be implemented in devices or systems that support the Thermostat Cluster. There are no dependencies or conditions that affect its optional status, so it can be included or omitted at the discretion of the implementer without affecting compliance with the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '3', named 'Quarter', which is summarized as 'Quarter Open'. The conformance rule for this entry is 'O', indicating that the 'Quarter' data type is optional. This means that while it is not required for implementation, it can be included without any dependencies or conditions. Implementers have the discretion to support this data type based on their specific needs or preferences, but it is not mandated by the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with a 'Value' of '4', named 'Half', which is summarized as 'Half Open'. The 'Conformance' field for this entry is marked as 'O', indicating that this element is Optional. This means that the 'Half' data type is not required for implementation and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this element in their designs without affecting compliance with the Matter specification.

* In the context of the Thermostat Cluster's Data Types, the table row describes an entry with the value '5', named 'ThreeQuarters', which summarizes as 'Three Quarters Open'. The conformance rule for this entry is 'O', indicating that the 'ThreeQuarters' data type is optional. This means that while it is not required for implementation, it can be included at the discretion of the developer, and there are no dependencies or conditions that must be met for its inclusion.

4.3.8.18. ACRefrigerantTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '0', named 'Unknown', which summarizes an 'Unknown Refrigerant Type'. The conformance rule for this entry is 'O', indicating that this element is optional. This means that the inclusion of this 'Unknown Refrigerant Type' data type is not required and does not depend on any other features or conditions. It can be implemented at the discretion of the developer or manufacturer, but it is not a mandatory component of the Matter specification for thermostats.

* In the context of the Thermostat Cluster's Data Types, the table row describes an entry with the value '1', named 'R22', which represents the 'R22 Refrigerant'. The conformance rule for this entry is 'O', indicating that the inclusion of this element is Optional. This means that the R22 Refrigerant data type is not required for implementation and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this element based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data element with the value '2', named 'R410a', which refers to the 'R410a Refrigerant'. The conformance rule for this element is marked as 'O', indicating that it is optional. This means that the inclusion of the 'R410a Refrigerant' data type is not required for compliance with the Matter specification, and there are no dependencies or conditions that affect its optional status. Implementers have the discretion to include or exclude this element based on their specific needs or preferences without impacting conformance.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '3', named 'R407c', which refers to the R407c Refrigerant. The conformance rule for this entry is 'O', indicating that the inclusion of the R407c Refrigerant data type is optional. This means that while it is available for use within the Thermostat Cluster, it is not required and does not depend on any other features or conditions to be implemented.

4.3.8.19. ACTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes an entry with the value '0', named 'Unknown', which summarizes as 'Unknown AC Type'. The conformance rule for this entry is 'O', indicating that this element is optional. This means that the inclusion of this data type, representing an unknown air conditioning type, is not required and has no dependencies on other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this element based on their specific needs or preferences.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named "CoolingFixed" with a value of '1' and a summary of "Cooling and Fixed Speed." The conformance rule for this element is 'O,' which stands for Optional. This means that the "CoolingFixed" element is not required to be implemented in devices that support the Thermostat Cluster. There are no dependencies or conditions that affect its optional status, allowing manufacturers the flexibility to include or exclude this feature based on their design preferences or product requirements.

* In the Thermostat Cluster, under the Data Types section, the entry for 'HeatPumpFixed' with a value of '2' and a summary of 'Heat Pump and Fixed Speed' is described. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'HeatPumpFixed' data type is not required to be implemented in devices supporting the Thermostat Cluster. It can be included at the discretion of the device manufacturer, as there are no dependencies or conditions mandating its inclusion.

* In the context of the Thermostat Cluster's Data Types, the table row entry describes a feature named "CoolingInverter," which is summarized as "Cooling and Inverter" and assigned the value '3'. The conformance rule for this feature is marked as 'O', indicating that the "CoolingInverter" feature is optional. This means that while the feature can be implemented, it is not required and has no dependencies on other features or conditions within the Matter specification. Implementers have the flexibility to include or exclude this feature based on their specific product requirements or design preferences.

* In the context of the Thermostat Cluster's Data Types, the table entry for 'HeatPumpInverter' with a value of '4' and a summary of 'Heat Pump and Inverter' indicates that this specific data type pertains to the functionality of heat pumps and inverters within a thermostat system. The conformance rule for this entry is marked as 'O', which means that the 'HeatPumpInverter' data type is optional. This implies that while it can be included in the implementation of a thermostat system, it is not a required element and does not depend on any other features or conditions to be considered optional.

4.3.8.20. SetpointRaiseLowerModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Thermostat Cluster, specifically in the Data Types section. The entry is for a data type with the value '0', named 'Heat', which is used to adjust the heat setpoint. The conformance rule 'HEAT' indicates that this element is mandatory if the feature 'HEAT' is supported by the device. In other words, if a device supports the 'HEAT' feature, it must include this data type to adjust the heat setpoint. If the 'HEAT' feature is not supported, the inclusion of this data type is not required.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, the table row describes a feature named "Cool" with a value of '1', which is associated with adjusting the Cool Setpoint. The conformance rule 'COOL' indicates that this feature is mandatory if the COOL feature is supported by the device. This means that if the device includes support for the COOL feature, the "Cool" data type must be implemented as part of its functionality. If the COOL feature is not supported, the conformance rule does not apply, and the "Cool" data type is not required.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '2', named 'Both', which summarizes the capability to adjust both the Heat Setpoint and Cool Setpoint. The conformance rule 'HEAT | COOL' indicates that this feature is mandatory if either the HEAT or COOL feature is supported by the device. In other words, if a thermostat supports either heating or cooling functionality, it must also support the ability to adjust both the heat and cool setpoints. This ensures that devices with either heating or cooling capabilities can manage both temperature settings effectively.

4.3.8.21. ControlSequenceOfOperationEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the entry for 'CoolingOnly' with a value of '0' indicates a mode where heating and emergency functions are not possible. The conformance rule '[COOL]' specifies that this element is optional if the 'COOL' feature is supported. This means that if the device or system includes the 'COOL' feature, the 'CoolingOnly' mode can be implemented, but it is not required. If the 'COOL' feature is not supported, this mode is not applicable.

* In the context of the Thermostat Cluster's Data Types, the entry for 'CoolingWithReheat' with a value of '1' indicates a specific operational mode where heating and emergency functions are not possible. The conformance rule '[COOL]' specifies that the 'CoolingWithReheat' feature is optional and can be implemented if the 'COOL' feature is supported. This means that if the device or system includes the 'COOL' feature, it has the option to support 'CoolingWithReheat', but it is not required to do so.

* In the Thermostat Cluster's Data Types section, the entry for 'HeatingOnly' with a value of '2' indicates a mode where only heating is possible, and cooling or precooling functions are not available. The conformance rule '[HEAT]' specifies that the 'HeatingOnly' mode is optional if the feature 'HEAT' is supported. This means that if a device or implementation supports the 'HEAT' feature, it may choose to include the 'HeatingOnly' mode, but it is not required to do so.

* In the Thermostat Cluster's Data Types section, the entry for 'HeatingWithReheat' with a value of '3' indicates a mode where cooling and precooling are not possible. The conformance rule '[HEAT]' specifies that this element is optional if the 'HEAT' feature is supported. This means that if a device supports the 'HEAT' feature, it may include the 'HeatingWithReheat' mode, but it is not required to do so. If the 'HEAT' feature is not supported, this mode is not applicable.

* In the Thermostat Cluster's Data Types section, the entry for 'CoolingAndHeating' with a value of '4' indicates that this mode allows for all possible heating and cooling operations. The conformance rule '[HEAT & COOL]' specifies that the 'CoolingAndHeating' mode is optional if both the HEAT and COOL features are supported. This means that if a device supports both heating and cooling functionalities, it may include this mode, but it is not required to do so.

* In the Thermostat Cluster's Data Types section, the entry for 'CoolingAndHeatingWithReheat' with a value of '5' and a summary stating 'All modes are possible' describes a specific operational mode for a thermostat. The conformance rule '[HEAT & COOL]' indicates that this mode is optional if both the HEAT and COOL features are supported. This means that the 'CoolingAndHeatingWithReheat' mode can be included in the thermostat's functionality when both heating and cooling capabilities are present, but it is not required.

CoolingAndHeating
A thermostat indicating it supports CoolingAndHeating (or CoolingAndHeatingWith
Reheat) SHOULD be able to request heating or cooling on demand and will usually
support the Auto SystemMode.
NOTE
Systems  which  support  cooling  or  heating,  requiring  external  intervention  to
change modes or where the whole building must be in the same mode, SHOULD
report CoolingOnly or HeatingOnly based on the current capability.
4.3.8.22. PresetScenarioEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, there is an entry with the name "Occupied," which has a value of '1'. This entry indicates that the area controlled by the thermostat is occupied. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Occupied" data type is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, the entry with the name "Unoccupied" and a value of "2" signifies that the thermostat-controlled area is unoccupied. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "Unoccupied" data type is a required element in the specification and must always be implemented in any device or system that conforms to the Matter specification for the Thermostat Cluster. There are no conditions or exceptions to this requirement, making it an essential part of the thermostat's functionality.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a data type with the value '3', named 'Sleep', which indicates a state where users are likely to be sleeping. The conformance rule for this entry is 'M', meaning that this data type is mandatory. It must always be implemented in any device or system that supports the Thermostat Cluster, without any conditions or exceptions. This ensures that the 'Sleep' state is consistently available across all compliant devices, facilitating standardized behavior and interoperability.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data type with the value '4', named 'Wake', which summarizes a state where users are likely to be waking up. The conformance rule for this entry is 'M', meaning that this data type is mandatory. This implies that any implementation of the Thermostat Cluster must include this 'Wake' data type, as it is a required element without any conditions or exceptions.

* In the Thermostat Cluster, under the Data Types section, there is an entry with the value '5' named 'Vacation', which indicates that users are on vacation. The conformance rule for this entry is 'M', meaning that the 'Vacation' data type is mandatory. This implies that it is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster's Data Types section, the table row entry describes a data type with the value '6' and the name 'GoingToSleep', which indicates a state where users are likely preparing to go to sleep. The conformance rule for this entry is 'M', meaning that this data type is mandatory. It must be implemented and supported in all devices or applications that conform to the Matter specification for this cluster, without any conditions or exceptions.

* In the Thermostat Cluster's Data Types section, the table row describes a data type with the value '254' named 'UserDefined', which pertains to custom presets. The conformance rule for this entry is 'M', indicating that the 'UserDefined' data type is mandatory. This means that any implementation of the Thermostat Cluster must include support for this data type, as it is a required element without any conditions or exceptions.

4.3.8.22.1. Undefined Value
This value SHALL have no specified scenario.
4.3.8.22.2. Occupied Value
This value SHALL indicate the preset for periods when the thermostat’s temperature-controlled
area is occupied. It is intended for thermostats that can automatically determine occupancy.
4.3.8.22.3. Unoccupied Value
This value SHALL indicate the preset for periods when the thermostat’s temperature-controlled
area is unoccupied. It is intended for thermostats that can automatically determine occupancy.
4.3.8.22.4. Sleep Value
This value SHALL indicate the preset for periods when users are likely to be asleep.
4.3.8.22.5. Wake Value
This value SHALL indicate the preset for periods when users are likely to be waking up.
4.3.8.22.6. Vacation Value
This value SHALL indicate the preset for periods when users are on vacation, or otherwise out-of-
home for extended periods of time.
4.3.8.22.7. GoingToSleep Value
This value SHALL indicate the preset for periods when users are likely to be going to sleep.
4.3.8.22.8. UserDefined Value
This value SHALL indicate a free-form preset; when set, the Name field on PresetStruct SHALL NOT
be null.
4.3.8.23. SetpointChangeSourceEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the entry describes a data type with the value '0' named 'Manual', which refers to a user-initiated setpoint change via the thermostat. The conformance rule for this entry is 'O', indicating that the 'Manual' feature is optional. This means that while the feature is available for implementation, it is not required and does not depend on any other conditions or features being supported. Implementers have the discretion to include or exclude this feature in their devices without affecting compliance with the Matter specification.

* In the Thermostat Cluster, under the Data Types section, the entry for 'Schedule' with a value of '1' refers to a setpoint change initiated by a schedule or internal programming. The conformance rule '[SCH | MSCH]' indicates that the 'Schedule' feature is optional if either the 'SCH' or 'MSCH' feature is supported. This means that the presence of the 'Schedule' feature is not mandatory but can be included if the device supports either of these features, providing flexibility in implementation based on the device's capabilities.

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the value '2', named 'External'. This entry represents an externally-initiated setpoint change, such as those triggered by a Demand Response and Load Control (DRLC) cluster command or an attribute write. The conformance rule for this entry is 'O', indicating that it is optional. This means that the implementation of this feature is not required and does not depend on any other conditions or features. Devices implementing the Thermostat Cluster may choose to support this feature, but it is not mandatory for compliance with the Matter specification.

4.3.8.24. StartOfWeekEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row entry specifies a data type with the value '0' and the name 'Sunday'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the element 'Sunday' with the value '0' is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or exceptions to this requirement; it must be included in all relevant implementations.

* In the Thermostat Cluster's Data Types section, the table row entry describes a data element named "Monday" with a value of '1'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Monday" data element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement; it must be present in all cases.

* In the context of the Thermostat Cluster's Data Types, the table row entry specifies a data type with the value '2' and the name 'Tuesday'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the element 'Tuesday' is always required to be implemented within the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement; it must be included in all implementations of this cluster.

* In the context of the Thermostat Cluster's Data Types, the table entry specifies a data type with the value '3' and the name 'Wednesday'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the element 'Wednesday' is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement status; it must be included without exception.

* In the context of the Thermostat Cluster's Data Types, the table row specifies an entry with the value '4' and the name 'Thursday'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the element 'Thursday' with the value '4' is a required component of the Thermostat Cluster's Data Types and must be implemented in all devices or systems that conform to this specification. There are no conditions or dependencies affecting this requirement; it is an absolute necessity within the given context.

* In the context of the Thermostat Cluster's Data Types, the table row entry specifies a data type with the value '5' and the name 'Friday'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the data type 'Friday' is a required element within the Thermostat Cluster and must always be implemented according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the cluster's data types.

* In the context of the Thermostat Cluster's Data Types, the table row entry specifies a data type with the value '6' and the name 'Saturday'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the element 'Saturday' is a required component of the Thermostat Cluster's Data Types and must be implemented in any device or application that conforms to this specification. There are no conditions or dependencies affecting its mandatory status, indicating that it is a fundamental and non-negotiable part of the specification.

4.3.8.25. SystemModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a data type with the value '0' and the name 'Off'. This indicates that the thermostat is not generating demand for either cooling or heating. The conformance rule for this entry is 'O', which means that this feature is optional. It is not required for implementation and does not have any dependencies on other features or conditions. This allows manufacturers the flexibility to include or exclude this feature based on their specific product design or market needs.

* In the context of the Thermostat Cluster's Data Types, the table row describes a feature with the name "Auto," which has a value of '1'. This feature automatically generates demand for either cooling or heating as needed. The conformance rule for this feature is specified as "AUTO." According to the Matter Conformance Interpretation Guide, "AUTO" is not a standard conformance tag or expression, suggesting that its conformance is likely described elsewhere in the documentation. This means that the specific conditions under which the "Auto" feature is required, optional, or otherwise specified are detailed in another section, and it is essential to refer to that documentation for a complete understanding of its implementation requirements.

* In the Thermostat Cluster, under the Data Types section, the entry with the value '3' and name 'Cool' indicates that this data type is associated with generating demand specifically for cooling purposes. The conformance rule '[COOL]' signifies that this element is optional and should be included if the 'COOL' feature is supported. If the 'COOL' feature is not supported, this element is not required. This allows for flexibility in implementation, ensuring that the 'Cool' data type is only present when relevant to the device's capabilities.

* In the context of the Thermostat Cluster's Data Types, the table row entry describes a feature named "Heat" with a value of '4'. This feature indicates that demand is generated solely for heating purposes. The conformance rule for this entry is specified as '[HEAT]', which means that the "Heat" feature is optional if the condition 'HEAT' is true. In other words, the feature is not required by default, but it becomes available for implementation if the HEAT feature is supported within the device or system.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the entry for 'EmergencyHeat' with a value of '5' indicates that the second stage of heating is being used to achieve the desired temperature. The conformance rule '[HEAT]' specifies that the 'EmergencyHeat' feature is optional and should be implemented only if the 'HEAT' feature is supported by the device. This means that if the device supports the 'HEAT' feature, it may include the 'EmergencyHeat' functionality, but it is not required to do so.

* In the Thermostat Cluster's Data Types section, the entry for 'Precooling' with a value of '6' is described with the summary '(see Terms)'. The conformance rule '[COOL]' indicates that the 'Precooling' feature is optional and should be included if the 'COOL' feature is supported. This means that if the thermostat device supports the 'COOL' feature, it may also support the 'Precooling' feature, but it is not mandatory to do so. If the 'COOL' feature is not supported, the 'Precooling' feature is not required.

* In the context of the Thermostat Cluster, specifically within the Data Types section, the table entry describes a data type with the name 'FanOnly' and a value of '7'. The conformance rule for 'FanOnly' is marked as 'O', which stands for Optional. This means that the 'FanOnly' data type is not a required element within the Thermostat Cluster specification. It can be implemented at the discretion of the developer or manufacturer, as there are no dependencies or conditions that mandate its inclusion.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a feature named "Dry" with a value of '8'. The conformance rule for this feature is marked as 'O', which stands for Optional. This means that the "Dry" feature is not required for implementation in devices that support the Thermostat Cluster. There are no dependencies or conditions that need to be met for this feature to be included; it is entirely at the discretion of the implementer whether to support this feature or not.

* In the context of the Thermostat Cluster's Data Types, the table entry describes a data type named "Sleep" with a value of '9'. The conformance rule for this entry is 'O', which stands for Optional. This means that the "Sleep" data type is not required to be implemented in devices that support the Thermostat Cluster. There are no dependencies or conditions that affect its optional status, allowing manufacturers the flexibility to include or exclude this data type based on their specific design choices or product requirements.

Table 9. Interpretation of Heat, Cool and Auto SystemModeEnum Values

_Table parsed from section 'Data Types':_

* This table row pertains to the Thermostat Cluster within the context of Data Types, specifically focusing on the attribute values related to temperature settings. The entry describes three scenarios: when the temperature is below the heat setpoint, between the heat and cool setpoints, and above the cool setpoint. Each scenario is associated with a specific status: "Temperature below target" for when it's below the heat setpoint, and "Temperature on target" for the other two scenarios. The conformance rule for this entry is not explicitly provided in the row data, but based on the context, it likely involves conditions under which these attribute values are required or optional. If a conformance string were provided, it would dictate whether these attributes are mandatory, optional, provisional, deprecated, or disallowed, potentially influenced by specific features or conditions related to the thermostat's operation.

* The table row pertains to the Thermostat Cluster within the Data Types section, focusing on attribute values related to temperature settings. Specifically, it describes the conditions under which certain temperature states are recognized: "Cool" when the temperature is below the heat setpoint, "Temperature on target" when the temperature is between the heat and cool setpoints, and "Temperature above target" when the temperature is above the cool setpoint. The conformance rule for this entry is not explicitly provided in the row data, but if we were to interpret a typical conformance scenario using the guide, it might involve conditions under which these temperature states are mandatory or optional based on the presence of specific features or configurations within the thermostat's implementation. Without a specific conformance string, we assume these attributes are standard for interpreting temperature states in a thermostat's operation.

* The table row describes a data type within the Thermostat Cluster, specifically focusing on attribute values related to temperature settings. The attributes include 'Auto', 'Temperature Below Heat Setpoint', 'Temperature Between Heat Setpoint and Cool Setpoint', and 'Temperature Above Cool Setpoint', each representing different temperature conditions relative to the thermostat's setpoints. The conformance rule for this entry is not explicitly provided in the row data, but if it were, it would dictate when these attributes are required or optional based on the presence or absence of certain features or conditions, as outlined in the Matter Conformance Interpretation Guide. For instance, if a conformance rule were given as `AB, O`, it would mean that the attribute is mandatory if feature `AB` is supported; otherwise, it is optional. Without a specific conformance rule, we assume these attributes are described in the broader context of the specification, potentially with complex conditions or dependencies.

4.3.8.26. ThermostatRunningModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes a data entry with the value '0' and the name 'Off'. This entry signifies that the thermostat is not generating a demand for either cooling or heating, as summarized by its description. The conformance rule for this entry is marked as 'O', which means it is optional. This indicates that the 'Off' state is not a required feature for devices implementing the Thermostat Cluster; it can be included at the discretion of the device manufacturer without any dependencies or conditions.

* In the Thermostat Cluster's Data Types section, the table row describes a data type with the value '3', named 'Cool', which indicates that demand is generated solely for cooling purposes. The conformance rule '[COOL]' means that this element is optional if the feature 'COOL' is supported. In other words, the 'Cool' data type is not required by default, but it can be included if the device or system supports the cooling feature.

* In the Thermostat Cluster's Data Types section, the table row describes a feature named "Heat," which is identified by the value '4' and summarized as "Demand is only generated for Heating." The conformance rule for this feature is '[HEAT]', indicating that the "Heat" feature is optional and can be included if the condition 'HEAT' is true, meaning if the device or implementation supports the 'HEAT' feature. If 'HEAT' is not supported, the inclusion of this feature is not required.

4.3.8.27. TemperatureSetpointHoldEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster, under the Data Types section, the entry for 'SetpointHoldOff' with a value of '0' and a summary of 'Follow scheduling program' is described. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'SetpointHoldOff' element is always required to be implemented in any device or application that supports the Thermostat Cluster. There are no conditions or exceptions; it must be included to ensure compliance with the Matter specification.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the entry for 'SetpointHoldOn' with a value of '1' is described as a feature that maintains the current setpoint, regardless of any schedule transitions. The conformance rule for this entry is 'M', which means that the 'SetpointHoldOn' feature is mandatory. This implies that any implementation of the Thermostat Cluster must include this feature, as it is always required according to the Matter specification.

4.3.8.28. PresetStruct Type

_Table parsed from section 'Data Types':_

* The table row entry describes an element within the Thermostat Cluster's Data Types section, specifically the 'PresetHandle'. This element is identified by the ID '0' and is of the type 'octstr', with a constraint that limits its maximum length to 16 characters. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is marked as 'M', which means that the 'PresetHandle' is a mandatory element within the Thermostat Cluster. This implies that it is always required to be implemented according to the Matter specification, without any conditional dependencies or exceptions.

* The table row describes an element within the Thermostat Cluster, specifically under the Data Types section. The element is identified by the ID '1' and is named 'PresetScenario'. It is of the type 'PresetScenarioEnum' and has a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'PresetScenario' element is always required to be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

* In the Thermostat Cluster's Data Types section, the table row describes an element with the ID '2', named 'Name', which is of the type 'string' and has a constraint of a maximum length of 64 characters. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The default value for this element is 'null'. The 'Conformance' field is marked as 'O', meaning that the inclusion of this 'Name' element is optional and not required, with no dependencies or conditions affecting its optional status.

* The table row describes an entry for the 'CoolingSetpoint' within the Thermostat Cluster's Data Types section. This entry is identified by the ID '3' and is of the 'temperature' type, with a default value set at 26°C. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' field is specified as 'COOL', which means that the 'CoolingSetpoint' is mandatory if the feature 'COOL' is supported. In other words, if the device or implementation includes the 'COOL' feature, the 'CoolingSetpoint' must be included as part of the configuration.

* The table row describes an attribute named "HeatingSetpoint" within the Thermostat Cluster's Data Types section. This attribute is of the "temperature" type, with a default value set to 20°C. The "Constraint" field is marked as "desc," indicating that the constraints for this attribute are detailed elsewhere in the documentation. The "Conformance" field is specified as "HEAT," meaning that the HeatingSetpoint attribute is mandatory if the feature or condition identified by "HEAT" is supported. In other words, if the thermostat device supports the "HEAT" feature, then it must include the HeatingSetpoint attribute.

* The table row describes an element within the Thermostat Cluster, specifically in the Data Types section. The element is identified by the ID '5' and is named 'BuiltIn'. It is of the boolean type ('bool') and applies universally ('Constraint': 'all'). The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in certain contexts, although the specifics are not detailed here. The default value for this element is 'false'. The 'Conformance' field is marked as 'M', which means that the 'BuiltIn' element is mandatory and must always be included in implementations of the Thermostat Cluster according to the Matter specification.

4.3.8.28.1. PresetHandle Field
This field SHALL indicate a device generated identifier for this preset. It SHALL be unique on the
device, and SHALL NOT be reused after the associated preset has been deleted.
This field SHALL only be null when the encompassing PresetStruct is appended to the Presets
attribute for the purpose of creating a new Preset. Refer to Presets for the creation of Preset han
dles.
4.3.8.28.2. PresetScenario Field
This field SHALL indicate the associated PresetScenarioEnum value for this preset.
4.3.8.28.3. Name Field
This field SHALL indicate a name provided by a user. The null value SHALL indicate no name.
Within each subset of presets sharing the same PresetScenario field value, there SHALL NOT be any
presets with the same value, including null as a value, in the Name field.
4.3.8.28.4. CoolingSetpoint Field
This field SHALL indicate the cooling setpoint for the preset. Refer to Setpoint Limits for value con
straints.
4.3.8.28.5. HeatingSetpoint Field
This field SHALL indicate the heating setpoint for the preset. Refer to Setpoint Limits for value con
straints.
4.3.8.28.6. BuiltIn Field
This field SHALL indicate whether the preset is marked as "built-in", meaning that it can be modi
fied, but it cannot be deleted.
4.3.8.29. PresetTypeStruct Type

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table entry for 'PresetScenario' with ID '0' and type 'PresetScenarioEnum' indicates a specific data type used within this cluster. The 'Constraint' being 'all' suggests that this data type applies universally within the cluster. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'PresetScenario' data type is a required element for any implementation of the Thermostat Cluster, without any conditions or exceptions. It must be supported and implemented in all cases where the Thermostat Cluster is used.

* In the Thermostat Cluster, under the Data Types section, the entry for 'NumberOfPresets' is identified by the ID '1' and is of type 'uint8', which means it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that this data type applies universally within its context. The default value for 'NumberOfPresets' is '0'. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'NumberOfPresets' attribute is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster's Data Types section, the table row with ID '2' refers to an element named 'PresetTypeFeatures', which is of the type 'PresetTypeFeaturesBitmap'. This element has a constraint labeled 'all', a default value of '0', and a conformance designation of 'M'. According to the Matter Conformance Interpretation Guide, the 'M' conformance tag indicates that 'PresetTypeFeatures' is a mandatory element. This means it is always required to be implemented in any device or application utilizing the Thermostat Cluster, without any conditions or exceptions.

4.3.8.29.1. PresetScenario Field
This field SHALL specify a PresetScenarioEnum value supported by this thermostat.
4.3.8.29.2. NumberOfPresets Field
This field SHALL specify a limit for the number of presets for this PresetScenarioEnum.
4.3.8.29.3. PresetTypeFeatures Field
This field SHALL specify a bitmap of features for this PresetTypeStruct.
4.3.8.30. WeeklyScheduleTransitionStruct Type
This represents a single transition in a Thermostat schedule

_Table parsed from section 'Data Types':_

* In the context of the Thermostat Cluster's Data Types, the table row describes an element named "TransitionTime" with an ID of '0'. This element is of type 'uint16', which is an unsigned 16-bit integer, and it has a constraint that limits its maximum value to 1439. The conformance rule for "TransitionTime" is marked as 'M', which means it is a Mandatory element. This indicates that the "TransitionTime" must always be implemented and supported within the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster's Data Types, the table row describes an element with the ID '1' named 'HeatSetpoint', which is of the 'temperature' type and has a constraint labeled as 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', meaning that the 'HeatSetpoint' element is mandatory. This implies that within the Thermostat Cluster, the 'HeatSetpoint' must always be implemented and supported, without any conditions or exceptions.

* The table row describes an element within the Thermostat Cluster, specifically a data type named "CoolSetpoint," which is of the type "temperature" and has a constraint labeled as "all." The "Quality" field is marked as "X," indicating that this element is explicitly disallowed in terms of quality. The "Conformance" field is marked with an "M," meaning that the "CoolSetpoint" is a mandatory element within the Thermostat Cluster. This implies that any implementation of the Thermostat Cluster must include the "CoolSetpoint" data type as a required component, without any conditional exceptions or dependencies.

4.3.8.30.1. TransitionTime Field
This field SHALL represent the start time of the schedule transition during the associated day. The
time will be represented by a 16 bits unsigned integer to designate the minutes since midnight. For
example, 6am will be represented by 360 minutes since midnight and 11:30pm will be represented
by 1410 minutes since midnight.
4.3.8.30.2. HeatSetpoint Field
This field SHALL represent the heat setpoint to be applied at this associated transition start time.
4.3.8.30.3. CoolSetpoint Field
This field SHALL represent the cool setpoint to be applied at this associated transition start time.
4.3.8.31. ScheduleStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an element within the Thermostat Cluster's Data Types section, specifically the 'ScheduleHandle'. This element is identified by the ID '0' and is of the type 'octstr', with a constraint that limits its maximum length to 16. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', which means that the 'ScheduleHandle' is a mandatory element within the Thermostat Cluster. This implies that it is always required to be implemented according to the Matter specification, regardless of any other conditions or features.

* The table row describes an entry within the Thermostat Cluster's Data Types section, specifically for the 'SystemMode' attribute. This attribute is identified by the ID '1' and is of the type 'SystemModeEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', which means that the 'SystemMode' attribute is mandatory. It is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster's Data Types, the table entry describes an attribute with the ID '2', named 'Name', which is of the type 'string' and has a constraint limiting it to a maximum length of 64 characters. The conformance rule for this attribute is marked as 'O', indicating that it is optional. This means that the inclusion of the 'Name' attribute is not required and there are no dependencies or conditions that mandate its presence in the implementation of the Thermostat Cluster. Implementers have the flexibility to include or exclude this attribute based on their specific needs or preferences.

* In the Thermostat Cluster's Data Types section, the table row describes an element with the ID '3' named 'PresetHandle'. This element is of type 'octstr', which is an octet string, and it has a constraint that limits its maximum length to 16 characters. The conformance rule for 'PresetHandle' is marked as 'O', indicating that it is an optional element. This means that the inclusion of 'PresetHandle' is not required and it does not depend on any other features or conditions within the Matter specification. Devices implementing the Thermostat Cluster can choose to support this element, but they are not obligated to do so.

* In the Thermostat Cluster's Data Types section, the table row describes an element with the ID '4' named 'Transitions'. This element is of the type 'list[ScheduleTransitionStruct]', which means it is a list composed of structures defined by the ScheduleTransitionStruct type. The constraint specifies that the list must contain between 1 and the value of 'NumberOfScheduleTransitions' entries. The default state of this list is 'empty', indicating that initially, it contains no entries. The conformance rule for 'Transitions' is marked as 'M', meaning this element is mandatory and must always be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an element with the ID '5', named 'BuiltIn', which is of the boolean type ('bool') and has a constraint of 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The default value for 'BuiltIn' is 'false'. The 'Conformance' is marked as 'M', which means that the 'BuiltIn' element is mandatory and must always be included in implementations of the Thermostat Cluster, without any conditions or exceptions.

4.3.8.31.1. ScheduleHandle Field
This field SHALL indicate a device generated identifier for this schedule. It SHALL be unique on the
device, and SHALL NOT be reused after the associated schedule has been deleted.
This field SHALL only be null when the encompassing ScheduleStruct is appended to the Schedules
attribute for the purpose of creating a new Schedule. Refer to Schedules for the creation of Sched
ule handles.
4.3.8.31.2. SystemMode Field
This field SHALL specify the default thermostat system mode for transitions in this schedule. The
only valid values for this field SHALL be Auto, Heat, and Cool.
4.3.8.31.3. Name Field
This field SHALL specify a name for the ScheduleStruct.
4.3.8.31.4. PresetHandle Field
This field SHALL indicate the default PresetHandle value for transitions in this schedule.
4.3.8.31.5. Transitions Field
This field SHALL specify a list of transitions for the schedule.
This field SHALL NOT contain more than one ScheduleStruct with the same TransitionTime field
and overlapping DayOfWeek fields; i.e. there SHALL be no duplicate transitions.
If the NumberOfScheduleTransitionsPerDay attribute is not null, then for each bit in ScheduleDay
OfWeekBitmap, the number of transitions with that bit set in DayOfWeek SHALL NOT be greater
than the value of the NumberOfScheduleTransitionsPerDay attribute.
For the purposes of determining which ScheduleStruct in this list is currently active, the current
time SHALL be the number of minutes past midnight in the display value of the current time, not
the actual number of minutes that have elapsed since midnight. On days which transition into or
out of daylight saving time, certain values may repeat or not occur during the transition period.
A ScheduleTransitionStruct in this list SHALL be active if the current day of the week matches its
DayOfWeek field and the current time is greater than or equal to the TransitionTime, but less than
the TransitionTime on any other ScheduleTransitionStruct in the Transitions field whose Day
OfWeek field also matches the current day of the week.
If the current time is less than every ScheduleTransitionStruct whose DayOfWeek field also matches
the current day of the week, the server SHALL attempt the same process to identify the active
ScheduleTransitionStruct for the day preceding the previously attempted day of the week, repeat
ing until an active ScheduleTransitionStruct is found or the attempted day is the current day of the
week again. If no active ScheduleTransitionStruct is found, then the active ScheduleTransition
Struct SHALL be the ScheduleTransitionStruct with the largest TransitionTime field from the set of
ScheduleTransitionStructs whose DayOfWeek field matches the current day of the week.
4.3.8.31.6. BuiltIn Field
This field SHALL indicate whether the schedule is marked as "built-in", meaning that it can be mod
ified, but it cannot be deleted.
4.3.8.32. ScheduleTransitionStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Thermostat Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'DayOfWeek'. It utilizes the data type 'ScheduleDayOfWeekBitmap', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'DayOfWeek' element is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Thermostat Cluster's Data Types section, the table row describes an entry with the ID '1', named 'TransitionTime', which is of type 'uint16' and has a constraint of a maximum value of 1439. The conformance rule for 'TransitionTime' is 'M', which stands for Mandatory. This means that the 'TransitionTime' data type is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster's Data Types section, the table row describes an element named 'PresetHandle' with an ID of '2'. This element is of type 'octstr' (octet string) and is constrained to a maximum length of 16. The conformance rule '[PRES]' indicates that the 'PresetHandle' is an optional element that becomes applicable if the 'PRES' feature is supported. If the 'PRES' feature is not supported, the 'PresetHandle' remains optional and does not need to be implemented.

* In the Thermostat Cluster, under the Data Types section, the table row describes an element with the ID '3' named 'SystemMode', which is of the type 'SystemModeEnum'. The 'Constraint' for this element is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' for 'SystemMode' is labeled as 'O', meaning that this element is optional. This implies that the 'SystemMode' element is not required for implementation and does not have any dependencies or conditions that would make it mandatory.

* In the Thermostat Cluster's Data Types section, the table entry for 'CoolingSetpoint' with ID '4' is defined as a 'temperature' type with constraints described elsewhere in the documentation. The conformance rule '[COOL]' indicates that the 'CoolingSetpoint' attribute is optional, but only if the 'COOL' feature is supported. This means that if the thermostat device supports the 'COOL' feature, it may include the 'CoolingSetpoint' attribute, but it is not required to do so. If the 'COOL' feature is not supported, the attribute is not applicable.

* In the Thermostat Cluster's Data Types section, the table row describes an element with the ID '5' named 'HeatingSetpoint', which is of the 'temperature' type. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' field is specified as '[HEAT]', meaning that the 'HeatingSetpoint' element is optional and should be included if the 'HEAT' feature is supported. If the 'HEAT' feature is not supported, the inclusion of this element is not required.

This struct provides a time of day and a set of days of the week for a state transition within a sched
ule. The thermostat SHALL use the following order of precedence for determining a new setpoint at
the time of transition:
1. If the PresetHandle field is provided, then the setpoint for the PresetStruct in the Presets
attribute with that identifier SHALL be used
2. If either the HeatingSetpoint or CoolingSetpoint is provided, then it SHALL be used
a. If the SystemMode field is provided, the HeatingSetpoint and CoolingSetpoint fields SHALL
be interpreted using the SystemMode field
b. If the SystemMode field is not provided, the HeatingSetpoint and CoolingSetpoint fields
SHALL be interpreted using the SystemMode field on the parent ScheduleStruct
3. If neither the PresetHandle field or any Setpoint field is provided, then the PresetHandle field
on the parent ScheduleStruct SHALL be used to determine the active PresetStruct
4. If the PresetHandle is not indicated and no setpoint is provided for the current SystemMode, the
server SHALL use a default value for the current SystemMode.
If the setpoint was derived from a preset, then the ActivePresetHandle SHALL be set to the Pre
setHandle of that preset.
If a CoolingSetpoint was used to determine the cooling setpoint:
• If the server supports the OCC feature, and the Occupied bit is not set on the Occupancy
attribute, then the UnoccupiedCoolingSetpoint attribute SHALL be set to the CoolingSetpoint
• Otherwise, the OccupiedCoolingSetpoint attribute SHALL be set to the CoolingSetpoint
If a HeatingSetpoint was used to determine the heating setpoint:
• If the server supports the OCC feature, and the Occupied bit is not set on the Occupancy
attribute, then the UnoccupiedHeatingSetpoint attribute SHALL be set to the HeatingSetpoint
• Otherwise, the OccupiedHeatingSetpoint attribute SHALL be set to the HeatingSetpoint
The ScheduleTransitionStruct SHALL be invalid if all the following are true:
• The HeatingSetpoint field is not provided
• The PresetHandle field is not provided
• The PresetHandle field on the encompassing ScheduleStruct is not provided
• The SystemMode field is provided and has the value Heat or Auto, or the SystemMode field on
the parent ScheduleStruct has the value Heat or Auto
The ScheduleTransitionStruct SHALL be invalid if all the following are true:
• The CoolingSetpoint field is not provided
• The PresetHandle field is not provided
• The PresetHandle field on the encompassing ScheduleStruct is not provided
• The SystemMode field is provided and has the value Cool or Auto, or the SystemMode field on
the parent ScheduleStruct has the value Cool or Auto
4.3.8.32.1. DayOfWeek Field
This field SHALL specify a bitmask of days of the week that the transition applies to. The Vacation
bit SHALL NOT be set; vacation schedules SHALL be set via the vacation preset.
4.3.8.32.2. TransitionTime Field
This SHALL specify the time of day at which the transition becomes active, in terms of minutes
within the day representing the wall clock, where 0 is 00:00:00, 1 is 00:01:00 and 1439 is 23:59:00.
Handling of transitions during the changeover of Daylight Saving Time is implementation-depen
dent.
4.3.8.32.3. PresetHandle Field
This field SHALL specify the preset used at the TransitionTime. If this field is provided, then the Sys
temMode, CoolingSetpoint and HeatingSetpoint fields SHALL NOT be provided.
4.3.8.32.4. SystemMode Field
This SHALL specify the default mode to which the thermostat will switch for this transition, over
riding the default for the schedule. The only valid values for this field SHALL be Auto, Heat, Cool
and Off. This field SHALL only be included when the required system mode differs from the sched
ule’s default SystemMode.
4.3.8.32.5. CoolingSetpoint Field
This field SHALL specify the cooling setpoint for the transition. If PresetHandle is set, this field
SHALL NOT be included. Refer to Setpoint Limits for value constraints.
4.3.8.32.6. HeatingSetpoint Field
This field SHALL specify the cooling setpoint for the transition. If PresetHandle is set, this field
SHALL NOT be included. Refer to Setpoint Limits for value constraints.
4.3.8.33. ScheduleTypeStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Thermostat Cluster, specifically under the Data Types section. The entry is for an attribute named "SystemMode," which is of the type "SystemModeEnum." The constraint for this attribute is described elsewhere in the documentation, as indicated by "desc." The conformance rule for "SystemMode" is marked as "M," which means that this attribute is mandatory. It must always be implemented in any device or application that supports the Thermostat Cluster according to the Matter specification.

* In the Thermostat Cluster's Data Types section, the table row describes an attribute named "NumberOfSchedules" with an ID of '1'. This attribute is of type 'uint8', indicating it is an 8-bit unsigned integer, and it is constrained by the maximum number of schedules that can be set. The default value for this attribute is '0'. The conformance rule for "NumberOfSchedules" is 'M', which means it is mandatory. This implies that the attribute must always be implemented and supported in any device or application that conforms to the Matter specification for the Thermostat Cluster.

* The table row describes an entry within the Thermostat Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'ScheduleTypeFeatures'. It is of the type 'ScheduleTypeFeaturesBitmap', which suggests it is a bitmap data type used to represent various scheduling features. The 'Constraint' is marked as 'desc', indicating that the constraints for this data type are detailed elsewhere in the documentation. The default value for this entry is '0'. The conformance rule for 'ScheduleTypeFeatures' is marked as 'M', meaning that this element is mandatory. It must always be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.8.33.1. SystemMode Field
This field SHALL specify a SystemModeEnum supported by this thermostat for Schedules. The only
valid values for this field SHALL be Auto, Heat, and Cool.
4.3.8.33.2. NumberOfSchedules Field
This field SHALL specify a limit for the number of Schedules for this SystemMode.
4.3.8.33.3. ScheduleTypeFeatures Field
This field SHALL specify a bitmap of features for this schedule entry. At least one of SupportsPresets
and SupportsSetpoints SHALL be set.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Thermostat Cluster, specifically the 'LocalTemperature' attribute. This attribute is identified by the ID '0x0000' and is of the 'temperature' type. It applies to all instances of the cluster, as indicated by the 'Constraint' field. The 'Quality' field suggests that while the attribute is disallowed ('X') and provisional ('P') in some contexts, this does not affect its conformance requirement here. The 'Default' value is 'null', meaning it does not have a predefined default value. The 'Access' field indicates that the attribute is readable ('R') and volatile ('V'), meaning its value can change frequently. The 'Conformance' field is marked as 'M', which means that the 'LocalTemperature' attribute is mandatory and must always be implemented in any device that supports the Thermostat Cluster.

* In the Thermostat Cluster, within the Attributes section, the 'OutdoorTemperature' attribute is identified by the ID '0x0001' and is of the 'temperature' type. This attribute is constrained to be applicable in all contexts ('Constraint': 'all') and is marked with a quality of 'X', indicating it is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access permissions ('Access': 'R V'). The conformance rule for 'OutdoorTemperature' is 'O', meaning that its inclusion is optional and not required by the Matter specification, with no dependencies or conditions affecting its optional status.

* In the Thermostat Cluster, under the Attributes section, the entry for 'Occupancy' with ID '0x0002' is of type 'OccupancyBitmap' and has a default value of '1'. It is constrained to 'all', meaning it applies universally within its context. The access level is 'R V', indicating that it is readable and has a volatile nature, possibly changing over time. The conformance rule 'OCC' specifies that the 'Occupancy' attribute is mandatory if the feature 'OCC' is supported. This means that if the Thermostat Cluster supports the 'OCC' feature, the 'Occupancy' attribute must be implemented; otherwise, its implementation is not required.

_Table parsed from section 'Attributes':_

* In the Thermostat Cluster, the attribute 'AbsMinHeatSetpointLimit' with ID '0x0003' is a temperature type attribute that defines the absolute minimum limit for the heating setpoint. The constraint for this attribute is described elsewhere in the documentation, and it has a default value of 7°C. The attribute is read-only and volatile, as indicated by the 'R V' access specification. The conformance rule '[HEAT]' means that this attribute is optional and should be implemented only if the HEAT feature is supported by the device. If the HEAT feature is not supported, the attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "AbsMaxHeatSetpointLimit" with an ID of '0x0004'. This attribute is of the 'temperature' type and has a default value of 30°C. It is subject to constraints that are described elsewhere in the documentation, indicated by 'desc'. The quality is marked as 'F', and it has read and view access ('R V'). The conformance rule '[HEAT]' means that this attribute is optional and only required if the 'HEAT' feature is supported by the device. If the 'HEAT' feature is not supported, the attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'AbsMinCoolSetpointLimit', which is identified by the ID '0x0005'. This attribute is of the 'temperature' type and has a default value of 16°C. It is constrained in a manner that is described elsewhere in the documentation ('desc'), and it is of 'F' quality, indicating a specific characteristic or requirement defined in the broader specification. The attribute has 'R V' access, meaning it can be read and is volatile. The conformance rule '[COOL]' indicates that this attribute is optional and only required if the 'COOL' feature is supported by the device. If the 'COOL' feature is not supported, this attribute is not required.

* In the Thermostat Cluster, within the Attributes section, the attribute 'AbsMaxCoolSetpointLimit' is identified by the ID '0x0006' and is of the 'temperature' type. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. It has a default value of 32°C and is accessible for reading and verification, as denoted by 'R V'. The conformance rule '[COOL]' indicates that this attribute is optional if the 'COOL' feature is supported. This means that if the thermostat device supports the 'COOL' feature, the 'AbsMaxCoolSetpointLimit' attribute may be included but is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "PICoolingDemand" attribute. This attribute has an ID of '0x0007' and is of type 'uint8', with a constraint that its value must range from 0% to 100%. The 'Quality' is marked as 'P', indicating that its status is provisional and may change in the future. The default value is unspecified ('-'), and it has read and view access ('R V'). The conformance rule '[COOL]' means that the "PICoolingDemand" attribute is optional and only required if the 'COOL' feature is supported by the device. If the 'COOL' feature is not supported, this attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "PIHeatingDemand" attribute, which is identified by the ID '0x0008'. This attribute is of type 'uint8' and is constrained to values between 0% and 100%. It has a quality status of 'Provisional', indicating that its current status is temporary and may change in the future. The default value is unspecified ('-'), and it has read and view access ('R V'). The conformance rule '[HEAT]' indicates that the "PIHeatingDemand" attribute is optional if the HEAT feature is supported. This means that if the HEAT feature is present in the device, the inclusion of this attribute is not mandatory but allowed.

* The table row describes an attribute within the Thermostat Cluster, specifically the "HVACSystemTypeConfiguration" attribute. This attribute has an ID of '0x0009' and is of the type 'HVACSystemTypeBitmap'. The 'Constraint' is described elsewhere in the documentation, indicated by 'desc', and it has a default value of '0'. The 'Access' field indicates that this attribute can be read ('R') and conditionally written ('[W]'), with VM suggesting it is a volatile memory attribute. The 'Quality' is marked as 'N', which typically means it is not a quality attribute. The 'Conformance' for this attribute is 'D', meaning it is deprecated in the current specification. This indicates that the attribute is considered obsolete and should not be used in new implementations, as it may be removed in future versions of the specification.

* The table row describes an attribute named "LocalTemperatureCalibration" within the Thermostat Cluster's Attributes section. This attribute has an ID of '0x0010' and is of the type 'SignedTemperature', with a constraint applicable to all instances. It has a default value of '0°C' and can be accessed with read and write permissions, specifically by the Verified Manufacturer (VM). The conformance rule '[!LTNE]' indicates that the "LocalTemperatureCalibration" attribute is optional if the feature 'LTNE' (Local Temperature Not Enabled) is not supported. In other words, if the device does not support the 'LTNE' feature, this attribute may be included but is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "OccupiedCoolingSetpoint" attribute. This attribute is identified by the ID '0x0011' and is of the 'temperature' type. The 'Constraint' is described elsewhere in the documentation, indicating it may have complex conditions or limitations. The 'Quality' is marked as 'N', suggesting no specific quality requirements are noted. The default value for this attribute is set to '26°C', and it has 'RW VO' access, meaning it is Read/Write and Volatile. The 'Conformance' field is marked as 'COOL', which implies that this attribute is mandatory if the 'COOL' feature is supported by the device. If the 'COOL' feature is not supported, the attribute is not required. This ensures that devices with cooling capabilities must implement this attribute to define the cooling setpoint when the space is occupied.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'OccupiedHeatingSetpoint'. This attribute, identified by the ID '0x0012', is of the 'temperature' type and has a default value of 20°C. The 'Constraint' is marked as 'desc', indicating that its constraints are detailed elsewhere in the documentation. The 'Quality' is 'N', suggesting no specific quality requirements are noted. The 'Access' is 'RW VO', meaning it is readable and writable, with volatile access. The 'Conformance' field is 'HEAT', which implies that this attribute is mandatory if the 'HEAT' feature is supported by the device. If the device supports heating functionality, it must include the 'OccupiedHeatingSetpoint' attribute.

* The table row describes an attribute named "UnoccupiedCoolingSetpoint" within the Thermostat Cluster, identified by the ID '0x0013'. This attribute is of the 'temperature' type, with a default value of 26°C, and has a constraint that is described elsewhere in the documentation. It is marked with a quality of 'N', indicating it may have specific quality considerations, and it is accessible with read and write permissions, as well as volatile operations (RW VO). The conformance rule 'COOL & OCC' indicates that the "UnoccupiedCoolingSetpoint" attribute is mandatory if both the 'COOL' and 'OCC' features are supported by the device. If either or both of these features are not supported, the attribute is not required.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Thermostat Cluster, specifically the "UnoccupiedHeatingSetpoint" with an ID of '0x0014'. This attribute is of the 'temperature' type and has a default value of 20°C. It is constrained by a description provided elsewhere in the documentation and has a quality of 'N', meaning it is not a quality attribute. The access level is 'RW VO', indicating it is readable and writable, with value-only access. The conformance rule 'HEAT & OCC' specifies that this attribute is mandatory if both the 'HEAT' and 'OCC' features are supported by the device. If either or both of these features are not supported, the attribute is not required.

* In the Thermostat Cluster, within the Attributes section, the entry for 'MinHeatSetpointLimit' (ID: 0x0015) is of type 'temperature' and has a constraint described elsewhere in the documentation. This attribute is not of high quality ('N'), and its default value is set to 'AbsMinHeatSetpointLimit'. It has read-write access and can be modified by the manufacturer ('RW VM'). The conformance rule '[HEAT]' indicates that the 'MinHeatSetpointLimit' attribute is optional and should be included if the HEAT feature is supported by the device. If the HEAT feature is not supported, this attribute is not required.

* In the Thermostat Cluster, the attribute 'MaxHeatSetpointLimit' with ID '0x0016' is a temperature type attribute that defines the maximum limit for the heat setpoint. The constraint for this attribute is described elsewhere in the documentation, indicating a complex condition. Its default value is set to 'AbsMaxHeatSetpointLimit', and it has read-write access with a viewable and modifiable quality. The conformance rule '[HEAT]' indicates that this attribute is optional and only required if the 'HEAT' feature is supported by the device. If the 'HEAT' feature is not supported, this attribute is not required.

* In the Thermostat Cluster, under the Attributes section, the entry for 'MinCoolSetpointLimit' with ID '0x0017' is a temperature attribute that defines the minimum cooling setpoint limit. The constraint for this attribute is described elsewhere in the documentation, indicating complexity beyond a simple constraint. It has a default value of 'AbsMinCoolSetpointLimit' and can be read and written (RW) with additional access control marked by 'VM'. The conformance rule '[COOL]' indicates that this attribute is optional if the 'COOL' feature is supported. This means that the attribute does not have to be implemented unless the device supports the cooling feature, in which case it becomes an optional attribute.

* The table row describes an attribute within the Thermostat Cluster, specifically the "MaxCoolSetpointLimit," which is identified by the ID '0x0018' and is of the type 'temperature'. This attribute is constrained by a description that is detailed elsewhere in the documentation, indicated by 'desc'. The quality is marked as 'N', and its default value is set to 'AbsMaxCoolSetpointLimit'. It has read and write access, with the ability to be modified by a verified manufacturer, as denoted by 'RW VM'. The conformance rule '[COOL]' specifies that the "MaxCoolSetpointLimit" attribute is optional if the COOL feature is supported. This means that if the device or implementation includes the COOL feature, this attribute can be included but is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "MinSetpointDeadBand" attribute. This attribute has an ID of '0x0019' and is of the type 'SignedTemperature', constrained to values between 0 and 12.7°C, with a default value of 2.5°C. The 'Access' field indicates that it is readable ('R') and optionally writable ('[W]') with a viewable ('VM') access level. The 'Quality' is marked as 'N', which typically denotes a non-critical attribute. The 'Conformance' field is labeled as 'AUTO', which is not directly explained in the provided conformance interpretation guide. However, in the context of Matter specifications, 'AUTO' might imply that the conformance is automatically determined based on certain conditions or configurations not explicitly detailed in the table. Therefore, the inclusion or requirement of this attribute could depend on the automatic configuration of the device or system, which is not

* In the Thermostat Cluster, the attribute 'RemoteSensing' is identified by the ID '0x001A' and is of the type 'RemoteSensingBitmap'. This attribute has a constraint pattern of '00000xxx', indicating specific bits that can be set. It is marked with a quality of 'N', has a default value of '0', and can be accessed with read and write permissions, as well as via a virtual machine ('RW VM'). The conformance rule for 'RemoteSensing' is 'O', meaning that this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ControlSequenceOfOperation" attribute. This attribute has an ID of '0x001B' and is of the type 'ControlSequenceOfOperationEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'N', and it has a default value of '4'. The 'Access' is specified as 'RW VM', meaning it is readable and writable with view and modify permissions. The 'Conformance' is marked as 'M', which means this attribute is mandatory and must always be implemented in devices that support the Thermostat Cluster.

* The table row describes an attribute within the Thermostat Cluster, specifically the "SystemMode" attribute. This attribute is identified by the ID '0x001C' and is of the type 'SystemModeEnum'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is 'N', the default value is '1', and it has 'Read/Write' and 'Viewable/Modifiable' access permissions. The 'Conformance' field is marked with 'M', which means that the "SystemMode" attribute is mandatory and must always be implemented in any device supporting the Thermostat Cluster, without any conditions or dependencies.

* In the Thermostat Cluster's Attributes section, the entry for 'AlarmMask' with ID '0x001D' is of type 'AlarmCodeBitmap' and has a default value of '0'. The 'Access' field indicates that it is readable and volatile ('R V'). The 'Conformance' field is specified as '[Zigbee]', which means that the 'AlarmMask' attribute is optional if the Zigbee feature is supported. This implies that in implementations where Zigbee is a supported feature, the inclusion of the 'AlarmMask' attribute is not mandatory, but it can be included at the developer's discretion. The 'Constraint' is described elsewhere, indicating that its conditions or limitations are detailed in another part of the documentation.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ThermostatRunningMode" attribute. This attribute is of the type "ThermostatRunningModeEnum" and has a default value of '0'. It is constrained by a description that is detailed elsewhere in the documentation, as indicated by 'desc'. The access level for this attribute is 'R V', meaning it is readable and has a volatile nature, which implies it can change frequently. The conformance rule '[AUTO]' indicates that this attribute is optional if the feature 'AUTO' is supported. In other words, the inclusion of the "ThermostatRunningMode" attribute is not mandatory unless the 'AUTO' feature is present, in which case it becomes optional.

* The table row describes an attribute within the Thermostat Cluster, specifically the "StartOfWeek" attribute, identified by the ID '0x0020'. This attribute is of the type 'StartOfWeekEnum' and has constraints that are described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'F', and there is no default value specified. The access level is 'R V', meaning it can be read and verified. The conformance rule for this attribute is 'SCH', which, according to the Matter Conformance Interpretation Guide, suggests that the conformance is determined by a specific schedule or condition described elsewhere in the documentation. This implies that the requirement for this attribute depends on certain conditions or configurations not explicitly detailed in the table row.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Thermostat Cluster, specifically the "NumberOfWeeklyTransitions" attribute. This attribute has an ID of '0x0021' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The constraint is 'all', indicating it applies universally within its context. The quality is marked as 'F', and it has a default value of '0'. The access level is 'R V', which typically means it is readable and possibly volatile. The conformance for this attribute is listed as 'SCH', which does not directly match any of the basic conformance tags or logical conditions provided in the guide. Therefore, it likely refers to a more complex conformance condition described elsewhere in the documentation. This means the specific requirements for when this attribute is mandatory, optional, or otherwise are detailed in another section of the Matter specification.

* The table row describes an attribute within the Thermostat Cluster, specifically the "NumberOfDailyTransitions" attribute. This attribute has an ID of '0x0022' and is of type 'uint8', meaning it is an 8-bit unsigned integer. It is constrained to apply universally ('all'), has a default value of '0', and its access is read-only and viewable ('R V'). The quality is marked as 'F', indicating a specific quality level as defined in the broader specification. The conformance for this attribute is listed as 'SCH', which is not directly explained by the provided conformance interpretation guide. Therefore, 'SCH' likely refers to a specific condition or description detailed elsewhere in the Matter specification documentation, indicating that the conformance of this attribute is complex and requires additional context to fully understand its requirements.

* In the Thermostat Cluster, under the Attributes section, the entry for 'TemperatureSetpointHold' with ID '0x0023' is of type 'TemperatureSetpointHoldEnum'. The constraint for this attribute is described elsewhere in the documentation, indicated by 'desc'. It has a default value of '0' and is accessible for reading and writing, with the additional requirement of being verified by a manufacturer ('RW VM'). The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the 'TemperatureSetpointHold' attribute is not required for implementation and does not depend on any other features or conditions to be included in a device's functionality.

* The table row describes an attribute within the Thermostat Cluster, specifically the "TemperatureSetpointHoldDuration" attribute. This attribute has an ID of '0x0024' and is of type 'uint16', with a constraint that its maximum value is 1440. The quality of this attribute is marked as 'NX', indicating it is not executable. The default value for this attribute is 'null', and it has read-write access with a viewable and modifiable (VM) permission. The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the implementation of this attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ThermostatProgrammingOperationMode" identified by ID '0x0025'. This attribute is of the type "ProgrammingOperationModeBitmap" and has a default value of '0'. It is provisionally marked with a quality of 'P', indicating its status may change in the future. The access level is 'RW VM', meaning it can be read and written, and is subject to view management. The conformance rule for this attribute is 'O', which means it is optional and not required for implementation, with no dependencies on other features or conditions. The constraint is described elsewhere in the documentation, as indicated by 'desc'.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ThermostatRunningState" attribute, identified by the ID '0x0029'. This attribute is of the type 'RelayState Bitmap', with constraints described elsewhere in the documentation. It does not have a default value and has read and view access ('R V'). The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the inclusion of the "ThermostatRunningState" attribute is not required for devices implementing the Thermostat Cluster, and there are no dependencies or conditions affecting this optional status.

* The table row describes an attribute within the Thermostat Cluster, specifically the "SetpointChangeSource" attribute. This attribute has an ID of '0x0030' and is of the type 'SetpointChangeSourceEnum'. The constraint for this attribute is described elsewhere in the documentation, indicated by 'desc'. Its default value is '0', and it has read and view access, denoted by 'R V'. The conformance rule for this attribute is 'O', meaning it is optional. This implies that the implementation of the "SetpointChangeSource" attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Thermostat Cluster, specifically the "SetpointChangeAmount" attribute. This attribute is of the type "TemperatureDifference" and is constrained to apply universally ("all"). The quality of this attribute is marked as "X," indicating it is explicitly disallowed in some contexts. The default value is "null," and it has read and view access permissions ("R V"). The conformance rule for this attribute is "O," meaning it is optional. This indicates that the "SetpointChangeAmount" attribute is not required to be implemented in devices supporting the Thermostat Cluster, and there are no dependencies or conditions that would change this optional status.

* The table row describes an attribute within the Thermostat Cluster, specifically the "SetpointChangeSourceTimestamp" attribute. This attribute has an ID of '0x0032' and is of type 'utc', indicating it records a timestamp. The 'Constraint' is listed as 'all', meaning it applies universally within the cluster context. The default value for this attribute is '0', and it has 'R V' access, signifying it can be read and is volatile. The conformance rule for this attribute is 'O', which means it is optional. This indicates that the implementation of this attribute is not required and does not depend on any other features or conditions within the Matter specification.

_Table parsed from section 'Attributes':_

* In the Thermostat Cluster, the attribute 'OccupiedSetback' is identified by the ID '0x0034' and is of the type 'UnsignedTemperature'. It is constrained between 'OccupiedSetbackMin' and 'OccupiedSetbackMax', with no default value specified. The attribute has read-write access and is visible to the manufacturer. The conformance rule 'SB' indicates that this attribute is mandatory if the feature 'SB' is supported. If the feature 'SB' is not supported, the attribute is not required. This means that the presence of the 'OccupiedSetback' attribute depends on whether the 'SB' feature is implemented in the device.

* The table row describes an attribute named "OccupiedSetbackMin" within the Thermostat Cluster's Attributes section. This attribute is identified by the ID '0x0035' and is of the type 'UnsignedTemperature'. It has a constraint that it must not exceed the value of 'OccupiedSetbackMax'. The quality is marked as 'XF', indicating specific quality characteristics, and it has a default value of 'null'. The access level is 'R V', meaning it can be read and is volatile. The conformance rule 'SB' indicates that the 'OccupiedSetbackMin' attribute is mandatory if the feature 'SB' is supported. If 'SB' is not supported, the attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "OccupiedSetbackMax" attribute, which is identified by the ID '0x0036'. This attribute is of the type 'UnsignedTemperature' and is constrained to values between 'OccupiedSetbackMin' and 25.4°C. The 'Quality' is marked as 'XF', indicating specific quality factors that might be defined elsewhere. The default value for this attribute is 'null', and it has 'Read' and 'View' access permissions, as indicated by 'R V'. The conformance rule 'SB' implies that this attribute is mandatory if the feature 'SB' is supported. If 'SB' is not supported, the conformance rule does not specify an alternative, suggesting that the attribute may not be required in such cases.

* The table row describes an attribute named "UnoccupiedSetback" within the Thermostat Cluster's Attributes section. This attribute is of type "UnsignedTemperature" and is constrained between "UnoccupiedSetbackMin" and "UnoccupiedSetbackMax." It has a quality of "XN," indicating it is not allowed in certain contexts, and a default value of "null." The access level is "RW VM," meaning it is readable and writable with viewable metadata. The conformance rule "SB & OCC" specifies that the "UnoccupiedSetback" attribute is mandatory if both the "SB" (Setback) and "OCC" (Occupancy) features are supported. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "UnoccupiedSetbackMin" attribute. This attribute is of type "UnsignedTemperature" and is constrained by the maximum value of "UnoccupiedSetbackMax." It has a quality of "XF," a default value of "null," and access permissions of "R V," indicating it can be read and is volatile. The conformance rule "SB & OCC" means that the "UnoccupiedSetbackMin" attribute is mandatory if both the "SB" (Setback) feature and the "OCC" (Occupancy) feature are supported. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute named "UnoccupiedSetbackMax" within the Thermostat Cluster's Attributes section. This attribute has an ID of '0x0039' and is of the type 'UnsignedTemperature', with a constraint range from 'UnoccupiedSetbackMin' to 25.4°C. The quality is marked as 'XF', the default value is 'null', and it has read and view access ('R V'). The conformance rule 'SB & OCC' indicates that the "UnoccupiedSetbackMax" attribute is mandatory if both the 'SB' (Setback) and 'OCC' (Occupancy) features are supported by the device. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute within the Thermostat Cluster, specifically the "EmergencyHeatDelta" attribute. This attribute is of the type "UnsignedTemperature" and is applicable to all instances of the cluster, as indicated by the constraint "all." It has a default value of 25.5°C and can be accessed with read and write permissions, as well as by the virtual machine (RW VM). The quality is marked as "N," which typically indicates a standard quality level. The conformance rule for "EmergencyHeatDelta" is "O," meaning this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would make it mandatory.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'ACType' attribute. This attribute is identified by the ID '0x0040' and is of the type 'ACTypeEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'N', which typically denotes a non-reportable attribute. The default value for 'ACType' is '0', and it has 'RW VM' access, meaning it is readable and writable, with VM likely indicating a specific access condition or mode. The 'Conformance' for this attribute is 'O', which means that the 'ACType' attribute is optional. It is not required for compliance with the Matter specification, and there are no dependencies or conditions that alter this optional status.

* The table row describes an attribute named "ACCapacity" within the Thermostat Cluster's Attributes section. This attribute has an ID of '0x0041' and is of type 'uint16', indicating it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', meaning it applies universally within its context. The 'Quality' is 'N', which typically denotes a normal or standard quality level. The default value for this attribute is '0', and it has 'RW VM' access, meaning it can be read and written, with the possibility of being volatile or managed. The conformance rule for "ACCapacity" is 'O', indicating that this attribute is optional. This means it is not required for implementation and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ACRefrigerantType" attribute, identified by the ID '0x0042'. This attribute is of the type 'ACRefrigerantTypeEnum' and has constraints that are described elsewhere in the documentation. It is not a quality attribute ('Quality': 'N'), has a default value of '0', and its access level is 'RW VM', meaning it is readable and writable with view and modify permissions. The conformance rule for this attribute is 'O', indicating that it is optional. This means that the implementation of the "ACRefrigerantType" attribute is not required and does not depend on any other features or conditions.

* In the Thermostat Cluster, within the Attributes section, the entry for 'ACCompressorType' is identified by the ID '0x0043' and is of the type 'ACCompressorTypeEnum'. The attribute's constraint is described elsewhere in the documentation, and it is not a quality attribute ('N'). The default value for this attribute is '0', and it has read-write access with viewable metadata ('RW VM'). The conformance rule for 'ACCompressorType' is 'O', meaning this attribute is optional. It is not required for implementation and does not depend on any specific conditions or features being supported.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Thermostat Cluster, specifically the "ACErrorCode" attribute. This attribute is identified by the ID '0x0044' and is of the type 'ACErrorCodeBitmap'. It has a constraint of 'all', a default value of '0', and an access level of 'RW VM', which means it is readable and writable with view and modify permissions. The conformance rule for this attribute is 'O', indicating that the "ACErrorCode" attribute is optional. This means that the implementation of this attribute is not required and there are no dependencies or conditions that mandate its inclusion in a device's implementation of the Thermostat Cluster.

* In the Thermostat Cluster, within the Attributes section, the entry for 'ACLouverPosition' is identified by the ID '0x0045' and is of the type 'ACLouverPositionEnum'. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. It has a default value of '0' and is accessible with read and write permissions, as well as being visible to management (RW VM). The quality is marked as 'N', which typically indicates a non-critical attribute. The conformance rule for 'ACLouverPosition' is 'O', meaning this attribute is optional. It is not required for implementation and does not have any dependencies on other features or conditions.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'ACCoilTemperature' attribute, identified by the ID '0x0046'. This attribute is of the 'temperature' type and applies universally ('Constraint': 'all'). It is marked with a 'Quality' of 'X', indicating that it is explicitly disallowed in some contexts, and it has a default value of 'null'. The attribute's access is defined as 'R V', meaning it can be read and is volatile. The 'Conformance' field is marked as 'O', which means that the 'ACCoilTemperature' attribute is optional. This implies that while it is not required to be implemented in all devices, it can be included at the discretion of the device manufacturer without any dependencies or conditions.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ACCapacityFormat" attribute. This attribute is identified by the ID '0x0047' and is of the type 'ACCapacityFormatEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'N', which typically refers to the quality or reliability of the data, though its specific meaning would be defined in the broader context of the specification. The default value for this attribute is '0', and it has 'RW VM' access, meaning it can be read and written, with VM likely indicating a specific access condition or mode. The 'Conformance' is marked as 'O', which means that the ACCapacityFormat attribute is optional. It is not required for all implementations of the Thermostat Cluster, and there are no dependencies or conditions that alter this optional status.

* The table row describes an attribute named "PresetTypes" within the Thermostat Cluster's Attributes section. This attribute has an ID of '0x0048' and is of the type 'list[PresetTypeStruct]'. The 'Constraint' is described elsewhere in the documentation, indicated by 'desc'. The 'Quality' is marked as 'F', and the default value is 'MS'. The attribute has 'Read' and 'View' access permissions, denoted by 'R V'. The conformance rule for this attribute is 'PRES', which means that the requirement for this attribute is determined by the support of the 'PRES' feature. If the 'PRES' feature is supported, the attribute is mandatory; otherwise, its inclusion is not required.

* The table row describes an attribute named "ScheduleTypes" within the Thermostat Cluster's Attributes section. This attribute is identified by the ID '0x0049' and is of the type 'list[ScheduleTypeStruct]'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'F', and the default value is 'MS'. It has 'R V' access, meaning it is readable and possibly volatile. The 'Conformance' field is 'MSCH', which, according to the Matter Conformance Interpretation Guide, suggests that the conformance condition is complex and likely described in more detail elsewhere in the documentation. This implies that the requirement for this attribute is not straightforward and depends on specific conditions or contexts that are not immediately apparent from the conformance string alone.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'NumberOfPresets' attribute. This attribute has an ID of '0x004A' and is of type 'uint8', meaning it is an 8-bit unsigned integer. It applies universally ('Constraint': 'all') and has a default value of '0'. The 'Quality' is marked as 'F', which typically indicates a specific quality or characteristic defined elsewhere in the specification. The 'Access' is 'R V', meaning it can be read and possibly verified. The 'Conformance' field is 'PRES', which, according to the Matter Conformance Interpretation Guide, suggests that the attribute is mandatory if the 'PRES' feature is supported. If the 'PRES' feature is not supported, the conformance of this attribute is not explicitly defined in this entry, implying it may not be required or its status is determined by other conditions not specified here.

* The table row describes an attribute within the Thermostat Cluster, specifically the 'NumberOfSchedules' attribute. This attribute has an ID of '0x004B' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is set to 'all', indicating it applies universally within its context. The 'Quality' is marked as 'F', which typically denotes a feature-related quality. The default value for this attribute is '0', and it has 'R V' access, meaning it is readable and can be viewed. The 'Conformance' field is marked as 'MSCH', which does not directly match any of the basic conformance tags or logical conditions outlined in the guide. This suggests that the conformance for 'NumberOfSchedules' may be described elsewhere in the documentation, possibly under a more complex or specific condition not covered by the basic tags or expressions. Therefore, to fully understand the conformance requirements for this attribute, one would

* The table row describes an attribute within the Thermostat Cluster, specifically the "NumberOfScheduleTransitions" attribute. This attribute has an ID of '0x004C' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is 'all', indicating it applies universally within its context. The 'Quality' is marked as 'F', and it has a default value of '0'. The 'Access' is 'R V', suggesting it is readable and possibly volatile. The 'Conformance' is specified as 'MSCH', which, according to the Matter Conformance Interpretation Guide, implies that this attribute is mandatory when the feature or condition 'MSCH' is supported. This means that if the 'MSCH' feature is present in the device, the "NumberOfScheduleTransitions" attribute must be implemented.

* The table row describes an attribute within the Thermostat Cluster, specifically the "NumberOfScheduleTransitionPerDay" attribute. This attribute is identified by the ID '0x004D' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that this attribute applies universally within its context. The 'Quality' is marked as 'XF', which typically refers to extended features or functionalities, though the specific meaning would depend on the broader documentation. The 'Default' value is 'null', suggesting there is no predefined default value for this attribute. The 'Access' is 'R V', meaning it is readable and possibly has some vendor-specific access considerations. The 'Conformance' is 'MSCH', which, according to the Matter Conformance Interpretation Guide, means this attribute is Mandatory if the feature 'MSCH' (likely referring to a specific scheduling feature within the thermostat context) is supported. If 'MSCH

* The table row describes an attribute within the Thermostat Cluster, specifically the 'ActivePresetHandle'. This attribute has an ID of '0x004E' and is of type 'octstr', with a maximum constraint of 16 characters. Its quality is marked as 'XN', indicating it is not allowed in certain contexts, and its default value is 'null'. The access permissions are 'R V', meaning it can be read and is volatile. The conformance rule 'PRES' indicates that the requirement for this attribute is described elsewhere in the documentation, as it is too complex to be captured by a simple expression. This means that the conditions under which 'ActivePresetHandle' is required or optional are detailed in another section, likely involving specific features or scenarios related to the Thermostat Cluster.

* The table row describes an attribute within the Thermostat Cluster, specifically the "ActiveScheduleHandle" attribute. This attribute has an ID of '0x004F' and is of type 'octstr' with a maximum constraint of 16 characters. It has a quality designation of 'XN', indicating it is not allowed in certain contexts, and its default value is 'null'. The access level is 'R V', meaning it is readable and volatile. The conformance rule 'MSCH' indicates that this attribute is mandatory when the feature 'MSCH' (likely referring to a specific scheduling feature within the thermostat context) is supported. If 'MSCH' is not supported, the attribute is not required. This means that the presence of the 'ActiveScheduleHandle' attribute is contingent upon the support of the 'MSCH' feature, making it a conditional requirement based on the device's capabilities.

_Table parsed from section 'Attributes':_

* In the Thermostat Cluster's Attributes section, the entry for 'Presets' with ID '0x0050' is a list of 'PresetStruct' types, constrained by the maximum number of presets allowed. It is marked with a quality of 'NT' (Non-Timed), has a default value of 'empty', and allows read-write access with viewable metadata (RW VM). The conformance rule 'PRES' indicates that the 'Presets' attribute is mandatory if the feature 'PRES' is supported. If 'PRES' is not supported, the attribute is not required. This means that the presence and requirement of the 'Presets' attribute depend on whether the 'PRES' feature is implemented in the device.

* In the Thermostat Cluster's Attributes section, the entry for 'Schedules' with ID '0x0051' is a list of 'ScheduleStruct' types. The 'Constraint' is described elsewhere in the documentation, indicating complexity beyond a simple expression. The 'Quality' is marked as 'NT', and the default state is 'empty'. It has 'RW VM' access, meaning it is readable and writable, with viewable metadata. The 'Conformance' field is marked as 'MSCH', which, according to the Matter Conformance Interpretation Guide, suggests that the conformance is described in detail elsewhere in the documentation. This implies that the requirement for the 'Schedules' attribute is complex and context-dependent, necessitating a review of the specific section in the documentation for precise implementation requirements.

* The table row describes an attribute within the Thermostat Cluster, specifically the "SetpointHoldExpiryTimestamp" attribute. This attribute is identified by the ID '0x0052' and is of type 'epoch-s', which likely represents a timestamp in seconds since a defined epoch. The 'Constraint' is listed as 'all', suggesting it applies universally within its context. The 'Quality' is 'XN', indicating specific quality characteristics, though the exact meaning of 'XN' would be defined elsewhere in the specification. The default value for this attribute is 'null', and it has 'R V' access, meaning it is readable and possibly volatile. The 'Conformance' is marked as 'O', meaning this attribute is optional; it is not required and has no dependencies on other features or conditions.

4.3.9.1. Calculated Local Temperature
The local temperature SHALL be calculated from the measured temperature, including any adjust
ments applied by LocalTemperatureCalibration attribute (if any) as follows:
Calculated Local Temperature = (measured temperature) + LocalTemperatureCalibration
The measured temperature value may be local, or remote, depending on the value of the Remote
Sensing attribute when supported.
All setpoint attributes in the Thermostat cluster SHALL be triggered based off this calculated value
(i.e., measured temperature and any calibration offset).
If the LocalTemperatureNotExposed feature is present, the behavior of the thermostat SHALL be
that the equipment’s temperature control uses the calculated local temperature even if that value is
not reported in the LocalTemperature attribute.
4.3.9.2. LocalTemperature Attribute
This attribute SHALL indicate the current Calculated Local Temperature, when available.
• If the LTNE feature is not supported:
◦ If the LocalTemperatureCalibration is invalid or currently unavailable, the attribute SHALL
report null.
◦ If the LocalTemperatureCalibration is valid, the attribute SHALL report that value.
• Otherwise, if the LTNE feature is supported, there is no feedback externally available for the
LocalTemperatureCalibration.  In  that  case,  the  LocalTemperature  attribute  SHALL  always
report null.
4.3.9.3. OutdoorTemperature Attribute
This attribute SHALL indicate the outdoor temperature, as measured locally or remotely (over the
network).
4.3.9.4. Occupancy Attribute
This attribute SHALL indicate whether the heated/cooled space is occupied or not, as measured
locally or remotely (over the network).
4.3.9.5. AbsMinHeatSetpointLimit Attribute
This attribute SHALL indicate the absolute minimum level that the heating setpoint MAY be set to.
This is a limitation imposed by the manufacturer.
Refer to Setpoint Limits for constraints
4.3.9.6. AbsMaxHeatSetpointLimit Attribute
This attribute SHALL indicate the absolute maximum level that the heating setpoint MAY be set to.
This is a limitation imposed by the manufacturer.
Refer to Setpoint Limits for constraints
4.3.9.7. AbsMinCoolSetpointLimit Attribute
This attribute SHALL indicate the absolute minimum level that the cooling setpoint MAY be set to.
This is a limitation imposed by the manufacturer.
Refer to Setpoint Limits for constraints
4.3.9.8. AbsMaxCoolSetpointLimit Attribute
This attribute SHALL indicate the absolute maximum level that the cooling setpoint MAY be set to.
This is a limitation imposed by the manufacturer.
Refer to Setpoint Limits for constraints
4.3.9.9. PICoolingDemand Attribute
This attribute SHALL indicate the level of cooling demanded by the PI (proportional integral) con
trol loop in use by the thermostat (if any), in percent. This value is 0 when the thermostat is in “off”
or “heating” mode.
This attribute is reported regularly and MAY be used to control a cooling device.
4.3.9.10. PIHeatingDemand Attribute
This attribute SHALL indicate the level of heating demanded by the PI loop in percent. This value is
0 when the thermostat is in “off” or “cooling” mode.
This attribute is reported regularly and MAY be used to control a heating device.
4.3.9.11. HVACSystemTypeConfiguration Attribute
This attribute SHALL indicate the HVAC system type controlled by the thermostat. If the thermostat
uses physical DIP switches to set these parameters, this information SHALL be available read-only
from the DIP switches. If these parameters are set via software, there SHALL be read/write access in
order to provide remote programming capability.
4.3.9.12. LocalTemperatureCalibration Attribute
This attribute SHALL indicate the offset the Thermostat server SHALL make to the measured tem
perature (locally or remotely) to adjust the Calculated Local Temperature prior to using, displaying
or reporting it.
The purpose of this attribute is to adjust the calibration of the Thermostat server per the user’s
preferences (e.g., to match if there are multiple servers displaying different values for the same
HVAC area) or compensate for variability amongst temperature sensors.
If a Thermostat client attempts to write LocalTemperatureCalibration attribute to an unsupported
value (e.g., out of the range supported by the Thermostat server), the Thermostat server SHALL
respond with a status of SUCCESS and set the value of LocalTemperatureCalibration to the upper or
lower limit reached.
Prior to revision 8 of this cluster specification the value of this attribute was con
NOTE
strained to a range of -2.5°C to 2.5°C.
4.3.9.13. OccupiedCoolingSetpoint Attribute
This attribute SHALL indicate the cooling mode setpoint when the room is occupied.
Refer to Setpoint Limits for constraints.
If an attempt is made to set this attribute to a value greater than MaxCoolSetpointLimit or less than
MinCoolSetpointLimit, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If this attribute is set to a value that is less than (OccupiedHeatingSetpoint + MinSetpointDeadBand),
the value of OccupiedHeatingSetpoint SHALL be adjusted to (OccupiedCoolingSetpoint - MinSet
pointDeadBand).
If the occupancy status of the room is unknown, this attribute SHALL be used as the cooling mode
setpoint.
If a client changes the value of this attribute, the server supports the PRES feature, and the server
either does not support the OCC feature or the Occupied bit is set on the Occupancy attribute, the
value of the ActivePresetHandle attribute SHALL be set to null.
4.3.9.14. OccupiedHeatingSetpoint Attribute
This attribute SHALL indicate the heating mode setpoint when the room is occupied.
Refer to Setpoint Limits for constraints.
If an attempt is made to set this attribute to a value greater than MaxHeatSetpointLimit or less than
MinHeatSetpointLimit, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If this attribute is set to a value that is greater than (OccupiedCoolingSetpoint - MinSetpointDead
Band), the value of OccupiedCoolingSetpoint SHALL be adjusted to (OccupiedHeatingSetpoint +
MinSetpointDeadBand).
If the occupancy status of the room is unknown, this attribute SHALL be used as the heating mode
setpoint.
If a client changes the value of this attribute, the server supports the PRES feature, and the server
either does not support the OCC feature or the Occupied bit is set on the Occupancy attribute, the
value of the ActivePresetHandle attribute SHALL be set to null.
4.3.9.15. UnoccupiedCoolingSetpoint Attribute
This attribute SHALL indicate the cooling mode setpoint when the room is unoccupied.
Refer to Setpoint Limits for constraints.
If an attempt is made to set this attribute to a value greater than MaxCoolSetpointLimit or less than
MinCoolSetpointLimit, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If this attribute is set to a value that is less than (UnoccupiedHeatingSetpoint + MinSetpointDead
Band), the value of UnoccupiedHeatingSetpoint SHALL be adjusted to (UnoccupiedCoolingSetpoint -
MinSetpointDeadBand).
If the occupancy status of the room is unknown, this attribute SHALL NOT be used.
If a client changes the value of this attribute, the server supports the PRES and OCC features, and
the Occupied bit is not set on the Occupancy attribute, the value of the ActivePresetHandle attribute
SHALL be set to null.
4.3.9.16. UnoccupiedHeatingSetpoint Attribute
This attribute SHALL indicate the heating mode setpoint when the room is unoccupied.
Refer to Setpoint Limits for constraints.
If an attempt is made to set this attribute to a value greater than MaxHeatSetpointLimit or less than
MinHeatSetpointLimit, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If this attribute is set to a value that is greater than (UnoccupiedCoolingSetpoint - MinSetpointDead
Band), the value of UnoccupiedCoolingSetpoint SHALL be adjusted to (UnoccupiedHeatingSetpoint
+ MinSetpointDeadBand).
If the occupancy status of the room is unknown, this attribute SHALL NOT be used.
If a client changes the value of this attribute, the server supports the PRES and OCC features, and
the Occupied bit is not set on the Occupancy attribute, the value of the ActivePresetHandle attribute
SHALL be set to null.
4.3.9.17. MinHeatSetpointLimit Attribute
This attribute SHALL indicate the minimum level that the heating setpoint MAY be set to.
This attribute, and the following three attributes, allow the user to define setpoint limits more con
strictive than the manufacturer imposed ones. Limiting users (e.g., in a commercial building) to
such setpoint limits can help conserve power.
Refer to Setpoint Limits for constraints. If an attempt is made to set this attribute to a value which
conflicts with setpoint values then those setpoints SHALL be adjusted by the minimum amount to
permit this attribute to be set to the desired value. If an attempt is made to set this attribute to a
value which is not consistent with the constraints and cannot be resolved by modifying setpoints
then a response with the status code CONSTRAINT_ERROR SHALL be returned.
4.3.9.18. MaxHeatSetpointLimit Attribute
This attribute SHALL indicate the maximum level that the heating setpoint MAY be set to.
Refer to Setpoint Limits for constraints. If an attempt is made to set this attribute to a value which
conflicts with setpoint values then those setpoints SHALL be adjusted by the minimum amount to
permit this attribute to be set to the desired value. If an attempt is made to set this attribute to a
value which is not consistent with the constraints and cannot be resolved by modifying setpoints
then a response with the status code CONSTRAINT_ERROR SHALL be returned.
4.3.9.19. MinCoolSetpointLimit Attribute
This attribute SHALL indicate the minimum level that the cooling setpoint MAY be set to.
Refer to Setpoint Limits for constraints. If an attempt is made to set this attribute to a value which
conflicts with setpoint values then those setpoints SHALL be adjusted by the minimum amount to
permit this attribute to be set to the desired value. If an attempt is made to set this attribute to a
value which is not consistent with the constraints and cannot be resolved by modifying setpoints
then a response with the status code CONSTRAINT_ERROR SHALL be returned.
4.3.9.20. MaxCoolSetpointLimit Attribute
This attribute SHALL indicate the maximum level that the cooling setpoint MAY be set to.
Refer to Setpoint Limits for constraints. If an attempt is made to set this attribute to a value which
conflicts with setpoint values then those setpoints SHALL be adjusted by the minimum amount to
permit this attribute to be set to the desired value. If an attempt is made to set this attribute to a
value which is not consistent with the constraints and cannot be resolved by modifying setpoints
then a response with the status code CONSTRAINT_ERROR SHALL be returned.
4.3.9.21. MinSetpointDeadBand Attribute
On devices which support the AUTO feature, this attribute SHALL indicate the minimum difference
between the Heat Setpoint and the Cool Setpoint.
Refer to Setpoint Limits for constraints.
Prior to revision 8 of this cluster specification the value of this attribute was con
NOTE
strained to a range of 0°C to 2.5°C.
For backwards compatibility, this attribute is optionally writeable. However any
NOTE
writes to this attribute SHALL be silently ignored.
4.3.9.22. RemoteSensing Attribute
This attribute SHALL indicate when the local temperature, outdoor temperature and occupancy are
being sensed by remote networked sensors, rather than internal sensors.
If the LTNE feature is present in the server, the LocalTemperature RemoteSensing bit value SHALL
always report a value of 0.
If the LocalTemperature RemoteSensing bit is written with a value of 1 when the LTNE feature is
present, the write SHALL fail and the server SHALL report a CONSTRAINT_ERROR.
4.3.9.23. ControlSequenceOfOperation Attribute
This attribute SHALL indicate the overall operating environment of the thermostat, and thus the
possible system modes that the thermostat can operate in.
If an attempt is made to write to this attribute, the server SHALL silently ignore the write and the
value of this attribute SHALL remain unchanged. This behavior is in place for backwards compati
bility with existing thermostats.
4.3.9.24. SystemMode Attribute
This attribute SHALL indicate the current operating mode of the thermostat. Its value SHALL be
limited by the ControlSequenceOfOperation attribute.
4.3.9.25. AlarmMask Attribute
This attribute SHALL indicate whether each of the alarms in AlarmCodeBitmap is enabled.
When the Alarms cluster is implemented on a device, and one of the alarm conditions included in
AlarmCodeBitmap occurs, an alarm notification is generated, with the alarm code field set as listed
in AlarmCodeBitmap.
4.3.9.26. ThermostatRunningMode Attribute
This attribute SHALL indicate the running mode of the thermostat. This attribute uses the same val
ues as SystemModeEnum but can only be Off, Cool or Heat. This attribute is intended to provide
additional information when the thermostat’s system mode is in auto mode.
4.3.9.27. StartOfWeek Attribute
This attribute SHALL indicate the day of the week that this thermostat considers to be the start of
week for weekly setpoint scheduling.
This attribute MAY be able to be used as the base to determine if the device supports weekly sched
uling by reading the attribute. Successful response means that the weekly scheduling is supported.
4.3.9.28. NumberOfWeeklyTransitions Attribute
This attribute SHALL indicate how many weekly schedule transitions the thermostat is capable of
handling.
4.3.9.29. NumberOfDailyTransitions Attribute
This attribute SHALL indicate how many daily schedule transitions the thermostat is capable of
handling.
4.3.9.30. TemperatureSetpointHold Attribute
This attribute SHALL indicate the temperature hold status on the thermostat. If hold status is on,
the thermostat SHOULD maintain the temperature setpoint for the current mode until a system
mode change. If hold status is off, the thermostat SHOULD follow the setpoint transitions specified
by its internal scheduling program. If the thermostat supports setpoint hold for a specific duration,
it SHOULD also implement the TemperatureSetpointHoldDuration attribute.
If the server supports a setpoint hold for a specific duration, it SHOULD also implement the Set
pointHoldExpiryTimestamp attribute.
If this attribute is updated to SetpointHoldOn and the TemperatureSetpointHoldDuration has a non-
null value and the SetpointHoldExpiryTimestamp is supported, the server SHALL update the Set
pointHoldExpiryTimestamp with a value of current UTC timestamp, in seconds, plus the value in
TemperatureSetpointHoldDuration multiplied by 60.
If this attribute is updated to SetpointHoldOff and the SetpointHoldExpiryTimestamp is supported,
the server SHALL set the SetpointHoldExpiryTimestamp to null.
4.3.9.31. TemperatureSetpointHoldDuration Attribute
This attribute SHALL indicate the period in minutes for which a setpoint hold is active. Thermostats
that support hold for a specified duration SHOULD implement this attribute. The null value indi
cates the field is unused. All other values are reserved.
If this attribute is updated to a non-null value and the TemperatureSetpointHold is set to Set
pointHoldOn and the SetpointHoldExpiryTimestamp is supported, the server SHALL update Set
pointHoldExpiryTimestamp with a value of current UTC timestamp, in seconds, plus the new value
of this attribute multiplied by 60.
If this attribute is set to null and the SetpointHoldExpiryTimestamp is supported, the server SHALL
set the SetpointHoldExpiryTimestamp to null.
4.3.9.32. ThermostatProgrammingOperationMode Attribute
This attribute SHALL indicate the operational state of the thermostat’s programming. The thermo
stat SHALL modify its programming operation when this attribute is modified by a client and
update this attribute when its programming operation is modified locally by a user. The thermostat
MAY support more than one active ProgrammingOperationModeBitmap. For example, the thermo
stat MAY operate simultaneously in Schedule Programming Mode and Recovery Mode.
Thermostats which contain a schedule MAY use this attribute to control how that schedule is used,
even if they do not support the ScheduleConfiguration feature.
When ScheduleActive is not set, the setpoint is altered only by manual up/down changes at the ther
mostat or remotely, not by internal schedule programming.
Modifying the ScheduleActive bit does not clear or delete previous weekly schedule
NOTE
programming configurations.
4.3.9.33. ThermostatRunningState Attribute
This attribute SHALL indicate the current relay state of the heat, cool, and fan relays.
Unimplemented outputs SHALL be treated as if they were Off.
4.3.9.34. SetpointChangeSource Attribute
This attribute SHALL indicate the source of the current active OccupiedCoolingSetpoint or Occu
piedHeatingSetpoint (i.e., who or what determined the current setpoint).
This attribute enables service providers to determine whether changes to setpoints were initiated
due to occupant comfort, scheduled programming or some other source (e.g., electric utility or
other service provider). Because automation services MAY initiate frequent setpoint changes, this
attribute clearly differentiates the source of setpoint changes made at the thermostat.
4.3.9.35. SetpointChangeAmount Attribute
This attribute SHALL indicate the delta between the current active OccupiedCoolingSetpoint or
OccupiedHeatingSetpoint and the previous active setpoint. This attribute is meant to accompany
the SetpointChangeSource attribute; devices implementing SetpointChangeAmount SHOULD also
implement SetpointChangeSource.
The null value indicates that the previous setpoint was unknown.
4.3.9.36. SetpointChangeSourceTimestamp Attribute
This  attribute  SHALL  indicate  the  time  in  UTC  at  which  the  SetpointChangeAmount  attribute
change was recorded.
4.3.9.37. OccupiedSetback Attribute
This attribute SHALL indicate the amount that the Thermostat server will allow the Calculated
Local Temperature to float above the OccupiedCoolingSetpoint (i.e., OccupiedCoolingSetpoint +
OccupiedSetback) or below the OccupiedHeatingSetpoint setpoint (i.e., OccupiedHeatingSetpoint –
OccupiedSetback) before initiating a state change to bring the temperature back to the user’s
desired setpoint. This attribute is sometimes also referred to as the “span.”
The purpose of this attribute is to allow remote configuration of the span between the desired set
point and the measured temperature to help prevent over-cycling and reduce energy bills, though
this may result in lower comfort on the part of some users.
The null value indicates the attribute is unused.
If the Thermostat client attempts to write OccupiedSetback to a value greater than OccupiedSet
backMax, the Thermostat server SHALL set its OccupiedSetback value to OccupiedSetbackMax and
SHALL send a Write Attribute Response command with a Status Code field enumeration of SUCCESS
response.
If the Thermostat client attempts to write OccupiedSetback to a value less than OccupiedSetback
Min,  the  Thermostat  server  SHALL  set  its  OccupiedSetback  value  to  OccupiedSetbackMin  and
SHALL send a Write Attribute Response command with a Status Code field enumeration of SUCCESS
response.
4.3.9.38. OccupiedSetbackMin Attribute
This attribute SHALL indicate the minimum value that the Thermostat server will allow the Occu
piedSetback attribute to be configured by a user.
The null value indicates the attribute is unused.
4.3.9.39. OccupiedSetbackMax Attribute
This attribute SHALL indicate the maximum value that the Thermostat server will allow the Occu
piedSetback attribute to be configured by a user.
The null value indicates the attribute is unused.
4.3.9.40. UnoccupiedSetback Attribute
This attribute SHALL indicate the amount that the Thermostat server will allow the Calculated
Local Temperature to float above the UnoccupiedCoolingSetpoint (i.e., UnoccupiedCoolingSetpoint +
UnoccupiedSetback) or below the UnoccupiedHeatingSetpoint setpoint (i.e., UnoccupiedHeatingSet
point - UnoccupiedSetback) before initiating a state change to bring the temperature back to the
user’s desired setpoint. This attribute is sometimes also referred to as the “span.”
The purpose of this attribute is to allow remote configuration of the span between the desired set
point and the measured temperature to help prevent over-cycling and reduce energy bills, though
this may result in lower comfort on the part of some users.
The null value indicates the attribute is unused.
If the Thermostat client attempts to write UnoccupiedSetback to a value greater than Unoccupied
SetbackMax, the Thermostat server SHALL set its UnoccupiedSetback value to UnoccupiedSetback
Max and SHALL send a Write Attribute Response command with a Status Code field enumeration of
SUCCESS response.
If the Thermostat client attempts to write UnoccupiedSetback to a value less than UnoccupiedSet
backMin, the Thermostat server SHALL set its UnoccupiedSetback value to UnoccupiedSetbackMin
and SHALL send a Write Attribute Response command with a Status Code field enumeration of
SUCCESS response.
4.3.9.41. UnoccupiedSetbackMin Attribute
This attribute SHALL indicate the minimum value that the Thermostat server will allow the Unoc
cupiedSetback attribute to be configured by a user.
The null value indicates the attribute is unused.
4.3.9.42. UnoccupiedSetbackMax Attribute
This attribute SHALL indicate the maximum value that the Thermostat server will allow the Unoc
cupiedSetback attribute to be configured by a user.
The null value indicates the attribute is unused.
4.3.9.43. EmergencyHeatDelta Attribute
This attribute SHALL indicate the delta between the Calculated Local Temperature and the Occu
piedHeatingSetpoint or UnoccupiedHeatingSetpoint attributes at which the Thermostat server will
operate in emergency heat mode.
If the difference between the Calculated Local Temperature and OccupiedCoolingSetpoint or Unoc
cupiedCoolingSetpoint is greater than or equal to the EmergencyHeatDelta and the Thermostat
server’s SystemMode attribute is in a heating-related mode, then the Thermostat server SHALL
immediately switch to the SystemMode attribute value that provides the highest stage of heating
(e.g., emergency heat) and continue operating in that running state until the OccupiedHeatingSet
point value is reached. For example:
• Calculated Local Temperature = 10.0°C
• OccupiedHeatingSetpoint = 16.0°C
• EmergencyHeatDelta = 2.0°C
⇒ OccupiedHeatingSetpoint - Calculated Local Temperature ≥? EmergencyHeatDelta
⇒ 16°C - 10°C ≥? 2°C
nd
⇒ TRUE >>> Thermostat server changes its SystemMode to operate in 2  stage or emergency
heat mode
The purpose of this attribute is to provide Thermostat clients the ability to configure rapid heating
when a setpoint is of a specified amount greater than the measured temperature. This allows the
heated space to be quickly heated to the desired level set by the user.
4.3.9.44. ACType Attribute
This attribute SHALL indicate the type of Mini Split ACTypeEnum of Mini Split AC is defined
depending on how Cooling and Heating condition is achieved by Mini Split AC.
4.3.9.45. ACCapacity Attribute
This attribute SHALL indicate capacity of Mini Split AC in terms of the format defined by the ACCa
pacityFormat attribute
4.3.9.46. ACRefrigerantType Attribute
This attribute SHALL indicate type of refrigerant used within the Mini Split AC.
4.3.9.47. ACCompressorType Attribute
This attribute SHALL indicate the type of compressor used within the Mini Split AC.
4.3.9.48. ACErrorCode Attribute
This attribute SHALL indicate the type of errors encountered within the Mini Split AC.
4.3.9.49. ACLouverPosition Attribute
This attribute SHALL indicate the position of Louver on the AC.
4.3.9.50. ACCoilTemperature Attribute
This attribute SHALL indicate the temperature of the AC coil, as measured locally or remotely (over
the network).
4.3.9.51. ACCapacityFormat Attribute
This attribute SHALL indicate the format for the ACCapacity attribute.
4.3.9.52. PresetTypes Attribute
This attribute SHALL indicate the supported PresetScenarioEnum values, limits on how many pre
sets can be created for each PresetScenarioEnum, and whether or not a thermostat can transition
automatically to a given scenario.
4.3.9.53. ScheduleTypes Attribute
This attribute SHALL indicate the supported SystemMode values for Schedules, limits on how many
schedules can be created for each SystemMode value, and whether or not a given SystemMode
value supports transitions to Presets, target setpoints, or both.
4.3.9.54. NumberOfPresets Attribute
This attribute SHALL indicate the maximum number of entries supported by the Presets attribute.
4.3.9.55. NumberOfSchedules Attribute
This  attribute  SHALL  indicate  the  maximum  number  of  entries  supported  by  the  Schedules
attribute.
4.3.9.56. NumberOfScheduleTransitions Attribute
This attribute SHALL indicate the maximum number of transitions per Schedules attribute entry.
4.3.9.57. NumberOfScheduleTransitionsPerDay Attribute
This attribute SHALL indicate the maximum number of transitions per day of the week supported
by each Schedules attribute entry. If this value is null, there is no limit on the number of transitions
per day.
4.3.9.58. ActivePresetHandle Attribute
This attribute SHALL indicate the PresetHandle of the active preset. If this attribute is null, then
there is no active preset.
4.3.9.59. ActiveScheduleHandle Attribute
This attribute SHALL indicate the ScheduleHandle of the active schedule. A null value in this
attribute indicates that there is no active schedule.
4.3.9.60. Presets Attribute
This attribute SHALL contain the current list of configured presets.
On receipt of a write request:
1. If the PresetHandle field is null, the PresetStruct SHALL be treated as an added preset, and the
device SHALL create a new unique value for the PresetHandle field.
a. If the BuiltIn field is true, a response with the status code CONSTRAINT_ERROR SHALL be
returned.
2. If the PresetHandle field is not null, the PresetStruct SHALL be treated as a modification of an
existing preset.
a. If the value of the PresetHandle field does not match any of the existing presets, a response
with the status code NOT_FOUND SHALL be returned.
b. If the value of the PresetHandle field is duplicated on multiple presets in the updated list, a
response with the status code CONSTRAINT_ERROR SHALL be returned.
c. If the BuiltIn field is true, and the PresetStruct in the current value with a matching Pre
setHandle field has a BuiltIn field set to false, a response with the status code CONSTRAIN
T_ERROR SHALL be returned.
d. If the BuiltIn field is false, and the PresetStruct in the current value with a matching Pre
setHandle field has a BuiltIn field set to true, a response with the status code CONSTRAIN
T_ERROR SHALL be returned.
3. If the specified PresetScenarioEnum value does not exist in PresetTypes, a response with the
status code CONSTRAINT_ERROR SHALL be returned.
4. If the Name is set, but the associated PresetTypeStruct does not have the SupportsNames bit set,
a response with the status code CONSTRAINT_ERROR SHALL be returned.
5. If appending the received PresetStruct to the pending list of Presets would cause the total num
ber of pending presets to exceed the value of the NumberOfPresets attribute, a response with
the status code RESOURCE_EXHAUSTED SHALL be returned.
6. If appending the received PresetStruct to the pending list of Presets would cause the total num
ber of pending presets whose PresetScenario field matches the appended preset’s PresetSce
nario field to exceed the value of the NumberOfPresets field on the PresetTypeStruct whose Pre
setScenario matches the appended preset’s PresetScenario field, a response with the status code
RESOURCE_EXHAUSTED SHALL be returned.
7. Otherwise, the write SHALL be pended until receipt of a commit request, and the status code
SUCCESS SHALL be returned.
a. If the BuiltIn field is null:
i. If there is a PresetStruct in the current value with a matching PresetHandle field, the
BuiltIn field on the pending PresetStruct SHALL be set to the value of the BuiltIn on the
matching PresetStruct.
ii. Otherwise, the BuiltIn field on the pending PresetStruct SHALL be set to false.
On an attempt to commit, the status of this attribute SHALL be determined as follows:
1. For all existing presets:
a. If, after applying all pending changes, the updated value of the Presets attribute would not
contain a PresetStruct with a matching PresetHandle field, indicating the removal of the Pre
setStruct, the server SHALL check for invalid removal of the PresetStruct:
i. If the BuiltIn field is true on the removed PresetStruct, the attribute status SHALL be
CONSTRAINT_ERROR.
ii. If the MSCH feature is supported and the removed PresetHandle would be referenced by
any PresetHandle on any ScheduleTransitionStruct on any ScheduleStruct in the updated
value of the Schedules attribute, the attribute status SHALL be INVALID_IN_STATE.
iii. If the removed PresetHandle is equal to the value of the ActivePresetHandle attribute,
the attribute status SHALL be INVALID_IN_STATE.
2. Otherwise, the attribute status SHALL be SUCCESS.
4.3.9.61. Schedules Attribute
This attribute SHALL contain a list of ScheduleStructs.
On receipt of a write request:
1. For all schedules in the write request:
a. If the ScheduleHandle field is null, the ScheduleStruct SHALL be treated as an added sched
ule, and the device SHALL create a new unique value for the ScheduleHandle field.
i. If the BuiltIn field is true, a response with the status code CONSTRAINT_ERROR SHALL
be returned.
b. Otherwise, if the ScheduleHandle field is not null, the ScheduleStruct SHALL be treated as a
modification of an existing schedule.
i. If the value of the ScheduleHandle field does not match any of the existing schedules, a
response with the status code NOT_FOUND SHALL be returned.
ii. If the BuiltIn field is true, and the ScheduleStruct in the current value with a matching
ScheduleHandle field has a BuiltIn field set to false, a response with the status code CON
STRAINT_ERROR SHALL be returned.
iii. If the BuiltIn field is false, and the ScheduleStruct in the current value with a matching
ScheduleHandle field has a BuiltIn field set to true, a response with the status code CON
STRAINT_ERROR SHALL be returned.
c. If the specified SystemMode does not exist in ScheduleTypes, a response with the status code
CONSTRAINT_ERROR SHALL be returned.
d. If the number of transitions exceeds the NumberOfScheduleTransitions value, a response
with the status code RESOURCE_EXHAUSTED SHALL be returned.
e. If the value of the NumberOfScheduleTransitionsPerDay attribute is not null, and the num
ber of transitions on any single day of the week exceeds the NumberOfScheduleTransition
sPerDay value, a response with the status code RESOURCE_EXHAUSTED SHALL be returned.
f. If the PresetHandle field is present, but the associated ScheduleTypeStruct does not have the
SupportsPresets bit set, a response with the status code CONSTRAINT_ERROR SHALL be
returned.
g. If the PresetHandle field is present, but after applying all pending changes, the Presets
attribute would not contain a PresetStruct whose PresetHandle field matches the value of
the PresetHandle field, a response with the status code CONSTRAINT_ERROR SHALL be
returned.
h. If the Name is set, but the associated ScheduleTypeStruct does not have the SupportsNames
bit set, a response with the status code CONSTRAINT_ERROR SHALL be returned.
i. For all transitions in all schedules in the write request:
i. If the PresetHandle field is present, but the ScheduleTypeStruct matching the value of
the SystemMode field on the encompassing ScheduleStruct does not have the SupportsP
resets bit set, a response with the status code CONSTRAINT_ERROR SHALL be returned.
j. If the PresetHandle field is present, but after applying all pending changes, the Presets
attribute would not contain a PresetStruct whose PresetHandle field matches the value of
the PresetHandle field, a response with the status code CONSTRAINT_ERROR SHALL be
returned.
i. If the SystemMode field is present, but the ScheduleTypeStruct matching the value of the
SystemMode field on the encompassing ScheduleStruct does not have the SupportsSet
points bit set, a response with the status code CONSTRAINT_ERROR SHALL be returned.
ii. If the SystemMode field is has a value of SystemModeOff, but the ScheduleTypeStruct
matching the value of the SystemMode field on the encompassing ScheduleStruct does
not have the SupportsOff bit set, a response with the status code CONSTRAINT_ERROR
SHALL be returned.
k. If the HeatingSetpoint field is present, but the ScheduleTypeStruct matching the value of the
SystemMode field on the encompassing ScheduleStruct does not have the SupportsSetpoints
bit set, a response with the status code CONSTRAINT_ERROR SHALL be returned.
l. If the CoolingSetpoint field is present, but the ScheduleTypeStruct matching the value of the
SystemMode field on the encompassing ScheduleStruct does not have the SupportsSetpoints
bit set, a response with the status code CONSTRAINT_ERROR SHALL be returned.
2. If appending the received ScheduleStruct to the pending list of Schedules would cause the total
number  of  pending  schedules  to  exceed  the  value  of  the  NumberOfSchedules  attribute,  a
response with the status code RESOURCE_EXHAUSTED SHALL be returned.
3. If appending the received ScheduleStruct to the pending list of Schedules would cause the total
number of pending schedules whose SystemMode field matches the appended schedule’s Sys
temMode field to exceed the value of the NumberOfSchedules field on the ScheduleTypeStruct
whose SystemMode field matches the appended schedule’s SystemMode field, a response with
the status code RESOURCE_EXHAUSTED SHALL be returned.
4. Otherwise, the write SHALL be pended until receipt of a commit request, and the attribute sta
tus SHALL be SUCCESS.
a. If the BuiltIn field is null:
i. If there is a ScheduleStruct in the current value with a matching ScheduleHandle field,
the BuiltIn field on the pending ScheduleStruct SHALL be set to the value of the BuiltIn
on the matching ScheduleStruct.
ii. Otherwise, the BuiltIn field on the pending ScheduleStruct SHALL be set to false.
On an attempt to commit, the status of this attribute SHALL be determined as follows:
1. For all existing schedules:
a. If, after applying all pending changes, the updated value of the Schedules attribute would
not contain a ScheduleStruct with a matching ScheduleHandle field, indicating the removal
of the ScheduleStruct, the server SHALL check for invalid removal of the ScheduleStruct:
i. If the BuiltIn field is true on the removed ScheduleStruct, the attribute status SHALL be
CONSTRAINT_ERROR.
ii. If  the  removed  ScheduleHandle  is  equal  to  the  value  of  the  ActiveScheduleHandle
attribute, the attribute status SHALL be INVALID_IN_STATE.
2. Otherwise, the attribute status SHALL be SUCCESS.
4.3.9.62. SetpointHoldExpiryTimestamp Attribute
If there is a known time when the TemperatureSetpointHold SHALL be cleared, this attribute
SHALL contain the timestamp in UTC indicating when that will happen. If there is no such known
time, this attribute SHALL be null.
If the TemperatureSetpointHold is set to SetpointHoldOff or the TemperatureSetpointHoldDuration
is set to null, this attribute SHALL be set to null indicating there is no hold on the Thermostat either
with or without a duration.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Thermostat Cluster, specifically the "SetpointRaiseLower" command. This command is designed to be sent from a client to a server, as indicated by the "Direction" field. The "Response" field marked as 'Y' suggests that the server is expected to send a response upon receiving this command. The "Access" field is marked as 'O', indicating that access to this command is optional. The "Conformance" field is marked with 'M', meaning that the "SetpointRaiseLower" command is mandatory within the Thermostat Cluster. This implies that any implementation of the Thermostat Cluster must support this command, ensuring its availability and functionality in all compliant devices.

* The table row describes a command within the Thermostat Cluster, specifically the "SetWeeklySchedule" command, which is identified by the ID '0x01'. This command is directed from the client to the server, and it requires a response ('Y'). The access level is mandatory ('M'), indicating that the command must be implemented. The conformance rule 'SCH' implies that the command is mandatory if the feature code 'SCH' (presumably representing a scheduling feature) is supported by the device. If the device supports the scheduling feature, it must implement the "SetWeeklySchedule" command; otherwise, the conformance rule does not apply, and the command may not be required.

* The table row describes a command within the Thermostat Cluster, specifically the "GetWeeklySchedule" command. This command is initiated by the client and directed towards the server, with an expected response of "GetWeeklyScheduleResponse." The access level for this command is optional, indicated by 'O'. The conformance rule 'SCH' implies that this command is mandatory if the feature 'SCH' (likely representing a scheduling feature) is supported by the device. If the device does not support the 'SCH' feature, the command is not required. This means that the implementation of the "GetWeeklySchedule" command depends on the presence of the scheduling feature within the device's capabilities.

* The table row describes a command within the Thermostat Cluster, specifically the "GetWeeklyScheduleResponse" command, which is directed from the server to the client. The command does not require a response, as indicated by 'Response': 'N'. The conformance rule for this command is 'SCH', meaning it is mandatory if the feature 'SCH' (likely representing a scheduling feature) is supported by the device. If the device supports the scheduling feature, it must implement this command; otherwise, the command is not required.

* The table row describes a command within the Thermostat Cluster, specifically the "ClearWeeklySchedule" command, which is identified by the ID '0x03'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning it must be implemented. The conformance rule 'SCH' indicates that the command is mandatory if the feature or condition represented by 'SCH' is supported. In this context, 'SCH' likely refers to a feature related to scheduling, such as a scheduling capability within the thermostat. Therefore, the "ClearWeeklySchedule" command must be implemented if the thermostat supports the scheduling feature.

* The table row describes a command within the Thermostat Cluster, specifically the "GetRelayStatusLog" command, which is directed from the client to the server and expects a "GetRelayStatusLogResponse" in return. The access level for this command is optional, indicated by 'O'. The conformance rule '[Zigbee]' means that the command is optional if the Zigbee feature is supported. In other words, if the device supports Zigbee, it may implement this command, but it is not required to do so.

* In the Thermostat Cluster, under the Commands section, the table row describes the command 'GetRelayStatusLogResponse' with an ID of '0x01'. This command is directed from the server to the client, as indicated by the direction 'client ⇐ server', and it does not require a response, as noted by 'Response': 'N'. The conformance rule 'GetRelayStatusLog' implies that the 'GetRelayStatusLogResponse' command is mandatory if the 'GetRelayStatusLog' feature is supported by the device. If the device does not support the 'GetRelayStatusLog' feature, then this command is not required. This conformance rule ensures that the command is implemented only when relevant to the device's capabilities.

* The table row describes a command within the Thermostat Cluster, specifically the "SetActiveScheduleRequest" command, which is identified by the ID '0x05'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required and has no dependencies. The conformance rule 'MSCH' suggests that the command is mandatory if the feature or condition 'MSCH' is supported. In this context, 'MSCH' likely refers to a specific feature or condition related to the Matter specification that, when present, necessitates the inclusion of this command. If 'MSCH' is not supported, the command is not required.

* In the Thermostat Cluster, the command 'SetActivePresetRequest' with ID '0x06' is a client-to-server command that requires a response ('Response': 'Y'). The access level for this command is optional ('Access': 'O'), meaning it is not required and has no dependencies. The conformance rule 'PRES' indicates that the command is mandatory if the feature 'PRES' is supported. If 'PRES' is not supported, the command is not required. This entry specifies that the command is conditionally mandatory based on the presence of the 'PRES' feature within the device's implementation.

4.3.10.1. SetpointRaiseLower Command

_Table parsed from section 'Commands':_

* In the Thermostat Cluster, within the Commands section, there is a command identified by the ID '0' named 'Mode', which utilizes the 'SetpointRaiseLowerModeEnum' type. The 'Constraint' for this command is described elsewhere in the documentation, indicating that its constraints are too complex to be summarized simply. The 'Conformance' for this command is marked as 'M', meaning it is mandatory. This implies that the 'Mode' command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, within the Commands section, there is an entry for a command identified by 'ID' 1, named 'Amount', which is of type 'int8' and has a constraint labeled as 'all'. The conformance rule for this command is 'M', indicating that it is mandatory. This means that the 'Amount' command must always be implemented and supported in any device or application that uses the Thermostat Cluster, without any conditions or exceptions.

4.3.10.1.1. Mode Field
The field SHALL specify which setpoints are to be adjusted.
4.3.10.1.1.1. Heat Value
If the server does not support the HEAT feature then it SHALL respond with INVALID_COMMAND. If
the server supports the AUTO feature and the resulting setpoint would be invalid solely due to Min
SetpointDeadBand then the Cooling setpoint SHALL be increased sufficiently to maintain the dead
band.
4.3.10.1.1.2. Cool Value
If the server does not support the COOL feature then it SHALL respond with INVALID_COMMAND.
If the server supports the AUTO feature and the resulting setpoint would be invalid solely due to
MinSetpointDeadBand then the Heating setpoint SHALL be decreased sufficiently to maintain the
deadband.
4.3.10.1.1.3. Both Value
The client MAY indicate Both regardless of the server feature support. The server SHALL only
adjust the setpoint that it supports and not respond with an error.
4.3.10.1.2. Amount Field
This field SHALL indicate the amount (possibly negative) that should be added to the setpoint(s), in
steps of 0.1°C.
4.3.10.1.3. Effect on Receipt
Upon receipt, the attributes for the indicated setpoint(s) SHALL have the amount specified in the
Amount field added to them. If the resulting value is outside the limits imposed by MinCoolSet
pointLimit, MaxCoolSetpointLimit, MinHeatSetpointLimit and MaxHeatSetpointLimit, the value is
clamped to those limits. This is not considered an error condition.
4.3.10.2. SetWeeklySchedule Command
This command is used to update the thermostat weekly setpoint schedule from a management sys
tem. If the thermostat already has a weekly setpoint schedule programmed, then it SHOULD replace
each daily setpoint set as it receives the updates from the management system. For example, if the
thermostat has 4 setpoints for every day of the week and is sent a SetWeeklySchedule command
with one setpoint for Saturday then the thermostat SHOULD remove all 4 setpoints for Saturday
and replace those with the updated setpoint but leave all other days unchanged. If the schedule is
larger than what fits in one frame or contains more than 10 transitions, the schedule SHALL then
be sent using multiple SetWeeklySchedule Commands.

_Table parsed from section 'Commands':_

* The table row describes a command within the Thermostat Cluster, specifically identified as 'NumberOfTransitionsForSequence' with an ID of '0'. This command is of type 'uint8', indicating it uses an 8-bit unsigned integer for its data representation, and it applies to all instances of the cluster, as denoted by the 'Constraint' being 'all'. The 'Conformance' field is marked as 'M', which means this command is mandatory. Therefore, it is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the context of the Thermostat Cluster, specifically within the Commands section, the table row describes a command identified as 'DayOfWeekForSequence'. This command uses the 'ScheduleDayOfWeekBitmap' type and has constraints that are detailed elsewhere in the documentation. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'DayOfWeekForSequence' command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, under the Commands section, the entry for 'ModeForSequence' with ID '2' is defined as having a type of 'ScheduleModeBitmap'. The 'Constraint' for this entry is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' for 'ModeForSequence' is marked as 'M', which means that this command is mandatory. Therefore, any implementation of the Thermostat Cluster must include the 'ModeForSequence' command as a required element, ensuring it is always supported and available in the system.

_Table parsed from section 'Commands':_

* In the Thermostat Cluster, within the Commands section, there is an entry for a command named "Transitions" with an ID of '3'. This command is of the type 'list[WeeklyScheduleTransitionStruct]' and is constrained to a maximum of 10 entries. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "Transitions" command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.10.2.1. NumberOfTransitionsForSequence Field
This field SHALL indicate how many individual transitions to expect for this sequence of com
mands. If a device supports more than 10 transitions in its schedule they can send this by sending
more than 1 “Set Weekly Schedule” command, each containing the separate information that the
device needs to set.
4.3.10.2.2. DayOfWeekForSequence Field
This field SHALL represent the day of the week at which all the transitions within the payload of
the command SHOULD be associated to. This field is a bitmap and therefore the associated setpoint
could overlap onto multiple days (you could set one transition time for all “week days” or whatever
combination of days the implementation requests).
Each setpoint transition will begin with the day of week for this transition. There can be up to 10
transitions for each command.
4.3.10.2.3. ModeForSequence Field
This field SHALL indicate how the application decodes the setpoint fields of each transition in the
Transitions list.
If the HeatSetpointPresent bit is On, the HeatSetpoint field SHALL NOT be null in every entry of the
Transitions list.
If the HeatSetpointPresent bit is Off, the HeatSetpoint field SHALL be null in every entry of the
Transitions list.
If the CoolSetpointPresent bit is On, the CoolSetpoint field SHALL NOT be null in every entry of the
Transitions list.
If the CoolSetpointPresent bit is Off, the CoolSetpoint field SHALL be null in every entry of the Tran
sitions list.
At least one of the bits in the Mode For Sequence byte SHALL be on.
Both bits must be respected, even if the HEAT or COOL feature is not supported, to ensure the com
mand is decoded and handled correctly.
4.3.10.2.4. Transitions Field
This field SHALL contain the list of setpoint transitions used to update the specified daily schedules
4.3.10.2.5. Effect on Receipt
Upon receipt, the weekly schedule for updating setpoints SHALL be stored in the thermostat and
SHOULD begin at the time of receipt. A status code SHALL be sent in response.
When a command is received that requires a total number of transitions greater than the device
supports, the status of the response SHALL be INSUFFICIENT_SPACE.
When any of the setpoints sent in the sequence is out of range (AbsMin/MaxSetPointLimit), or when
the Mode for Sequence field includes a mode not supported by the device, the status of the response
SHALL be CONSTRAINT_ERROR and no setpoints from the entire sequence SHOULD be used.
When an overlapping transition is detected, the status of the response SHALL be FAILURE.
When a device which does not support multiple days in a command receives a command with more
than one bit set in the DayOfWeekForSequence field, or when a device which does not support mul
tiple modes in a command receives a command with more than one bit set in the ModeForSequence
field, or when the contents of the Transitions field does not agree with NumberOfTransitionsForSe
quence,  DayOfWeekForSequence  or  ModeForSequence,  the  status  of  the  response  SHALL  be
INVALID_COMMAND.
When the transitions could be added successfully, the status of the response SHALL be SUCCESS.
4.3.10.3. GetWeeklySchedule Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Thermostat Cluster, specifically the "DaysToReturn" command. This command is identified by the ID '0' and utilizes the data type 'ScheduleDayOfWeekBitmap'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M', which means that the "DaysToReturn" command is mandatory. This implies that any implementation of the Thermostat Cluster must include this command, as it is always required according to the Matter specification.

* In the context of the Thermostat Cluster, specifically within the Commands section, the table row describes a command identified as 'ModeToReturn' with an ID of '1'. This command is of the type 'ScheduleModeBitmap', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'ModeToReturn' is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.10.3.1. DaysToReturn Field
This field SHALL indicate the number of days the client would like to return the setpoint values for
and could be any combination of single days or the entire week.
4.3.10.3.2. ModeToReturn Field
This field SHALL indicate the mode the client would like to return the set point values for and could
be any combination of heat only, cool only or heat & cool.
4.3.10.3.3. Effect on Receipt
Upon receipt, the unit SHOULD send in return the Get Weekly Schedule Response command. The
Days to Return and Mode to Return fields are defined as bitmask for the flexibility to support multi
ple days and multiple modes within one command. If thermostat cannot handle incoming com
mand with multiple days and/or multiple modes within one command, it SHALL send default
response of INVALID_COMMAND in return.
4.3.10.4. GetWeeklyScheduleResponse Command
This command has the same payload format as the Set Weekly Schedule.

_Table parsed from section 'Commands':_

* In the context of the Thermostat Cluster, specifically within the Commands section, the table row describes an element with the ID '0' named 'NumberOfTransitionsForSequence'. This element is of type 'uint8', which indicates it is an 8-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'NumberOfTransitionsForSequence' command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* The table row describes a command within the Thermostat Cluster, specifically named "DayOfWeekForSequence," which is identified by the ID '1' and uses the type 'ScheduleDayOfWeekBitmap.' The 'Constraint' field is marked as 'desc,' indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M,' signifying that this command is mandatory. This means that the "DayOfWeekForSequence" command must always be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, within the Commands section, the entry for 'ModeForSequence' is identified by ID '2' and is of the type 'ScheduleModeBitmap'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', which means that the 'ModeForSequence' command is mandatory. This implies that any implementation of the Thermostat Cluster must include this command, as it is always required according to the Matter specification.

* In the Thermostat Cluster, under the Commands section, there is an entry for a command named "Transitions" with an ID of '3'. This command is of the type 'list[WeeklyScheduleTransitionStruct]' and is constrained to a maximum of 10 items. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Transitions" command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.10.5. ClearWeeklySchedule Command
This command is used to clear the weekly schedule. The Clear weekly schedule has no payload.
Upon receipt, all transitions currently stored SHALL be cleared and a default response of SUCCESS
SHALL be sent in response. There are no error responses to this command.
4.3.10.6. GetRelayStatusLog Command
This command is used to query the thermostat internal relay status log. This command has no pay
load.
Upon receipt, the unit SHALL respond with Relay Status Log command if the relay status log feature
is supported on the unit.
The log storing order is First in First Out (FIFO) when the log is generated and stored into the
Queue.
The first record in the log (i.e., the oldest) one, is the first to be replaced when there is a new record
and there is no more space in the log. Thus, the newest record will overwrite the oldest one if there
is no space left.
The log storing order is Last In First Out (LIFO) when the log is being retrieved from the Queue by a
client device.
Once the "Get Relay Status Log Response" frame is sent by the Server, the "Unread Entries" attribute
SHOULD be decremented to indicate the number of unread records that remain in the queue.
If the "Unread Entries" attribute reaches zero and the Client sends a new "Get Relay Status Log
Request", the Server MAY send one of the following items as a response:
i. Resend the last Get Relay Status Log Response
or
ii. Generate new log record at the time of request and send Get Relay Status Log Response with the
new data
For both cases, the "Unread Entries" attribute will remain zero.
4.3.10.7. GetRelayStatusLogResponse Command
This command is sent from the thermostat cluster server in response to the Get Relay Status Log.
After the Relay Status Entry is sent over the air to the requesting client, the specific entry will be
cleared from the thermostat internal log.

_Table parsed from section 'Commands':_

* In the Thermostat Cluster's Commands section, the table row describes an element with the ID '0' named 'TimeOfDay', which is of type 'uint16' and constrained to a maximum value of 1439. The 'Conformance' field is marked as 'M', indicating that this element is mandatory. This means that the 'TimeOfDay' command must always be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions. The mandatory status ensures that this command is a fundamental part of the cluster's functionality.

* The table row describes a command within the Thermostat Cluster, specifically the "RelayStatus" command. This command is of the type "RelayStateBit map" and has constraints that are detailed elsewhere in the documentation, as indicated by "desc" in the Constraint column. The Conformance column is marked with "M," which means that the "RelayStatus" command is mandatory. This implies that any implementation of the Thermostat Cluster must include this command, as it is always required according to the Matter specification.

* In the context of the Thermostat Cluster, the table row describes a command identified as 'LocalTemperature' with an ID of '2'. This command is of the 'temperature' type and is applicable to all constraints. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', which means that the 'LocalTemperature' command is mandatory and must always be implemented in any device or system that supports the Thermostat Cluster. This requirement is unconditional and does not depend on any other features or conditions.

* In the Thermostat Cluster, under the Commands section, the entry for 'HumidityInPercentage' is identified by ID '3' and is of type 'uint8', constrained to values between 0% and 100%. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. However, the 'Conformance' is marked as 'M', meaning that, according to the Matter specification, the 'HumidityInPercentage' command is mandatory and must always be implemented. Despite the disallowed quality, the conformance rule dictates that this command is a required component of the Thermostat Cluster, ensuring that devices supporting this cluster must include this command to be compliant with the specification.

* The table row describes a command within the Thermostat Cluster, specifically the "SetPoint" command, which is of the type "temperature" and applies to all constraints. The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "SetPoint" command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

* In the Thermostat Cluster, within the Commands section, the table row describes a command identified by the ID '5' and named 'UnreadEntries'. This command is of the type 'uint16', indicating it uses a 16-bit unsigned integer. The constraint 'all' suggests that this command applies universally within its context. The conformance rule for 'UnreadEntries' is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.10.7.1. TimeOfDay Field
This field SHALL indicate the sample time of the day, in minutes since midnight, when the relay sta
tus was captured for this associated log entry. For example, 6am will be represented by 360 minutes
since midnight and 11:30pm will be represented by 1410 minutes since midnight.
4.3.10.7.2. RelayStatus Field
This field SHALL indicate the relay status for thermostat when the log is captured. Each bit repre
sents one relay used by the thermostat. If the bit is on, the associated relay is on and active. Each
thermostat manufacturer can create its own mapping between the bitmap and the associated relay.
4.3.10.7.3. LocalTemperature Field
This field SHALL indicate the LocalTemperature when the log is captured. The null value indicates
that LocalTemperature was invalid or unavailable.
4.3.10.7.4. Humidity Field
This field SHALL indicate the humidity as a percentage when the log was captured. The null value
indicates that the humidity value was invalid or unknown.
4.3.10.7.5. Setpoint Field
This field SHALL indicate the target setpoint temperature when the log is captured.
4.3.10.7.6. UnreadEntries Field
This field SHALL indicate the number of unread entries within the thermostat internal log system.
4.3.10.8. SetActiveScheduleRequest Command

_Table parsed from section 'Commands':_

* In the Thermostat Cluster, under the Commands section, the entry for 'ScheduleHandle' is identified by the ID '0' and is of type 'octstr' with a constraint of a maximum length of 16 characters. The conformance rule for 'ScheduleHandle' is marked as 'M', which stands for Mandatory. This means that the 'ScheduleHandle' command is always required to be implemented in any device or application that supports the Thermostat Cluster, without any conditions or exceptions.

4.3.10.8.1. ScheduleHandle Field
This field SHALL specify the value of the ScheduleHandle field on the ScheduleStruct to be made
active.
4.3.10.8.2. Effect on Receipt
Upon receipt, if the Schedules attribute contains a ScheduleStruct whose ScheduleHandle field
matches the value of the ScheduleHandle field, the server SHALL set the thermostat’s ActiveSched
uleHandle attribute to the value of the ScheduleHandle field.
Otherwise, the server SHALL return a status code of INVALID_COMMAND.
4.3.10.9. SetActivePresetRequest Command

_Table parsed from section 'Commands':_

* In the Thermostat Cluster's Commands section, the table row describes a command identified by 'ID' 0, named 'PresetHandle'. This command is of type 'octstr' (octet string) with a constraint limiting its maximum length to 16. The 'Quality' field is marked as 'X', indicating that this command is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', meaning that the 'PresetHandle' command is mandatory and always required within the context of the Thermostat Cluster, regardless of any other conditions or features.

4.3.10.9.1. PresetHandle Field
This field SHALL specify the value of the PresetHandle field on the PresetStruct to be made active. If
the field is set to null, that indicates there should be no active preset.
4.3.10.9.2. Effect on Receipt
Upon receipt of this command,
1. If the PresetHandle field is null, the server SHALL clear the ActivePresetHandle attribute by set
ting it to null.
2. Otherwise,
a. If this command is received with a PresetHandle such that the Presets attribute does not
contain a PresetStruct whose PresetHandle field matches the value of the PresetHandle, the
server SHALL return a status code of INVALID_COMMAND.
b. The server SHALL set the ActivePresetHandle attribute to the value of the PresetHandle
field.
3. The server SHALL return a status code of SUCCESS.