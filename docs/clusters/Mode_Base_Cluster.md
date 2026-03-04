
# 1.10 Mode Base Cluster

This cluster provides an interface for controlling a characteristic of a device that can be set to one
of several predefined values. For example, the light pattern of a disco ball, the mode of a massage
chair, or the wash cycle of a laundry machine.
The server allows the client to set a mode on the server. A mode is one of a list of options that may
be presented by a client for a user choice, or understood by the client, via the mode’s tags.
A mode tag is either a standard tag within a standard category namespace, or a manufacturer spe
cific tag, within the namespace of the vendor ID of the manufacturer.
Any derived cluster specification based on this cluster SHALL support the standard mode tag value
definitions and command status definitions defined in this cluster and MAY define additional stan
dard mode tag values and standard command status values that are supported in the respective
derived cluster instances.
Each cluster ID that indicates this specification SHALL define a distinct purpose for the cluster
instance. For example: A LightBlinking cluster ID supports blinking modes for a light (and is
described that way).
An anonymous mode SHALL NOT replace the meaning of a standard mode tag, when one exists, for
the cluster purpose.

## Data Types
1.10.5.1. ModeTagStruct Type
A Mode Tag is meant to be interpreted by the client for the purpose the cluster serves.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Mode Base Cluster, specifically under the Data Types section. The entry is for an element named "MfgCode" with an ID of '0' and a type specified as 'vendor-id'. The constraint for this element is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The conformance rule for "MfgCode" is labeled as 'O', meaning that this element is optional. This implies that the inclusion of "MfgCode" is not required and does not depend on any other features or conditions within the Matter specification.

* In the context of the Mode Base Cluster's Data Types, the table row describes an element with the ID '1', named 'Value', which is of the type 'enum16' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Value' element is always required to be implemented in any device or application that supports the Mode Base Cluster, without any conditions or exceptions. The 'enum16' type indicates that this element is an enumerated data type with 16 possible values, and the 'all' constraint suggests that all enumerated values are valid for this element.

1.10.5.1.1. MfgCode Field
If the MfgCode field exists, the Value field SHALL be in the manufacturer-specific value range (see
Section 1.10.8, “Mode Namespace”).
This field SHALL indicate the manufacturer’s VendorID and it SHALL determine the meaning of the
Value field.
The same manufacturer code and mode tag value in separate cluster instances are part of the same
namespace and have the same meaning. For example: a manufacturer tag meaning "pinch" can be
used both in a cluster whose purpose is to choose the amount of sugar, or in a cluster whose pur
pose is to choose the amount of salt.
1.10.5.1.2. Value Field
This field SHALL indicate the mode tag within a mode tag namespace which is either manufacturer
specific or standard.
1.10.5.2. ModeOptionStruct Type
This is a struct representing a possible mode of the server.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Mode Base Cluster, specifically under the Data Types section. The element is identified by the ID '0' and is named 'Label'. It is of the 'string' type with a constraint that limits its maximum length to 64 characters. The 'Quality' is marked as 'F', and it has a default value of 'MS'. The 'Conformance' field is marked as 'M', which, according to the Matter Conformance Interpretation Guide, means that this element is mandatory. Therefore, the 'Label' element must always be included and supported in any implementation of the Mode Base Cluster, without any conditions or exceptions.

* The table row describes an entry within the Mode Base Cluster, specifically under the Data Types section. The entry is identified by the ID '1' and is named 'Mode'. It is of type 'uint8', indicating it is an 8-bit unsigned integer. The 'Quality' is marked as 'F', and the default value is 'MS'. The conformance rule for this entry is 'M', which means that the 'Mode' data type is mandatory. This implies that it is always required to be implemented in any device or application that supports the Mode Base Cluster, without any conditions or exceptions.

* The table row describes an element within the Mode Base Cluster, specifically a data type called "ModeTags." This element is a list of structures, each of type "ModeTagStruct," and is constrained to a maximum of 8 entries. The "Quality" field is marked as "F," and the default value is "MS." The conformance rule for "ModeTags" is "M," which means this element is mandatory. It is always required to be implemented according to the Matter specification, with no conditions or exceptions.

