
# 1.2 Identify Cluster

This cluster supports an endpoint identification state (e.g., flashing a light), that indicates to an
observer (e.g., an installer) which of several nodes and/or endpoints it is. It also supports a multi
cast request that any endpoint that is identifying itself to respond to the initiator.
The state of this cluster MAY be shared on more than one endpoint on a node.
For Example: Two endpoints on a single node, one a temperature sensor, and one a humidity
sensor, may both share the same cluster instance and therefore identification state (e.g. single
LED on the node).

## Data Types
1.2.4.1. IdentifyTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the "Identify Cluster" under the "Data Types" section, the table row describes an entry with the value '0x00' and the name 'None', which has a summary stating 'No presentation.' The conformance rule for this entry is 'M', which stands for Mandatory. This means that the element is always required to be implemented in any device or application that supports the Identify Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it a fundamental component of the cluster's data types.

* The table row describes a data type within the Identify Cluster, specifically for a feature named "LightOutput," which is identified by the value '0x01'. This feature pertains to the light output of a lighting product. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that supports the Identify Cluster. There are no conditions or exceptions; the LightOutput feature must be included to comply with the Matter specification for this cluster.

* In the context of the Identify Cluster's Data Types, the table row describes an element named "VisibleIndicator," which is typically a small LED, with a value of '0x02'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the VisibleIndicator is a required component in any implementation of the Identify Cluster according to the Matter specification. It must be included and supported without any conditions or exceptions.

* The table row describes an entry within the "Identify Cluster" under the "Data Types" section, specifically for a data type named "AudibleBeep" with a value of '0x03'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "AudibleBeep" data type is always required to be implemented in any device or application that supports the Identify Cluster according to the Matter IoT specification. There are no conditions or exceptions; it must be included as part of the standard implementation.

* The table row describes an element within the "Identify Cluster" under the "Data Types" section, specifically a data type named "Display" with a value of '0x04'. The summary indicates that this element pertains to the presentation being visible on a display screen. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Display" data type is always required to be implemented according to the Matter specification, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the "Identify Cluster" section, specifically for an element named "Actuator" with a value of '0x05'. The summary indicates that this element is related to functionalities such as operating a window blind or an in-wall relay, which are examples of actuator presentations. The conformance rule for this element is 'M', meaning it is mandatory. This indicates that the "Actuator" data type is always required to be implemented in any device or application that supports the Identify Cluster, without any conditions or exceptions.

1.2.4.2. EffectIdentifierEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the "Identify Cluster" under the "Data Types" section, specifically detailing a data type with the value '0x00' and the name 'Blink'. The summary indicates that this data type represents an action where, for example, a light is turned on and off once. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Blink' data type is always required to be implemented in any device or application that supports the Identify Cluster according to the Matter specification. There are no conditions or exceptions; it must be included as a fundamental part of the cluster's functionality.

* The table row entry pertains to the "Identify Cluster" within the "Data Types" section of the Matter specification. It describes a data type with the value '0x01' named 'Breathe'. The summary indicates that this data type represents an action where, for example, a light is turned on and off over a duration of one second and this cycle is repeated 15 times. The conformance rule for this entry is 'M', which means that the 'Breathe' data type is mandatory. This implies that any implementation of the Identify Cluster must include support for this 'Breathe' data type, as it is a required element without any conditions or exceptions.

* In the context of the Identify Cluster's Data Types, the table row describes an entry with the 'Value' of '0x02' and the 'Name' of 'Okay'. The 'Summary' suggests that this entry is used to indicate a successful operation, such as a colored light turning green for one second or a non-colored light flashing twice. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'Okay' entry is a required element in the specification and must be implemented in all devices that support the Identify Cluster, without any conditions or exceptions.

* The table row describes a data type within the "Identify Cluster" context, specifically focusing on the "ChannelChange" element. This element is identified by the value '0x0B' and is summarized as a behavior where, for example, a colored light turns orange for 8 seconds, while a non-colored light adjusts its brightness to maximum for 0.5 seconds and then to minimum for 7.5 seconds. The conformance rule for "ChannelChange" is marked as 'M', which means it is a Mandatory element. This indicates that the "ChannelChange" feature must always be implemented and supported in any device or application that conforms to this part of the Matter specification.

* The table row describes an entry within the "Identify Cluster" under the "Data Types" section, specifically focusing on a data type named "FinishEffect" with a value of '0xFE'. The "FinishEffect" is intended to complete the current effect sequence before terminating, such as finishing a breathe effect before stopping. The conformance rule for "FinishEffect" is marked as 'M', which stands for Mandatory. This means that the "FinishEffect" data type is always required to be implemented in any device or application that supports the Identify Cluster, ensuring that the functionality to complete ongoing effects before termination is consistently available.

* In the context of the Identify Cluster's Data Types, the table row describes an entry with the value `0xFF`, named `StopEffect`. This entry is summarized as a command to terminate the effect as soon as possible. The conformance rule for `StopEffect` is marked as `M`, which means it is a Mandatory element. This indicates that the `StopEffect` command must always be implemented and supported in any device or application that adheres to the Matter specification for the Identify Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

