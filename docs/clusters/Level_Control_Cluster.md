
# 1.6 Level Control Cluster

This cluster provides an interface for controlling a characteristic of a device that can be set to a
level, for example the brightness of a light, the degree of closure of a door, or the power output of a
heater.

## Data Types
1.6.5.1. OptionsBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the Level Control Cluster, specifically the 'ExecuteIfOff' feature, which is associated with bit '0'. This feature has a dependency on the On/Off cluster, as indicated in the summary. The conformance rule 'LT | OO' specifies that the 'ExecuteIfOff' feature is mandatory if either the 'LT' feature or the 'OO' feature is supported. In simpler terms, if a device supports either the 'LT' feature (which could stand for a specific functionality related to Level Control) or the 'OO' feature (likely referring to the On/Off capability), then the 'ExecuteIfOff' feature must be implemented. If neither of these features is supported, the 'ExecuteIfOff' feature is not required.

* In the Level Control Cluster, under the Data Types section, the entry for 'CoupleColorTempToLevel' with a bit value of '1' indicates a dependency on the Color Control cluster. The conformance rule 'LT' specifies that this element is mandatory if the feature 'LT' (likely representing a specific condition or feature related to Level and Temperature control) is supported. If the feature 'LT' is not supported, the conformance rule does not apply, implying that the element is not required. This entry highlights the conditional requirement based on the presence of a specific feature within the device's implementation.

1.6.5.1.1. ExecuteIfOff Bit
This bit indicates if this cluster has a dependency with the On/Off cluster.
1.6.5.1.2. CoupleColorTempToLevel Bit
This bit indicates if this cluster has a dependency with the Color Control cluster.
1.6.5.2. MoveModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Level Control Cluster, under the Data Types section, the table row describes an entry with the value '0', named 'Up', which is summarized as 'Increase the level'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Up' data type, which is used to increase the level, is a required component of the Level Control Cluster and must be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the Level Control Cluster, under the Data Types section, the table row describes an entry with the name "Down," which has a value of '1' and a summary indicating its function is to "Decrease the level." The conformance rule for this entry is marked as 'M,' which stands for Mandatory. This means that the "Down" element is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

1.6.5.3. StepModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Level Control Cluster, under the Data Types section, the table row describes an entry with the value '0', named 'Up', which summarizes the action of stepping upwards. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Up' data type must always be implemented and supported in any device or application that utilizes the Level Control Cluster, without any conditions or exceptions.

* In the Level Control Cluster, under the Data Types section, the table row describes an element with the name "Down," which has a value of '1' and a summary indicating it represents a "Step downwards" action. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Down" element is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "CurrentLevel" within the Level Control Cluster. This attribute has an ID of '0x0000' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The value of "CurrentLevel" is constrained between 'MinLevel' and 'MaxLevel', ensuring it falls within a specified range. The quality indicators 'S N X Q' suggest specific characteristics or requirements for this attribute, although their exact meanings are not detailed here. The default value for "CurrentLevel" is 'null', indicating it does not have a predefined starting value. The access permissions 'R V' imply that the attribute can be read and is volatile. The conformance rule 'M' signifies that the "CurrentLevel" attribute is mandatory, meaning it must always be implemented and supported in any device or application utilizing the Level Control Cluster.

* The table row describes an attribute named "RemainingTime" within the Level Control Cluster. This attribute has an ID of '0x0001' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The attribute is constrained to apply to all instances, has a quality indicator 'Q', and defaults to a value of '0'. It has read and view access permissions, denoted by 'R V'. The conformance rule 'LT' indicates that the "RemainingTime" attribute is mandatory if the feature or condition represented by 'LT' is supported. If 'LT' is not supported, the attribute is not required. This implies that the presence of the "RemainingTime" attribute is conditional upon the support of the 'LT' feature within the Level Control Cluster.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "MinLevel" within the Level Control Cluster. This attribute has an ID of '0x0002' and is of type 'uint8', with a constraint that its value must be between 1 and 254. The default value for "MinLevel" is set to 1. It has an access level of 'R V', indicating that it is readable and can be viewed. The conformance rule '[LT]' specifies that the "MinLevel" attribute is optional if the condition 'LT' is true, meaning that it is not required unless the specific feature or condition represented by 'LT' is supported. If 'LT' is not supported, the attribute is not required.

* The table row describes an attribute named "MinLevel" within the Level Control Cluster. This attribute has an ID of '0x0002' and is of type 'uint8', with a constraint that its maximum value can be 254. The default value for "MinLevel" is set to 0, and it has read and view access permissions, indicated by 'R V'. The conformance rule '[!LT]' specifies that the "MinLevel" attribute is optional if the feature 'LT' is not supported. In other words, if the 'LT' feature is not present, the inclusion of the "MinLevel" attribute is not required, but it can be included if desired.

* The table row describes an attribute named "MaxLevel" within the Level Control Cluster, identified by the ID '0x0003'. This attribute is of type 'uint8' and has a constraint that limits its value between 'MinLevel' and 254, with a default value set to 254. The access permissions for this attribute are 'R V', indicating it is readable and has a volatile nature. The conformance rule for "MaxLevel" is 'O', which means that this attribute is optional. It is not required for implementation and does not depend on any other features or conditions within the Matter specification.