1.10.5.2.1. Label Field
This field SHALL indicate readable text that describes the mode option, so that a client can provide
it to the user to indicate what this option means. This field is meant to be readable and understand
able by the user.
1.10.5.2.2. Mode Field
This field is used to identify the mode option.
1.10.5.2.3. ModeTags Field
This field SHALL contain a list of tags that are associated with the mode option. This MAY be used
by clients to determine the full or the partial semantics of a certain mode, depending on which tags
they understand, using standard definitions and/or manufacturer specific namespace definitions.
The standard mode tags are defined in this cluster specification. For the derived cluster instances, if
the specification of the derived cluster defines a namespace, the set of standard mode tags also
includes the mode tag values from that namespace.
Mode tags can help clients look for options that meet certain criteria, render the user interface, use
the mode in an automation, or to craft help text their voice-driven interfaces. A mode tag SHALL be
either a standard tag or a manufacturer specific tag, as defined in each ModeTagStruct list entry.
A mode option MAY have more than one mode tag. A mode option MAY be associated with a mix
ture of standard and manufacturer specific mode tags. A mode option SHALL be associated with at
least one standard mode tag.
A few examples are provided below.
• A mode named "100%" can have both the High (manufacturer specific) and Max (standard)
mode tag. Clients seeking the mode for either High or Max will find the same mode in this case.
• A mode that includes a LowEnergy tag can be displayed by the client using a widget icon that
shows a green leaf.
• A mode that includes a LowNoise tag may be used by the client when the user wishes for a
lower level of audible sound, less likely to disturb the household’s activities.
• A mode that includes a LowEnergy tag (standard, defined in this cluster specification) and also a
Delicate tag (standard, defined in the namespace of a Laundry Mode derived cluster).
• A mode that includes both a generic Quick tag (defined here), and Vacuum and Mop tags,
(defined in the RVC Clean cluster that is a derivation of this cluster).

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Mode Base Cluster, specifically the 'SupportedModes' attribute. This attribute is identified by the ID '0x0000' and is of the type 'list[ModeOptionStruct]', which means it is a list containing structures that define mode options. The constraint specifies that the list must contain between 2 and 255 entries. The 'Quality' is marked as 'F', and the default value is 'MS'. The 'Access' field indicates that this attribute is readable and viewable ('R V'). The conformance rule 'M' signifies that the 'SupportedModes' attribute is mandatory, meaning it is always required to be implemented in any device that supports the Mode Base Cluster, without any conditions or exceptions.

* The table row describes an attribute named "CurrentMode" within the Mode Base Cluster's Attributes section. This attribute has an ID of '0x0001' and is of type 'uint8'. The constraints on this attribute are described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'N', and it has a default value of 'MS'. The access level is 'R V', meaning it is readable and viewable. The conformance rule for "CurrentMode" is 'M', which signifies that this attribute is mandatory. It must always be implemented and supported in any device or application that uses the Mode Base Cluster, with no conditions or exceptions.

* The table row describes an attribute named "StartUpMode" within the Mode Base Cluster, identified by the ID '0x0002'. This attribute is of type 'uint8', with constraints described elsewhere in the documentation. It has a quality designation of 'NX', a default value of 'MS', and access permissions of 'Read/Write' and 'Volatile'. The conformance rule for "StartUpMode" is 'O', meaning that this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would alter its optional status. Therefore, developers can choose whether or not to include this attribute in their implementation of the Mode Base Cluster.

* The table row describes an attribute named "OnMode" within the Mode Base Cluster, identified by the ID '0x0003'. This attribute is of type 'uint8' and has a constraint that is described elsewhere in the documentation. It has a quality designation of 'NX', indicating it is not executable. The default value is 'null', and it has read-write (RW) and view-only (VO) access permissions. The conformance rule 'DEPONOF' suggests that the attribute is mandatory if the feature 'DEPONOF' is supported. If 'DEPONOF' is not supported, the conformance status is not explicitly defined in this entry, implying that further documentation might be needed to fully understand its optionality or other status in such cases.

