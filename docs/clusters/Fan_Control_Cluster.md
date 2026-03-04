
# 4.4 Fan Control Cluster

This cluster specifies an interface to control the speed of a fan.

## Data Types
4.4.5.1. RockBitmap Type

_Table parsed from section 'Data Types':_

* In the context of the Fan Control Cluster, specifically within the Data Types section, the table entry for the 'Bit' labeled '0' with the 'Name' 'RockLeftRight' is designed to indicate the feature of rocking a fan left to right. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'RockLeftRight' feature is always required to be implemented in any device or system that supports the Fan Control Cluster according to the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental part of the cluster's functionality.

* In the Fan Control Cluster, within the Data Types section, the table row describes a feature named "RockUpDown," which is represented by the bit value '1' and serves to indicate the rock up and down functionality. The conformance rule for this feature is marked as 'M,' which stands for Mandatory. This means that the "RockUpDown" feature is always required to be implemented in any device or application that supports the Fan Control Cluster, without any conditions or exceptions.

* In the context of the Fan Control Cluster, specifically within the Data Types section, the table row describes a data element with the bit position '2', named 'RockRound', which serves the purpose of indicating a "rock around" feature. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'RockRound' feature is always required to be implemented in any device or application that supports the Fan Control Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the cluster.

4.4.5.2. WindBitmap Type

_Table parsed from section 'Data Types':_

* In the Fan Control Cluster, under the Data Types section, the table row describes a feature named 'SleepWind', which is associated with the bit position '0'. This feature is summarized as indicating sleep wind. According to the conformance rule 'M', 'SleepWind' is a mandatory element. This means that it is always required to be implemented in any device or application that supports the Fan Control Cluster, without any conditions or exceptions.

* In the context of the Fan Control Cluster, within the Data Types section, the table entry describes a feature named "NaturalWind," which is represented by the bit value '1'. This feature is summarized as indicating "natural wind." According to the conformance rule 'M', this feature is mandatory, meaning it is always required to be implemented in any device or application that supports the Fan Control Cluster. There are no conditions or dependencies affecting its requirement; it must be included as part of the standard implementation.

4.4.5.2.1. SleepWind Value
The fan speed, based on current settings, SHALL gradually slow down to a final minimum speed.
For this process, the sequence, speeds and duration are MS.
4.4.5.2.2. NaturalWind Value
The fan speed SHALL vary to emulate natural wind. For this setting, the sequence, speeds and dura
tion are MS.
4.4.5.3. StepDirectionEnum Type

_Table parsed from section 'Data Types':_

* In the context of the Fan Control Cluster, within the Data Types section, the table row describes a data type with the value '0' named 'Increase'. This data type is summarized as representing a step that moves in the increasing direction. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Increase' data type is always required to be implemented in any device or application that supports the Fan Control Cluster, without any conditions or exceptions.

* In the context of the Fan Control Cluster, specifically within the Data Types section, the table entry describes a data type with the value '1' named 'Decrease'. This data type is summarized as representing a step that moves in a decreasing direction. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Decrease' data type is a required element in the Fan Control Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

4.4.5.4. AirflowDirectionEnum Type

_Table parsed from section 'Data Types':_

* In the Fan Control Cluster, under the Data Types section, there is an entry for a data type with the value '0' named 'Forward'. This entry indicates that the airflow is in the forward direction. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Forward' data type is always required to be implemented in any device or application that supports the Fan Control Cluster, without any conditions or exceptions.

* In the context of the Fan Control Cluster's Data Types, the table row describes a feature named "Reverse," which is assigned a value of '1' and is summarized as indicating that airflow is in the reverse direction. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the "Reverse" feature is always required to be implemented in any device or application that supports the Fan Control Cluster according to the Matter IoT specification. There are no conditions or dependencies that alter this requirement; it is an absolute necessity for compliance.

4.4.5.5. FanModeEnum Type

_Table parsed from section 'Data Types':_

* In the context of the Fan Control Cluster, within the Data Types section, the table row describes a data entry with the value '0', named 'Off', which indicates that the fan is off. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that the 'Off' state, represented by the value '0', must always be supported and implemented in any device or application that adheres to the Matter specification for the Fan Control Cluster. There are no conditions or exceptions; the 'Off' state is a required feature.

