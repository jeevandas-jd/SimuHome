
# 4.2 Pump Configuration and Control Cluster

The Pump Configuration and Control cluster provides an interface for the setup and control of
pump devices, and the automatic reporting of pump status information. Note that control of pump
speed is not included – speed is controlled by the On/Off and Level Control clusters.
Pump
Pump controller
Pump configuration and control
C S
C S
Level control
C S
On/Off
C S
= Client = Server
Note: Device names are examples for illustration purposes only
Figure 14. Typical Usage of Pump Configuration and Control Cluster

## Dependencies
Where external pressure, flow, and temperature measurements are processed by this cluster (see
ControlMode attribute), these are provided by a Pressure Measurement cluster, a Flow Measure
ment cluster, and a Temperature Measurement client cluster, respectively. These 3 client clusters
are used for connection to a remote sensor device. The pump is able to use the sensor measurement
provided by a remote sensor for regulation of the pump speed.
Note that control of the pump setpoint is not included in this cluster – the On/Off and Level Control
clusters (see Typical Usage of Pump Configuration and Control Cluster) MAY be used by a pump
device to turn it on and off and control its setpoint. Note that the Pump Configuration and Control
cluster MAY override on/off/setpoint settings for specific operation modes (See OperationMode
attribute for detailed description of the operation and control of the pump.).

## Data Types
4.2.6.1. PumpStatusBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the context of the Pump Configuration and Control Cluster, under the Data Types section, the table row describes a data element named 'DeviceFault' associated with bit '0'. The summary indicates that this element is used to detect faults related to the system or pump device. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that supports this cluster. There are no conditions or dependencies affecting its requirement; it must be present in all implementations.

* In the Pump Configuration and Control Cluster, under the Data Types section, the table row describes a data element named 'SupplyFault', which is represented by the bit '1'. This element indicates that a fault related to the supply to the pump has been detected. The conformance rule for 'SupplyFault' is marked as 'M', meaning it is mandatory. This implies that the 'SupplyFault' element is always required to be implemented in any device or system that uses this cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, within the Data Types section, the table row describes a feature named 'SpeedLow', which is associated with bit '2'. The summary indicates that this feature is used to signal when the setpoint is too low to achieve. The conformance rule for 'SpeedLow' is marked as 'M', which stands for Mandatory. This means that the 'SpeedLow' feature is always required to be implemented in any device or application that supports the Pump Configuration and Control Cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, under the Data Types section, the table entry for 'Bit' 3 is named 'SpeedHigh' and is summarized as indicating that the setpoint is too high to achieve. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'SpeedHigh' element is a required feature that must always be implemented in any device or system using this cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for the 'LocalOverride' feature, identified by bit '4', indicates that this feature is used when device control is overridden by hardware, such as an external STOP button or a local Human-Machine Interface (HMI). The conformance rule for 'LocalOverride' is marked as 'M', which means it is a Mandatory feature. This implies that the 'LocalOverride' feature must always be implemented in any device that supports the Pump Configuration and Control Cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, under the Data Types section, the table row describes a data element with the bit position '5', named 'Running'. This element indicates whether the pump is currently running. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Running' data element is always required to be implemented in any device or system that supports the Pump Configuration and Control Cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'RemotePressure' with a bit value of '6' indicates that this data type represents the use of a remote pressure sensor for regulating the pump. The conformance rule for 'RemotePressure' is marked as 'M', which stands for Mandatory. This means that the inclusion of this element is always required within the context of the specification. Therefore, any implementation of the Pump Configuration and Control Cluster must include support for the 'RemotePressure' data type, ensuring that a remote pressure sensor is used for pump regulation.

* In the Pump Configuration and Control Cluster, under the Data Types section, the table row describes a feature named 'RemoteFlow', which is associated with bit 7. The summary indicates that this feature involves using a remote flow sensor to regulate the pump. The conformance rule for 'RemoteFlow' is marked as 'M', which stands for Mandatory. This means that the feature is always required to be implemented in any device or system that supports this cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'RemoteTemperature' is defined with a bit size of 8. This data type represents a remote temperature sensor used for regulating the pump. The conformance rule for 'RemoteTemperature' is marked as 'M', which stands for Mandatory. This means that the inclusion of this element is always required in any implementation of the Pump Configuration and Control Cluster, without any conditions or exceptions.

4.2.6.1.1. DeviceFault Bit
If this bit is set, it MAY correspond to an event in the range 2-16, see Events.
4.2.6.1.2. SupplyFault Bit
If this bit is set, it MAY correspond to an event in the range 0-1 or 13, see Events.
4.2.6.1.3. LocalOverride Bit
While this bit is set, the EffectiveOperationMode is adjusted to Local. Any request changing Opera
tionMode SHALL generate a FAILURE error status until LocalOverride is cleared on the physical
device. When LocalOverride is cleared, the device SHALL return to the operation mode set in Oper
ationMode.
4.2.6.1.4. RemotePressure Bit
If this bit is set, EffectiveControlMode is ConstantPressure and the setpoint for the pump is inter
preted as a percentage of the range of the remote sensor ([MinMeasuredValue – MaxMeasured
Value]).
4.2.6.1.5. RemoteFlow Bit
If this bit is set, EffectiveControlMode is ConstantFlow, and the setpoint for the pump is interpreted
as a percentage of the range of the remote sensor ([MinMeasuredValue – MaxMeasuredValue]).
4.2.6.1.6. RemoteTemperature Bit
If this bit is set, EffectiveControlMode is ConstantTemperature, and the setpoint for the pump is
interpreted as a percentage of the range of the remote sensor ([MinMeasuredValue – MaxMeasured
Value])
4.2.6.2. OperationModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Pump Configuration and Control Cluster, specifically within the Data Types section, the table entry describes a data type with the value '0' named 'Normal'. This data type indicates that the pump is being controlled by a setpoint, which can be determined by a connected remote sensor or the ControlMode attribute. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Normal' data type is always required to be implemented in any device or system that supports the Pump Configuration and Control Cluster, ensuring consistent behavior across all compliant devices.

