
# 3.3 Ballast Configuration Cluster

This cluster is used for configuring a lighting ballast.
NOTE Support for Ballast Configuration cluster is provisional.

## Dependencies
If the Alarms server cluster is supported on the same endpoint then the Alarms functionality is
enabled and the LampAlarmMode attribute SHALL be supported.

## Data Types
3.3.5.1. BallastStatusBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Ballast Configuration Cluster, under the Data Types section, the entry for 'Bit' 0 is named 'BallastNonOperational' and summarizes the operational state of the ballast. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'BallastNonOperational' element is always required to be implemented in any device or application that supports the Ballast Configuration Cluster, without any conditions or exceptions.

* In the Ballast Configuration Cluster, under the Data Types section, the entry for 'LampFailure' with a bit value of '1' represents the operational state of the lamps. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. There are no conditions or exceptions; the 'LampFailure' data type must be included to conform to the Matter specification for this cluster.

3.3.5.1.1. BallastNonOperational Bit
This bit SHALL indicate whether the ballast is operational.
• 0 = The ballast is fully operational
• 1 = The ballast is not fully operational
3.3.5.1.2. LampFailure Bit
This bit SHALL indicate whether all lamps is operational.
• 0 = All lamps are operational
• 1 = One or more lamp is not in its socket or is faulty
3.3.5.2. LampAlarmModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Ballast Configuration Cluster, under the Data Types section, the entry for 'LampBurnHours' with a bit value of '0' represents the state of the LampBurnHours alarm generation. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'LampBurnHours' feature is always required to be implemented in any device or application that supports the Ballast Configuration Cluster, without any conditions or exceptions.

3.3.5.2.1. LampBurnHours Bit
This bit SHALL indicate that the LampBurnHours attribute MAY generate an alarm.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the "PhysicalMinLevel" attribute. This attribute has an ID of '0x0000' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The value of this attribute is constrained to be between 1 and 254, with a default value set to 1. The access level for this attribute is 'R V', indicating it is readable and has a volatile nature. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "PhysicalMinLevel" attribute is always required to be implemented in any device that supports the Ballast Configuration Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the "PhysicalMaxLevel" attribute. This attribute has an ID of '0x0001' and is of type 'uint8', meaning it is an 8-bit unsigned integer. It has a constraint that limits its value between 1 and 254, with a default value set at 254. The access permissions are 'R V', indicating that the attribute is readable and has a volatile nature, meaning it may change without being explicitly set. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "PhysicalMaxLevel" attribute is always required to be implemented in any device that supports the Ballast Configuration Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the 'BallastStatus' attribute. This attribute is identified by the ID '0x0002' and is of the type 'BallastStatusBitmap'. It has a constraint labeled as 'all', a default value of '0', and access permissions denoted as 'R V', which typically means it is readable and possibly volatile. The conformance rule for this attribute is 'O', indicating that it is optional. This means that the inclusion of the 'BallastStatus' attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute named "MinLevel" within the Ballast Configuration Cluster. This attribute has an ID of '0x0010' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The value of "MinLevel" is constrained between 'PhysicalMinLevel' and 'MaxLevel', with a default value set to 'PhysicalMinLevel'. It has read and write access, indicated by 'RW', and is subject to view management, as denoted by 'VM'. The conformance rule for "MinLevel" is 'M', which means this attribute is mandatory and must always be implemented in any device or application that supports the Ballast Configuration Cluster. There are no conditions or dependencies affecting its requirement status.

* The table row describes an attribute named "MaxLevel" within the Ballast Configuration Cluster. This attribute has an ID of '0x0011' and is of type 'uint8'. It is constrained to values between 'MinLevel' and 'PhysicalMaxLevel', with a default value set to 'PhysicalMaxLevel'. The access permissions for this attribute are 'RW VM', indicating it can be read and written, and it is visible to management. The conformance rule for "MaxLevel" is 'M', meaning this attribute is mandatory and must always be implemented in any device or application that supports the Ballast Configuration Cluster.

* The table row entry pertains to the "PowerOnLevel" attribute within the Ballast Configuration Cluster, identified by the ID '0x0012'. According to the conformance rule 'D', this attribute is classified as Deprecated. This means that the "PowerOnLevel" attribute is considered obsolete in the current Matter specification and is no longer recommended for use in new implementations. Existing implementations may still recognize it, but it is advised to transition away from using this attribute in future developments.

