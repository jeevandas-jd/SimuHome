
# 8.13 Microwave Oven Control Cluster

This cluster defines the requirements for the Microwave Oven Control cluster.
This cluster has dependencies with the Operational State and Microwave Oven Mode clusters. The
Operational State cluster and the Microwave Oven Mode clusters, or derivatives of those clusters
SHALL appear on the same endpoint as this cluster.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Microwave Oven Control Cluster, specifically the "CookTime" attribute. This attribute is identified by the ID '0x0000' and is of type 'elapsed-s', which likely represents elapsed seconds. It has a constraint that limits its value between 1 and a maximum defined by 'MaxCookTime', with a default value set to 30. The access level is 'R V', indicating it is readable and possibly volatile. The conformance rule for this attribute is 'M', meaning it is mandatory. This implies that the "CookTime" attribute must always be implemented in any device or application that supports the Microwave Oven Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "MaxCookTime" within the Microwave Oven Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0001' and is of type 'elapsed-s', which likely represents elapsed seconds. It has a constraint that limits its value between 1 and 86400, indicating it can represent a maximum cook time from 1 second to 24 hours. The quality is marked as 'F', and the default value is 'MS'. The access level is 'R V', suggesting it is readable and possibly volatile. The conformance rule for "MaxCookTime" is 'M', meaning this attribute is mandatory and must always be implemented in any device supporting the Microwave Oven Control Cluster, without any conditions or dependencies.

* The table row describes an attribute named "PowerSetting" within the Microwave Oven Control Cluster. This attribute has an ID of '0x0002' and is of type 'uint8', with constraints and default values that are described elsewhere in the documentation. The access level for this attribute is 'R V', indicating it is readable and can be viewed. The conformance rule 'PWRNUM' specifies that the "PowerSetting" attribute is mandatory if the feature 'PWRNUM' is supported. If 'PWRNUM' is not supported, the attribute is not required. This means that the inclusion of the "PowerSetting" attribute is conditional upon the support of the 'PWRNUM' feature within the device or implementation.

* The table row describes an attribute named "MinPower" within the Microwave Oven Control Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0003' and is of type 'uint8', with a value constraint ranging from 1 to 99. It has a default value of 10 and is accessible for reading and viewing (denoted by 'R V'). The 'Quality' field is marked as 'F', which might indicate a specific quality or feature level, though this is not detailed in the provided context. The conformance rule 'PWRLMTS' indicates that the "MinPower" attribute is mandatory if the feature or condition represented by 'PWRLMTS' is supported. If 'PWRLMTS' is not supported, the attribute is not required. This suggests that the inclusion of "MinPower" is contingent upon the presence of specific power limit features within the device's capabilities.

* The table row describes an attribute named "MaxPower" within the Microwave Oven Control Cluster's Attributes section. This attribute has an ID of '0x0004' and is of type 'uint8', with a value constraint ranging from one unit above 'MinPower' to a maximum of 100. The quality of this attribute is marked as 'F', indicating a specific quality level defined in the broader specification. Its default value is set to 100, and it has read and view access permissions ('R V'). The conformance for this attribute is specified as 'PWRLMTS', which means that the attribute is mandatory if the feature or condition represented by 'PWRLMTS' is supported. If 'PWRLMTS' is not supported, the attribute is not required. This conformance rule ensures that the 'MaxPower' attribute is included in implementations where power limits are a relevant feature.

* The table row describes an attribute named "PowerStep" within the Microwave Oven Control Cluster. This attribute has an ID of '0x0005' and is of type 'uint8', with a default value of 10. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. It has a quality of 'F' and access permissions of 'R V', meaning it can be read and is volatile. The conformance rule 'PWRLMTS' indicates that the attribute is mandatory if the feature or condition represented by 'PWRLMTS' is supported. If 'PWRLMTS' is not supported, the attribute is not required. The conformance rule does not specify any fallback options, so the attribute's requirement is solely dependent on the presence of the 'PWRLMTS' feature.

