
# 2.7 Occupancy Sensing Cluster

The server cluster provides an interface to occupancy sensing functionality based on one or more
sensing modalities, including configuration and provision of notifications of occupancy status.

## Data Types
2.7.5.1. OccupancyBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster, under the Data Types section, the table row describes a data element with the bit position '0' named 'Occupied'. This element is summarized as indicating the sensed occupancy state. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Occupied' data element is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

2.7.5.1.1. Occupied Bit
If this bit is set, it SHALL indicate the occupied state else if the bit if not set, it SHALL indicate the
unoccupied state.
2.7.5.2. OccupancySensorTypeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster's Data Types, the table row describes a feature with the bit identifier '0' named 'PIR', which stands for a passive infrared sensor. The summary indicates that this feature is used to detect motion through infrared sensing. The conformance rule for this feature is marked as 'M', meaning it is mandatory. This implies that the PIR feature is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

* In the context of the Occupancy Sensing Cluster's Data Types, the table row describes a data type with the bit position '1', named 'Ultrasonic'. This data type is used to indicate the presence of an ultrasonic sensor. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the inclusion of the 'Ultrasonic' data type is always required in any implementation of the Occupancy Sensing Cluster, without any conditions or exceptions.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes a data type with the bit position '2' named 'PhysicalContact'. This data type represents a sensor that detects physical contact. The conformance rule for 'PhysicalContact' is marked as 'M', which stands for Mandatory. This means that the 'PhysicalContact' data type is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster. There are no conditions or dependencies affecting its requirement; it must be included as part of the cluster's functionality.

This enum is as defined in ClusterRevision 4 and its definition SHALL NOT be
NOTE extended; the feature flags provide the sensor modality (or modalities) for later
cluster revisions. See Backward Compatibility section.
2.7.5.3. OccupancySensorTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Occupancy Sensing Cluster, specifically under the Data Types section. The entry is for a data type with the name "PIR," which stands for Passive Infrared sensor, and is identified by the value '0'. The summary indicates that this data type is used to represent a passive infrared sensor. The conformance rule for this entry is 'M', which means that the inclusion of this data type is mandatory. In other words, any implementation of the Occupancy Sensing Cluster must include support for the PIR data type, as it is a required element according to the Matter specification.

* In the Occupancy Sensing Cluster, under the Data Types section, the table entry describes a data type with the value '1' named 'Ultrasonic', which signifies the presence of an ultrasonic sensor. The conformance rule for this entry is 'M', indicating that the inclusion of this data type is mandatory. This means that any implementation of the Occupancy Sensing Cluster must support the 'Ultrasonic' data type, as it is a required element without any conditions or exceptions.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row entry describes a data type with the value '2' named 'PIRAndUltrasonic'. This data type represents a sensor that combines both passive infrared (PIR) and ultrasonic technologies to detect occupancy. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'PIRAndUltrasonic' data type is always required to be supported in implementations of the Occupancy Sensing Cluster according to the Matter specification. There are no conditions or dependencies affecting this requirement, making it an essential component of the cluster.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table entry describes a data type with the value '3' named 'PhysicalContact'. This data type is summarized as indicating a physical contact sensor. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'PhysicalContact' data type is always required to be implemented in any device or application that adheres to this specification. There are no conditions or dependencies that alter its mandatory status; it must be included as part of the Occupancy Sensing Cluster.

This enum is as defined in ClusterRevision 4 and its definition SHALL NOT be
NOTE
extended; the feature flags provide the sensor modality (or modalities) for later
cluster revisions. See Backward Compatibility section.
2.7.5.4. HoldTimeLimitsStruct Type
This structure provides information on the server’s supported values for the HoldTime attribute.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table entry describes an attribute named "HoldTimeMin" with an ID of '0'. This attribute is of type 'uint16', which is an unsigned 16-bit integer, and it has a constraint that specifies a minimum value of 1. The conformance rule for "HoldTimeMin" is marked as 'M', indicating that this attribute is mandatory. This means that within the Occupancy Sensing Cluster, the "HoldTimeMin" attribute must always be implemented and supported, without any conditions or exceptions.

* The table row describes an entry for the "HoldTimeMax" attribute within the Occupancy Sensing Cluster's Data Types section. This attribute is identified by the ID '1' and is of the type 'uint16', which is an unsigned 16-bit integer. The constraints for "HoldTimeMax" specify that its value must be at least as large as the value of "HoldTimeMin" and must also be a minimum of 10. The conformance rule 'M' indicates that the "HoldTimeMax" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster according to the Matter specification.

* The table row describes an entry within the Occupancy Sensing Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'HoldTimeDefault'. It is of the type 'uint16', which means it is a 16-bit unsigned integer. The value of 'HoldTimeDefault' is constrained to lie between 'HoldTimeMin' and 'HoldTimeMax'. The conformance rule for this entry is 'M', indicating that the 'HoldTimeDefault' attribute is mandatory. This means that it is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