* In the context of the Fan Control Cluster, specifically within the Data Types section, the table row describes a data type with the value '1', named 'Low', which represents the fan operating at a low speed. The conformance for this entry is marked as 'desc', indicating that the conformance requirements for this element are too complex to be captured by a simple tag or expression. Instead, the specific conditions or rules governing its use are detailed elsewhere in the documentation. This means that to fully understand when and how this 'Low' speed setting should be implemented or supported, one must refer to the additional descriptive information provided in the broader documentation.

* In the Fan Control Cluster, under the Data Types section, the entry for 'Medium' with a value of '2' represents a fan operating at medium speed. The conformance rule for this entry is marked as 'desc', indicating that the conformance requirements for this feature are too complex to be captured by a simple tag or expression. Instead, the specific conditions or rules governing its implementation are detailed elsewhere in the documentation. This means that to fully understand when and how the 'Medium' speed setting should be applied, one would need to refer to the additional descriptive information provided in the broader Matter specification documentation.

* In the context of the Fan Control Cluster's Data Types, the table row describes a data type entry with the value '3', named 'High', which signifies that the fan is operating at a high speed. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'High' speed setting is a required element in the implementation of the Fan Control Cluster. Any device or application that supports this cluster must include the 'High' speed setting as part of its functionality, ensuring consistent behavior across all implementations that adhere to the Matter specification.

* In the context of the Fan Control Cluster's Data Types, the table row entry describes a data type with the value '4' and the name 'On'. The conformance rule for this entry is 'D', which stands for Deprecated. This means that the 'On' data type is considered obsolete in the current Matter specification and should not be used in new implementations. Existing implementations that use this data type should plan to transition away from it, as it may be removed in future versions of the specification.

* In the context of the Fan Control Cluster, specifically within the Data Types section, the table row describes a data type with the value '5' named 'Auto', which indicates that the fan is operating in automatic mode. The conformance rule for this entry is 'AUT', which implies that the presence and implementation of this data type are contingent upon the support of the 'AUT' feature. If the 'AUT' feature is supported, this data type becomes mandatory. If the 'AUT' feature is not supported, the data type is not required. This conformance rule ensures that the 'Auto' mode is only implemented when the relevant feature is available, maintaining consistency and relevance within the device's capabilities.

* In the context of the Fan Control Cluster, within the Data Types section, the table row describes a data type with the value '6', named 'Smart', which indicates that the fan is operating in a smart mode. The conformance rule for this entry is 'D', which stands for Deprecated. This means that the 'Smart' mode is considered obsolete in the current Matter specification and should not be used in new implementations. It is likely retained for backward compatibility or reference purposes, but developers are discouraged from relying on it for future designs.

4.4.5.5.1. Low Value
If the fan supports 2 or more speeds, the Low value SHALL be supported.
The Low value SHALL be supported if and only if the FanModeSequence attribute value is less than
4.
4.4.5.5.2. Medium Value
If the fan supports 3 or more speeds, the Medium value SHALL be supported.
The Medium value SHALL be supported if and only if the FanModeSequence attribute value is 0 or
2.
4.4.5.6. FanModeSequenceEnum Type

_Table parsed from section 'Data Types':_

* In the Fan Control Cluster, under the Data Types section, the entry for 'OffLowMedHigh' with a value of '0' indicates that the fan is capable of operating in off, low, medium, and high modes. The conformance rule '[!AUT].a' specifies that this feature is optional if the condition '!AUT' is true, meaning it is optional if the 'AUT' feature is not supported. The '.a' suffix suggests that further details or conditions might be described elsewhere in the documentation. This entry allows for flexibility in implementation based on the presence or absence of the 'AUT' feature.

* In the Fan Control Cluster, within the Data Types section, the table row describes an entry named "OffLowHigh" with a value of '1'. This entry indicates that the fan is capable of operating in off, low, and high modes. The conformance rule for "OffLowHigh" is specified as `[!AUT].a`. According to the conformance interpretation guide, this means that the "OffLowHigh" feature is optional if the condition `!AUT` is true, where `AUT` likely represents a feature code. Therefore, if the `AUT` feature is not supported, the "OffLowHigh" capability is optional. The `.a` suffix suggests there might be additional context or details provided elsewhere in the documentation regarding this conformance condition.