* The table row describes an attribute named "CurrentFrequency" within the Level Control Cluster. This attribute has an ID of '0x0004' and is of type 'uint16', constrained between 'MinFrequency' and 'MaxFrequency'. It has a default value of '0' and can be accessed with 'R V' permissions, indicating it is readable and possibly volatile. The quality indicators 'P S Q' suggest specific characteristics or requirements not detailed here. The conformance rule 'FQ' implies that the "CurrentFrequency" attribute is mandatory if the feature 'FQ' is supported. If 'FQ' is not supported, the conformance rule does not specify an alternative, suggesting that the attribute may not be required in such cases.

* The table row describes an attribute named "MinFrequency" within the Level Control Cluster, identified by the ID '0x0005'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally as indicated by the 'Constraint' set to 'all'. The default value for this attribute is '0', and it has read and view access permissions, denoted by 'R V'. The conformance rule 'FQ' implies that the "MinFrequency" attribute is mandatory if the feature 'FQ' is supported. If the feature 'FQ' is not supported, the attribute is not required.

* The table row describes an attribute named "MaxFrequency" within the Level Control Cluster, identified by the ID '0x0006'. This attribute is of type 'uint16', with a constraint that its value must be at least as large as the 'MinFrequency'. It has a default value of '0' and access permissions of 'R V', indicating it is readable and has a volatile nature. The conformance rule 'FQ' indicates that the "MaxFrequency" attribute is mandatory if the feature 'FQ' is supported. If 'FQ' is not supported, the attribute is not required. This means that the presence of this attribute is contingent upon the support of the 'FQ' feature within the device's implementation.

* The table row describes an attribute named "OnOffTransitionTime" within the Level Control Cluster, identified by the ID '0x0010'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally as indicated by the 'Constraint' being 'all'. The default value for this attribute is '0', and it has read-write access with volatile operation ('RW VO'), meaning it can be read and modified, and changes may not persist across device resets. The 'Conformance' field is marked as 'O', which means that the "OnOffTransitionTime" attribute is optional. It is not required for the implementation of the Level Control Cluster and does not depend on any other features or conditions.

* The table row describes an attribute named "OnLevel" within the Level Control Cluster, identified by the ID '0x0011'. This attribute is of type 'uint8' and is constrained to values between 'MinLevel' and 'MaxLevel'. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in certain contexts, though the specifics are not detailed here. The default value for "OnLevel" is 'null', and it has read-write access with volatile optional (RW VO) permissions. The 'Conformance' is marked as 'M', meaning that the "OnLevel" attribute is mandatory and must always be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "OnTransitionTime" within the Level Control Cluster, identified by the ID `0x0012`. This attribute is of type `uint16`, meaning it is a 16-bit unsigned integer, and it applies universally across all relevant contexts as indicated by the constraint "all." The quality is marked as "X," meaning this attribute is explicitly disallowed in certain contexts or configurations. The default value for this attribute is `null`, and it has read-write access with volatile and optional characteristics, as denoted by "RW VO." The conformance rule for "OnTransitionTime" is "O," which signifies that this attribute is optional. It is not required and does not have any dependencies, meaning its implementation is at the discretion of the device manufacturer or developer, without any mandatory conditions imposed by the Matter specification.

* The table row describes an attribute named "OffTransitionTime" within the Level Control Cluster. This attribute has an ID of '0x0013' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' field indicates that this attribute applies universally ('all'), and its 'Quality' is marked as 'X', meaning it is explicitly disallowed. The default value for this attribute is 'null', and it has read-write access with volatile and optional characteristics ('RW VO'). The 'Conformance' field is marked as 'O', which means that the "OffTransitionTime" attribute is optional. This indicates that it is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an attribute named "DefaultMoveRate" within the Level Control Cluster, identified by the ID '0x0014'. This attribute is of type 'uint8' and has a constraint that its minimum value must be 1. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed in certain contexts, although the specifics are not detailed here. The default value is 'MS', and it has read-write access with volatile behavior ('RW VO'). The conformance rule for this attribute is 'O', meaning that its inclusion is optional and not required by any dependencies or conditions. In essence, the "DefaultMoveRate" attribute can be implemented at the discretion of the developer, but it is not a mandatory component of the Level Control Cluster according to the Matter specification.

* The table row describes an attribute within the Level Control Cluster, specifically the "Options" attribute. This attribute has an ID of '0x000F' and is of the type 'OptionsBitmap'. The constraints for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The default value for this attribute is '0', and it has read-write access with volatile options ('RW VO'). The conformance rule for this attribute is 'M', which means it is mandatory. This indicates that the "Options" attribute must always be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "StartUpCurrentLevel" within the Level Control Cluster. It is identified by the ID '0x4000' and is of type 'uint8'. The attribute has a constraint that is described elsewhere in the documentation, indicated by 'desc'. The quality 'XN' suggests it is not allowed in certain contexts, and its default value is 'MS'. The access level is 'RW VM', meaning it can be read and written, and is subject to view management. The conformance rule 'LT' indicates that the attribute is mandatory if the feature 'LT' is supported. If 'LT' is not supported, the conformance rule does not specify an alternative, implying that the attribute may not be required.