* The table row describes an entry within the Pump Configuration and Control Cluster, specifically under the Data Types section. The entry is named "Minimum" and has a value of '1'. It represents a setting that configures the pump to operate at its minimum possible speed without stopping. The conformance rule for this entry is 'SPD', which indicates that the "Minimum" setting is mandatory if the feature or condition represented by 'SPD' is supported. If 'SPD' is not supported, the conformance of this entry is not explicitly defined in this row, implying it may not be required.

* The table row describes a data type within the Pump Configuration and Control Cluster, specifically named "Maximum," which is assigned a value of '2'. This data type is used to set the pump to operate at its maximum possible speed. The conformance rule for this entry is 'SPD', indicating that the element is mandatory if the feature 'SPD' (likely representing a specific speed-related feature) is supported. If the 'SPD' feature is not supported, the conformance of this element is not explicitly defined in this entry, suggesting it may not be required or applicable.

* The table row describes a data type within the Pump Configuration and Control Cluster, specifically the 'Local' value, which is assigned the numerical value '3'. This setting allows the pump to operate according to its local settings, irrespective of what those settings might be. The 'Conformance' field for this entry is marked as 'LOCAL', which, according to the Matter Conformance Interpretation Guide, suggests that the conformance condition is described elsewhere in the documentation. This implies that the rules or conditions under which the 'Local' value is required or optional are too complex to be captured by a simple conformance tag or expression and need to be referenced in another part of the specification for a detailed explanation.

4.2.6.2.1. Normal Value
If the pump is running in this operation mode the setpoint is an internal variable which MAY be
controlled between 0% and 100%, e.g., by means of the Level Control cluster
4.2.6.3. ControlModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Pump Configuration and Control Cluster, the data type entry for 'ConstantSpeed' with a value of '0' indicates that this represents a state where the pump operates at a constant speed. The summary succinctly describes this operational mode. The conformance rule 'SPD' suggests that the inclusion or requirement of this element is contingent upon the support of a feature or condition denoted by 'SPD'. If the feature 'SPD' is supported, then the 'ConstantSpeed' element is mandatory. If 'SPD' is not supported, the conformance of 'ConstantSpeed' is not explicitly defined in this entry, implying that it may not be required or applicable.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'ConstantPressure' with a value of '1' indicates a mode where the pump adjusts its speed to maintain a constant differential pressure across its flanges. The conformance rule 'PRSCONST' suggests that the inclusion of this feature is conditional based on the support of a specific feature or condition labeled 'PRSCONST'. If 'PRSCONST' is supported, then the 'ConstantPressure' feature is mandatory. The conformance rule does not specify any alternative conditions or fallback options, implying that the presence of 'PRSCONST' is the sole determinant for this feature's requirement.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'ProportionalPressure' indicates a feature where the pump adjusts its speed to keep a constant differential pressure across its flanges. The conformance rule 'PRSCOMP' suggests that the requirement for this feature is described elsewhere in the documentation, as it does not fit into the basic conformance tags or logical conditions provided. This implies that the conditions under which 'ProportionalPressure' is required are complex and need to be referenced from a detailed description outside of the standard conformance tags.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'ConstantFlow' with a value of '3' indicates that this feature allows the pump to regulate its speed to maintain a constant flow. The conformance rule 'FLW' specifies that the 'ConstantFlow' feature is mandatory if the 'FLW' feature is supported. This means that if the system or device includes the 'FLW' feature, it must also implement the 'ConstantFlow' capability to ensure consistent flow regulation.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry for 'ConstantTemperature' with a value of '5' indicates that this feature allows the pump to adjust its speed to maintain a constant temperature. The conformance rule 'TEMP' implies that the inclusion of this feature is mandatory if the 'TEMP' condition is met. This means that if the system or device supports the 'TEMP' feature, then the 'ConstantTemperature' capability must be implemented. If 'TEMP' is not supported, the conformance rule does not specify an alternative requirement, suggesting that the feature is not required in such cases.

* In the Pump Configuration and Control Cluster, under the Data Types section, the entry with the value '7' and name 'Automatic' describes a mode where the pump's operation is automatically optimized for optimal performance, balancing comfort and energy efficiency. The conformance rule 'AUTO' indicates that this feature is conditionally mandatory based on the support of the 'AUTO' feature. If the 'AUTO' feature is supported, the 'Automatic' mode is required; otherwise, the conformance of this mode is not specified in this entry, implying it may not be applicable or is described elsewhere.