* In the Ballast Configuration Cluster, within the Attributes section, the attribute identified by 'ID' 0x0013 is named 'PowerOnFadeTime'. According to the conformance rule 'D', this attribute is marked as Deprecated. This means that 'PowerOnFadeTime' is considered obsolete in the current Matter specification and is no longer recommended for use. It suggests that while the attribute may still exist in some implementations, it is expected to be phased out and should not be relied upon for future development or compatibility.

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the "IntrinsicBallastFactor" with an ID of '0x0014'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies to all instances of the cluster as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'X', which means this attribute is explicitly disallowed in the current context. The 'Access' is specified as 'RW VM', indicating that the attribute can be read and written, and it is volatile, meaning its value may change without notice. The 'Conformance' is 'O', which signifies that the "IntrinsicBallastFactor" attribute is optional. This means that while it is not required to be implemented, it can be included if desired, without any dependencies or conditions.

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the 'BallastFactorAdjustment' attribute. This attribute has an ID of '0x0015' and is of type 'uint8', with a constraint range from 100 to a maximum specified value (MS). The quality of this attribute is marked as 'X', indicating it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read-write access with view and modify permissions ('RW VM'). The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the implementation of this attribute is not required and has no dependencies on other features or conditions within the specification.

* In the Ballast Configuration Cluster, the attribute with ID '0x0020' is named 'LampQuantity' and is of type 'uint8', which means it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that this attribute applies universally without specific restrictions. The 'Access' is marked as 'R V', meaning it is readable and has a volatile nature, which typically implies that its value can change frequently or is not stored persistently. The 'Conformance' is specified as 'M', indicating that the 'LampQuantity' attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Ballast Configuration Cluster, with no conditions or exceptions.

* The table row describes an attribute named "LampType" within the Ballast Configuration Cluster. This attribute has an ID of '0x0030' and is of type 'string', constrained to a maximum length of 16 characters. Its default value is an empty string (""), and it has read-write access with the possibility of being a volatile memory (RW VM). The conformance rule for "LampType" is 'O', which means this attribute is optional. It is not required to be implemented and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute named "LampManufacturer" within the Ballast Configuration Cluster. This attribute has an ID of '0x0031' and is of type 'string', with a maximum length constraint of 16 characters. Its default value is an empty string (""), and it has read-write access with view and modify permissions (RW VM). The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the inclusion of the "LampManufacturer" attribute is not required and does not depend on any other features or conditions within the Matter specification.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "LampRatedHours" within the Ballast Configuration Cluster. This attribute has an ID of '0x0032' and is of type 'uint24', meaning it is a 24-bit unsigned integer. The constraint 'all' suggests it applies universally within its context. The quality is marked as 'X', indicating that this attribute is explicitly disallowed for certain quality-related purposes. The default value is 'null', and it has read-write access with a viewable and modifiable (VM) designation. The conformance rule 'O' signifies that the "LampRatedHours" attribute is optional, meaning it is not required and has no dependencies on other features or conditions. This allows implementers the flexibility to include or exclude this attribute based on their specific needs or preferences without affecting compliance with the Matter specification.

* The table row describes an attribute named "LampBurnHours" within the Ballast Configuration Cluster. This attribute has an ID of '0x0033' and is of type 'uint24', indicating it stores a 24-bit unsigned integer. The 'Constraint' is listed as 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed from having any quality-related specifications. The default value for this attribute is '0', and it has 'RW VM' access, indicating it can be read and written, with VM likely referring to a specific access context or mode. The 'Conformance' is marked as 'O', which means the "LampBurnHours" attribute is optional. It is not required to be implemented and has no dependencies on other features or conditions.

* The table row describes an attribute within the Ballast Configuration Cluster, specifically the "LampAlarmMode" attribute. This attribute is identified by the ID '0x0034' and is of the type 'LampAlarmModeBitmap', with a constraint of 'all', meaning it applies universally within its context. The default value for this attribute is '0', and it has read-write access with the possibility of being a volatile memory (RW VM). The conformance rule for "LampAlarmMode" is 'O', which means that this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