2.7.5.4.1. HoldTimeMin Field
This field SHALL specify the minimum value of the server’s supported value for the HoldTime
attribute, in seconds.
2.7.5.4.2. HoldTimeMax Field
This field SHALL specify the maximum value of the server’s supported value for the HoldTime
attribute, in seconds.
2.7.5.4.3. HoldTimeDefault Field
This field SHALL specify the (manufacturer-determined) default value of the server’s HoldTime
attribute, in seconds. This is the value that a client who wants to reset the settings to a valid default
SHOULD use.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "Occupancy" attribute. This attribute is identified by the ID '0x00 00' and is of the type 'OccupancyBitmap', with a constraint range from 0 to 1. The quality of this attribute is marked as 'P', indicating it is provisional, and it has read and view access ('R V'). The conformance rule for this attribute is 'M', meaning it is mandatory. This signifies that the "Occupancy" attribute is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "OccupancySensorType" attribute, which is of the type "OccupancySensorTypeEnum." The attribute has a constraint that is described elsewhere in the documentation, indicated by "desc." It has a quality designation of "F" and an access level of "R V," meaning it is readable and possibly volatile. The conformance rule "M, D" indicates that this attribute is currently mandatory, meaning it must be implemented. However, it is also marked as deprecated, suggesting that while it is required now, it is considered obsolete and may be removed or replaced in future versions of the specification.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "OccupancySensorTypeBitmap" with an ID of '0x00 02'. This attribute is of type 'OccupancySensorTypeBitmap' and has a constraint range from 0 to 7. It is marked with a quality of 'F' and has read and view access ('R V'). The conformance rule 'M, D' indicates that this attribute is currently mandatory, meaning it must be implemented in any device supporting this cluster. However, it is also marked as deprecated, suggesting that while it is required now, it is considered obsolete in the current specification and may be removed or replaced in future versions.

* The table row describes an attribute named "HoldTime" within the Occupancy Sensing Cluster. This attribute has an ID of '0x00 03' and is of type 'uint16'. The constraints for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'N', and it has read-write access with volatile memory ('RW VM'). The conformance rule for "HoldTime" is 'O', meaning that this attribute is optional. It is not required and has no dependencies, so its implementation is at the discretion of the device manufacturer.

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically named "HoldTimeLimits" with an ID of '0x00 04'. This attribute is of the type 'HoldTimeLimitsStruct' and has a quality designation of 'F', indicating it is a feature-related attribute. The access level is 'R V', meaning it is readable and possibly volatile. The conformance rule for this attribute is 'HoldTime', which implies that the attribute is mandatory if the feature or condition 'HoldTime' is supported. If 'HoldTime' is not supported, the attribute's inclusion is not required. This rule ensures that the "HoldTimeLimits" attribute is present only when relevant to the device's functionality, based on the support of the 'HoldTime' feature.

* The table row describes an attribute named `PIROccupiedToUnoccupiedDelay` within the Occupancy Sensing Cluster. This attribute is of type `uint16`, with a default value of `0`, and is accessible for read and write operations with volatile memory (`RW VM`). The conformance rule `[HoldTime & (PIR | (!PIR & !US & !PHY))], D` indicates that this attribute is optional if the `HoldTime` feature is supported and either the `PIR` feature is supported, or none of the `PIR`, `US`, and `PHY` features are supported. If these conditions are not met, the attribute is considered deprecated. This means that the attribute's inclusion is conditional based on the presence of certain features, and it is otherwise obsolete in the current specification.

* The table row describes an attribute named `PIRUnoccupiedToOccupiedDelay` within the Occupancy Sensing Cluster. This attribute is of type `uint16`, with a default value of `0`, and is accessible for read and write operations with volatile memory (`RW VM`). The conformance rule for this attribute is complex and involves several conditions. It is mandatory if the `HoldTime` feature is supported and either the `PIR` feature is supported or both `US` (ultrasonic) and `PHY` (physical) features are not supported, and the `PIRUnoccupiedToOccupiedThreshold` is also supported. If only the `HoldTime` feature is supported and either `PIR` is supported or both `US` and `PHY` are not supported, the attribute is optional. If none of these conditions are met, the attribute is deprecated. This conformance rule ensures that the attribute is used appropriately based on the specific features supported by the device.

* The table row describes an attribute named "PIRUnoccupiedToOccupiedThreshold" within the Occupancy Sensing Cluster. This attribute is of type `uint8`, with a value constraint ranging from 1 to 254, and a default value of 1. It has read-write access and is volatile memory (RW VM). The conformance rule for this attribute is complex: it is mandatory if the "HoldTime" feature is supported and either the "PIR" feature is supported or none of the "PIR", "US", and "PHY" features are supported, and the "PIRUnoccupiedToOccupiedDelay" feature is also supported. Alternatively, it is optional if "HoldTime" is supported and either "PIR" is supported or none of "PIR", "US", and "PHY" are supported. If neither of these conditions is met, the attribute is deprecated.

* The table row describes an attribute named "UltrasonicOccupiedToUnoccupiedDelay" within the Occupancy Sensing Cluster. This attribute has an ID of '0x00 20' and is of type 'uint16', with a default value of '0'. It is accessible with read and write permissions, and it is volatile memory (RW VM). The conformance rule '[HoldTime & US], D' indicates that this attribute is optional if both the 'HoldTime' and 'US' (Ultrasonic) features are supported. If these conditions are not met, the attribute is considered deprecated. This means that in systems where both conditions are true, the attribute can be implemented optionally, but in other cases, it should not be used as it is obsolete.