4.2.6.3.1. ConstantSpeed Value
The setpoint is interpreted as a percentage of the range derived from the [MinConstSpeed – Max
ConstSpeed] attributes.
4.2.6.3.2. ConstantPressure Value
The setpoint is interpreted as a percentage of the range of the sensor used for this control mode. In
case of the internal pressure sensor, this will be the range derived from the [MinConstPressure –
MaxConstPressure] attributes. In case of a remote pressure sensor, this will be the range derived
from the [MinMeasuredValue – MaxMeasuredValue] attributes of the remote pressure sensor.
4.2.6.3.3. ProportionalPressure Value
The setpoint is interpreted as a percentage of the range derived of the [MinCompPressure – Max
CompPressure] attributes. The internal setpoint will be lowered (compensated) dependent on the
flow in the pump (lower flow ⇒ lower internal setpoint).
4.2.6.3.4. ConstantFlow Value
The setpoint is interpreted as a percentage of the range of the sensor used for this control mode. In
case of the internal flow sensor, this will be the range derived from the [MinConstFlow – MaxConst
Flow] attributes. In case of a remote flow sensor, this will be the range derived from the [MinMea
suredValue – MaxMeasuredValue] attributes of the remote flow sensor.
4.2.6.3.5. ConstantTemperature Value
The setpoint is interpreted as a percentage of the range of the sensor used for this control mode. In
case of the internal temperature sensor, this will be the range derived from the [MinConstTemp –
MaxConstTemp] attributes. In case of a remote temperature sensor, this will be the range derived
from the [MinMeasuredValue – MaxMeasuredValue] attributes of the remote temperature sensor.
4.2.6.3.6. Automatic Value
This behavior is manufacturer defined. The pump can be stopped by setting the setpoint of the level
control cluster to 0, or by using the On/Off cluster. If the pump is started (at any setpoint), the speed
of the pump is entirely determined by the pump.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Pump Configuration and Control Cluster, specifically the 'MaxPressure' attribute. This attribute has an ID of '0x0000' and is of type 'int16', meaning it is a 16-bit integer. The 'Constraint' field indicates that this attribute applies universally ('all'), and its 'Quality' is marked as 'X F', suggesting specific quality or feature constraints that are not detailed here. The 'Default' value is 'null', indicating that it does not have a predefined default value. The 'Access' field 'R V' signifies that the attribute is readable and has some form of volatile access. The 'Conformance' field is marked as 'M', which means that the 'MaxPressure' attribute is mandatory and must always be implemented in any device supporting this cluster, without any conditions or exceptions.

* In the Pump Configuration and Control Cluster, the attribute 'MaxSpeed' is identified by the ID '0x0001' and is of type 'uint16'. It has a constraint applicable to all instances, and its quality is marked as 'X F', indicating specific quality characteristics that are not detailed here. The default value for 'MaxSpeed' is 'null', and it has read and view access permissions ('R V'). The conformance rule for 'MaxSpeed' is 'M', which means this attribute is mandatory and must always be implemented in any device that supports the Pump Configuration and Control Cluster. This requirement is unconditional, with no dependencies or conditions affecting its mandatory status.

* The table row describes an attribute named "MaxFlow" within the Pump Configuration and Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0002' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' field indicates that this attribute applies universally ('all'), and its 'Quality' is marked as 'X F', suggesting certain quality characteristics or restrictions, though these are not detailed here. The 'Default' value is 'null', indicating that it does not have a predefined default value. The 'Access' is specified as 'R V', meaning it is readable and possibly volatile. The 'Conformance' is marked as 'M', which, according to the Matter Conformance Interpretation Guide, signifies that the "MaxFlow" attribute is mandatory. This means it is always required to be implemented in any device or application using this cluster, without any conditions or exceptions.

* The table row describes an attribute named "MinConstPressure" within the Pump Configuration and Control Cluster, identified by the ID '0x0003'. This attribute is of type 'int16' and applies universally ('Constraint': 'all'). Its quality is marked as 'X F', indicating it is disallowed for some reason, and it has no default value ('Default': 'null'). The access level is 'R V', meaning it is readable and volatile. The conformance rule 'PRSCONST, [AUTO]' indicates that this attribute is mandatory if the feature 'PRSCONST' (likely representing a specific pressure constant feature) is supported. If 'PRSCONST' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. This rule ensures that the attribute's requirement is conditional based on the presence of these specific features.

* The table row describes an attribute named "MaxConstPressure" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0004' and is of type 'int16', with a constraint labeled as 'all'. The quality is marked as 'X F', indicating it is disallowed in some contexts and possibly flagged for future consideration. The default value is 'null', and it has read and view access ('R V'). The conformance rule 'PRSCONST, [AUTO]' means that the "MaxConstPressure" attribute is mandatory if the feature 'PRSCONST' is supported. If 'PRSCONST' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. This rule provides flexibility depending on the features implemented in the device.

* The table row describes an attribute named "MinCompPressure" within the Pump Configuration and Control Cluster, specifically in the Attributes section. This attribute has an ID of '0x0005' and is of type 'int16', with a constraint applicable to all instances. It has a quality designation of 'X F', indicating it is disallowed in some contexts and has a specific feature-related quality. The default value is 'null', and it has read and volatile access permissions ('R V'). The conformance rule 'PRSCOMP, [AUTO]' indicates that the "MinCompPressure" attribute is mandatory if the feature 'PRSCOMP' is supported. If 'PRSCOMP' is not supported but 'AUTO' is, then the attribute becomes optional. If neither condition is met, the attribute is not required.

