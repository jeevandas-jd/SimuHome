
# 9.6 Water Heater Mode Cluster

This cluster is derived from the Mode Base cluster and defines additional mode tags and name
spaced enumerated values for water heater devices.

## Data Types
9.6.5.1. ModeOptionStruct Type
The table below lists the changes relative to the Mode Base cluster for the fields of the ModeOption
Struct type. A blank field indicates no change.

_Table parsed from section 'Data Types':_

* In the Water Heater Mode Cluster, within the Data Types section, the table row describes an element with the ID '0' and the name 'Label'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Label' data type is a required element in the Water Heater Mode Cluster and must be implemented in all instances of this cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, indicating its fundamental importance in the cluster's functionality.

* In the Water Heater Mode Cluster, under the Data Types section, the table row with ID '1' pertains to an element named 'Mode'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'Mode' element is a required component of the Water Heater Mode Cluster and must be implemented in all instances of this cluster without any conditions or exceptions.

* In the context of the Water Heater Mode Cluster, specifically within the Data Types section, the table entry for 'ModeTags' with an ID of '2' indicates that this element is a data type with a constraint allowing values from 1 to 8. The conformance rule for 'ModeTags' is marked as 'M', which means that this element is mandatory. Therefore, 'ModeTags' must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row entry for the Water Heater Mode Cluster under the Attributes section, with ID '0x0000' and Name 'SupportedModes', represents an attribute that specifies the modes supported by a water heater. The conformance rule for this attribute is not explicitly provided in the data given. However, based on the Matter Conformance Interpretation Guide, if the conformance were specified, it would dictate whether the 'SupportedModes' attribute is mandatory, optional, provisional, deprecated, or disallowed, possibly with conditions based on other features or elements. For example, if the conformance were 'M', it would mean that the 'SupportedModes' attribute is always required for any implementation of the Water Heater Mode Cluster. If it were 'O', it would be optional, allowing flexibility in implementation. The actual conformance rule would determine the necessity and conditions under which this attribute must be implemented in devices supporting the Water Heater Mode Cluster.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "CurrentMode" within the Water Heater Mode Cluster, identified by the ID '0x0001'. The conformance rule for this attribute is not explicitly provided in the data snippet, so we must infer its meaning based on the provided context and rules. If we assume a typical conformance scenario, the attribute's conformance could be described using the Matter Conformance Interpretation Guide. For instance, if the conformance were 'M', it would mean that the "CurrentMode" attribute is mandatory and must always be implemented in any device supporting the Water Heater Mode Cluster. If the conformance were 'O', it would indicate that the attribute is optional and can be implemented at the discretion of the device manufacturer. Without a specific conformance string, we cannot definitively state the requirement level for "CurrentMode," but it is crucial to refer to the full specification document to understand its exact conformance requirements.

* In the Water Heater Mode Cluster, under the Attributes section, the entry for 'StartUpMode' with ID '0x0002' has a conformance designation of 'X'. According to the Matter Conformance Interpretation Guide, 'X' indicates that the 'StartUpMode' attribute is explicitly disallowed. This means that within the current specification, the 'StartUpMode' attribute should not be implemented or used in any devices or applications that conform to this standard.

* In the Water Heater Mode Cluster, within the Attributes section, the entry for 'OnMode' with ID '0x0003' has a conformance designation of 'X'. According to the Matter Conformance Interpretation Guide, 'X' signifies that the 'OnMode' attribute is explicitly disallowed. This means that within the current specification, the 'OnMode' attribute is not permitted to be implemented or used in any context related to the Water Heater Mode Cluster.

9.6.6.1. SupportedModes Attribute
At least one entry in the SupportedModes attribute SHALL include the Manual mode tag in the
ModeTags field list.
At least one entry in the SupportedModes attribute SHALL include the Off mode tag in the Mode
Tags field list.
An entry in the SupportedModes attribute that includes one of an Off, Manual, or Timed tag SHALL
NOT also include an additional instance of any one of these tag types.