* The table row describes an attribute named "UltrasonicUnoccupiedToOccupiedDelay" within the Occupancy Sensing Cluster. This attribute is of type `uint16` and applies universally (`Constraint: all`). It is not a quality attribute (`Quality: N`) and has a default value of `0`. The access level is read-write with viewable metadata (`Access: RW VM`). The conformance rule for this attribute is complex and follows a conditional chain: it is mandatory if both the `HoldTime` and `US` (Ultrasonic) features are supported, and the `UltrasonicUnoccupiedToOccupiedThreshold` is also supported. If only `HoldTime` and `US` are supported, it becomes optional. If neither condition is met, the attribute is deprecated. This means the attribute's requirement is highly dependent on the presence of specific features and their combinations, reflecting its relevance in certain configurations of the Occupancy Sensing Cluster.

* The table row describes an attribute named "UltrasonicUnoccupiedToOccupiedThreshold" within the Occupancy Sensing Cluster. This attribute is of type `uint8`, constrained to values between 1 and 254, with a default value of 1. It has read-write access and is non-volatile (RW VM). The conformance rule for this attribute is expressed as "HoldTime & US & UltrasonicUnoccupiedToOccupiedDelay, [HoldTime & US], D". This means the attribute is mandatory if the features "HoldTime", "US" (Ultrasonic), and "UltrasonicUnoccupiedToOccupiedDelay" are all supported. If only "HoldTime" and "US" are supported, the attribute is optional. If neither of these conditions is met, the attribute is deprecated.

* The table row describes an attribute named "PhysicalContactOccupiedToUnoccupiedDelay" within the Occupancy Sensing Cluster. This attribute has an ID of '0x00 30' and is of type 'uint16', with a constraint applicable to all instances. The attribute is not of high quality ('N'), has a default value of '0', and its access is read-write with a viewable and modifiable (RW VM) status. The conformance rule '[HoldTime & PHY], D' indicates that this attribute is optional if both the 'HoldTime' and 'PHY' features are supported. If these conditions are not met, the attribute is considered deprecated, meaning it is obsolete in the current specification.

* The table row describes an attribute named "PhysicalContactUnoccupiedToOccupiedDelay" within the Occupancy Sensing Cluster. This attribute is of type `uint16`, with a constraint applicable to all, and a default value of `0`. It has read-write access with a viewable and modifiable quality. The conformance rule for this attribute is expressed as "HoldTime & PHY & PhysicalContactUnoccupiedToOccupiedThreshold, [HoldTime & PHY], D". This means that the attribute is mandatory if the features `HoldTime`, `PHY`, and `PhysicalContactUnoccupiedToOccupiedThreshold` are all supported. If only `HoldTime` and `PHY` are supported, the attribute becomes optional. If neither of these conditions is met, the attribute is considered deprecated.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "PhysicalContactUnoccupiedToOccupiedThreshold" within the Occupancy Sensing Cluster. This attribute is of type `uint8` and has a constraint range from 1 to 254. It is marked with a quality of 'N', a default value of 1, and access permissions of 'RW VM', indicating it is readable and writable with specific access controls. The conformance rule for this attribute is "HoldTime & PHY & PhysicalContactUnoccupiedToOccupiedDelay, [HoldTime & PHY], D". This means that the attribute is mandatory if all three conditions—HoldTime, PHY, and PhysicalContactUnoccupiedToOccupiedDelay—are supported. If only HoldTime and PHY are supported, the attribute is optional. If neither of these conditions is met, the attribute is deprecated.

2.7.6.1. Occupancy Attribute
This attribute SHALL indicate the sensed (processed) status of occupancy. For compatibility reasons
this is expressed as a bitmap where the status is indicated in bit 0: a value of 1 means occupied, and
0 means unoccupied, with the other bits set to 0; this can be considered equivalent to a boolean.
2.7.6.2. OccupancySensorType and OccupancySensorTypeBitmap Attributes
<=
These attributes SHALL indicate the type of sensor. In ClusterRevision   4, these were used to spec
>=
ify the type of the occupancy sensor using a bitmap. For ClusterRevision   5, the server SHALL
indicate the type of sensor using the feature flags, and the server SHALL provide these attributes
<=
for the backward compatibility with clients implementing a cluster revision   4, using the mapping
according to the following table. Also see Backward Compatibility section.

_Table parsed from section 'Attributes':_

* In the context of the Occupancy Sensing Cluster's attributes, the table row for the 'Feature Flag Value' with the conformance rule 'US' indicates that this attribute is conditionally required based on the support of certain features. According to the conformance interpretation guide, the absence of brackets around 'US' implies that the attribute is mandatory if the feature 'US' is supported. This means that if a device or implementation includes the 'US' feature, it must also include the 'Feature Flag Value' attribute as part of its configuration. If the 'US' feature is not supported, the conformance rule does not specify any requirement for this attribute, implying it is not mandatory in such cases.