* The table row describes an attribute named "MaxCompPressure" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0006' and is of type 'int16', with no specific default value assigned ('null'). It is constrained to apply to all instances ('Constraint': 'all') and has a quality designation of 'X F', indicating it is explicitly disallowed for some reason, possibly related to future considerations. The access level is 'R V', meaning it is readable and may have volatile characteristics. The conformance rule 'PRSCOMP, [AUTO]' indicates that the "MaxCompPressure" attribute is mandatory if the feature 'PRSCOMP' is supported. If 'PRSCOMP' is not supported, the attribute becomes optional if the 'AUTO' condition is met. This rule ensures that the attribute's requirement is contextually dependent on the presence of specific features or conditions within the device's implementation.

* The table row describes an attribute named "MinConstSpeed" within the Pump Configuration and Control Cluster, identified by the ID '0x0007'. This attribute is of type 'uint16', with a constraint applicable to all instances, and it has no default value specified ('null'). The attribute's quality is marked as 'X F', indicating it is disallowed in some contexts. Access to this attribute is read-only ('R') and it is volatile ('V'). The conformance rule 'SPD, [AUTO]' specifies that the "MinConstSpeed" attribute is mandatory if the feature 'SPD' is supported. If 'SPD' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. If neither condition is met, the attribute is not required.

* The table row describes an attribute named "MaxConstSpeed" within the Pump Configuration and Control Cluster, identified by the ID '0x0008'. This attribute is of type 'uint16' and applies universally ('Constraint': 'all'). It is marked with a quality of 'X F', indicating it is disallowed in some contexts and may have future considerations. The default value is 'null', and it has read ('R') and volatile ('V') access permissions. The conformance rule 'SPD, [AUTO]' specifies that the "MaxConstSpeed" attribute is mandatory if the 'SPD' feature is supported. If 'SPD' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. This rule ensures that the attribute's requirement is contingent on the presence of specific features within the device's configuration.

* The table row describes an attribute named "MinConstFlow" within the Pump Configuration and Control Cluster, identified by the ID '0x0009'. This attribute is of type 'uint16', with a constraint applicable to all instances, and it does not have a default value ('null'). Its quality is marked as 'X F', indicating it is disallowed in some contexts. The access level is 'R V', meaning it is readable and volatile. The conformance rule 'FLW, [AUTO]' specifies that the "MinConstFlow" attribute is mandatory if the feature 'FLW' is supported. If 'FLW' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. This rule ensures that the attribute's requirement is contingent on the presence of specific features, adapting its necessity based on the device's capabilities.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "MaxConstFlow" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x000A' and is of type 'uint16', with no specific default value ('null'). It is constrained to be applicable in all contexts ('Constraint': 'all') and has a quality designation of 'X F', which typically indicates specific quality or feature-related notes. The access level is 'R V', meaning it is readable and possibly volatile. The conformance rule 'FLW, [AUTO]' indicates that the "MaxConstFlow" attribute is mandatory if the feature 'FLW' (likely related to flow control) is supported. If 'FLW' is not supported, the attribute becomes optional if the 'AUTO' feature (possibly related to automatic control) is supported. If neither condition is met, the attribute is not required.

* The table row describes an attribute named "MinConstTemp" within the Pump Configuration and Control Cluster's Attributes section. This attribute has an ID of '0x000B' and is of type 'int16', with a constraint that it cannot be less than -27315. The 'Quality' field indicates that this attribute is disallowed ('X') and has a future status ('F'). The default value is 'null', and it has read ('R') and volatile ('V') access permissions. The conformance rule 'TEMP, [AUTO]' means that the "MinConstTemp" attribute is mandatory if the feature 'TEMP' is supported. If 'TEMP' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. If neither condition is met, the attribute is not required.

* The table row describes an attribute named "MaxConstTemp" within the Pump Configuration and Control Cluster, identified by the ID '0x000C'. This attribute is of type 'int16' and has a minimum constraint of -27315. It is marked with a quality of 'X F', indicating it is disallowed and has a future status. The default value is 'null', and it has read and view access ('R V'). The conformance rule 'TEMP, [AUTO]' means that the "MaxConstTemp" attribute is mandatory if the feature 'TEMP' is supported. If 'TEMP' is not supported, the attribute becomes optional if the 'AUTO' feature is supported. If neither condition is met, the attribute is not required.

* The table row describes an attribute named "PumpStatus" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0010' and is of the type 'PumpStatusBitmap'. The constraint for this attribute is described elsewhere in the documentation, indicating complexity. It is marked with a quality of 'P', meaning its status is provisional and may change in the future. The default value for this attribute is '0', and it has read and view access ('R V'). The conformance rule for "PumpStatus" is 'O', which means that this attribute is optional and not required to be implemented, with no dependencies on other features or conditions.

* The table row describes an attribute within the Pump Configuration and Control Cluster, specifically the "EffectiveOperationMode" attribute. This attribute is identified by the ID '0x0011' and is of the type 'OperationModeEnum'. The constraints and default values for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The attribute has a quality of 'N', meaning it is not nullable, and it has read and view access, as denoted by 'R V'. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "EffectiveOperationMode" attribute must always be implemented in any device that supports the Pump Configuration and Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "EffectiveControlMode" within the Pump Configuration and Control Cluster, identified by the ID '0x0012'. This attribute is of the type 'ControlModeEnum' and has constraints and default values that are described elsewhere in the documentation. The 'Quality' is marked as 'N', and the 'Access' is specified as 'R V', indicating it is readable and has volatile access characteristics. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "EffectiveControlMode" attribute must always be implemented in any device supporting the Pump Configuration and Control Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Pump Configuration and Control Cluster, specifically the 'Capacity' attribute. This attribute has an ID of '0x0013' and is of type 'int16', meaning it is a 16-bit integer. The 'Constraint' field indicates that this attribute applies universally ('all'). The 'Quality' field lists 'X P', suggesting that while the attribute is currently disallowed ('X'), it is provisionally marked ('P') for potential future use. The 'Default' value is 'null', indicating no default value is set. The 'Access' field 'R V' means the attribute is readable ('R') and has volatile characteristics ('V'). The 'Conformance' field is marked as 'M', which means this attribute is mandatory and must always be implemented in any device using this cluster, according to the Matter specification.

