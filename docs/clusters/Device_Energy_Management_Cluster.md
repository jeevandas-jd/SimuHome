
# 9.2 Device Energy Management Cluster

This cluster allows a client to manage the power draw of a device. An example of such a client could
be an Energy Management System (EMS) which controls an Energy Smart Appliance (ESA).
In most deployments the EMS will be the client, and the ESA will host the Device Energy Manage
ment Cluster server.
Figure 17. Example of the how an EMS is a client of multiple ESAs Device Energy Management clusters.
This cluster is intended to be generic in nature and could apply to any electrical load or generator
(e.g. a Battery Electric Storage System - BESS, solar PV inverter, EVSE, HVAC, heat pump, hot water
heater, white goods appliances etc).
It consists of the following areas which SHALL be supported by all devices implementing this clus
ter:
• Description of ESA and its capabilities & power limits (sometimes referred to as a nameplate)
• Current state of operation (including user opt-out, safety limitations / alarms)
There are some optional capabilities that some ESAs may be able to offer:
• Ability to control the load or generation
• Forecast data, including when it can be flexible (i.e. modify the power or time period)
• The ability to have their power profile adjusted by an EMS, and to provide an updated Forecast
back to the EMS.
This allows the EMS to manage multiple home loads and where ESAs can be flexible, continuously
optimizing the home energy to minimize cost, reduce CO2 impact, maximize self-consumption of
solar PV and provide Demand Side Response (DSR) Grid services.
It is likely that the ESA may also use the Pricing Cluster to obtain incentive signals such as 'grid car
bon intensity', 'time of use' or 'type of use' tariffs to schedule its operation to run at the cheapest
and greenest times.
Figure 18. Example of the how an HVAC may use multiple clusters
Grid Services are market dependent and will use other protocols ([OpenADR] /
NOTE [IEEE2030.5]) to communicate grid events to the EMS. These are outside the scope of
Matter.
Different  markets  may  follow  different  approaches,  but  the  UK  [PAS1878]  and
NOTE [EUCodeOfConduct] give examples of how ESAs may be mandated to support these
features in the future.

## Dependencies
This cluster does not report electrical power and electrical energy. Devices that use this cluster
SHALL also support the Electrical Power Measurement and optionally support the Electrical Energy
Measurement cluster to allow an energy management system to perform its role. See Device Type
library for device specific details.

## Definitions
9.2.6.1. Power
Power is defined in the main specification (see Data Model) in units of milliwatts. It is a signed
value, where positive values indicate the direction of power flow into the node. A negative value
indicates that the device is supplying power, and thus reducing the overall load of the premises on
the grid supply.
Figure 19. Power flows into devices
Solar PV inverter example: A solar PV inverter is normally connected to the premises' wiring, so
its generation power will be indicated as a negative integer, since power is flowing out of the node
towards the mains connection. Note that at night (when there is no solar production) the PV
inverter will consume some standby power, and this will result in a small positive power reading.
Grid Power: Power from the grid is measured by a utility meter which is imported into the node, so
positive power values indicate that power is flowing into the premises. Negative values indicate
power is flowing back towards the grid.
EVSE example: An EVSE provides power to the EV (when charging) so a positive value indicates
that the power is flowing into the EVSE from the mains supply when the EV is charging, and is act
ing as a load on the grid supply, and negative value indicates that the EV is discharging.
BESS example: A battery storage inverter normally provides power to loads when discharging, so
negative power indicates discharging (power is flowing back to the mains supply) therefore reduc
ing the load on the grid, and positive power indicates power flowing from the mains to the battery
during charging (adding load to the grid).
Washing Machine example: A washing machine only consumes power (i.e. is a load), so it will
always have a positive power value.
9.2.6.2. Energy
Energy is defined in the main specification (see Data Model). This is defined in units of mWh (milli
watt-hours). It is signed value, where positive values indicate the direction of current flow towards
a load.

## Data Types
9.2.7.1. CostTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, within the Data Types section, the table row describes an entry with the 'Name' "Financial" and a 'Value' of "0", which summarizes the concept of "Financial cost." The 'Conformance' field is marked as "M," indicating that this element is mandatory. This means that the "Financial" data type must always be included and supported in any implementation of the Device Energy Management Cluster, without any conditions or exceptions.

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section and describes a data type named "GHGEmissions," which represents the cost of grid CO2e grams. The conformance rule for this entry is marked as "M," indicating that the "GHGEmissions" data type is mandatory. This means that any implementation of the Device Energy Management Cluster must include this data type without exception. It is a required element, ensuring that the measurement of grid CO2e emissions is consistently supported across all devices utilizing this cluster.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "Comfort" and a value of "2." This entry is summarized as representing the "Consumer comfort impact cost." According to the conformance rule specified as "M," this element is mandatory, meaning it is always required to be implemented in any system or device that adheres to this specification. There are no conditions or dependencies affecting its mandatory status, indicating its fundamental importance within the cluster's framework.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an element named "Temperature," which has a value of '3' and is summarized as "Temperature impact cost." The conformance rule for this element is 'M,' indicating that it is mandatory. This means that the "Temperature" element is always required to be implemented in any device or system that adheres to this specification. There are no conditions or dependencies affecting its inclusion; it must be present in all compliant implementations of the Device Energy Management Cluster.

9.2.7.1.1. Financial Value
This value SHALL indicate that the cost is related to the financial cost to provide the energy.
9.2.7.1.2. GHGEmissions Value
This value SHALL indicate that the cost is related to greenhouse gas emissions (in grams of CO2e).
9.2.7.1.3. Comfort Value
This value SHALL indicate that the cost is related to some abstract sense of comfort expressed by
the consumer; a higher value indicates more discomfort. For example, a consumer may be more
comfortable knowing that their EV is charged earlier in the day in case there is a sudden need to
depart and drive to the hospital. Or the consumer may feel inconvenienced by the fact that they
need to wait for the washing machine to finish its load so that they can use it again.
9.2.7.1.4. Temperature Value
This value SHALL indicate that the cost is related to the temperature of the home or water being at
its setpoint. Some consumers may be more sensitive to being too hot or too cold.
This is expressed in degrees Celsius.
9.2.7.2. ESATypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '0' and the name 'EVSE', which stands for Electric Vehicle Supply Equipment. The summary indicates that this entry pertains to equipment used for supplying power to electric vehicles. The conformance rule for this entry is 'O', meaning that the inclusion of this element is optional. It is not required for implementation and does not depend on any other features or conditions. This allows developers the flexibility to include or exclude this element based on their specific needs or preferences without any mandatory obligation.

* In the context of the Device Energy Management Cluster, under the Data Types section, the table entry describes a data type named "SpaceHeating," which represents a space heating appliance. The conformance rule for this entry is marked as "O," indicating that the "SpaceHeating" data type is optional. This means that the inclusion of this data type in a device's implementation is not required and has no dependencies on other features or conditions. Devices can choose to support this data type, but it is not mandatory for compliance with the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "WaterHeating," which corresponds to a value of '2'. This entry represents a data type associated with a water heating appliance. The conformance rule for this entry is marked as 'O', meaning that the inclusion of this data type is optional. There are no dependencies or conditions that require its implementation, allowing developers the flexibility to include or exclude this feature based on their specific application needs without any mandatory obligation.

* In the context of the Device Energy Management Cluster, under the Data Types section, the entry for 'SpaceCooling' with a value of '3' represents a data type associated with space cooling appliances. The summary indicates that this data type pertains to appliances used for cooling spaces. The conformance rule for this entry is 'O', which means that the 'SpaceCooling' data type is optional. This implies that its implementation is not required and there are no dependencies or conditions that mandate its inclusion in a device's functionality.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section and describes a data type with the name "SpaceHeatingCooling," which is identified by the value '4'. This data type represents a space heating and cooling appliance. The conformance rule for this entry is marked as 'O', which stands for Optional. This means that the inclusion of the "SpaceHeatingCooling" data type is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this data type in their implementations without any mandatory obligation.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an element named "BatteryStorage," which represents a Battery Electric Storage System and is assigned the value '5'. The conformance rule for this element is marked as 'O', indicating that it is optional. This means that the inclusion of the "BatteryStorage" element is not required and has no dependencies on other features or conditions. Devices implementing this cluster can choose to support this element, but it is not mandatory for compliance with the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '6' named 'SolarPV', which refers to a Solar PV inverter. The conformance rule for this entry is 'O', indicating that the inclusion of the 'SolarPV' element is optional. This means that while the element can be supported within the cluster, it is not required and has no dependencies on other features or conditions. Therefore, implementers have the discretion to include or exclude this element based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the context of the Device Energy Management Cluster, within the Data Types section, the table entry describes a data type with the value '7', named 'FridgeFreezer', which summarizes as 'Fridge / Freezer'. The conformance rule for this entry is 'O', indicating that the 'FridgeFreezer' data type is optional. This means that while it is available for implementation, there are no requirements or dependencies mandating its inclusion in a device's feature set. Implementers can choose to support this data type based on their specific needs or product design without any obligation from the Matter specification.

* In the context of the Device Energy Management Cluster, under the Data Types section, the table row describes a data type with the value '8', named 'WashingMachine', which represents a washing machine. The conformance rule for this entry is 'O', meaning that the inclusion of this data type is optional. There are no dependencies or conditions that need to be met for its implementation, and it is not required for compliance with the Matter specification. This allows manufacturers the flexibility to include or exclude this data type based on their product design and feature set.

* In the context of the Device Energy Management Cluster, under the Data Types section, the table row describes a data type with the value '9' and the name 'Dishwasher', which is summarized as 'Dishwasher'. The conformance rule for this entry is 'O', indicating that the inclusion of this data type is optional. This means that while the 'Dishwasher' data type can be implemented within the Device Energy Management Cluster, it is not required and does not depend on any other features or conditions. Implementers have the flexibility to include or exclude this data type based on their specific needs or preferences without any mandatory obligation.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes a data type with the value '10', named 'Cooking', which represents a 'Cooking appliance'. The conformance rule for this entry is 'O', indicating that the inclusion of this data type is optional. This means that while it is available for use within the specification, there are no requirements or dependencies mandating its implementation. Developers have the flexibility to include or exclude this data type based on their specific needs or preferences without affecting compliance with the Matter specification.

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section, specifically focusing on a data type with the value '11' named "HomeWaterPump." This data type represents a home water pump, such as one used for a drinking well. According to the conformance rule 'O,' this element is classified as "Optional." This means that the inclusion of the "HomeWaterPump" data type is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this element based on their specific needs or preferences without any mandatory obligation.

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section and describes a data type named "IrrigationWaterPump," which is summarized as an "Irrigation water pump." The 'Conformance' field for this entry is marked as 'O,' indicating that the "IrrigationWaterPump" data type is optional. This means that the inclusion of this data type is not required and does not depend on any other features or conditions. Devices implementing the Device Energy Management Cluster can choose to support this data type, but they are not obligated to do so according to the Matter specification.

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section, specifically describing a data type with the value '13', named 'PoolPump', which is summarized as 'Pool pump'. The conformance rule for this entry is 'O', indicating that the 'PoolPump' data type is optional. This means that the inclusion of the 'PoolPump' data type is not required and does not depend on any other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this data type based on their specific needs or use cases without any mandatory obligation.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '255' and the name 'Other', which represents an 'Other appliance type'. The conformance rule for this entry is 'O', indicating that this element is optional. This means that the inclusion of this 'Other' appliance type is not required and has no dependencies on other features or conditions within the Matter specification. Implementers have the flexibility to include or exclude this element based on their specific needs or preferences without affecting compliance with the standard.

9.2.7.3. ESAStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes a data type with the value '0' named 'Offline'. This indicates that the Energy Service Agent (ESA) is not available to the Energy Management System (EMS), such as during start-up or maintenance mode. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Offline' data type is always required to be implemented in any system or device that adheres to this specification, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "Online," which has a value of '1'. This entry signifies that the Energy Service Appliance (ESA) is functioning normally and can be controlled by the Energy Management System (EMS). The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Online" status is a required element in the specification and must always be implemented in any system using this cluster.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '2' named 'Fault'. This entry indicates that the Energy Service Appliance (ESA) has encountered a fault and is unable to provide service. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Fault' data type is always required to be implemented in any device or system that conforms to this specification. There are no conditions or exceptions; it must be included to comply with the Matter IoT specification for this cluster.

* In the Device Energy Management Cluster, under the Data Types section, the entry for 'PowerAdjustActive' with a value of '3' indicates that the Energy Service Agent (ESA) is currently engaged in a power adjustment event. The conformance rule 'PA' signifies that this element is currently in a provisional state, meaning its status is temporary. The 'A' following the 'P' suggests that the element is intended to become mandatory in the future. Therefore, while 'PowerAdjustActive' is not yet a required element, it is anticipated to become mandatory as the specification evolves.

* In the context of the Device Energy Management Cluster, under the Data Types section, the table row describes a data type with the value '4' named 'Paused'. This indicates that the Energy Service Agreement (ESA) is currently paused by a client using the PauseRequest command. The conformance rule 'PAU' suggests that the presence or requirement of this data type is conditional upon the support of a feature or condition labeled 'PAU'. If the 'PAU' feature is supported, then the 'Paused' data type becomes mandatory. If 'PAU' is not supported, the conformance rule does not specify an alternative, implying that the data type may not be required or applicable.

