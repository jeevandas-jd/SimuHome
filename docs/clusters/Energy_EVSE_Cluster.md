
# 9.3 Energy EVSE Cluster

Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or
Plug-In Hybrid Electric Vehicle. This cluster provides an interface to the functionality of Electric
Vehicle Supply Equipment (EVSE) management.
Devices targeted by this cluster include Electric Vehicle Supply Equipment (EVSE). The cluster
generically assumes a signaling protocol (J1772 in NA and IEC61851 in Europe and Asia) between
the EVSE and Electric Vehicle (EV) that utilizes a pilot signal to manage the states of the charging
process. [SAE J2847/3_202311] version and IEC61841 define Pilot signal as a modulated DC voltage
on a single wire.
Power Line Communication (PLC) is supported by some EVSEs (e.g. for support of ISO 15118 in
Europe and SAE J2931/4 in NA) and may enable features such as Vehicle to Grid (V2G) or Vehicle to
Home (V2H) that allows for bi-directional charging/discharging of electric vehicles.
More modern EVSE devices may optionally support ISO 15118-20 in Europe and SAE J2836/3 for NA
to support bi-directional charging (Vehicle to Grid - V2G) and Plug and Charge capabilities.
This cluster definition assumes AC charging only. DC charging options may be added in future revi
sions of this cluster.
This cluster supports a safety mechanism that may lockout remote operation until the initial latch
ing conditions have been met. Some of the fault conditions defined in SAE J1772, such as Ground-
Fault Circuit Interrupter (GFCI) or Charging Circuit Interrupting Device (CCID), may require clear
ing by an operator by, for example, pressing a button on the equipment or breaker panel.
This EVSE cluster is written around support of a single EVSE. Having multiple EVSEs at home or a
business is managed by backend system and outside scope of this cluster.
Note that in many deployments the EVSE may be outside the home and may suffer from intermit
tent network connections (e.g. a weak WiFi signal). It also allows for a charging profile to be pre-
configured, in case there is a temporary communications loss during a charging session.

## Dependencies
The server side of this cluster SHALL depend on setting time from another device or using a real-
time clock.
This can either use a built-in real-time clock or non Matter time source, or can be derived using the
Time Synchronization cluster.
9.3.5.1. Diagnostic Event logs
It is quite common that users may experience issues charging their vehicle, which, without
logs to understand what happened, makes it very difficult to resolve the root cause.
Matter supports events (see Matter specification section 7.14) which includes a buffered log of
previous events including a Timestamp (see Matter specification 7.14.2.2).
This Timestamp can be the System Time (since boot) or Epoch Time. It is recommended to use
Epoch time (which can be set using the Time Synchronization cluster), which would allow
remote  support  operatives  to  retrieve  the  event  logs  and  analyze  them  against  a  user
reported actual time.

## Definitions
EVSE Session - An EVSE session starts when an EV is plugged in. It ends when it is unplugged.

## Data Types
9.3.7.1. TargetDayOfWeekBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element with the bit position '0' named 'Sunday'. This element is summarized simply as 'Sunday'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Sunday' element is always required to be implemented in any device or system that supports the Energy EVSE Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status; it must be included without exception.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element with the bit position '1', named 'Monday', which is summarized as 'Monday'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'Monday' data element is always required to be implemented in any device or application that conforms to this specification. There are no conditions or dependencies affecting its requirement; it must be included as part of the implementation.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element named "Tuesday," which is associated with bit position '2'. The summary also identifies it as "Tuesday." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Tuesday" element is always required to be implemented in any system or device that adheres to this specification. There are no conditions or dependencies affecting its requirement; it must be included as part of the implementation.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element named "Wednesday," which is represented by the bit position '3'. The summary also labels it as "Wednesday." The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Wednesday" data element is always required to be implemented in any system or device that adheres to this specification. There are no conditions or dependencies affecting its mandatory status, ensuring its consistent presence across implementations.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element with the bit position '4' named 'Thursday', which is summarized as 'Thursday'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Thursday' element is always required to be implemented in any device or system that supports the Energy EVSE Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status; it must be included without exception.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element with the bit position '5', named 'Friday', which is summarized simply as 'Friday'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'Friday' data element is always required to be implemented in any device or application that adheres to this specification. There are no conditions or dependencies affecting its mandatory status, making it a fundamental and non-negotiable part of the implementation.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data element labeled 'Saturday' associated with bit position '6'. The 'Summary' reiterates the name 'Saturday'. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'Saturday' element is a required component of the specification and must be implemented in all instances of this cluster without exception. There are no conditions or dependencies affecting its mandatory status, making it an essential part of the cluster's data structure.

9.3.7.2. StateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data type with the value '0' and the name 'NotPluggedIn'. This data type indicates that the electric vehicle (EV) is not currently plugged into the charging station. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'NotPluggedIn' data type is always required to be implemented in any system or device that supports the Energy EVSE Cluster, ensuring that this status can be consistently reported across all compliant implementations.

* The table row describes a data type within the Energy EVSE Cluster, specifically named "PluggedInNoDemand." This data type has a value of '1' and is summarized as indicating that an electric vehicle (EV) is plugged in but not currently demanding any current. The conformance rule for this data type is marked as 'M,' which stands for Mandatory. This means that the "PluggedInNoDemand" data type is always required to be implemented in any system or device that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, under the Data Types section, the entry for 'PluggedInDemand' with a value of '2' indicates a specific state where the electric vehicle (EV) is plugged in and requesting current, but the Electric Vehicle Supply Equipment (EVSE) is not permitting the current to flow. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'PluggedInDemand' state is a required element within the specification and must be implemented in all compliant devices or systems that utilize this cluster. There are no conditions or exceptions; it is an essential part of the functionality.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "PluggedInCharging" with a value of '3'. This element signifies that an electric vehicle (EV) is plugged in, charging is actively in progress, and current is flowing. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "PluggedInCharging" element is always required to be implemented in any system or device that adheres to this part of the Matter specification. There are no conditions or exceptions; it is a fundamental requirement for compliance.

* The table row describes a data type within the Energy EVSE Cluster, specifically named "PluggedInDischarging." This data type represents a state where an electric vehicle (EV) is plugged in, discharging is in progress, and current is flowing. The conformance rule for this data type is "V2X," which indicates that it is mandatory if the V2X feature is supported. In other words, if the system or device supports vehicle-to-everything (V2X) communication, this data type must be implemented. If V2X is not supported, the conformance rule does not apply, and the data type is not required.

* In the Energy EVSE Cluster, within the Data Types section, the entry for 'SessionEnding' with a value of '5' indicates a specific state where the Electric Vehicle Supply Equipment (EVSE) transitions from any plugged-in state to a NotPluggedIn state. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented according to the Matter specification. This ensures that any device or system adhering to this specification must support the 'SessionEnding' state transition to maintain compliance.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an entry with the name "Fault," which has a value of '6'. The summary indicates that this entry signifies the presence of a fault, as detailed by the FaultState attribute. The conformance rule for this entry is marked as 'M', which means it is mandatory. This implies that the "Fault" entry is a required element in the specification and must always be implemented in any device or system that adheres to this cluster's standards.

9.3.7.3. SupplyStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data entry with the value '0' and the name 'Disabled'. This entry indicates that the electric vehicle (EV) is not currently permitted to charge or discharge. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Disabled' state is a required element within the specification and must always be implemented in any system or device that adheres to the Matter specification for this cluster.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "ChargingEnabled" with a value of '1'. This element indicates whether an electric vehicle (EV) is currently permitted to charge. The conformance rule for "ChargingEnabled" is marked as 'M', which stands for Mandatory. This means that the "ChargingEnabled" element is always required to be implemented in any system or device that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row entry pertains to the "DischargingEnabled" data type within the Energy EVSE Cluster, specifically under the Data Types section. This entry indicates that the "DischargingEnabled" attribute signifies whether an electric vehicle (EV) is currently permitted to discharge energy. The conformance rule `[V2X]` implies that this attribute is optional and only applicable if the feature or condition represented by `V2X` is supported. In other words, the "DischargingEnabled" attribute is not mandatory by default but becomes relevant and can be included if the system or device supports the V2X feature, which typically refers to vehicle-to-everything communication capabilities.

* In the context of the Energy EVSE Cluster, under the Data Types section, the table row describes a data type named "DisabledError" with a value of '3'. This data type indicates that the electric vehicle (EV) is currently unable to charge or discharge due to an error, and the error must be resolved before normal operation can resume. The conformance rule for "DisabledError" is marked as 'M', which stands for Mandatory. This means that the "DisabledError" data type is always required to be implemented in any system or device that conforms to this specification, ensuring that the system can appropriately handle and communicate error states that prevent charging or discharging.

* In the context of the Energy EVSE Cluster, under the Data Types section, the table row describes an element named "DisabledDiagnostics" with a value of '4'. This element indicates that the electric vehicle (EV) is not currently permitted to charge or discharge because it is in a self-diagnostics mode. The conformance rule for "DisabledDiagnostics" is marked as 'M', which stands for Mandatory. This means that this element is always required to be implemented in any system or device that supports the Energy EVSE Cluster, ensuring that the functionality to recognize and handle the self-diagnostics mode is consistently available.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "Enabled" with a value of '5'. This element indicates that the electric vehicle (EV) is currently permitted to charge and discharge. The conformance rule for this element is specified as '[V2X]', which means that the "Enabled" element is optional if the V2X (Vehicle-to-Everything) feature is supported. If the V2X feature is not supported, the element is not required. This conditional optionality allows for flexibility in implementation depending on the presence of V2X capabilities.

