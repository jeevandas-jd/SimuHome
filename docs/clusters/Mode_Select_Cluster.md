
# 1.9 Mode Select Cluster

This cluster provides an interface for controlling a characteristic of a device that can be set to one
of several predefined values. For example, the light pattern of a disco ball, the mode of a massage
chair, or the wash cycle of a laundry machine.
The server allows the client to set a mode on the server. A mode is one of a list of options that may
be presented by a client for a user choice, or understood by the client, via the semantic tags on the
mode.
A semantic tag is either a standard tag within a standard category namespace, or a manufacturer
specific tag, within the namespace of the vendor ID of the manufacturer. If there is no semantic tag,
the mode is anonymous, and the selection is made by the user solely based on the Label string.
Each cluster ID that indicates this specification SHALL define a distinct purpose for the cluster
instance. For example: A LightBlinking cluster ID supports blinking modes for a light (and is
described that way).
An anonymous mode SHALL support the derived cluster purpose. A manufacturer specific seman
tic tag SHALL support the derived cluster purpose. An anonymous mode SHALL NOT replace the
meaning of a standard semantic tag, when one exists, for the cluster purpose.

## Data Types
1.9.5.1. SemanticTagStruct Type
A Semantic Tag is meant to be interpreted by the client for the purpose the cluster serves.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Mode Select Cluster, specifically in the Data Types section, for an element named 'MfgCode'. This element is of the type 'vendor-id' and has constraints that are described elsewhere in the documentation. The 'Quality' is marked as 'F', which typically indicates a specific quality or characteristic defined in the broader context of the specification. The 'Conformance' for 'MfgCode' is marked as 'M', meaning it is a Mandatory element. This indicates that the 'MfgCode' must always be included and supported in any implementation of the Mode Select Cluster, without any conditions or exceptions.

* In the Mode Select Cluster, under the Data Types section, the table row describes an element with the ID '1' and the name 'Value'. This element is of the type 'enum16', which indicates it is a 16-bit enumerated data type. The constraint 'all' suggests that this element can take any value within the defined range of the enum16 type. The quality 'F' is noted, though its specific meaning is not detailed in the provided context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Value' element is always required to be implemented in any device or application that supports the Mode Select Cluster, without any conditions or exceptions.

1.9.5.1.1. Value Field
This field SHALL indicate the semantic tag within a semantic tag namespace which is either manu
facturer specific or standard. For semantic tags in a standard namespace, see Standard Namespace.
1.9.5.1.2. MfgCode Field
This field SHALL indicate a manufacturer code (Vendor ID), and the Value field SHALL indicate a
semantic tag defined by the manufacturer. Each manufacturer code supports a single namespace of
values. The same manufacturer code and semantic tag value in separate cluster instances are part
of the same namespace and have the same meaning. For example: a manufacturer tag meaning
"pinch", has the same meaning in a cluster whose purpose is to choose the amount of sugar, or
amount of salt.
1.9.5.2. ModeOptionStruct Type
This is a struct representing a possible mode of the server.

_Table parsed from section 'Data Types':_

* In the Mode Select Cluster, under the Data Types section, the table row describes an element with the ID '0' named 'Label'. This element is of the 'string' type and is constrained to a maximum length of 64 characters. It has a quality designation of 'F' and a default value of 'MS'. The conformance rule for this element is 'M', which means that the 'Label' is a mandatory component of the Mode Select Cluster. It is always required to be implemented, with no conditions or exceptions.

* The table row describes an element within the Mode Select Cluster, specifically under the Data Types section. The element is identified by the ID '1' and is named 'Mode'. It is of type 'uint8', which indicates it is an unsigned 8-bit integer. The 'Quality' is marked as 'F', and it has a default value of 'MS'. The conformance rule for this element is 'M', which means that the 'Mode' element is mandatory. This indicates that it is always required to be implemented in any device or application that supports the Mode Select Cluster, with no conditions or exceptions.

* The table row describes an entry within the Mode Select Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'SemanticTags'. It is a data type of 'list[SemanticTagStruct]' with a constraint allowing a maximum of 64 entries. The quality is marked as 'F', and the default value is 'MS'. The conformance rule for this entry is 'M', which means that the 'SemanticTags' element is mandatory. This indicates that it is always required to be implemented in any device or application that supports the Mode Select Cluster, without any conditions or exceptions.