9.2.7.4. OptOutStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "NoOptOut" and a value of '0'. This entry signifies that the user has not opted out of either local or grid optimizations. The conformance rule for "NoOptOut" is marked as 'M', which stands for Mandatory. This means that the presence of this element is always required in the implementation of the Device Energy Management Cluster, with no conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an element named "LocalOptOut" with a value of '1'. This element indicates that the user has chosen to opt out of local Energy Management System (EMS) optimizations. The conformance rule for "LocalOptOut" is marked as 'M', which stands for Mandatory. This means that the "LocalOptOut" element is always required to be implemented in any device or system that conforms to this specification. There are no conditions or dependencies affecting its mandatory status; it must be included in all relevant implementations.

* In the Device Energy Management Cluster, under the Data Types section, the entry for 'GridOptOut' with a value of '2' indicates a specific data type where the user has chosen to opt out of grid Energy Management System (EMS) optimizations only. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'GridOptOut' data type is always required to be implemented in any device or system that adheres to this specification. There are no conditions or dependencies affecting its necessity; it must be included in all relevant implementations.

* In the context of the Device Energy Management Cluster, within the Data Types section, the table row describes an entry with the name "OptOut" and a value of "3". This entry signifies that the user has chosen to opt out of all external optimizations. The conformance rule for "OptOut" is marked as "M", which stands for Mandatory. This means that the "OptOut" data type is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

9.2.7.5. CauseEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes a data type named "NormalCompletion" with a value of '0'. This data type indicates that the Energy Service Agreement (ESA) has successfully completed the power adjustment as requested. The conformance rule for "NormalCompletion" is marked as 'M', which means it is a mandatory element. This implies that any implementation of the Device Energy Management Cluster must include this data type, as it is always required according to the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '1' and the 'Name' of 'Offline', which summarizes that the Energy Service Agreement (ESA) was set to offline. The 'Conformance' field for this entry is marked as 'M', indicating that this element is mandatory. This means that the 'Offline' status must always be supported and implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "Fault" and a value of "2." The summary indicates that this entry pertains to a situation where the Energy Service Agreement (ESA) has encountered a fault, preventing the completion of an adjustment. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "Fault" data type is a required element in the specification and must always be implemented in any device or system that adheres to this cluster's standards.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the name "UserOptOut" and a value of '3'. This entry signifies that the user has chosen to disable the Energy Service Agreement's (ESA) flexibility capability. The conformance rule for "UserOptOut" is marked as 'M', which stands for Mandatory. This means that the "UserOptOut" element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '4' and the name 'Cancelled'. This entry signifies that an adjustment was cancelled by a client. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Cancelled' data type is a required element in the specification and must always be implemented in any system or device that supports the Device Energy Management Cluster. There are no conditions or exceptions to this requirement; it is an essential component of the cluster's functionality.

9.2.7.6. AdjustmentCauseEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Device Energy Management Cluster, under the Data Types section, the entry for 'LocalOptimization' with a value of '0' indicates that this feature is related to adjusting settings to optimize local energy usage. The conformance rule for 'LocalOptimization' is marked as 'M', which stands for Mandatory. This means that the 'LocalOptimization' feature is always required to be implemented in any device or system that supports this cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Device Energy Management Cluster, specifically under the Data Types section. The element is named "GridOptimization" and is identified by the value '1'. Its purpose is to adjust settings to optimize grid energy usage. The conformance rule for this element is 'M', which stands for Mandatory. This means that the GridOptimization feature is always required to be implemented in any device or system that conforms to the Matter specification for this cluster. There are no conditions or exceptions; it must be included in all relevant implementations.

9.2.7.7. ForecastUpdateReasonEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '0' named 'InternalOptimization'. This entry signifies that an update was triggered due to internal optimization of the ESA (Energy Service Architecture) device. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'InternalOptimization' element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the Device Energy Management Cluster, under the Data Types section, the entry for 'LocalOptimization' with a value of '1' indicates that this data type represents an update due to local Energy Management System (EMS) optimization. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented in any device or system that supports this cluster. There are no conditions or dependencies affecting its necessity; it must be included as part of the standard implementation.

* The table row entry pertains to the "Device Energy Management Cluster" within the "Data Types" section and describes a data type named "GridOptimization" with a value of '2'. The summary indicates that this data type is related to updates due to grid optimization. The conformance rule for "GridOptimization" is marked as 'M', which stands for Mandatory. This means that the "GridOptimization" data type is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

9.2.7.8. PowerAdjustReasonEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an entry with the value '0' and the name 'NoAdjustment'. This entry summarizes that there is no active power adjustment. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'NoAdjustment' element is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the entry for 'LocalOptimizationAdjustment' is identified by the value '1'. This entry indicates that there is an active PowerAdjustment due to local Energy Management System (EMS) optimization. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'LocalOptimizationAdjustment' element is always required to be implemented in any device or system that supports this cluster, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Data Types section, the table row describes an element named "GridOptimizationAdjustment" with a value of '2'. This element indicates that there is an active PowerAdjustment due to local Energy Management System (EMS) optimization. The conformance rule for "GridOptimizationAdjustment" is marked as 'M', which means it is mandatory. This implies that this element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

9.2.7.9. CostStruct Type
This indicates a generic mechanism for expressing cost to run an appliance, in terms of financial,
GHG emissions, comfort value etc.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'CostType'. It is of the type 'CostTypeEnum' and has a constraint labeled as 'all', with a default value of '0'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'CostType' element is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically in the Data Types section. The entry has an ID of '1' and is named 'Value', with a data type of 'int32'. It has a constraint labeled 'all', indicating it applies universally, and a default value of '0'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Value' attribute is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "DecimalPoints" within the Device Energy Management Cluster, specifically in the Data Types section. This attribute is of type `uint8`, meaning it is an 8-bit unsigned integer, and it applies universally as indicated by the constraint "all." The default value for this attribute is set to `0`. The conformance rule for "DecimalPoints" is marked as "M," which stands for Mandatory. This means that the "DecimalPoints" attribute is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Device Energy Management Cluster, under the Data Types section, the table row describes an entry with the ID '3', named 'Currency'. This entry is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that limits its maximum value to 999. The default value for this entry is '0'. The conformance rule for 'Currency' is marked as 'O', which means that this element is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

9.2.7.9.1. CostType Field
This field SHALL indicate the type of cost being represented (see CostTypeEnum).
9.2.7.9.2. Value Field
This field SHALL indicate the value of the cost. This may be negative (indicating that it is not a cost,
but a free benefit).
For example, if the Value was -302 and DecimalPoints was 2, then this would represent a benefit of
3.02.
9.2.7.9.3. DecimalPoints Field
This field SHALL indicate the number of digits to the right of the decimal point in the Value field.
For example, if the Value was 102 and DecimalPoints was 2, then this would represent a cost of 1.02.
9.2.7.9.4. Currency Field
Indicates the currency for the value in the Value field. The value of the currency field SHALL match
the values defined by [ISO 4217].
This is an optional field. It SHALL be included if CostType is Financial.
9.2.7.10. PowerAdjustStruct Type

_Table parsed from section 'Data Types':_

* In the Device Energy Management Cluster, within the Data Types section, the table row describes an element with the ID '0' named 'MinPower'. This element is of the type 'power-mW', indicating it measures power in milliwatts. The 'Constraint' field specifies 'all', meaning there are no specific restrictions on its values beyond the type constraint. The 'Default' value is set to '0', indicating that if no other value is specified, it defaults to zero milliwatts. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'MinPower' element is always required to be implemented in any device that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'MaxPower'. This element is of the type 'power-mW', meaning it measures power in milliwatts, and it has a constraint that its value must be at least equal to 'MinPower'. The default value for 'MaxPower' is set to '0'. The conformance rule for 'MaxPower' is 'M', which indicates that this element is mandatory. This means that 'MaxPower' is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, within the Data Types section, the table row describes an element named 'MinDuration' with an ID of '2'. This element is of type 'elapsed-s', which likely represents a duration measured in seconds, and it has a constraint labeled as 'all', indicating it applies universally within its context. The default value for 'MinDuration' is set to '0'. The conformance rule for this element is 'M', which means that 'MinDuration' is a mandatory element. It is always required to be implemented in any device or system that supports the Device Energy Management Cluster, with no exceptions or conditions.

* In the context of the Device Energy Management Cluster, the table row describes a data type named 'MaxDuration' with an ID of '3'. This data type is of type 'elapsed-s', which likely represents a duration measured in seconds, and it has a constraint that it must be at least as large as 'MinDuration'. The conformance rule for 'MaxDuration' is marked as 'M', meaning it is mandatory. This indicates that the 'MaxDuration' data type is always required to be implemented within the Device Energy Management Cluster, with no conditions or exceptions.

9.2.7.10.1. MinPower Field
This field SHALL indicate the minimum power that the ESA can have its power adjusted to.
Note that this is a signed value. Negative values indicate power flows out of the node (e.g. discharg
ing a battery).
9.2.7.10.2. MaxPower Field
This field SHALL indicate the maximum power that the ESA can have its power adjusted to.
Note that this is a signed value. Negative values indicate power flows out of the node (e.g. discharg
ing a battery).
For example, if the charging current of an EVSE can be adjusted within the range of 6A to 32A on a
230V supply, then the power adjustment range is between 1380W and 7360W. Here the MinPower
would be 1380W, and MaxPower would be 7360W.
For example, if a battery storage inverter can discharge between 0 to 3000W towards a load, then
power is flowing out of the node and is therefore negative. Its MinPower would be -3000W and its
MaxPower would be 0W.
In another example, if a battery storage inverter can charge its internal battery, between 0W and
2000W. Here power is flowing into the node when charging. As such the MinPower becomes 0W
and MaxPower becomes 2000W.
9.2.7.10.3. MinDuration field
This field SHALL indicate the minimum duration, in seconds, that a controller may invoke an ESA
power adjustment. Manufacturers may use this to as an anti-cycling capability to avoid controllers
from rapidly making power adjustments.
9.2.7.10.4. MaxDuration field
This field SHALL indicate the maximum duration, in seconds, that a controller may invoke an ESA
power adjustment. Manufacturers may use this to protect the user experience, to avoid over heat
ing of the ESA, ensuring that there is sufficient headroom to use or store energy in the ESA or for
any other reason.
9.2.7.11. PowerAdjustCapabilityStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'PowerAdjustCapability'. It is a data type defined as a list of 'PowerAdjustStruct' with a constraint that limits the list to a maximum of 8 elements. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed from having any quality attributes. The default value for this entry is 'null'. The 'Conformance' field is marked as 'M', which means that the 'PowerAdjustCapability' element is mandatory. This implies that it is always required to be implemented in any device that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically in the Data Types section. The entry is identified by the ID '1' and is named 'Cause'. It is of the type 'PowerAdjustReasonEnum', which implies it is an enumerated data type used to specify reasons for power adjustments. The 'Constraint' is listed as 'all', indicating that this data type applies universally within its context. The default value for this entry is '0'. The 'Conformance' field is marked as 'M', which means that the 'Cause' element is mandatory. This indicates that it is always required to be implemented and supported in any device or application that utilizes the Device Energy Management Cluster, with no exceptions or conditions.

9.2.7.12. PowerAdjustCapability
This field SHALL indicate how the ESA can be adjusted at the current time.
For example, a battery storage inverter may need to regulate its internal temperature, or the charg
ing rate of the battery may be limited due to cold temperatures, or a change in the state of charge of
the battery may mean that the maximum charging or discharging rate is limited.
An empty list SHALL indicate that no power adjustment is currently possible.
Multiple entries in the list allow indicating that permutations of scenarios may be possible.
For example, a 10kWh battery could be at 80% state of charge. If charging at 2kW, then it would be
full in 1 hour. However, it could be discharged at 2kW for 4 hours.
In this example the list of PowerAdjustStructs allows multiple scenarios to be offered as follows:

_Table parsed from section 'Data Types':_

* The table row entry 'Entry [0] - Charging option:' in the context of the Device Energy Management Cluster under the Data Types section refers to the 'MinPower' element. The conformance rule for this element is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance of 'MinPower' would be determined by the specific conditions or feature codes associated with the Device Energy Management Cluster. If the conformance string were provided, it would specify whether 'MinPower' is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on the presence or absence of certain features. Without the specific conformance string, we cannot definitively state its requirement status, but it would typically be interpreted using the rules outlined in the guide.

* The table row entry titled "Entry [0] - Charging option: MaxPower" pertains to the Device Energy Management Cluster within the Data Types section. The conformance rule for this entry is not explicitly provided in the prompt, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance would typically dictate when the "MaxPower" data type is required or optional. If we assume a conformance string like "M", it would mean that the "MaxPower" data type is mandatory and must always be implemented within the cluster. If it were "O", it would indicate that the "MaxPower" data type is optional and can be included at the implementer's discretion. Without the specific conformance string, we can only provide a general interpretation based on typical usage within the Matter specification.

* The table row entry 'MinDuration' within the 'Device Energy Management Cluster' under the 'Data Types' section refers to a specific data type related to charging options. The conformance rule for 'MinDuration' is not explicitly provided in the given data, but based on the context, it would typically define whether this data type is mandatory, optional, provisional, deprecated, or disallowed. If the conformance were specified, it would determine the conditions under which 'MinDuration' must be implemented or can be omitted, using logical expressions and conditional rules as outlined in the Matter Conformance Interpretation Guide. For instance, if 'MinDuration' had a conformance of 'M', it would be mandatory for all implementations of the Device Energy Management Cluster. If it were 'O', it would be optional, and so on, depending on the specific conformance expression provided.

* The table row entry 'MaxDuration' within the 'Device Energy Management Cluster' under the 'Data Types' section pertains to a specific data type related to charging options. The conformance rule for 'MaxDuration' is indicated as 'Entry [0]'. According to the Matter Conformance Interpretation Guide, this suggests that the conformance is described elsewhere in the documentation, likely due to its complexity or specific conditions that cannot be succinctly expressed with basic tags or logical conditions. Therefore, to fully understand the requirements or optionality of 'MaxDuration', one would need to refer to the detailed description provided in the relevant section of the documentation. This approach ensures that all necessary conditions and dependencies are considered for this data type.