* The table row describes an attribute named "LampBurnHoursTrip Point" within the Ballast Configuration Cluster. This attribute has an ID of '0x0035' and is of type 'uint24', meaning it is a 24-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that there are no specific constraints on its value beyond the typical range for a uint24. The 'Quality' is marked as 'X', which means this attribute is explicitly disallowed in some contexts, though this does not affect its conformance status. The 'Default' value is 'null', suggesting that there is no predefined default value for this attribute. The 'Access' is 'RW VM', indicating that the attribute can be read and written, and it is subject to view management. The 'Conformance' is 'O', meaning that the "LampBurnHoursTrip Point" attribute is optional; it is not required and does not have any dependencies that would necessitate its inclusion in

3.3.6.1. PhysicalMinLevel Attribute
This attribute SHALL specify the minimum light output the ballast can achieve according to the
dimming light curve (see Dimming Curve).
3.3.6.2. PhysicalMaxLevel Attribute
This attribute SHALL specify the maximum light output the ballast can achieve according to the
dimming light curve (see Dimming Curve).
3.3.6.3. BallastStatus Attribute
This attribute SHALL specify the status of various aspects of the ballast or the connected lights, see
BallastStatusBitmap.
3.3.6.4. MinLevel Attribute
This attribute SHALL specify the light output of the ballast according to the dimming light curve
(see Dimming Curve) when the Level Control Cluster’s CurrentLevel attribute equals to 1 (and the
On/Off Cluster’s OnOff attribute equals to TRUE).
The value of this attribute SHALL be both greater than or equal to PhysicalMinLevel and less than
or equal to MaxLevel. If an attempt is made to set this attribute to a level where these conditions
are not met, a response SHALL be returned with status code set to CONSTRAINT_ERROR, and the
level SHALL NOT be set.
3.3.6.5. MaxLevel Attribute
This attribute SHALL specify the light output of the ballast according to the dimming light curve
(see Dimming Curve) when the Level Control Cluster’s CurrentLevel attribute equals to 254 (and the
On/Off Cluster’s OnOff attribute equals to TRUE).
The value of this attribute SHALL be both less than or equal to PhysicalMaxLevel and greater than
or equal to MinLevel. If an attempt is made to set this attribute to a level where these conditions are
not met, a response SHALL be returned with status code set to CONSTRAINT_ERROR, and the level
SHALL NOT be set.
3.3.6.6. IntrinsicBallastFactor Attribute
This attribute SHALL specify the ballast factor, as a percentage, of the ballast/lamp combination,
prior to any adjustment.
A value of null indicates in invalid value.
3.3.6.7. BallastFactorAdjustment Attribute
This attribute SHALL specify the multiplication factor, as a percentage, to be applied to the config
ured light output of the lamps. A typical use for this attribute is to compensate for reduction in effi
ciency over the lifetime of a lamp.
The light output is given by
actual light output = configured light output x BallastFactorAdjustment / 100%
The range for this attribute is manufacturer dependent. If an attempt is made to set this attribute to
a level that cannot be supported, a response SHALL be returned with status code set to CONSTRAIN
T_ERROR, and the level SHALL NOT be changed. The value of null indicates that ballast factor scal
ing is not in use.
3.3.6.8. LampQuantity Attribute
This attribute SHALL specify the number of lamps connected to this ballast. (Note 1: this number
does not take into account whether lamps are actually in their sockets or not).
3.3.6.9. LampType Attribute
This attribute SHALL specify the type of lamps (including their wattage) connected to the ballast.
3.3.6.10. LampManufacturer Attribute
This attribute SHALL specify the name of the manufacturer of the currently connected lamps.
3.3.6.11. LampRatedHours Attribute
This attribute SHALL specify the number of hours of use the lamps are rated for by the manufac
turer.
A value of null indicates an invalid or unknown time.
3.3.6.12. LampBurnHours Attribute
This attribute SHALL specify the length of time, in hours, the currently connected lamps have been
operated, cumulative since the last re-lamping. Burn hours SHALL NOT be accumulated if the
lamps are off.
This attribute SHOULD be reset to zero (e.g., remotely) when the lamps are changed. If partially
used lamps are connected, LampBurnHours SHOULD be updated to reflect the burn hours of the
lamps.
A value of null indicates an invalid or unknown time.
3.3.6.13. LampAlarmMode Attribute
1
This attribute SHALL specify which attributes MAY cause an alarm notification to be generated. A
in each bit position means that its associated attribute is able to generate an alarm.
NOTE All alarms are also logged in the alarm table – see Alarms cluster.
3.3.6.14. LampBurnHoursTripPoint Attribute
This attribute SHALL specify the number of hours the LampBurnHours attribute MAY reach before
an alarm is generated.
If the Alarms cluster is not present on the same device this attribute is not used and thus MAY be
omitted (see Dependencies).
The Alarm Code field included in the generated alarm SHALL be 0x01.
If this attribute has the value of null, then this alarm SHALL NOT be generated.