* The table row describes an attribute named "Speed" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0014' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that there are no specific constraints on its value beyond the typical range for a uint16. The 'Quality' is marked as 'X', which means this attribute is explicitly disallowed from being used in certain contexts or configurations. The 'Default' value is 'null', suggesting that there is no predefined default value for this attribute. The 'Access' is 'R V', indicating that the attribute is readable ('R') and volatile ('V'), meaning its value can change without a write operation. The 'Conformance' is 'O', which means that the "Speed" attribute is optional; it is not required to be implemented and has no dependencies on other features or conditions.

* The table row describes an attribute named "LifetimeRunningHours" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0015' and is of type 'uint24', meaning it is a 24-bit unsigned integer. The 'Constraint' is set to 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X N', suggesting it is disallowed in certain contexts or configurations. The default value for this attribute is '0', and it has 'RW VM' access, meaning it is readable and writable, with VM indicating it may have vendor-specific modifications. The 'Conformance' is labeled as 'O', which means this attribute is optional and not required for implementation, with no dependencies affecting its inclusion.

* The table row describes an attribute within the Pump Configuration and Control Cluster, specifically the "Power" attribute with an ID of '0x0016'. This attribute is of type 'uint24', meaning it is a 24-bit unsigned integer, and it is constrained to be applicable in all contexts. The quality of this attribute is marked as 'X', indicating that it is explicitly disallowed and should not be used. The default value for this attribute is 'null', and it has read and volatile access permissions, denoted by 'R V'. The conformance rule for this attribute is 'O', meaning that its inclusion is optional and there are no dependencies or conditions that mandate its presence.

* The table row describes an attribute named "LifetimeEnergyConsumed" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0017' and is of type 'uint32', meaning it stores a 32-bit unsigned integer. The 'Constraint' is 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X N', suggesting it is disallowed in certain contexts or configurations. The default value for this attribute is '0', and it has 'RW VM' access, meaning it can be read and written, with VM indicating specific access conditions or modes. The 'Conformance' is 'O', which means this attribute is optional and not required by default, with no dependencies or conditions affecting its inclusion.

* The table row describes an attribute named "OperationMode" within the Pump Configuration and Control Cluster. This attribute has an ID of '0x0020' and is of the type 'OperationModeEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'N', and the default value is '0'. The attribute has 'RW VM' access, meaning it is readable and writable, with additional access control based on vendor-specific mechanisms. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the "OperationMode" attribute must always be implemented in any device that supports the Pump Configuration and Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "ControlMode" within the Pump Configuration and Control Cluster, identified by the ID '0x0021'. This attribute is of the type 'ControlModeEnum' and has a default value of '0'. It is constrained by a description detailed elsewhere in the documentation, indicated by 'desc'. The attribute has a quality of 'N', which typically denotes a specific characteristic or requirement not elaborated here. The access level is 'RW VM', meaning it can be read and written, and it is subject to verification and monitoring. The conformance rule for "ControlMode" is 'O', indicating that this attribute is optional. It is not required for implementation and does not depend on any other features or conditions within the specification.

* In the Pump Configuration and Control Cluster, within the context of Attributes, the entry for 'AlarmMask' with ID '0x0022' is marked with a conformance of 'D'. This indicates that the 'AlarmMask' attribute is considered deprecated according to the current Matter specification. As a deprecated element, it is obsolete and should not be used in new implementations. Existing implementations that still use this attribute should plan for its removal or replacement, as it may be removed in future versions of the specification.