* In the context of the Device Energy Management Cluster, the table row entry 'Charging option:' and 'Discharging option:' pertains to data types related to energy management features. The conformance rule for this entry is not explicitly provided in the prompt, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance string would dictate when these options are required or optional. For instance, if the conformance were `M`, both options would be mandatory for any device implementing this cluster. If it were `O`, they would be optional and could be implemented at the discretion of the device manufacturer. The specific conformance string would determine the exact requirements, such as whether these options are always required, conditionally required based on other features, or optional. Without the specific conformance string, we can only generalize that these options are part of the data types used in managing device energy, and their implementation depends on the conformance rules set forth in the specification.

* The table row entry 'Entry [0] - Charging option:' with the data type 'MinPower' is part of the Device Energy Management Cluster, specifically within the Data Types section. The conformance rule for this entry is not explicitly provided in the data you shared. However, based on the Matter Conformance Interpretation Guide, if a conformance string were provided, it would dictate the conditions under which the 'MinPower' data type is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were `M`, it would mean that 'MinPower' is a mandatory element that must always be implemented. If it were `O`, it would be optional with no dependencies. Without a specific conformance string, we cannot determine the exact requirements for 'MinPower' in this context.

* The table row entry 'Entry [0] - Charging option:' with the data type 'MaxPower' is part of the Device Energy Management Cluster within the Data Types section. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would involve understanding whether 'MaxPower' is mandatory, optional, provisional, deprecated, or disallowed based on certain conditions or features. For instance, if the conformance were 'M', it would mean that 'MaxPower' is always required. If it were 'O', it would be optional with no dependencies. The specific conformance rule would dictate how 'MaxPower' should be implemented in devices supporting the Device Energy Management Cluster, ensuring consistent behavior across different implementations.

* The table row entry 'MinDuration' within the 'Device Energy Management Cluster' under the 'Data Types' section refers to a specific data type related to charging options. The conformance rule for 'MinDuration' is not explicitly provided in the given data, but based on the context of the Matter Conformance Interpretation Guide, we can infer that the conformance would dictate whether 'MinDuration' is mandatory, optional, provisional, deprecated, or disallowed based on certain conditions or features. If a specific conformance string were provided, it would detail under what conditions 'MinDuration' must be implemented or can be omitted, using logical expressions and conditional rules as outlined in the guide. Without the specific conformance string, we cannot determine the exact requirements for 'MinDuration', but it would typically involve evaluating feature support or other conditions to decide its necessity in the implementation.

* The table row entry 'MaxDuration' within the 'Device Energy Management Cluster' under the 'Data Types' section refers to a specific data type related to charging options. The conformance rule for 'MaxDuration' is not explicitly provided in the prompt, but based on the context, it would typically define when this data type is required or optional. If we assume a conformance string like `AB, O`, it would mean that 'MaxDuration' is mandatory if the feature `AB` is supported; otherwise, it is optional. This conformance rule helps implementers understand under what conditions they must include the 'MaxDuration' data type in their implementation of the Device Energy Management Cluster.

9.2.7.12.1. Cause field
This field SHALL indicate the cause of the currently active power adjustment.
9.2.7.13. ForecastStruct Type
This indicates a list of 'slots' describing the overall timing of the ESA’s planned energy and power
use, with different power and energy demands per slot. For example, slots might be used to
describe the distinct stages of a washing machine cycle.
SFR
Where an ESA does not know the actual power and energy use of the system, it may support the
feature and instead report its internal state.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is for an attribute named "ForecastID," which is of type `uint32` and has a constraint of "all," meaning it applies universally without specific limitations. The default value for this attribute is set to `0`. The conformance rule for "ForecastID" is marked as "M," indicating that this attribute is mandatory. This means that the "ForecastID" attribute is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "ActiveSlotNumber" within the Device Energy Management Cluster, specifically under the Data Types section. This attribute is identified by the ID '1' and is of type 'uint16', which means it is a 16-bit unsigned integer. The 'Constraint' field indicates that this attribute applies universally ('all'), and its 'Quality' is marked as 'X', meaning it is explicitly disallowed for certain quality-related purposes. The default value for this attribute is '0'. The 'Conformance' field is marked as 'M', which signifies that the "ActiveSlotNumber" attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, with no conditions or exceptions.

* In the context of the Device Energy Management Cluster, within the Data Types section, the table row describes an entry with the ID '2' named 'StartTime'. This entry is of the type 'epoch-s', which likely represents a timestamp format. The 'Constraint' is listed as 'all', indicating that there are no specific restrictions on its usage across different implementations. The 'Conformance' for 'StartTime' is marked as 'M', meaning it is a Mandatory element. This implies that the 'StartTime' data type must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

* In the Device Energy Management Cluster, under the Data Types section, the table row with ID '3' refers to an element named 'EndTime', which is of the type 'epoch-s' and has a constraint labeled 'all'. The conformance for 'EndTime' is marked as 'M', which stands for Mandatory. This means that the 'EndTime' element is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row entry for the "EarliestStartTime" data type within the Device Energy Management Cluster specifies that this element is identified by ID '4' and is of the type 'epoch-s', indicating it represents a time value in seconds since the epoch. The constraint 'all' suggests that this data type is universally applicable within its context. The quality 'X' indicates that this element is explicitly disallowed, meaning it should not be used or implemented. The conformance rule 'STA' does not directly match any of the basic conformance tags or logical conditions provided in the Matter Conformance Interpretation Guide. Therefore, it may refer to a specific condition or description detailed elsewhere in the documentation, which is not provided here. Without additional context, the exact conformance requirement for 'STA' remains unclear.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "LatestEndTime" data type within the Device Energy Management Cluster, specifically under the Data Types section. The "LatestEndTime" is identified by the ID '5' and is of the type 'epoch-s', which likely represents a timestamp in seconds since the epoch. The constraint 'all' suggests that this data type is applicable universally within its context. The conformance rule 'STA' indicates that the element is subject to a described conformance condition that is too complex to be captured by a simple tag or expression. Therefore, the specific requirements or conditions under which "LatestEndTime" is mandatory, optional, or otherwise must be referred to in a detailed description elsewhere in the documentation.

* The table row entry for the "IsPausable" attribute in the Device Energy Management Cluster, under the Data Types section, specifies that this attribute is of type 'bool' and applies to all instances within its context. The conformance rule for "IsPausable" is marked as 'M', which means it is a Mandatory element. This indicates that the "IsPausable" attribute is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, under the Data Types section, the entry for 'Slots' is identified by the ID '7'. It is defined as a list of 'SlotStruct' types, with a constraint that limits the list to a maximum of 10 items. The conformance rule for 'Slots' is marked as 'M', which means that this element is mandatory. Therefore, the 'Slots' list must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

* The table row entry describes a data type within the Device Energy Management Cluster, specifically named 'ForecastUpdateReason', which is of the type 'ForecastUpdateReasonEnum'. The 'Constraint' for this data type is listed as 'all', indicating that it applies universally within its context. The 'Conformance' field is marked as 'M', which means that the 'ForecastUpdateReason' data type is mandatory. This implies that it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

9.2.7.13.1. ForecastID Field
This field SHALL indicate the sequence number for the current forecast. If the ESA updates a fore
cast, it shall monotonically increase this value.
The ESA does not need to persist this value across reboots, since the EMS SHOULD be able to detect
that any previous subscriptions are lost if a device reboots. The loss of a subscription and subse
quent re-subscription allows the EMS to learn about any new forecasts.
The value of ForecastID is allowed to wrap.
9.2.7.13.2. ActiveSlotNumber Field
This  field  SHALL  indicate  which  element  of  the  Slots  list  is  currently  active  in  the  Forecast
sequence. A null value indicates that the sequence has not yet started.
9.2.7.13.3. StartTime Field
This field SHALL indicate the planned start time, in UTC, for the entire Forecast.
9.2.7.13.4. EndTime Field
This field SHALL indicate the planned end time, in UTC, for the entire Forecast.
9.2.7.13.5. EarliestStartTime Field
This field SHALL indicate the earliest start time, in UTC, that the entire Forecast can be shifted to.
A null value indicates that it can be started immediately.
9.2.7.13.6. LatestEndTime Field
This field SHALL indicate the latest end time, in UTC, for the entire Forecast.
e.g. for an EVSE charging session, this may indicate the departure time for the vehicle, by which
time the charging session must end.
9.2.7.13.7. IsPausable Field
This field SHALL indicate that some part of the Forecast can be paused. It aims to allow a client to
read this flag and if it is false, then none of the slots contain SlotIsPausable set to true. This can save
a client from having to check each slot in the list.
9.2.7.13.8. Slots Field
This field SHALL contain a list of SlotStructs.
It SHALL contain at least 1 entry, and a maximum of 10.
9.2.7.13.9. ForecastUpdateReason Field
This field SHALL contain the reason the current Forecast was generated.
9.2.7.14. SlotStruct Type
This indicates a specific stage of an ESA’s operation.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'MinDuration'. It is of the type 'elapsed-s', which likely indicates that it represents a duration measured in elapsed seconds. The 'Constraint' field is marked as 'all', suggesting that this data type applies universally within its context. The 'Conformance' field is marked with 'M', which, according to the Matter Conformance Interpretation Guide, means that the 'MinDuration' element is mandatory. This implies that the 'MinDuration' data type must always be implemented and supported within the Device Energy Management Cluster, with no exceptions or conditions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '1' and is named 'MaxDuration'. It is of the type 'elapsed-s', which likely indicates a measurement of elapsed time in seconds. The constraint 'all' suggests that this data type applies universally within its context. The conformance rule for 'MaxDuration' is marked as 'M', meaning it is mandatory. This indicates that the 'MaxDuration' data type is a required element in the Device Energy Management Cluster and must be implemented in all instances of this cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'DefaultDuration'. It is of the type 'elapsed-s', which likely refers to a time duration measured in seconds. The 'Constraint' field is marked as 'all', suggesting that this data type applies universally within its context. The 'Conformance' field is marked with 'M', indicating that the 'DefaultDuration' element is mandatory. This means that it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an element within the Device Energy Management Cluster, specifically under the Data Types section. The element is identified by the ID '3' and is named 'ElapsedSlotTime', with a data type of 'elapsed-s'. The 'Constraint' is listed as 'all', indicating that this element applies universally within its context. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'ElapsedSlotTime' element is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '4' and is named 'RemainingSlotTime'. It is of the type 'elapsed-s', which likely indicates a measurement in elapsed seconds, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'RemainingSlotTime' element is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row entry pertains to the "SlotIsPausable" attribute within the Device Energy Management Cluster, specifically under the Data Types section. This attribute is of the boolean type, indicating it can hold a true or false value, and it applies universally without specific constraints. The conformance rule for "SlotIsPausable" is denoted as "PAU," which implies that this attribute is mandatory if the feature "PAU" is supported. In simpler terms, if a device supports the "PAU" feature, it must include the "SlotIsPausable" attribute; otherwise, there is no requirement for this attribute to be present.

* In the context of the Device Energy Management Cluster, the table row describes a data type named "MinPauseDuration" with an ID of '6' and a type of 'elapsed-s', indicating it measures elapsed time in seconds. The constraint 'all' suggests it applies universally within its context. The conformance rule 'PAU' indicates that the "MinPauseDuration" element is currently in a provisional state, meaning its status is temporary and subject to change. The 'P' suggests that while it is not mandatory at this moment, it is intended to become mandatory in the future as the specification evolves.

* The table row entry for 'MaxPauseDuration' in the Device Energy Management Cluster under the Data Types section indicates that this element has an ID of '7' and is of the type 'elapsed-s', which suggests it measures time in seconds. The 'Constraint' being 'all' implies that there are no specific restrictions on its use across different implementations. The 'Conformance' field is marked as 'PAU', which, according to the Matter Conformance Interpretation Guide, suggests that the element is currently in a Provisional state. This means that while it is not yet mandatory, it is intended to become mandatory in the future. Therefore, developers should anticipate that 'MaxPauseDuration' will eventually be a required element in the Device Energy Management Cluster, and they should prepare for its mandatory implementation in upcoming updates of the specification.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '8' and is named 'ManufacturerESAState', which is of type 'uint16', indicating it is a 16-bit unsigned integer. The constraint 'all' suggests that this data type is applicable universally within its context. The conformance field 'SFR' is not directly explained by the provided conformance interpretation guide, indicating that 'SFR' might be a specific feature code or condition relevant to this context. Without additional documentation explaining 'SFR', it is unclear whether this element is mandatory, optional, or subject to other conditions. Therefore, further reference to the specific Matter specification or related documentation would be necessary to fully understand the conformance requirements for 'ManufacturerESAState'.

* The table row describes an element within the Device Energy Management Cluster, specifically under the Data Types section. The element is identified by the ID '9' and is named 'NominalPower', with a data type of 'power-mW' and a constraint applicable to 'all'. The conformance rule for 'NominalPower' is 'PFR', which indicates that this element is currently in a provisional state. This means that its status is temporary and subject to change in future revisions of the specification. The conformance does not specify any immediate mandatory, optional, or deprecated status, but it suggests that the element's requirements may be clarified or altered in subsequent updates to the Matter specification.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "MinPower" attribute within the Device Energy Management Cluster, specifically under the Data Types section. This attribute is identified by the ID '10' and is of the type 'power-mW', with a constraint applicable to all instances. The conformance rule for "MinPower" is denoted as 'PFR', which indicates that the attribute is currently in a Provisional state. This means that while it is not yet mandatory, it is expected to become a required element in future iterations of the specification. The provisional status suggests that implementers should be prepared for this attribute to transition to a mandatory requirement, although it is not obligatory at this moment.