## The Dimming Light Curve
The dimming curve is recommended to be logarithmic, as defined by the following equation:
Where: %Light is the percent light output of the ballast and
Level is an 8-bit integer between 1 (0.1% light output) and 254 (100% output) that is adjusted for
MinLevel and MaxLevel using the following equation:
Level = (MaxLevel – MinLevel) * CurrentLevel / 253 + (254 * MinLevel – MaxLevel) / 253.
Note 1: Value 255 is not used.
Note 2: The light output is determined by this curve together with the IntrinsicBallastFactor and
BallastFactorAdjustment attributes.
The table below gives a couple of examples of the dimming light curve for different values of Min
Level, MaxLevel and CurrentLevel.
Table 7. Examples of The Dimming Light Curve

_Table parsed from section 'The Dimming Light Curve':_

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the section concerning the Dimming Light Curve. It describes a feature or attribute related to the 'MinLevel', which has a value of '1', indicating the minimum level setting for the dimming light curve. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely follows a standard conformance pattern. If we assume a typical conformance rule, such as 'M' for mandatory, this would mean that the 'MinLevel' is a required element within the Ballast Configuration Cluster for devices implementing this cluster. The values 'MaxLevel', 'CurrentLevel', 'Level', and '%Light' provide additional context or constraints for the dimming functionality, with 'MaxLevel' being '254', 'CurrentLevel' and 'Level' both set to '1', and '%Light' indicating a 0.10% light output at the minimum level. This setup ensures

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes an element labeled 'MinLevel' with a value of '1', indicating the minimum level setting for the dimming function. The 'MaxLevel' is set at '254', representing the maximum level setting. The 'CurrentLevel' and 'Level' both have a value of '10', suggesting the current operational level of the dimming function. The '%Light' is noted as '0.13%', which likely represents the percentage of light output relative to the maximum level. The conformance rule for this entry is not explicitly provided in the data, but if we were to interpret it based on the guide, it would involve determining whether the element is mandatory, optional, or subject to other conditions based on the presence or absence of specific features or conditions within the Matter specification. Without a specific conformance string, we assume the element's inclusion is determined by the broader context

* The table row entry pertains to the Ballast Configuration Cluster, specifically focusing on the Dimming Light Curve section. It describes a feature or attribute related to the dimming functionality of a light ballast. The 'MinLevel' is set at '1', indicating the minimum dimming level, while 'MaxLevel' is '254', representing the maximum dimming level. The 'CurrentLevel' and 'Level' are both set at '100', which suggests the current operational dimming level. The '%Light' value of '1.49%' likely represents the percentage of light output relative to the maximum level. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically define whether these attributes are mandatory, optional, or have conditional requirements based on the presence of certain features or conditions. Without a specific conformance string, we assume these attributes are essential for the operation of the dimming light curve within the Ballast Configuration Cluster.

* The table row entry for the Ballast Configuration Cluster, specifically under the section "The Dimming Light Curve," provides details about the 'MinLevel', 'MaxLevel', 'CurrentLevel', 'Level', and '%Light'. These values indicate the operational parameters for dimming control, where 'MinLevel' is set to 1, 'MaxLevel' and 'CurrentLevel' are both set to 254, and the 'Level' is also 254, corresponding to a '%Light' of 100%. This suggests that the dimming light curve is configured to allow a full range of dimming from nearly off (1) to full brightness (254). The conformance rule for this entry is not explicitly provided in the table row data, but based on the context, it likely involves ensuring that these parameters are set correctly within the specified range to achieve the desired dimming performance. The absence of a specific conformance string implies that these values are standard settings within the cluster, potentially mandatory for

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes a feature or attribute named 'MinLevel' with a value of '170', which indicates the minimum level of dimming allowed. The 'MaxLevel' is set at '254', representing the maximum dimming level. The 'CurrentLevel' is '1', suggesting the current dimming level setting. The 'Level' is also '170', aligning with the minimum level, and '%Light' is '10.1%', indicating the percentage of light output at the minimum level. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context, it would typically specify whether these attributes are mandatory, optional, or conditional based on certain features or conditions. In this case, without a specific conformance string, we assume these values are part of a mandatory or default configuration for devices implementing the Ballast Configuration Cluster, ensuring consistent