## Derived Cluster Namespace
This namespace includes definitions for data associated exclusively with the derived cluster.
9.6.7.1. Mode Tags
The following table defines the base and derived-cluster-specific ModeTag values.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry describes a feature within the Water Heater Mode Cluster, specifically a mode tag value labeled 'Auto' with a hexadecimal identifier of '0x0000'. The conformance rule for this entry is not explicitly provided in the data you shared, so we cannot directly interpret its conformance status. However, if we assume a typical scenario where the conformance might be 'M', it would mean that the 'Auto' mode is a mandatory feature for devices implementing the Water Heater Mode Cluster. If the conformance were 'O', it would indicate that the 'Auto' mode is optional and can be included at the manufacturer's discretion. Without the specific conformance string, we can only speculate based on standard interpretations.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" and describes a mode tag value labeled "Quick" with a hexadecimal identifier of '0x0001'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if we assume a typical conformance string, it would dictate when the "Quick" mode is required, optional, or otherwise specified. For instance, if the conformance were 'M', it would mean that the "Quick" mode is a mandatory feature of the Water Heater Mode Cluster. If it were 'O', it would be optional, allowing manufacturers to include it at their discretion. Without a specific conformance string provided, we cannot definitively state its requirement status, but the guide would be used to interpret any such string if it were available.

* In the context of the Water Heater Mode Cluster, specifically within the Derived Cluster Namespace, the table entry describes a feature with the 'Mode Tag Value' of '0x0002', named 'Quiet'. The conformance rule for this entry is not explicitly provided in the data you've shared, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string to determine the conditions under which the 'Quiet' mode is required, optional, or otherwise. If the conformance string were, for example, 'M', it would mean that the 'Quiet' mode is a mandatory feature for any implementation of the Water Heater Mode Cluster. If it were 'O', it would indicate that the 'Quiet' mode is optional and can be included at the discretion of the implementer. Without the specific conformance string, we cannot determine the exact requirement status of the 'Quiet' mode, but the guide provides a framework for interpreting such rules when they are available.

* The table row entry pertains to the "LowNoise" mode tag value within the Water Heater Mode Cluster, identified by the hexadecimal code '0x0003'. This entry is situated in the Derived Cluster Namespace section. The conformance rule for this entry is not explicitly provided in the data, but if we were to interpret a typical conformance string, it would dictate the conditions under which the "LowNoise" mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the "LowNoise" mode is always mandatory for devices implementing this cluster. If it were 'O', the mode would be optional, allowing manufacturers to include it at their discretion. Without a specific conformance string provided, we can only assume that the "LowNoise" mode has a defined role within the cluster, potentially enhancing the functionality of water heaters by offering a quieter operational mode.

* The table row entry pertains to the "LowEnergy" mode tag value within the Water Heater Mode Cluster, specifically in the Derived Cluster Namespace section. The mode tag value is identified by the hexadecimal code '0x0004'. The conformance rule for this entry is not explicitly provided in the data you've shared, but typically, it would indicate whether the "LowEnergy" mode is mandatory, optional, provisional, deprecated, or disallowed based on certain conditions or feature support. If the conformance string were provided, it would define when and how the "LowEnergy" mode should be implemented in devices supporting the Water Heater Mode Cluster, following the rules outlined in the Matter Conformance Interpretation Guide.