DEPONOFF
1.10.6.1. SupportedModes Attribute
This attribute SHALL contain the list of supported modes that may be selected for the CurrentMode
attribute. Each item in this list represents a unique mode as indicated by the Mode field of the Mod
eOptionStruct.
Each entry in this list SHALL have a unique value for the Mode field.
Each entry in this list SHALL have a unique value for the Label field.
1.10.6.2. CurrentMode Attribute
This attribute SHALL indicate the current mode of the server.
The value of this field SHALL match the Mode field of one of the entries in the SupportedModes
attribute.
The value of this attribute may change at any time via an out-of-band interaction outside of the
server, such as interactions with a user interface, via internal mode changes due to autonomously
progressing through a sequence of operations, on system time-outs or idle delays, or via interac
tions coming from a fabric other than the one which last executed a ChangeToMode.
1.10.6.3. StartUpMode Attribute
This attribute SHALL indicate the desired startup mode for the server when it is supplied with
power.
If this attribute is not null, the CurrentMode attribute SHALL be set to the StartUpMode value, when
the server is powered up, except in the case when the OnMode attribute overrides the StartUpMode
attribute (see OnModeWithPowerUp).
This behavior does not apply to reboots associated with OTA. After an OTA restart, the CurrentMode
attribute SHALL return to its value prior to the restart.
The value of this field SHALL match the Mode field of one of the entries in the SupportedModes
attribute.
If this attribute is not implemented, or is set to the null value, it SHALL have no effect.
1.10.6.4. OnMode Attribute
This attribute SHALL indicate whether the value of CurrentMode depends on the state of the On/Off
cluster on the same endpoint. If this attribute is not present or is set to null, there is no dependency,
otherwise the CurrentMode attribute SHALL depend on the OnOff attribute in the On/Off cluster as
described in the table below:

_Table parsed from section 'Attributes':_

* The table row entry for the "Mode Base Cluster" under the "Attributes" section describes a specific behavior related to the 'OnOff Change' and 'CurrentMode Change' attributes. The 'OnOff Change' is specified as 'ON → OFF', indicating that this attribute involves a transition from an ON state to an OFF state. The 'CurrentMode Change' is noted as 'No change', meaning that this attribute remains unchanged during the operation. The conformance rule for this entry is not explicitly provided in the data snippet, but if it were, it would dictate the conditions under which these attributes are required, optional, or otherwise specified, based on the logical conditions and expressions outlined in the Matter Conformance Interpretation Guide. Without a specific conformance string, we can infer that the behavior described is a standard operation within the cluster, likely subject to the general rules of the Matter specification for such transitions.

* The table row entry pertains to the "Mode Base Cluster" within the "Attributes" section, specifically focusing on the behavior when there is an "OnOff Change" from 'OFF' to 'ON'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it likely describes the conditions under which the "CurrentMode Change" attribute should change the "CurrentMode" to "OnMode". If we assume a typical conformance expression, it could mean that when the device transitions from an 'OFF' state to an 'ON' state, the "CurrentMode" attribute should be updated to reflect the "OnMode". The conformance rule would dictate whether this behavior is mandatory, optional, or conditional based on specific features or conditions. Without the exact conformance string, we can infer that this behavior is likely a standard operation within the cluster, potentially mandatory when the device supports the relevant features for mode changes.

* The table row entry pertains to the "Mode Base Cluster" within the "Attributes" section, specifically focusing on the attribute related to "OnOff Change" with a transition from 'OFF → OFF' and "CurrentMode Change" indicating 'No change'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically describe the conditions under which this attribute is required or optional. If we were to apply the conformance interpretation guide, we would analyze any provided conformance string to determine whether this attribute is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions. However, since the conformance string is missing, we can only infer that this entry describes a specific behavior of the Mode Base Cluster when the OnOff state remains unchanged, and the CurrentMode does not alter, without additional conformance conditions.

* The table row entry pertains to the "Mode Base Cluster" within the "Attributes" section, specifically focusing on the attribute changes described as 'OnOff Change': 'ON → ON' and 'CurrentMode Change': 'No change'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves a condition where the attribute's behavior is described in terms of its state transitions. In this case, the 'OnOff Change' indicates that the attribute remains in the 'ON' state without transitioning, while the 'CurrentMode Change' signifies that there is no alteration in the current mode. The conformance interpretation would typically explain whether these changes are mandatory, optional, or subject to specific conditions, but without a direct conformance string provided, we can infer that the behavior is likely standard or expected under certain operational conditions within the cluster.