* The table row describes an attribute named "SupportedWatts" within the Microwave Oven Control Cluster. This attribute is identified by the ID '0x0006' and is a list of unsigned 16-bit integers, constrained to contain between 1 and 10 entries. The attribute has a quality of 'F', a default value of 'MS', and access permissions of 'R V', indicating it is readable and viewable. The conformance rule 'P, WATTS' indicates that the "SupportedWatts" attribute is currently provisional, meaning its status is temporary and may change in the future. Specifically, it will become mandatory if the feature 'WATTS' is supported. If 'WATTS' is not supported, the attribute remains provisional.

* The table row describes an attribute named "SelectedWattIndex" within the Microwave Oven Control Cluster's Attributes section. This attribute has an ID of '0x0007' and is of type 'uint8'. Its constraints are described elsewhere in the documentation, and it has a default value of 'MS'. The access level is read-only and volatile ('R V'). The conformance rule 'P, WATTS' indicates that the "SelectedWattIndex" attribute is currently provisional, meaning its status is temporary and subject to change. However, if the feature 'WATTS' is supported, this attribute becomes mandatory. In essence, the attribute is in a transitional state but will be required if the microwave oven supports the 'WATTS' feature.

* The table row describes an attribute named "WattRating" within the Microwave Oven Control Cluster, identified by the ID '0x0008'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally ('Constraint': 'all'). The 'Quality' is marked as 'F', and it has a default value of 'MS'. The 'Access' is specified as 'R V', indicating that it can be read and is volatile. The 'Conformance' for this attribute is 'O', which means it is optional. This implies that the inclusion of the "WattRating" attribute is not mandatory and does not depend on any other features or conditions; it can be implemented at the discretion of the device manufacturer.

8.13.5.1. CookTime Attribute
This attribute SHALL indicate the total cook time associated with the operation of the device.
This attribute SHALL remain unchanged during the operation of the oven unless the value is
changed via a command or out-of-band action.
8.13.5.2. MaxCookTime Attribute
This attribute SHALL indicate the maximum value to which the CookTime attribute can be set.
8.13.5.3. PowerSetting Attribute
This attribute SHALL indicate the power level associated with the operation of the device.
If the MinPower, MaxPower, and PowerStep attributes are not supported:
• The minimum value of this attribute SHALL be 10,
• The maximum value of this attribute SHALL be 100,
• The value SHALL be in even multiples of 10,
• The default value SHALL be 100.
If the MinPower, MaxPower, and PowerStep attributes are supported:
• The value of this attribute SHALL be between MinPower and MaxPower inclusive.
(PowerSetting - MinPower) % PowerStep == 0
• The value of this attribute SHALL be such that
8.13.5.4. MinPower Attribute
This attribute SHALL indicate the minimum value to which the PowerSetting attribute that can be
set on the server.
8.13.5.5. MaxPower Attribute
This attribute SHALL indicate the maximum value to which the PowerSetting attribute that can be
set on the server.
8.13.5.6. PowerStep Attribute
This attribute SHALL indicate the increment of power that can be set on the server.
The value of this attribute SHALL be between 1 and MaxPower inclusive.
(MaxPower - MinPower) % PowerStep == 0
The value of this attribute SHALL be such that
For example, if MinPower is 1, MaxPower is 10, and PowerSetting can be set to any integer between
MinPower and MaxPower, PowerStep would be set to 1.
8.13.5.7. SupportedWatts Attribute
This attribute SHALL indicate the list of power levels (in W) supported by the server.
8.13.5.8. SelectedWattIndex Attribute
This attribute SHALL indicate the index into the list of SupportedWatts of the currently selected
power setting.
The index SHALL be a valid index into the SupportedWatts list.
8.13.5.9. WattRating Attribute
This attribute SHALL indicate the rating, in Watts, of the microwave power of the oven.
Supporting this attribute can assist clients in suggesting cooking settings for various foods and bev
erages.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Microwave Oven Control Cluster, specifically the "SetCookingParameters" command. This command is directed from the client to the server, indicating that the client sends this command to the server. The command requires a response, as indicated by the 'Response' field being 'Y'. The 'Access' field is marked as 'O', meaning the access level is optional, which typically refers to the permissions or roles that can execute this command. The 'Conformance' field is marked with 'M', which stands for Mandatory. This means that the "SetCookingParameters" command is a required feature in the Microwave Oven Control Cluster and must be implemented in any device that supports this cluster, without any conditions or exceptions.

