
# 9.7 Energy Preference Cluster

This cluster provides an interface to specify preferences for how devices should consume energy.
NOTE Support for Energy Preference cluster is provisional.

## Data Types
9.7.5.1. EnergyPriorityEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Energy Preference Cluster, under the Data Types section, there is an entry with the value '0' named 'Comfort', which is summarized as 'User comfort'. The conformance rule for this entry is 'M', indicating that it is a Mandatory element. This means that the 'Comfort' data type must always be implemented and supported in any device or application that utilizes the Energy Preference Cluster, without any conditions or exceptions.

* In the context of the Energy Preference Cluster, specifically within the Data Types section, the table row describes an element named "Speed" with a value of '1' and a summary indicating it pertains to the "Speed of operation." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Speed" element is always required to be implemented in any device or application that supports the Energy Preference Cluster, without any conditions or exceptions.

* In the Energy Preference Cluster, under the Data Types section, the entry for 'Efficiency' with a value of '2' represents the amount of energy consumed by the device. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Efficiency' data type is always required to be implemented in any device or application that supports the Energy Preference Cluster, without any conditions or exceptions.

* In the Energy Preference Cluster, under the Data Types section, the entry for 'WaterConsumption' represents the amount of water consumed by the device. The conformance rule for this entry is marked as 'M', which means that the 'WaterConsumption' data type is mandatory. This indicates that any implementation of the Energy Preference Cluster must include the 'WaterConsumption' data type, as it is always required according to the Matter specification.

9.7.5.1.1. Comfort Value
This value SHALL emphasize user comfort; e.g. local temperature for a thermostat.
9.7.5.1.2. Speed Value
This value SHALL emphasize how quickly a device accomplishes its targeted use; e.g. how quickly a
robot vacuum completes a cleaning cycle.
9.7.5.1.3. Efficiency Value
This value SHALL emphasize how much energy a device uses; e.g. electricity usage for a Pump.
9.7.5.1.4. Water consumption Value
This value SHALL emphasize how much water is consumed during device use; e.g. how much water
a dishwasher uses during a cleaning cycle.
9.7.5.2. BalanceStruct Type
This represents a step along a scale of preferences.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Energy Preference Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'Step'. It is of the 'percent' type, with a constraint labeled as 'all', indicating it applies universally within its context. The quality is marked as 'F', and the default value is 'MS'. The conformance rule for this entry is 'M', which means that the 'Step' element is mandatory. It is always required to be implemented in any device or application that supports the Energy Preference Cluster, without any conditions or exceptions.

* In the Energy Preference Cluster, under the Data Types section, there is an entry identified by 'ID' 1, named 'Label'. This entry is of the 'string' type and is constrained to a maximum length of 64 characters. The 'Quality' is marked as 'F', which may denote a specific quality attribute relevant to the context. The 'Conformance' for this entry is 'O', indicating that the 'Label' element is optional. This means that while it is not required to implement this element, it can be included at the discretion of the developer or manufacturer, as there are no dependencies or conditions mandating its inclusion.

9.7.5.2.1. Step Field
This field SHALL indicate the relative value of this step.
9.7.5.2.2. Label Field
This field SHALL indicate an optional string explaining which actions a device might take at the
given step value.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "EnergyBalances" within the Energy Preference Cluster, specifically under the Attributes section. This attribute has an ID of '0x0000' and is of type 'list[BalanceStruct]', with a constraint indicating that the list must contain between 2 to 10 elements. The 'Quality' is marked as 'F', and the 'Access' is 'R V', meaning it is readable and has volatile access characteristics. The conformance rule 'BALA' indicates that the "EnergyBalances" attribute is mandatory if the feature 'BALA' is supported. If 'BALA' is not supported, the attribute is not required. Thus, the presence of this attribute depends on the support for the 'BALA' feature within the device or implementation.

* The table row describes an attribute named "CurrentEnergyBalance" within the Energy Preference Cluster. This attribute has an ID of '0x0001' and is of type 'uint8', with a constraint labeled as 'all', indicating it applies universally within its context. The quality is marked as 'N', and it has 'RW VO' access, meaning it is readable and writable with volatile access. The conformance rule 'BALA' indicates that the attribute is mandatory if the feature 'BALA' is supported. If the feature 'BALA' is not supported, the attribute is not required. This rule ensures that the attribute is implemented in devices where the 'BALA' feature is present, aligning with the specific requirements of the Energy Preference Cluster.