The value of this field SHALL match the Mode field of one of the entries in the SupportedModes
attribute.
1.10.6.4.1. OnMode with Power Up
If the On/Off feature is supported and the On/Off cluster attribute StartUpOnOff is present, with a
value of On (turn on at power up), then the CurrentMode attribute SHALL be set to the OnMode
attribute value when the server is supplied with power, except if the OnMode attribute is null.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Mode Base Cluster, specifically the "ChangeToMode" command, which is directed from the client to the server and expects a "ChangeToModeResponse" in return. The access level for this command is optional, meaning it is not required by default. However, the conformance rule for this command is marked as "M," indicating that it is mandatory. This means that, according to the Matter specification, the "ChangeToMode" command must always be implemented and supported in any device or application that utilizes the Mode Base Cluster, regardless of any other conditions or features.

* The table row describes a command within the Mode Base Cluster, specifically the "ChangeToModeResponse" command, which is directed from the server to the client. The 'Response' field indicates that this command does not require a response. The 'Conformance' field is marked as 'M', meaning that this command is mandatory. This implies that any implementation of the Mode Base Cluster must include the "ChangeToModeResponse" command as a required feature, with no conditions or exceptions.

1.10.7.1. ChangeToMode Command
This command is used to change device modes.
On receipt of this command the device SHALL respond with a ChangeToModeResponse command.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Mode Base Cluster, specifically the "NewMode" command, which is identified by the ID '0' and has a data type of 'uint8'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "NewMode" command is always required to be implemented in any device or application that supports the Mode Base Cluster, with no conditions or exceptions.

1.10.7.1.1. NewMode Field
If the NewMode field doesn’t match the Mode field of any entry of the SupportedModes list, the
ChangeToModeResponse command’s Status field SHALL indicate UnsupportedMode and the Status
Text field SHALL be included and MAY be used to indicate the issue, with a human readable string,
or include an empty string.
If the NewMode field matches the Mode field of one entry of the SupportedModes list, but the
device is not able to transition as requested, the ChangeToModeResponse command SHALL:
• Have the Status set to a product-specific Status value representing the error, or GenericFailure if
a more specific error cannot be provided. See Status field for details.
• Provide a human readable string in the StatusText field.
If the NewMode field matches the Mode field of one entry of the SupportedModes list and the
device is able to transition as requested, the server SHALL transition into the mode associated with
NewMode, the ChangeToModeResponse command SHALL have the Status field set to Success, the
StatusText field MAY be supplied with a human readable string or include an empty string and the
CurrentMode field SHALL be set to the value of the NewMode field.
If the NewMode field is the same as the value of the CurrentMode attribute the ChangeToModeRe
sponse command SHALL have the Status field set to Success and the StatusText field MAY be sup
plied with a human readable string or include an empty string.
1.10.7.2. ChangeToModeResponse Command
This command is sent by the device on receipt of the ChangeToMode command. This command
SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Mode Base Cluster, specifically the "Status" command, which is identified by the ID '0' and is of type 'enum8'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the "Status" command must always be implemented and supported in any device or application that utilizes the Mode Base Cluster, without any conditions or exceptions.

* In the Mode Base Cluster, under the Commands section, the entry for the command with ID '1', named 'StatusText', is of type 'string' with a constraint of a maximum length of 64 characters. The conformance rule for this command is specified as '[Status == Success], M'. This means that the 'StatusText' command is optional if the condition 'Status == Success' is true, indicating that it should be included when the status is successful. However, if this condition is not met, the command becomes mandatory, meaning it must be implemented regardless of the status outcome.

1.10.7.2.1. Status Field
1.10.7.2.1.1. Mode Base Status Code Ranges
The following table defines the enumeration ranges for the ChangeToModeResponse command’s
Status field values.

_Table parsed from section 'Commands':_

* In the Mode Base Cluster, under the Commands section, the table row describes a range of status codes from '0x00 to 0x3F', labeled as 'CommonCodes'. These codes represent common standard values as defined in the generic Mode Base cluster specification. The conformance rule for this entry is not explicitly provided in the data, but based on the context of the Mode Base Cluster and the typical use of such status codes, it is likely that these codes are mandatory for any implementation of the Mode Base Cluster. This means that any device or application implementing this cluster must support these common status codes to ensure interoperability and adherence to the Matter specification.