* The table row describes a command within the Microwave Oven Control Cluster, specifically the "AddMoreTime" command. This command is initiated by the client and directed towards the server, and it requires a response from the server. The access level for this command is optional, meaning it is not required by default and has no dependencies. The conformance rule for this command is marked as "O," indicating that its implementation is optional. This means that devices implementing the Microwave Oven Control Cluster may choose to support the "AddMoreTime" command, but they are not obligated to do so according to the Matter specification.

8.13.6.1. Command Responses Impacted By the Operational State Cluster
When the Operational State cluster or a cluster derived from it is included on the same endpoint as
this cluster, the server MAY respond to commands defined in this cluster with an INVALID_IN_S
TATE response if the server is unable to accept those command due to restrictions imposed by the
current operational state of the device or other factors.
8.13.6.2. SetCookingParameters Command
This command is used to set the cooking parameters associated with the operation of the device.
This command supports the following fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Microwave Oven Control Cluster, specifically the 'CookMode' command, which is identified by the ID '0' and is of type 'uint8'. The constraints and default values for this command are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule 'O.b+' suggests that the 'CookMode' command is optional, with the 'b+' indicating that there might be additional conditions or notes associated with its optional status, which are likely detailed in another part of the specification. This means that while the command is not required by default, there may be specific scenarios or configurations where its inclusion is recommended or further clarified.

* The table row describes a command named "CookTime" within the Microwave Oven Control Cluster, specifically in the Commands section. This command is identified by the ID '1' and is of the type 'elapsed-s', which likely refers to elapsed seconds. It has a constraint that the value must be between 1 and a defined 'MaxCookTime', with a default value set to 30. The conformance rule 'O.b+' indicates that the "CookTime" command is optional, and there are no additional conditions or dependencies affecting its optional status. This means that while the command is not required to be implemented, it can be included at the discretion of the device manufacturer without any further stipulations.

* In the Microwave Oven Control Cluster, the command 'PowerSetting' is identified by ID '2' and is of type 'uint8'. It is constrained to values between 'MinPower' and 'MaxPower', with a default setting at 'MaxPower'. The conformance rule '[PWRNUM].b+' indicates that the 'PowerSetting' command is optional if the condition 'PWRNUM' is true. The use of brackets around 'PWRNUM' specifies that the optional status is conditional upon the presence of the 'PWRNUM' feature. If 'PWRNUM' is supported, then the 'PowerSetting' command can be included, but it is not mandatory.

* The table row describes a command named "WattSettingIndex" within the Microwave Oven Control Cluster. This command has an ID of '3' and is of type 'uint8'. The constraints for this command are described elsewhere in the documentation, as indicated by 'desc'. The default value for this command is 'MS'. The conformance rule '[WATTS].b+' indicates that the "WattSettingIndex" command is optional if the feature 'WATTS' is supported. The use of brackets around 'WATTS' specifies that the optional status is conditional upon the presence of this feature. If the 'WATTS' feature is not supported, the command does not have any mandatory requirement based on the given conformance expression.

_Table parsed from section 'Commands':_

* The table row describes a command named "StartAfterSetting" within the Microwave Oven Control Cluster, identified by ID '4'. This command is of the boolean type, meaning it can be either true or false, and it applies universally as indicated by the 'Constraint' being 'all'. The default value for this command is 'false'. According to the conformance rule 'O', this command is optional, meaning it is not required for implementation and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this command in their devices without affecting compliance with the Matter specification.