* In the context of the Occupancy Sensing Cluster, the table row describes an attribute related to the 'Value of OccupancySensorTypeBitmap' and 'Value of OccupancySensorType', both specified as 'PIR *'. The conformance rule for this attribute is indicated by the 'Feature Flag Value' of '0', which suggests that the attribute is currently in a provisional state. This means that while the attribute is not yet mandatory, it is expected to become mandatory in the future. The use of 'PIR *' implies that the attribute is specifically related to Passive Infrared (PIR) sensor types, which are commonly used for detecting motion. The provisional status indicates that implementers should be prepared for this attribute to become a required part of the specification in subsequent updates.

* In the context of the Occupancy Sensing Cluster, the table row describes an attribute related to the occupancy sensor's type, specifically when the sensor is a Passive Infrared (PIR) type. The 'Feature Flag Value' of '0' indicates that there are no additional features influencing this attribute's conformance. The 'Value of OccupancySensorTypeBitmap' and 'Value of OccupancySensorType' both being 'PIR' suggest that this attribute is specifically relevant to PIR sensors. The conformance rule, while not explicitly detailed in the provided data, would typically imply that the attribute is either mandatory, optional, or provisional based on the presence of the PIR sensor type. Given the lack of a specific conformance string in the data, it is likely that the attribute's inclusion is provisional, pending further specification or dependent on the presence of the PIR sensor type in the device's configuration.

* In the context of the Occupancy Sensing Cluster's attributes, the table row specifies a feature related to the 'Feature Flag Value' of '1', with both the 'Value of OccupancySensorTypeBitmap' and 'Value of OccupancySensorType' set to 'Ultrasonic'. This indicates that the attribute in question is associated with ultrasonic occupancy sensing technology. The conformance rule, while not explicitly provided in the row data, would typically dictate how this feature is implemented based on the Matter Conformance Interpretation Guide. If we assume a conformance expression was provided, it would determine whether the ultrasonic sensor attribute is mandatory, optional, provisional, deprecated, or disallowed, depending on the presence or absence of certain features or conditions. For example, if the conformance was `Ultrasonic, O`, it would mean the attribute is mandatory if the ultrasonic feature is supported; otherwise, it is optional.

* In the Occupancy Sensing Cluster, within the Attributes section, the table row describes a feature related to occupancy sensing capabilities. Specifically, it indicates that the 'Feature Flag Value' is '1', which typically denotes an enabled or active state. The 'Value of OccupancySensorTypeBitmap' is 'PIR + Ultrasonic', and the 'Value of OccupancySensorType' is 'PIRAndUltrasonic'. This suggests that the sensor is capable of detecting occupancy using both Passive Infrared (PIR) and Ultrasonic methods. The conformance rule for this entry is not explicitly provided in the row data, but based on the context, it likely implies that the combination of PIR and Ultrasonic sensing is either a provisional or optional feature, potentially becoming mandatory in future revisions. This aligns with the provisional status often indicated by 'P' in conformance tags, suggesting that while the feature is currently not mandatory, it is anticipated to become more integral in future specifications.

* In the context of the Occupancy Sensing Cluster, the table row describes an attribute related to the 'Feature Flag Value' of '0', specifically concerning the 'Value of OccupancySensorTypeBitmap' and 'Value of OccupancySensorType', both set to 'PhysicalContact'. The conformance rule for this entry is not explicitly provided in the row data, but based on the context, it suggests that the attribute is likely mandatory when the Occupancy Sensor Type is 'PhysicalContact'. This means that if a device supports the 'PhysicalContact' sensor type, this attribute must be implemented. If the conformance rule were more complex, it would typically involve conditional expressions or alternative conformance states, but in this case, the straightforward setting implies a mandatory requirement for devices with this specific sensor type.

* In the context of the Occupancy Sensing Cluster, specifically within the Attributes section, the table row describes an attribute with a 'Feature Flag Value' of '0', indicating no specific feature flags are set. The 'Value of OccupancySensorTypeBitmap' is 'PhysicalContact + PIR', which means the sensor supports both Physical Contact and Passive Infrared (PIR) types. The 'Value of OccupancySensorType' is 'PIR **', suggesting that the primary sensor type is PIR. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it implies that the attribute is relevant when the Occupancy Sensor supports the PIR type. If the conformance rule were to be interpreted, it would likely state that the attribute is mandatory or optional depending on the presence of the PIR feature, following the logical conditions and expressions outlined in the conformance interpretation guide.

* In the context of the Occupancy Sensing Cluster, the table row describes an attribute related to the 'Feature Flag Value' of '1', indicating that the feature is enabled. The 'Value of OccupancySensorTypeBitmap' is set to 'PhysicalContact + Ultrasonic', which means that the sensor can detect occupancy using both physical contact and ultrasonic methods. The 'Value of OccupancySensorType' is specified as 'Ultrasonic **', suggesting a particular emphasis or note regarding the ultrasonic type, possibly indicating a special condition or requirement. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it implies that the attribute is likely mandatory when the feature flag is set to '1', and the sensor type includes ultrasonic capabilities. This ensures that devices implementing this cluster must support these specific sensor types when the feature is active.