* In the Mode Base Cluster's Commands section, the table row describes a range of status codes from '0x40 to 0x7F', labeled as 'DerivedClusterCodes'. These codes represent standard values specific to derived clusters, as defined in the derived Mode Base cluster specification. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely indicates that these status codes are either mandatory or optional depending on the specific derived cluster's implementation. Without a specific conformance string, it suggests that the requirement for these codes is described elsewhere in the documentation, possibly under a more complex set of conditions or dependencies.

* In the context of the Mode Base Cluster, specifically within the Commands section, the table row describes a range of status codes from '0x80 to 0xBF' labeled as 'MfgCodes'. These codes are designated for manufacturer-specific values, meaning that for instances derived from the Mode Base cluster, these codes are reserved for use by manufacturers to define their own specific commands or statuses. The conformance rule for this entry is not explicitly stated in the provided data, but given the context of manufacturer-specific values, it is likely that the use of these codes is optional and dependent on the manufacturer's implementation. This allows manufacturers the flexibility to define custom behaviors or features within the specified range, without imposing mandatory requirements on all implementations of the Mode Base Cluster.

The set of Status field values defined in each of the generic or derived Mode Base cluster specifica
tions is called StatusCode.
1.10.7.2.1.2. Mode Base Status CommonCodes Range
The following table defines the common StatusCode values.

_Table parsed from section 'Commands':_

* The table row describes a command within the Mode Base Cluster, specifically the "Success" status code with a hexadecimal value of '0x00'. This command indicates that switching to the mode specified by the NewMode field is both allowed and feasible, resulting in the CurrentMode attribute being updated to match the NewMode field's value. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context of the "Success" status code in IoT specifications, it is typically considered a fundamental part of the command's functionality. Therefore, it is likely to be a mandatory element, meaning it is always required for the proper operation of the Mode Base Cluster commands.

* The table row entry describes a command within the Mode Base Cluster, specifically the "UnsupportedMode" command, which is identified by the status code '0x01'. This command is triggered when the value of the NewMode field does not correspond to any entries in the SupportedModes attribute, indicating that the requested mode is not supported by the device. The conformance rule for this command is not explicitly provided in the row data, but based on the context of the Matter specification, it would typically be interpreted as a mandatory command for devices implementing the Mode Base Cluster. This means that any device supporting this cluster must implement the "UnsupportedMode" command to handle cases where an unsupported mode is requested.

_Table parsed from section 'Commands':_

* The table row entry describes a command within the Mode Base Cluster, specifically the 'GenericFailure' command, which is identified by the status code '0x02'. This command is used to indicate a generic failure, meaning that switching to the mode specified by the NewMode field is either not allowed or not possible. The conformance rule for this command is not explicitly provided in the data, but based on the context, it would typically be interpreted as a mandatory or optional command depending on the specific conditions or features supported by the device. Without a specific conformance string, we assume that the command's inclusion is determined by the broader requirements of the Mode Base Cluster or the specific implementation details of the device.

* The table row entry pertains to the "Mode Base Cluster" within the "Commands" section and describes a status code labeled "InvalidInMode" with a hexadecimal value of '0x03'. This status code indicates that the device cannot process a received request because it is currently in a mode that does not support the requested action. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it is likely that the "InvalidInMode" status code is a mandatory element for devices implementing the Mode Base Cluster. This means that any device supporting this cluster must be able to return this status code when a request is incompatible with the device's current mode.

that switching to the mode is not allowed or possible, as indicated by the relevant status code.
The derived cluster code definitions SHALL NOT duplicate the common code definitions. For exam
ple, a derived cluster specification SHALL NOT define a status code with the same semantic as the
common code of 0x01 (UnsupportedMode).
If the Status field is set to Success, the StatusText field is optional.
If the Status field is set to UnsupportedMode, the StatusText field SHALL be an empty string.
If the Status field is not set to Success or UnsupportedMode, the StatusText field SHALL include a
vendor-defined error description which can be used to explain the error to the user. For example, if
the Status field is set to InvalidInMode, the StatusText field SHOULD indicate why the transition to
the requested mode is not allowed, given the current mode of the device, which may involve other
clusters.