8.13.6.2.1. CookMode Field
This field SHALL indicate the value to which the CurrentMode attribute of the Microwave Oven
Mode cluster should be set. The value of this field SHALL be one from the list of SupportedModes
from the Microwave Oven Mode cluster.
If this field is missing, the CurrentMode attribute SHALL be set to a mode having the Normal mode
tag.
8.13.6.2.2. CookTime Field
This field SHALL indicate the CookTime associated with the operation of the device. The value of
this field SHALL be subject to the constraints of the CookTime attribute of this cluster.
If this field is missing, the CookTime attribute SHALL be set to 30 seconds by the server.
8.13.6.2.3. PowerSetting Field
This field SHALL indicate the PowerSetting associated with the operation of the device. The value of
this field SHALL be subject to the constraints of the PowerSetting attribute of this cluster. If the
PowerSetting field does not conform to the constraints of the PowerSetting attribute, the server
SHALL return a CONSTRAINT_ERROR status.
If this field is missing, the PowerSetting attribute SHALL be set to 100 if MaxPower is not supported
by the server, otherwise it SHALL be set to MaxPower if the MaxPower attribute is supported by the
server.
8.13.6.2.4. WattSettingIndex Field
This field SHALL indicate the value to which the SelectedWattIndex attribute is set. If the value of
this field is greater than or equal to the length of the SupportedWatts attribute list, the server
SHALL  return  a  CONSTRAINT_ERROR  status  and  the  value  of  the  SelectedWattIndex  attribute
SHALL be unchanged.
If this field is missing, the SelectedWattIndex attribute SHALL be set by the server to the index asso
ciated with the highest Watt setting for the selected CookMode.
8.13.6.2.5. StartAfterSetting Field
This field SHALL indicate whether or not oven operation SHALL be started when the command is
received.
8.13.6.2.6. Effect on Receipt
If this command is received while the operational state of the server cannot support the command
in that state, the server SHALL respond with an INVALID_IN_STATE response and the attributes and
state SHALL remain unchanged. See Operational State Cluster for details on the operational states.
If this command is received and any fields sent with the command do not meet the constraints of
any of the associated attributes (i.e. bearing the same name as the field or as described in the field
description), the server SHALL respond with a response of CONSTRAINT_ERROR and the attributes
and state SHALL remain unchanged.
If the StartAfterSetting field is present in the command but the Start command of the Operational
State cluster or one of its derivatives on the same endpoint as this cluster is not supported, the
server SHALL respond with a response of INVALID_COMMAND and the attributes and state SHALL
remain unchanged.
Otherwise:
• The attributes associated with any included fields SHALL be set to the values of those fields.
• The attributes associated with any missing fields SHALL be set to the values as specified in
descriptions of the missing fields.
• If the StartAfterSetting field is included:
◦ If the value of StartAfterSetting is TRUE, oven operation SHALL start.
◦ If the value of StartAfterSetting is FALSE, oven operation SHALL NOT start.
8.13.6.3. AddMoreTime Command
This command is used to add more time to the CookTime attribute of the server.
This command supports these fields:

_Table parsed from section 'Commands':_

* In the context of the Microwave Oven Control Cluster, the command with ID '0', named 'TimeToAdd', is of type 'elapsed-s' and is constrained to values between 1 and the maximum cooking time ('MaxCookTime'). The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'TimeToAdd' command is always required to be implemented in any device or system that supports the Microwave Oven Control Cluster. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the cluster's functionality.

8.13.6.3.1. TimeToAdd Field
This field SHALL indicate the number of seconds to be added to the CookTime attribute.
8.13.6.3.2. Effect on Receipt
Upon receipt of this command, if the sum of the value of the TimeToAdd field and the current value
of the CookTime attribute is greater than the MaxCookTime attribute, the server SHALL respond
with a response of CONSTRAINT_ERROR and the command SHALL be ignored.
If this command is received while the operational state of the server cannot support the command
in that state, the server SHALL respond with an INVALID_IN_STATE response. See Operational State
Cluster for details on the operational states.
Otherwise, the server SHALL add the value of the TimeToAdd field to the value of the CookTime
attribute of this cluster and the server SHALL add the value of the TimeToAdd field to the value of
the CountdownTime attribute of the Operational State cluster if that cluster or a derivative is on the
same endpoint as this cluster.
Chapter 9. Energy Management
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter.
9.1. General Description

## Introduction
The clusters specified in this chapter are for use typically in Energy Management applications with
associated security controls at the application layer. These clusters may be used in any application
domain.

## Cluster List
This section lists the Energy Management specific clusters as specified in this chapter.
Table 16. Overview of the Energy Management Clusters

_Table parsed from section 'Cluster List':_

