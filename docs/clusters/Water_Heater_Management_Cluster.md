
# 9.5 Water Heater Management Cluster

This cluster is used to allow clients to control the operation of a hot water heating appliance so that
it can be used with energy management.
Heating of hot water is one of the main energy uses in homes, and when coupled with the Energy
Management cluster, it can help consumers save cost (e.g. using power at cheaper times or from
local solar PV generation).

## Dependencies
This cluster SHALL be on an endpoint that also includes the Thermostat cluster as this cluster is
dependent on the Thermostat cluster.

## Data Types
9.5.6.1. WaterHeaterHeatSourceBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Water Heater Management Cluster, under the Data Types section, the table entry for 'Bit' 0, named 'ImmersionElement1', refers to the Immersion Heating Element 1. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the ImmersionElement1 data type is a required element within the Water Heater Management Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

* In the Water Heater Management Cluster, under the Data Types section, the table row describes a data element named "ImmersionElement2," which corresponds to bit '1' and is summarized as "Immersion Heating Element 2." The conformance rule for this element is marked as 'M,' indicating that it is mandatory. This means that the "ImmersionElement2" data element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the Water Heater Management Cluster, under the Data Types section, the table row describes a feature identified by the bit value '2', named 'HeatPump', which pertains to heat pump heating. The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that the 'HeatPump' feature is always required to be implemented in any device or system that supports the Water Heater Management Cluster, without any conditions or exceptions.

* In the Water Heater Management Cluster, under the Data Types section, the table row describes a data element with the bit position '3', named 'Boiler', which summarizes its function as 'Boiler Heating (e.g., Gas or Oil)'. The conformance rule for this element is marked as 'M', indicating that it is mandatory. This means that the 'Boiler' data element is always required to be implemented in any device or system that conforms to the Matter specification for this cluster. There are no conditions or exceptions; the inclusion of this element is obligatory.

* In the Water Heater Management Cluster, under the Data Types section, the table row describes a data type with the bit value '4', named 'Other', which summarizes as 'Other Heating'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Other' heating data type must always be implemented and supported in any system or device that adheres to the Matter specification for this cluster. There are no conditions or exceptions; it is a required element for compliance.

9.5.6.2. BoostStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Water Heater Management Cluster, under the Data Types section, the table row describes a data type with the value '0', named 'Inactive', which indicates that the boost function is not currently active. The conformance rule for this entry is marked as 'M', meaning that this element is mandatory. This implies that the 'Inactive' state must always be supported and implemented in any device or system utilizing this cluster, as it is a required component of the specification.

* In the Water Heater Management Cluster, under the Data Types section, the table entry describes a data type with the value '1' named 'Active', which indicates that the boost function is currently active. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Active' data type is always required to be implemented in any device or system that conforms to this specification. There are no conditions or dependencies affecting its requirement; it must be included in all implementations of the Water Heater Management Cluster.

9.5.6.3. WaterHeaterBoostInfoStruct Type

_Table parsed from section 'Data Types':_

* In the Water Heater Management Cluster, under the Data Types section, the table row describes an element with the ID '0' named 'Duration'. This element is of the type 'elapsed-s', which likely refers to a time duration measured in seconds, and it has a constraint that specifies a minimum value of 1. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Duration' element is always required to be implemented in any device or application that supports the Water Heater Management Cluster, without any conditions or exceptions.

* In the Water Heater Management Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'OneShot', which is a boolean type with a default value of 'False' and no specific constraints. The conformance rule '[!TP], [TP].a-' indicates that the 'OneShot' element is optional based on certain conditions. Specifically, it is optional if the feature 'TP' is not supported, as denoted by '[!TP]'. If 'TP' is supported, the element is also optional, but with an additional unspecified condition 'a-' that might be detailed elsewhere in the documentation. This suggests that the 'OneShot' feature is not strictly required and its inclusion depends on the presence or absence of the 'TP' feature and potentially other conditions.