* The table row entry describes an element within the Device Energy Management Cluster, specifically in the Data Types section, with the ID '11' and the name 'MaxPower'. This element is of the type 'power-mW' and is constrained to 'all', indicating it applies universally within the specified context. The conformance rule for 'MaxPower' is 'PFR', which means it is currently in a Provisional state. This suggests that while the element is not yet mandatory, it is expected to become mandatory in the future, as indicated by the typical usage of 'P' followed by another conformance tag. However, since 'PFR' does not directly follow the standard conformance tags outlined in the guide, it might imply a specific provisional status that requires further clarification in the broader documentation.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '12' and is named 'NominalEnergy'. It is of the type 'energy- mWh', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance field is marked as 'PFR', which suggests that the 'NominalEnergy' element is currently in a provisional state. This means that while it is not yet mandatory, it is intended to become mandatory in the future. The provisional status indicates that users should prepare for its eventual mandatory implementation, even though it is not required at this moment.

* In the Device Energy Management Cluster, under the Data Types section, the entry with ID '13' refers to a data type named 'Costs', which is a list of 'CostStruct' with a maximum constraint of 5 elements. The conformance rule for this entry is 'O', indicating that the 'Costs' data type is optional. This means that the implementation of this data type is not required and does not depend on any other features or conditions. Implementers have the flexibility to include or exclude this element based on their specific needs or preferences without any mandatory obligation.

* The table row entry describes a data type named 'MinPowerAdjustment' within the Device Energy Management Cluster, specifically under the Data Types section. This data type is of the type 'power-mW' and applies universally as indicated by the 'Constraint' being 'all'. The 'Conformance' field is expressed as 'FA & PFR', which means that the 'MinPowerAdjustment' element is mandatory if both the features 'FA' and 'PFR' are supported. In other words, for a device implementing the Device Energy Management Cluster, the 'MinPowerAdjustment' data type must be included if the device supports both the 'FA' and 'PFR' features.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '15' and is named 'MaxPowerAdjustment'. It is of the type 'power-mW' and applies universally, as indicated by the 'Constraint' being 'all'. The 'Conformance' field for this entry is 'FA & PFR', which means that the 'MaxPowerAdjustment' element is mandatory if both the features 'FA' and 'PFR' are supported by the device. In other words, the presence of this data type is required only when both these specific features are available, ensuring that the device can adjust its maximum power usage in accordance with these features.

* The table row entry pertains to the "MinDurationAdjustment" data type within the Device Energy Management Cluster, specifically under the Data Types section. This data type is identified by the ID '16' and is of the type 'elapsed-s', which likely indicates it measures elapsed time in seconds. The constraint 'all' suggests that this data type applies universally within its context. The conformance rule 'FA' indicates that the "MinDurationAdjustment" is mandatory if the feature 'FA' is supported. In other words, if a device or implementation supports the feature labeled 'FA', then it must include the "MinDurationAdjustment" data type. If 'FA' is not supported, the conformance rule does not apply, and the requirement for this data type is not specified in this entry.

* The table row entry describes a data type within the Device Energy Management Cluster, specifically named "MaxDurationAdjustment" with an ID of '17'. This data type is of the type 'elapsed-s', which likely represents a duration measured in seconds. The constraint 'all' suggests that this data type applies universally within its context. The conformance rule 'FA' indicates that the "MaxDurationAdjustment" element is mandatory if the feature or condition represented by 'FA' is supported. In other words, if the system or device supports the feature 'FA', then the "MaxDurationAdjustment" data type must be implemented. If 'FA' is not supported, the conformance rule does not specify any alternative, implying that the element is not required in that case.

9.2.7.14.1. MinDuration Field
This field SHALL indicate the minimum time (in seconds) that the appliance expects to be in this
slot for.
9.2.7.14.2. MaxDuration Field
This field SHALL indicate the maximum time (in seconds) that the appliance expects to be in this
slot for.
9.2.7.14.3. DefaultDuration Field
This field SHALL indicate the expected time (in seconds) that the appliance expects to be in this slot
for.
9.2.7.14.4. ElapsedSlotTime Field
This field SHALL indicate the time (in seconds) that has already elapsed whilst in this slot. If the slot
has not yet been started, then it SHALL be 0. Once the slot has been completed, then this reflects
how much time was spent in this slot.
When subscribed to, a change in this field value SHALL NOT cause the Forecast attribute to be
updated since this value may change every 1 second.
When the Forecast attribute is read, then this value SHALL be the most recent value.
9.2.7.14.5. RemainingSlotTime Field
This field SHALL indicate the time (in seconds) that is estimated to be remaining.
Note that it may not align to the DefaultDuration - ElapsedSlotTime since an appliance may have
revised its planned operation based on conditions.
When subscribed to, a change in this field value SHALL NOT cause the Forecast attribute to be
updated, since this value may change every 1 second.
Note that if the ESA is currently paused, then this value SHALL NOT change.
When the Forecast attribute is read, then this value SHALL be the most recent value.
9.2.7.14.6. SlotIsPausable Field
This field SHALL indicate whether this slot can be paused.
9.2.7.14.7. MinPauseDuration Field
This field SHALL indicate the shortest period that the slot can be paused for. This can be set to avoid
controllers trying to pause ESAs for short periods and then resuming operation in a cyclic fashion
which may damage or cause excess energy to be consumed with restarting of an operation.
9.2.7.14.8. MaxPauseDuration Field
This field SHALL indicate the longest period that the slot can be paused for.
9.2.7.14.9. ManufacturerESAState Field
This field SHALL indicate a manufacturer defined value indicating the state of the ESA.
This may be used by an observing EMS which also has access to the metering data to ascertain the
typical power drawn when the ESA is in a manufacturer defined state.
Some appliances, such as smart thermostats, may not know how much power is being drawn by the
HVAC system, but do know what they have asked the HVAC system to do.
Manufacturers can use this value to indicate a variety of states in an unspecified way. For example,
they may choose to use values between 0-100 as a percentage of compressor modulation, or could
use these values as Enum states meaning heating with fan, heating without fan etc.
NOTE An ESA SHALL always use the same value to represent the same operating state.
By providing this information a smart EMS may be able to learn the observed power draw when
the ESA is put into a specific state. It can potentially then use the ManufacturerESAState field in the
Forecast attribute along with observed power drawn to predict the power draw from the appliance
and potentially ask it to modify its timing via one of the adjustment request commands, or adjust
other ESAs power to compensate.
9.2.7.14.10. NominalPower Field
This field SHALL indicate the expected power that the appliance will use during this slot. It may be
considered the average value over the slot, and some variation from this would be expected (for
example, as it is ramping up).
9.2.7.14.11. MinPower Field
This field SHALL indicate the lowest power that the appliance expects to use during this slot. (e.g.
during a ramp up it may be 0W).
Some appliances (e.g. battery inverters which can charge and discharge) may have a negative
power.
9.2.7.14.12. MaxPower Field
This field SHALL indicate the maximum power that the appliance expects to use during this slot.
(e.g. during a ramp up it may be 0W). This field ignores the effects of short-lived inrush currents.
Some appliances (e.g. battery inverters which can charge and discharge) may have a negative
power.
9.2.7.14.13. NominalEnergy Field
This field SHALL indicate the expected energy that the appliance expects to use or produce during
this slot.
Some appliances (e.g. battery inverters which can charge and discharge) may have a negative
energy.
9.2.7.14.14. Costs Field
This field SHALL indicate the current estimated cost for operating.
For example, if the device has access to an Energy pricing server it may be able to use the tariff to
estimate the cost of energy for this slot in the power forecast.
When an Energy Management System requests a change in the schedule, then the device MAY sug
gest a change in the cost as a result of shifting its energy. This can allow a demand side response
service to be informed of the relative cost to use energy at a different time.
The Costs field is a list of CostStruct structures which allows multiple CostTypeEnum and Values to
be shared by the energy appliance. These could be based on GHG emissions, comfort value for the
consumer etc.
For example, comfort could be expressed in abstract units or in currency. A water heater that is
heated earlier in the day is likely to lose some of its heat before it is needed, which could require a
top-up heating event to occur later in the day (which may incur additional cost).
If the ESA cannot calculate its cost for any reason (such as losing its connection to a Price server) it
may omit this field. This is treated as extra meta data that an EMS may use to optimize a system.
9.2.7.14.15. MinPowerAdjustment Field
This field SHALL indicate the minimum power that the appliance can be requested to use.
For example, some EVSEs cannot be switched on to charge below 6A which may equate to ~1.3kW
in EU markets. If the slot indicates a NominalPower of 0W (indicating it is expecting to be off), this
allows an ESA to indicate it could be switched on to charge, but this would be the minimum power
limit it can be set to.
9.2.7.14.16. MaxPowerAdjustment Field
This field SHALL indicate the maximum power that the appliance can be requested to use.
For example, an EVSE may be limited by its electrical supply to 32A which would be ~7.6kW in EU
markets. If the slot indicates a NominalPower of 0W (indicating it is expecting to be off), this allows
an ESA to indicate it could be switched on to charge, but this would be the maximum power limit it
can be set to.
9.2.7.14.17. MinDurationAdjustment Field
This field SHALL indicate the minimum time, in seconds, that the slot can be requested to short
ened to.
For example, if the slot indicates a NominalPower of 0W (indicating it is expecting to be off), this
would allow an ESA to specify the minimum time it could be switched on for. This is to help protect
the appliance from being damaged by short cycling times.
For example, a heat pump compressor may have a minimum cycle time of order a few minutes.
9.2.7.14.18. MaxDurationAdjustment Field
This field SHALL indicate the maximum time, in seconds, that the slot can be requested to extended
to.
For example, if the slot indicates a NominalPower of 0W (indicating it is expecting to be off), this
allows an ESA to specify the maximum time it could be switched on for. This may allow a battery or
water heater to indicate the maximum duration that it can charge for before becoming full. In the
case of a battery inverter which can be discharged, it may equally indicate the maximum time the
battery could be discharged for (at the MaxPowerAdjustment power level).
9.2.7.15. SlotAdjustmentStruct Type

_Table parsed from section 'Data Types':_

* The table row entry describes a data type within the Device Energy Management Cluster, specifically named "SlotIndex" with an ID of '0'. This data type is of the type 'uint8', which means it is an unsigned 8-bit integer. The 'Constraint' field is marked as 'desc', indicating that the constraints for this data type are detailed elsewhere in the documentation and are too complex to be summarized in a simple expression. The 'Conformance' field is marked as 'M', which signifies that the "SlotIndex" data type is mandatory. This means that it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '1' and is named 'NominalPower', which is of the type 'power-mW'. The constraint for this entry is described elsewhere in the documentation, as indicated by 'desc'. The conformance for 'NominalPower' is marked as 'PFR', which means it is currently in a Provisional state. This suggests that while the element is not yet mandatory, it is intended to become mandatory in the future, following the Matter specification's evolution. The 'PFR' tag indicates that this status is temporary and subject to change, highlighting the importance of monitoring updates to the specification for any changes in its conformance requirements.

* In the context of the Device Energy Management Cluster, the table entry for the data type 'Duration' with ID '2' is defined as having the type 'elapsed-s', which likely refers to a measurement of time in elapsed seconds. The 'Constraint' is marked as 'desc', indicating that specific constraints or conditions for this data type are detailed elsewhere in the documentation. The 'Conformance' is labeled as 'M', which means that this data type is mandatory. This implies that the 'Duration' data type must always be implemented and supported within the Device Energy Management Cluster, without any conditions or exceptions.

9.2.7.15.1. SlotIndex Field
This field SHALL indicate the index into the Slots list within the Forecast that is to be modified. It
SHALL be less than the actual length of the Slots list (implicitly it must be in the range 0 to 9 based
on the maximum length of the Slots list constraint).
9.2.7.15.2. NominalPower Field
This field SHALL indicate the new requested power that the ESA SHALL operate at. It MUST be
PFR
between the AbsMinPower and AbsMaxPower attributes as advertised by the ESA if it supports  .
This is a signed value and can be used to indicate charging or discharging.
PFR
If the ESA does NOT support   this value SHALL be ignored by the ESA.
9.2.7.15.3. Duration Field
This field SHALL indicate the new requested duration, in seconds, that the ESA SHALL extend or
shorten the slot duration to. It MUST be between the MinDurationAdjustment and MaxDurationAd
justment for the slot as advertised by the ESA.
9.2.7.16. ConstraintsStruct Type
The ConstraintsStruct allows a client to inform an ESA about a constraint period (such as a grid
event, or perhaps excess solar PV). The format allows the client to suggest that the ESA can either
turn up its energy consumption, or turn down its energy consumption during this period.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Device Energy Management Cluster, specifically in the Data Types section. The element is identified by the ID '0' and is named 'StartTime'. It is of the type 'epoch-s', which likely refers to a time format based on seconds since a specific epoch. The 'Constraint' field is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M', meaning that the 'StartTime' element is mandatory. This implies that it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is for an element named "Duration," which is of the type "elapsed-s" and has a constraint limiting its maximum value to 86,400 seconds (equivalent to 24 hours). The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Duration" element is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an entry within the Device Energy Management Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'NominalPower', which is of the type 'power-mW'. The constraint for this entry is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'NominalPower' is 'PFR', which means it is currently in a Provisional status. This suggests that while the element is not yet mandatory, it is intended to become mandatory in the future. The conformance does not specify any additional conditions or dependencies, indicating that the transition to mandatory status is planned but not yet finalized.

