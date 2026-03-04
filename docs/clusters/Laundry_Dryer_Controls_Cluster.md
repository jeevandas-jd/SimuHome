
# 8.9 Laundry Dryer Controls Cluster

This cluster provides a way to access options associated with the operation of a laundry dryer
device type.

## Data Types
8.9.4.1. DrynessLevelEnum Type
This data type is derived from enum8.
This enum provides a representation of the level of dryness that will be used while drying in a
selected mode.
It is up to the device manufacturer to determine the mapping between the enum values and the
corresponding temperature level.

_Table parsed from section 'Data Types':_

* In the context of the Laundry Dryer Controls Cluster, specifically within the Data Types section, the table row describes a data type entry with the value '0' and the name 'Low'. This entry represents a setting that provides a low dryness level for the selected mode of the dryer. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Low' dryness level setting is a required element in the implementation of the Laundry Dryer Controls Cluster, and it must always be included in any compliant device or application that supports this cluster.

_Table parsed from section 'Data Types':_

* In the context of the Laundry Dryer Controls Cluster, specifically within the Data Types section, the table row describes a data type with the value '1' named 'Normal'. This data type provides the normal level of dryness for the selected mode. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Normal' level of dryness is a required element in the specification and must be implemented in any device or system that adheres to the Matter specification for laundry dryer controls. There are no conditions or exceptions; it is an essential component of the cluster.

* In the context of the Laundry Dryer Controls Cluster, specifically within the Data Types section, the table row describes an entry with the value '2' and the name 'Extra'. This entry provides an additional dryness level option for the selected mode, enhancing the functionality of the dryer by allowing users to choose an extra level of dryness. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Extra' dryness level is a required feature in any implementation of the Laundry Dryer Controls Cluster, ensuring that all compliant devices must support this additional dryness level option.

* In the context of the Laundry Dryer Controls Cluster, specifically within the Data Types section, the table row describes an element with the name "Max" and a value of "3". This element provides information about the maximum dryness level available for the selected mode of the dryer. The conformance rule for this element is marked as "M", which stands for Mandatory. This means that the "Max" element is always required to be implemented in any device or application that supports the Laundry Dryer Controls Cluster, ensuring that users can always access information about the maximum dryness level setting.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Laundry Dryer Controls Cluster, specifically the "SupportedDrynessLevels" attribute. This attribute has an ID of '0x0000' and is of the type 'list[DrynessLevelEnum]', indicating it is a list containing enumerated values representing different dryness levels. The constraint '1 to 4' specifies that the list must contain between one and four entries. The access type 'R V' indicates that this attribute is readable and has a volatile nature, meaning its value can change without a write operation. The conformance rule 'M' signifies that the "SupportedDrynessLevels" attribute is mandatory, meaning it is always required to be implemented in any device that supports the Laundry Dryer Controls Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Laundry Dryer Controls Cluster, specifically the "SelectedDrynessLevel" attribute. This attribute is identified by the ID '0x0001' and is of the type 'DrynessLevelEnum'. The constraints and default values for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The quality of this attribute is marked as 'X', meaning it is explicitly disallowed in terms of quality considerations. The access level is 'RW VO', indicating that it can be read and written, and it is volatile, meaning it may change or reset under certain conditions. The conformance rule for this attribute is 'M', which means it is mandatory and always required to be implemented in any device supporting the Laundry Dryer Controls Cluster.

8.9.5.1. SupportedDrynessLevels Attribute
This attribute SHALL indicate the list of supported dryness levels available to the appliance in the
currently selected mode. The dryness level values are determined by the manufacturer. At least one
dryness level value SHALL be provided in the SupportedDrynessLevels list. The list of dryness lev
els MAY change depending on the currently-selected Laundry Dryer mode.
8.9.5.2. SelectedDrynessLevel Attribute
This attribute SHALL indicate the currently-selected dryness level and it SHALL be the index into
the SupportedDrynessLevels list of the selected dryness level.
If an attempt is made to write this attribute with a value other than null or a value contained in
SupportedDrynessLevels, a CONSTRAINT_ERROR response SHALL be sent as the response. If an
attempt is made to write this attribute while the device is not in a state that supports modifying the
dryness level, an INVALID_IN_STATE error SHALL be sent as the response. A value of null SHALL
indicate that there will be no dryness level setting for the current mode.