9.3.7.4. FaultStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes a data type entry with the value '0' and the name 'NoError'. This entry indicates that the Electric Vehicle Supply Equipment (EVSE) is not experiencing any error state. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'NoError' data type is a required element in the specification and must always be implemented in any system or device that adheres to the Matter specification for this cluster.

* The table row describes a data type within the Energy EVSE Cluster, specifically named "MeterFailure." This data type has a value of '1' and is summarized as indicating that the Electric Vehicle Supply Equipment (EVSE) is unable to obtain electrical measurements. The conformance rule for "MeterFailure" is marked as 'M', which stands for Mandatory. This means that the "MeterFailure" data type is always required to be implemented in any system or device that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the Energy EVSE Cluster, under the Data Types section, the entry for 'OverVoltage' with a value of '2' indicates a condition where the EVSE (Electric Vehicle Supply Equipment) input voltage level is too high. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'OverVoltage' data type is a required element in the specification and must be implemented in all devices or systems that conform to this cluster. There are no conditions or exceptions; it is an essential component that must always be included.

* In the Energy EVSE Cluster, under the Data Types section, there is an entry with the name "UnderVoltage," which has a value of '3'. This entry indicates that the input voltage level for the Electric Vehicle Supply Equipment (EVSE) is too low. The conformance rule for this entry is marked as 'M', meaning it is mandatory. This implies that the "UnderVoltage" data type must always be implemented and supported in any device or system that conforms to this specification, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an entry with the name "OverCurrent" and a value of '4'. This entry summarizes a condition where the Electric Vehicle Supply Equipment (EVSE) detects a charging current that exceeds the limits allowed by the charger. According to the conformance rule 'M', this element is mandatory, meaning that it is always required to be implemented in any system or device that adheres to this specification. There are no conditions or exceptions; the detection and handling of an overcurrent situation must be supported.

* The table row entry pertains to the "Energy EVSE Cluster" within the "Data Types" section, specifically describing a data type named "ContactWetFailure." This data type is identified by the value '5' and is summarized as a condition where the Electric Vehicle Supply Equipment (EVSE) detects voltage on the charging pins while the contactor is open, indicating a potential fault. The conformance rule for "ContactWetFailure" is marked as 'M', which stands for Mandatory. This means that the inclusion of this data type is always required in implementations of the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "ContactDryFailure" with a value of '6'. This element signifies a condition where the Electric Vehicle Supply Equipment (EVSE) has detected an absence of voltage after the contactor has been enabled. The conformance rule for "ContactDryFailure" is marked as 'M', which stands for Mandatory. This means that the presence and implementation of this element are always required within the specified context of the Matter IoT specification, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, under the Data Types section, the table row describes an entry with the value '7' named 'GroundFault'. This entry indicates that the Electric Vehicle Supply Equipment (EVSE) is experiencing an unbalanced current supply, which is summarized as a 'GroundFault'. The conformance rule for this entry is 'M', meaning that the 'GroundFault' element is mandatory. It is always required to be implemented in any system or device that supports the Energy EVSE Cluster, ensuring that the system can detect and report unbalanced current supply conditions.

* In the context of the Energy EVSE Cluster, under the Data Types section, the table row describes an entry with the name "PowerLoss" and a value of '8'. This entry signifies that the Electric Vehicle Supply Equipment (EVSE) has detected a loss in power. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "PowerLoss" element is always required to be implemented in any device or system that adheres to this specification. There are no conditions or dependencies affecting its mandatory status, ensuring that the detection of power loss is a fundamental feature of the Energy EVSE Cluster.

* The table row entry pertains to the "PowerQuality" data type within the Energy EVSE Cluster, specifically under the Data Types section. The "PowerQuality" attribute, identified by the value '9', indicates that the Electric Vehicle Supply Equipment (EVSE) has detected a power quality issue, such as a phase imbalance. The conformance rule for this attribute is marked as 'M', which stands for Mandatory. This means that the "PowerQuality" attribute is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the Energy EVSE Cluster, under the Data Types section, the entry for 'PilotShortCircuit' with a value of '10' represents a specific condition where the EVSE pilot signal amplitude is short-circuited to ground. The conformance rule for this entry is marked as 'M', which means it is mandatory. This indicates that the 'PilotShortCircuit' element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the Energy EVSE Cluster, under the Data Types section, the entry for 'EmergencyStop' with a value of '11' indicates a data type that represents the event of an emergency stop button being pressed. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'EmergencyStop' data type is a required element in the implementation of the Energy EVSE Cluster. It must always be included and supported, ensuring that the system can recognize and respond to the pressing of an emergency stop button.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an entry with the value '12' named 'EVDisconnected'. This entry signifies that the Electric Vehicle Supply Equipment (EVSE) has detected that the cable has been disconnected. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'EVDisconnected' data type is always required to be implemented in any system or device that adheres to the Matter specification for this cluster. There are no conditions or exceptions; it is a fundamental requirement for compliance.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "WrongPowerSupply" with a value of '13'. This element indicates that the Electric Vehicle Supply Equipment (EVSE) could not determine the proper power supply level. The conformance rule for "WrongPowerSupply" is marked as 'M', which stands for Mandatory. This means that the "WrongPowerSupply" element is always required to be implemented in any system or device that conforms to this specification, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "LiveNeutralSwap" data type within the Energy EVSE Cluster, specifically under the Data Types section. This entry indicates that the EVSE (Electric Vehicle Supply Equipment) has detected a situation where the live and neutral wires are swapped. The conformance rule for this data type is marked as "M," which stands for Mandatory. This means that the "LiveNeutralSwap" data type is a required element in the implementation of the Energy EVSE Cluster, and it must always be included and supported according to the Matter specification.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an element named "OverTemperature" with a value of '15'. This element indicates that the internal temperature of the Electric Vehicle Supply Equipment (EVSE) is too high. The conformance rule for "OverTemperature" is marked as 'M', which stands for Mandatory. This means that the "OverTemperature" element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '255' and the 'Name' of 'Other', which is summarized as representing "Any other reason." The 'Conformance' for this entry is marked as 'M', indicating that this element is mandatory. This means that within the specification, the 'Other' data type with a value of '255' must always be implemented and supported in any system or device that adheres to the Energy EVSE Cluster specifications. There are no conditions or exceptions; it is a required element.

9.3.7.5. EnergyTransferStoppedReasonEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row pertains to the "Energy EVSE Cluster" within the "Data Types" section and describes a data type with the value '0' named "EVStopped." This data type signifies that the electric vehicle (EV) has decided to stop. The conformance rule for this entry is 'M,' which stands for Mandatory. This means that the "EVStopped" data type is always required in the implementation of the Energy EVSE Cluster, with no conditions or exceptions. It is a fundamental element that must be included to comply with the Matter specification for this cluster.

* The table row entry pertains to the "Energy EVSE Cluster" within the "Data Types" section and describes a data type named "EVSEStopped" with a value of '1'. The summary indicates that this data type represents a state where the Electric Vehicle Supply Equipment (EVSE) has decided to stop. The conformance rule for "EVSEStopped" is marked as 'M', meaning it is mandatory. This indicates that the "EVSEStopped" data type is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, specifically within the Data Types section, the table row describes an entry with the value '2' and the name 'Other', which is summarized as representing "an other unknown reason." The conformance rule for this entry is marked as 'M', indicating that it is a Mandatory element. This means that the 'Other' data type must always be included and supported in implementations of the Energy EVSE Cluster, without any conditions or exceptions.

9.3.7.6. ChargingTargetStruct Type
This represents a single user specified charging target for an EV.
An EVSE or EMS system optimizer may use this information to take the Time of Use Tariff, grid car
bon intensity, local generation (solar PV) into account to provide the cheapest and cleanest energy
to the EV.
The optimization strategy is not defined here, however in simple terms, the AddedEnergy require
ment can be fulfilled by knowing the charging Power (W) and the time needed to charge.
To compute the Charging Time: Required Energy (Wh) = Power (W) x ChargingTime (s) / 3600
Therefore: ChargingTime (s) = (3600 x RequiredEnergy (wH)) / Power (W)
To  compute  the  charging  time:  Charging  StartTime  =  TargetTimeMinutesPastMidnight  -
ChargingTime

_Table parsed from section 'Data Types':_

* The table row describes an attribute within the Energy EVSE Cluster, specifically under the Data Types section. The attribute is named "TargetTimeMinutesPastMidnight" and is of type `uint16`, which means it is a 16-bit unsigned integer. It has a constraint that limits its maximum value to 1439, representing the number of minutes in a day minus one. The default value for this attribute is set to 0. The conformance rule for this attribute is marked as "M," indicating that it is mandatory. This means that the "TargetTimeMinutesPastMidnight" attribute must always be implemented and supported in any device or application that uses the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically in the Data Types section. The element is identified by the ID '1' and is named 'TargetSoC', which stands for Target State of Charge. It is of the 'percent' type, with a default value of '0'. The conformance rule 'SOC, O.a+' indicates that the 'TargetSoC' element is mandatory if the feature 'SOC' (State of Charge) is supported. If 'SOC' is not supported, the element is optional, as denoted by 'O.a+'. This means that the element's inclusion is conditional based on the presence of the 'SOC' feature, and it defaults to optional if 'SOC' is not present.

_Table parsed from section 'Data Types':_

* The table row describes an attribute named "AddedEnergy" within the Energy EVSE Cluster, specifically under the Data Types section. This attribute is of type "energy- mWh" and has a constraint that its minimum value must be 0, with a default value of 0. The conformance rule for "AddedEnergy" is `[SOC], O.a`, which means that this attribute is optional if the feature `SOC` (State of Charge) is supported. If `SOC` is not supported, the attribute remains optional due to the `O.a` designation, which indicates a general optional status without additional conditions.

