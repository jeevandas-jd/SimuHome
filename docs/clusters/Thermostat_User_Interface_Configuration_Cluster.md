
# 4.5 Thermostat User Interface Configuration Cluster

This cluster provides an interface to allow configuration of the user interface for a thermostat, or a
thermostat controller device, that supports a keypad and LCD screen.

## Conversion of Temperature Values for Display
See the Temperature Conversion section in the Data Model for unit conversion between Fahrenheit
and Celsius.

## Data Types
4.5.5.1. TemperatureDisplayModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the Thermostat User Interface Configuration Cluster, specifically for the value '0', which is named 'Celsius'. This data type indicates that the temperature is displayed in degrees Celsius (°C). The conformance rule for this entry is 'M', meaning that this element is mandatory. Therefore, the Celsius temperature display is a required feature for any implementation of this cluster, and it must always be supported and available.

* The table row entry pertains to the "Thermostat User Interface Configuration Cluster" within the "Data Types" section. It describes a data type with the value '1', named 'Fahrenheit', which indicates that the temperature is displayed in degrees Fahrenheit (°F). The conformance rule for this entry is 'M', meaning that this feature is mandatory. Therefore, any implementation of the Thermostat User Interface Configuration Cluster must include the capability to display temperature in Fahrenheit, as it is a required element of the specification.

4.5.5.2. KeypadLockoutEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes a data type entry within the Thermostat User Interface Configuration Cluster, specifically for the value '0' named 'NoLockout'. This entry signifies that all functionality is available to the user, meaning there are no restrictions or lockouts on the thermostat's user interface. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any device or system that supports this cluster. There are no conditions or exceptions; the 'NoLockout' functionality must be present and available to users in all implementations of this cluster.

* The table row describes an element within the Thermostat User Interface Configuration Cluster, specifically a data type named "Lockout1," which represents a level 1 reduced functionality. The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "Lockout1" data type is always required to be implemented in any device or system that supports the Thermostat User Interface Configuration Cluster, without any conditions or exceptions.

* In the Thermostat User Interface Configuration Cluster, under the Data Types section, the entry for 'Lockout2' with a value of '2' and a summary of 'Level 2 reduced functionality' is described. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Lockout2' feature is always required to be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the Thermostat User Interface Configuration Cluster, within the Data Types section, the entry for 'Lockout3' with a value of '3' and a summary of 'Level 3 reduced functionality' is described. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Lockout3' feature is always required to be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the Thermostat User Interface Configuration Cluster, under the Data Types section, the entry for 'Lockout4' with a value of '4' and a summary of 'Level 4 reduced functionality' is described. The conformance for this entry is marked as 'M', which stands for Mandatory. This means that the 'Lockout4' element is always required to be implemented in any device or system that supports this cluster, without any conditions or exceptions.

* The table row entry pertains to the "Thermostat User Interface Configuration Cluster" within the "Data Types" section. It describes a data type named "Lockout5," which is identified by the value '5' and summarized as providing the "least functionality available to the user." The conformance rule for "Lockout5" is marked as 'M', indicating that this element is mandatory. This means that "Lockout5" must always be implemented and supported in any device or system that utilizes this cluster, without any conditions or exceptions.

The interpretation of the various levels is device-dependent.
4.5.5.3. ScheduleProgrammingVisibilityEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Thermostat User Interface Configuration Cluster, under the Data Types section, the entry for 'ScheduleProgrammingPermitted' with a value of '0' indicates that the local schedule programming functionality is enabled at the thermostat. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'ScheduleProgrammingPermitted' feature is always required to be implemented in devices that support this cluster, ensuring that users can always enable or disable local schedule programming on their thermostats.

* In the Thermostat User Interface Configuration Cluster, under the Data Types section, the entry for 'ScheduleProgrammingDenied' with a value of '1' indicates that the local schedule programming functionality is disabled at the thermostat. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented in any device that supports this cluster. This ensures that the functionality to disable local schedule programming is consistently available across all compliant devices.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Thermostat User Interface Configuration Cluster, specifically the "TemperatureDisplayMode" attribute. This attribute has an ID of '0x0000' and is of the type 'TemperatureDisplayModeEnum'. It is constrained to apply universally ('all'), with a default setting of 'Celsius'. The access level is 'RW VO', indicating it is readable and writable, and may have volatile access. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "TemperatureDisplayMode" attribute must always be implemented in any device that supports the Thermostat User Interface Configuration Cluster, without any conditions or exceptions.

* The table row describes an attribute named "KeypadLockout" within the Thermostat User Interface Configuration Cluster. This attribute has an ID of '0x0001' and is of the type 'KeypadLockoutEnum'. It applies universally ('Constraint': 'all') and defaults to 'NoLockout'. The attribute is accessible for reading and writing ('Access': 'RW') and is visible to management ('VM'). The conformance rule 'M' indicates that the "KeypadLockout" attribute is mandatory, meaning it is always required to be implemented in any device supporting this cluster, without any conditions or exceptions.

* The table row describes an attribute named "ScheduleProgrammingVisibility" within the Thermostat User Interface Configuration Cluster. This attribute has an ID of '0x0002' and is of the type 'ScheduleProgrammingVisibilityEnum'. It applies universally ('Constraint': 'all') and defaults to 'ScheduleProgrammingPermitted'. The attribute can be read and written ('Access': 'RW') and is subject to view management ('VM'). The conformance rule for this attribute is 'O', indicating that it is optional. This means that the implementation of this attribute is not required and does not depend on any other features or conditions.

4.5.6.1. TemperatureDisplayMode Attribute
This attribute SHALL indicate the units of the temperature displayed on the thermostat screen.
4.5.6.2. KeypadLockout Attribute
This attribute SHALL indicate the level of functionality that is available to the user via the keypad.
4.5.6.3. ScheduleProgrammingVisibility Attribute
This attribute is used to hide the weekly schedule programming functionality or menu on a thermo
stat from a user to prevent local user programming of the weekly schedule. The schedule program
ming MAY still be performed via a remote interface, and the thermostat MAY operate in schedule
programming mode.
This attribute is designed to prevent local tampering with or disabling of schedules that MAY have
been programmed by users or service providers via a more capable remote interface. The program
ming schedule SHALL continue to run even though it is not visible to the user locally at the thermo
stat.