* The table row entry pertains to the "Ballast Configuration Cluster" within the section focused on "The Dimming Light Curve." It describes various parameters related to light dimming levels. Specifically, the 'MinLevel' is set at 170, indicating the minimum dimming level, while 'MaxLevel' is 254, representing the maximum level. The 'CurrentLevel' is 10, which is the current setting of the dimming level. The 'Level' is 173, which might be a target or reference level, and '%Light' is 11.0%, indicating the percentage of light output relative to the maximum possible output. The conformance rule for this entry is not explicitly provided in the data, but if it were, it would dictate the conditions under which these parameters are required, optional, or otherwise specified according to the Matter specification guidelines.

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes various attributes related to light dimming levels. The 'MinLevel' is set at 170, indicating the minimum dimming level, while 'MaxLevel' is 254, representing the maximum dimming level. The 'CurrentLevel' is 100, which is the present dimming level setting. The 'Level' is 203, likely indicating a target or default dimming level, and '%Light' is 24.8%, which could represent the current light output as a percentage of the maximum. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically involve conditions under which these attributes are mandatory, optional, or have other statuses as defined by the Matter specification. Without a specific conformance string, we assume these attributes are part of the standard configuration for managing dimming in lighting devices within the

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes a feature or attribute related to the 'MinLevel', 'MaxLevel', 'CurrentLevel', 'Level', and '%Light'. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would dictate when these attributes are required or optional based on certain conditions or feature support. For instance, if the conformance were `M`, it would mean these attributes are always mandatory. If it were `O`, they would be optional without dependencies. The values '170', '254', '254', '254', and '100%' likely represent specific configuration or operational parameters for the dimming functionality, indicating minimum and maximum levels, the current level, and the percentage of light output. Without a specific conformance string, we assume these values are part of the

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes a feature or attribute labeled 'MinLevel' with a value of '170', indicating the minimum level setting for a dimming light. The 'MaxLevel' is set to '230', defining the upper limit for the light level. The 'CurrentLevel' is '1', suggesting the present setting of the light level, while 'Level' is also '170', likely indicating the starting or default level. The '%Light' is '10.1%', which represents the percentage of light output relative to the maximum possible output. The conformance rule for this entry is not explicitly provided in the data, but if we were to interpret it based on the guide, it would involve understanding the conditions under which this feature is mandatory, optional, or otherwise. However, without a specific conformance string, we can only infer that these values are part of the configuration parameters for managing

* The table row entry pertains to the Ballast Configuration Cluster, specifically within the context of the Dimming Light Curve. It describes a feature or attribute related to the dimming capabilities of a lighting device. The data provided includes specific values for 'MinLevel' (170), 'MaxLevel' (230), 'CurrentLevel' (10), 'Level' (172), and '%Light' (10.7%). However, the conformance rule for this entry is not explicitly stated in the provided data. If we were to interpret a conformance rule, it would typically indicate whether these attributes are mandatory, optional, or subject to certain conditions based on the presence of specific features or other conditions. Without a specific conformance string, we cannot determine the exact requirements for these attributes, but they likely define the operational parameters for how the device manages its dimming light curve within the specified levels.

* The table row entry pertains to the "Ballast Configuration Cluster" within the section "The Dimming Light Curve." It describes a feature or attribute related to light dimming levels, specifically focusing on the 'MinLevel', 'MaxLevel', 'CurrentLevel', 'Level', and '%Light'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves conditions under which these levels are mandatory, optional, or otherwise specified. Typically, such entries define the operational parameters for dimming control, where 'MinLevel' and 'MaxLevel' set the boundaries for dimming, 'CurrentLevel' indicates the present dimming state, 'Level' might represent a target or set level, and '%Light' translates the level into a percentage of light output. Without a specific conformance string, we assume these parameters are crucial for configuring and managing the dimming behavior of a lighting device within the Matter specification, ensuring compatibility and interoperability across devices.

