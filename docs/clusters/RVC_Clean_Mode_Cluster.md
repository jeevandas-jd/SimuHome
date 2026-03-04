
# 7.3 RVC Clean Mode Cluster

This cluster is derived from the Mode Base cluster and defines additional mode tags and name
spaced enumerated values for the cleaning type of robotic vacuum cleaner devices.

## Data Types
7.3.5.1. ModeOptionStruct Type
The table below lists the changes relative to the Mode Base cluster for the fields of the ModeOption
Struct type. A blank field indicates no change.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Label" data type within the RVC Clean Mode Cluster, specifically under the Data Types section. The 'Conformance' field is marked with an 'M', indicating that this element is Mandatory. This means that the "Label" data type is always required to be implemented in any device or system that supports the RVC Clean Mode Cluster, with no exceptions or conditions.

* The table row describes an entry within the RVC Clean Mode Cluster, specifically under the Data Types section. The entry has an ID of '1' and is named 'Mode'. According to the conformance rule 'M', this indicates that the 'Mode' element is mandatory. This means that the 'Mode' data type must always be implemented and supported within the RVC Clean Mode Cluster, without any conditions or exceptions. It is a required component of the cluster's specification.

* In the context of the RVC Clean Mode Cluster, specifically within the Data Types section, the table entry for 'ModeTags' with ID '2' indicates that this element is a data type constrained to values between 1 and 8. The conformance rule for 'ModeTags' is marked as 'M', which stands for Mandatory. This means that the 'ModeTags' element is always required to be implemented in any device or application that supports the RVC Clean Mode Cluster, without any conditions or exceptions.

## Attributes
The table below lists the changes relative to the Mode Base cluster for the attributes. A blank field
indicates no change.

_Table parsed from section 'Attributes':_

* The table row entry for the RVC Clean Mode Cluster under the Attributes section describes an attribute with the ID '0x0000' named 'SupportedModes'. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance rule would dictate when this attribute is required, optional, or otherwise. For example, if the conformance were `M`, it would mean that the 'SupportedModes' attribute is always mandatory for devices implementing this cluster. If it were `O`, the attribute would be optional with no dependencies. If the conformance were a complex expression, such as `AB, O`, it would mean the attribute is mandatory if a specific feature `AB` is supported, otherwise optional. Without the specific conformance string, we cannot determine the exact requirement, but the guide provides a framework for understanding how such rules are applied.

* The table row entry for the RVC Clean Mode Cluster under the Attributes section describes an attribute with the ID '0x0001' and the name 'CurrentMode'. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string to determine when this attribute is required. For instance, if the conformance string were 'M', it would mean that the 'CurrentMode' attribute is always mandatory for implementation. If it were 'O', the attribute would be optional with no dependencies. If a more complex conformance expression were provided, it would specify conditions under which the attribute is mandatory, optional, deprecated, or disallowed, using logical operators and conditional expressions as outlined in the guide. Without the specific conformance string, we cannot definitively state the requirement status of 'CurrentMode', but the guide provides a framework for interpreting such rules when they are available.

* In the context of the RVC Clean Mode Cluster, the attribute with the ID '0x0002' and the name 'StartUpMode' is described in the table. According to the conformance rule 'X', this attribute is explicitly disallowed. This means that within the current Matter specification, the 'StartUpMode' attribute should not be implemented or supported in any device or application that adheres to this cluster's guidelines. The use of 'X' indicates a strict prohibition, ensuring that this attribute is not included in any compliant implementation.

* In the context of the RVC Clean Mode Cluster, within the Attributes section, the table row describes an attribute named 'OnMode' with an ID of '0x0003'. The conformance rule for 'OnMode' is marked as 'X', which means this attribute is explicitly disallowed. According to the Matter Conformance Interpretation Guide, this indicates that the 'OnMode' attribute should not be implemented or supported in any devices or applications adhering to the current Matter specification for this cluster.

7.3.6.1. SupportedModes Attribute
At least one entry in the SupportedModes attribute SHALL include the Vacuum and/or the Mop
mode tag in the ModeTags field list.

## Derived Cluster Namespace
This namespace includes definitions for data associated exclusively with the derived cluster.
7.3.7.1. ChangeToModeResponse Command Namespace Definitions
The following table defines the derived cluster specific StatusCode values.

_Table parsed from section 'Derived Cluster Namespace':_