1.9.5.2.1. Label Field
This field is readable text that describes the mode option that can be used by a client to indicate to
the user what this option means. This field is meant to be readable and understandable by the user.
1.9.5.2.2. Mode Field
The Mode field is used to identify the mode option. The value SHALL be unique for every item in
the SupportedModes attribute.
1.9.5.2.3. SemanticTags Field
This field is a list of semantic tags that map to the mode option. This MAY be used by clients to
determine the meaning of the mode option as defined in a standard or manufacturer specific name
space. Semantic tags can help clients look for options that meet certain criteria. A semantic tag
SHALL be either a standard tag or manufacturer specific tag as defined in each SemanticTagStruct
list entry.
A mode option MAY have more than one semantic tag. A mode option MAY be mapped to a mixture
of standard and manufacturer specific semantic tags.
All standard semantic tags are from a single namespace indicated by the StandardNamespace
attribute.
HIGH MAX
For example: A mode labeled "100%" can have both the   (MS) and   (standard) semantic tag.
HIGH MAX
Clients seeking the option for either   or   will find the same option in this case.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Mode Select Cluster, specifically the "Description" attribute, which is identified by the ID '0x0000'. This attribute is of type 'string' with a maximum constraint of 64 characters. It has a quality of 'F', a default value of 'MS', and access permissions of 'R V', indicating it can be read and is viewable. The conformance rule for this attribute is 'M', meaning it is mandatory. This indicates that the "Description" attribute must always be implemented in any device or application that supports the Mode Select Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Mode Select Cluster, specifically the 'StandardNamespace' attribute. This attribute is identified by the ID '0x0001' and is of the type 'enum16', which means it is an enumerated type with 16 possible values. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is 'FX', suggesting a fixed quality level, and the 'Default' value is 'null', meaning it does not have a predefined default value. The 'Access' is 'R V', which means the attribute is readable and has a volatile nature. The 'Conformance' is marked as 'M', indicating that the 'StandardNamespace' attribute is mandatory and must always be implemented in any device supporting the Mode Select Cluster.

* The table row describes an attribute within the Mode Select Cluster, specifically the "SupportedModes" attribute. This attribute has an ID of '0x0002' and is of the type 'list[ModeOptionStruct]', with a constraint allowing a maximum of 255 entries. It is marked with a quality of 'F', has a default value of 'MS', and access permissions of 'R V', indicating it can be read and is viewable. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "SupportedModes" attribute must always be implemented in any device or application that supports the Mode Select Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Mode Select Cluster, specifically the "CurrentMode" attribute. This attribute is identified by the ID '0x0003' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'N', and the default value is 'MS'. The access level is 'R V', which typically means it is readable and possibly volatile. The conformance rule for this attribute is 'M', indicating that the "CurrentMode" attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Mode Select Cluster, with no conditions or exceptions.

* The table row describes an attribute named "StartUpMode" within the Mode Select Cluster. This attribute has an ID of '0x0004' and is of type 'uint8'. The constraints for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'NX', which typically denotes a specific quality characteristic defined in the broader context of the specification. The default value for this attribute is 'MS', and it has read-write access with volatile and optional characteristics ('RW VO'). The conformance rule for "StartUpMode" is 'O', meaning that this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an attribute named "OnMode" within the Mode Select Cluster. This attribute has an ID of '0x0005' and is of type 'uint8'. Its constraints are described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'NX', suggesting it has specific quality characteristics not detailed here. The default value for this attribute is 'null', and it has read-write access with volatile and optional characteristics ('RW VO'). The conformance rule 'DEPONOFF' indicates that the "OnMode" attribute is deprecated if the OnOff feature is supported. This means that in contexts where the OnOff feature is present, the use of the "OnMode" attribute is considered obsolete and should be avoided.

1.9.6.1. Description Attribute
This attribute describes the purpose of the server, in readable text.
For example, a coffee machine may have a Mode Select cluster for the amount of milk to add, and
another Mode Select cluster for the amount of sugar to add. In this case, the first instance can have
Milk Sugar
the description   and the second instance can have the description  . This allows the user to
tell the purpose of each of the instances.
1.9.6.2. StandardNamespace Attribute
This attribute, when not null, SHALL indicate a single standard namespace for any standard seman
tic tag value supported in this or any other cluster instance with the same value of this attribute. A
null value indicates no standard namespace, and therefore, no standard semantic tags are provided
in this cluster instance. Each standard namespace and corresponding values and value meanings
SHALL be defined in another document.
1.9.6.3. SupportedModes Attribute
This attribute is the list of supported modes that may be selected for the CurrentMode attribute.
Each item in this list represents a unique mode as indicated by the Mode field of the ModeOption
Struct. Each entry in this list SHALL have a unique value for the Mode field.
1.9.6.4. CurrentMode Attribute
This attribute represents the current mode of the server.
SupportedModes
The value of this field must match the Mode field of one of the entries in the
attribute.
1.9.6.5. StartUpMode Attribute
The StartUpMode attribute value indicates the desired startup mode for the server when it is sup
plied with power.
If this attribute is not null, the CurrentMode attribute SHALL be set to the StartUpMode value, when
the server is powered up, except in the case when the OnMode attribute overrides the StartUpMode
attribute (see OnModeWithPowerUp).
This behavior does not apply to reboots associated with OTA. After an OTA restart, the CurrentMode
attribute SHALL return to its value prior to the restart.
SupportedModes
The value of this field SHALL match the Mode field of one of the entries in the
attribute.
If this attribute is not implemented, or is set to the null value, it SHALL have no effect.
1.9.6.6. OnMode Attribute
This attribute SHALL indicate the value of CurrentMode that depends on the state of the On/Off
cluster on the same endpoint. If this attribute is not present or is set to null, it SHALL NOT have an
effect, otherwise the CurrentMode attribute SHALL depend on the OnOff attribute of the On/Off
cluster as described in the table below:

_Table parsed from section 'Attributes':_

* The table row entry pertains to the "Mode Select Cluster" within the "Attributes" section and describes a specific attribute change scenario: 'OnOff Change' from 'ON' to 'OFF' with 'CurrentMode Change' remaining unchanged. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage of conformance rules, it likely indicates how the system should handle this specific change scenario. If the conformance rule were included, it would specify whether this behavior is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on the presence of certain features or states. Without the explicit conformance string, we can infer that the behavior described is a standard operational scenario within the Mode Select Cluster, likely requiring specific handling as per the Matter specification guidelines.

* The table row describes an attribute change within the Mode Select Cluster, specifically focusing on the transition from 'OFF' to 'ON' for the 'OnOff Change' attribute and the corresponding change of 'CurrentMode' to 'OnMode'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance expression, it would dictate under what conditions these changes are required or optional. For instance, if the conformance were something like `M`, it would mean that this transition is mandatory for any implementation of the Mode Select Cluster. If it were `O`, it would be optional, allowing flexibility for implementations that do not require this specific behavior. The actual conformance rule would determine the necessity and conditionality of implementing these attribute changes in a device's firmware or software.

* The table row entry pertains to the "Mode Select Cluster" within the "Attributes" section, specifically addressing the behavior of the "OnOff Change" and "CurrentMode Change" attributes. The "OnOff Change" is described as transitioning from 'OFF' to 'OFF', indicating no change in the OnOff state. Similarly, the "CurrentMode Change" is noted as having 'No change', suggesting that the current mode remains constant. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it implies that these attributes are likely subject to specific conditions or states within the device's operation. If a conformance string were provided, it would dictate whether these attributes are mandatory, optional, or subject to other conditions as per the Matter specification guidelines.

* The table row entry pertains to the "Mode Select Cluster" within the "Attributes" section, specifically focusing on the behavior of the 'OnOff Change' attribute when transitioning from 'ON' to 'ON', and the 'CurrentMode Change' attribute, which remains unchanged. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it suggests that the 'OnOff Change' attribute does not require any action or update when the state remains 'ON', indicating that the attribute's behavior is consistent with maintaining the current mode without necessitating a change. This implies that the attribute is likely optional or has no significant impact in this specific scenario, aligning with the typical behavior of maintaining state consistency in IoT device operations.

The value of this field SHALL match the Mode field of one of the entries in the SupportedModes
attribute.
1.9.6.6.1. OnMode with Power Up
If the On/Off feature is supported and the On/Off cluster attribute StartUpOnOff is present, with a
value of On (turn on at power up), then the CurrentMode attribute SHALL be set to the OnMode
attribute value when the server is supplied with power, except if the OnMode attribute is null.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Mode Select Cluster, specifically the "ChangeToMode" command, which is sent from a client to a server. The command has an ID of '0x00' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required for all implementations. However, the conformance rule for this command is 'M', indicating that it is mandatory. This means that regardless of any conditions or features, the "ChangeToMode" command must be implemented in any device that supports the Mode Select Cluster.

1.9.7.1. ChangeToMode Command
NewMode
On receipt of this command, if the   field indicates a valid mode transition within the sup
NewMode
ported list, the server SHALL set the CurrentMode attribute to the   value, otherwise, the
INVALID_COMMAND
server SHALL respond with an   status response.

_Table parsed from section 'Commands':_

* In the context of the Mode Select Cluster, within the Commands section, the table row describes a command identified by 'ID' 0, named 'NewMode', which is of type 'uint8'. The 'Constraint' for this command is marked as 'desc', indicating that the specific constraints are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M', which means that the 'NewMode' command is mandatory. This implies that any implementation of the Mode Select Cluster must include this command, as it is always required according to the Matter specification.