4.2.7.1. MaxPressure Attribute
This attribute specifies the maximum pressure the pump can achieve. It is a physical limit, and does
not apply to any specific control mode or operation mode.
Valid range is -3,276.7 kPa to 3,276.7 kPa (steps of 0.1 kPa).
This attribute SHALL be null if the value is invalid.
4.2.7.2. MaxSpeed Attribute
This attribute specifies the maximum speed the pump can achieve. It is a physical limit, and does
not apply to any specific control mode or operation mode.
Valid range is 0 to 65,534 RPM (steps of 1 RPM).
This attribute SHALL be null if the value is invalid.
4.2.7.3. MaxFlow Attribute
This attribute specifies the maximum flow the pump can achieve. It is a physical limit, and does not
apply to any specific control mode or operation mode.
3 3 3
Valid range is 0 m /h to 6,553.4 m /h (steps of 0.1 m /h).
This attribute SHALL be null if the value is invalid.
4.2.7.4. MinConstPressure Attribute
This attribute specifies the minimum pressure the pump can achieve when it is working with the
ControlMode attribute set to ConstantPressure.
Valid range is –3,276.7 kPa to 3,276.7 kPa (steps of 0.1 kPa).
This attribute SHALL be null if the value is invalid.
4.2.7.5. MaxConstPressure Attribute
This attribute specifies the maximum pressure the pump can achieve when it is working with the
ControlMode attribute set to ConstantPressure.
Valid range is –3,276.7 kPa to 3,276.7 kPa (steps of 0.1 kPa).
This attribute SHALL be null if the value is invalid.
4.2.7.6. MinCompPressure Attribute
This attribute specifies the minimum compensated pressure the pump can achieve when it is work
ing with the ControlMode attribute set to ProportionalPressure.
Valid range is –3,276.7 kPa to 3,276.7 kPa (steps of 0.1 kPa).
This attribute SHALL be null if the value is invalid.
4.2.7.7. MaxCompPressure Attribute
This attribute specifies the maximum compensated pressure the pump can achieve when it is work
ing with the ControlMode attribute set to ProportionalPressure.
Valid range is –3,276.7 kPa to 3,276.7 kPa (steps of 0.1 kPa).
This attribute SHALL be null if the value is invalid.
4.2.7.8. MinConstSpeed Attribute
This attribute specifies the minimum speed the pump can achieve when it is working with the Con
trolMode attribute set to ConstantSpeed.
Valid range is 0 to 65,534 RPM (steps of 1 RPM).
This attribute SHALL be null if the value is invalid.
4.2.7.9. MaxConstSpeed Attribute
This attribute specifies the maximum speed the pump can achieve when it is working with the Con
trolMode attribute set to ConstantSpeed.
Valid range is 0 to 65,534 RPM (steps of 1 RPM).
This attribute SHALL be null if the value is invalid.
4.2.7.10. MinConstFlow Attribute
This attribute specifies the minimum flow the pump can achieve when it is working with the Con
trolMode attribute set to ConstantFlow.
3 3 3
Valid range is 0 m /h to 6,553.4 m /h (steps of 0.1 m /h).
This attribute SHALL be null if the value is invalid.
4.2.7.11. MaxConstFlow Attribute
This attribute specifies the maximum flow the pump can achieve when it is working with the Con
trolMode attribute set to ConstantFlow.
3 3 3
Valid range is 0 m /h to 6,553.4 m /h (steps of 0.1 m /h).
This attribute SHALL be null if the value is invalid.
4.2.7.12. MinConstTemp Attribute
This attribute specifies the minimum temperature the pump can maintain in the system when it is
working with the ControlMode attribute set to ConstantTemperature.
Valid range is –273.15 °C to 327.67 °C (steps of 0.01 °C).
This attribute SHALL be null if the value is invalid.
4.2.7.13. MaxConstTemp Attribute
This attribute specifies the maximum temperature the pump can maintain in the system when it is
working with the ControlMode attribute set to ConstantTemperature.
MaxConstTemp SHALL be greater than or equal to MinConstTemp
Valid range is –273.15 °C to 327.67 °C (steps of 0.01 °C).
This attribute SHALL be null if the value is invalid.
4.2.7.14. PumpStatus Attribute
This attribute specifies the activity status of the pump functions as listed in PumpStatusBitmap.
Where a pump controller function is active, the corresponding bit SHALL be set to 1. Where a pump
controller function is not active, the corresponding bit SHALL be set to 0.
4.2.7.15. EffectiveOperationMode Attribute
This attribute specifies current effective operation mode of the pump as defined in OperationMod
eEnum.
The value of the EffectiveOperationMode attribute is the same as the OperationMode attribute,
unless one of the following points are true:
• The pump is physically set to run with the local settings
• The LocalOverride bit in the PumpStatus attribute is set,
See OperationMode and ControlMode attributes for a detailed description of the operation and con
trol of the pump.
4.2.7.16. EffectiveControlMode Attribute
This attribute specifies the current effective control mode of the pump as defined in ControlMod
eEnum.
This attribute contains the control mode that currently applies to the pump. It will have the value of
the ControlMode attribute, unless one of the following points are true:
• The ControlMode attribute is set to Automatic. In this case, the value of the EffectiveCon
trolMode SHALL match the behavior of the pump.
• A remote sensor is used as the sensor for regulation of the pump. In this case, EffectiveCon
trolMode will display ConstantPressure, ConstantFlow or ConstantTemperature if the remote
sensor is a pressure sensor, a flow sensor or a temperature sensor respectively, regardless of the
value of the ControlMode attribute.
In case the ControlMode attribute is not included on the device and no remote sensors are con
nected, the value of the EffectiveControlMode SHALL match the vendor-specific behavior of the
pump.
See OperationMode and ControlMode attributes for detailed a description of the operation and con
trol of the pump.
4.2.7.17. Capacity Attribute
This attribute specifies the actual capacity of the pump as a percentage of the effective maximum
setpoint value. It is updated dynamically as the speed of the pump changes.
If the value is not available (the measurement or estimation of the speed is done in the pump), this
attribute will indicate the null value.
Valid range is 0 % to 163.835% (0.005 % granularity). Although this attribute is a signed value, val
ues of capacity less than zero have no physical meaning.
4.2.7.18. Speed Attribute
This attribute specifies the actual speed of the pump measured in RPM. It is updated dynamically as
the speed of the pump changes.
If the value is not available (the measurement or estimation of the speed is done in the pump), this
attribute will indicate the null value.
Valid range is 0 to 65,534 RPM.
4.2.7.19. LifetimeRunningHours Attribute
This attribute specifies the accumulated number of hours that the pump has been powered and the
motor has been running. It is updated dynamically as it increases. It is preserved over power cycles
of the pump. If LifeTimeRunningHours rises above maximum value it “rolls over” and starts at 0
(zero).
This attribute is writeable, in order to allow setting to an appropriate value after maintenance. If
the value is not available, this attribute will indicate the null value.
Valid range is 0 to 16,777,214 hrs.
4.2.7.20. Power Attribute
This attribute specifies the actual power consumption of the pump in Watts. The value of this
attribute is updated dynamically as the power consumption of the pump changes.
This attribute is read only. If the value is not available (the measurement of power consumption is
not done in the pump), this attribute will indicate the null value.
Valid range is 0 to 16,777,214 Watts.
4.2.7.21. LifetimeEnergyConsumed Attribute
This attribute specifies the accumulated energy consumption of the pump through the entire life
time of the pump in kWh. The value of the LifetimeEnergyConsumed attribute is updated dynami
cally as the energy consumption of the pump increases. If LifetimeEnergyConsumed rises above
maximum value it “rolls over” and starts at 0 (zero).
This attribute is writeable, in order to allow setting to an appropriate value after maintenance.
Valid range is 0 kWh to 4,294,967,294 kWh.
This attribute SHALL be null if the value is unknown.
4.2.7.22. OperationMode Attribute
This attribute specifies the operation mode of the pump as defined in OperationModeEnum.
The actual operating mode of the pump is a result of the setting of the attributes OperationMode,
ControlMode and the optional connection of a remote sensor. The operation and control is priori
tized as shown in the scheme below:
Priority Scheme of Pump Operation and Control
If this attribute is Maximum, Minimum or Local, the OperationMode attribute decides how the
pump is operated.
If this attribute is Normal and a remote sensor is connected to the pump, the type of the remote sen
sor decides the control mode of the pump. A connected remote pressure sensor will make the pump
run in control mode Constant pressure and vice versa for flow and temperature type sensors. This
is regardless of the setting of the ControlMode attribute.
If this attribute is Normal and no remote sensor is connected, the control mode of the pump is
decided by the ControlMode attribute.
OperationMode MAY be changed at any time, even when the pump is running. The behavior of the
pump at the point of changing the value of this attribute is vendor-specific.
In the case a device does not support a specific operation mode, the write interaction to this
attribute with an unsupported operation mode value SHALL be ignored and a response containing
the status of CONSTRAINT_ERROR SHALL be returned.
4.2.7.23. ControlMode Attribute
This attribute specifies the control mode of the pump as defined in ControlModeEnum.
See the OperationMode attribute for a detailed description of the operation and control of the
pump.
ControlMode MAY be changed at any time, even when the pump is running. The behavior of the
pump at the point of changing is vendor-specific.
In the case a device does not support a specific control mode, the write interaction to this attribute
with an unsupported control mode value SHALL be ignored and a response containing the status of
CONSTRAINT_ERROR SHALL be returned.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "SupplyVoltageLow" event, identified by the ID '0x00'. This event has a priority level of 'INFO', indicating it provides informational messages about the system's status. The 'Access' field is marked as 'V', which typically denotes that the event is visible or can be accessed in some manner. The 'Conformance' field is marked as 'O', meaning that the "SupplyVoltageLow" event is optional. This indicates that the implementation of this event is not required and has no dependencies on other features or conditions. Therefore, manufacturers or developers can choose whether to include this event in their devices without any obligation from the Matter specification.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "SupplyVoltageHigh" event, identified by the ID '0x01'. This event has a priority level of 'INFO', indicating it provides informational messages. The access level is marked as 'V', which typically denotes that the event is visible or can be accessed for viewing. The conformance rule for this event is 'O', meaning it is optional. This indicates that the implementation of the "SupplyVoltageHigh" event is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this event based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the context of the Pump Configuration and Control Cluster, the table row describes an event with the ID '0x02' named 'PowerMissingPhase'. This event is categorized with a priority level of 'INFO', indicating it provides informational messages. The 'Access' field marked as 'V' suggests that this event is visible or can be accessed in some way. The 'Conformance' field is marked as 'O', which means that the 'PowerMissingPhase' event is optional. This implies that the implementation of this event is not required and does not depend on any other features or conditions. Devices or systems implementing the Pump Configuration and Control Cluster can choose to include this event, but it is not mandatory for compliance with the Matter specification.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "SystemPressureLow" event, identified by the ID '0x03'. This event has a priority level of 'INFO', indicating it provides informational messages about the system's status. The 'Access' field is marked as 'V', which typically denotes that the event is viewable. The 'Conformance' field is marked as 'O', meaning that the "SystemPressureLow" event is optional. This implies that the implementation of this event is not required and there are no dependencies or conditions that mandate its inclusion in a device's functionality. Therefore, manufacturers have the discretion to include or exclude this event based on their specific product requirements or design choices.