* In the Fan Control Cluster, under the Data Types section, the entry 'OffLowMedHighAuto' with a value of '2' indicates that the fan is capable of operating in off, low, medium, high, and auto modes. The conformance rule '[AUT].a' specifies that this feature is optional if the condition 'AUT' is true, meaning that if the 'AUT' feature is supported, the 'OffLowMedHighAuto' capability can be included but is not required. The use of brackets around 'AUT' indicates the optional nature of this feature under the specified condition.

* In the Fan Control Cluster, under the Data Types section, the entry for 'OffLowHighAuto' with a value of '3' indicates that the fan is capable of operating in off, low, high, and auto modes. The conformance rule '[AUT].a' specifies that this feature is optional if the condition 'AUT' is true, meaning that if the 'AUT' feature is supported, the 'OffLowHighAuto' mode can be included but is not required. The use of brackets around 'AUT' indicates that the inclusion of this feature is conditional and not mandatory.

* In the Fan Control Cluster, under the Data Types section, the entry for 'OffHighAuto' with a value of '4' indicates that the fan is capable of operating in off, high, and auto modes. The conformance rule '[AUT].a' specifies that this feature is optional if the condition 'AUT' is true. This means that if the 'AUT' feature is supported, the 'OffHighAuto' capability can be included, but it is not mandatory. The use of brackets around 'AUT' indicates that the inclusion of this feature is conditional and not required unless the specified condition is met.

* In the Fan Control Cluster, under the Data Types section, the entry labeled 'OffHigh' with a value of '5' indicates that the fan is capable of operating in both off and high modes. The conformance rule '[!AUT].a' specifies that this feature is optional if the 'AUT' feature is not supported. The use of brackets around '!AUT' indicates that the optionality is conditional; specifically, the feature becomes optional only when the 'AUT' feature is absent. If 'AUT' is supported, the condition does not apply, and the entry is not required.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Fan Control Cluster, specifically the 'FanMode' attribute. This attribute is identified by the ID '0x0000' and is of the type 'FanModeEnum'. It is applicable to all devices within this cluster ('Constraint': 'all'), and its default value is set to '0'. The 'FanMode' attribute has read and write access, with the ability to be updated by the device itself ('Access': 'RW VO'). The 'Quality' field marked as 'N' indicates no specific quality constraints. The conformance rule for this attribute is 'M', meaning that the 'FanMode' attribute is mandatory and must always be implemented in any device that supports the Fan Control Cluster.

* The table row describes an attribute within the Fan Control Cluster, specifically the "FanModeSequence" attribute. This attribute is identified by the ID `0x0001` and is of the type `FanModeSequenceEnum`, which suggests it enumerates different sequences for fan modes. The constraint "all" indicates that all possible values of this enumeration are applicable. The quality "N" implies that this attribute does not have a specific quality requirement, and the default value is set to "MS". The access specification `R[W] VO` indicates that the attribute is readable and optionally writable, with volatile access. The conformance rule "Zigbee" implies that the requirement for this attribute is defined by its compatibility with Zigbee standards, suggesting that its implementation is mandatory or optional based on Zigbee's specifications rather than the Matter specification itself.

* The table row describes an attribute within the Fan Control Cluster, specifically the "FanModeSequence" attribute, identified by the ID '0x0001'. This attribute is of the type 'FanModeSequenceEnum' and applies to all instances of the cluster, as indicated by the constraint 'all'. The quality 'F' suggests it is a fundamental attribute, with a default value of 'MS'. The access rights 'R V' imply that the attribute can be read and is volatile. The conformance rule 'M' indicates that the "FanModeSequence" attribute is mandatory, meaning it is always required to be implemented in any device that supports the Fan Control Cluster, without any conditions or exceptions.