[SOC], O.a+
9.3.7.6.1. TargetTimeMinutesPastMidnight Field
This field SHALL indicate the desired charging completion time of the associated day. The time will
be represented by a 16 bits unsigned integer to designate the minutes since midnight. For example,
6am will be represented by 360 minutes since midnight and 11:30pm will be represented by 1410
minutes since midnight.
This field is based on local wall clock time. In case of Daylight Savings Time transition which may
result in an extra hour or one hour less in the day, the charging algorithm should take into account
the shift appropriately.
Note that if the TargetTimeMinutesPastMidnight values are too close together (e.g. 2 per day) these
may overlap. The EVSE may have to coalesce the charging targets into a single target. e.g. if the 1st
charging target cannot be met in the time available, the EVSE may be forced to begin working
towards the 2nd charging target and immediately continue until both targets have been satisfied
(or the vehicle becomes full).
The EVSE itself cannot predict the behavior of the vehicle (i.e. if it cannot obtain the SoC from the
vehicle), so should attempt to perform a sensible operation based on these targets. It is recom
mended that the charging schedule is pessimistic (i.e. starts earlier) since the vehicle may charge
more slowly than the electrical supply may provide power (especially if it is cold).
If the user configures large charging targets (e.g. high values of AddedEnergy or SoC) then it is
expected that the EVSE may need to begin charging immediately, and may not be able to guarantee
that the vehicle will be able to reach the target.
9.3.7.6.2. TargetSoC Field
This  field  represents  the  target  SoC  that  the  vehicle  should  be  charged  to  before  the  Target
TimeMinutesPastMidnight.
If the EVSE supports the SOC feature and can obtain the SoC of the vehicle:
• the TargetSoC field SHALL take precedence over the AddedEnergy field.
• the EVSE SHOULD charge to the TargetSoC and then stop the charging automatically when it
reaches that point.
• if the TargetSoC value is set to 100% then the EVSE SHOULD continue to charge the vehicle until
the vehicle decides to stop charging.
If the EVSE does not support the SOC feature or cannot obtain the SoC of the vehicle:
• the AddedEnergy field SHALL take precedence over the TargetSoC field, and if the EVSE does
not support the SOC feature then the TargetSoC field may only take the values null or 100%.
• if the AddedEnergy field has not been provided, the EVSE SHOULD assume the vehicle is empty
and charge until the vehicle stops demanding a charge.
9.3.7.6.3. AddedEnergy Field
This field represents the amount of energy that the user would like to have added to the vehicle
before the TargetTimeMinutesPastMidnight.
This represents a positive value in mWh that SHOULD be added during the session (i.e. if the vehi
cle charging is stopped and started several times, this equates to the total energy since the vehicle
has been plugged in).
The maximum value (500kWh) is much larger than most EV batteries on the market today. If the
client tries to set this value too high then the EVSE will need to start charging immediately and con
tinue charging until the vehicle stops demanding charge (i.e. it is full). Therefore the maximum
value should be set based on typical battery size of the vehicles on the market (e.g. 70000Wh), how
ever this is up to the client to carefully choose a value.
If the EVSE can obtain the Battery Capacity of the vehicle, it SHOULD NOT limit this
AddedEnergy value to the Battery Capacity of the vehicle, since the EV may also
NOTE
require energy for heating and cooling of the battery during charging, or for heat
ing or cooling the cabin.
9.3.7.7. ChargingTargetScheduleStruct Type
This represents a set of user specified charging targets for an EV for a set of specified days.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "DayOfWeekForSequence" within the Energy EVSE Cluster's Data Types section. This entry specifies that "DayOfWeekForSequence" is of the type "TargetDayOfWeekBitmap" and has a constraint labeled as "all," indicating that it applies universally without specific limitations. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "DayOfWeekForSequence" element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, with no conditions or exceptions.

* In the Energy EVSE Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'ChargingTargets'. This element is of the type 'list[ChargingTargetStruct]' and is constrained to a maximum of 10 entries. The conformance rule for 'ChargingTargets' is marked as 'M', which means it is mandatory. This indicates that the 'ChargingTargets' element is always required to be implemented in any device or application that conforms to this specification, without any conditions or exceptions.

9.3.7.8. DayOfWeekForSequence Field
This field SHALL indicate the days of the week that the charging targets SHOULD be associated to.
This field is a bitmap and therefore the associated targets could be applied to multiple days.
9.3.7.9. ChargingTargets Field
This field SHALL indicate a list of up to 10 charging targets for each of the associated days of the
week.

## Attributes

_Table parsed from section 'Attributes':_

* In the Energy EVSE Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0000' named 'State', which is of the type 'StateEnum'. The 'Constraint' is listed as 'all', indicating that this attribute applies universally within its context. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed in terms of quality considerations. The 'Access' is denoted as 'R V', suggesting that the attribute is readable and has volatile access characteristics. The 'Conformance' is specified as 'M', which means that this attribute is mandatory and always required to be implemented in any device or application that supports the Energy EVSE Cluster.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "SupplyState" attribute, which is identified by the ID '0x0001' and is of the type 'SupplyStateEnum'. This attribute is constrained to apply universally ('all') and has an access level of 'R V', indicating it is readable and possibly volatile. The conformance rule for this attribute is 'M', meaning it is mandatory. This implies that the "SupplyState" attribute must always be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "FaultState" attribute. This attribute has an ID of '0x0002' and is of the type 'FaultStateEnum'. It is constrained to 'all', meaning it applies universally within its context. The access level is 'R V', indicating that it is readable and possibly volatile, meaning its value can change frequently. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "FaultState" attribute is always required to be implemented in any device or application that supports the Energy EVSE Cluster, with no conditions or exceptions.

* The table row describes an attribute named "ChargingEnabledUntil" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute has an ID of '0x0003' and is of type 'epoch-s', indicating it represents a timestamp in seconds since the epoch. The 'Constraint' is 'all', suggesting it applies universally without specific limitations. The 'Quality' is marked as 'X N', which typically indicates certain quality characteristics or constraints, though further context would be needed for precise interpretation. The default value for this attribute is '0', and it has 'Access' permissions of 'R V', meaning it is readable and possibly volatile. The 'Conformance' is marked as 'M', which means this attribute is mandatory and must always be implemented in any device or application supporting the Energy EVSE Cluster.

* The table row describes an attribute named "DischargingEnabledUntil" within the Energy EVSE Cluster, specifically in the context of attributes. This attribute is identified by the ID '0x0004' and is of the type 'epoch-s', which likely represents a timestamp in seconds. The 'Constraint' is listed as 'all', indicating that there are no specific limitations on its values beyond those inherent to its type. The 'Quality' field is marked as 'X N', suggesting that this attribute is disallowed and not to be used in new implementations. The default value for this attribute is '0', and it has 'R V' access, meaning it is readable and possibly volatile. The 'Conformance' field is 'V2X', indicating that this attribute is mandatory if the V2X feature is supported. In summary, "DischargingEnabledUntil" is a timestamp attribute that is required when the V2X feature is present, but it is otherwise disallowed and should not

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "CircuitCapacity" attribute. This attribute is identified by the ID '0x0005' and is of the type 'amperage- mA', with a constraint that it must be at least 0. The quality is marked as 'N', indicating it is a numeric value, and it has a default value of 0. The access level is 'R V', meaning it is readable and has a volatile nature. The conformance for this attribute is marked as 'M', which means it is mandatory. This indicates that the "CircuitCapacity" attribute is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an attribute named "MinimumChargeCurrent" within the Energy EVSE Cluster, specifically in the context of attributes. This attribute is identified by the ID '0x0006' and is of the type 'amperage- mA', with a constraint that it must be at least 0. The quality is marked as 'N', indicating a specific quality characteristic, and it has a default value of 6000 mA. The access level is 'R V', meaning it is readable and possibly volatile. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the "MinimumChargeCurrent" attribute is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "MaximumChargeCurrent" attribute. This attribute has an ID of '0x0007' and is of the type 'amperage- mA', indicating it measures current in milliamperes. The attribute has a constraint that specifies a minimum value of 0, ensuring that the current cannot be negative. Its quality is marked as 'N', and it has a default value of 0. The access level is 'R V', meaning it is readable and has a volatile nature, possibly changing frequently. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "MaximumChargeCurrent" attribute is always required to be implemented in any device or application that supports the Energy EVSE Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "MaximumDischargeCurrent" attribute. This attribute is identified by the ID '0x0008' and is of the type 'amperage- mA', indicating it measures current in milliamperes. It has a constraint of 'min 0', meaning the value cannot be negative, and a default value of '0'. The quality is marked as 'N', and the access is 'R V', which typically means it is readable and possibly volatile. The conformance rule 'V2X' indicates that this attribute is mandatory if the V2X feature is supported. In other words, if the system supports V2X (Vehicle-to-Everything) communication, then the "MaximumDischargeCurrent" attribute must be implemented.