* The table row describes an event named "SystemPressureHigh" within the Pump Configuration and Control Cluster, identified by the ID '0x04'. This event is categorized with a priority level of 'INFO', indicating it provides informational messages about the system's status. The 'Access' field marked as 'V' suggests that this event is visible or can be accessed in some manner. The 'Conformance' field is marked as 'O', which means that the "SystemPressureHigh" event is optional. This implies that the implementation of this event is not required and has no dependencies on other features or conditions within the Matter specification. Therefore, manufacturers can choose whether to include this event in their devices without affecting compliance with the standard.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "DryRunning" event, which is identified by the ID '0x05'. This event is categorized with a 'CRITICAL' priority, indicating its importance in the system. The 'Access' field is marked as 'V', suggesting it is visible or can be accessed in some manner. The 'Conformance' field is marked as 'O', which means that the "DryRunning" event is optional. This implies that while the event can be implemented within the system, it is not required and has no dependencies on other features or conditions. Therefore, manufacturers have the discretion to include or exclude this event based on their specific product requirements or design choices.

* The table row entry pertains to the "MotorTemperatureHigh" event within the Pump Configuration and Control Cluster, specifically under the Events section. This event is identified by the ID '0x06' and has a priority level of 'INFO', indicating that it provides informational alerts regarding the motor temperature. The access level is marked as 'V', which typically denotes that the event is viewable or can be accessed for monitoring purposes. The conformance rule for this event is 'O', meaning it is optional. This indicates that the implementation of the "MotorTemperatureHigh" event is not required and can be included at the discretion of the device manufacturer, without any dependencies or conditions that mandate its presence.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "PumpMotorFatalFailure" event, identified by the ID '0x07'. This event is classified with a 'CRITICAL' priority, indicating its importance in the system. The 'Access' field is marked as 'V', which typically denotes that the event is viewable or can be accessed in some manner. The 'Conformance' field is marked as 'O', meaning that the "PumpMotorFatalFailure" event is optional. This implies that the implementation of this event is not required and does not depend on any other features or conditions. Therefore, manufacturers have the discretion to include or exclude this event in their devices without affecting compliance with the Matter specification.