* In the Fan Control Cluster, within the Attributes section, the table row describes the attribute 'PercentSetting' with an ID of '0x0002'. This attribute is of the 'percent' type and is constrained to a maximum value of 100. It has a default value of 0 and allows read and write access with volatile (VO) quality. The conformance rule for 'PercentSetting' is marked as 'M', indicating that this attribute is mandatory. This means that it is always required to be implemented in any device or application that supports the Fan Control Cluster, without any conditions or exceptions.

* In the Fan Control Cluster, within the Attributes section, the table row describes an attribute named "PercentCurrent" with an ID of '0x0003'. This attribute is of the type 'percent' and is constrained to a maximum value of 100. The default value is described elsewhere in the documentation, as indicated by 'desc'. The access level for this attribute is 'R V', meaning it is readable and has volatile characteristics. The conformance rule 'M' signifies that the "PercentCurrent" attribute is mandatory, meaning it is always required to be implemented in any device or application using this cluster, without any conditions or exceptions.

* The table row describes an attribute within the Fan Control Cluster, specifically the "SpeedMax" attribute. This attribute has an ID of '0x0004' and is of type 'uint8', constrained to values between 1 and 100. It is marked with a quality of 'F', has a default value of 'MS', and access rights of 'R V', indicating it is readable and has a volatile nature. The conformance rule 'SPD' indicates that the "SpeedMax" attribute is mandatory if the feature 'SPD' (likely representing a specific speed-related feature within the Fan Control Cluster) is supported. If 'SPD' is not supported, the conformance rule does not apply, implying that the attribute may not be required.

_Table parsed from section 'Attributes':_

* In the Fan Control Cluster, within the Attributes section, the 'SpeedSetting' attribute is identified by the ID '0x0005' and is of type 'uint8'. It is constrained by a maximum value defined by 'SpeedMax', with a default value of '0'. The access level for this attribute is read-write and volatile ('RW VO'), meaning it can be read and modified, and its value may change without notice. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in some contexts. The conformance rule 'SPD' signifies that the 'SpeedSetting' attribute is mandatory if the feature 'SPD' (presumably a feature related to speed control) is supported. If 'SPD' is not supported, the attribute is not required.

* The table row describes an attribute named "SpeedCurrent" within the Fan Control Cluster. This attribute has an ID of '0x0006' and is of type 'uint8', with a constraint that its value should not exceed 'SpeedMax'. The quality of this attribute is marked as 'Provisional' (P), indicating that its status is temporary and may change in future specifications. The default value is described elsewhere in the documentation ('desc'), and it has read and view access ('R V'). The conformance rule 'SPD' means that the "SpeedCurrent" attribute is mandatory if the feature 'SPD' is supported. If the 'SPD' feature is not supported, the attribute is not required.

* The table row describes an attribute named "RockSupport" within the Fan Control Cluster, identified by the ID '0x0007'. This attribute is of the type 'RockBitmap' and has a constraint that is described elsewhere in the documentation. It is a feature-quality attribute ('F') with a default value of '0', and it has read and view access ('R V'). The conformance rule 'RCK' indicates that the "RockSupport" attribute is mandatory if the feature 'RCK' is supported. If 'RCK' is not supported, the attribute is not required. This means that the presence of the "RockSupport" attribute is contingent upon the support of the 'RCK' feature within the device or implementation.

* The table row describes an attribute named "RockSetting" within the Fan Control Cluster, identified by the ID '0x0008'. This attribute is of the type 'RockBitmap' and has constraints that are described elsewhere in the documentation. It is provisionally marked with a quality status of 'P', indicating that its status is temporary and may change in the future. The default value for this attribute is '0', and it has read-write access with volatile (VO) characteristics, meaning changes may not persist across device reboots. The conformance rule 'RCK' indicates that the "RockSetting" attribute is mandatory if the feature or condition represented by 'RCK' is supported. If 'RCK' is not supported, the attribute is not required.

* The table row describes an attribute named "WindSupport" within the Fan Control Cluster, identified by the ID '0x0009'. This attribute is of type 'WindBitmap' and has a default value of '0'. It is constrained by a description found elsewhere in the documentation, indicated by 'desc'. The attribute is of quality 'F', which typically denotes a specific feature or functionality, and it has read and view access permissions, as indicated by 'R V'. The conformance rule 'WND' implies that the "WindSupport" attribute is mandatory if the feature 'WND' is supported by the device. If 'WND' is not supported, the attribute is not required. This means that the presence of this attribute is contingent upon the support for the 'WND' feature within the device's implementation.

