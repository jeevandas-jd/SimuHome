
# 9.8 Device Energy Management Mode Cluster

This cluster is derived from the Mode Base cluster and defines additional mode tags and name
spaced enumerated values for Device Energy Management devices.

## Data Types
9.8.5.1. ModeOptionStruct Type
The table below lists the changes relative to the Mode Base cluster for the fields of the ModeOption
Struct type. A blank field indicates no change.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Data Types" section and describes an element with the ID '0' and the name 'Label'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Label' element is always required to be implemented in any device or application that supports the Device Energy Management Mode Cluster. There are no conditions or exceptions to this requirement, making the inclusion of the 'Label' element non-negotiable according to the Matter specification.

* The table row describes an entry within the Device Energy Management Mode Cluster, specifically under the Data Types section. The entry is identified by the ID '1' and is named 'Mode'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Mode' data type is always required to be implemented in any device or system that supports the Device Energy Management Mode Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Mode Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'ModeTags'. It has a constraint that allows for a range of 1 to 8, indicating the permissible values or instances for this data type. The conformance rule for 'ModeTags' is marked as 'M', which stands for Mandatory. This means that the 'ModeTags' element is always required to be implemented in any device or application that supports the Device Energy Management Mode Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row entry for the "SupportedModes" attribute within the Device Energy Management Mode Cluster indicates that this attribute is part of the cluster's attributes section. The conformance rule for this attribute is not explicitly provided in the data snippet, so we must assume a default interpretation based on typical conformance practices. If we consider a common scenario where no specific conformance string is given, the attribute might be considered optional unless specified otherwise in the broader documentation. Therefore, the "SupportedModes" attribute likely represents a list or set of modes that the device can support in terms of energy management, and its inclusion in a device's implementation would depend on the specific requirements or capabilities of that device as outlined in the Matter specification. If the conformance string were provided, it would dictate whether this attribute is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on other features or elements.

* The table row entry for the "CurrentMode" attribute within the Device Energy Management Mode Cluster specifies its unique identifier as '0x0001'. The conformance rule for this attribute is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string if it were available. Typically, the conformance string would indicate whether the "CurrentMode" attribute is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions. For example, if the conformance were 'M', it would mean that the "CurrentMode" attribute is always required in any implementation of the Device Energy Management Mode Cluster. If it were 'AB, O', it would mean the attribute is mandatory if feature 'AB' is supported, otherwise optional. Without the specific conformance string, we can only describe the attribute's role and potential conformance scenarios based on the guide.

* In the context of the Device Energy Management Mode Cluster, specifically within the Attributes section, the table row describes an attribute identified by the ID `0x0002` and named `StartUpMode`. The conformance rule for this attribute is marked as `X`, which means that the `StartUpMode` attribute is explicitly disallowed according to the Matter specification. This indicates that the attribute should not be implemented or used within this cluster, as it is not permitted by the current standards.

* In the context of the Device Energy Management Mode Cluster, specifically within the Attributes section, the table row describes an attribute with the ID '0x0003' and the name 'OnMode'. The conformance rule for this attribute is marked as 'X', which means it is explicitly disallowed according to the Matter specification. This indicates that the 'OnMode' attribute should not be implemented or used in any devices or applications that conform to the current version of the Matter specification.

9.8.6.1. SupportedModes Attribute
At least one entry in the SupportedModes attribute SHALL include the NoOptimization mode tag in
the ModeTags field.
At least one entry in the SupportedModes attribute SHALL include the LocalOptimization mode tag
in the ModeTags field list.
At least one entry in the SupportedModes attribute SHALL include the GridOptimization mode tag
in the ModeTags field list.
An entry in the SupportedModes attribute that includes one of an DeviceOptimization, LocalOpti
mization, or GridOptimization tags SHALL NOT also include NoOptimization tag.

## Derived Cluster Namespace
This namespace includes definitions for data associated exclusively with the derived cluster.
9.8.7.1. Mode Tags
The following table defines the base and derived-cluster-specific ModeTag values.

