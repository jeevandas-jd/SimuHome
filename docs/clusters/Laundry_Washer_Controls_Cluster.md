
# 8.6 Laundry Washer Controls Cluster

This cluster provides a way to access options associated with the operation of a laundry washer
device type.

## Data Types
8.6.5.1. NumberOfRinsesEnum Type
This data type is derived from enum8.
The NumberOfRinsesEnum provides a representation of the number of rinses that will be per
formed for a selected mode. NumberOfRinsesEnum is derived from enum8. It is up to the device
manufacturer to determine the mapping between the enum values and the corresponding numbers
of rinses.

_Table parsed from section 'Data Types':_

* In the context of the Laundry Washer Controls Cluster, specifically within the Data Types section, the table row describes a mode labeled as 'None' with a value of '0'. This mode indicates that the laundry washer does not perform rinse cycles. The conformance rule for this entry is 'RINSE', which means that the 'None' mode is mandatory if the RINSE feature is supported by the device. If the RINSE feature is not supported, this mode is not required. This ensures that devices with rinse capabilities must include this mode to indicate the absence of rinse cycles.

* In the context of the Laundry Washer Controls Cluster, specifically within the Data Types section, the table row describes a mode named "Normal" with a value of '1'. This mode is designed to perform standard rinse cycles as determined by the manufacturer. The conformance rule for this entry is 'RINSE', which means that the "Normal" mode is mandatory if the RINSE feature is supported by the device. If the RINSE feature is not supported, this mode is not required. This conformance ensures that devices with the capability to perform rinse cycles must include this standard mode to maintain consistency and functionality across different implementations.

* The table row describes a data type within the Laundry Washer Controls Cluster, specifically a mode named "Extra" with a value of '2'. This mode is summarized as performing an extra rinse cycle. The conformance rule for this entry is 'RINSE', which means that the "Extra" mode is mandatory if the RINSE feature is supported by the device. If the RINSE feature is not supported, the "Extra" mode is not required. This conformance ensures that devices with the capability to perform a rinse cycle must include this additional rinse mode.

_Table parsed from section 'Data Types':_

* In the context of the Laundry Washer Controls Cluster, specifically within the Data Types section, the table row describes a feature named "Max" with a value of '3'. This feature indicates a laundry washer mode that performs the maximum number of rinse cycles as determined by the manufacturer. The conformance rule for this feature is 'RINSE', which implies that the "Max" mode is mandatory if the RINSE feature is supported by the device. If the RINSE feature is not supported, the "Max" mode is not required. This conformance condition ensures that the "Max" mode is only implemented when relevant to the device's capabilities.

## Attributes

_Table parsed from section 'Attributes':_

* In the Laundry Washer Controls Cluster, the attribute 'SpinSpeeds' is identified by the ID '0x0000' and is of the type 'list[string]', with a constraint allowing a maximum of 16 entries, each up to 64 characters long. The access level is 'R V', indicating that it is readable and can be viewed. The conformance rule 'SPIN' implies that the 'SpinSpeeds' attribute is mandatory if the feature 'SPIN' is supported by the device. If 'SPIN' is not supported, the attribute is not required. This ensures that devices with spinning capabilities must include this attribute to list the available spin speeds.

* The table row describes an attribute named "SpinSpeedCurrent" within the Laundry Washer Controls Cluster. This attribute has an ID of '0x0001' and is of type 'uint8', with a constraint limiting its maximum value to 15. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed. The 'Default' is described elsewhere in the documentation, and the 'Access' is set to 'RW VO', meaning it is readable and writable with volatile access. The 'Conformance' field is specified as 'SPIN', which implies that the attribute is mandatory if the feature 'SPIN' is supported. If 'SPIN' is not supported, the attribute is not required.

* The table row describes an attribute named "NumberOfRinses" within the Laundry Washer Controls Cluster. This attribute is identified by the ID '0x0002' and is of the type 'NumberOfRinsesEnum'. The constraints for this attribute are described elsewhere in the documentation, as indicated by 'desc'. It has a default value of '1' and can be accessed with read and write permissions, with the additional requirement of VO (Vendor Optional) access. The conformance rule 'RINSE' indicates that the inclusion of this attribute is mandatory if the feature or condition represented by 'RINSE' is supported. If the 'RINSE' feature is not supported, the attribute is not required.