* In the Fan Control Cluster, under the Attributes section, the entry for 'WindSetting' with ID '0x000A' is of type 'WindBitmap' and has a constraint described elsewhere in the documentation. It is provisionally marked with a quality of 'P', indicating that its status is temporary and may change in future specifications. The default value for this attribute is '0', and it has read-write access with volatile (VO) quality, meaning it can be modified and may change without notice. The conformance rule 'WND' specifies that this attribute is mandatory if the feature 'WND' is supported. If 'WND' is not supported, the attribute is not required.

* The table row describes an attribute named "AirflowDirection" within the Fan Control Cluster. This attribute is identified by the ID '0x000B' and is of the type 'AirflowDirectionEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is 'P', meaning it is provisional and may change in the future. The default value for this attribute is '0', and it has 'RW VO' access, which means it is readable and writable, with the ability to be overridden. The 'Conformance' field is 'DIR', which implies that the conformance requirements for this attribute are described in more detail elsewhere in the documentation, as 'DIR' does not match any basic conformance tags or logical conditions directly. This suggests that the specific conditions under which this attribute is required are complex and need to be referenced from additional documentation.

4.4.6.1. FanMode Attribute
This attribute SHALL indicate the current speed mode of the fan. This attribute MAY be written by
the client to request a different fan mode. A server SHALL return INVALID_IN_STATE to indicate
that the fan is not in a state where the FanMode can be changed to the requested value. A server
MAY have FanMode values that it can never be set to. For example, where this cluster appears on
the same or another endpoint as other clusters with a system dependency, for example the Thermo
stat cluster, attempting to set the FanMode attribute of this cluster to Off may not be allowed by the
system.
This attribute SHALL be set to one of the values in FanModeEnum.
When the FanMode attribute is successfully written to, the PercentSetting and SpeedSetting (if
present) attributes SHALL be set to appropriate values, as defined by the Section 4.4.6.3.1 and Sec
tion 4.4.6.6.1 respectively, unless otherwise specified below.
When the FanMode attribute is set to any given mode, the PercentCurrent and SpeedCurrent (if
present) SHALL indicate the actual currently operating fan speed, unless otherwise specified below.
4.4.6.1.1. Off Value
Setting the attribute value to Off SHALL set the values of these attributes to 0 (zero):
• PercentSetting
• PercentCurrent
• SpeedSetting (if present)
• SpeedCurrent (if present)
4.4.6.1.2. Auto Value
Setting the attribute value to Auto SHALL set the values of these attributes to null:
• PercentSetting
• SpeedSetting (if present)
These attributes SHALL continue to indicate the current state of the fan while this attribute value is
Auto:
• PercentCurrent
• SpeedCurrent (if present)
4.4.6.1.3. On Value
If a client attempts to write a value of On, the attribute SHALL be set to High.
4.4.6.1.4. Smart Value
If a client attempts to write a value of Smart and the AUT feature is supported, the attribute SHALL
be set to Auto, otherwise the attribute SHALL be set to High.
4.4.6.2. FanModeSequence Attribute
This attribute indicates the fan speed ranges that SHALL be supported.
4.4.6.3. PercentSetting Attribute
This attribute SHALL indicate the speed setting for the fan. This attribute MAY be written by the
client to indicate a new fan speed. If the client writes null to this attribute, the attribute value
SHALL NOT change. A server SHALL return INVALID_IN_STATE to indicate that the fan is not in a
state where the PercentSetting can be changed to the requested value.
If this is successfully written to 0, the server SHALL set the FanMode attribute value to Off.
4.4.6.3.1. Percent Rules
It is up to the server implementation to map between ranges of the PercentSetting attribute and
FanMode attribute enumerated values. Percent values are split into ranges, each range correspond
ing to a supported FanMode attribute value. Percent ranges SHALL NOT overlap. All percent values
in the High speed range SHALL be higher than all percent values in the Medium and Low speed
ranges, if supported. All percent values in the Medium speed range SHALL be higher than all per
cent values in the Low speed range. If the client sets the FanMode attribute to Low, Medium or
High, the server SHALL set the PercentSetting attribute to a value within the corresponding range.
If the client sets the PercentSetting attribute, the server SHALL set the FanMode attribute to Low,
Medium or High, based on the percent value being in the corresponding range.
If the MultiSpeed feature is supported, the calculation of SpeedSetting or SpeedCurrent (speed)
from a percent value change for PercentSetting or PercentCurrent respectively (percent) SHALL
hold true:
• speed = ceil( SpeedMax * (percent * 0.01) )
For example: If the SpeedMax attribute is 42 (42 speed fan) and PercentSetting is changed to
25, then SpeedSetting and SpeedCurrent become 11 (rounding up 10.5).
4.4.6.4. PercentCurrent Attribute
This attribute SHALL indicate the actual currently operating fan speed, or zero to indicate that the
fan is off. There MAY be a temporary mismatch between the value of this attribute and the value of
the PercentSetting attribute due to other system requirements that would not allow the fan to oper
ate at the requested setting. See Section 4.4.6.3.1 for more details.
4.4.6.5. SpeedMax Attribute
This attribute SHALL indicate that the fan has one speed (value of 1) or the maximum speed, if the
fan is capable of multiple speeds.
4.4.6.6. SpeedSetting Attribute
This attribute SHALL indicate the speed setting for the fan. This attribute MAY be written by the
client to indicate a new fan speed. If the client writes null to this attribute, the attribute value
SHALL NOT change. A server SHALL return INVALID_IN_STATE to indicate that the fan is not in a
state where the SpeedSetting can be changed to the requested value.
If this is successfully written to 0, the server SHALL set the FanMode attribute value to Off. Please
see the Section 4.4.6.6.1 for details on other values.
4.4.6.6.1. Speed Rules
It is up to the server implementation to map between ranges of the SpeedSetting attribute and Fan
Mode attribute enumerated values. Speed values are split into ranges, each range corresponding to
a FanMode attribute value. Speed ranges SHALL NOT overlap. All speed values in the High speed
range SHALL be higher than all speed values in the Medium and Low speed ranges, if supported.
All speed values in the Medium speed range SHALL be higher than all speed values in the Low
speed range. If the client sets the FanMode attribute to Low, Medium or High, the server SHALL set
the SpeedSetting attribute to a value within the corresponding range. If the client sets the SpeedSet
ting attribute, the server SHALL set the FanMode attribute to Low, Medium or High, based on the
speed value being in the corresponding range.
This calculation for the value of PercentSetting or PercentCurrent (percent) from a speed value
change for SpeedSetting or SpeedCurrent respectively (speed) SHALL hold true:
• percent = floor( speed/SpeedMax * 100 )
For example: If the SpeedMax attribute is 42 (42 speed fan) and SpeedSetting attribute is
changed to 11, then PercentSetting and PercentCurrent become 26.
4.4.6.7. SpeedCurrent Attribute
This attribute SHALL indicate the actual currently operating fan speed, or zero to indicate that the
fan is off. There MAY be a temporary mismatch between the value of this attribute and the value of
the SpeedSetting attribute due to other system requirements that would not allow the fan to oper
ate at the requested setting.
4.4.6.8. RockSupport Attribute
This attribute is a bitmap that indicates what rocking motions the server supports.
4.4.6.9. RockSetting Attribute
This attribute is a bitmap that indicates the current active fan rocking motion settings. Each bit
SHALL only be set to 1, if the corresponding bit in the RockSupport attribute is set to 1, otherwise a
status code of CONSTRAINT_ERROR SHALL be returned.
If a combination of supported bits is set by the client, and the server does not support the combina
tion, the lowest supported single bit in the combination SHALL be set and active, and all other bits
SHALL indicate zero.
For example: If RockUpDown and RockRound are both set, but this combination is not possi
ble, then only RockUpDown becomes active.
4.4.6.10. WindSupport Attribute
This attribute is a bitmap that indicates what wind modes the server supports. At least one wind
mode bit SHALL be set.
4.4.6.11. WindSetting Attribute
This attribute is a bitmap that indicates the current active fan wind feature settings. Each bit SHALL
only be set to 1, if the corresponding bit in the WindSupport attribute is set to 1, otherwise a status
code of CONSTRAINT_ERROR SHALL be returned.
If a combination of supported bits is set by the client, and the server does not support the combina
tion, the lowest supported single bit in the combination SHALL be set and active, and all other bits
SHALL indicate zero.
For example: If Sleep Wind and Natural Wind are set, but this combination is not possible,
then only Sleep Wind becomes active.
4.4.6.12. AirflowDirection Attribute
This attribute SHALL indicate the current airflow direction of the fan. This attribute MAY be writ
ten by the client to indicate a new airflow direction for the fan. This attribute SHALL be set to one
of the values in the AirflowDirectionEnum table.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Fan Control Cluster, specifically the "Step" command, which is identified by the ID '0x00'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'STEP', which, according to the guide, suggests that the command is mandatory if the feature or condition 'STEP' is supported. If 'STEP' is not supported, the conformance status is not explicitly defined in this entry, implying that further documentation may be needed to fully understand its conditional requirements.