_Table parsed from section 'Derived Cluster Namespace':_

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a specific mode tag value, '0x0000', which is named 'Auto'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if it were to be included, it would specify when the 'Auto' mode is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Auto' mode is mandatory for all devices implementing this cluster. If it were 'O', the 'Auto' mode would be optional, allowing devices to implement it at their discretion. The absence of a specific conformance rule in the provided data suggests that further context from the documentation would be necessary to determine the exact requirements for the 'Auto' mode.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a feature identified by the 'Mode Tag Value' of '0x0001', named 'Quick'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the guide, it would specify under what conditions the 'Quick' mode is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean that the 'Quick' mode is a mandatory feature for devices implementing this cluster. If it were 'O', it would be optional, allowing manufacturers the flexibility to include or exclude it without affecting compliance. The absence of a specific conformance rule in the provided data suggests that further context or documentation might be needed to fully understand its implementation requirements.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" identified as '0x0002', which is named 'Quiet'. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically indicate how the 'Quiet' mode should be implemented in terms of its necessity or optionality. If a conformance rule were provided, it would dictate whether the 'Quiet' mode is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on other features or elements. Without a specific conformance string, we cannot determine its exact requirement status, but it would typically guide developers on how to implement this mode in compliance with the Matter specification.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" with a hexadecimal identifier of '0x0003' and the name 'LowNoise'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context of the Matter Conformance Interpretation Guide, if a conformance rule were given, it would dictate the conditions under which the 'LowNoise' mode is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that the 'LowNoise' mode is always required. If it were 'O', it would be optional with no dependencies. The specific conformance rule would guide implementers on how to handle the 'LowNoise' mode in their device energy management implementations.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" of '0x0004', which is named 'LowEnergy'. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically indicate how the 'LowEnergy' mode should be implemented in devices supporting this cluster. If we assume a conformance rule, it might specify whether the 'LowEnergy' mode is mandatory, optional, or subject to specific conditions based on the presence or absence of certain features. For instance, if the conformance were 'M', it would mean that the 'LowEnergy' mode is a mandatory feature for any device implementing the Device Energy Management Mode Cluster. However, without the specific conformance string, we cannot definitively interpret its requirement status.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on a mode identified by the tag value '0x0005', named 'Vacation'. The conformance rule for this entry is not explicitly provided in the data, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the 'Vacation' mode is a feature within this cluster. If a conformance rule were provided, it would dictate whether the 'Vacation' mode is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or feature support. Without a specific conformance string, we cannot determine its exact requirement status, but it would typically be described in the broader context of the cluster's documentation.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section, specifically focusing on the "Mode Tag Value" with a hexadecimal identifier of '0x0006', named 'Min'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate whether the 'Min' mode tag value is mandatory, optional, provisional, deprecated, or disallowed within the cluster. If the conformance rule were provided, it would specify under what conditions this mode tag value must be implemented or can be omitted, using logical expressions and conditions as outlined in the Matter Conformance Interpretation Guide. Without the specific conformance string, we can only infer that the 'Min' mode tag value is a defined element within the cluster, awaiting further details on its implementation requirements.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a feature identified by the 'Mode Tag Value' of '0x0007', which is named 'Max'. The conformance rule for this feature is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which the 'Max' feature is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', the 'Max' feature would be mandatory for all implementations of this cluster. If it were 'O', it would be optional, allowing implementers to choose whether to include it without any dependencies. If a more complex expression were provided, it would specify conditions based on the support of other features or elements, using logical operators and conditional expressions to define when 'Max' should be included.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a feature identified by the "Mode Tag Value" of '0x0008', which is named "Night". The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it would typically indicate whether the "Night" mode is mandatory, optional, provisional, deprecated, or disallowed within the cluster. If the conformance rule were provided, it would specify under what conditions the "Night" mode must be implemented or can be omitted, using the logical expressions and conditional rules outlined in the Matter Conformance Interpretation Guide. Without the specific conformance string, we cannot determine the exact requirements for the "Night" mode, but it would generally guide implementers on how to handle this mode in their device energy management solutions.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a specific mode tag value, '0x0009', which is named 'Day'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if a conformance rule were present, it would dictate the conditions under which the 'Day' mode tag is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the 'Day' mode tag is always required. If it were 'O', it would be optional with no dependencies. Without a specific conformance rule provided, we cannot determine the exact requirement status for this mode tag within the cluster.

* In the Device Energy Management Mode Cluster, within the Derived Cluster Namespace section, the table row describes a feature called "NoOptimization" with a Mode Tag Value of '0x4000'. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically specify when the "NoOptimization" mode is required or optional. If we assume a conformance string was provided, it would dictate the conditions under which this mode must be implemented or can be optionally included in a device's functionality. For instance, if the conformance were 'M', it would mean that the "NoOptimization" mode is always required. If it were 'O', it would mean that the mode is optional and can be included at the discretion of the device manufacturer. Without a specific conformance string, we can only infer that the "NoOptimization" mode is a defined feature within the cluster, awaiting further specification on its implementation requirements.

* The table row entry pertains to the "DeviceOptimization" feature within the Device Energy Management Mode Cluster, specifically under the Derived Cluster Namespace section. The 'Mode Tag Value' assigned to this feature is '0x4001'. The conformance rule for this entry is not explicitly provided in the data you shared, so I cannot directly interpret its conformance status. However, if we assume a typical scenario where a conformance string is present, it would dictate when the "DeviceOptimization" feature is required, optional, provisional, deprecated, or disallowed based on the presence or absence of certain conditions or features. Without the specific conformance string, we can only acknowledge that this entry defines a feature related to optimizing device energy management, identified by its unique tag value.

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a feature identified by the "Mode Tag Value" of '0x4002', named "LocalOptimization". The conformance rule for this feature is not explicitly provided in the data snippet, but based on the context, it would typically indicate whether the "LocalOptimization" feature is mandatory, optional, provisional, deprecated, or disallowed according to the Matter specification. If a conformance string were provided, it would dictate the conditions under which this feature must be implemented in devices supporting the Device Energy Management Mode Cluster, using logical expressions and conditional rules as outlined in the Matter Conformance Interpretation Guide. Without the specific conformance string, we cannot determine the exact requirements for "LocalOptimization".