1.2.4.3. EffectVariantEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Identify Cluster's Data Types, the table row describes an entry with the value `0x00` and the name "Default," which signifies that the default effect is used. The conformance rule for this entry is marked as `M`, indicating that it is mandatory. This means that the "Default" effect must always be implemented and supported in any device or application that adheres to the Matter specification for this cluster. There are no conditions or exceptions; the inclusion of this element is required without any dependencies or optionality.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "IdentifyTime" within the "Identify Cluster" under the "Attributes" section. This attribute has an ID of '0x0000' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The "Constraint" is listed as 'all', indicating that it applies universally without specific restrictions. Its default value is '0', and it has 'RW VO' access, meaning it is readable and writable, with the 'VO' suggesting it may have volatile characteristics. The conformance rule 'M' indicates that the "IdentifyTime" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Identify Cluster, without any conditions or exceptions.

* The table row describes an attribute named "IdentifyType" within the "Identify Cluster" under the "Attributes" section. This attribute is of the type "IdentifyTypeEnum" and has a constraint described elsewhere in the documentation. Its default value is "MS," and it has read-only access with the ability to be viewed (denoted by 'R V'). The conformance rule for this attribute is 'M', indicating that it is mandatory. This means that the "IdentifyType" attribute must always be implemented and supported in any device or application using the Identify Cluster according to the Matter specification.

1.2.5.1. IdentifyTime Attribute
This attribute SHALL represent the remaining length of time, in seconds, that the endpoint will con
tinue to identify itself.
If this attribute is set to a value other than 0 then the device SHALL enter its identification state, in
order to indicate to an observer which of several nodes and/or endpoints it is. It is RECOMMENDED
that this state consists of flashing a light with a period of 0.5 seconds. The IdentifyTime attribute
SHALL be decremented every second while in this state.
If this attribute reaches or is set to the value 0 then the device SHALL terminate its identification
state.
1.2.5.2. IdentifyType Attribute
This attribute SHALL indicate how the identification state is presented to the user.
This attribute SHALL contain one of the values defined in IdentifyTypeEnum. The value None
SHALL NOT be used if the device is capable of presenting its identification state using one of the
other methods defined in IdentifyTypeEnum.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Identify Cluster, specifically the "Identify" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning it must be implemented. The conformance rule for this command is 'M', which signifies that the "Identify" command is always required and must be supported by any implementation of the Identify Cluster. There are no conditions or dependencies affecting this requirement, making it a straightforward mandatory element in the Matter specification.

* The table row describes a command named "TriggerEffect" within the Identify Cluster, which is directed from the client to the server. The command has an ID of '0x40' and requires a response from the server, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning that any implementation of this cluster must support this command. The 'Conformance' field is marked as 'O', which stands for Optional. This means that while the command is defined and available for use, it is not required for all implementations of the Identify Cluster. Devices or applications can choose to implement this command based on their specific needs or capabilities, but they are not obligated to do so.

1.2.6.1. Identify Command
This command starts or stops the receiving device identifying itself.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes an entry within the "Identify Cluster" under the "Commands" section, specifically focusing on the "IdentifyTime" command. This command is of type `uint16`, indicating it is a 16-bit unsigned integer, and it applies universally as indicated by the "Constraint" being "all." The "Conformance" field is marked as "M," which stands for Mandatory. This means that the "IdentifyTime" command is a required element within the Identify Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

1.2.6.1.1. Effect on Receipt
On receipt of this command, the device SHALL set the IdentifyTime attribute to the value of the
IdentifyTime field. This then starts, continues, or stops the device’s identification state as detailed in
IdentifyTime.
1.2.6.2. TriggerEffect Command
This command allows the support of feedback to the user, such as a certain light effect. It is used to
allow an implementation to provide visual feedback to the user under certain circumstances such
as a color light turning green when it has successfully connected to a network. The use of this com
mand and the effects themselves are entirely up to the implementer to use whenever a visual feed
back is useful but it is not the same as and does not replace the identify mechanism used during
commissioning.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command named "EffectIdentifier" within the "Identify Cluster" context, specifically under the "Commands" section. The command is of the type "EffectIdentifierEnum" and has constraints that are described elsewhere in the documentation. The conformance rule for this command is marked as "M," which means it is mandatory. This indicates that the "EffectIdentifier" command is always required to be implemented in any device or application that supports the Identify Cluster, without any conditions or exceptions.

* The table row entry pertains to the "Identify Cluster" within the "Commands" section and describes a command named "EffectVariant" with an ID of '1'. This command is of the type "EffectVariantEnum" and has constraints that are described elsewhere in the documentation. The conformance rule for "EffectVariant" is marked as 'M', which means it is mandatory. This indicates that the "EffectVariant" command must always be implemented and supported in any device or application that adheres to this part of the Matter specification, without any conditions or exceptions.

1.2.6.2.1. EffectIdentifier Field
This field SHALL indicate the identify effect to use and SHALL contain one of the non-reserved val
ues in EffectIdentifierEnum.
All values of the EffectIdentifierEnum SHALL be supported. Implementors MAY deviate from the
example light effects in EffectIdentifierEnum, but they SHOULD indicate during testing how they
handle each effect.
1.2.6.2.2. EffectVariant Field
This field SHALL indicate which variant of the effect, indicated in the EffectIdentifier field, SHOULD
be triggered. If a device does not support the given variant, it SHALL use the default variant. This
field SHALL contain one of the values in EffectVariantEnum.
1.2.6.2.3. Effect on Receipt
On receipt of this command, the device SHALL execute the trigger effect indicated in the EffectIden
tifier and EffectVariant fields. If the EffectVariant field specifies a variant that is not supported on
the device, it SHALL execute the default variant.