4.4.7.1. Step Command
This command speeds up or slows down the fan, in steps, without the client having to know the fan
speed. This command supports, for example, a user operated wall switch, where the user provides
the feedback or control to stop sending this command when the proper speed is reached. The step
speed values are implementation specific. How many step speeds are implemented is implementa
tion specific.
This command supports these fields:

_Table parsed from section 'Commands':_

* In the Fan Control Cluster, within the Commands section, there is an entry for a command identified by 'ID' 0, named 'Direction'. This command is of the type 'StepDirectionEnum' and has a default value of 'Increase'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the 'Direction' command must always be implemented and supported in any device or application that utilizes the Fan Control Cluster, without any conditions or exceptions.

* In the Fan Control Cluster, within the Commands section, there is a command identified by ID '1' named 'Wrap'. This command is of the boolean type and has a default value of 'false'. The conformance rule for this command is marked as 'O', which stands for Optional. This means that the 'Wrap' command is not required to be implemented in devices that support the Fan Control Cluster, and there are no dependencies or conditions that affect its optional status. Implementers have the discretion to include or exclude this command based on their specific needs or design choices.

* In the Fan Control Cluster, within the Commands section, the table row describes a command identified by 'ID' 2, named 'LowestOff', which is of type 'bool' and has a default value of 'true'. The conformance rule for this command is 'O', indicating that it is optional. This means that the implementation of the 'LowestOff' command is not required and has no dependencies on other features or conditions. Devices or systems implementing the Fan Control Cluster can choose to include this command, but it is not mandatory for compliance with the Matter specification.