* In the Energy EVSE Cluster, within the Attributes section, the table row describes the attribute 'UserMaximumChargeCurrent' with an ID of '0x0009'. This attribute is of the type 'amperage- mA' and has a constraint described elsewhere in the documentation. It is marked with a quality of 'N', indicating it may have specific quality considerations, and has a default value of '0'. The access level is 'RW VM', meaning it is readable and writable with potential vendor-specific modifications. The conformance rule for this attribute is 'O', which means it is optional. This indicates that the implementation of the 'UserMaximumChargeCurrent' attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute named "RandomizationDelayWindow" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute has an ID of '0x000A' and is of type 'elapsed-s', with a constraint that its value cannot exceed 86400 seconds. The quality is marked as 'N', indicating a specific characteristic or requirement not detailed here, and it has a default value of 600 seconds. The access level is 'RW VM', meaning it can be read and written, and it may have volatile memory implications. The conformance rule for this attribute is 'O', which signifies that it is optional. This means that the implementation of this attribute is not required and has no dependencies on other features or conditions within the specification.

* The table row describes an attribute named "NextChargeStartTime" within the Energy EVSE Cluster, identified by the ID '0x0023'. This attribute is of type 'epoch-s', meaning it represents a time value in seconds since the epoch. It has a constraint of 'all', indicating it applies universally within its context. The quality is marked as 'X', meaning this attribute is explicitly disallowed in terms of quality. The default value is 'null', and it has read and volatile access permissions ('R V'). The conformance rule 'PREF' suggests that the attribute is provisionally required, with the expectation that it may become mandatory in the future. This means that while it is not currently mandatory, it is anticipated to be required in upcoming versions of the specification.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "NextChargeTargetTime" within the Energy EVSE Cluster, specifically in the Attributes section. This attribute has an ID of '0x0024' and is of type 'epoch-s', indicating it represents a time value in seconds since the epoch. The 'Constraint' is 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed in terms of quality considerations. The default value is 'null', and the access level is 'R V', which indicates it can be read and is volatile. The 'Conformance' field is labeled as 'PREF', which is not a standard conformance tag according to the provided guide. However, if interpreted as a provisional status, it suggests that the attribute's current status is temporary and may be subject to change in future specifications.

* The table row describes an attribute within the Energy EVSE Cluster, specifically named "NextChargeRequired Energy," identified by the ID '0x0025'. This attribute is of type 'energy-mWh' with a constraint that it must be at least 0. It has a quality designation of 'X', indicating it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read and volatile access ('R V'). The conformance rule 'PREF' suggests that the attribute is currently provisional, with an expectation that it might become mandatory in the future. This means that while it is not yet a required element, it is anticipated that it will be required in subsequent versions of the specification.

* The table row describes an attribute named "NextChargeTargetSoC" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute has an ID of '0x0026' and is of the 'percent' type. Its quality is marked as 'X', indicating that it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read and view access ('R V'). The conformance rule for "NextChargeTargetSoC" is 'PREF', which suggests that its status is provisional, with an expectation that it might become mandatory in the future. However, the current conformance status is not explicitly defined in the provided guide, indicating that further documentation might be necessary to fully understand its intended future status.

* The table row describes an attribute named "ApproximateEVEfficiency" within the Energy EVSE Cluster, identified by the ID '0x0027'. This attribute is of type 'uint16', and its constraints are described elsewhere in the documentation. The quality of this attribute is marked as 'X N', indicating it is disallowed in some contexts. The default value for this attribute is 'null', and it has read-write access with a viewable and modifiable quality ('RW VM'). The conformance rule '[PREF]' indicates that this attribute is optional if the feature 'PREF' is supported. In other words, the inclusion of this attribute is not mandatory but can be included if the 'PREF' condition is met, allowing for flexibility based on specific implementation needs.

* In the Energy EVSE Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0030' named 'StateOfCharge'. This attribute is of the 'percent' type, indicating it represents a percentage value. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed from having any quality-related features. The 'Default' value is 'null', suggesting there is no predefined default value for this attribute. The 'Access' is specified as 'R V', indicating that the attribute is readable ('R') and may have volatile ('V') characteristics, meaning its value can change frequently. The 'Conformance' is defined as 'SOC', which implies that the attribute is mandatory if the feature or condition represented by 'SOC' is supported. If 'SOC' is not supported, the attribute is not required.

* The table row describes an attribute named "BatteryCapacity" within the Energy EVSE Cluster, specifically in the context of Attributes. This attribute has an ID of '0x0031' and is of type 'energy- mWh', with a constraint that its value must be a minimum of 0. The quality of this attribute is marked as 'X', indicating it is explicitly disallowed. The default value for this attribute is 'null', and its access is defined as 'R V', meaning it is readable and volatile. The conformance rule 'SOC' implies that the attribute is mandatory if the feature 'SOC' (State of Charge) is supported. If 'SOC' is not supported, the attribute is not required.

* The table row describes an attribute named "VehicleID" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0032' and is of type 'string' with a maximum length constraint of 32 characters. The quality of this attribute is marked as 'X', indicating it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule 'PNC' suggests that the attribute is currently provisional, meaning its status is temporary and may change in future specifications. However, the rule does not specify a future intended conformance, leaving its eventual requirement status open to future updates.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "SessionID" attribute. This attribute has an ID of '0x0040' and is of type 'uint32', meaning it is a 32-bit unsigned integer. The 'Constraint' field indicates that this attribute applies universally ('all'), and the 'Quality' field marked as 'X N' suggests it is disallowed in certain contexts or configurations. The default value for this attribute is 'null', and it has 'R V' access, meaning it is readable and possibly volatile. The 'Conformance' field is marked as 'M', indicating that the 'SessionID' attribute is mandatory and must always be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an attribute named "SessionDuration" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute has an ID of '0x0041' and is of type 'elapsed-s', indicating it measures elapsed time in seconds. The constraint 'all' suggests it applies universally within its context. The quality indicators 'X N Q' provide additional, unspecified quality characteristics, while the default value is 'null', meaning it does not have a predefined initial value. The access permissions 'R V' indicate that this attribute is readable and possibly volatile. The conformance rule 'M' specifies that the "SessionDuration" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Energy EVSE Cluster, specifically the "SessionEnergyCharged" attribute. This attribute has an ID of '0x0042' and is of type 'energy- mWh', with a constraint that it must be a minimum of 0. The quality indicators are 'X N Q', and it has a default value of 'null'. The access level is 'R V', indicating it is readable and volatile. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "SessionEnergyCharged" attribute is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or dependencies.

* The table row describes an attribute named "SessionEnergyDischarged" within the Energy EVSE Cluster, specifically under the Attributes section. This attribute has an ID of '0x0043' and is of the type 'energy- mWh', with a constraint that it must be a minimum of 0. The quality indicators are 'X N Q', and it has a default value of 'null'. The access level is 'R V', indicating it is readable and volatile. The conformance rule 'V2X' specifies that this attribute is mandatory if the V2X feature is supported. In simpler terms, if the V2X feature is implemented in the device, the "SessionEnergyDischarged" attribute must be included; otherwise, it is not required.