* In the Water Heater Management Cluster, under the Data Types section, the entry for 'EmergencyBoost' is identified by ID '2' and is of the boolean type, with a constraint applicable to all instances and a default value of 'False'. The conformance rule for 'EmergencyBoost' is marked as 'O', indicating that this feature is optional. This means that the 'EmergencyBoost' attribute is not required to be implemented in devices supporting this cluster, and there are no dependencies or conditions that alter its optional status.

* In the Water Heater Management Cluster, under the Data Types section, the entry for 'TemporarySetpoint' with ID '3' is defined as a data type of 'temperature'. The 'Constraint' is marked as 'desc', indicating that the specific constraints for this data type are detailed elsewhere in the documentation. The 'Conformance' is labeled as 'O', meaning that the 'TemporarySetpoint' is an optional element. This implies that while it is not required for implementation, it can be included at the discretion of the developer or manufacturer without any dependencies or conditions.

* In the Water Heater Management Cluster, under the Data Types section, the entry for 'TargetPercentage' with ID '4' and type 'percent' is subject to specific conformance rules. The conformance expression 'TargetReheat, [TP]' indicates that the 'TargetPercentage' element is mandatory if the 'TargetReheat' feature is supported. If 'TargetReheat' is not supported, then the element becomes optional if the 'TP' feature is supported. This means that the presence of 'TargetPercentage' is primarily driven by the support of 'TargetReheat', but it can still be optionally included if 'TP' is supported in the absence of 'TargetReheat'.