* The table row describes an attribute named "SupportedRinses" within the Laundry Washer Controls Cluster, specifically in the Attributes section. This attribute has an ID of '0x0003' and is of the type 'list[NumberOfRinsesEnum]', with a constraint that limits the list to a maximum of 4 entries. The access level for this attribute is 'R V', indicating it is readable and has a volatile nature, meaning its value can change without a specific event triggering the change. The conformance rule 'RINSE' suggests that the presence of this attribute is mandatory if the feature or condition represented by 'RINSE' is supported by the device. If the device supports the 'RINSE' feature, it must implement the 'SupportedRinses' attribute; otherwise, the requirement does not apply.

8.6.6.1. SpinSpeeds Attribute
This attribute SHALL indicate the list of spin speeds available to the appliance in the currently
selected mode. The spin speed values are determined by the manufacturer. At least one spin speed
value SHALL be provided in the SpinSpeeds list. The list of spin speeds MAY change depending on
the currently selected Laundry Washer mode. For example, Quick mode might have a completely
different list of SpinSpeeds than Delicates mode.
8.6.6.2. SpinSpeedCurrent Attribute
This attribute SHALL indicate the currently selected spin speed. It is the index into the SpinSpeeds
list of the selected spin speed, as such, this attribute can be an integer between 0 and the number of
entries in SpinSpeeds - 1. If a value is received that is outside of the defined constraints, a CON
STRAINT_ERROR SHALL be sent as the response. If a value is attempted to be written that doesn’t
match a valid index (e.g. an index of 5 when the list has 4 values), a CONSTRAINT_ERROR SHALL be
sent as the response. If null is written to this attribute, there will be no spin speed for the selected
cycle. If the value is null, there will be no spin speed on the current mode.
8.6.6.3. NumberOfRinses Attribute
This attribute SHALL indicate how many times a rinse cycle SHALL be performed on a device for
the current mode of operation. A value of None SHALL indicate that no rinse cycle will be per
formed. This value may be set by the client to adjust the number of rinses that are performed for
the current mode of operation. If the device is not in a compatible state to accept the provided
value, an INVALID_IN_STATE error SHALL be sent as the response.
8.6.6.4. SupportedRinses Attribute
This attribute SHALL indicate the amount of rinses allowed for a specific mode. Each entry SHALL
indicate a NumberOfRinsesEnum value that is possible in the selected mode on the device. The
value of this attribute MAY change at runtime based on the currently selected mode. Each entry
SHALL be distinct.
8.7. Refrigerator And Temperature Controlled Cabinet
Mode Cluster
This cluster is derived from the Mode Base cluster and defines additional mode tags and name
spaced enumerated values for refrigerator and temperature controlled cabinet devices.

## Data Types
8.7.5.1. ModeOptionStruct Type
The table below lists the changes relative to the Mode Base cluster for the fields of the ModeOption
Struct type. A blank field indicates no change.

_Table parsed from section 'Data Types':_

* In the context of the Laundry Washer Controls Cluster, specifically within the Data Types section, the table row describes an element with the ID '0' and the name 'Label'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Label' data type is a required element within the Laundry Washer Controls Cluster. It must be implemented in all instances of this cluster, without any conditions or exceptions, according to the Matter IoT specification.

* In the context of the Laundry Washer Controls Cluster, specifically within the Data Types section, the table row describes an element with the ID '1' and the Name 'Mode'. The 'Conformance' field for this element is marked as 'M', which stands for Mandatory. This means that the 'Mode' data type is a required element in the implementation of the Laundry Washer Controls Cluster. It must always be included and supported, with no conditions or exceptions, according to the Matter IoT specification.

* The table row describes an entry within the Laundry Washer Controls Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'ModeTags'. It has a constraint indicating that its value should range from 1 to 8. The conformance rule for 'ModeTags' is marked as 'M', which stands for Mandatory. This means that the 'ModeTags' element is always required to be implemented in any device or application that supports the Laundry Washer Controls Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row entry pertains to the "SupportedModes" attribute within the Laundry Washer Controls Cluster, specifically under the Attributes section. The 'ID' for this attribute is '0x0000'. According to the conformance rule 'M', this attribute is classified as Mandatory. This means that the "SupportedModes" attribute is always required to be implemented in any device or application that supports the Laundry Washer Controls Cluster, without any conditions or exceptions. This ensures that all compliant devices consistently include this attribute, facilitating interoperability and standard functionality across different implementations.

* In the context of the Laundry Washer Controls Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0001' and the name 'CurrentMode'. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the 'CurrentMode' attribute is always required to be implemented in any device or application that supports the Laundry Washer Controls Cluster. There are no conditions or exceptions; it is a fundamental part of the cluster's specification.

* The table row entry for the "StartUpMode" attribute within the Laundry Washer Controls Cluster indicates that this attribute is identified by the ID '0x0002'. The conformance rule for this attribute is marked as 'X', which means it is explicitly disallowed in the current specification. This implies that the "StartUpMode" attribute should not be implemented or used within the context of the Laundry Washer Controls Cluster according to the Matter IoT specification.