9.3.8.1. State Attribute
This attribute SHALL indicate the current status of the EVSE. This higher-level status is partly
derived from the signaling protocol as communicated between the EVSE and the vehicle through
the pilot signal.
The State attribute SHALL change when the EVSE detects change of condition of the EV (plugged in
or unplugged, whether the vehicle is asking for demand or not, and if it is charging or discharging).
SessionEnding is not really a state but a transition. However, the transition period
NOTE
may take a few seconds and is useful for some clean up purposes.
The Fault state is used to indicate that the FaultState attribute is not NoError.
A null value SHALL indicate that the state cannot be determined.
9.3.8.2. SupplyState Attribute
This attribute SHALL indicate whether the EV is currently allowed to charge from or discharge to
the EVSE.
9.3.8.3. FaultState Attribute
This attribute SHALL indicate the type of fault detected by the EVSE (internally or as detected in the
pilot signal).
When the SupplyState attribute is DisabledError, the FaultState attribute will be one of the values
listed in FaultStateEnum, except NoError. For all values of SupplyState other than DisabledError,
the FaultState attribute SHALL be NoError.
9.3.8.4. ChargingEnabledUntil Attribute
This attribute SHALL indicate the time, in UTC, that the EVSE will automatically stop current flow to
the EV.
A null value indicates the EVSE is always enabled for charging.
A value in the past or 0x0 indicates that EVSE charging SHALL be disabled. The attribute is only set
via the payload of the EnableCharging command.
This attribute SHALL be persisted, for example a temporary power failure should not stop the vehi
cle from being charged.
9.3.8.5. DischargingEnabledUntil Attribute
This attribute SHALL indicate the time, in UTC, that the EVSE will automatically stop current flow
from the EV.
A null value indicates the EVSE is always enabled for discharging.
A value in the past or 0x0 indicates that EVSE discharging SHALL be disabled. The attribute is only
set via the payload of the EnableDischarging command.
This attribute SHALL be persisted, for example a temporary power failure should not stop the vehi
cle from being discharged.
9.3.8.6. CircuitCapacity Attribute
This attribute SHALL indicate the capacity that the circuit that the EVSE is connected to can pro
vide. It is intended to allow implementation of a self-managed network of EVSEs. It is assumed that
the device will allow the setting of such values by an installer.
9.3.8.7. MinimumChargeCurrent Attribute
This attribute SHALL indicate the minimum current that can be delivered by the EVSE to the EV.
The attribute can be set using the EnableCharging command.
9.3.8.8. MaximumChargeCurrent Attribute
This attribute SHALL indicate the maximum current that can be delivered by the EVSE to the EV.
This SHALL represent the actual maximum current offered to the EV at any time. Note that the EV
can draw less current than this value. For example, the EV may be limiting its power draw based on
the operating conditions of the battery, such as temperature and state of charge.
The attribute can be initially set using the EnableCharging command or by adjusting the UserMaxi
mumChargeCurrent attribute.
This attribute value SHALL be the minimum of:
• CircuitCapacity - Electrician’s installation setting
• CableAssemblyCurrentLimit (detected by the EVSE when the cable is plugged in)
• MaximumChargeCurrent field in the EnableCharging command
• UserMaximumChargeCurrent attribute
9.3.8.9. MaximumDischargeCurrent Attribute
This attribute SHALL indicate the maximum current that can be received by the EVSE from the EV.
This attribute can be set using the EnableDischarging command.
This attribute value SHALL be the minimum of:
• CircuitCapacity - Electrician’s installation setting
• CableAssemblyCurrentLimit (detected by the EVSE when the cable is plugged in)
• MaximumDischargeCurrent field in the EnableDischarging command
9.3.8.10. UserMaximumChargeCurrent Attribute
This attribute SHALL indicate a maximum current that can set by the consumer (e.g. via an app) as
a preference to further reduce the charging rate. This may be desirable if the home owner has a
solar PV or battery storage system which may only be able to deliver a limited amount of power.
The consumer can manually control how much they allow the EV to take.
This attribute value SHALL be limited by the EVSE to be in the range of:
MinimumChargeCurrent <= UserMaximumChargeCurrent <= MaximumChargeCurrent
where  MinimumChargeCurrent  and  MaximumChargeCurrent  are  the  values  received  in  the
EnableCharging command.
Its default value SHOULD be initialized to the same as the CircuitCapacity attribute. This value
SHALL be persisted across reboots to ensure it does not cause charging issues during temporary
power failures.
9.3.8.11. RandomizationDelayWindow Attribute
This attribute SHALL indicate the size of a random window over which the EVSE will randomize
the start of a charging session. This value is in seconds.
This is a feature that is mandated in some markets (such as UK) where the EVSE should by default
randomize its start time within the randomization window. By default in the UK this should be
600s.
For example, if the RandomizationDelayWindow is 600s (i.e. 10 minutes) and if there was a cheap
rate energy starting at 00:30, then the EVSE must compute a random delay between 0-599s and add
this to its initial planned start time.
9.3.8.12. NextChargeStartTime Attribute
This attribute SHALL indicate the time, in UTC, when the EVSE plans to start the next scheduled
charge based on the charging preferences.
A null value indicates that there is no scheduled charging (for example, the EVSE Mode is set to use
Manual mode tag), or that the vehicle is not plugged in with the SupplyState indicating that charg
ing is enabled.
9.3.8.13. NextChargeTargetTime Attribute
This attribute SHALL indicate the time, in UTC, when the EVSE SHOULD complete the next sched
uled charge based on the charging preferences.
A null value indicates that there is no scheduled charging (for example, the EVSE Mode is set to use
Manual mode tag), or that the vehicle is not plugged in with the SupplyState indicating that charg
ing is enabled.
9.3.8.14. NextChargeRequiredEnergy Attribute
This attribute SHALL indicate the amount of energy that the EVSE is going to attempt to add to the
vehicle in the next charging target.
A null value indicates that there is no scheduled charging (for example, the EVSE Mode is set to use
Manual mode tag), or that the vehicle is not plugged in with the SupplyState indicating that charg
ing is enabled, or that the next ChargingTargetStruct is using the TargetSoC value to charge the
vehicle.
9.3.8.15. NextChargeTargetSoC Attribute
This attribute SHALL indicate the target SoC the EVSE is going to attempt to reach when the vehicle
is next charged.
A null value indicates that there is no scheduled charging (for example, the EVSE Mode is set to use
Manual mode tag), or that the vehicle is not plugged in with the SupplyState indicating that charg
ing is enabled, or that the next ChargingTargetStruct is using the AddedEnergy value to charge the
vehicle.
If the SOC feature is not supported, only the values null and 100% are supported.
9.3.8.16. ApproximateEVEfficiency Attribute
This attribute SHALL indicate the vehicle efficiency rating for a connected vehicle.
This can be used to help indicate to the user approximately how many miles or km of range will be
added. It allows user interfaces to display to the user simpler terms that they can relate to com
pared to kWh.
This is value is stored in km per kWh multiplied by a scaling factor of 1000.
A  null  value  indicates  that  the  EV  efficiency  is  unknown  and  the  NextChargeRequiredEnergy
attribute cannot be converted from Wh to miles or km.
To convert from Wh into Range:
AddedRange (km)    = AddedEnergy (Wh) x ApproxEVEfficiency (km/kWh x 1000)
AddedRange (Miles) = AddedEnergy (Wh) x ApproxEVEfficiency (km/kWh x 1000) x
0.6213
Example:
ApproxEVEfficiency (km/kWh x 1000): 4800 (i.e. 4.8km/kWh x 1000)
AddedEnergy (Wh): 10,000
AddedRange (km)    = 10,000 x 4800 / 1,000,000 = 48 km
AddedRange (Miles) = AddedEnergy (Wh) x ApproxEVEfficiency (km/kWh x 1000) x
0.6213
= 29.82 Miles
9.3.8.17. StateOfCharge Attribute
This attribute SHALL indicate the state of charge of the EV battery in steps of 1%. The values are in
the 0-100%. This attribute is only available on EVSEs which can read the state of charge from the
SOC
vehicle and that support the   feature. If the StateOfCharge cannot be read from the vehicle it
SHALL be returned with a NULL value.
9.3.8.18. BatteryCapacity Attribute
This attribute SHALL indicate the capacity of the EV battery in mWh. This value is always positive.
9.3.8.19. VehicleID Attribute
PNC
This attribute SHALL indicate the vehicle ID read by the EVSE via ISO-15118 using the   feature, if
the EVSE supports this capability.
The field may be based on the e-Mobility Account Identifier (EMAID).
A null value SHALL indicate that this is unknown.
9.3.8.20. Session Attributes
The following set of attributes provides information about a charging session, defined as the period
from the EVSE detecting an EV plug-in to when it is unplugged.
the session attributes hold their values from the previous session and are reset
NOTE
when the next plug-in event happens.
Whenever the State leaves the NotPluggedIn state and moves to any ‘Plugged’ state (see the State
attribute), the SessionID attribute SHALL be incremented. The SessionDuration, SessionEnergy
Charged and SessionEnergyDischarged attributes SHALL be reset to zero.
9.3.8.20.1. SessionID Attribute
This attribute SHALL indicate a unique identifier for the current or last session. A value of null indi
cates no sessions have occurred. The SessionID SHALL be incremented each time a plugin is
detected. A session begins when the vehicle is plugged in and ends when the vehicle is unplugged.
SessionIDs are allowed to roll over, although the range of SessionID is a large number and it is
unlikely that the EVSE will have this many sessions in its lifetime unless there is a electrical fault
causes sessions to be detected at a rapid rate.
If there is no session in progress, the Session ID attribute will remain at the value for the last ses
sion.
9.3.8.20.2. SessionDuration Attribute
This attribute SHALL indicate the duration in seconds for the current or last charging session. A
default value of null indicates no sessions have occurred. A charge session begins when the vehicle
is plugged in and ends when the vehicle is unplugged.
The SessionDuration can be calculated from the start time of the session. Manufacturers SHALL
ensure this can be correctly calculated if there has been an power failure or reboot since the start
of the session.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once every 10 seconds on changes, or
• When it changes from null to any other value and vice versa, such as at the beginning and end
of a charging session.
9.3.8.20.3. SessionEnergyCharged Attribute
This attribute SHALL indicate the energy, in mWh, delivered by the EVSE to the EV for the current
or last charging session. A default value of null indicates no sessions have occurred.
The SessionEnergyCharged value can be calculated by knowing the initial value of the energy meter
at the start time of the session. Manufacturers SHALL ensure this can be correctly calculated if
there has been an power failure or reboot since the start of the session.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once every 10 seconds on changes, or
• When it changes from null to any other value and vice versa, such as at the beginning and end
of a charging session.
9.3.8.20.4. SessionEnergyDischarged Attribute
This attribute SHALL indicate the energy, in mWh, received by the EVSE from the EV for the current
or last charging session. A default value of null indicates no sessions have occurred.
The SessionEnergyDischarged value can be calculated by knowing the initial value of the energy
meter at the start time of the session. Manufacturers SHALL ensure this can be correctly calculated
if there has been an power failure or reboot since the start of the session.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once every 10 seconds on changes, or
• When it changes from null to any other value and vice versa, such as at the beginning and end
of a charging session.

## Commands

_Table parsed from section 'Commands':_

* In the context of the Energy EVSE Cluster, the command with ID '0x01' is named 'Disable' and is directed from the client to the server, with a response expected ('Y'). The access level is marked as 'O T', indicating specific access permissions or roles, though these are not detailed here. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the 'Disable' command must always be implemented and supported in any device or application that conforms to the Matter specification for this cluster, without any conditions or exceptions.

* The table row describes a command within the Energy EVSE Cluster, specifically the "EnableCharging" command, which is directed from the client to the server. The command has an ID of '0x02' and requires a response ('Y'). The access level is marked as 'O T', indicating it is optional and possibly tied to certain conditions or features. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "EnableCharging" command must always be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes a command within the Energy EVSE Cluster, specifically the "EnableDischarging" command, which is directed from the client to the server and requires a response. The access level is marked as "O T," indicating it is optional and may have specific access conditions. The conformance rule "V2X" implies that this command is mandatory if the V2X feature (Vehicle-to-Everything communication) is supported. In other words, if a device supports V2X, it must implement the "EnableDischarging" command; otherwise, the command is not required.