## Mode Namespace
This section provides the definitions of the mode tag ranges and of the common standard mode tag
values available in the instances of this cluster.
The following table defines the enumeration ranges for the ModeTagStruct Value field values.

_Table parsed from section 'Mode Namespace':_

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" section, specifically focusing on the "Mode Tag Value Range" from '0x0000 to 0x3FFF', which is named "CommonTags". This range encompasses common standard values as defined in the cluster specification. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it likely indicates that these values are a standard part of the specification. If the conformance were to be described, it would typically specify whether these values are mandatory, optional, or subject to certain conditions as per the Matter Conformance Interpretation Guide. However, without a specific conformance string, we can infer that these values are integral to the cluster's operation, serving as a baseline for common functionalities.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" section, specifically addressing the "Mode Tag Value Range" from '0x4000 to 0x7FFF'. This range is designated as 'DerivedClusterTags', which refers to standard values that are specific to derived clusters, as defined in their respective specifications. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves conditions or dependencies described elsewhere in the documentation. This means that the applicability or requirement of these tag values is determined by additional specifications or conditions that are not directly stated in this entry.

* The table row describes a specific range of values, from `0x8000` to `0xBFFF`, within the Mode Base Cluster's Mode Namespace, labeled as "MfgTags." These values are designated for manufacturer-specific purposes, meaning that they are reserved for use by manufacturers to define custom behaviors or features within derived cluster instances. The conformance rule for this entry is not explicitly provided, but given the context of manufacturer-specific tags, it is likely that these values are optional and can be utilized at the manufacturer's discretion to implement proprietary features. The absence of a specific conformance tag suggests that the use of these values is not mandated by the Matter specification, allowing flexibility for manufacturers to define their own implementations.

defined in this cluster specifica
turer specific under the derived
The derived cluster specific standard value definitions SHALL not duplicate the common standard
value definitions. For example, a derived cluster specification can’t define a mode tag value with
the same mode as the common standard tag value of 0x0001 (Quick).
The set of ModeTagStruct Value field values defined in each of the generic or derived Mode Base
cluster specifications is called ModeTag.
The following table defines the common ModeTag values.

_Table parsed from section 'Mode Namespace':_

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a specific mode tag value, '0x0000', named 'Auto'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance status would dictate whether the 'Auto' mode is mandatory, optional, provisional, deprecated, or disallowed. If a conformance string were provided, it would specify under what conditions the 'Auto' mode must be implemented or can be omitted. For instance, if the conformance were 'M', the 'Auto' mode would be a mandatory feature of the Mode Base Cluster, meaning it must always be supported. If it were 'O', it would be optional, allowing flexibility in implementation. Without the specific conformance string, we can only describe the potential implications based on the guide's rules.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a feature identified as 'Mode Tag Value' with the hexadecimal code '0x0001', named 'Quick'. The conformance rule for this entry is not explicitly provided in the data snippet, so we cannot determine its exact conformance status (e.g., Mandatory, Optional, etc.) based on the provided information. Typically, the conformance field would specify conditions under which this feature is required or optional, using the rules outlined in the Matter Conformance Interpretation Guide. Without this specific conformance data, we can only acknowledge that 'Quick' is a named feature within the Mode Base Cluster, but its implementation requirements remain unspecified here.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a feature identified by the 'Mode Tag Value' of '0x0002', named 'Quiet'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically specify whether the 'Quiet' mode is mandatory, optional, provisional, deprecated, or disallowed. If we assume a common conformance scenario, such as 'M', it would mean that the 'Quiet' mode is a mandatory feature that must be implemented in any device supporting the Mode Base Cluster. Without the specific conformance string, we cannot definitively state its requirement status, but it would be interpreted according to the rules outlined in the Matter Conformance Interpretation Guide if provided.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a feature or attribute identified by the 'Mode Tag Value' of '0x0003', named 'LowNoise'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret any conformance string associated with 'LowNoise' to determine its requirement status. For instance, if the conformance was 'M', 'LowNoise' would be a mandatory feature for any device implementing the Mode Base Cluster. If it were 'O', it would be optional, allowing implementers to include it at their discretion without any dependencies. If a more complex conformance expression were provided, it would dictate the conditions under which 'LowNoise' is required, optional, or otherwise, based on the presence or absence of other features or conditions.