* In the context of the Ballast Configuration Cluster, specifically under the section concerning the Dimming Light Curve, the table row describes a feature or attribute related to light dimming levels. The entry specifies various parameters: 'MinLevel' is set at 170, 'MaxLevel' at 230, 'CurrentLevel' at 254, 'Level' at 230, and the percentage of light output is 51.9%. However, the conformance rule for this entry is not explicitly provided in the data, so we cannot directly interpret its conformance status using the guide. Typically, such an entry would define the operational range and current state of a dimmable light, indicating how the light's brightness can be adjusted within the specified levels. The absence of a conformance string suggests that further documentation or context is needed to determine whether these parameters are mandatory, optional, or subject to any conditional requirements.

Chapter 4. HVAC
The Cluster Library is made of individual chapters such as this one. References between chapters
are made using a X.Y notation where X is the chapter and Y is the sub-section within that chapter.
4.1. General Description

## Introduction
The clusters specified in this document are for use typically in HVAC applications, but MAY be used
in any application domain.

## Terms
Precooling: Cooling a building in the early (cooler) part of the day, so that the thermal mass of the
building decreases cooling needs in the later (hotter) part of the day.

## Cluster List
This section lists the HVAC specific clusters as specified in this chapter.
Table 8. Overview of the HVAC Clusters

_Table parsed from section 'Cluster List':_

* The table row describes an entry within the Ballast Configuration Cluster, specifically focusing on the "Pump Configuration and Control" cluster, identified by the Cluster ID '0x0200'. This cluster provides an interface for configuring and controlling pumps. The conformance rule for this entry is not explicitly provided in the data you shared, so we cannot determine its specific requirements or optionality based on the given information. Typically, the conformance field would indicate whether this cluster is mandatory, optional, provisional, deprecated, or disallowed within the context of the Ballast Configuration Cluster, or if its inclusion depends on certain conditions or features. Without the conformance string, we cannot provide a detailed interpretation of its conformance status.

* The table row describes a cluster within the Ballast Configuration Cluster, specifically the Thermostat cluster, identified by the Cluster ID `0x0201`. This cluster provides an interface for configuring and controlling the functionality of a thermostat. The conformance rule for this cluster is not explicitly provided in the data given, but if we were to apply the Matter Conformance Interpretation Guide, we would need to know the specific conformance string to determine whether the Thermostat cluster is mandatory, optional, provisional, deprecated, or disallowed within the context of the Ballast Configuration Cluster. Without the conformance string, we cannot definitively state the requirements for this cluster's implementation.

* The table row describes a cluster within the Ballast Configuration Cluster, specifically the "Fan Control" cluster, identified by the Cluster ID `0x0202`. This cluster provides an interface for controlling a fan. The conformance rule for this cluster is not explicitly provided in the data you shared, but typically, the conformance would dictate under what conditions this cluster is required, optional, or otherwise. For example, if the conformance were `M`, it would mean that the Fan Control cluster is always mandatory in the context of the Ballast Configuration Cluster. If it were `O`, it would be optional, meaning it could be included but is not required. The actual conformance rule would provide specific guidance on whether the Fan Control cluster must be implemented, can be optionally included, or is subject to other conditions as outlined in the Matter Conformance Interpretation Guide.

* The table row describes the "Thermostat User Interface Configuration" cluster, identified by the Cluster ID '0x0204', within the context of the Ballast Configuration Cluster's Cluster List. This cluster provides an interface for configuring the user interface of a thermostat, which may be located remotely from the thermostat itself. The conformance rule for this cluster is not explicitly provided in the row data, but based on the guide, if it were to be included, it would specify the conditions under which this cluster is required, optional, or otherwise. For example, if the conformance was 'M', it would mean this cluster is always mandatory. If it were 'O', it would be optional with no dependencies. Without specific conformance data, we can only infer that this cluster is part of the configuration options available for thermostats within the Ballast Configuration Cluster.

* The table row describes a cluster within the Ballast Configuration Cluster, specifically identified by the Cluster ID '0x0081' and named 'Valve Configuration and Control'. This cluster serves as an interface for configuring and controlling the functionality of a valve. The 'Conformance' field for this entry is not explicitly provided in the data you shared, so I cannot directly interpret its conformance rule. However, if the conformance rule were available, it would dictate whether the inclusion of this cluster is mandatory, optional, provisional, deprecated, or disallowed, based on the conditions or logical expressions outlined in the Matter Conformance Interpretation Guide. This would help implementers understand when and how to include this cluster in their Matter-compliant devices.