* In the Energy EVSE Cluster, within the Commands section, the table row describes the command 'StartDiagnostics' with an ID of '0x04'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level is specified as 'O T', which typically denotes optional access with certain conditions or roles, though further context would be needed for precise interpretation. The conformance rule for 'StartDiagnostics' is marked as 'O', meaning this command is optional. It is not required for implementation and does not have any dependencies or conditions that would alter its optional status.

* The table row describes a command within the Energy EVSE Cluster, specifically the "SetTargets" command, which is identified by the ID `0x05`. This command is directed from the client to the server and requires a response (`Response: Y`). The access level is marked as `O T`, indicating it is optional and may require specific conditions or roles for access. The conformance for this command is labeled as `PREF`, which is not a standard conformance tag according to the provided guide. However, it suggests a provisional status with a potential future requirement or preference. In this context, it implies that the "SetTargets" command is currently in a provisional state, possibly indicating that its mandatory status or specific conditions for its use are still under consideration or development.

* The table row describes a command within the Energy EVSE Cluster, specifically the "GetTargets" command, which is directed from the client to the server and expects a "GetTargetsResponse" in return. The access level is marked as "O T," indicating it is optional and possibly tied to a specific access level or feature. The conformance for this command is labeled as "PREF," which, according to the conformance interpretation guide, suggests that the command is currently in a provisional state. This means that its status is temporary and subject to change, potentially becoming mandatory or optional in future revisions of the specification. The exact future status is not specified in this entry, so further documentation would be needed to understand its intended evolution.

* The table row describes a command named "ClearTargets" within the Energy EVSE Cluster, specifically in the context of commands directed from a client to a server. The command has an ID of '0x07' and requires a response ('Y'). The access level is marked as 'O T', which typically indicates optional access with some specific conditions or roles (though further context would be needed for precise interpretation). The conformance for this command is labeled as 'PREF', which, based on the provided guide, suggests a provisional status. This means that the command is currently in a temporary state and may be subject to change, potentially becoming mandatory or optional in future revisions of the specification. The exact future status is not specified in the provided conformance string, indicating that further documentation may be needed to understand its intended evolution.

* The table row describes a command within the Energy EVSE Cluster, specifically the "GetTargetsResponse" command, which is directed from the server to the client. The 'Response' field indicates that this command does not require a response. The 'Conformance' field is marked as 'PREF', which is not directly defined in the provided conformance interpretation guide. However, it suggests a provisional status with a potential future requirement or preference that is not explicitly detailed in the guide. This implies that the command is currently in a state of transition or consideration for future mandatory or preferred status, but further documentation would be needed to clarify its exact conformance implications.

9.3.9.1. Disable Command
Allows a client to disable the EVSE from charging and discharging.
9.3.9.1.1. Effect on Receipt
On receipt of this command, the EVSE will stop any power flow between the EV and EVSE.
If the command cannot be handled, a status of FAILURE SHALL be returned.
If the SupplyState attribute is already Disabled, a response with status of SUCCESS SHALL be
returned.
Otherwise, if successful, the ChargingEnabledUntil and DischargingEnabledUntil attributes SHALL
be set to 0x0, the SupplyState attribute changed to Disabled, and a response with status of SUCCESS
SHALL be returned.
If any energy was being transferred, then a corresponding EnergyTransferStopped event SHALL be
generated.
9.3.9.2. EnableCharging Command
This command allows a client to enable the EVSE to charge an EV, and to provide or update the
maximum and minimum charge current.

_Table parsed from section 'Commands':_

* The table row describes a command named "ChargingEnabledUntil" within the Energy EVSE Cluster, specifically under the Commands section. This command has an ID of '0' and is of the type 'epoch-s', which likely refers to a timestamp format. The 'Constraint' is listed as 'all', suggesting that this command applies universally within its context. The 'Quality' is marked as 'X', indicating that this command is explicitly disallowed in terms of quality considerations. The 'Default' value is 'null', meaning there is no predefined default value for this command. The 'Conformance' is marked as 'M', which means that the "ChargingEnabledUntil" command is mandatory and always required to be implemented within the Energy EVSE Cluster, regardless of any other conditions or features.

* In the context of the Energy EVSE Cluster, specifically within the Commands section, the table row describes a command identified by ID '1' named 'MinimumChargeCurrent'. This command is of the type 'amperage- mA' and has a constraint that specifies a minimum value of 0 milliamperes. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the 'MinimumChargeCurrent' command is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the Energy EVSE Cluster, under the Commands section, the table row describes a command identified as 'MaximumChargeCurrent' with an ID of '2'. This command is of the type 'amperage- mA' and has a constraint specifying a minimum value of 0. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the 'MaximumChargeCurrent' command is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

9.3.9.2.1. ChargingEnabledUntil Field
This field SHALL indicate the expiry time, in UTC, when charging will be automatically disabled.
A value in the past in this field SHALL disable the EVSE charging whereas a null value SHALL
enable it permanently.
9.3.9.2.2. MinimumChargeCurrent Field
This field SHALL indicate the minimum current that can be delivered by the EVSE to the EV in
trickle mode. The EVSE current limit can be advertised to an EV in 0.6A steps.
The value of the MinimumChargeCurrent attribute SHALL be set to the value of this field (see Mini
mumChargeCurrent attribute for further details).
9.3.9.2.3. MaximumChargeCurrent Field
This field SHALL indicate the maximum current that can be delivered by the EVSE to the EV. The
EVSE current limit can be advertised to an EV in 0.6A steps.
The value of the this field SHALL be stored by the EVSE to determine the value of MaximumCharge
Current attribute. For example, if the UserMaximumChargeCurrent attribute is adjusted below then
this value, and then later adjusted above this value, the resulting MaximumChargeCurrent attribute
will be limited to this value.
9.3.9.2.4. Effect on Receipt
On receipt of this command, this SHALL allow the EVSE to charge the EV until the specified time
stamp within the current limits specified in the fields of the command.
If there is currently an error present on the EVSE, or Diagnostics are currently active, then the com
mand SHALL be ignored and a response with a status of FAILURE SHALL be returned.
If successful, the SupplyState attribute SHALL be set to ChargingEnabled (if previously Disabled) or
Enabled (if previously DischargingEnabled), and a response with status of SUCCESS SHALL be
returned.
The timestamp indicated in the ChargingEnabledUntil attribute SHALL be updated to the time
stamp of the ChargingEnabledUntil field if the command is successful.
If the ChargingEnabledUntil is null (i.e. should be permanently enabled), then the EVSE should
enable charging indefinitely.
If the ChargingEnabledUntil time is not null, then when this time expires then the EVSE SHALL stop
charging and SHALL update the State attribute to indicate it is no longer charging, and SHALL
update the SupplyState attribute to Disabled (if DischargingEnabledUntil is also in the past) or Dis
chargingEnabled (if DischargingEnabledUntil is in the future or null).
9.3.9.3. EnableDischarging Command
Upon receipt, this SHALL allow a client to enable the discharge of an EV, and to provide or update
the maximum discharge current.

_Table parsed from section 'Commands':_

* The table row describes a command named "DischargingEnabledUntil" within the Energy EVSE Cluster, specifically under the Commands section. This command is identified by the ID '0' and is of the type 'epoch-s', which likely refers to a timestamp format. The constraint 'all' suggests that this command applies universally within its context. The quality is marked as 'X', indicating that this command is explicitly disallowed in terms of quality considerations. The default value for this command is 'null', meaning it does not have a predefined default state. The conformance rule is 'M', which means that the "DischargingEnabledUntil" command is mandatory and must always be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, specifically within the Commands section, the table row describes a command identified as "MaximumDischargeCurrent" with an ID of '1'. This command pertains to the type 'amperage- mA' and is constrained to a minimum value of 0, indicating that the discharge current cannot be negative. The conformance rule for this command is marked as 'M', which means it is Mandatory. This implies that the "MaximumDischargeCurrent" command is an essential requirement for any implementation of the Energy EVSE Cluster, and it must always be supported and implemented without exception.

9.3.9.3.1. DischargingEnabledUntil Field
This field SHALL indicate the expiry time, in UTC, when discharging will be automatically disabled.
A value in the past in this field SHALL disable the EVSE discharging whereas a null value SHALL
enable EVSE discharging permanently.
9.3.9.3.2. MaximumDischargeCurrent Field
This field SHALL indicate the maximum current that can be received by the EVSE from the EV. The
EVSE current limit can be advertised to an EV in 0.6A steps. The value of the MaximumDischarge
Current attribute SHALL be stored and persisted across reboots by the EVSE to the value of this
field.
9.3.9.3.3. Effect on Receipt
On receipt of this command, this SHALL allow the EVSE to discharge the EV until the specified time
stamp, and allows a maximum current limit to be specified in the fields of the command.
If there is currently an error present on the EVSE, or Diagnostics are currently active, then the com
mand SHALL be ignored and a response with a status of FAILURE SHALL be returned.
If successful, the SupplyState attribute SHALL be set to DischargingEnabled (if previously Disabled)
or Enabled (if previously ChargingEnabled), and a response with status of SUCCESS SHALL be
returned.
The timestamp indicated in the DischargingEnabledUntil attribute SHALL be updated to the time
stamp of the DischargingEnabledUntil field if the command is successful.
If the DischargingEnabledUntil is null (i.e. should be permanently enabled), then the EVSE should
enable discharging indefinitely.
If the DischargingEnabledUntil time is not null, then when this time expires then the EVSE SHALL
stop discharging and SHALL update the State attribute to indicate it is no longer discharging, and
SHALL update the SupplyState attribute to Disabled (if ChargingEnabledUntil is also in the past) or
ChargingEnabled (if ChargingEnabledUntil is in the future or null).
9.3.9.4. StartDiagnostics Command
Allows a client to put the EVSE into a self-diagnostics mode.
9.3.9.4.1. Effect on Receipt
On receipt of this command, the EVSE SHALL enter a Diagnostics state only if the SupplyState
attribute is in the Disabled state.
If the EVSE cannot start diagnostics, a response SHALL be generated with a status of FAILURE.
If successful, the SupplyState attribute SHALL be set to DisabledDiagnostics, and a response with
status of SUCCESS SHALL be returned.
The diagnostics are at the discretion of the manufacturer and usually include internal checks. Upon
completion of the diagnostics, the EVSE SHALL restore SupplyState to the Disabled state (see Sup
plyState attribute for further details).
9.3.9.5. SetTargets Command
Allows a client to set the user specified charging targets.