* In the Pump Configuration and Control Cluster, within the Events section, the entry with ID '0x08' is named 'ElectronicTemperatureHigh' and is categorized with a priority level of 'INFO'. The access level is denoted as 'V', indicating that it is viewable. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'ElectronicTemperatureHigh' event is not required to be implemented in all devices or systems using this cluster; it can be included at the discretion of the implementer without any dependencies or conditions.

* The table row entry describes an event within the Pump Configuration and Control Cluster, specifically the "PumpBlocked" event, which has an ID of '0x09'. This event is categorized with a "CRITICAL" priority, indicating its importance in the system. The "Access" field is marked as 'V', which typically denotes that the event is visible or can be accessed in some manner. The "Conformance" field is marked as 'O', meaning that the "PumpBlocked" event is optional. This indicates that the implementation of this event is not required and does not depend on any other features or conditions. Therefore, developers have the discretion to include or exclude this event in their implementation of the Pump Configuration and Control Cluster without any mandatory requirements.

* In the Pump Configuration and Control Cluster, within the Events section, the table row describes an event identified by the ID '0x0A' and named 'SensorFailure'. This event has a priority level of 'INFO', indicating it provides informational messages about sensor failures. The access level is 'V', which typically means it is viewable. The conformance rule for this event is 'O', meaning it is optional. This indicates that the inclusion of the 'SensorFailure' event is not required and has no dependencies on other features or conditions. Implementers of the Matter specification can choose to support this event at their discretion.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically identified by the ID '0x0B' and named 'ElectronicNonFatalFailure'. This event is categorized with a priority level of 'INFO', indicating it provides informational messages about non-critical issues. The 'Access' is marked as 'V', which typically denotes visibility or read access. The 'Conformance' field is labeled as 'O', meaning that the 'ElectronicNonFatalFailure' event is optional. This implies that the implementation of this event is not required and does not depend on any other features or conditions within the Matter specification. Devices implementing this cluster can choose to support this event, but it is not mandatory for compliance.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "ElectronicFatalFailure" event, identified by the ID '0x0C'. This event is categorized with a 'CRITICAL' priority, indicating its high importance when it occurs. The 'Access' level is marked as 'V', which typically denotes that the event is visible or can be accessed for viewing. The 'Conformance' field is marked as 'O', meaning that the inclusion of this event is optional. There are no dependencies or conditions that mandate its implementation, so it is up to the implementer to decide whether to support this event in their device or system.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically identified by the ID '0x0D' and named 'GeneralFault'. This event is categorized with a priority level of 'INFO', indicating it is informational in nature. The access level is marked as 'V', which typically denotes visibility or read access. The conformance rule for this event is 'O', meaning that the 'GeneralFault' event is optional. It is not required for implementation and does not depend on any other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this event based on their specific use case or product requirements.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "Leakage" event, identified by the ID `0x0E`. This event has a priority level of "INFO," indicating it provides informational messages. The access level is denoted by "V," which typically means it is visible or can be accessed in some manner. The conformance rule for this event is marked as "O," meaning it is optional. This indicates that the implementation of the "Leakage" event is not required and can be included at the discretion of the device manufacturer or developer, without any dependencies or conditions that must be met.

* The table row describes an event within the Pump Configuration and Control Cluster, specifically the "AirDetection" event, identified by the ID '0x0F'. This event has a priority level of 'INFO', indicating it provides informational messages. The 'Access' field is marked as 'V', which typically denotes that the event is visible or can be accessed in some manner. The 'Conformance' field is marked as 'O', meaning that the "AirDetection" event is optional. This indicates that the implementation of this event is not required and there are no dependencies or conditions that mandate its inclusion in a device or system. Therefore, manufacturers can choose whether or not to support this event based on their specific product requirements or design choices.

_Table parsed from section 'Events':_

* The table row describes an event named "TurbineOperation" within the Pump Configuration and Control Cluster, identified by the ID '0x10'. This event has a priority level of 'INFO' and requires 'V' (view) access. The conformance rule for "TurbineOperation" is marked as 'O', indicating that this event is optional. This means that the implementation of this event is not required and has no dependencies on other features or conditions. Devices or systems implementing the Pump Configuration and Control Cluster can choose to support the "TurbineOperation" event, but it is not mandatory for compliance with the Matter specification.