4.4.7.1.1. Direction Field
This field SHALL indicate whether the fan speed increases or decreases to the next step value.
4.4.7.1.2. Wrap Field
This field SHALL indicate if the fan speed wraps between highest and lowest step value.
4.4.7.1.3. LowestOff Field
This field SHALL indicate that the fan being off (speed value 0) is included as a step value.
4.4.7.1.4. When Generated
The client sends this command to speed the fan up or down in a step by step fashion.
4.4.7.1.5. Effect Upon Receipt
• This command SHALL be executed even if the fan speed is not currently at an implemented step
value.
• If the Direction field is Increase,
◦ If the fan speed is lower than the highest step value, the fan speed SHALL change to the low
est step value that is higher than the current fan speed.
◦ Else if Wrap is TRUE, the fan speed SHALL change to the lowest step value.
◦ Else the fan speed SHALL change to (or remain at) the highest step value.
• If the Direction field is Decrease,
◦ If the fan speed is higher than the lowest step value, the fan speed SHALL change to the
highest step value that is lower than the current fan speed.
◦ Else if Wrap is TRUE, the fan speed SHALL change to the highest step value.
◦ Else the fan speed SHALL change to (or remain at) the lowest step value.
• Although the effect of the Step command is implementation specific, the effect on receipt of the
Step command SHALL adhere to the conformance of the affected attributes.