* The table row entry pertains to the "MaximumEnergy" data type within the Device Energy Management Cluster, specifically under the Data Types section. This data type is identified by the ID '3' and is measured in milliWatt-hours (mWh), with a constraint applicable to all instances. The conformance rule for "MaximumEnergy" is denoted as 'PFR', which indicates that its current status is provisional. This means that while it is not yet mandatory, it is expected to become mandatory in the future. The conformance does not specify any complex conditions or dependencies, suggesting that the provisional status is straightforward and not contingent on other features or elements.

* The table row entry pertains to the "LoadControl" data type within the Device Energy Management Cluster, specifically under the Data Types section. The "LoadControl" is identified by the ID '4' and is of type 'int8', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for "LoadControl" is specified as 'SFR'. According to the Matter Conformance Interpretation Guide, 'SFR' is not a standard conformance tag or expression as outlined in the guide. Therefore, it may represent a specific condition or requirement described elsewhere in the documentation, possibly indicating a specialized or situational conformance rule that needs further clarification from additional documentation sources.

9.2.7.16.1. StartTime Field
This field SHALL indicate the start time of the constraint period that the client wishes the ESA to
compute a new Forecast.
This value is in UTC and MUST be in the future.
9.2.7.16.2. Duration Field
This field SHALL indicate the duration of the constraint in seconds.
9.2.7.16.3. NominalPower Field
This field SHALL indicate the nominal power that client wishes the ESA to operate at during the
constrained period. It MUST be between the AbsMinPower and AbsMaxPower attributes as adver
PFR
tised by the ESA if it supports  .
This is a signed value and can be used to indicate charging or discharging.
9.2.7.16.4. MaximumEnergy Field
This field SHALL indicate the maximum energy that can be transferred to or from the ESA during
the constraint period.
This is a signed value and can be used to indicate charging or discharging.
9.2.7.16.5. LoadControl Field
This field SHALL indicate the turn up or turn down nature that the grid wants as the outcome by
the ESA during the constraint period.
This is expressed as a signed value between -100 to +100. A value of 0 would indicate no bias to
using more or less energy. A negative value indicates a request to use less energy. A positive value
indicates a request to use more energy.
Note that the mapping between values and operation is manufacturer specific.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Device Energy Management Cluster, specifically the 'ESAType' attribute. This attribute is identified by the ID '0x0000' and is of the type 'ESATypeEnum'. It applies to all instances of the cluster ('Constraint': 'all') and has a default value of 'Other'. The attribute is read-only and volatile ('Access': 'R V'), and it is marked with a quality of 'F'. The conformance rule 'M' indicates that the 'ESAType' attribute is mandatory, meaning it is always required to be implemented in any device that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named `ESACanGenerate` within the Device Energy Management Cluster, specifically in the Attributes section. This attribute has an ID of `0x0001` and is of type `bool`, meaning it can hold a true or false value. The constraint 'all' suggests that this attribute applies universally within its context. It has a quality designation of 'F', a default value of 'false', and access permissions of 'R V', indicating it is readable and can be viewed. The conformance rule for `ESACanGenerate` is marked as 'M', which means this attribute is mandatory. It is always required to be implemented in any device that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, within the Attributes section, the table row describes an attribute identified by 'ID' 0x0002, named 'ESAState', which is of the type 'ESAStateEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The default value for this attribute is '0', and it has 'Read' and 'View' access permissions, as denoted by 'R V'. The 'Conformance' field is marked as 'M', meaning that the 'ESAState' attribute is mandatory and must always be implemented in any device that supports this cluster. This requirement is unconditional and does not depend on any other features or conditions.

* The table row describes an attribute within the Device Energy Management Cluster, specifically the "AbsMinPower" attribute. This attribute has an ID of '0x0003' and is of the type 'power-mW', indicating it measures power in milliwatts. The 'Constraint' is listed as 'all', suggesting it applies universally across all relevant devices or contexts. The default value for this attribute is '0', and it has 'R V' access, meaning it is readable and has a volatile characteristic. The 'Conformance' is marked as 'M', which, according to the Matter Conformance Interpretation Guide, means that this attribute is mandatory. Therefore, it is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Device Energy Management Cluster, specifically the "AbsMaxPower" attribute. This attribute has an ID of '0x0004' and is of the type 'power-mW', indicating it measures power in milliwatts. The attribute is constrained to have a minimum value equal to 'AbsMinPower', and it defaults to '0'. The access level is 'R V', meaning it is readable and may have volatile data. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "AbsMaxPower" attribute is always required to be implemented in any device that supports the Device Energy Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "PowerAdjustmentCapability" within the Device Energy Management Cluster, identified by the ID '0x0005'. This attribute is of the type 'PowerAdjustCapabilityStruct' and is constrained to apply to all instances. The quality 'X Q' indicates that it is disallowed and has a quality constraint, while the default value is 'null'. The access level 'R V' suggests it is readable and has volatile characteristics. The conformance rule 'PA' indicates that the attribute is currently provisional, meaning its status is temporary and may change in the future. Specifically, it is expected to become mandatory later, as indicated by the 'P, M' notation.

* The table row describes an attribute named "Forecast" within the Device Energy Management Cluster, identified by the ID '0x0006'. This attribute is of the type 'ForecastStruct' and is constrained to apply to all relevant contexts. Its quality is marked as 'X Q', indicating it is disallowed in certain contexts, and its default value is 'null'. The access level is 'R V', meaning it is readable and has volatile characteristics. The conformance rule 'PFR | SFR' indicates that the "Forecast" attribute is mandatory if either the PFR (Primary Forecast Requirement) or SFR (Secondary Forecast Requirement) feature is supported. In other words, the attribute must be implemented if at least one of these features is present.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "OptOutState" within the Device Energy Management Cluster, identified by the ID '0x0007'. This attribute is of the type 'OptOutStateEnum' and has a default value of '0'. It is constrained by a description found elsewhere in the documentation and has read and view access ('R V'). The conformance rule 'PA | STA | PAU | FA | CON' indicates that the "OptOutState" attribute is mandatory if any one of the features PA (Power Awareness), STA (Scheduled Time Awareness), PAU (Power Awareness Update), FA (Feature Awareness), or CON (Connectivity) is supported. If at least one of these features is present, the attribute must be implemented.

9.2.8.1. ESAType Attribute
This attribute SHALL indicate the type of ESA.
This attribute enables an EMS to understand some of the basic properties about how the energy
may be consumed, generated, and stored by the ESA.
For example, the heat energy converted by a heat pump will naturally be lost through the building
to the outdoor environment relatively quickly, compared to storing heat in a well-insulated hot
water tank. Similarly, battery storage and EVs can store electrical energy for much longer dura
tions.
This attribute can also help the EMS display information to a user and to make basic assumptions
about typical best use of energy. For example, an EVSE may not always have an EV plugged in, so
knowing the type of ESA that is being controlled can allow advanced energy management strate
gies.
9.2.8.2. ESACanGenerate Attribute
This attribute SHALL indicate whether the ESA is classed as a generator or load. This allows an EMS
to understand whether the power values reported by the ESA need to have their sign inverted
when dealing with forecasts and adjustments.
For example, a solar PV inverter (being a generator) may produce negative values to indicate gener
ation (since power is flowing out of the node into the home), however a display showing the power
to the consumers may need to present a positive solar production value to the consumer.
For example, a home battery storage system (BESS) which needs to charge the battery and then dis
charge to the home loads, would be classed as a generator. These types of devices SHALL have this
field set to true. When generating its forecast or advertising its PowerAdjustmentCapability, the
power values shall be negative to indicate discharging to the loads in the home, and positive to indi
cate when it is charging its battery.
GRID meter = Σ LoadPowers + Σ GeneratorPowers
Example:

_Table parsed from section 'Attributes':_

* In the context of the Device Energy Management Cluster, under the section for Attributes, the entry 'Home has the following loads: Water Heater:' refers to an attribute that specifies whether a water heater is part of the home's energy management system. The conformance rule for this attribute is not explicitly provided in the table row data you've shared. However, if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would describe the conditions under which this attribute is required, optional, or otherwise specified. For example, if the conformance were 'M', it would mean that the inclusion of the water heater attribute is mandatory for all devices implementing this cluster. If it were 'O', it would be optional, allowing for flexibility depending on the specific implementation or device capabilities. Without the specific conformance string, we can only generalize based on typical usage within the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Attributes section, the entry 'Home has the following loads:' with the specific load 'TV:' pertains to the identification or listing of energy-consuming devices within a home. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance rule using the provided guide, it would describe the conditions under which this attribute (the presence of a TV as a load) is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean that listing the TV as a load is always mandatory. If it were 'O', it would be optional, meaning the TV does not need to be listed unless desired. Without a specific conformance string, we can only infer that this entry is part of a broader framework for managing and monitoring energy loads within a smart home environment, potentially allowing for more efficient energy use and management.

* In the context of the Device Energy Management Cluster, under the Attributes section, the entry 'FridgeFreezer' refers to a specific attribute that indicates whether a home has a fridge-freezer load. The conformance rule for this attribute is not explicitly given in the provided data, but based on the Matter Conformance Interpretation Guide, we would interpret any conformance string associated with it to determine its requirement status. For example, if the conformance was `M`, it would mean that the 'FridgeFreezer' attribute is mandatory for all devices implementing this cluster. If it were `O`, it would be optional, allowing for flexibility in implementation. Without a specific conformance string provided, we cannot definitively state its requirement status, but the guide would be used to interpret any such string if it were available.

3400W

_Table parsed from section 'Attributes':_

* The table row entry pertains to the "Device Energy Management Cluster" within the "Attributes" section, specifically focusing on the attribute related to home energy generation capabilities. The attribute in question is described as "Home has the following generators (ESACanGenerate = true): Solar: -2500W." This indicates that the attribute is concerned with the capability of a home to generate energy using solar power, with a specified capacity of -2500 watts. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the context, it likely involves conditions related to the presence of energy generation features (e.g., ESACanGenerate). If the attribute's conformance were to be expressed, it might involve conditions such as being mandatory if the home supports energy generation, optional if certain features are present, or deprecated if the feature is no longer supported. However, without a specific conformance string, we can only infer that the attribute is relevant when the home has solar generation

* The table row entry pertains to the "Device Energy Management Cluster" within the "Attributes" section. It describes an attribute related to the energy management capabilities of a home, specifically focusing on the presence of home generators and their energy generation status. The conformance rule for this attribute is not explicitly provided in the given data snippet, but based on the context, it likely involves conditions related to the presence of energy storage systems (BESS) and their ability to generate power, indicated by the "-900W" value. This suggests that the attribute may be conditionally required or optional based on whether the home has energy storage systems capable of generating power. Without a specific conformance string, further details would be needed to determine the exact conformance requirements.

* The table row from the Device Energy Management Cluster, specifically within the Attributes section, describes an attribute related to the energy generation capabilities of a home. The attribute indicates the total energy generation capacity, which in this case is specified as '-3400W'. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the context, it likely involves conditions related to the presence of energy generation features in the home. If the conformance were to follow the Matter Conformance Interpretation Guide, it might specify conditions under which this attribute is mandatory, optional, or otherwise, depending on the support for specific energy management features or configurations within the home. However, without a clear conformance string, we can only infer that this attribute is relevant when energy generation is a factor in the device's operation.

-2500W
-900W
-3400W

_Table parsed from section 'Attributes':_

* In the context of the Device Energy Management Cluster, specifically within the Attributes section, the table row entry labeled 'GRID Meter:' with the attribute 'Σ Loads:' pertains to the measurement or reporting of the total loads connected to the grid. The conformance rule for this attribute is not explicitly provided in the data snippet, but if we were to interpret a typical conformance expression, it would dictate the conditions under which this attribute is required, optional, or otherwise specified. For instance, if the conformance were `M`, it would mean that the 'Σ Loads:' attribute is always mandatory for devices implementing the GRID Meter feature. If the conformance were `O`, it would indicate that this attribute is optional and can be implemented at the discretion of the device manufacturer. Without a specific conformance expression provided, we can only infer that the attribute's inclusion depends on the broader conformance rules applicable to the Device Energy Management Cluster.

* In the context of the Device Energy Management Cluster, specifically within the Attributes section, the table row entry for 'GRID Meter:' with the attribute 'Σ Generators:' pertains to the capability of a device to report or manage the cumulative energy generation from multiple generators connected to the grid. The conformance rule for this attribute is not explicitly provided in the data snippet, but if we were to interpret a typical conformance scenario, it might involve conditions under which this attribute is mandatory, optional, or otherwise specified based on the presence or absence of certain features or conditions. For instance, if the conformance were something like `GRID, O`, it would mean that the 'Σ Generators:' attribute is mandatory if the GRID feature is supported; otherwise, it is optional. Without the specific conformance string, we can only infer that the attribute's inclusion and behavior are determined by the rules outlined in the Matter Conformance Interpretation Guide, which would dictate its necessity based on the device's supported features and configurations.

* The table row entry pertains to the "GRID Meter" attribute within the "Device Energy Management Cluster" under the "Attributes" section. The conformance rule for this attribute is not explicitly provided in the data snippet. However, if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would specify the conditions under which the "GRID Meter" attribute is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance string were "AB, O," it would mean that the "GRID Meter" attribute is mandatory if the feature "AB" is supported; otherwise, it is optional. Without the specific conformance string, we cannot determine the exact requirement status of the "GRID Meter" attribute.