* In the context of the Occupancy Sensing Cluster, specifically within the Attributes section, the table row describes a feature related to the 'Feature Flag Value' set to '1'. This indicates that the feature is active. The 'Value of OccupancySensorTypeBitmap' includes 'PhysicalContact + PIR + Ultrasonic', suggesting that the sensor can detect occupancy through physical contact, passive infrared (PIR), and ultrasonic methods. The 'Value of OccupancySensorType' is specified as 'PIRAndUltrasonic **', which implies a combination of PIR and ultrasonic sensing capabilities. The conformance rule for this entry is not explicitly provided in the row data, but based on the context, it likely involves a condition where the feature is mandatory if the sensor supports both PIR and ultrasonic detection, given the emphasis on these types in the 'Value of OccupancySensorType'. This setup ensures that devices implementing this cluster can effectively utilize multiple sensing technologies to detect occupancy, enhancing accuracy and reliability.

pancySensorType

*
In case the feature flags PIR, US and PHY are all set to 0, these attributes are set to mimic a PIR sen
<=
sor since this likely will give the best compatibility with clients implementing a cluster revision   4,
which are not aware of the feature flags and the added modalities. In this case, timing parameters
(when HoldTime is supported) are expressed using the PIROccupiedToUnoccupiedDelay, PIRUnoc
cupiedToOccupiedDelay and PIRUnoccupiedToOccupiedThreshold attributes.

**
These combinations of sensor type were not defined for OccupancySensorType in ClusterRevision
<=
4, so they are mapped to a combination which was defined in that version.
2.7.6.3. HoldTime Attribute
This attribute SHALL specify the time delay, in seconds, before the sensor changes to its unoccupied
state after the last detection of occupancy in the sensed area. This is equivalent to the legacy *Occu
piedToUnoccupiedDelay attributes.
The value of HoldTime SHALL be within the limits provided in the HoldTimeLimits attribute, i.e.
<= <=
HoldTimeMin   HoldTime   HoldTimeMax
Low values of HoldTime SHOULD be avoided since they could lead to many reporting messages. A
value 0 for HoldTime SHALL NOT be used.
The figure below illustrates this with an example of how this attribute is used for a PIR sensor. It
uses threshold detection to generate an "internal detection" signal, which needs post-processing to
become usable for transmission (traffic shaping). The bit in the Occupancy attribute will be set to 1
when the internal detection signal goes high, and will stay at 1 for HoldTime after the (last) instance
where the internal detection signal goes low.
The top half of the figure shows the case of a single trigger: the bit in the Occupancy attribute will
be 1 for the duration of the PIR signal exceeding the threshold plus HoldTime. The bottom half of
the figure shows the case of multiple triggers: the second trigger starts before the HoldTime of the
first trigger has expired; this results in a single period of the bit in the Occupancy attribute being 1.
The bit in the Occupancy attribute will be set to 1 from the start of the first period where the PIR
signal exceeds the threshold until HoldTime after the last moment where the PIR exceeded the
threshold.
Figure 13. Processing of PIR signal towards Occupancy attribute using HoldTime
2.7.6.4. HoldTimeLimits Attribute
This attribute SHALL indicate the server’s limits, and default value, for the HoldTime attribute.
2.7.6.5. Attributes to support legacy implementations
<=
The following 3 sets of 3 attributes each were used in ClusterRevision   4 to indicate timings and
conditions to tune the reporting by the sensor - separately for each of the three sensor modalities
>=
defined in that revision. In ClusterRevision   5, these are replaced by the HoldTime attribute
>=
(shared for all modalities). A server with ClusterRevision   5 MAY (under the conformance condi
tions stated in the attributes table above) provide these attributes for backward compatibility with
<=
clients implementing a cluster revision   4. When doing so, the provided values for these legacy