* The table row describes the "Device Energy Management Mode" cluster within the Microwave Oven Control Cluster, identified by the Cluster ID '0x009F'. This cluster encompasses commands and attributes designed to set the mode of devices that have energy management capabilities. The conformance rule for this cluster is not explicitly provided in the data you shared, but if it were, it would dictate the conditions under which this cluster is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that this cluster is mandatory for all devices implementing the Microwave Oven Control Cluster. If the conformance were 'AB, O', it would mean the cluster is mandatory if feature 'AB' is supported; otherwise, it is optional. Understanding the conformance rule is crucial for determining how and when this cluster should be implemented in devices.

* The table row describes a cluster within the Microwave Oven Control Cluster, specifically the Device Energy Management cluster, identified by the Cluster ID '0x0098'. This cluster is designed to facilitate power management by enabling power adjustments, sharing power forecasts, and modifying power forecasts for devices. The conformance rule for this cluster is not explicitly provided in the data given, but based on the context, it would typically specify whether the inclusion of this cluster is mandatory, optional, or subject to certain conditions within the Microwave Oven Control Cluster. If a conformance rule were provided, it would dictate the circumstances under which this cluster must be implemented, using the rules outlined in the Matter Conformance Interpretation Guide.

* The table row describes a cluster within the Microwave Oven Control Cluster, specifically identified by the Cluster ID '0x0099' and named 'Energy EVSE'. This cluster encompasses commands and attributes designed for controlling an Electric Vehicle Supply Equipment (EVSE). The conformance rule for this cluster is not explicitly provided in the data, but based on the context, it would typically specify the conditions under which the 'Energy EVSE' cluster is required, optional, or otherwise categorized according to the Matter Conformance Interpretation Guide. Without a specific conformance string, we cannot determine its exact requirement status, but it would generally involve conditions related to the support of certain features or configurations within the broader Matter specification.

* The table row entry pertains to the "Energy EVSE Mode" within the Microwave Oven Control Cluster, identified by the Cluster ID '0x009D'. This cluster encompasses commands and attributes specifically designed for setting the mode of an Electric Vehicle Supply Equipment (EVSE). The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically define the conditions under which the "Energy EVSE Mode" cluster is required, optional, or otherwise specified. For instance, if the conformance were 'M', it would indicate that this cluster is mandatory for all devices implementing the Microwave Oven Control Cluster. If it were 'O', it would be optional, allowing implementers to decide whether to include it based on their specific needs or device capabilities. Without the specific conformance string, we can only infer that the entry describes a feature related to EVSE mode control, which may be subject to certain conditions or requirements as outlined in the Matter specification.

* The table row describes a cluster within the Microwave Oven Control Cluster, specifically the "Water Heater Management" cluster, identified by the Cluster ID '0x0094'. This cluster includes commands and attributes designed for controlling a water heater. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance rule using the guide, it would specify under what conditions this cluster is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance was 'M', it would mean that the Water Heater Management cluster is always required in the Microwave Oven Control Cluster. If it were 'O', it would be optional, meaning it could be included at the implementer's discretion without any dependencies. Without a specific conformance rule provided, we cannot determine the exact requirement status of this cluster within the context of the specification.

* The table row describes a cluster within the Microwave Oven Control Cluster, specifically identified by the Cluster ID '0x009E' and named 'Water Heater Mode'. This cluster encompasses commands and attributes related to configuring the mode of a water heater. The conformance rule for this cluster is not explicitly provided in the data given. However, if we were to interpret a typical conformance rule using the guide, it would specify under what conditions this cluster is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean that the Water Heater Mode cluster is always mandatory in the Microwave Oven Control Cluster. If it were 'O', it would be optional, and so on. Without a specific conformance string, we cannot determine the exact requirement status of this cluster.

* The table row describes the "Energy Preference" cluster within the Microwave Oven Control Cluster, identified by the Cluster ID '0x009B'. This cluster includes attributes and commands that allow users to express their preferences regarding energy consumption. The conformance rule for this cluster is not explicitly provided in the data you shared, but if we assume a typical conformance scenario, it might indicate whether the inclusion of this cluster is mandatory, optional, or subject to certain conditions based on the presence of other features or elements. For instance, if the conformance were 'M', it would mean that the Energy Preference cluster is always required in the Microwave Oven Control Cluster. If it were 'O', it would be optional, allowing manufacturers to include it at their discretion without any dependencies. If the conformance were a complex expression, it would specify conditions under which the cluster must be included or could be omitted, based on the presence or absence of other features.

