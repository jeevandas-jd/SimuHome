
# 8.8 Refrigerator Alarm Cluster

This cluster is a derived cluster of Alarm Base cluster and provides the alarm definition related to
refrigerator and temperature controlled cabinet devices.

## Data Types
8.8.5.1. AlarmBitmap Type
This data type is derived from map32.

_Table parsed from section 'Data Types':_

* In the Refrigerator Alarm Cluster, under the Data Types section, the table row describes a feature identified by the bit '0' and named 'DoorOpen'. This feature indicates that the refrigerator's cabinet door has been open for a vendor-defined amount of time. The conformance rule 'M' signifies that this feature is mandatory, meaning it is always required to be implemented in any device or system that supports the Refrigerator Alarm Cluster. There are no conditions or exceptions to this requirement, ensuring that the 'DoorOpen' feature is consistently available across all implementations of this cluster.

## Attributes
8.8.6.1. Mask Attribute
If the generation of the alarm has not been suppressed at the device itself, then this attribute
SHALL have these fixed values.

_Table parsed from section 'Attributes':_

* In the context of the Refrigerator Alarm Cluster, specifically within the Attributes section, the table row describes an attribute with the bit position '0', named 'DoorOpen', and assigned a value of '1'. This attribute likely indicates whether a refrigerator door is open. The conformance rule for this attribute is not explicitly provided in the data, but if we assume it follows a typical pattern, it might be mandatory (M) or optional (O) based on certain conditions or features. Without a specific conformance string, we cannot definitively state its requirement status. However, if this attribute is crucial for the basic functionality of the refrigerator alarm system, it would typically be mandatory. If additional context or conditions are provided elsewhere in the documentation, they would clarify whether this attribute is required, optional, or subject to other conditions.

This alarm SHALL be cleared only when the door is closed (manual action).
If the generation of the alarm is suppressed at the device itself, then bit 0 SHALL have a value of 0.
It SHALL be re-set to 1 if the alarm is re-enabled at the device itself.

## Commands

_Table parsed from section 'Commands':_

* In the context of the Refrigerator Alarm Cluster, specifically within the Commands section, the table row describes a command identified by the ID `0x01` and named `ModifyEnabledAlarms`. The conformance rule for this command is marked as `X`, which means it is explicitly disallowed according to the Matter specification. This indicates that the `ModifyEnabledAlarms` command should not be implemented or used within this cluster, as it is not permitted under the current guidelines.