* The table row entry for the Mode Base Cluster, specifically within the Mode Namespace, describes a feature identified by the 'Mode Tag Value' of '0x0004', named 'LowEnergy'. The conformance rule for this entry is not explicitly provided in the data snippet, so we must infer its meaning based on the context and the rules outlined in the Matter Conformance Interpretation Guide. Generally, if a conformance rule were provided, it would specify under what conditions the 'LowEnergy' feature is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that the 'LowEnergy' feature is always mandatory. If it were 'O', it would be optional with no dependencies. Without a specific conformance string, we can only assume that the feature's inclusion is determined by other documentation or context-specific rules not included in the snippet.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a specific mode tag value labeled "Vacation" with a hexadecimal identifier of '0x0005'. The conformance rule for this entry is not explicitly provided in the data you shared, so we cannot directly interpret its conformance status. However, if a conformance string were provided, it would dictate whether the "Vacation" mode tag is mandatory, optional, provisional, deprecated, or disallowed based on the conditions outlined in the Matter Conformance Interpretation Guide. This would determine how and when this mode tag should be implemented or supported within devices that adhere to the Matter specification.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" section, specifically focusing on the element identified as 'Mode Tag Value' with the hexadecimal code '0x0006', named 'Min'. The conformance rule for this element is not explicitly provided in the data snippet, so we must infer its status based on the context or additional documentation. Generally, if the conformance rule were included, it would dictate whether the 'Min' element is mandatory, optional, provisional, deprecated, or disallowed, or if its requirement is conditional based on the presence of other features. Without a specific conformance string, we assume that further details would be described elsewhere in the documentation, potentially under a "described" conformance tag, indicating that the requirement for 'Min' is complex and context-dependent.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" section, specifically describing a feature or attribute named "Max" with a mode tag value of '0x0007'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret any conformance string provided to determine the conditions under which "Max" is required, optional, or otherwise. For example, if the conformance string were `M`, it would mean that "Max" is a mandatory element within the Mode Base Cluster. If it were `O`, it would be optional, and if a more complex expression were provided, we would use logical conditions to determine its status based on the presence or absence of certain features. However, since the conformance string is not included here, we cannot specify its exact requirement status without additional information.

* The table row entry for the "Mode Tag Value" of '0x0008' with the "Name" 'Night' pertains to the Mode Base Cluster within the Mode Namespace. This entry specifies a particular mode identified as 'Night'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context of the Mode Namespace, it would typically define whether the 'Night' mode is mandatory, optional, provisional, deprecated, or disallowed. If the conformance were to be provided, it would dictate the conditions under which the 'Night' mode must be implemented or can be optionally included in a device's feature set, following the rules outlined in the Matter Conformance Interpretation Guide.

* The table row entry pertains to the "Mode Base Cluster" within the "Mode Namespace" and describes a feature identified as "Mode Tag Value" with the hexadecimal code '0x0009', named "Day". The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate how the "Day" mode should be implemented concerning its necessity or optionality. If we assume a conformance rule was provided, it would dictate whether the "Day" mode is mandatory, optional, provisional, deprecated, or disallowed, or if its implementation depends on certain conditions or features being supported. Without the specific conformance string, we can't determine its exact requirement status, but the guide would help interpret it if available.

1.10.8.1. Auto Tag
The device decides which options, features and setting values to use.
1.10.8.2. Quick Tag
The mode of the device is optimizing for faster completion.
1.10.8.3. Quiet Tag
The device is silent or barely audible while in this mode.
1.10.8.4. LowNoise Tag
Either the mode is inherently low noise or the device optimizes for that.
1.10.8.5. LowEnergy Tag
The device is optimizing for lower energy usage in this mode. Sometimes called "Eco mode".
1.10.8.6. Vacation Tag
A mode suitable for use during vacations or other extended absences.
1.10.8.7. Min Tag
The mode uses the lowest available setting value.
1.10.8.8. Max Tag
The mode uses the highest available setting value.
1.10.8.9. Night Tag
The mode is recommended or suitable for use during night time.
1.10.8.10. Day Tag
The mode is recommended or suitable for use during day time.