3400W
-3400W
0W
9.2.8.3. ESAState Attribute
This attribute SHALL indicate the current state of the ESA.
If the ESA is in the Offline or Fault state it cannot be controlled by an EMS, and may not be able to
report its Forecast information. An EMS may subscribe to the ESAState to get notified about changes
in operational state.
The ESA may have a local user interface to allow a service technician to put the ESA into Offline
mode, for example to avoid the EMS accidentally starting or stopping the appliance when it is being
serviced or tested.
9.2.8.4. AbsMinPower Attribute
This attribute SHALL indicate the minimum electrical power that the ESA can consume when
switched on. This does not include when in power save or standby modes.
For Generator ESAs that can discharge an internal battery (such as a battery storage
NOTE inverter) to loads in the home, the AbsMinPower will be a negative number repre
senting the maximum power that the ESA can discharge its internal battery.
9.2.8.5. AbsMaxPower Attribute
This attribute SHALL indicate the maximum electrical power that the ESA can consume when
switched on.
Note that for Generator ESAs that can charge a battery by importing power into the node (such as a
battery storage inverter), the AbsMaxPower will be a positive number representing the maximum
power at which the ESA can charge its internal battery.
For example, a battery storage inverter that can charge its battery at a maximum power of 2000W
and can discharge the battery at a maximum power of 3000W, would have a AbsMinPower: -3000,
AbsMaxPower: 2000W.
9.2.8.6. PowerAdjustmentCapability Attribute
This attribute SHALL indicate how the ESA can be adjusted at the current time, and the state of any
active adjustment.
A null value indicates that no power adjustment is currently possible, and nor is any adjustment
currently active.
This attribute SHOULD be updated periodically by ESAs to reflect any changes in internal state, for
example temperature or stored energy, which would affect the power or duration limits.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once every 10 seconds on changes, or
• When it changes from null to any other value and vice versa.
9.2.8.7. Forecast Attribute
This attribute allows an ESA to share its intended forecast with a client (such as an Energy Manage
ment System).
A null value indicates that there is no forecast currently available (for example, a program has not
yet been selected by the user).
A server MAY reset this value attribute to null on a reboot, and it does not need to persist any previ
ous forecasts.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once every 10 seconds on changes, or
• When it changes from null to any other value and vice versa, or
• As a result of a command which causes the forecast to be updated, or
• As a result of a change in the opt-out status which in turn may cause the ESA to recalculate its
forecast.
9.2.8.8. OptOutState Attribute
This attribute SHALL indicate the current Opt-Out state of the ESA. The ESA may have a local user
interface to allow the user to control this OptOutState. An EMS may subscribe to the OptOutState to
get notified about changes in operational state.
If the ESA is in the LocalOptOut or OptOut states, so it cannot be controlled by an EMS for local opti
mization reasons, it SHALL reject any commands which have the AdjustmentCauseEnum value
LocalOptimization. If the ESA is in the GridOptOut or OptOut states, so it cannot be controlled by an
EMS for grid optimization reasons, it SHALL reject any commands which have the Adjustment
CauseEnum value GridOptimization.
If the user changes the Opt-Out state of the ESA which is currently operating with a Forecast that is
due to a previous StartTimeAdjustRequest, ModifyForecastRequest or RequestConstraintBasedFore
cast command that would now not be permitted due to the new Opt-out state (i.e. the Forecast
attribute ForecastUpdateReason field currently contains a reason which is now opted out), the ESA
SHALL behave as if it had received a CancelRequest command.
If the user changes the Opt-Out state of the ESA which currently has the ESAStateEnum with value
Paused
due to a previous PauseRequest command that would now not be permitted due to the new
PFR SFR
Opt-out state, and the ESA supports the   or   features (i.e. the Forecast attribute ForecastUp
dateReason field currently contains a reason which is now opted out), the ESA SHALL behave as if it
had received a ResumeRequest command.
If the user changes the Opt-Out state of the ESA which currently has the ESAStateEnum with value
PowerAdjustActive
due to a previous PowerAdjustRequest command that would now not be permit
ted due to the new Opt-out state (i.e. the Forecast attribute ForecastUpdateReason field currently
contains a reason which is now opted out), the ESA SHALL behave as if it had received a Can
celPowerAdjustRequest command.
If the ESA is in the LocalOptOut, GridOptOut, or NoOptOut states, the device is still permitted to
optimize its own energy usage, for example, using tariff information it may obtain.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Device Energy Management Cluster, specifically the "PowerAdjustRequest" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'PA' indicates that the command is currently in a provisional state ('P'), with the intention of becoming mandatory ('M') in the future. This means that while the command is not yet required, it is expected to become a mandatory feature in subsequent versions of the specification.

* The table row describes a command within the Device Energy Management Cluster, specifically the "CancelPowerAdjustRequest" command, which is directed from the client to the server. The command requires a response, as indicated by 'Response: Y', and has optional access permissions, denoted by 'Access: O'. The conformance rule 'PA' signifies that the command is currently in a provisional state, with the intention of becoming mandatory in the future. This means that while the command is not yet required, it is expected to become a mandatory part of the specification at a later date.

* The table row describes a command within the Device Energy Management Cluster, specifically the "StartTimeAdjustRequest" command, which is identified by the ID '0x02'. This command is sent from the client to the server, and it requires a response, as indicated by 'Response': 'Y'. The access level for this command is optional ('Access': 'O'), meaning it is not required and has no dependencies. The conformance rule 'STA' suggests that the command is mandatory if the feature code 'STA' is supported. In essence, if the 'STA' feature is part of the device's capabilities, the "StartTimeAdjustRequest" command must be implemented; otherwise, it is not required.

* The table row describes a command within the Device Energy Management Cluster, specifically the "PauseRequest" command, which is directed from the client to the server. The command requires a response, as indicated by 'Response: Y', and has optional access, denoted by 'Access: O'. The conformance rule 'PAU' suggests that the command's inclusion is conditional based on the support of the feature 'PAU'. If the feature 'PAU' is supported, the "PauseRequest" command is mandatory. If 'PAU' is not supported, the command is not required. This means that the implementation of this command depends on whether the device supports the 'PAU' feature, making it a conditional requirement.

* The table row describes a command called "ResumeRequest" within the Device Energy Management Cluster, specifically in the context of commands sent from a client to a server. The command has an ID of '0x04' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'PAU' indicates that the command is currently provisional ('P'), suggesting that its status is temporary and may change in the future. The 'A' and 'U' in the conformance string do not correspond to any standard conformance tags as per the provided guide, which might imply a need for further clarification or context from the documentation. Overall, the "ResumeRequest" command is not mandatory at present, and its future status is uncertain, pending further specification updates.

* The table row describes a command within the Device Energy Management Cluster, specifically the "ModifyForecastRequest" command, which is directed from the client to the server and requires a response. The access level for this command is optional, meaning it is not required and has no dependencies. The conformance rule "FA" indicates that the command is mandatory if the feature represented by "FA" is supported. If "FA" is not supported, the command is not required. This means that the necessity of implementing this command depends on whether the specific feature "FA" is part of the device's capabilities.

* The table row describes a command within the Device Energy Management Cluster, specifically the "RequestConstraintBasedForecast" command, identified by the ID '0x06'. This command is sent from the client to the server and requires a response. The access level for this command is optional, indicated by 'O'. The conformance rule for this command is 'CON', which suggests that the requirement for this command is conditional and depends on specific conditions or features that are described elsewhere in the documentation. This means that the command's necessity is not straightforwardly mandatory or optional but instead relies on certain criteria being met, which are detailed in another part of the specification.

* The table row describes a command within the Device Energy Management Cluster, specifically the "CancelRequest" command, which is directed from the client to the server and requires a response. The access level for this command is optional, meaning it is not required and has no dependencies. The conformance rule "STA | FA | CON" indicates that the "CancelRequest" command is mandatory if any of the features STA (Standard), FA (Feature A), or CON (Condition) are supported. In other words, if a device supports any one of these features, it must implement the "CancelRequest" command. If none of these features are supported, the command is not required.

STA | FA | CON
9.2.9.1. PowerAdjustRequest Command
Allows a client to request an adjustment in the power consumption of an ESA for a specified dura
tion.

_Table parsed from section 'Commands':_

* In the Device Energy Management Cluster, within the Commands section, there is an entry for a command identified by 'ID' 0, named 'Power', with a type of 'power-mW'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the 'Power' command must always be implemented and supported in any device or system that adheres to the Matter specification for this cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, under the Commands section, the table row describes an element with the ID '1' named 'Duration'. This element is of the type 'elapsed-s', which likely refers to a time duration measured in seconds. The 'Constraint' is marked as 'desc', indicating that specific constraints or conditions for this element are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', meaning that the 'Duration' element is mandatory. This implies that it is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row describes a command with the ID '2' named 'Cause'. This command is of the type 'AdjustmentCauseEnum', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the 'Cause' command must always be implemented and supported in any device or application that adheres to this part of the Matter specification, without any conditions or exceptions.

9.2.9.1.1. Power Field
This field SHALL indicate the power that the ESA SHALL use during the adjustment period.
This value SHALL be between the MinPower and MaxPower fields of the PowerAdjustStruct in the
PowerAdjustmentCapability attribute.
9.2.9.1.2. Duration Field
This field SHALL indicate the duration that the ESA SHALL maintain the requested power for.
This value SHALL be between the MinDuration and MaxDuration fields of the PowerAdjustStruct in
the PowerAdjustmentCapability attribute.
9.2.9.1.3. Cause Field
This field SHALL indicate the cause of the request from the EMS.
9.2.9.1.4. Effect on receipt
On receipt of this command, the ESA SHALL validate that the Power and Duration specified in the
command are within the limits of its current operation and advertised PowerAdjustmentCapability
attribute,  the  OptOutState  permits  the  specified  AdjustmentCauseEnum  (see  OptOutState  for
details), and the ESAState is Online.
If the PowerAdjustRequest command is accepted, then the ESA SHALL change its ESAState to Pow
erAdjustActive, and the PowerAdjustmentCapability attribute SHALL be updated to set the Cause
value from the Cause field of this command.
The command status returned SHALL be SUCCESS if the adjustment is accepted; otherwise the com
mand SHALL be rejected with CONSTRAINT_ERROR if the Power, Duration, or Cause values are not
permitted as above, or with FAILURE otherwise.
Start of adjustment
The ESA SHALL generate a PowerAdjustStart Event when it begins to adjust its power.
The ESA then begins to adjust its power consumption or generation to the power level commanded
in the Power field.
End of adjustment (normal completion)
After the elapsed duration, the ESA SHALL revert to normal (or idle) power levels.
The ESA SHALL also generate a PowerAdjustEnd Event with a cause code to indicate a 'Normal
completion',  the  ESAState  SHALL  be  restored  to  Online,  and  the  PowerAdjustmentCapability
attribute SHALL be updated to set the Cause value to 'NoAdjustment'.
Failure or Opt-out during adjustment
If during the power adjustment session a failure or other condition occurs (such as the user decid
ing to opt-out by updating the OptOutState) then the ESA SHALL generate a PowerAdjustEnd Event
to indicate the end of the session, with the appropriate cause code.
The ESAState SHALL be updated to reflect the new state, and the PowerAdjustmentCapability
attribute SHALL be updated to set the Cause value to 'NoAdjustment'.
Receiving a new PowerAdjustRequest command when adjustment is on-going
If an existing power adjustment is already happening, and a new PowerAdjustRequest command is
received, then if the ESA allows it, the ESA SHALL return SUCCESS, and the PowerAdjustmentCapa
bility attribute SHALL be updated to set the Cause value from the Cause field of the new command.
If the ESA does not permit this new PowerAdjustmentRequest command to interrupt the adjust
ment that is in progress, it SHALL return BUSY.
Note that if the new command is accepted, then the ESA SHALL NOT generate a new PowerAdjus
tEnd Event until the new duration has elapsed. This is to avoid generating too many events in cases
where a device is routinely commanded with overlapping power adjustments.
For example, a battery inverter ESA may be sent a new request every 5 seconds to adjust its dis
charge power based on real-time meter readings. Each command may have a 60 second duration,
but this command is superseded after 5 seconds by a new request.
After the client has sent its last command and after this command duration expires then the last
active power adjustment has been completed. This final command causes the PowerAdjustEnd
Event to be generated when the ESAState is restored to Online, and the PowerAdjustmentCapability
attribute SHALL be updated to set the Cause value to 'NoAdjustment'.
9.2.9.2. CancelPowerAdjustRequest Command
Allows a client to cancel an ongoing PowerAdjustmentRequest operation.
9.2.9.2.1. Effect on receipt
On receipt of this command, the ESA SHALL end the active power adjustment session and return to
normal (or idle) power levels.
If the ESAState is not PowerAdjustActive, then the command SHALL be rejected with INVALID_IN_S
TATE.
If the command is accepted, the ESA SHALL generate an PowerAdjustEnd Event and the ESAState
SHALL be restored to Online, the PowerAdjustmentCapability attribute SHALL be updated to set the
Cause value to 'NoAdjustment', and the command status returned SHALL be SUCCESS.
9.2.9.3. StartTimeAdjustRequest Command
Allows a client to adjust the start time of a Forecast sequence that has not yet started operation (i.e.
where the current Forecast StartTime is in the future).

_Table parsed from section 'Commands':_

* The table row describes a command within the Device Energy Management Cluster, specifically the "RequestedStartTime" command. This command is identified by the ID '0' and uses the data type 'epoch-s', which likely refers to a timestamp format. The 'Constraint' is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', meaning that the "RequestedStartTime" command is mandatory. This implies that any implementation of the Device Energy Management Cluster must include this command as a required element, without any conditions or exceptions.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row describes a command identified by 'ID' 1, named 'Cause', which is of the type 'AdjustmentCauseEnum' and applies to all constraints. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'Cause' command is always required to be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

