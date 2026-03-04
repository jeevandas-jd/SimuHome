
# 9.4 Energy EVSE Mode Cluster

This cluster is derived from the Mode Base cluster and defines additional mode tags and name
spaced enumerated values for EVSE devices.

## Data Types
9.4.5.1. ModeOptionStruct Type
The table below lists the changes relative to the Mode Base cluster for the fields of the ModeOption
Struct type. A blank field indicates no change.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Mode Cluster, specifically within the Data Types section, the table row describes an element with the ID '0' and the name 'Label'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'Label' data type is a required element within this cluster and must always be implemented according to the Matter specification. There are no conditions or exceptions; it is essential for compliance with the standard.

* The table row describes an entry within the Energy EVSE Mode Cluster, specifically under the Data Types section. The entry has an ID of '1' and is named 'Mode'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Mode' data type is always required to be implemented in any device or system that supports the Energy EVSE Mode Cluster. There are no conditions or dependencies affecting its requirement; it must be included in all implementations without exception.

* The table row entry pertains to the "ModeTags" data type within the Energy EVSE Mode Cluster, specifically under the section for Data Types. The "ID" for this entry is '2', and it has a constraint indicating that its value should range from 1 to 8. The conformance rule for "ModeTags" is marked as 'M', which stands for Mandatory. This means that the "ModeTags" data type is always required to be implemented in any device or application that supports the Energy EVSE Mode Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row entry for the "SupportedModes" attribute within the "Energy EVSE Mode Cluster" under the "Attributes" section is identified by the ID '0x0000'. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance string would dictate the conditions under which the "SupportedModes" attribute is required, optional, or otherwise specified. If the conformance string were, for example, `M`, it would mean that the "SupportedModes" attribute is always mandatory. If it were `O`, the attribute would be optional with no dependencies. If a more complex expression were provided, it would specify conditions based on the presence or absence of certain features or other elements, determining whether the attribute is mandatory, optional, deprecated, or disallowed. The specific conformance rule would guide implementers on how to handle this attribute in their Matter-compliant devices.

* The table row describes an attribute named "CurrentMode" within the Energy EVSE Mode Cluster, identified by the ID '0x0001'. The conformance rule for this attribute is not explicitly provided in the prompt, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance string would dictate when the "CurrentMode" attribute is required. If, for instance, the conformance was 'M', it would mean that the "CurrentMode" attribute is mandatory and must always be implemented in devices using the Energy EVSE Mode Cluster. If it were 'O', it would be optional, allowing for flexibility in implementation. The specific conformance string would provide detailed guidance on the conditions under which this attribute is required, optional, or otherwise specified, ensuring that developers understand how to implement it in compliance with the Matter specification.

* In the context of the Energy EVSE Mode Cluster, specifically within the Attributes section, the table row describes an attribute identified by the ID '0x0002' and named 'StartUpMode'. The conformance rule for this attribute is marked as 'X', which means it is explicitly disallowed. This indicates that within the current specification of the Matter IoT standard, the 'StartUpMode' attribute should not be implemented or used in any devices or applications that adhere to this cluster's guidelines.

* In the context of the Energy EVSE Mode Cluster, specifically within the Attributes section, the table row describes an attribute identified by the ID '0x0003' and named 'OnMode'. The conformance rule for this attribute is marked as 'X', which means it is explicitly disallowed. This indicates that the 'OnMode' attribute is not permitted to be implemented or used within this cluster according to the current Matter specification.

9.4.6.1. SupportedModes Attribute
At least one entry in the SupportedModes attribute SHALL include the Manual mode tag in the
ModeTags field list.
Modes with entries in the SupportedModes attribute which contain multiple mode tags permitting
charging or discharging under different conditions SHALL permit the charging or discharging to
occur if any of the conditions are satisfied.
Modes SHALL NOT have both the Manual tag and the TimeOfUse or SolarCharging tags defined in
the SupportedModes attribute.

## Derived Cluster Namespace
This namespace includes definitions for data associated exclusively with the derived cluster.
9.4.7.1. Mode Tags
The following table defines the base and derived-cluster-specific ModeTag values.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry pertains to the "Mode Tag Value" with a hexadecimal identifier of '0x0000' and is named 'Auto' within the context of the Energy EVSE Mode Cluster, specifically under the Derived Cluster Namespace section. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the guide, it would dictate when and how the 'Auto' mode is required or optional. For instance, if the conformance were 'M', it would mean that the 'Auto' mode is always mandatory for implementation. If it were 'O', it would be optional, allowing flexibility in its implementation. Without a specific conformance rule provided, we cannot definitively state its requirement status, but the guide would help interpret any such rule if it were available.