* In the context of the Laundry Washer Controls Cluster, specifically within the Attributes section, the table row describes an attribute named "OnMode" with an ID of '0x0003'. The conformance rule for this attribute is marked as 'X', which means that the "OnMode" attribute is explicitly disallowed in the current specification. This indicates that the attribute should not be implemented or used within devices conforming to this version of the Matter specification for laundry washer controls.

8.7.6.1. SupportedModes Attribute
At least one entry in the SupportedModes attribute SHALL include the Auto mode tag in the Mode
Tags field list.

## Derived Cluster Namespace
This namespace includes definitions for data associated exclusively with the derived cluster.
8.7.7.1. Mode Tags
The following table defines the base and derived-cluster-specific ModeTag values.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry pertains to the "Mode Tag Value" with a hexadecimal identifier of '0x0000' and is named 'Auto' within the Laundry Washer Controls Cluster, specifically in the Derived Cluster Namespace section. The conformance rule for this entry is not explicitly provided in the data given, but if we assume it follows the standard conformance tags and expressions outlined in the Matter Conformance Interpretation Guide, it would dictate the conditions under which the 'Auto' mode is required, optional, provisional, deprecated, or disallowed. Without a specific conformance string, we cannot definitively state its requirement status. However, typically, such entries would be evaluated based on the presence or absence of certain features or conditions within the cluster, determining whether the 'Auto' mode is a necessary or optional feature for devices implementing this cluster.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry for the "Mode Tag Value" with the hexadecimal identifier '0x0001' and the name 'Quick' pertains to the Laundry Washer Controls Cluster within the Derived Cluster Namespace. This entry describes a specific mode that can be used in the context of laundry washer operations, specifically the "Quick" mode. The conformance rule for this entry is not explicitly provided in the data you shared, but if we were to interpret a typical conformance string, it would dictate the conditions under which this mode is required, optional, or otherwise specified. For instance, if the conformance were 'M', it would mean the "Quick" mode is mandatory for all implementations of this cluster. If it were 'O', it would be optional, allowing manufacturers the flexibility to include or exclude it based on their product design. Without the specific conformance string, we can only infer that the "Quick" mode is a recognized feature within the cluster, with its inclusion subject to the rules defined by

* The table row entry for the "Mode Tag Value" with a hexadecimal identifier '0x0002' and the name 'Quiet' pertains to the Laundry Washer Controls Cluster within the Derived Cluster Namespace. This entry specifies a particular mode, labeled as "Quiet," which is likely intended to reduce noise during the washer's operation. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would detail the conditions under which this mode is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean that the "Quiet" mode is a mandatory feature for all devices implementing this cluster. If it were 'O', the mode would be optional, allowing manufacturers to decide whether to include it. Without a specific conformance string, we cannot definitively state the requirement level for this mode, but the guide provides a framework for understanding how such rules would

* The table row entry for the "LowNoise" mode tag value, identified by '0x0003', within the Laundry Washer Controls Cluster's Derived Cluster Namespace, specifies how this feature should be implemented according to its conformance rule. The conformance rule for "LowNoise" is not explicitly provided in the table row data you shared, so we would need that information to interpret it accurately. However, if we assume a typical conformance scenario, such as "M" for Mandatory, it would mean that the "LowNoise" mode must always be supported by any device implementing this cluster. If the conformance were "O" for Optional, it would indicate that supporting the "LowNoise" mode is not required and has no dependencies. Without the specific conformance string, we can only outline potential interpretations based on the guide's rules.

* The table row entry pertains to the "LowEnergy" mode tag value within the Laundry Washer Controls Cluster, specifically under the Derived Cluster Namespace section. The mode tag value is identified by the hexadecimal code '0x0004'. The conformance rule for this entry is not explicitly provided in the data snippet, so we cannot directly interpret its conformance status. However, if we were to apply the Matter Conformance Interpretation Guide, we would need to know the specific conformance string associated with this entry to determine whether "LowEnergy" is mandatory, optional, provisional, deprecated, disallowed, or described elsewhere. Without this information, we can only acknowledge that "LowEnergy" is a defined mode tag value for the cluster, but its requirement status remains unspecified in this context.

* The table row entry for the "Mode Tag Value" of '0x0005', named 'Vacation', within the Laundry Washer Controls Cluster's Derived Cluster Namespace, represents a specific mode that can be set on a laundry washer. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance string, it would dictate when this 'Vacation' mode is required, optional, or otherwise specified based on the presence or absence of certain features or conditions. For instance, if the conformance were 'M', it would mean that the 'Vacation' mode is always required for any device implementing this cluster. If it were 'O', the mode would be optional and could be implemented at the manufacturer's discretion without any dependencies. The actual conformance rule would need to be specified to provide a precise interpretation.