9.2.9.3.1. RequestedStartTime Field
This field SHALL indicate the requested start time, in UTC, that the client would like the appliance
to shift its Forecast to. This value MUST be in the future.
A client can estimate the entire Forecast sequence duration by computing the EndTime - StartTime
fields from the Forecast attribute, and therefore avoid scheduling the start time too late.
This value SHALL be after the EarliestStartTime in the Forecast attribute. The new EndTime, that
can be computed from the RequestedStartTime and the Forecast sequence duration, SHALL be
before the LatestEndTime.
9.2.9.3.2. Cause Field
This field SHALL indicate the cause of the request from the EMS.
9.2.9.3.3. Effect on receipt
STA
On receipt of this command, if the ESA supports  , and the OptOutState permits the specified
AdjustmentCauseEnum  (see  OptOutState  for  details),  and  the  RequestedStartTime  adjustment
would be within constraints described in RequestedStartTime then ESA SHALL accept the request
to modify the Start Time.
If the RequestedStartTime value resulted in a time shift which is outside the time constraints of Ear
liestStartTime and LatestEndTime, or the Cause is not permitted, then the command SHALL be
rejected with CONSTRAINT_ERROR; in other failure scenarios the command SHALL be rejected with
FAILURE.
The command status returned SHALL be SUCCESS if the StartTime in the Forecast is updated. The
ESA SHALL update its Forecast attribute using the new RequestedStartTime including a new Fore
castID, StartTime, EndTime, and ForecastUpdateReason.
9.2.9.4. PauseRequest Command
Allows a client to temporarily pause an operation and reduce the ESAs energy demand.

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, the table row describes a command named "Duration" with an ID of '0' and a type of 'elapsed-s'. The 'Constraint' is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' is labeled as 'M', which means that this command is mandatory. It must always be implemented and supported in any device or system that adheres to the Matter specification for this cluster. There are no conditions or dependencies affecting its mandatory status.

* The table row describes a command within the Device Energy Management Cluster, specifically identified by the ID '1' and named 'Cause'. This command is of the type 'AdjustmentCauseEnum' and applies universally, as indicated by the 'Constraint' being 'all'. The 'Conformance' field is marked as 'M', which, according to the Matter Conformance Interpretation Guide, signifies that this command is Mandatory. This means that the 'Cause' command must always be implemented in any device or application that supports the Device Energy Management Cluster, with no exceptions or conditions.

9.2.9.4.1. Duration Field
This field SHALL indicate the duration that the ESA SHALL be paused for. This value SHALL be
between the MinPauseDuration and MaxPauseDuration indicated in the ActiveSlotNumber index in
the Slots list in the Forecast.
9.2.9.4.2. Cause Field
This field SHALL indicate the cause of the request from the EMS.
9.2.9.4.3. Effect on receipt
PAU
On receipt of this command, if the ESA supports   and the SlotIsPausable field is true in the
ActiveSlotNumber  index  in  the  Slots  list,  the  OptOutState  permits  the  specified  Adjustment
CauseEnum (see OptOutState for details), and the OptOutState is Online or PowerAdjustActive, the
ESA SHALL allow its current operation to be Paused. If the Cause is not permitted, then the com
mand SHALL be rejected with CONSTRAINT_ERROR.
If the ESA SlotIsPausable field is false for the ActiveSlotNumber, then the command SHALL be
rejected with FAILURE.
The ESA SHALL validate that the Duration field is within the range of MinPauseDuration and Max
PauseDuration. If it is outside of this range then the command SHALL be rejected with CONSTRAIN
T_ERROR.
The command status returned SHALL be SUCCESS if the ESA is paused.
Once the command has been accepted, the ESA SHALL also generate a Paused Event and the ESAS
tate SHALL be set to Paused.
The ESA SHALL update its update its Forecast to account for the pause, including updating the Fore
castUpdateReason from the Cause field.
Pause timer start The ESA SHALL start a Pause timer based on the value of the Duration field.
Paused State Whilst in the Paused state, the ESA SHALL NOT consume or produce significant
power (other than required to keep its basic control system operational).
Pause timer expiry When the Pause timer expires the ESA SHALL automatically resume operation.
When it does this, then it SHALL also generate a Resumed Event and the ESAState SHALL be
updated accordingly to reflect its current state (for example, it may still have PowerAdjustActive
now it has resumed from the Pause). The ESA SHALL update its Forecast including setting Forecas
InternalOptimization
tUpdateReason to   to account for the resumption after the pause.
Receiving  a  further  pause  request  command  whilst  paused  If  a  further  Pause  Request  is
received in the same forecast slot whilst already in the paused state, the ESA SHALL again validate
that the Duration value is within the range of the (possibly revised) MinPauseDuration and Max
PauseDuration. If it is outside of this range then the command SHALL be rejected with CONSTRAIN
T_ERROR.
If the command is accepted the pause timer SHALL be extended by the new Duration.
ResumeRequest  A  client  MAY  send  a  ResumeRequest  command,  before  the  Pause  timer  has
expired, to request the ESA to return to its normal operating state. See ResumeRequest for details.
Failure or Opt-out during PauseRequest A consumer MAY decide to opt-out of the remotely com
manded PauseRequest by updating the OptOutState, and the ESA SHALL also change the ESAState
to the new state.
If the ESA develops a fault whilst Paused, the ESAState SHALL be set to Fault.
On change of ESAState (from Paused to another state), the ESA SHALL generate a Resumed Event.
9.2.9.5. ResumeRequest Command
Allows a client to cancel the PauseRequest command and enable earlier resumption of operation.
9.2.9.5.1. Effect on receipt
PAU
On receipt of this command, if the ESA supports   and it is currently Paused, the ESA MAY decide
not to resume immediately if the MinPauseDuration has not yet elapsed. This behavior is manufac
turer specific.
If accepted, the ESA SHALL resume its operation. The ESA SHALL also generate a Resumed Event
and the ESAState SHALL be updated accordingly to reflect its current state.
The command status returned SHALL be SUCCESS if the operation is resumed, or the command
SHALL be rejected with the response INVALID_IN_STATE if the ESA is not currently Paused, other
wise the command SHALL be rejected with FAILURE.
InternalOptimization
The ESA SHALL update its Forecast including setting ForecastUpdateReason to
to account for the resumption after the pause.
9.2.9.6. ModifyForecastRequest Command
Allows a client to modify a Forecast within the limits allowed by the ESA.

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row describes an element with the ID '0' named 'ForecastID'. This element is of type 'uint32', indicating it is a 32-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally without specific limitations. The conformance rule for 'ForecastID' is marked as 'M', which stands for Mandatory. This means that the 'ForecastID' command is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, under the Commands section, the entry for 'SlotAdjustments' with ID '1' is defined as a list of 'SlotAdjustmentStruct' types, constrained to a maximum of 10 entries. The conformance rule 'M' indicates that this command is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. There are no conditions or dependencies affecting its necessity; it must be included as specified.

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, within the Commands section, the table row describes a command identified by 'ID' 2, named 'Cause', which is of the type 'AdjustmentCauseEnum' and applies to all constraints. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'Cause' command is always required to be implemented in any device or system that supports the Device Energy Management Cluster, with no exceptions or conditions.

9.2.9.6.1. ForecastID Field
This field SHALL indicate the ForecastID that is to be modified.
9.2.9.6.2. SlotAdjustments Field
This field SHALL contain a list of SlotAdjustment parameters that should be modified in the corre
sponding Forecast with matching ForecastID.
9.2.9.6.3. Cause Field
This field SHALL indicate the cause of the request from the EMS.
9.2.9.6.4. Effect on receipt
FA
On receipt of this command, if the ESA supports  , and the OptOutState permits the specified
AdjustmentCauseEnum (see OptOutState for details), it SHALL attempt to adjust its forecast.
The client may be an energy management system which has retrieved the forecasts from multiple
ESA and then performed some optimization (for example, taking advantage of local solar PV gener
ation).
The ESA SHALL inspect the requested forecast and ensure that it does not exceed the limits set in
each of its slots. The ESA manufacturer may also reject the request if it could cause the user’s pref
erences to be breached (for example, if it may cause the home to be too hot or too cold, or a battery
to be insufficiently charged).
Note that the client may make an adjustment when the ESA’s program has already been started. In
this case the ActiveSlotNumber may have moved through the Forecast sequence. Any attempts to
modify slots which have already been run SHALL result in the entire command being rejected.
The command allows a single modification to a particular slot, or to multiple slots in a single com
mand by sending a list of modifications.
If the ESA accepts the requested Forecast then it SHALL update its Forecast attribute (incrementing
its ForecastID, and updating its ForecastUpdateReason from the Cause value) and run the revised
Forecast as its new intended operation.
Note that an ESA may adapt its Forecast based on a slot modification. For example, if an ESA was
switched on earlier in the day to take account of available solar PV, then it may not need to use
energy later in the day. It may add or remove slots as it chooses. This may result in several itera
tions for the Energy Management System to reprocess updated forecasts until it has stabilized on an
agreed set of changes.
If for any reason the ESA cannot accept the entire requested forecast adjustments then it SHALL
reject the entire command.
If the Cause is not permitted, or the requested forecast exceeds any of the limits in the respective
slots, then the command SHALL be rejected with CONSTRAINT_ERROR, otherwise if the ForecastID
is valid, and the entire list of SlotAdjustmentStruct are accepted, the command status returned
SHALL be SUCCESS, otherwise the command SHALL be rejected with FAILURE.
9.2.9.7. RequestConstraintBasedForecast Command
Allows a client to ask the ESA to recompute its Forecast based on power and time constraints.

_Table parsed from section 'Commands':_

* In the Device Energy Management Cluster, within the Commands section, the table row describes a command named "Constraints" with an ID of '0'. This command is of the type 'list[ConstraintsStruct]', indicating it consists of a list of structures defined as 'ConstraintsStruct'. The list has a constraint that limits it to a maximum of 10 entries. The conformance rule for this command is marked as 'M', which means it is mandatory. This implies that the "Constraints" command must always be implemented in any device or application that supports the Device Energy Management Cluster, without any conditions or exceptions.

* In the Device Energy Management Cluster, within the Commands section, the table row describes an element with the ID '1' named 'Cause', which is of the type 'AdjustmentCauseEnum' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Cause' command is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

9.2.9.7.1. Constraints Field
This field SHALL indicate the series of turn up or turn down power requests that the ESA is being
asked to constrain its operation within. These requests SHALL be in the future, SHALL be in
chronological order, starting with the earliest start time, and SHALL NOT overlap in time.
For example, a grid event which requires devices to reduce power (turn down) between 4pm and
6pm and due to excess power on the grid overnight, may request ESAs to increase their power
demand (turn up) between midnight and 6am.
PFR
If this ESA supports   this would have 2 entries in the list as follows:

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, specifically under the Commands section, the table row entry for 'Turn Down' with the attribute 'StartTime' needs to be interpreted according to its conformance rule. However, since the conformance rule for 'StartTime' is not explicitly provided in your request, we must assume a typical scenario based on the Matter Conformance Interpretation Guide. If 'StartTime' were to have a conformance rule such as `M`, it would mean that the 'StartTime' attribute is mandatory and must always be implemented for the 'Turn Down' command. If the conformance were `O`, it would indicate that 'StartTime' is optional and can be implemented at the discretion of the developer, with no dependencies. Without the specific conformance string, we can only provide this general interpretation based on typical conformance tags.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry 'Entry [0] - Turn Down': 'Duration' refers to a command related to energy management that involves a 'Duration' parameter. The conformance rule for this entry is not explicitly provided in your query, but based on the Matter Conformance Interpretation Guide, the conformance string would dictate when this 'Duration' parameter is required or optional. For instance, if the conformance string were `M`, it would mean that the 'Duration' parameter is always required for the 'Turn Down' command. If the conformance string were `O`, it would indicate that the 'Duration' parameter is optional and can be included at the implementer's discretion. If the conformance string involved logical conditions or expressions, it would specify under what conditions the 'Duration' parameter becomes mandatory or optional, based on the presence or absence of certain features or other conditions.

* The table row entry 'Entry [0] - Turn Down': 'NominalPower' within the Device Energy Management Cluster's Commands section specifies the conformance requirements for the 'NominalPower' element. According to the Matter Conformance Interpretation Guide, the conformance rule for this entry is not explicitly provided in the prompt. However, if we assume a typical conformance expression, such as `AB, O`, it would mean that the 'NominalPower' element is mandatory if a specific feature or condition `AB` is supported; otherwise, it is optional. This implies that the inclusion of 'NominalPower' in the command is contingent upon the presence of certain features or conditions within the device's energy management capabilities. Without the exact conformance expression, we can only infer that its requirement is conditional based on specific criteria outlined in the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry 'Turn Down' with the conformance rule 'MaximumEnergy' indicates that this command is conditionally mandatory. According to the conformance interpretation guide, the absence of brackets around 'MaximumEnergy' means that the 'Turn Down' command is mandatory if the 'MaximumEnergy' feature is supported. If the 'MaximumEnergy' feature is not supported, the conformance rule does not specify any alternative, implying that the command is not required. This ensures that devices with the capability to manage maximum energy levels must implement the 'Turn Down' command to comply with the Matter specification.

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry 'Turn Up: StartTime' pertains to a command related to energy management devices. The conformance rule for this entry is 'Entry [1]', which indicates that the 'StartTime' element is conditionally optional. According to the Matter Conformance Interpretation Guide, the presence of brackets around a condition (e.g., `[1]`) implies that the element is optional if the specified condition is true. However, since the condition itself is not explicitly detailed in the provided data, it suggests that further documentation or context is necessary to determine when the 'StartTime' becomes optional. In essence, 'StartTime' is not always required and depends on specific conditions outlined elsewhere in the documentation.