* In the Water Heater Management Cluster, under the Data Types section, the entry with ID '5' refers to the 'TargetReheat' attribute, which is of type 'percent' and is constrained by the maximum 'TargetPercentage'. The conformance rule '[TP].a-' indicates that the 'TargetReheat' attribute is optional if the feature 'TP' (presumably representing a specific feature related to the water heater's target percentage functionality) is supported. The use of brackets around 'TP' signifies that the attribute is not mandatory but becomes optional under the condition that 'TP' is present. If 'TP' is not supported, the conformance rule does not specify any further requirements, implying no additional mandatory or optional status beyond this condition.

9.5.6.3.1. Duration Field
This field SHALL indicate the time period, in seconds, for which the boost state is activated.
9.5.6.3.2. OneShot Field
This field SHALL indicate whether the boost state SHALL be automatically canceled once the hot
water has reached either:
• the set point temperature (from the thermostat cluster)
• the TemporarySetpoint temperature (if specified)
• the TargetPercentage (if specified).
9.5.6.3.3. EmergencyBoost Field
This field SHALL indicate that the consumer wants the water to be heated quickly. This MAY cause
multiple heat sources to be activated (e.g. a heat pump and direct electric immersion heating ele
ment).
The choice of which heat sources are activated is manufacturer specific.
9.5.6.3.4. TemporarySetpoint Field
This field SHALL indicate the target temperature to which the water will be heated.
If included, it SHALL be used instead of the thermostat cluster set point temperature whilst the
boost state is activated.
The value of this field SHALL be within the constraints of the MinHeatSetpointLimit and MaxHeat
SetpointLimit attributes (inclusive), of the thermostat cluster.
9.5.6.3.5. TargetPercentage Field
This field SHALL indicate the target percentage of hot water in the tank that the TankPercentage
attribute must reach before the heating is switched off.
9.5.6.3.6. TargetReheat Field
This field SHALL indicate the percentage to which the hot water in the tank SHALL be allowed to
fall before again beginning to reheat it.
For example if the TargetPercentage was 80%, and the TargetReheat was 40%, then after initial
heating to 80% hot water, the tank may have hot water drawn off until only 40% hot water remains.
At this point the heater will begin to heat back up to 80% of hot water. If this field and the OneShot
field were both omitted, heating would begin again after any water draw which reduced the
TankPercentage below 80%.
This field SHALL be less than or equal to the TargetPercentage field.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Water Heater Management Cluster, specifically the "HeaterTypes" attribute. This attribute is identified by the ID '0x0000' and is of the type 'WaterHeaterHeatSourceBit map', with a constraint of 'all', indicating that all bits in the map are relevant. The quality is marked as 'F', and it has a default value of '0'. The access level is 'R V', meaning it is readable and possibly volatile. The conformance rule for this attribute is 'M', which signifies that the "HeaterTypes" attribute is mandatory. This means it must always be implemented in any device or application that supports the Water Heater Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "HeatDemand" within the Water Heater Management Cluster, specifically under the Attributes section. This attribute has an ID of '0x0001' and is of the type 'WaterHeaterHeatSourceBitmap', with a constraint of 'all', indicating it applies universally within its context. The default value for this attribute is '0', and it has read and view access permissions, denoted by 'R V'. The conformance rule for "HeatDemand" is 'M', meaning it is a mandatory attribute. This indicates that the "HeatDemand" attribute must always be implemented in any device or application that supports the Water Heater Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "TankVolume" within the Water Heater Management Cluster. This attribute has an ID of '0x0002' and is of type 'uint16', indicating it is a 16-bit unsigned integer. It applies universally, as indicated by the 'Constraint' being 'all', and has a default value of '0'. The 'Access' field 'R V' suggests that this attribute is readable and may have volatile characteristics. The 'Conformance' field 'EM' indicates that the "TankVolume" attribute is mandatory under the condition that the feature or context 'E' is supported. If 'E' is not supported, the conformance rule does not specify an alternative, implying that the attribute is not required in such cases.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "EstimatedHeatRequired" within the Water Heater Management Cluster. This attribute has an ID of '0x0003' and is of the type 'energy- mWh', with a constraint that its value must be at least 0, and it defaults to 0. The access permissions for this attribute are 'R V', indicating it is readable and has a volatile nature. The conformance rule 'EM' signifies that this attribute is mandatory for devices that support the Water Heater Management Cluster, meaning it must always be implemented and available in such devices.

* In the Water Heater Management Cluster, the attribute 'TankPercentage' is identified by the ID '0x0004' and is of the type 'percent'. It applies universally ('Constraint': 'all') and has a default value of '0'. The access permissions for this attribute are 'R V', indicating it is readable and can be viewed. The 'Conformance' field is marked as 'TP', which means this attribute is currently in a provisional state ('P'), suggesting that its status is temporary and subject to change. The 'T' in 'TP' is not a standard conformance tag, but it might imply a specific condition or feature related to the Water Heater Management Cluster that is not explicitly defined in the provided guide. Therefore, the attribute is provisionally included, and its future conformance status may be updated to mandatory or another status as the specification evolves.

* The table row describes an attribute named "BoostState" within the Water Heater Management Cluster. This attribute has an ID of '0x0005' and is of the type 'BoostStateEnum'. It is constrained to apply to all instances, with a default value set to 'Inactive'. The access level for this attribute is 'R V', indicating it is readable and can be viewed. The conformance rule for "BoostState" is 'M', which means this attribute is mandatory. It is always required to be implemented in any device or application that supports the Water Heater Management Cluster, without any conditions or exceptions.

9.5.7.1. HeaterTypes Attribute
This attribute SHALL indicate the heat sources that the water heater can call on for heating. If a bit
is set then the water heater supports the corresponding heat source.
9.5.7.2. HeatDemand Attribute
This attribute SHALL indicate if the water heater is heating water. If a bit is set then the corre
sponding heat source is active.
9.5.7.3. TankVolume Attribute
This attribute SHALL indicate the volume of water that the hot water tank can hold (in units of
Litres). This allows an energy management system to estimate the required heating energy needed
to reach the target temperature.
9.5.7.4. EstimatedHeatRequired Attribute
This attribute SHALL indicate the estimated heat energy needed to raise the water temperature to
the target setpoint. This can be computed by taking the specific heat capacity of water (4182 J/kg °C)
and by knowing the current temperature of the water, the tank volume and target temperature.
For example, if the target temperature was 60°C, the current temperature was 20°C and the
tank volume was 100L:
Mass of water          = 1kg per Litre
Total Mass             = 100 x 1kg = 100kg
Δ Temperature          = (target temperature - current temperature)
= (60°C - 20°C) = 40°C
Energy required to
heat the water to 60°C = 4182 x 40 x 100 = 16,728,000 J
Converting Joules in to Wh of heat (divide by 3600):
= 16,728,000 J / 3600
= 4647 Wh (4.65kWh)
If the TankPercent feature is supported, then this estimate SHALL also take into account the per
centage of the water in the tank which is already hot.
The electrical energy required to heat the water depends on the heating system
used to heat the water. For example, a direct electric immersion heating element
can be close to 100% efficient, so the electrical energy needed to heat the hot water
is nearly the same as the EstimatedHeatEnergyRequired. However some forms of
NOTE
heating, such as an air-source heat pump which extracts heat from ambient air,
requires much less electrical energy to heat hot water. Heat pumps can be produce
3kWh of heat output for 1kWh of electrical energy input. The conversion between
heat energy and electrical energy is outside the scope of this cluster.
9.5.7.5. TankPercentage Attribute
This attribute SHALL indicate an approximate level of hot water stored in the tank, which might
help consumers understand the amount of hot water remaining in the tank. The accuracy of this
attribute is manufacturer specific.
In most hot water tanks, there is a stratification effect where the hot water layer rests above a
cooler layer of water below. For this reason cold water is fed in at the bottom of the tank and the
hot water is drawn from the top.
Some water tanks might use multiple temperature probes to estimate the level of the hot water
layer. A water heater with multiple temperature probes is likely to implement an algorithm to esti
mate the hot water tank percentage by taking into account the temperature values of each probe to
determine the height of the hot water.
However it might be possible with a single temperature probe to estimate how much hot water is
left using a simpler algorithm:
For example, if the target temperature was 60°C, the CurrentTemperature was 40°C from a
single temperature probe measuring the average water temperature and the temperature of
incoming cold water (COLD_WATER_TEMP) was assumed to be 20°C:
TankPercentage = int(((current temperature - COLD_WATER_TEMP) / (target
temperature - COLD_WATER_TEMP)) * 100)
TankPercentage = min( max(TankPercentage,0), 100)
TankPercentage = 50%
9.5.7.6. BoostState Attribute
This attribute SHALL indicate whether the Boost, as triggered by a Boost command, is currently
Active Inactive
or  .
See Boost and CancelBoost commands for more details.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Water Heater Management Cluster, specifically the "Boost" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response from the server, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'M', meaning that access to this command is mandatory. The 'Conformance' field is also marked 'M', signifying that the "Boost" command is a mandatory element within this cluster. This means that any implementation of the Water Heater Management Cluster must include the "Boost" command as a required feature, with no conditions or exceptions.

* In the Water Heater Management Cluster, the command identified as 'CancelBoost' (ID: 0x01) is a client-to-server command that requires a response from the server. The access level for this command is mandatory ('M'), indicating that it must always be implemented in devices supporting this cluster. The conformance rule for 'CancelBoost' is also marked as 'M', meaning that this command is a mandatory feature of the Water Heater Management Cluster. Therefore, any implementation of this cluster must include the 'CancelBoost' command, ensuring that it is consistently available and functional across all compliant devices.

9.5.8.1. Boost Command
Allows a client to request that the water heater is put into a Boost state.

_Table parsed from section 'Commands':_

* In the Water Heater Management Cluster, within the Commands section, the entry for 'BoostInfo' with ID '0' is defined as a command of type 'WaterHeaterBoostInfoStruct'. The 'Constraint' is listed as 'all', indicating that this command applies universally without specific limitations. The 'Conformance' for 'BoostInfo' is marked as 'M', which means that this command is mandatory. It is required to be implemented in all devices or systems that support the Water Heater Management Cluster, without any exceptions or conditional requirements.

9.5.8.1.1. Effect on receipt
On receipt of this command, this SHALL allow the water heater to attempt to heat the water, which
Off Timed
may override other settings, for example, if the Water Heater Mode is set to  , or   and it is
during one of the Off periods.
If the duration field is too short for the water heater to accept, for example a heat pump may take
several minutes to ramp up in operation, then the boost command SHALL be rejected with a status
of INVALID_IN_STATE.
Active
If successful, the value of the BoostState attribute SHALL transition to  , and a response with
status of SUCCESS SHALL be returned, and a BoostStarted event SHALL be generated to include the
field values received in the command.
The water in the tank SHALL be heated until one of the following conditions is met:
• the temperature reaches the set point in the corresponding thermostat cluster or the Tempo
rarySetpoint (if included)
• the TankPercentage attribute value reaches the TargetPercentage (if it was included)
If OneShot is specified then once the hot water has reached the set point temperature (or the Tem
porarySetpoint temperature, if specified) or the TargetPercentage (if specified), or the boost com
Inactive
mand’s duration times out after the specified Duration, then BoostState transitions to  . This
SHALL cause the BoostEnded event to be generated.
If the Water Heater was already in the BoostState 'Active' when this command is received, it SHALL
continue in this BoostState, but SHALL discard the effect of the values of the fields from the previ
ous Boost commands, and SHALL continue with the values of the fields from the new Boost com
mand. A new BoostStarted event SHALL be generated to include the field values received in the
new command.
9.5.8.2. CancelBoost Command
Allows a client to cancel an ongoing Boost operation.
This command has no payload.
9.5.8.2.1. Effect on receipt
Inactive
If the BoostState attribute value was already   when this command is received, the Boost
Inactive
State attribute value shall remain   and the server SHALL return SUCCESS.
Inactive
Otherwise the Water Heater SHALL transition the BoostState to  , generate a BoostEnded
event, and the water heating reverts to being controlled through the current Water Heater Mode
Off Manual Timed
(e.g.  ,   or  ).

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Water Heater Management Cluster, specifically the "BoostStarted" event. This event has an ID of '0x00' and is categorized under the 'INFO' priority level. The 'Access' field is marked as 'V', indicating that it is viewable. The 'Conformance' field is marked with an 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "BoostStarted" event is always required to be implemented in any device or application that supports the Water Heater Management Cluster. There are no conditions or dependencies affecting its mandatory status, ensuring that it is a fundamental part of the cluster's functionality.

* The table row describes an event within the Water Heater Management Cluster, specifically the "BoostEnded" event, which has an ID of '0x01'. This event is categorized under the 'INFO' priority level, indicating it provides informational messages. The 'Access' field is marked as 'V', suggesting that this event is visible or can be accessed in some manner. The 'Conformance' field is marked with 'M', meaning that the "BoostEnded" event is mandatory. This implies that any implementation of the Water Heater Management Cluster must include this event, as it is a required element of the specification.

9.5.9.1. BoostStarted Event
This event SHALL be generated whenever a Boost command is accepted.

_Table parsed from section 'Events':_

* In the Water Heater Management Cluster, under the Events section, the entry with ID '0' is named 'BoostInfo' and is of the type 'WaterHeaterBoostInfoStruct'. The 'Constraint' for this entry is 'all', indicating it applies universally within its context. The 'Conformance' for 'BoostInfo' is marked as 'M', which stands for Mandatory. This means that the 'BoostInfo' event is a required element in the Water Heater Management Cluster and must be implemented in all devices or systems that support this cluster, without any conditions or exceptions.

The corresponding structure fields within the WaterHeaterBoostInfoStruct are copied from the
Boost command.
9.5.9.2. BoostEnded Event
Active Inactive
This event SHALL be generated whenever the BoostState transitions from   to  .