* The table row entry pertains to the "Mode Tag Value" with a hexadecimal identifier of '0x0001' and is named 'Quick' within the Energy EVSE Mode Cluster's Derived Cluster Namespace. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would specify under what conditions this 'Quick' mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Quick' mode is a mandatory feature of the Energy EVSE Mode Cluster, always required to be implemented. If it were 'O', it would be optional, allowing flexibility in implementation. Without a specific conformance string provided, we can only assume that the 'Quick' mode is a defined feature within this cluster, and its implementation requirements would depend on the actual conformance rule associated with it in the full specification.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section. It describes a specific mode tag value, '0x0002', which is named 'Quiet'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would specify the conditions under which the 'Quiet' mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Quiet' mode is always mandatory for devices implementing this cluster. If it were 'O', the 'Quiet' mode would be optional with no dependencies. Without the specific conformance string, we can only infer that the 'Quiet' mode is a defined mode tag value within this cluster, and its implementation would depend on the conformance rules set forth in the full specification document.

* In the context of the Energy EVSE Mode Cluster, specifically within the Derived Cluster Namespace section, the table row describes a feature with the 'Mode Tag Value' of '0x0003' and the 'Name' of 'LowNoise'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if we assume a conformance string was given, it would dictate the conditions under which the 'LowNoise' mode is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that the 'LowNoise' mode is always required. If it were 'O', it would be optional with no dependencies. Without a specific conformance string, we can only infer that the 'LowNoise' mode is a defined feature within this cluster, and its implementation would depend on the specific conformance rules outlined elsewhere in the documentation.

* In the context of the Energy EVSE Mode Cluster, specifically within the Derived Cluster Namespace section, the table row describes an element with the 'Mode Tag Value' of '0x0004', named 'LowEnergy'. The conformance rule for this element is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret any conformance string associated with this element to determine its requirement status. For example, if the conformance were 'M', it would mean that the 'LowEnergy' mode is always required. If it were 'O', it would be optional without dependencies. If a more complex expression were provided, such as 'AB, O', it would mean the 'LowEnergy' mode is mandatory if feature 'AB' is supported, otherwise optional. Without the specific conformance string, we can only outline potential interpretations based on the guide.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically describing a mode tag value labeled "Vacation" with a hexadecimal identifier of '0x0005'. The conformance rule for this entry is not explicitly provided in the data, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the "Vacation" mode tag value is a feature or attribute within the Energy EVSE Mode Cluster. If a conformance rule were provided, it would dictate whether this mode is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply. Without a specific conformance string, we cannot determine the exact requirements or conditions for the "Vacation" mode, but it would typically be used to define a specific operational state or behavior for an EVSE (Electric Vehicle Supply Equipment) when the system is set to a vacation mode, potentially affecting how energy is managed or consumed during this period.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" with a hexadecimal identifier of '0x0006', named 'Min'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance status would dictate whether the 'Min' mode tag value is mandatory, optional, provisional, deprecated, disallowed, or described in more detail elsewhere. Without a specific conformance string, it is unclear what the exact requirement is, but this entry likely defines a specific operational mode or setting within the Energy EVSE Mode Cluster, which could be critical for ensuring compatibility and functionality in devices that implement this cluster.

* The table row entry for the Energy EVSE Mode Cluster, specifically within the Derived Cluster Namespace section, describes a feature with the 'Mode Tag Value' of '0x0007' and the 'Name' 'Max'. The conformance rule for this entry is not explicitly provided in the data given, but if we were to interpret a typical conformance expression, it would dictate when this 'Max' mode tag is required or optional based on certain conditions or features. For instance, if the conformance were something like `AB, O`, it would mean that the 'Max' mode is mandatory if feature 'AB' is supported; otherwise, it is optional. Without a specific conformance expression provided, we can only assume that the conformance status would be detailed elsewhere in the documentation, possibly under a 'desc' tag, indicating a complex conformance condition.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on a mode tag value labeled as "Night" with a hexadecimal identifier of '0x0008'. The conformance rule for this entry is not explicitly provided in the data, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance status would dictate when and how this "Night" mode tag value should be implemented within the cluster. If the conformance were specified, it would indicate whether this mode is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply. Without the specific conformance string, we cannot determine the exact implementation requirements for the "Night" mode tag value.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically describing a mode tag value labeled as "Day" with a hexadecimal identifier of "0x0009". The conformance rule for this entry is not explicitly provided in the data snippet. However, if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would specify the conditions under which the "Day" mode tag value is required, optional, or otherwise. For instance, if the conformance were "M", it would indicate that the "Day" mode tag is always mandatory. If it were "O", it would mean the mode tag is optional and has no dependencies. Without a specific conformance string provided, we can only infer that the "Day" mode tag is a defined element within the cluster, but its requirement status is not detailed in the given data.