_Table parsed from section 'Commands':_

* In the Energy EVSE Cluster, within the Commands section, the table row describes a command named "ChargingTargetSchedules" with an ID of '0'. This command is of the type 'list[ChargingTargetScheduleStruct]' and is constrained to a maximum of 7 entries. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "ChargingTargetSchedules" command is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

9.3.9.5.1. ChargingTargetSchedules Field
This field SHALL indicate a list of up to 7 sets of daily charging targets together with their associ
ated days of the week. Each of the days of the week may only be included in a single ChargingTar
getSchedule within this list field.
9.3.9.5.2. Effect on Receipt
On receipt of this command, the EVSE SHALL validate that all of the charging targets are within a
valid range, and that each day of the week is included in at most one of the ChargingTargetSched
ule, if they are not then the response SHALL be CONSTRAINT_ERROR.
When a command is received that requires a total number of charging targets greater than the
device supports, the status of the response SHALL be RESOURCE_EXHAUSTED.
If the charging targets are accepted, then the charging targets SHALL be stored for all of days that
are set in the DayOfWeekForSequence bitmap fields in all the ChargingTargetSchedules. If a Charg
ingTargetSchedule is defined with no ChargingTargets then the ChargingTargets are cleared for
those days defined in the DayOfWeekForSequence
The SetTargets command is used to update the EVSE’s weekly charging schedule. If the EVSE
already has some stored weekly charging targets, then it SHALL replace each daily charging target
as it receives the updates from the client. For example, if the EVSE has 2 charging targets for every
day of the week and is sent a SetTargets command with one target for Saturday then the EVSE
SHALL remove both charging targets for Saturday and replace those with the updated charging tar
get but leave all other days unchanged.
the EVSE may not be able to compute the schedules by itself, or may rely upon an
NOTE
EMS or other optimizer to do this.
In a standalone mode (e.g. without using a ToU tariff from the Pricing Cluster) the EVSE should be
able  to  compute  the  latest  NextChargeStartTime  based  on  the  preset  MaximumChargeCurrent
attribute and local grid voltage to determine the charging duration required. It should automati
cally begin charging and following the charging schedule if the EVSE is plugged in (and the EVSE is
enabled for charging).
PFR
If the EVSE supports the   (PowerForecastReporting) feature in the Device Energy Management
cluster, it SHALL auto update the Forecast with the indicative power forecast.
FA
If the EVSE supports the   (ForecastAdjustment) feature in the Device Energy Management cluster,
it SHALL indicate its adjustment capability in each of the Forecast slots (see Device Energy Manage
ment Cluster for more details).
The EVSE SHALL be responsible for updating the NextChargeEndTime, NextChargeRequiredEnergy
and/or NextChargeTargetSoC attributes as it runs through its internal schedule. For example, as a
scheduled charging session is completed or as it transitions to the next day, it should compute the
next time it expects to start charging, and then update the corresponding attributes accordingly.
9.3.9.6. GetTargets Command
Allows a client to retrieve the current set of charging targets.
9.3.9.6.1. Effect on Receipt
On receipt of this command, the EVSE SHALL send the GetTargetsResponse command to the client.
9.3.9.7. GetTargetsResponse Command
The GetTargetsResponse is sent in response to the GetTargets Command.

_Table parsed from section 'Commands':_

* In the Energy EVSE Cluster, within the Commands section, the table row describes a command named "ChargingTargetSchedules" with an ID of '0'. This command is of the type 'list[ChargingTargetScheduleStruct]' and is constrained to a maximum of 7 entries. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the "ChargingTargetSchedules" command must always be implemented and supported in any device or system that conforms to this specification, without any conditions or exceptions.

9.3.9.7.1. ChargingTargetSchedules Field
This field SHALL indicate a list of up to 7 sets of daily charging targets together with their associ
ated days of the week.
9.3.9.8. ClearTargets Command
Allows a client to clear all stored charging targets.
9.3.9.8.1. Effect on Receipt
On receipt of this command, all weekly targets that are currently stored SHALL be cleared and a
default response of SUCCESS SHALL be sent in response. There are no error responses to this com
mand.
If the EVSE is currently charging based on being in automatic mode, then it SHALL stop the EVSE
charging.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Energy EVSE Cluster, specifically the "EVConnected" event. This event is identified by the ID '0x00' and has a priority level of 'INFO', indicating it provides informational messages. The access level is marked as 'V', which typically denotes visibility or access permissions related to the event. The conformance rule for this event is 'M', meaning it is mandatory. This implies that the "EVConnected" event must always be implemented and supported within the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an event within the Energy EVSE (Electric Vehicle Supply Equipment) Cluster, specifically the "EVNotDetected" event. This event has an ID of '0x01' and is categorized with a priority level of 'INFO', indicating it provides informational messages. The 'Access' field is marked as 'V', which typically denotes visibility or access level, though the specific meaning would depend on the broader context of the specification. The 'Conformance' field is marked with 'M', which stands for Mandatory. This means that the "EVNotDetected" event is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row entry pertains to the "EnergyTransferStarted" event within the Energy EVSE Cluster, specifically under the Events section. This event is identified by the ID '0x02' and is categorized with a priority level of 'INFO', indicating it provides informational updates. The access level is marked as 'V', suggesting it is visible or accessible in some capacity. The conformance rule for this event is denoted by 'M', which stands for Mandatory. This means that the "EnergyTransferStarted" event is a required component of the Energy EVSE Cluster and must be implemented in all instances where this cluster is supported, without any conditions or exceptions.

* The table row entry pertains to the "EnergyTransferStopped" event within the Energy EVSE Cluster, specifically under the Events section. This event is identified by the ID '0x03' and is categorized with a priority level of 'INFO', indicating it provides informational updates. The 'Access' field is marked as 'V', which typically denotes visibility or access level, though the specific meaning would depend on the broader context of the specification. The 'Conformance' field is marked as 'M', which means that the "EnergyTransferStopped" event is mandatory. This implies that any implementation of the Energy EVSE Cluster must include this event as a required feature, ensuring that it is always supported and available in compliant devices or systems.

* The table row describes an event within the Energy EVSE Cluster, specifically the "Fault" event, which is identified by the ID '0x04'. This event is categorized with a "CRITICAL" priority, indicating its high importance in the system. The "Access" field is marked as 'V', suggesting that this event is viewable. The conformance rule for this event is 'M', which stands for Mandatory. This means that the "Fault" event is a required element in the Energy EVSE Cluster and must be implemented in any system or device that supports this cluster, without any conditions or exceptions.

* In the Energy EVSE Cluster, under the Events section, the table row describes an event with the ID '0x05' named 'RFID'. This event has an informational priority and is accessible with a 'V' access level. The conformance rule '[RFID]' indicates that the RFID event is optional if the RFID feature is supported. This means that the inclusion of the RFID event is not mandatory but can be implemented if the RFID feature is present in the system. If the RFID feature is not supported, the event does not need to be included.

9.3.10.1. EVConnected Event
This event SHALL be generated when the EV is plugged in.

_Table parsed from section 'Events':_

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '0' and is named 'SessionID', with a data type of 'uint32'. The constraint 'all' indicates that this element applies universally within its context. The conformance rule 'M' signifies that the 'SessionID' is a mandatory element, meaning it is always required to be implemented in any device or system that supports the Energy EVSE Cluster. There are no conditions or dependencies affecting its mandatory status; it must be present in all instances.

9.3.10.1.1. SessionID Field
This is the new session ID created after the vehicle is plugged in.
9.3.10.2. EVNotDetected Event
This event SHALL be generated when the EV is unplugged or not detected (having been previously
plugged in). When the vehicle is unplugged then the session is ended.

_Table parsed from section 'Events':_

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '0' and is named 'SessionID'. It is of type 'uint32', meaning it is a 32-bit unsigned integer, and it has a constraint labeled 'all', indicating it applies universally within its context. The conformance rule for 'SessionID' is 'M', which stands for Mandatory. This means that the 'SessionID' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '1' and is named 'State'. It is of the type 'StateEnum' and has a constraint labeled as 'all', indicating that it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'State' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '2' and is named 'SessionDuration'. It is of the type 'elapsed-s', which likely indicates that it measures elapsed time in seconds. The constraint 'all' suggests that this element applies universally within its context. The conformance rule for 'SessionDuration' is marked as 'M', meaning it is mandatory. This indicates that the 'SessionDuration' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row entry pertains to the "SessionEnergyCharged" event within the Energy EVSE Cluster, specifically under the Events section. This event is identified by the ID '3' and is of the type 'energy-mWh', with a constraint that the value must be a minimum of 0. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "SessionEnergyCharged" event is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '4' and is named 'SessionEnergyDischarged'. It is of the type 'energy-mWh', which measures energy in milli-watt hours, and it has a constraint that specifies a minimum value of 0, indicating that the energy discharged cannot be negative. The conformance rule for this element is 'V2X', which implies that the element is mandatory if the feature or condition represented by 'V2X' is supported. In this context, 'V2X' likely refers to a specific feature or capability related to vehicle-to-everything communication, and the presence of this feature necessitates the inclusion of the 'SessionEnergyDischarged' element.