* The table row entry 'Turn Up: Duration' within the Device Energy Management Cluster's Commands section specifies a feature related to the 'Turn Up' command. The conformance rule for this entry is not explicitly provided in the prompt, but based on the Matter Conformance Interpretation Guide, we can infer that the 'Duration' attribute's inclusion and behavior depend on specific conditions or feature support. If the conformance string were, for example, `AB, O`, it would mean that the 'Duration' attribute is mandatory if the feature `AB` is supported; otherwise, it is optional. Without the exact conformance string, we can only conclude that the 'Duration' attribute's requirement is conditional and depends on the presence or absence of certain features or conditions within the Device Energy Management Cluster.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry titled 'Turn Up' refers to the 'NominalPower' element. The conformance rule for 'NominalPower' is not explicitly provided in the data snippet you shared. However, based on the Matter Conformance Interpretation Guide, if we were to interpret a typical conformance expression, it would detail the conditions under which 'NominalPower' is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were something like `AB, O`, it would mean that 'NominalPower' is mandatory if feature `AB` is supported; otherwise, it is optional. Without the specific conformance string, we can only infer that the conformance rule would dictate the necessity of 'NominalPower' based on certain conditions or features within the Matter specification.

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry titled 'Turn Up' with the attribute 'MaximumEnergy' has a conformance rule that needs interpretation. According to the conformance guide, the rule 'Entry [1] - Turn Up': 'MaximumEnergy' suggests that the 'MaximumEnergy' element is conditionally optional. The presence of brackets around the condition indicates that if the condition specified by 'Entry [1] - Turn Up' is met, then 'MaximumEnergy' is optional. This means that the 'MaximumEnergy' command is not required unless the specific condition defined by 'Entry [1] - Turn Up' is satisfied, in which case it becomes an optional feature within the Device Energy Management Cluster.

SFR
If this ESA supports   where it does not know the actual power, but has an understanding of the
functions that use more energy, it could be requested to use more or less energy using the LoadCon
trol field as follows:

_Table parsed from section 'Commands':_

* In the context of the Device Energy Management Cluster, specifically within the Commands section, the table row entry 'Entry [0] - Turn Down': 'StartTime' refers to a command element related to managing energy usage by initiating a "turn down" action at a specified start time. The conformance rule for this element is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, the conformance would dictate when this 'StartTime' element is required or optional. If a specific conformance string were provided, it would clarify whether 'StartTime' is mandatory, optional, provisional, deprecated, disallowed, or described in more detail elsewhere. The interpretation would depend on the presence of any logical conditions or expressions that determine its necessity based on supported features or other conditions.

* The table row entry 'Entry [0] - Turn Down': 'Duration' within the Device Energy Management Cluster's Commands section refers to a specific command related to energy management, specifically the 'Turn Down' command, which includes a 'Duration' parameter. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we assume a typical conformance rule format, it would specify under what conditions the 'Duration' parameter is required, optional, or otherwise. For instance, if the conformance was 'M', it would mean that the 'Duration' parameter is always mandatory for the 'Turn Down' command. If it were 'O', it would be optional, and so forth. Without the specific conformance string, we cannot determine the exact requirement, but the rule would guide implementers on whether and when to include the 'Duration' parameter in their implementations of the 'Turn Down' command.

* The table row entry 'Entry [0] - Turn Down' within the Device Energy Management Cluster's Commands section refers to the 'LoadControl' command. According to the conformance rules, the 'LoadControl' command is subject to a conditional requirement. Specifically, the conformance expression 'Entry [0]' indicates that the command is Optional if the condition 'Entry [0]' is true. This means that if the specific condition or feature represented by 'Entry [0]' is supported or applicable, the 'LoadControl' command can be implemented but is not mandatory. If 'Entry [0]' is not supported or applicable, the command is not required, and there are no further conditions or requirements specified for its implementation.

_Table parsed from section 'Commands':_

* The table row entry 'Entry [1] - Turn Up' within the Device Energy Management Cluster, under the Commands section, refers to the 'StartTime' attribute. According to the conformance rules, the 'StartTime' attribute is described as having a conformance status of 'Entry [1]'. This indicates that the conformance of 'StartTime' is too complex to be expressed with a simple tag or logical condition and is instead detailed elsewhere in the documentation. Therefore, to fully understand when and how 'StartTime' is required or optional, one would need to refer to the specific description provided in the documentation for 'Entry [1]'. This approach ensures that any nuanced conditions or dependencies related to 'StartTime' are accurately captured and communicated.

* The table row entry 'Turn Up' under the 'Duration' field in the Device Energy Management Cluster's Commands section specifies the conformance requirements for the 'Duration' element. According to the Matter Conformance Interpretation Guide, the conformance rule for this entry is not explicitly provided in the prompt, but let's assume a hypothetical conformance string for explanation purposes. If the conformance string were, for example, `AB, O`, it would mean that the 'Duration' element is mandatory if the feature 'AB' is supported. If 'AB' is not supported, then the 'Duration' element is optional. This interpretation allows implementers to understand when they must include the 'Duration' element in their implementation of the 'Turn Up' command, depending on the presence or absence of specific features or conditions.

* The table row entry 'Turn Up' within the 'Device Energy Management Cluster' under the 'Commands' section pertains to the 'LoadControl' feature. The conformance rule 'Entry [1]' indicates that the 'Turn Up' command is conditionally optional based on the presence of a specific feature or condition, which is not explicitly detailed in the provided data. According to the Matter Conformance Interpretation Guide, the use of brackets around a condition (e.g., `[1]`) signifies that the element is optional if the condition is met. Therefore, the 'Turn Up' command is not mandatory but may be implemented if the specified condition for 'Entry [1]' is satisfied. If the condition is not met, the command remains optional and not required for implementation.

9.2.9.7.2. Cause Field
This field SHALL indicate the cause of the request from the EMS.
9.2.9.7.3. Effect on receipt
CON
On receipt of this command, if the ESA supports  , and the OptOutState permits the specified
AdjustmentCauseEnum (see OptOutState for details), it may be requested to generate a new forecast
by a client.
For example the client may be an energy management system which has determined that the peak
load on the home should be reduced (for example a grid event) or that there is more local genera
tion available and the solar export power needs to be consumed.
The EMS may not be best placed to make the forecast adjustment because the ESA knows more
about its internal operation and system efficiencies.
For example the total energy used when charging a battery faster may result in increased heat
losses in the inverter, so the total energy required to charge a battery with 10kWh of stored energy
may vary based on charging power.
The ESA SHALL inspect the constraints field to ensure that the constraints defined for that field and
its elements are met. The ESA manufacturer may also reject the request if it could cause the user’s
preferences to be breached (e.g. may cause the home to be too hot or too cold, or a battery to be
insufficiently charged).
If the ESA can meet the requested power limits, it SHALL regenerate a new Power Forecast with a
new ForecastID and ForecastUpdateReason from the Cause value.
If an appliance has already begun running a program (and agreed to modify its schedule), it may
continue to run the same program and meet the same user settings (e.g. ECO mode), but may take
more or less time to complete the cycle. The new reported Forecast will start from the current time,
i.e. the slots that have already been completed SHALL NOT be included in the new forecast.
The command status returned SHALL be SUCCESS, otherwise if the Cause is not permitted, or the
constraints field value does not meet the defined constraints, the command SHALL be rejected with
CONSTRAINT_ERROR, otherwise the command SHALL be rejected with FAILURE.
9.2.9.8. CancelRequest Command
Allows a client to request cancellation of a previous adjustment request in a StartTimeAdjustRe
quest, ModifyForecastRequest or RequestConstraintBasedForecast command.
9.2.9.8.1. Effect on receipt
On receipt of this command, the ESA SHALL attempt to cancel the effects of any previous adjust
ment request commands, and re-evaluate its forecast for intended operation ignoring those previ
ous requests.
Internal Optimization
If the ESA ForecastUpdateReason was already  , then the command SHALL be
rejected with INVALID_IN_STATE.
If the command is accepted, the ESA SHALL update its ESAState if required, and the command sta
tus returned SHALL be SUCCESS. The ESA SHALL update its Forecast attribute to match its new
Internal Optimization
intended operation, and update the ForecastUpdateReason to  .

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Device Energy Management Cluster, specifically the "PowerAdjustStart" event, which has an ID of '0x00'. This event is categorized under the 'INFO' priority level and has an access level of 'V', indicating it is visible. The conformance rule for "PowerAdjustStart" is 'PA', which means it is currently in a provisional state. This suggests that the event's status is temporary and subject to change, with the potential to become mandatory in the future. Therefore, while it is not currently required, it is expected that this event may become a necessary component of the specification at a later date.

* The table row describes an event within the Device Energy Management Cluster, specifically the "PowerAdjustEnd" event, identified by the ID '0x01'. This event has an informational priority level and requires 'V' access, which typically indicates a specific type of access or visibility requirement. The conformance rule for "PowerAdjustEnd" is 'PA', which, according to the Matter Conformance Interpretation Guide, means that the event is currently in a provisional state ('P'). This indicates that its status is temporary and subject to change. The 'A' following the provisional status suggests that there is an intended future conformance, but without additional context, it's unclear what 'A' specifically denotes. Therefore, the "PowerAdjustEnd" event is currently not mandatory but may become so or have another defined status in future updates of the specification.

* The table row describes an event within the Device Energy Management Cluster, specifically an event named "Paused" with an ID of '0x02'. This event has a priority level of 'INFO' and an access level denoted by 'V', which typically indicates visibility or read access. The conformance rule for this event is 'PAU', which, according to the Matter Conformance Interpretation Guide, suggests a conditional rule based on the presence of certain features or conditions. However, 'PAU' does not directly match any standard conformance tags or logical conditions provided in the guide, indicating that it might be a shorthand or a specific condition described elsewhere in the documentation. Without additional context or a specific description of 'PAU', it is unclear whether this event is mandatory, optional, or subject to other conditions. Therefore, further reference to the detailed documentation would be necessary to fully understand the conformance requirements for this event.

* In the Device Energy Management Cluster, under the Events section, there is an event identified by the ID '0x03' named 'Resumed'. This event has a priority level of 'INFO' and requires 'V' access. The conformance rule for this event is 'PAU', which indicates that the event is currently in a Provisional status, meaning its requirement status is temporary and subject to change. The 'PAU' conformance suggests that the event is intended to become mandatory in the future, but for now, it is not strictly required. This provisional status allows for flexibility as the specification evolves, potentially leading to a mandatory requirement in subsequent updates.

9.2.10.1. PowerAdjustStart Event
This event SHALL be generated when the Power Adjustment session is started.
9.2.10.2. PowerAdjustEnd Event
This event SHALL be generated when the Power Adjustment session ends.

_Table parsed from section 'Events':_

* The table row describes an event within the Device Energy Management Cluster, specifically focusing on the 'Cause' attribute. This attribute is identified by the ID '0' and is of the type 'CauseEnum', which suggests it enumerates various causes related to energy management events. The constraint 'all' indicates that this attribute applies universally within its context, and its default value is set to 'NormalCompletion'. The conformance rule 'M' signifies that the 'Cause' attribute is mandatory, meaning it is always required to be implemented in any device or system that supports the Device Energy Management Cluster. There are no conditions or exceptions to this requirement, ensuring consistent inclusion across all relevant implementations.

* In the context of the Device Energy Management Cluster, under the Events section, the table row describes an event with the ID '1' named 'Duration'. This event is of the type 'elapsed-s', which likely refers to a measurement of elapsed time in seconds. The constraint 'all' suggests that this event applies universally within its context. The conformance rule 'M' indicates that the 'Duration' event is mandatory, meaning it is always required to be implemented in any device or application that supports the Device Energy Management Cluster. There are no conditions or exceptions; this event must be included as per the Matter specification.

* The table row describes an event named "EnergyUse" within the Device Energy Management Cluster, specifically under the Events section. The event is identified by the ID '2' and is of the type 'energy-mWh', indicating it measures energy usage in milliwatt-hours. The constraint 'all' suggests that this event applies universally within its context. The conformance rule 'M' signifies that the "EnergyUse" event is mandatory, meaning it is always required to be implemented in any device or system that supports the Device Energy Management Cluster, without any conditions or exceptions.

9.2.10.2.1. Cause Field
This field SHALL indicate the reason why the power adjustment session ended.
9.2.10.2.2. Duration Field
This field SHALL indicate the number of seconds that the power adjustment session lasted before
ending.
9.2.10.2.3. EnergyUse Field
This field SHALL indicate the approximate energy used by the ESA during the session.
For example, if the ESA was on and was adjusted to be switched off, then this SHALL be 0 mWh. If
this was a battery inverter that was requested to discharge it would have a negative EnergyUse
value. If this was a normal load that was turned on, then it will have positive value.
9.2.10.3. Paused Event
This event SHALL be generated when the ESA enters the Paused state.
There is no data for this event.
9.2.10.4. Resumed Event
This event SHALL be generated when the ESA leaves the Paused state and resumes operation.

_Table parsed from section 'Events':_

* The table row describes an event within the Device Energy Management Cluster, specifically the 'Cause' event. This event is identified by the ID '0' and uses the 'CauseEnum' type, which encompasses all possible constraints. The default value for this event is set to 'NormalCompletion'. According to the conformance rule 'M', this event is mandatory, meaning it is always required to be implemented in any device or system that supports the Device Energy Management Cluster. There are no conditions or exceptions to this requirement, ensuring that the 'Cause' event is consistently available across all implementations.

9.2.10.4.1. Cause Field
This field SHALL indicate the reason why the pause ended.