*OccupiedToUnoccupied  attributes  SHALL  follow  the  values  in  the  HoldTime  attribute  when
updated, and vice-versa, such that any present *OccupiedToUnoccupiedDelay attribute maintains
equality to HoldTime.
Also see Backward Compatibility section.
Some, but not all, of the implications of the conformance rules for these attributes are:
• if attribute HoldTime is not supported, these 9 legacy attributes SHALL NOT be supported
• if modality PIR is supported, while both PHY and US modalities are not supported,
◦ the 3 legacy attributes related to PIR MAY be supported (if allowed by the other rules)
◦ the 6 legacy attributes related to Ultrasonic and PhysicalContact SHALL NOT be supported
• if modality US is supported while both PIR and PHY modalities are not supported:
◦ the 3 legacy attributes related to UltraSonic MAY be supported (if allowed by the other rules)
◦ the 6 legacy attributes related to PIR and PhysicalContact SHALL NOT be supported
• if modality PHY is supported while both PIR and US modalities are not supported:
◦ the 3 legacy attributes related to PhysicalContact MAY be supported (if allowed by the other
rules)
◦ the 6 legacy attributes related to PIR and Ultrasonic SHALL NOT be supported
• the  legacy  attributes  related  to  UnoccupiedToOccupiedDelay  and  UnoccupiedToOccu
piedThreshold for a certain modality SHALL be both supported or both not supported
• if none of the modalities PIR, US, and PHY is supported (this case is presented as a PIR sensor for
compatibility):
◦ the 3 legacy attributes related to PIR MAY be supported (if allowed by the other rules)
◦ the 6 legacy attributes related to Ultrasonic and PhysicalContact SHALL NOT be supported
For cases where more than one of the PIR, PHY and US modalities is supported and the timing para
meters are provided for more than one modality, it is manufacturer specific how to combine those
timing parameters.
2.7.6.6. PIROccupiedToUnoccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the PIR sensor changes to its unoccu
pied state after the last detection of occupancy in the sensed area.
2.7.6.7. PIRUnoccupiedToOccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the PIR sensor changes to its occu
pied state after the first detection of occupancy in the sensed area.
2.7.6.8. PIRUnoccupiedToOccupiedThreshold Attribute
This attribute SHALL specify the number of occupancy detection events that must occur in the
period PIRUnoccupiedToOccupiedDelay, before the PIR sensor changes to its occupied state.
2.7.6.9. UltrasonicOccupiedToUnoccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the Ultrasonic sensor changes to its
unoccupied state after the last detection of occupancy in the sensed area.
2.7.6.10. UltrasonicUnoccupiedToOccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the Ultrasonic sensor changes to its
occupied state after the first detection of occupancy in the sensed area.
2.7.6.11. UltrasonicUnoccupiedToOccupiedThreshold Attribute
This attribute SHALL specify the number of occupancy detection events that must occur in the
period UltrasonicUnoccupiedToOccupiedDelay, before the Ultrasonic sensor changes to its occupied
state.
2.7.6.12. PhysicalContactOccupiedToUnoccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the physical contact occupancy sen
sor changes to its unoccupied state after detecting the unoccupied event.
2.7.6.13. PhysicalContactUnoccupiedToOccupiedDelay Attribute
This attribute SHALL specify the time delay, in seconds, before the physical contact sensor changes
to its occupied state after the first detection of the occupied event.
2.7.6.14. PhysicalContactUnoccupiedToOccupiedThreshold Attribute
This attribute SHALL specify the number of occupancy detection events that must occur in the
period PhysicalContactUnoccupiedToOccupiedDelay, before the PhysicalContact sensor changes to
its occupied state.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Occupancy Sensing Cluster, specifically the "OccupancyChanged" event, identified by the ID '0x00'. This event has an informational priority level ('INFO') and requires view access ('V'). The conformance rule for this event is marked as 'O', indicating that it is optional. This means that the implementation of the "OccupancyChanged" event is not required and has no dependencies on other features or conditions. Devices or systems implementing the Occupancy Sensing Cluster can choose to support this event, but they are not obligated to do so according to the Matter specification.

2.7.7.1. OccupancyChanged Event
If this event is supported, it SHALL be generated when the Occupancy attribute changes.

_Table parsed from section 'Events':_

* In the context of the Occupancy Sensing Cluster, within the Events section, the table row describes an event with the ID '0' named 'Occupancy', which is of the type 'OccupancyBitmap'. The conformance rule for this event is marked as 'M', indicating that it is mandatory. This means that the 'Occupancy' event must always be implemented and supported in any device or application that utilizes the Occupancy Sensing Cluster, without any conditions or exceptions.

2.7.7.1.1. Occupancy Field
This field SHALL indicate the new value of the Occupancy attribute.
2.8. Resource Monitoring Clusters
This generic cluster provides an interface to the current condition of a resource. A resource is a
component of a device that is designed to be replaced, refilled, or emptied when exhausted or full.
Examples of resources include filters, cartridges, and water tanks. While batteries fit this definition
they are not intended to be used with this cluster. Use the power source cluster for batteries
instead.
This cluster is not meant to be used for monitoring of the system resources, such as
NOTE
processing, memory utilization, networking properties, etc.
This cluster SHALL be used via an alias to a specific resource type (see Cluster IDs).

## Cluster IDs
The table below is a list of aliased Cluster IDs which represent different resource types and conform
to this cluster definition.

_Table parsed from section 'Cluster IDs':_

* The table row entry describes a feature within the Occupancy Sensing Cluster, specifically identified by the ID '0x0071' and named 'HEPA Filter Monitoring', with the PICS (Protocol Implementation Conformance Statement) code 'HEPAFREMON'. The conformance rule for this feature is not explicitly provided in the data, but based on the context, it would typically indicate whether the feature is mandatory, optional, provisional, deprecated, or disallowed. Since the conformance rule is not specified, we cannot determine its exact status. However, if it were to follow the Matter Conformance Interpretation Guide, it would be essential to know the specific conformance string to accurately interpret whether the HEPA Filter Monitoring feature is required, optional, or subject to any conditions within the Occupancy Sensing Cluster.

* The table row describes an element within the Occupancy Sensing Cluster, specifically the "Activated Carbon Filter Monitoring" feature, identified by the ID `0x0072` and associated with the PICS code `ACFREMON`. The conformance rule for this feature is not explicitly provided in the data snippet. However, based on the Matter Conformance Interpretation Guide, if a conformance string were provided, it would dictate whether this feature is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on the support of other features. Without a specific conformance string, we cannot determine the exact requirements for this feature, but it would typically involve assessing its necessity or optionality in the context of the Occupancy Sensing Cluster.