9.3.10.2.1. SessionID Field
This field SHALL indicate the current value of the SessionID attribute.
9.3.10.2.2. State Field
This field SHALL indicate the value of the State attribute prior to the EV not being detected.
9.3.10.2.3. SessionDuration Field
This field SHALL indicate the total duration of the session, from the start of the session when the EV
was plugged in, until it was unplugged.
9.3.10.2.4. SessionEnergyCharged Field
This field SHALL indicate the total amount of energy transferred from the EVSE to the EV during
the session.
Note that if bi-directional charging occurs during the session, then this value SHALL only include
the sum of energy transferred from the EVSE to the EV, and SHALL NOT be a net value of charging
and discharging energy.
9.3.10.2.5. SessionEnergyDischarged Field
This field SHALL indicate the total amount of energy transferred from the EV to the EVSE during
the session.
Note that if bi-directional discharging occurs during the session, then this value SHALL only include
the sum of energy transferred from the EV to the EVSE, and SHALL NOT be a net value of charging
and discharging energy.
9.3.10.3. EnergyTransferStarted Event
This event SHALL be generated whenever the EV starts charging or discharging, except when an EV
has switched between charging and discharging under the control of the PowerAdjustment feature
of the Device Energy Management cluster of the associated Device Energy Management device.

_Table parsed from section 'Events':_

* In the Energy EVSE Cluster, within the context of Events, the table row describes an element with the ID '0' named 'SessionID', which is of type 'uint32' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that 'SessionID' is a Mandatory element. This means that the 'SessionID' must always be included and supported in any implementation of the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, within the Events section, the table row describes an element with the ID '1' and the name 'State', which is of the type 'StateEnum' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'State' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster. There are no conditions or dependencies that alter this requirement; it is an essential component that must be present in all relevant implementations.

* In the Energy EVSE Cluster, under the Events section, the table row describes an element with the ID '2' named 'MaximumCurrent'. This element is of the type 'amperage- mA' and has a constraint specifying a minimum value of 0. The conformance rule for 'MaximumCurrent' is 'M', which means it is a Mandatory element. This indicates that the 'MaximumCurrent' attribute must always be implemented and supported in any device or system that adheres to this specification, without any conditions or exceptions.

* The table row entry describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '3' and is named 'MaximumDischargeCurrent'. It is of the type 'amperage- mA', with a constraint indicating that its minimum value is 0. The conformance rule for this element is 'V2X', which means that the 'MaximumDischargeCurrent' is mandatory if the V2X feature is supported. If the V2X feature is not supported, the element is not required. This conformance rule ensures that the element is included in implementations where V2X capabilities are present, reflecting its relevance in such contexts.

9.3.10.3.1. SessionID Field
This field SHALL indicate the value of the SessionID attribute at the time the event was generated.
9.3.10.3.2. State Field
This field SHALL indicate the value of the State attribute at the time the event was generated.
9.3.10.3.3. MaximumCurrent Field
This field SHALL indicate the value of the maximum charging current at the time the event was
generated.
A non-zero value indicates that the EV has been enabled for charging and the value is taken directly
from  the  MaximumChargeCurrent  attribute.  A  zero  value  indicates  that  the  EV  has  not  been
enabled for charging.
9.3.10.3.4. MaximumDischargeCurrent Field
This field SHALL indicate the value of the maximum discharging current at the time the event was
generated.
A non-zero value indicates that the EV has been enabled for discharging and the value is taken
directly from the MaximumDischargeCurrent attribute. A zero value indicates that the EV has not
been enabled for discharging.
9.3.10.4. EnergyTransferStopped Event
This event SHALL be generated whenever the EV stops charging or discharging, except when an EV
has switched between charging and discharging under the control of the PowerAdjustment feature
of the Device Energy Management cluster of the associated Device Energy Management device.

_Table parsed from section 'Events':_

* The table row describes an element within the Energy EVSE Cluster, specifically under the Events section. The element is identified by the ID '0' and is named 'SessionID'. It is of the data type 'uint32', which indicates it is a 32-bit unsigned integer. The 'Constraint' field is marked as 'all', suggesting that this element applies universally within its context. The 'Conformance' field is marked with 'M', meaning that the 'SessionID' is a mandatory element. This indicates that the 'SessionID' must always be implemented and supported in any device or application that uses the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, within the Events section, the table row describes an element with the ID '1' named 'State', which is of the type 'StateEnum' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'State' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions. It is an essential component of the cluster's functionality and must be present in all implementations.

* The table row entry pertains to the "Reason" event within the Energy EVSE Cluster, specifically under the Events section. The "Reason" is identified by the ID '2' and is of the type "EnergyTransferStoppedReasonEnum," with a constraint labeled as "all," indicating that it applies universally within its context. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Reason" event is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* In the context of the Energy EVSE Cluster, specifically within the Events section, the table row describes an element with the ID '4' named 'EnergyTransferred'. This element is of the type 'energy-mWh' and has a constraint that specifies a minimum value of 0. The conformance rule for 'EnergyTransferred' is marked as 'M', which means it is a Mandatory element. This indicates that the 'EnergyTransferred' event must always be implemented and supported in any device or system that conforms to this specification, without any conditions or exceptions.

* The table row entry describes an event within the Energy EVSE Cluster, specifically named "EnergyDischarged," which is of the type "energy-mWh" and has a constraint that the value must be a minimum of 0. The conformance rule for this event is "V2X," indicating that the event is mandatory if the V2X feature is supported. In the context of the Matter specification, this means that if a device or system supports the V2X feature, it must also support the "EnergyDischarged" event as part of its functionality. If V2X is not supported, the conformance rule does not apply, and the event may not be required.

9.3.10.4.1. SessionID Field
This field SHALL indicate the value of the SessionID attribute prior to the energy transfer stopping.
9.3.10.4.2. State Field
This field SHALL indicate the value of the State attribute prior to the energy transfer stopping.
9.3.10.4.3. Reason Field
This field SHALL indicate the reason why the energy transferred stopped.
9.3.10.4.4. EnergyTransferred Field
This field SHALL indicate the amount of energy transferred from the EVSE to the EV since the previ
ous EnergyTransferStarted event, in mWh.
9.3.10.4.5. EnergyDischarged Field
This field SHALL indicate the amount of energy transferred from the EV to the EVSE since the previ
ous EnergyTransferStarted event, in mWh.
9.3.10.5. Fault Event
If the EVSE detects a fault it SHALL generate a Fault Event. The SupplyState attribute SHALL be set
to DisabledError and the type of fault detected by the EVSE SHALL be stored in the FaultState
attribute.
This event SHALL be generated when the FaultState changes from any error state. i.e. if it changes
from NoError to any other state and if the error then clears, this would generate 2 events.
It is assumed that the fault will be cleared locally on the EVSE device. When all faults have been
cleared,  the  EVSE  device  SHALL  set  the  FaultState  attribute  to  NoError  and  the  SupplyState
attribute SHALL be set back to its previous state.

_Table parsed from section 'Events':_

* In the Energy EVSE Cluster, within the context of Events, the table row describes an element with the ID '0' named 'SessionID'. This element is of type 'uint32', indicating it is a 32-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is marked as 'M', which means that the 'SessionID' is a mandatory element. This implies that the 'SessionID' must always be included and supported in implementations of the Energy EVSE Cluster's Events section, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically in the context of Events. The element is identified by the ID '1' and is named 'State'. It is of the type 'StateEnum' and has a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'State' element is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row entry for the Energy EVSE Cluster within the Events section describes an element with the ID '2', named 'FaultStatePreviousState'. This element is of the type 'FaultStateEnum' and has a constraint labeled as 'all', indicating that it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'FaultStatePreviousState' element is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

* The table row describes an element within the Energy EVSE Cluster, specifically in the Events section, with an ID of '4' and named 'FaultStateCurrentState'. This element is of the type 'FaultStateEnum' and has a constraint labeled as 'all', indicating it applies universally across all relevant contexts. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'FaultStateCurrentState' element is always required to be implemented in any device or system that supports the Energy EVSE Cluster, without any conditions or exceptions.

9.3.10.5.1. SessionID Field
This field SHALL indicate the value of the SessionID attribute prior to the Fault State being changed.
A value of null indicates no sessions have occurred before the fault occurred.
9.3.10.5.2. State Field
This field SHALL indicate the value of the State attribute prior to the Fault State being changed.
9.3.10.5.3. FaultStatePreviousState Field
This  field  SHALL  indicate  the  value  of  the  FaultState  attribute  prior  to  the  Fault  State  being
changed.
9.3.10.5.4. FaultStateCurrentState Field
This field SHALL indicate the current value of the FaultState attribute.
9.3.10.6. RFID Event
This event SHALL be generated when a RFID card has been read. This allows a controller to register
the card ID and use this to authenticate and start the charging session.

_Table parsed from section 'Events':_

* In the context of the Energy EVSE Cluster, specifically within the Events section, the table row describes an element with the ID '0' named 'UID'. This element is of the type 'octstr', which is a string of octets, and it has a constraint limiting its maximum length to 10 octets. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'UID' element is always required to be implemented in any device or application that supports the Energy EVSE Cluster, without any conditions or exceptions.

9.3.10.6.1. UID Field
The UID field (ISO 14443A UID) is either 4, 7 or 10 bytes.