* The table row entry pertains to the "Device Energy Management Mode Cluster" within the "Derived Cluster Namespace" section. It describes a feature identified by the 'Mode Tag Value' of '0x4003', named 'GridOptimization'. The conformance rule for this feature is not explicitly provided in the data snippet, but based on the context of the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate when the 'GridOptimization' feature is required or optional. For instance, if the conformance were 'M', it would mean that 'GridOptimization' is a mandatory feature for devices implementing this cluster. If it were 'O', the feature would be optional, allowing flexibility in its implementation. The absence of a conformance string in the provided data suggests that the specific conditions or requirements for 'GridOptimization' might be detailed elsewhere in the documentation or are assumed to be understood within the context of the cluster's overall requirements.

9.8.7.1.1. NoOptimization Tag
The device prohibits optimization of energy usage management: its energy usage is determined
only by the user configuration and internal device needs.
9.8.7.1.2. DeviceOptimization Tag
The device is permitted to manage its own energy usage. For example, using tariff information it
may obtain.
9.8.7.1.3. LocalOptimization Tag
The device permits management of energy usage by an energy manager to optimize the local
energy usage.
9.8.7.1.4. GridOptimization Tag
The device permits management of energy usage by an energy manager to optimize the grid energy
usage.

## Mode Examples
A few examples of Device Energy Management modes and their mode tags are provided below.
• For the "No Energy Management (Forecast reporting only)" mode, tags: 0x4000 (NoOptimiza
tion).
• For the "Device Energy Management" mode, tags: 0x4001 (DeviceOptimization).
• For  the  "Home  Energy  Management"  mode,  tags:  0x4001  (DeviceOptimization),  0x4002
(LocalOptimization).
• For the "Grid Energy Management" mode, tags: 0x4003 (GridOptimization).
• For the "Full Energy Management" mode, tags: 0x4001 (DeviceOptimization), 0x4002 (LocalOpti
mization), 0x4003 (GridOptimization).
Chapter 10. Network Infrastructure
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter.
10.1. General Description

## Introduction
The clusters specified in this section are used to control network infrastructure devices, such as
home internet gateways, Wi-Fi access points, Thread Border Routers, etc.

## Cluster List
This section lists the clusters specified in this document, and gives examples of typical usage for the
purpose of clarification.
Table 17. Clusters Specified in the Network Infrastructure Functional Domain

_Table parsed from section 'Cluster List':_

* The table row entry pertains to the "Wi-Fi Network Management" cluster within the "Device Energy Management Mode Cluster" context, identified by the Cluster ID '0x0451'. This cluster is responsible for handling requests related to Wi-Fi network details. The conformance rule for this cluster is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, the conformance would dictate when and how this cluster is required to be implemented in a device. For example, if the conformance were 'M', it would mean that the Wi-Fi Network Management cluster is mandatory for all devices supporting the Device Energy Management Mode Cluster. If it were 'O', it would be optional, allowing manufacturers the discretion to include it based on their device's capabilities and intended functionality. The specific conformance rule would determine the necessity and conditions under which this cluster must be supported.

* The table row describes a cluster within the Device Energy Management Mode Cluster, specifically the "Thread Border Router Management" cluster, identified by the Cluster ID `0x0452`. This cluster is responsible for managing a Thread Border Router or Network, which is crucial for facilitating communication and connectivity within a Thread network. The conformance rule for this cluster is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate whether the inclusion of this cluster is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on the support of other features or elements. Without a specific conformance string, we cannot determine the exact requirement status of this cluster.

* The table row describes an entry for the "Thread Network Directory Cluster" within the "Device Energy Management Mode Cluster" context. This cluster, identified by the Cluster ID '0x0453', serves as a directory for Thread networks and Border Routers. The conformance rule for this cluster is not explicitly provided in the row, but based on the context, it would typically indicate whether the inclusion of this cluster is mandatory, optional, or subject to specific conditions. If the conformance rule were provided, it would specify under what conditions the cluster must be implemented, using the rules outlined in the Matter Conformance Interpretation Guide. For instance, if the conformance were 'M', it would mean that the cluster is always required. If it were 'O', the cluster would be optional, and if a more complex expression were provided, it would detail specific conditions under which the cluster is required or optional.