* The table row describes an attribute named "EnergyPriorities" within the Energy Preference Cluster, identified by the ID '0x0002'. This attribute is of type 'list[EnergyPriorityEnum]' and has a constraint of '2', which likely specifies the minimum or maximum number of elements in the list. The quality 'F' and access 'R V' indicate that this attribute is a feature and can be read and viewed. The conformance rule 'BALA' specifies that the "EnergyPriorities" attribute is mandatory if the feature 'BALA' is supported. If the feature 'BALA' is not supported, the attribute is not required. This means that the presence of the "EnergyPriorities" attribute is conditional on the support of the 'BALA' feature within the device or implementation.

* The table row describes an attribute named "LowPowerModeSensitivities" within the Energy Preference Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0003' and is of the type 'list[BalanceStruct]', with a constraint that the list must contain between 2 to 10 elements. The quality is marked as 'F', and it has an access level of 'R V', indicating it is readable and volatile. The conformance rule 'LPMS' signifies that this attribute is mandatory if the feature 'LPMS' (Low Power Mode Sensitivities) is supported by the device. If the device supports this feature, the attribute must be implemented; otherwise, it is not required.

* The table row describes an attribute named "CurrentLowPowerModeSensitivity" within the Energy Preference Cluster. This attribute has an ID of '0x0004' and is of type 'uint8', with a constraint applicable to all instances. It is marked with a quality of 'N' and has read-write access with volatile and optional characteristics ('RW VO'). The conformance rule 'LPMS' indicates that this attribute is mandatory if the feature 'LPMS' (Low Power Mode Sensitivity) is supported. Therefore, any implementation of the Energy Preference Cluster that supports the 'LPMS' feature must include this attribute.

9.7.6.1. EnergyBalances Attribute
This attribute SHALL indicate a list of BalanceStructs, each representing a step along a linear scale
of relative priorities. A Step field with a value of zero SHALL indicate that the device SHOULD
entirely favor the priority specified by the first element in EnergyPriorities; whereas a Step field
with a value of 100 SHALL indicate that the device SHOULD entirely favor the priority specified by
the second element in EnergyPriorities. The midpoint value of 50 SHALL indicate an even split
between the two priorities.
This SHALL contain at least two BalanceStructs.
Each BalanceStruct SHALL have a Step field larger than the Step field on the previous BalanceStruct
in the list.
The first BalanceStruct SHALL have a Step value of zero, and the last BalanceStruct SHALL have a
Step value of 100.
9.7.6.2. CurrentEnergyBalance Attribute
This attribute SHALL indicate the current preference of the user for balancing different priorities
during  device  use.  The  value  of  this  attribute  is  the  index,  0-based,  into  the  EnergyBalances
attribute for the currently selected balance.
If an attempt is made to set this attribute to an index outside the maximum index for EnergyBal
ances, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If the value of EnergyBalances changes after an update, the device SHALL migrate the value of the
CurrentEnergyBalance  attribute  to  the  index  which  the  manufacturer  specifies  most  closely
matches the previous value, while preserving extreme preferences as follows:
1. If the previous value of CurrentEnergyBalance was zero, indicating a total preference for the
priority specified by the first element in EnergyPriorities, the new value of CurrentEnergyBal
ance SHALL also be zero.
2. If the previous value of CurrentEnergyBalance was the index of the last BalanceStruct in the
previous value of EnergyBalances, indicating a total preference for the priority specified by the
last element in EnergyPriorities, the new value of CurrentEnergyBalance SHALL be the index of
the last element in the updated value of EnergyBalances.
9.7.6.3. EnergyPriorities Attribute
This attribute SHALL indicate two extremes for interpreting the values in the EnergyBalances
attribute. These two priorities SHALL be in opposition to each other; e.g. Comfort vs. Efficiency or
Speed vs. WaterConsumption.
If the value of EnergyPriorities changes after an update to represent a new balance between priori
ties, the value of the CurrentEnergyBalance attribute SHALL be set to its default.
9.7.6.4. LowPowerModeSensitivities Attribute
This attribute SHALL indicate a list of BalanceStructs, each representing a condition or set of condi
tions for the device to enter a low power mode.
This SHALL contain at least two BalanceStructs.
Each BalanceStruct SHALL have a Step field larger than the Step field on the previous BalanceStruct
in the list.
9.7.6.5. CurrentLowPowerModeSensitivity Attribute
This attribute SHALL indicate the current preference of the user for determining when the device
should enter a low power mode. The value of this attribute is the index, 0-based, into the LowPow
erModeSensitivities attribute for the currently selected preference.
If an attempt is made to set this attribute to an index outside the maximum index for LowPower
ModeSensitivities, a response with the status code CONSTRAINT_ERROR SHALL be returned.
If the value of LowPowerModeSensitivities changes after an update, the device SHALL migrate the
value of the LowPowerModeSensitivity attribute to the index which the manufacturer specifies
most closely matches the previous value.