1.6.6.1. Scene Table Extensions
If the Scenes Management server cluster is implemented on the same endpoint, the following
attributes SHALL be part of the ExtensionFieldSetStruct of the Scene Table. If the implicit form of
the ExtensionFieldSetStruct is used, the order of the attributes in the AttributeValueList is in the
given order, i.e., the attribute listed as 1 is added first:
1. CurrentLevel
2. CurrentFrequency
Attributes in the scene table that are not supported by the device (according to the FeatureMap
attribute) SHALL be present in the scene table but ignored. An extension field set value outside of
the accepted values of the corresponding MoveTo<Target> command, e.g. a null value for the Cur
rentLevel attribute, corresponding to the MoveToLevel command, SHALL be ignored.
1.6.6.2. CurrentLevel Attribute
This attribute SHALL indicate the current level of this device. The meaning of 'level' is device
dependent.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second, or
• At the end of the movement/transition, or
• When it changes from null to any other value and vice versa.
1.6.6.3. RemainingTime Attribute
This attribute SHALL indicate the time remaining until the current command is complete - it is
specified in 1/10ths of a second.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• When it changes from 0 to any value higher than 10, or
• When it changes, with a delta larger than 10, caused by the invoke of a command, or
• When it changes to 0.
For commands with a transition time or changes to the transition time less than 1 second, changes
to this attribute SHALL NOT be reported.
As this attribute is not being reported during a regular countdown, clients SHOULD NOT rely on the
reporting of this attribute in order to keep track of the remaining duration.
1.6.6.4. MinLevel Attribute
This attribute SHALL indicate the minimum value of CurrentLevel that is capable of being assigned.
1.6.6.5. MaxLevel Attribute
This  attribute  SHALL  indicate  the  maximum  value  of  CurrentLevel  that  is  capable  of  being
assigned.
1.6.6.6. CurrentFrequency Attribute
This attribute SHALL indicate the frequency at which the device is at CurrentLevel. A CurrentFre
quency of 0 is unknown.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second, or
• At the start of the movement/transition, or
• At the end of the movement/transition.
1.6.6.7. MinFrequency Attribute
This attribute SHALL indicate the minimum value of CurrentFrequency that is capable of being
assigned. MinFrequency SHALL be less than or equal to MaxFrequency. A value of 0 indicates unde
fined.
1.6.6.8. MaxFrequency Attribute
This attribute SHALL indicate the maximum value of CurrentFrequency that is capable of being
assigned. MaxFrequency SHALL be greater than or equal to MinFrequency. A value of 0 indicates
undefined.
1.6.6.9. Options Attribute
This attribute SHALL indicate the selected options of the device.
The Options attribute is a bitmap that determines the default behavior of some cluster commands.
Each command that is dependent on the Options attribute SHALL first construct a temporary
Options bitmap that is in effect during the command processing. The temporary Options bitmap has
the same format and meaning as the Options attribute, but includes any bits that may be overrid
den by command fields.
This attribute is meant to be changed only during commissioning.
Command execution SHALL NOT continue beyond the Options processing if all of these criteria are
true:
• The command is one of the ‘without On/Off’ commands: Move, Move to Level, Step, or Stop.
• The On/Off cluster exists on the same endpoint as this cluster.
• The OnOff attribute of the On/Off cluster, on this endpoint, is FALSE.
• The value of the ExecuteIfOff bit is 0.
1.6.6.9.1. ExecuteIfOff Bit
If this bit is set, commands in this cluster are executed and potentially change the CurrentLevel
attribute when the OnOff attribute of the On/Off cluster is FALSE.
1.6.6.9.2. CoupleColorTempToLevel Bit
If this bit is set, changes to the CurrentLevel attribute SHALL be coupled with the color temperature
set in the Color Control cluster.
When not supporting the Lighting feature, this bit SHALL be zero and ignored.
1.6.6.10. OnOffTransitionTime Attribute
This attribute SHALL indicate the time taken to move to or from the target level when On or Off
commands are received by an On/Off cluster on the same endpoint. It is specified in 1/10ths of a sec
ond.
The actual time taken SHOULD be as close to OnOffTransitionTime as the device is able. Please note
that if the device is not able to move at a variable rate, the OnOffTransitionTime attribute SHOULD
NOT be implemented.
1.6.6.11. OnLevel Attribute
This attribute SHALL indicate the value that the CurrentLevel attribute is set to when the OnOff
attribute of an On/Off cluster on the same endpoint is set to TRUE, as a result of processing an
On/Off cluster command. If the OnLevel attribute is not implemented, or is set to the null value, it
has no effect. For more details see Effect of On/Off Commands on the CurrentLevel attribute.
OnLevel represents a mandatory field that was previously not present or optional. Implementers
should be aware that older devices may not implement it.
1.6.6.12. OnTransitionTime Attribute
This attribute SHALL indicate the time taken to move the current level from the minimum level to
the maximum level when an On command is received by an On/Off cluster on the same endpoint. It
is specified in 1/10ths of a second. If this attribute is not implemented, or contains a null value, the
OnOffTransitionTime SHALL be used instead.
1.6.6.13. OffTransitionTime Attribute
This attribute SHALL indicate the time taken to move the current level from the maximum level to
the minimum level when an Off command is received by an On/Off cluster on the same endpoint. It
is specified in 1/10ths of a second. If this attribute is not implemented, or contains a null value, the
OnOffTransitionTime SHALL be used instead.
1.6.6.14. DefaultMoveRate Attribute
This attribute SHALL indicate the movement rate, in units per second, when a Move command is
received with a null value Rate parameter.
1.6.6.15. StartUpCurrentLevel Attribute
This attribute SHALL indicate the desired startup level for a device when it is supplied with power
and this level SHALL be reflected in the CurrentLevel attribute. The values of the StartUpCur
rentLevel attribute are listed below:

_Table parsed from section 'Attributes':_

* In the Level Control Cluster, under the Attributes section, the table row describes the behavior of the 'Value' attribute, which is set to '0'. The action specified for this attribute upon power-up is to set the 'CurrentLevel' attribute to the minimum value permitted on the device. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage, it likely implies a mandatory action that must be followed whenever the device powers up. This ensures that the device starts at a known, minimum level, which is crucial for consistent and predictable operation. If there were specific conformance conditions, they would dictate whether this action is mandatory, optional, or subject to other conditions, but in this case, the action appears to be a standard requirement.

_Table parsed from section 'Attributes':_

* In the Level Control Cluster, under the Attributes section, there is an entry concerning the 'Value' attribute, which is set to 'null'. The action specified for this attribute upon power-up is to set the 'CurrentLevel' attribute to its previous value. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context, it implies that the action of setting the 'CurrentLevel' attribute to its previous value is a necessary behavior when the device powers up. This suggests that the attribute's behavior is likely mandatory, ensuring that the device retains its previous level setting after a power cycle, which is crucial for maintaining consistent device operation and user experience.

* In the Level Control Cluster, under the Attributes section, the table row describes an attribute with the 'Value' set to 'other values' and specifies that the 'Action on power up' is to set the CurrentLevel attribute to this value. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would dictate when this attribute is required or optional based on certain conditions or features. For example, if the conformance was `M`, it would mean this action is always mandatory. If it were `O`, it would be optional. If a more complex expression were given, it would specify conditions under which this action becomes mandatory or optional, or if it is deprecated or disallowed. Without a specific conformance string provided, we can only infer that the action described is a standard behavior for setting the CurrentLevel attribute upon power-up, potentially subject to further conditions not detailed here