* In the context of the RVC Clean Mode Cluster, specifically within the Derived Cluster Namespace section, the table row entry for 'Status Code Value' of '0x40' with the name 'CleaningInProgress' represents a specific status code used to indicate that a cleaning operation is currently underway. The conformance rule for this entry is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, if it were to be described, it would specify whether this status code is mandatory, optional, provisional, deprecated, or disallowed under certain conditions. Since the conformance rule is not included, we can assume that further details might be described elsewhere in the documentation, or it might be a straightforward mandatory or optional element depending on the broader context of the specification.

7.3.7.2. Mode Tags
The following table defines the base and derived-cluster-specific ModeTag values.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry pertains to the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" and describes a mode tag value of '0x0000', named 'Auto'. This entry specifies a particular mode within the cluster, identified by its hexadecimal value and name. However, the conformance rule for this entry is not explicitly provided in the data given. Typically, the conformance rule would dictate whether this mode is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirement status of the 'Auto' mode within the context of the Matter specification.

* The table row entry for the RVC Clean Mode Cluster within the Derived Cluster Namespace describes a mode tag value identified by '0x0001', named 'Quick'. This entry specifies a particular mode that can be used within the context of the RVC Clean Mode Cluster. The conformance rule for this entry is not explicitly provided in the data you shared, but if we were to interpret a typical conformance string, it would dictate the conditions under which the 'Quick' mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Quick' mode is mandatory for implementation in all devices supporting this cluster. If the conformance were 'O', it would indicate that the 'Quick' mode is optional and can be implemented at the discretion of the manufacturer. Without the specific conformance string, we can only infer that the 'Quick' mode is a defined option within the cluster, and its implementation depends on the

* The table row entry pertains to the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" and describes a mode tag value of '0x0002', named 'Quiet'. This entry likely represents a specific operational mode for a device or component within the Matter IoT specification, specifically for a robotic vacuum cleaner (RVC) that operates in a quieter mode. The conformance rule for this entry is not explicitly provided in the data snippet, but if we assume a typical conformance scenario, it would dictate the conditions under which the 'Quiet' mode must be implemented or supported by a device. For example, if the conformance were 'M', it would mean that the 'Quiet' mode is mandatory for all devices supporting the RVC Clean Mode Cluster. If it were 'O', the mode would be optional, allowing manufacturers the discretion to include it based on their design preferences. Understanding the specific conformance rule would require additional context or data from the specification.

* The table row entry pertains to the "LowNoise" mode tag value within the RVC Clean Mode Cluster, specifically under the Derived Cluster Namespace section. The mode tag value is identified by the hexadecimal code '0x0003'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if we assume a typical scenario where no specific conformance string is given, it might default to being optional or described elsewhere. If a conformance string were provided, it would dictate whether the "LowNoise" mode is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features. Without the specific conformance string, we can only infer that the "LowNoise" mode is a defined option within the cluster, potentially offering a quieter operational mode for devices implementing this cluster.

* The table row entry pertains to the "LowEnergy" mode tag value within the RVC Clean Mode Cluster, specifically in the context of the Derived Cluster Namespace. The mode tag value is represented by the hexadecimal code '0x0004'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret it using the Matter Conformance Interpretation Guide, we would need additional information from the 'Conformance' column to determine whether this mode is mandatory, optional, provisional, deprecated, disallowed, or described in detail elsewhere. Without this specific conformance string, we cannot definitively state the requirements or conditions under which the "LowEnergy" mode must be implemented or supported.

* The table row entry pertains to the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" section, specifically describing a mode tag value labeled as "Vacation" with a hexadecimal identifier of '0x0005'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we assume a typical conformance scenario, it would detail when this "Vacation" mode is required, optional, or otherwise specified based on the presence or absence of certain features or conditions. For instance, if the conformance were something like `AB, O`, it would mean that the "Vacation" mode is mandatory if a feature 'AB' is supported; otherwise, it is optional. Without the specific conformance string, we can only infer that the entry's inclusion in a product would depend on the conditions outlined in the full specification document.

* In the context of the RVC Clean Mode Cluster, specifically within the Derived Cluster Namespace section, the table row describes an element with the 'Mode Tag Value' of '0x0006', named 'Min'. The conformance rule for this element is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if we assume a typical conformance expression, it would dictate when this 'Min' element is required or optional. For example, if the conformance were 'M', it would mean that the 'Min' element is always mandatory. If it were 'O', it would be optional with no dependencies. Without the specific conformance string, we cannot determine the exact requirement status of this element, but the guide provides a framework for interpreting such rules when they are available.