* In the context of the Energy EVSE Mode Cluster, specifically within the Derived Cluster Namespace section, the table row describes a feature with the 'Mode Tag Value' of '0x4000' and the 'Name' 'Manual'. The conformance rule for this feature is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which this 'Manual' mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Manual' mode is always required. If it were 'O', it would be optional with no dependencies. The absence of a conformance string in the provided data suggests that further documentation or context is needed to determine the specific conformance requirements for this feature.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically describing a feature identified by the 'Mode Tag Value' of '0x4001', named 'TimeOfUse'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate how the 'TimeOfUse' feature should be implemented within devices supporting the Energy EVSE Mode Cluster. If a conformance rule were provided, it would specify whether the 'TimeOfUse' feature is mandatory, optional, provisional, deprecated, or disallowed, or if its implementation depends on certain conditions or features being supported. Without the specific conformance string, we cannot determine the exact requirement for 'TimeOfUse', but it would be interpreted using the rules outlined in the Matter Conformance Interpretation Guide.

* The table row describes a feature within the Energy EVSE Mode Cluster, specifically in the Derived Cluster Namespace section. The entry is for a mode tag with the value '0x4002', named 'SolarCharging'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string (if provided) to determine whether the 'SolarCharging' mode is mandatory, optional, provisional, deprecated, or disallowed. Without the specific conformance string, we cannot definitively state its requirement status. However, if a conformance string were provided, it would dictate the conditions under which the 'SolarCharging' mode must be implemented or can be optionally included in a device supporting the Energy EVSE Mode Cluster.

* The table row entry pertains to the "Energy EVSE Mode Cluster" within the "Derived Cluster Namespace" section, specifically describing a mode tag value identified as '0x4003' with the name 'V2X'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate how the 'V2X' mode should be implemented within the cluster. If a conformance rule were provided, it would specify whether the 'V2X' mode is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply. For example, if the conformance were 'M', it would mean that the 'V2X' mode is a mandatory feature of the Energy EVSE Mode Cluster. If the conformance were a complex expression, it would detail the specific conditions under which 'V2X' is required or optional, using logical operators and feature codes as defined in the Matter Conformance

9.4.7.1.1. Manual Tag
While in modes with this tag, and once enabled with the EnableCharging command, the EVSE will
permit charging based on demand from the EV.
9.4.7.1.2. TimeOfUse Tag
While in modes with this tag, and once enabled with the EnableCharging command, the EVSE will
attempt to automatically start charging based on the user’s charging targets (for example, set based
on a Time of Use tariff to charge at the cheapest times of the day).
9.4.7.1.3. SolarCharging Tag
While in modes with this tag, and once enabled with the EnableCharging, the EVSE will attempt to
automatically start charging based on available excess solar PV generation, limiting the charging
power to avoid importing energy from the grid.
9.4.7.1.4. V2X Tag
While in modes with this tag, and once enabled with the EnableDischarging command, the EVSE
will permit discharging based on the current charge state of the EV, and its control from an associ
ated Device Energy Management cluster.
being  in  a  mode  with  this  tag  set  or  not  does  not  affect  the  handling  of  the
NOTE EnableDischarging command by the Energy EVSE cluster, but once enabled, only
modes with this tag enable the discharging to actually occur.

## Mode Examples
A few examples of EVSE modes and their mode tags are provided below.
• For the "Manual" mode, tags: 0x4000 (Manual)
• For the "Auto-scheduled" mode, tags: 0x4001 (TimeOfUse)
• For the "Solar" mode, tags: 0x4002 (SolarCharging)
• For the "Auto-scheduled with Solar charging" mode, tags: 0x4001 (TimeOfUse), 0x4002 (Solar
Charging)
• For the "Vehicle-to-home with Solar charging" mode, tags: 0x4002 (SolarCharging), 0x4003 (V2X)