* The table row entry for the Occupancy Sensing Cluster under the section "Cluster IDs" describes a feature named "Water Tank Level Monitoring" with the ID '0x0079' and PICS code 'WTLREPMON'. The conformance rule for this feature is not explicitly provided in the data, but based on the context, it likely follows the general conformance rules outlined in the Matter specification. Without a specific conformance string, we can infer that the feature's inclusion or requirement status would depend on additional documentation or context not provided here. Typically, such a feature might be optional or conditional based on the presence of related features or specific use cases within the Matter framework. To fully understand its conformance, one would need to refer to the detailed documentation or conformance expressions associated with this feature in the Matter specification.

## Data Types
2.8.5.1. DegradationDirectionEnum Type
This data type is derived from enum8.
Indicates the direction in which the condition of the resource changes over time.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster's Data Types, the table row describes an element with the name "Up," which has a value of '0'. This element signifies that the degradation of the resource is indicated by an upwards moving or increasing value. The conformance rule for this element is marked as 'M', meaning it is mandatory. This indicates that the "Up" element is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes an entry with the name "Down" and a value of '1'. This entry signifies that the degradation of the resource is indicated by a downwards moving or decreasing value. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Down" data type is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

2.8.5.2. ChangeIndicationEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster, within the Data Types section, the table row describes a data type with the value '0', named 'OK'. This indicates that the resource is in good condition and no intervention is required. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'OK' status is a required element in the specification and must always be implemented in any device or system that supports the Occupancy Sensing Cluster. There are no conditions or dependencies affecting this requirement, making it a fundamental part of the cluster's functionality.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes a data type with the name "Warning" and a value of '1'. This data type indicates that a resource is nearing exhaustion and will soon require intervention. The conformance rule for this entry is 'WRN', which is not explicitly defined in the provided conformance guide. However, based on the context, it likely represents a specific condition or feature related to warnings within the Matter specification. Since 'WRN' does not match any standard conformance tags or logical conditions outlined in the guide, it suggests that this entry's conformance is described elsewhere in the documentation, possibly under a specific feature or condition related to warnings.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes an entry with the value '2', named 'Critical'. This entry signifies a state where a resource is exhausted, necessitating immediate intervention. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any device or system that supports the Occupancy Sensing Cluster. There are no conditions or exceptions; the 'Critical' state must be included as part of the cluster's data types.

2.8.5.3. ProductIdentifierTypeEnum Type
This data type is derived from enum8.
Indicate the type of identifier used to describe the product. Devices SHOULD use globally-recog
nized IDs over OEM specific ones.

_Table parsed from section 'Data Types':_

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes an entry with the value '0' and the name 'UPC', which stands for a 12-digit Universal Product Code. The conformance rule for this entry is marked as 'M', indicating that it is a Mandatory element. This means that the inclusion of the 'UPC' data type is always required within the Occupancy Sensing Cluster, with no conditions or exceptions.

* In the context of the Occupancy Sensing Cluster's Data Types, the table row describes an entry with the value '1', named 'GTIN-8', which stands for an 8-digit Global Trade Item Number. The conformance rule for this entry is marked as 'M', indicating that the GTIN-8 data type is mandatory. This means that within the Occupancy Sensing Cluster, the inclusion of the GTIN-8 data type is always required and must be supported without any conditions or exceptions.

* In the context of the Occupancy Sensing Cluster's Data Types, the table row describes an entry with the name "EAN," which stands for the 13-digit European Article Number. The 'Value' associated with this entry is '2', and it serves as a unique identifier for this data type within the cluster. The 'Conformance' field is marked as 'M', which means that the EAN is a Mandatory element. This implies that the inclusion of the EAN data type is always required in any implementation of the Occupancy Sensing Cluster, without any conditions or exceptions.

* In the Occupancy Sensing Cluster, under the Data Types section, there is an entry for a data type named "GTIN-14," which stands for a 14-digit Global Trade Item Number. The 'Value' associated with this data type is '3'. The conformance rule for this entry is marked as 'M', which means that the GTIN-14 data type is mandatory. This indicates that it is a required element within the Occupancy Sensing Cluster and must be implemented in any device or application that conforms to this part of the Matter specification.

* In the context of the Occupancy Sensing Cluster, specifically within the Data Types section, the table row describes an entry with the value '4' and the name 'OEM', which stands for Original Equipment Manufacturer part number. The summary indicates that this entry pertains to the part number associated with the original equipment manufacturer. The conformance rule for this entry is 'M', which means that this element is mandatory. It is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

2.8.5.4. ReplacementProductStruct Type
Indicates the product identifier that can be used as a replacement for the resource.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Occupancy Sensing Cluster, specifically in the Data Types section. The element is identified by the ID '0' and is named 'ProductIdentifierType'. It is of the type 'ProductIdentifierTypeEnum', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this element is 'M', which means that the 'ProductIdentifierType' is a mandatory element. It is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, with no conditions or exceptions.