This behavior does not apply to reboots associated with OTA. After an OTA restart, the CurrentLevel
attribute SHALL return to its value prior to the restart.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the "MoveToLevel" command. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level is optional ('Access: O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "MoveToLevel" command is always required to be implemented in any device that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Level Control Cluster, specifically the "Move" command, which is identified by the ID '0x01'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented by default. However, the conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that within the context of the Matter specification, any implementation of the Level Control Cluster must include the "Move" command as a required feature, regardless of any other conditions or features present.

* The table row describes a command within the Level Control Cluster, specifically the "Step" command, which is identified by the ID '0x02'. This command is directed from the client to the server, indicating that it is initiated by the client and received by the server. The command requires a response, as indicated by 'Response: Y', and has optional access control, denoted by 'Access: O'. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "Step" command must always be implemented in any device that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Level Control Cluster, specifically the "Stop" command, which is identified by the ID '0x03'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level is optional ('Access: O'), meaning it is not required to be implemented by all devices. However, the conformance rule for this command is 'M', which means it is mandatory. This indicates that, according to the Matter specification, all devices implementing the Level Control Cluster must support the "Stop" command, ensuring consistent functionality across compliant devices.

* The table row describes a command within the Level Control Cluster, specifically the "MoveToLevelWithOnOff" command. This command is identified by the ID '0x04' and is directed from the client to the server, indicating that it is initiated by the client and processed by the server. The command requires a response, as indicated by 'Response: Y', and has optional access control, denoted by 'Access: O'. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "MoveToLevelWithOnOff" command must always be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Level Control Cluster, specifically the "MoveWithOnOff" command, which is identified by the ID '0x05'. This command is directed from the client to the server, and it requires a response, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', meaning the access level is optional. The 'Conformance' field is marked 'M', which signifies that the "MoveWithOnOff" command is mandatory. This means that any implementation of the Level Control Cluster must include this command, as it is always required without any conditions or dependencies.

* The table row describes a command within the Level Control Cluster, specifically the "StepWithOnOff" command, which is identified by the ID '0x06'. This command is directed from the client to the server and requires a response, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', suggesting that access to this command is optional. The 'Conformance' field is marked 'M', which means that the "StepWithOnOff" command is mandatory. This implies that any implementation of the Level Control Cluster must include this command, ensuring it is always supported and available for use in the specified client-server direction.

* The table row describes a command within the Level Control Cluster, specifically the "StopWithOnOff" command, which is directed from the client to the server. The command has an ID of '0x07' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented by all devices. The conformance rule for this command is 'M', indicating that it is mandatory. This means that any implementation of the Level Control Cluster must include the "StopWithOnOff" command as a required feature, ensuring consistent functionality across devices that support this cluster.

* The table row describes a command within the Level Control Cluster, specifically the "MoveToClosestFrequency" command, which is identified by the ID '0x08'. This command is sent from a client to a server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'FQ' indicates that the command is mandatory if the feature 'FQ' is supported. If the feature 'FQ' is not supported, the command is not required. This means that the implementation of this command depends on the presence of the 'FQ' feature within the device's capabilities.

1.6.7.1. MoveToLevel Command

_Table parsed from section 'Commands':_

* In the Level Control Cluster, under the Commands section, the table row describes a command with the ID '0' named 'Level'. This command is of type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that its maximum value is 254. The conformance rule for this command is 'M', indicating that it is mandatory. This means that the 'Level' command is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* In the Level Control Cluster, within the context of commands, the table row describes an element with the ID '1' named 'TransitionTime', which is of type 'uint16' and has a constraint labeled 'all'. The quality of this element is marked as 'X', indicating it is explicitly disallowed in terms of quality. The conformance rule for 'TransitionTime' is 'M', meaning that this element is mandatory and always required within the Level Control Cluster. This implies that any implementation of this cluster must include the 'TransitionTime' element as a necessary component.

* The table row describes an element within the Level Control Cluster, specifically a command named "OptionsMask" with an ID of '2'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a Mandatory element. This indicates that the "OptionsMask" command must always be implemented and supported in any device or application that uses the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Level Control Cluster, specifically named "OptionsOverride" with an ID of '3'. This command is of the type "OptionsBitmap" and has a constraint described elsewhere in the documentation, with a default value of '0'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "OptionsOverride" command must always be implemented and supported in any device or application that includes the Level Control Cluster, without any conditions or exceptions.

1.6.7.1.1. Effect on Receipt
The OptionsMask and OptionsOverride fields SHALL both be present. Default values are provided
to interpret missing fields from legacy devices. A temporary Options bitmap SHALL be created from
the Options attribute, using the OptionsMask and OptionsOverride fields. Each bit of the temporary
Options bitmap SHALL be determined as follows:
Each bit in the Options attribute SHALL determine the corresponding bit in the temporary Options
bitmap, unless the OptionsMask field is present and has the corresponding bit set to 1, in which
case the corresponding bit in the OptionsOverride field SHALL determine the corresponding bit in
the temporary Options bitmap.
The  resulting  temporary  Options  bitmap  SHALL  then  be  processed  as  defined  in  the  Options
attribute.
On receipt of this command, a device SHALL move from its current level to the value given in the
Level field. The meaning of ‘level’ is device dependent – e.g., for a light it MAY mean brightness
level.
The movement SHALL be as continuous as technically practical, i.e., not a step function, and the
time taken to move to the new level SHALL be equal to the value of the TransitionTime field, in
tenths of a second, or as close to this as the device is able.
If the TransitionTime field takes the value null then the time taken to move to the new level SHALL
instead be determined by the OnOffTransitionTime attribute. If OnOffTransitionTime, which is an
optional attribute, is not present, the device SHALL move to its new level as fast as it is able.
If the device is not able to move at a variable rate, the TransitionTime field MAY be disregarded.
1.6.7.2. Move Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the "MoveMode" command. This command is identified by the ID '0' and utilizes the data type 'MoveModeEnum'. The constraint for this command is marked as 'desc', indicating that the specific constraints are detailed elsewhere in the documentation. The conformance rule for this command is 'M', which means it is mandatory. This implies that the "MoveMode" command is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* In the Level Control Cluster, under the Commands section, the table row describes a command with the ID '1' named 'Rate', which is of type 'uint8' and has a constraint applicable to all. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The 'Conformance' is marked as 'M', meaning that the 'Rate' command is mandatory and always required according to the Matter specification. However, given the 'Quality' is 'X', it suggests a contradiction where the command is both mandatory and disallowed, which might require further clarification or correction in the documentation.

* The table row describes an element within the Level Control Cluster, specifically a command named "OptionsMask" with an ID of '2'. This command is of the type 'OptionsBitmap', and its constraints are described elsewhere in the documentation. The default value for this command is '0'. The conformance rule for "OptionsMask" is 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* In the Level Control Cluster, under the Commands section, the entry for 'OptionsOverride' with ID '3' is defined as having a type of 'OptionsBitmap' and a default value of '0'. The constraint for this entry is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'OptionsOverride' is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

1.6.7.2.1. MoveMode Field
This field SHALL be one of the non-reserved values in MoveModeEnum.
1.6.7.2.2. Rate Field
This field SHALL indicate the rate of movement in units per second. The actual rate of movement
SHOULD be as close to this rate as the device is able. If the Rate field is null, then the value of the
DefaultMoveRate attribute SHALL be used if that attribute is supported and its value is not null. If
the Rate field is null and the DefaultMoveRate attribute is either not supported or set to null, then
the device SHOULD move as fast as it is able. If the device is not able to move at a variable rate, this
field MAY be disregarded.
1.6.7.2.3. Effect on Receipt
On receipt of this command, if the Rate field has a value of zero, the command has no effect and a
response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL first create and process a temporary Options bitmap as described in the
MoveToLevel command.
On receipt of this command, a device SHALL move from its current level in an up or down direction
in a continuous fashion, as detailed below.

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the 'MoveMode' set to 'Up'. This command's action upon receipt is to increase the device's level at a specified rate, stopping when the maximum level allowed by the device is reached. The conformance rule for this command is not explicitly provided in the row data, but if we were to interpret it using the Matter Conformance Interpretation Guide, it would typically indicate whether this command is mandatory, optional, or subject to certain conditions based on the device's features. For instance, if the conformance were 'M', it would mean that this command must always be supported by devices implementing the Level Control Cluster. If it were 'O', it would mean that supporting this command is optional and not dependent on other features. Without the specific conformance string, we can only infer that the command is an integral part of the Level Control Cluster's functionality, intended to adjust the device's level upwards within its operational limits.

* The table row entry pertains to the "MoveMode" command within the Level Control Cluster, specifically focusing on the "Down" mode. The action specified for this command is to decrease the device's level at a rate specified in the Rate field, ceasing the decrease once the minimum level allowed by the device is reached. The conformance rule for this entry is not explicitly provided in the data given, but if we were to interpret a typical conformance scenario using the guide, it might involve conditions under which this command is mandatory, optional, or otherwise. For instance, if the conformance were something like `OO, O`, it would mean that the "MoveMode: Down" command is mandatory if the OnOff feature is supported; otherwise, it is optional. However, without the specific conformance string, we can only describe the action and its intended effect on the device.

1.6.7.3. Step Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the "StepMode" command. This command is identified by the ID '0' and uses the data type 'StepModeEnum'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' field is marked with an 'M', which means that the "StepMode" command is mandatory. This implies that any implementation of the Level Control Cluster must include this command, as it is always required according to the Matter specification.

* The table row describes a command within the Level Control Cluster, specifically the "StepSize" command. This command is identified by the ID '1' and is of type 'uint8', which indicates it is an 8-bit unsigned integer. The constraint 'all' suggests that this command applies universally without specific limitations. The conformance rule for "StepSize" is marked as 'M', which stands for Mandatory. This means that the "StepSize" command is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Level Control Cluster, specifically the "TransitionTime" command. This command is identified by the ID '2' and is of type 'uint16', which indicates it uses a 16-bit unsigned integer. The 'Constraint' field is marked as 'all', suggesting that this command applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in some contexts, although this does not affect its conformance requirement. The 'Conformance' field is marked as 'M', which means that the "TransitionTime" command is mandatory and must always be implemented within the Level Control Cluster according to the Matter specification.

* The table row describes an element within the Level Control Cluster, specifically a command named "OptionsMask" with an ID of '3'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by "desc". The conformance rule for "OptionsMask" is marked as 'M', which means it is a Mandatory element. This implies that the "OptionsMask" command must always be implemented and supported in any device or application that utilizes the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command named "OptionsOverride" within the Level Control Cluster, specifically in the context of commands. This command has an ID of '4' and is of the type 'OptionsBitmap', with constraints described elsewhere in the documentation. The default value for this command is '0'. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Level Control Cluster. There are no conditions or exceptions to this requirement, indicating its fundamental importance in the cluster's functionality.

1.6.7.3.1. StepMode Field
This field SHALL be one of the non-reserved values in StepModeEnum.
1.6.7.3.2. StepSize Field
This field SHALL indicate the change to CurrentLevel.
1.6.7.3.3. TransitionTime Field
This field SHALL indicate the time that SHALL be taken to perform the step, in tenths of a second. A
step is a change in the CurrentLevel of StepSize units. The actual time taken SHOULD be as close to
this as the device is able. If the TransitionTime field is equal to null, the device SHOULD move as
fast as it is able.
If the device is not able to move at a variable rate, the TransitionTime field MAY be disregarded.
1.6.7.3.4. Effect on Receipt
On receipt of this command, if the StepSize field has a value of zero, the command has no effect and
a response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL first create and process a temporary Options bitmap as described in the
MoveToLevel command.
On receipt of this command, a device SHALL move from its current level in an up or down direction
as detailed below.

_Table parsed from section 'Commands':_

* The table row entry pertains to the "StepMode" command within the Level Control Cluster, specifically when the mode is set to "Up." The action on receipt of this command is to increase the "CurrentLevel" by a specified "StepSize" until the maximum level permitted by the device is reached. If the maximum level is reached during this process, the transition time must be proportionally reduced. The conformance rule for this command is not explicitly provided in the data, but based on the context, it would likely be mandatory (M) or optional (O) depending on the specific device capabilities and features supported. If the conformance were specified, it would dictate whether this command is always required, conditionally required, or optional based on the presence or absence of certain features or conditions.

* The table row entry pertains to the "StepMode" command within the Level Control Cluster, specifically when the mode is set to "Down." The action to be taken upon receipt of this command is to decrease the "CurrentLevel" by a specified "StepSize" until it either reaches the minimum level allowed by the device or the step is completed. If the minimum level is reached before the step is completed, the transition time must be proportionally reduced. The conformance rule for this command is not explicitly provided in the row data, but based on the context and typical usage in the Matter specification, it would likely be mandatory (M) for devices that support level control functionality. This means that any device implementing the Level Control Cluster must support this command to ensure consistent behavior across different devices and manufacturers.

Increase CurrentLevel by StepSize units, or until
device if this reached in the process. In the latter
Decrease CurrentLevel by StepSize units, or until
device if this reached in the process. In the latter
1.6.7.4. Stop Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the "OptionsMask" command. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the "OptionsMask" command is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

* The table row describes a command named "OptionsOverride" within the Level Control Cluster, specifically under the Commands section. This command is of the type "OptionsBitmap" and has a constraint that is described elsewhere in the documentation, with a default value of 0. The conformance rule for this command is marked as "M," which stands for Mandatory. This means that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Level Control Cluster, without any conditions or exceptions.

1.6.7.4.1. Effect of Receipt
On receipt of this command, a device SHALL first create and process a temporary Options bitmap
as described in the MoveToLevel command.
Upon receipt of this command, any MoveToLevel, Move or Step command (and their 'with On/Off'
variants) currently in process SHALL be terminated. The value of CurrentLevel SHALL be left at its
value upon receipt of the Stop command, and RemainingTime SHALL be set to zero.
This command has two entries in the Commands list, one for the MoveToLevel, Move and Step com
mands, and one for their 'with On/Off' counterparts. This is solely for symmetry, to allow easy
choice of one or other set of commands – the Stop commands are identical, because the dependency
on On/Off is determined by the original command that is being stopped.
1.6.7.5. MoveToClosestFrequency Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Level Control Cluster, specifically the "Frequency" command, which is identified by the ID '0' and has a data type of 'uint16'. The constraint 'all' indicates that this command applies universally within its context. The default value for this command is '0'. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Level Control Cluster. There are no conditions or exceptions to this requirement, ensuring that the "Frequency" command is consistently available across all implementations of this cluster.

1.6.7.5.1. Effect of Receipt
Upon receipt of this command, the device SHALL change its current frequency to the requested fre
quency, or to the closest frequency that it can generate. If the device cannot approximate the fre
quency, then it SHALL return a default response with an error code of CONSTRAINT_ERROR. Deter
mining if a requested frequency can be approximated by a supported frequency is a manufacturer-
specific decision.
1.6.7.6. 'With On/Off' Commands
The MoveToLevelWithOnOff, MoveWithOnOff and StepWithOnOff commands have identical data
fields compared to the MoveToLevel, Move and Step commands respectively. They also have the
same effects, except for the following additions.
Before commencing any command that has the effect of setting the CurrentLevel attribute above
the minimum level allowed by the device, the OnOff attribute of the On/Off cluster on the same end
point, if implemented, SHALL be set to TRUE (‘On’).
If any command that has the effect of setting the CurrentLevel attribute to the minimum level
allowed by the device, the OnOff attribute of the On/Off cluster on the same endpoint, if imple
mented, SHALL be set to FALSE (‘Off’).
The StopWithOnOff command has identical data fields compared to the Stop command. Both Stop
commands are identical, because the dependency on On/Off is determined by the original com
mand that is being stopped.

## State Change Table for Lighting
Below is a table of examples of state changes when Level Control and On/Off clusters are on the
same endpoint and the Lighting feature is set.
EiO - ExecuteIfOff field in the Options attribute
OnOff – Attribute value of On/Off cluster: FALSE=‘Off’, TRUE=‘On’
MIN - MinLevel
MAX - MaxLevel
MID – Midpoint between MinLevel and MaxLevel
1.6.8.1. Lighting Device State Change examples

_Table parsed from section 'State Change Table for Lighting':_

* In the Level Control Cluster's State Change Table for Lighting, the table row describes a scenario where the 'CurrentLevel' remains the same, the 'EiO' (Error in Operation) is '0', the 'OnOff' attribute is 'FALSE', and the 'Physical Device' is 'Off'. The command 'MoveToLevel(l =MID, t=2 sec)' is issued, but the 'Device Output Result' indicates that the device 'Stays off'. This suggests that despite the command to change the level, the device does not turn on or change its state. The conformance rule for this scenario is not explicitly provided in the row data, but based on the context, it implies that the device's behavior is consistent with the expectation that it should remain off when the 'OnOff' attribute is 'FALSE', regardless of level change commands. This behavior is likely mandatory when the 'OnOff' attribute is not active, ensuring that the device does not respond to level change

* This table row describes a scenario within the Level Control Cluster, specifically in the context of the State Change Table for Lighting. The entry details the behavior of a lighting device when the `MoveToLevelWithOnOff` command is issued with a level set to "MID" and a transition time of 2 seconds. The device is expected to turn on and adjust its output level to or maintain it at half brightness. The conformance rule 'MID' indicates that this behavior is mandatory for devices that support the specified conditions or features, as defined by the context of the table. The 'EiO' value of '0' and 'OnOff' being 'TRUE' suggest that the device must be capable of turning on and adjusting its brightness level as described, without any exceptions or optional conditions.

* This table row pertains to the Level Control Cluster within the context of the State Change Table for Lighting. It describes the behavior of a lighting device when a "MoveToLevel" command is issued with a level parameter set to "MID" and a transition time of 2 seconds. The current level is "MID," the "EiO" (Effect in Operation) is set to "1," the "OnOff" attribute is "FALSE," and the physical device is "Off." The command does not change the device's state, as the "Device Output Result" indicates that the device "Stays off." The conformance rule for this entry is not explicitly provided in the table row data, but based on the context, it implies that the described behavior is a mandatory requirement for devices implementing the Level Control Cluster, ensuring consistent behavior when the specified command is executed under these conditions.

* This table row from the Level Control Cluster, specifically within the State Change Table for Lighting, describes the behavior of a lighting device when a specific command is issued. The command in question is `MoveToLevelWithOnOff(l= MID, t=2 sec)`, which instructs the device to turn on and adjust its output level to the midpoint over a duration of 2 seconds. The initial state of the device is "On" with the "CurrentLevel" set to "MID" and the "OnOff" attribute as "TRUE". The result of this command is that the device turns on (if it was off) and adjusts its output level to or maintains it at half. The conformance rule for this entry is not explicitly detailed in the provided data, but based on the context, it implies that the described behavior is mandatory for devices implementing the Level Control Cluster with the OnOff feature, ensuring consistent operation across compliant devices.

* In the context of the Level Control Cluster, specifically within the State Change Table for Lighting, the table row describes a scenario where the 'CurrentLevel' is set to 'MAX', with 'EiO' (Energy in Operation) as '1', 'OnOff' status as 'FALSE', and the 'Physical Device' is 'Off'. The command 'Move(up, rate=64/s)' is issued, but the 'Device Output Result' remains 'Stays off'. The conformance rule 'MAX' indicates that this element is mandatory when the 'CurrentLevel' is at its maximum value. This means that whenever the level is at its maximum, the described behavior and conditions must be adhered to, ensuring that the device stays off despite the command to move up at a rate of 64 units per second.

* This table row from the Level Control Cluster, specifically within the State Change Table for Lighting, describes the behavior of a lighting device when a "MoveWithOnOff" command is issued with an upward direction at a rate of 64 units per second. The context indicates that the "CurrentLevel" is set to "MAX," the "EiO" (Effect in Operation) is "1," the "OnOff" attribute is "TRUE," and the "Physical Device" is "On." As a result of this command, the device will turn on, and its output level will adjust to or remain at full brightness. The conformance rule for this entry is 'MAX,' which is not a standard conformance tag or expression as per the provided guide. However, in this context, it likely implies that this behavior is mandatory when the current level is at its maximum, ensuring that the device responds appropriately to the command by maintaining or reaching full brightness.

* In the Level Control Cluster's State Change Table for Lighting, the table row describes a scenario where the 'CurrentLevel' is set to 'MIN', with 'EiO' (Execute if On) as '1', 'OnOff' as 'FALSE', and the 'Physical Device' is 'Off'. The command 'MoveWithOnOff(down, rate=64/s)' is issued, resulting in the 'Device Output Result' of 'Stays off'. The conformance rule for this entry is 'MIN', which indicates that this behavior is mandatory when the 'CurrentLevel' is at its minimum setting. This means that regardless of other conditions, when the 'CurrentLevel' is at 'MIN', the device must adhere to this behavior, ensuring that the device remains off when the specified command is executed under these conditions.

* This table row from the Level Control Cluster, specifically within the State Change Table for Lighting, describes the behavior of a lighting device when a command is issued. The 'CurrentLevel' is set to 'MID', indicating a midpoint brightness level. The 'EiO' (Effect in Operation) is 'any', meaning the command applies regardless of any ongoing effects. The 'OnOff' attribute is 'TRUE', signifying that the device is currently on. The 'Physical Device' state is 'On (mid-point brightness)', reflecting the device's current operational state. The 'Command Before After' column specifies the command 'MoveToLevelWithOnOff(l= MID, t=2 sec)', which instructs the device to adjust its brightness to the midpoint over a duration of 2 seconds. The 'Device Output Result' indicates that the output level will adjust to or remain at half brightness. The conformance rule 'MID' is interpreted as follows: the feature or behavior described is mandatory if the

adjusts or
adjusts to
adjusts to
adjusts to

_Table parsed from section 'State Change Table for Lighting':_

* In the Level Control Cluster, specifically within the State Change Table for Lighting, the table row describes the behavior of a lighting device when a "MoveWithOnOff" command is issued with an upward movement at a rate of 64 units per second. The 'CurrentLevel' is set to 'MAX', indicating that the light is at its maximum brightness. The 'EiO' (Event in Operation) is 'any', meaning this behavior applies regardless of other events. The 'OnOff' status is 'TRUE', signifying that the light is currently on. The 'Physical Device' state is 'On (full brightness)', indicating that the device is fully illuminated. The 'Device Output Result' specifies that the output level will adjust to or remain at full brightness. The conformance rule 'MAX' suggests that this behavior is mandatory when the light is at its maximum level, ensuring that the device consistently responds by maintaining full brightness under these conditions.

* This table row from the Level Control Cluster, specifically within the State Change Table for Lighting, describes the behavior of a lighting device when certain conditions are met. The entry indicates that when the 'CurrentLevel' is set to 'MIN', the 'EiO' (External input/output) can be any value, and the 'OnOff' attribute is 'TRUE', the physical device should be 'On' but at its minimum brightness. The command 'Move(down, rate=64/s)' is executed, resulting in the device's output level adjusting to the minimum. The conformance rule 'MIN' suggests that this behavior is mandatory when the 'CurrentLevel' is at its minimum, meaning that the device must support this functionality under these conditions without exception.

* In the Level Control Cluster, specifically within the State Change Table for Lighting, the table row describes the behavior when the 'CurrentLevel' is set to 'MIN'. The 'EiO' (Event in Operation) can be any event, and the 'OnOff' attribute is 'FALSE', indicating that the device is not currently on. The 'Physical Device' is in the 'Off' state. The command 'MoveWithOnOff(down, rate=64/s)' is issued, which means the device is instructed to decrease its level at a rate of 64 units per second while considering the On/Off state. As a result, the 'Device Output Result' is that the output level adjusts to off. The conformance rule 'MIN' in this context implies that this behavior is mandatory when the 'CurrentLevel' is at its minimum, ensuring that the device consistently transitions to an off state under these conditions.