* The table row entry for the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" section describes a feature with the 'Mode Tag Value' of '0x0007', named 'Max'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance rule would dictate when this 'Max' feature is required or optional. If the conformance were, for example, 'M', it would mean that the 'Max' feature is always mandatory. If it were 'O', it would be optional with no dependencies. If the conformance were a more complex expression like 'AB, O', it would mean the 'Max' feature is mandatory if a certain condition 'AB' is met, otherwise, it is optional. Without the specific conformance rule provided, the exact requirement status of the 'Max' feature cannot be determined.

* The table row entry pertains to the "Night" mode tag value within the RVC Clean Mode Cluster, specifically in the context of the Derived Cluster Namespace. The mode tag value is identified by the hexadecimal code '0x0008'. However, the conformance rule for this entry is not explicitly provided in the data snippet. To interpret the conformance accurately, one would need additional information from the 'Conformance' column, which is not included here. Generally, this entry would describe a specific operational mode (Night mode) for a device or system that supports the RVC Clean Mode Cluster, and its conformance would dictate whether this mode is mandatory, optional, provisional, deprecated, or disallowed based on the conditions outlined in the Matter Conformance Interpretation Guide.

* The table row entry pertains to the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on a mode tag value identified as '0x0009', which is named 'Day'. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically define the conditions under which the 'Day' mode is required, optional, or otherwise. If we assume a conformance string was provided, it would dictate whether the 'Day' mode is always required (Mandatory), not required (Optional), temporarily required (Provisional), obsolete (Deprecated), or explicitly not allowed (Disallowed). Additionally, if the conformance involved logical conditions or expressions, it would specify the dependencies on other features or conditions that determine the applicability of the 'Day' mode. Without the specific conformance string, we can only infer that the 'Day' mode is a defined operational mode within the RVC Clean Mode Cluster, potentially subject

* The table row entry describes a feature within the "RVC Clean Mode Cluster" under the "Derived Cluster Namespace" section. Specifically, it details a mode tag value of '0x4000' named 'DeepClean'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the context, it would typically indicate whether the 'DeepClean' mode is mandatory, optional, provisional, deprecated, or disallowed. If a conformance rule were provided, it would dictate the conditions under which the 'DeepClean' mode must be implemented or can be optionally included in a device's functionality. Without the specific conformance string, we cannot determine the exact requirement status of the 'DeepClean' mode.

_Table parsed from section 'Derived Cluster Namespace':_

* In the context of the RVC Clean Mode Cluster, specifically within the Derived Cluster Namespace section, the table row describes a feature with the 'Mode Tag Value' of '0x4001', named 'Vacuum'. This entry represents a specific mode or feature associated with the operation of a vacuum cleaner within the Matter IoT specification. The conformance rule for this entry is not explicitly provided in the data, but based on the guide, if it were to follow a typical conformance pattern, it would specify under what conditions this 'Vacuum' mode is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean that the 'Vacuum' mode is a mandatory feature for any device implementing this cluster. If it were 'O', it would be optional, meaning devices could support it but are not required to. Without the specific conformance string, we can only infer that this entry is a defined mode within the cluster, awaiting further context to determine

* The table row entry pertains to the "RVC Clean Mode Cluster" within the "Derived Cluster Namespace" and describes a specific mode tag value, '0x4002', named 'Mop'. This entry indicates that the 'Mop' mode is associated with the hexadecimal identifier '0x4002'. However, the conformance rule for this entry is not explicitly provided in the data, leaving its requirement status unspecified. Typically, such entries would detail whether the mode is mandatory, optional, provisional, deprecated, or disallowed based on the conformance rules. Without this information, we cannot definitively state the requirement level of the 'Mop' mode within the cluster.

7.3.7.2.1. Deep Clean Tag
While in this mode, the device is optimizing for improved cleaning.
7.3.7.2.2. Vacuum Tag
The device’s vacuuming feature is enabled in this mode.
7.3.7.2.3. Mop Tag
The device’s mopping feature is enabled in this mode.

## Mode Examples
A few examples of modes and their mode tags are provided below.
For the "Turbo, Vacuum Only" mode, tags: 0x4000 (Deep Clean), 0x4001 (Vacuum).
For the "Mop Only" mode, tags: 0x4002 (Mop), 0x0003 (Low Noise).
For the "Rapid Vacuum and Mop" mode, tags: 0x0001 (Quick), 0x4001 (Vacuum), 0x4002 (Mop).
Note that the "Low Noise" and "Quick" mode tags are defined in the generic Mode Base cluster spec
ification.