* In the Occupancy Sensing Cluster, under the Data Types section, the table entry for 'ProductIdentifierValue' is identified by the ID '1' and is of type 'string' with a constraint limiting its length to a maximum of 20 characters. The conformance rule for this entry is 'M', which means that the 'ProductIdentifierValue' is a mandatory element. This implies that it is always required to be implemented in any device or application that supports the Occupancy Sensing Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "Condition" attribute, which is identified by the ID `0x0000` and is of the type `percent`. This attribute has an access level of `R V`, indicating it is readable and can have its value reported. The conformance rule for this attribute is `CON`, which, according to the Matter Conformance Interpretation Guide, would need to be defined elsewhere in the documentation as it is not a standard conformance tag or expression. Therefore, the specific requirements or conditions under which this attribute is mandatory, optional, or otherwise must be looked up in the detailed documentation where `CON` is described.

* The table row describes an attribute named "DegradationDirection" within the Occupancy Sensing Cluster, identified by the ID '0x0001'. This attribute is of the type 'DegradationDirectionEnum' and has constraints that are detailed elsewhere in the documentation ('desc'). The quality of this attribute is marked as 'F', indicating it is a feature-specific attribute. It has read and view access permissions ('R V'). The conformance rule for this attribute is 'CON', which is not a standard conformance tag or expression as per the provided guide. Therefore, 'CON' likely refers to a specific condition or description that is detailed elsewhere in the documentation, indicating that the conformance of this attribute is context-dependent and requires further reference to understand its specific requirements.

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically identified by the ID `0x0002` and named `ChangeIndication`. This attribute is of the type `ChangeIndicationEnum` and has a default value of `0`. It is accessible with read (`R`) and view (`V`) permissions. The conformance rule for this attribute is marked as `M`, which means it is mandatory. This indicates that the `ChangeIndication` attribute must always be implemented and supported in any device or application that utilizes the Occupancy Sensing Cluster, without any conditions or exceptions.

* In the Occupancy Sensing Cluster, within the context of Attributes, the table row describes an attribute with the ID '0x0003' named 'InPlaceIndicator'. This attribute is of type 'bool', indicating it holds a boolean value, and it has an access level of 'R V', meaning it is readable and can be viewed. The conformance rule for 'InPlaceIndicator' is marked as 'O', which signifies that this attribute is optional. This means that while it is not required to implement this attribute, it can be included without any dependencies or conditions.

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "LastChangedTime" attribute, identified by the ID '0x0004'. This attribute is of type 'epoch-s', indicating it records time in seconds since a specific epoch. The 'Constraint' is listed as 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X N', which typically indicates specific quality or implementation notes, such as being disallowed in certain contexts or having specific nuances. The 'Default' value is 'null', meaning it does not have a predefined default value. The 'Access' is 'RW VO', indicating that the attribute is Read-Write and Volatile, meaning its value can change and is not persistent across device reboots. The 'Conformance' is 'O', which means this attribute is Optional. It is not required for compliance with the Matter specification and does not depend on any other conditions or features to be implemented.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Occupancy Sensing Cluster, specifically the "ReplacementProductList" attribute. This attribute has an ID of '0x0005' and is of the type 'list[ReplacementProductStruct]', with a constraint that limits the list to a maximum of 5 items. The quality is marked as 'F', and the access level is 'R V', indicating it is readable and possibly volatile. The conformance rule 'REP' indicates that the attribute is provisionally required, with the expectation that it will become mandatory in the future. This means that while it is not currently mandatory, it is anticipated to be a required element in upcoming versions of the specification.

2.8.6.1. Condition Attribute
This attribute SHALL indicate the current condition of the resource in percent.
2.8.6.2. DegradationDirection Attribute
This attribute SHALL indicate the direction of change for the condition of the resource over time,
which helps to determine whether a higher or lower condition value is considered optimal.
2.8.6.3. ChangeIndication Attribute
This attribute SHALL be populated with a value from ChangeIndicationEnum that is indicative of
the current requirement to change the resource.
2.8.6.4. InPlaceIndicator Attribute
This attribute SHALL indicate whether a resource is currently installed. A value of true SHALL indi
cate that a resource is installed. A value of false SHALL indicate that a resource is not installed.
2.8.6.5. LastChangedTime Attribute
This attribute MAY indicates the time at which the resource has been changed, if supported by the
server. The attribute SHALL be null if it was never set or is unknown.
2.8.6.6. ReplacementProductList Attribute
This attribute SHALL indicate the list of supported products that may be used as replacements for
the current resource. Each item in this list represents a unique ReplacementProductStruct.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Occupancy Sensing Cluster, specifically the "ResetCondition" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'). The access level is marked as 'O', indicating that access to this command is optional. The conformance rule for this command is 'O', meaning that the implementation of the "ResetCondition" command is optional and not required by default. There are no additional conditions or dependencies specified, so implementers have the discretion to include or exclude this command based on their specific needs or preferences.

2.8.7.1. ResetCondition Command
Upon receipt, the device SHALL reset the Condition and ChangeIndicator attributes, indicating full
resource availability and readiness for use, as initially configured. Invocation of this command
MAY cause the LastChangedTime to be updated automatically based on the clock of the server, if
the server supports setting the attribute.