* The table row entry pertains to the "Mode Tag Value" with a hexadecimal identifier of '0x0005', named 'Vacation', within the Water Heater Mode Cluster, specifically in the Derived Cluster Namespace section. The conformance rule for this entry is not explicitly provided in the data, but if we assume it follows the typical conformance patterns, it would specify under what conditions the 'Vacation' mode is required, optional, or otherwise categorized. For instance, if the conformance were 'M', it would mean that the 'Vacation' mode is a mandatory feature of the Water Heater Mode Cluster. If it were 'O', it would be optional, allowing for flexibility in implementation. Without a specific conformance string provided, we can only infer that the 'Vacation' mode is a recognized mode within the cluster, and its implementation would depend on the specific conformance rules outlined in the Matter specification for this cluster.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" section, specifically addressing the "Mode Tag Value" identified by the hexadecimal code '0x0006', which is named 'Min'. The conformance rule for this entry is not explicitly provided in the data snippet, so we cannot determine its specific requirements or optionality based on the provided information. Typically, the conformance field would dictate whether the 'Min' mode tag value is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features. Without this conformance data, we can only identify that 'Min' is a recognized mode tag value within the Water Heater Mode Cluster.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" and describes a feature with the 'Mode Tag Value' of '0x0007', named 'Max'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate whether the 'Max' mode is mandatory, optional, provisional, deprecated, or disallowed within the cluster. If a conformance string were provided, it would specify the conditions under which the 'Max' mode must be implemented or can be omitted, using the rules outlined in the Matter Conformance Interpretation Guide. For instance, if the conformance were 'M', it would mean that the 'Max' mode is always required in the Water Heater Mode Cluster.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" identified as '0x0008', which is named 'Night'. The conformance rule for this entry is not explicitly provided in the data given, so we cannot directly interpret its conformance status using the provided guide. However, if we assume a typical scenario where conformance rules apply, this entry would describe the conditions under which the 'Night' mode is required, optional, or otherwise specified for a water heater's operational modes. If the conformance were specified, it would indicate whether the 'Night' mode is a mandatory feature, optional, provisional, deprecated, or disallowed, or if its conformance depends on certain conditions or features being present.

* In the context of the Water Heater Mode Cluster, specifically within the Derived Cluster Namespace section, the table entry describes a mode tag value labeled 'Day' with a hexadecimal identifier of '0x0009'. The conformance rule for this entry is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, it would typically specify whether the 'Day' mode is mandatory, optional, provisional, deprecated, or disallowed. If a conformance expression were provided, it would indicate under what conditions the 'Day' mode must be supported or can be optionally implemented, using logical conditions and feature dependencies. Without a specific conformance string, we assume that additional documentation or context is needed to determine its precise requirement status.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" with a hexadecimal identifier of '0x4000' and the name 'Off'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically specify whether the 'Off' mode is a mandatory, optional, provisional, deprecated, or disallowed feature within the cluster. If the conformance were provided, it would dictate the conditions under which the 'Off' mode must be implemented or can be omitted, using logical expressions and conditionality as outlined in the Matter Conformance Interpretation Guide. Without the specific conformance string, we cannot determine the exact requirement status of this mode.

* The table row entry for the Water Heater Mode Cluster, specifically within the Derived Cluster Namespace, describes a feature called 'Mode Tag Value' with a hexadecimal identifier of '0x4001' and a name 'Manual'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we can infer that if a conformance string were present, it would dictate the conditions under which the 'Manual' mode is required, optional, or otherwise specified. For instance, if the conformance were 'M', it would mean the 'Manual' mode is always required. If it were 'O', it would be optional with no dependencies. Without the specific conformance string, we cannot definitively state the requirements for this feature, but the guide provides a framework for understanding how such rules would be interpreted.

* The table row entry pertains to the "Water Heater Mode Cluster" within the "Derived Cluster Namespace" section, specifically detailing a mode tag value labeled as "Timed" with a hexadecimal identifier of '0x4002'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically describe the conditions under which the "Timed" mode is required, optional, or otherwise specified according to the Matter specification. If a conformance string were provided, it would dictate whether the "Timed" mode must always be implemented (Mandatory), can be optionally included (Optional), is temporarily included with future changes expected (Provisional), is obsolete (Deprecated), or is not allowed (Disallowed). Additionally, if the conformance involved logical conditions or dependencies on other features, it would specify these using logical operators and conditional expressions to clarify when the "Timed" mode should be applied.

9.6.7.1.1. Off Tag
While in modes with this tag, the device will not attempt to keep the water warm.
9.6.7.1.2. Manual Tag
While in modes with this tag, the device will attempt to keep the water warm based on the Occu
piedHeatingSetpoint attribute of the associated Thermostat cluster.
9.6.7.1.3. Timed Tag
While in modes with this tag, the device will attempt to keep the water warm based on the Sched
ules attribute of the associated Thermostat cluster.

## Mode Examples
A few examples of Water Heater modes and their mode tags are provided below.
• For the "Off" mode, tags: 0x4000 (Off)
• For the "Manual" mode, tags: 0x4001 (Manual)
• For the "Timed" mode, tags: 0x4002 (Timed)