* The table row entry for the "Mode Tag Value" of '0x0006' with the name 'Min' in the Laundry Washer Controls Cluster, under the Derived Cluster Namespace section, represents a specific mode or setting within the cluster. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate how the 'Min' mode should be implemented or supported within devices that utilize this cluster. If the conformance were specified, it would dictate whether the 'Min' mode is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply, using logical expressions and conditional rules as outlined in the Matter Conformance Interpretation Guide.

* In the context of the Laundry Washer Controls Cluster, within the Derived Cluster Namespace section, the table row describes an element with the 'Mode Tag Value' of '0x0007', named 'Max'. The conformance rule for this element is not explicitly provided in the data snippet, but if we were to interpret a typical conformance string using the guide, it would specify the conditions under which the 'Max' element is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Max' element is always mandatory. If it were 'O', it would be optional with no dependencies. Without the specific conformance string, we can only infer that the 'Max' element is a defined part of the cluster's functionality, and its inclusion or behavior would depend on the specific conformance rules applied to it as per the Matter specification.

* In the context of the Laundry Washer Controls Cluster, specifically within the Derived Cluster Namespace section, the table entry describes a feature called 'Mode Tag Value' with an identifier of '0x0008' and a name 'Night'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if we assume a typical conformance string, it would dictate when the 'Night' mode is required, optional, or otherwise specified. For instance, if the conformance string were 'M', it would mean that the 'Night' mode is a mandatory feature for devices implementing this cluster. If it were 'O', the 'Night' mode would be optional, allowing manufacturers to choose whether to include it. Without the specific conformance string, we cannot definitively state its requirement status, but the guide provides a framework for interpreting such rules when they are available.

* The table row entry pertains to the "Mode Tag Value" with a hexadecimal identifier of '0x0009', named 'Day', within the context of the Laundry Washer Controls Cluster, specifically under the Derived Cluster Namespace section. The conformance rule for this entry is not explicitly provided in the data snippet. However, if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would specify under what conditions the 'Day' mode tag is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that the 'Day' mode tag is always mandatory for implementation in this cluster. If it were 'O', it would be optional, allowing flexibility in its inclusion. Without a specific conformance string provided, we can only infer that the 'Day' mode tag is a defined element within the cluster, awaiting further context to determine its implementation requirements.

* The table row entry for the "RapidCool" mode tag value, identified by '0x4000', is part of the Laundry Washer Controls Cluster within the Derived Cluster Namespace. The conformance rule for this entry is not explicitly provided in the data snippet, so we must infer its meaning based on typical conformance patterns. If we assume a common scenario, this entry might be subject to a conformance rule such as "M" (Mandatory), "O" (Optional), or a conditional expression. Without specific conformance data, we cannot definitively state its requirement status. However, if it were marked as "M", it would mean that the "RapidCool" mode is always required for devices implementing this cluster. If marked as "O", it would be optional and not required. If a conditional expression were provided, it would specify under what conditions the "RapidCool" mode is mandatory or optional.

* In the context of the Laundry Washer Controls Cluster, specifically within the Derived Cluster Namespace section, the table entry for 'Mode Tag Value' with the identifier '0x4001' and the name 'RapidFreeze' represents a specific feature or mode that can be implemented in devices adhering to this cluster specification. The conformance rule for this entry is not explicitly provided in the data given, but if we were to interpret a typical conformance string, it would dictate when and how the 'RapidFreeze' mode should be implemented. For instance, if the conformance were 'M', it would mean that the 'RapidFreeze' mode is a mandatory feature for all devices implementing this cluster. If it were 'O', the mode would be optional, allowing manufacturers the choice to include it or not without affecting compliance. The absence of a conformance string in the provided data suggests that further context or documentation is needed to determine the exact requirements for this feature.

8.7.7.1.1. RapidCool Tag
This mode reduces the temperature rapidly, typically above freezing grade.
8.7.7.1.2. RapidFreeze Tag
This mode reduces the temperature rapidly, below freezing grade.

## Mode Examples
A few examples of Refrigerator and Temperature Controlled Cabinet modes and their mode tags
are provided below.
• For the "Normal" mode, tags: 0x0000 (Auto)
• For the "Energy Save" mode, tags: 0x0004 (LowEnergy)
• For the "Rapid Cool" mode, tags: 0x4000 (RapidCool)