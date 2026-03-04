
# 2.13 Electrical Power Measurement Cluster

This cluster provides a mechanism for querying data about electrical power as measured by the
server.

## Data Types
2.13.5.1. PowerModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Electrical Power Measurement Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '0' and the 'Name' of 'Unknown'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'Unknown' data type is a required element within this cluster and must always be implemented according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, indicating its fundamental role in the cluster's functionality.

_Table parsed from section 'Data Types':_

* In the context of the Electrical Power Measurement Cluster, under the Data Types section, the table row describes an entry with the name 'DC', which stands for 'Direct current'. The 'Value' assigned to this entry is '1', indicating its identifier within this context. The 'Conformance' field is marked as 'M', which means that this element is Mandatory. According to the Matter Conformance Interpretation Guide, a Mandatory conformance tag indicates that the 'DC' data type is always required to be implemented in any device or application utilizing this cluster. There are no conditions or dependencies that alter this requirement, making 'DC' an essential component of the Electrical Power Measurement Cluster.

* In the context of the Electrical Power Measurement Cluster, specifically within the Data Types section, the table row describes an entry with the name "AC," which stands for Alternating Current, applicable to either single-phase or polyphase systems. The 'Value' assigned to this entry is '2'. The 'Conformance' field for this entry is marked as 'M', indicating that this element is Mandatory. This means that the inclusion of the "AC" data type is always required in implementations of this cluster, with no conditions or exceptions.

2.13.5.2. MeasurementRangeStruct Type
This struct SHALL indicate the maximum and minimum values of a given measurement type dur
ing a measurement period, along with the observation times of these values.
A server which does not have the ability to determine the time in UTC, or has not yet done so,
SHALL use the system time fields to specify the measurement period and observation times.
A server which has determined the time in UTC SHALL use the timestamp fields to specify the mea
surement period and observation times. Such a server MAY also include the systime fields to indi
cate how many seconds had passed since boot for a given timestamp; this allows for client-side res
olution of UTC time for previous reports that only included systime.

_Table parsed from section 'Data Types':_

* In the context of the Electrical Power Measurement Cluster, the table row describes an element with the ID '0' named 'MeasurementType', which is of the type 'MeasurementTypeEnum'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'MeasurementType' element is always required to be implemented in any device or system that supports the Electrical Power Measurement Cluster, without any conditions or exceptions. This ensures that the 'MeasurementType' is consistently available across all implementations of this cluster, providing a standardized way to represent measurement types within the cluster.

* In the context of the Electrical Power Measurement Cluster, the table row describes a data type entry with the ID '1', named 'Min', which is of type 'int64' and has a constraint range from -262 to 262. The conformance rule for this entry is 'M', indicating that the 'Min' data type is mandatory. This means that within this cluster, the 'Min' attribute must always be implemented and supported, without any conditions or exceptions.

* In the context of the Electrical Power Measurement Cluster, the table entry describes a data type named 'Max' with an identifier 'ID' of '2'. This data type is of type 'int64' and has a constraint range from -262 to 262. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Max' data type is always required to be implemented in any device or application that supports the Electrical Power Measurement Cluster, without any conditions or exceptions.

* In the context of the Electrical Power Measurement Cluster, the table row describes a data type entry with the ID '3' named 'StartTimestamp', which is of type 'epoch-s'. The conformance rule for 'StartTimestamp' is 'EndTimestamp'. According to the Matter Conformance Interpretation Guide, this means that the 'StartTimestamp' element is mandatory if the 'EndTimestamp' feature is supported. If 'EndTimestamp' is not supported, the conformance of 'StartTimestamp' is not explicitly defined in this entry, implying it may not be required. This setup ensures that 'StartTimestamp' is used in conjunction with 'EndTimestamp' to provide a complete temporal context for power measurement data.

* The table row describes an element within the Electrical Power Measurement Cluster, specifically in the Data Types section. The element is identified by the ID '4' and is named 'EndTimestamp'. It is of the type 'epoch-s', which likely refers to a timestamp format based on seconds since the epoch (a common time representation in computing). The constraint for this element is that it must be at least one second greater than the 'StartTimestamp', indicating a dependency on another timestamp to ensure chronological order. The conformance for 'EndTimestamp' is marked as 'desc', which means that the rules governing when this element is required or optional are too complex to be captured by simple tags or expressions. Instead, these rules are detailed elsewhere in the documentation, suggesting that its inclusion depends on specific conditions or scenarios not immediately apparent from the table alone.

* The table row entry for the Electrical Power Measurement Cluster under the Data Types section describes an element with the ID '5' named 'MinTimestamp', which is of the type 'epoch-s'. The conformance rule for 'MinTimestamp' is specified as 'EndTimestamp'. According to the Matter Conformance Interpretation Guide, this means that the 'MinTimestamp' element is mandatory if the feature or element 'EndTimestamp' is supported. In other words, the presence of 'MinTimestamp' is contingent upon the support of 'EndTimestamp'; if 'EndTimestamp' is part of the implementation, then 'MinTimestamp' must also be included.

* The table row describes an element within the Electrical Power Measurement Cluster, specifically under the Data Types section. The element is identified by the ID '6' and is named 'MaxTimestamp'. It is of the type 'epoch-s', which likely refers to a timestamp format representing seconds since the epoch. The constraint for this element is defined as 'min (MinTimestamp + 1)', indicating that its value must be at least one second greater than the 'MinTimestamp'. The conformance rule for 'MaxTimestamp' is 'EndTimestamp', which implies that this element is mandatory if the feature or condition 'EndTimestamp' is supported. If 'EndTimestamp' is not supported, the conformance of 'MaxTimestamp' is not explicitly defined in this entry, suggesting it may not be required or its requirement is described elsewhere.

* The table row entry for the Electrical Power Measurement Cluster under the Data Types section describes an element with the ID '7' named 'StartSystime', which is of the type 'systime-ms'. The conformance rule for 'StartSystime' is specified as 'EndSystime'. According to the Matter Conformance Interpretation Guide, this means that the 'StartSystime' element is mandatory if the feature or condition 'EndSystime' is supported. In other words, the presence of 'StartSystime' is contingent upon the support for 'EndSystime', making it a required element only when 'EndSystime' is implemented within the system.

* The table row describes an element within the Electrical Power Measurement Cluster, specifically under the Data Types section. The element is identified by the ID '8' and is named 'EndSystime'. It is of the type 'systime-ms', which likely refers to a system time measured in milliseconds. The constraint for this element is that it must be at least one millisecond greater than 'StartSystime'. The conformance for 'EndSystime' is marked as 'desc', indicating that its conformance requirements are too complex to be captured by a simple tag or expression. Instead, the specific conditions or rules governing its necessity or optionality are detailed elsewhere in the documentation. This suggests that understanding when 'EndSystime' is required or optional involves more intricate conditions that need to be reviewed in the broader context of the specification.

* The table row entry for the Electrical Power Measurement Cluster in the Data Types section describes an element with the ID '9' and the name 'MinSystime', which is of the type 'systime-ms'. The conformance rule for this element is 'EndSystime'. According to the Matter Conformance Interpretation Guide, this means that the 'MinSystime' element is mandatory if the feature or condition 'EndSystime' is supported. If 'EndSystime' is not supported, the conformance of 'MinSystime' is not explicitly defined in this entry, implying that it may not be required or is subject to other conditions not specified here.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Electrical Power Measurement Cluster, specifically under the Data Types section. The element is identified by the ID '10' and is named 'MaxSystime'. It is of the type 'systime-ms', which likely refers to a time measurement in milliseconds. The constraint for this element is that its value must be at least one unit greater than 'MinSystime'. The conformance rule for 'MaxSystime' is 'EndSystime', which means that this element is mandatory if the feature or condition 'EndSystime' is supported. If 'EndSystime' is not supported, the conformance of 'MaxSystime' is not specified in this entry, implying that it might not be required or its requirement is described elsewhere.

2.13.5.2.1. MeasurementType Field
This field SHALL be the type of measurement for the range provided.
2.13.5.2.2. Min Field
This field SHALL be the smallest measured value for the associated measurement over either the
period  between  StartTimestamp  and  EndTimestamp,  or  the  period  between  StartSystime  and
EndSystime, or both.
2.13.5.2.3. Max Field
This field SHALL be the largest measured value for the associated measurement over the period
between  either  StartTimestamp  and  EndTimestamp  or  the  period  between  StartSystime  and
EndSystime, or both.
2.13.5.2.4. StartTimestamp Field
This field SHALL be the timestamp in UTC of the beginning of the measurement period.
If the server had not yet determined the time in UTC at or before the beginning of the measurement
period, or does not have the capability of determining the time in UTC, this field SHALL be omitted.
2.13.5.2.5. EndTimestamp Field
This field SHALL be the timestamp in UTC of the end of the measurement period.
If the server had not yet determined the time in UTC at or before the beginning of the measurement
period, or does not have the capability of determining the time in UTC, this field SHALL be omitted.
2.13.5.2.6. MinTimestamp Field
This field SHALL be the most recent timestamp in UTC that the value in the Min field was mea
sured.
This field SHALL be greater than or equal to the value of the StartTimestamp field.
This field SHALL be less than or equal to the value of the EndTimestamp field.
2.13.5.2.7. MaxTimestamp Field
This field SHALL be the most recent timestamp in UTC of the value in the Max field.
This field SHALL be greater than or equal to the value of the StartTimestamp field.
This field SHALL be less than or equal to the value of the EndTimestamp field.
2.13.5.2.8. StartSystime Field
This field SHALL be the time since boot of the beginning of the measurement period.
If the server had determined the time in UTC at or before the start of the measurement period, this
field MAY be omitted along with the EndSystime, MinSystime, and MaxSystime fields.
2.13.5.2.9. EndSystime Field
This field SHALL be the time since boot of the end of the measurement period.
If the server had determined the time in UTC at the end of the measurement period, this field MAY
be omitted along with the StartSystime field, MinSystime, and MaxSystime fields.
2.13.5.2.10. MinSystime Field
This field SHALL be the measurement time since boot of the value in the Min field was measured.
This field SHALL be greater than or equal to the value of the StartSystime field.
This field SHALL be less than or equal to the value of the EndSystime field.
2.13.5.2.11. MaxSystime Field
This field SHALL be the measurement time since boot of the value in the Max field.
This field SHALL be greater than or equal to the value of the StartSystime field.
This field SHALL be less than or equal to the value of the EndSystime field.
2.13.5.3. HarmonicMeasurementStruct Type

_Table parsed from section 'Data Types':_

* In the context of the Electrical Power Measurement Cluster, the table row describes a data type entry with the ID '0', named 'Order'. This entry is of type 'uint8', meaning it is an unsigned 8-bit integer, and it has a constraint specifying a minimum value of 1. The default value for this data type is set to 1. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Order' data type is always required to be implemented in any device or application that supports the Electrical Power Measurement Cluster, without any conditions or exceptions.

* In the context of the Electrical Power Measurement Cluster, the table row describes a data type entry with the ID '1' named 'Measurement'. This entry is of type 'int64', which means it is a 64-bit integer, and it has a constraint that limits its values between -262 and 262. The 'Quality' field is marked as 'X', indicating that quality-related features are explicitly disallowed for this entry. The default value for this data type is 'null', meaning it does not have a predefined initial value. The 'Conformance' field is marked as 'M', which signifies that the 'Measurement' data type is mandatory. This means it is always required to be implemented in any device or application using the Electrical Power Measurement Cluster, without any conditions or exceptions.

2.13.5.3.1. Order Field
This field SHALL be the order of the harmonic being measured. Typically this is an odd number,
but servers may choose to report even harmonics.
2.13.5.3.2. Measurement Field
This field SHALL be the measured value for the given harmonic order.
For the Harmonic Currents attribute, this value is the most recently measured harmonic current
reading in milliamps (mA). A positive value indicates that the measured harmonic current is posi
tive, and a negative value indicates that the measured harmonic current is negative.
For the Harmonic Phases attribute, this value is the most recent phase of the given harmonic order
in millidegrees (mDeg). A positive value indicates that the measured phase is leading, and a nega
tive value indicates that the measured phase is lagging.
If this measurement is not currently available, a value of null SHALL be returned.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the 'PowerMode' attribute. This attribute is identified by the ID '0x0000' and is of the type 'PowerModeEnum'. It has an access level of 'R V', indicating that it is readable and can be viewed. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the 'PowerMode' attribute is always required to be implemented in any device or application that supports the Electrical Power Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the 'NumberOfMeasurementTypes' attribute. This attribute has an ID of '0x0001' and is of type 'uint8', which means it is an 8-bit unsigned integer. It has a constraint of a minimum value of 1, indicating that the number of measurement types must be at least 1. The quality 'F' suggests it is a feature attribute, and the access 'R V' indicates that it is readable and has volatile data. The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device supporting the Electrical Power Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute named "Accuracy" within the Electrical Power Measurement Cluster, specifically in the context of attributes. This attribute is identified by the ID '0x0002' and is of the type 'list[MeasurementAccuracyStruct]', which means it is a list containing structures that define measurement accuracy. The constraint '1 to NumberOfMeasurementTypes' indicates that the list must contain at least one entry and can have as many entries as there are measurement types. The quality 'F' suggests that this attribute is a feature of the cluster, while the access 'R V' indicates that it is readable and can be viewed. The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device that supports the Electrical Power Measurement Cluster.

* In the Electrical Power Measurement Cluster, within the Attributes section, the attribute identified by 'ID' 0x0003 is named 'Ranges'. This attribute is of the type 'list[MeasurementRangeStruct]', which means it can hold a list of structures defined by 'MeasurementRangeStruct'. The constraint specifies that the list can contain between 0 and 'NumberOfMeasurementTypes' entries. The 'Quality' is marked as 'Q', and the default value for this attribute is 'empty'. The 'Access' is specified as 'R V', indicating that it is readable and volatile. The conformance rule for this attribute is 'O', meaning that the 'Ranges' attribute is optional; it is not required to be implemented and has no dependencies on other features or conditions.

* In the context of the Electrical Power Measurement Cluster, the table row describes an attribute named "Voltage" with an ID of '0x0004'. This attribute measures voltage in millivolts ('voltage-mV') and has a constraint range from -262 to 262. The 'Quality' field is marked as 'X Q', indicating specific quality or usage restrictions, and the 'Default' value is 'null', meaning it does not have a predefined default value. The 'Access' field is 'R V', suggesting it is readable and possibly volatile. The 'Conformance' field is marked as 'O', which means that the Voltage attribute is optional. This implies that while it is not required to be implemented in all devices supporting the Electrical Power Measurement Cluster, it can be included at the discretion of the device manufacturer without any dependencies or conditions.

* The table row describes an attribute named "ActiveCurrent" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x0005' and is measured in milliamperes (mA), with a constraint range from -262 to 262. The quality is marked as 'X Q', indicating specific quality characteristics, and the default value is 'null'. The access level is 'R V', meaning it is readable and has volatile characteristics. The conformance for "ActiveCurrent" is marked as 'O', which means this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an attribute named "ReactiveCurrent" within the Electrical Power Measurement Cluster. This attribute is identified by the ID '0x0006' and measures amperage in milliamps (mA), with a valid range from -262 to 262. The quality of this attribute is marked as 'X Q', indicating it is disallowed and has a quality issue. The default value for this attribute is 'null', and it has read and volatile access permissions ('R V'). The conformance rule '[ALTC]' specifies that the "ReactiveCurrent" attribute is optional if the condition 'ALTC' is true. This means that if the feature or condition represented by 'ALTC' is supported, the implementation of this attribute is optional; otherwise, it is not required.

* The table row describes an attribute named "ApparentCurrent" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x0007' and is measured in milliamperes (mA), with a constraint range from 0 to 262. The quality is marked as 'X Q', indicating it is disallowed and has a quality issue. The default value is 'null', and it has read-only ('R') and volatile ('V') access permissions. The conformance rule '[ALTC]' specifies that the "ApparentCurrent" attribute is optional if the feature 'ALTC' is supported. If 'ALTC' is not supported, the attribute is not required.

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the 'ActivePower' attribute. This attribute is identified by the ID '0x0008' and is of the type 'power-mW', with a value constraint ranging from -262 to 262. The 'Quality' field indicates that this attribute is disallowed for certain quality levels, denoted by 'X Q'. The default value for 'ActivePower' is 'null', and it has read and volatile access permissions, as indicated by 'R V'. The conformance rule 'M' signifies that the 'ActivePower' attribute is mandatory, meaning it is always required to be implemented in any device or application using this cluster, without any conditions or exceptions.

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the 'ReactivePower' attribute. This attribute has an ID of '0x0009' and is of type 'power-mW', with a constraint range from -262 to 262. The 'Quality' field indicates that this attribute is disallowed ('X') and has a quality issue ('Q'). The default value for this attribute is 'null', and it has read and volatile access ('R V'). The conformance rule '[ALTC]' specifies that the 'ReactivePower' attribute is optional if the condition 'ALTC' is true. This means that the attribute is not required unless the feature or condition 'ALTC' is supported, in which case it becomes optional.

* The table row describes an attribute named "ApparentPower" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x000A' and is of the type 'power-mW', with a value constraint ranging from -262 to 262. The 'Quality' field indicates that this attribute is disallowed ('X') and has a quality indicator ('Q'). The default value for this attribute is 'null', and it has read and volatile access permissions ('R V'). The conformance rule '[ALTC]' specifies that the "ApparentPower" attribute is optional if the condition 'ALTC' is true. This means that if the feature or condition represented by 'ALTC' is supported, the attribute may be included but is not required.

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the "RMSVoltage" attribute, identified by the ID '0x000B'. This attribute measures voltage in millivolts and has a constraint range from -262 to 262. The quality is marked as 'X Q', indicating it is disallowed and has a quality constraint. The default value for this attribute is 'null', and it has read and volatile access permissions ('R V'). The conformance rule '[ALTC]' indicates that the RMSVoltage attribute is optional if the condition 'ALTC' is true, meaning it is not required unless the specific feature or condition 'ALTC' is supported.

* The table row describes an attribute named "RMSCurrent" within the Electrical Power Measurement Cluster, identified by the ID '0x000C'. This attribute measures current in milliamperes (mA) and has a value constraint ranging from -262 to 262. The quality is marked as 'X Q', indicating that certain quality aspects are disallowed or not applicable. The default value for this attribute is 'null', and it has read-only access with volatile data ('R V'). The conformance rule '[ALTC]' specifies that the "RMSCurrent" attribute is optional if the condition 'ALTC' is true. This means that the attribute does not have to be implemented unless the specific feature or condition 'ALTC' is supported, in which case its inclusion is optional.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "RMSPower" within the Electrical Power Measurement Cluster. This attribute is identified by the ID '0x000D' and is of type 'power-mW', with a value constraint ranging from -262 to 262. The quality is marked as 'X Q', indicating it is disallowed in some contexts, and the default value is 'null'. The access level is 'R V', meaning it is readable and volatile. The conformance rule '[ALTC]' specifies that the RMSPower attribute is optional if the condition 'ALTC' is true. This means that if the feature or condition represented by 'ALTC' is supported, the inclusion of the RMSPower attribute is not mandatory but allowed.

* In the Electrical Power Measurement Cluster, the attribute with ID '0x000E' is named 'Frequency' and is of type 'int64', constrained to values between 0 and 1,000,000. It has a quality designation of 'X Q', indicating specific quality characteristics, and a default value of 'null'. The access level is 'R V', meaning it is readable and has volatile characteristics. The conformance rule '[ALTC]' indicates that the 'Frequency' attribute is optional if the feature 'ALTC' is supported. If 'ALTC' is not supported, the attribute is not required. This entry specifies the conditions under which the 'Frequency' attribute should be implemented in devices supporting the Electrical Power Measurement Cluster.

* The table row describes an attribute within the Electrical Power Measurement Cluster, specifically the "HarmonicCurrents" attribute. This attribute is identified by the ID '0x000F' and is of the type 'list[HarmonicMeasurementStruct]'. The 'Constraint' field is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' field is 'X Q', meaning that this attribute is explicitly disallowed from having a certain quality, which is not specified here. The default value for this attribute is 'null', and it has 'Read' and 'Volatile' access permissions, as indicated by 'R V'. The 'Conformance' field is 'HARM', which means that the attribute is mandatory if the feature 'HARM' is supported. If 'HARM' is not supported, the attribute is not required. This entry specifies the conditions under which the "HarmonicCurrents" attribute must be implemented in a device

* The table row describes an attribute named "HarmonicPhases" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x0010' and is of the type 'list[HarmonicMeasurementStruct]'. The 'Constraint' is described elsewhere in the documentation, indicating complexity. The 'Quality' is marked as 'X Q', meaning it is disallowed for quality purposes. The default value is 'null', and the access is 'R V', indicating it is readable and volatile. The 'Conformance' is specified as 'PWRQ', which means this attribute is mandatory if the feature 'PWRQ' is supported. If 'PWRQ' is not supported, the attribute is not required. This conformance rule implies that the attribute's inclusion is conditional based on the support of the 'PWRQ' feature, reflecting its provisional status in the specification.

* The table row describes an attribute named "PowerFactor" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x0011' and is of type 'int64', with a value constraint ranging from -10000 to 10000. The 'Quality' field indicates that this attribute is disallowed for some reason, as denoted by 'X Q'. The default value for this attribute is 'null', and it has read ('R') and volatile ('V') access permissions. The conformance rule '[ALTC]' specifies that the "PowerFactor" attribute is optional if the feature 'ALTC' is supported. If 'ALTC' is not supported, the attribute does not need to be included. This means that the inclusion of the "PowerFactor" attribute is conditional based on the presence of the 'ALTC' feature, allowing flexibility in implementation depending on the device's capabilities.

* The table row describes an attribute named "NeutralCurrent" within the Electrical Power Measurement Cluster. This attribute has an ID of '0x0012' and is measured in milliamperes (mA), with a constraint range from -262 to 262. The quality is marked as 'X Q', indicating that it is disallowed and has a quality constraint. The default value for this attribute is 'null', and it has read and volatile access permissions ('R V'). The conformance rule '[POLY]' indicates that the presence of this attribute is optional if the condition 'POLY' is true. In other words, the attribute is not required unless the specific feature or condition identified by 'POLY' is supported, making it optional in such cases.

2.13.6.1. PowerMode Attribute
This SHALL indicate the current mode of the server. For some servers, such as an EV, this may
change depending on the mode of charging or discharging.
2.13.6.2. NumberOfMeasurementTypes Attribute
This SHALL indicate the maximum number of measurement types the server is capable of report
ing.
2.13.6.3. Accuracy Attribute
This SHALL indicate a list of accuracy specifications for the measurement types supported by the
server. There SHALL be an entry for ActivePower, as well as any other measurement types imple
mented by this server.
2.13.6.4. Ranges Attribute
This SHALL indicate a list of measured ranges for different measurement types. Each measurement
type SHALL have at most one entry in this list, representing the range of measurements in the most
recent measurement period.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
2.13.6.5. Voltage Attribute
This SHALL indicate the most recent Voltage reading in millivolts (mV).
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the voltage cannot be measured, a value of null SHALL be returned.
2.13.6.6. ActiveCurrent Attribute
This SHALL indicate the most recent ActiveCurrent reading in milliamps (mA).
A positive value represents current flowing into the server, while a negative value represents cur
rent flowing out of the server.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the current cannot be measured, a value of null SHALL be returned.
2.13.6.7. ReactiveCurrent Attribute
This SHALL indicate the most recent ReactiveCurrent reading in milliamps (mA).
A positive value represents current flowing into the server, while a negative value represents cur
rent flowing out of the server.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the current cannot be measured, a value of null SHALL be returned.
2.13.6.8. ApparentCurrent Attribute
This SHALL indicate the most recent ApparentCurrent (square root sum of the squares of active
and reactive currents) reading in milliamps (mA).
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the active or reactive currents cannot be measured, a value of null SHALL be returned.
2.13.6.9. ActivePower Attribute
This SHALL indicate the most recent ActivePower reading in milliwatts (mW). If the power cannot
be measured, a value of null SHALL be returned.
A positive value represents power imported, while a negative value represents power exported.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the Polyphase Power feature is set, this value represents the combined active power imported or
exported.
2.13.6.10. ReactivePower Attribute
This SHALL indicate the most recent ReactivePower reading in millivolt-amps reactive (mVAR).
A positive value represents power imported, while a negative value represents power exported.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the reactive power cannot be measured, a value of null SHALL be returned.
If the Polyphase Power feature is supported, this value represents the combined reactive power
imported or exported.
2.13.6.11. ApparentPower Attribute
This SHALL indicate the most recent ApparentPower reading in millivolt-amps (mVA).
A positive value represents power imported, while a negative value represents power exported.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the apparent power cannot be measured, a value of null SHALL be returned.
2.13.6.12. RMSVoltage Attribute
This SHALL indicate the most recent RMSVoltage reading in millivolts (mV).
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the RMS voltage cannot be measured, a value of null SHALL be returned.
2.13.6.13. RMSCurrent Attribute
This SHALL indicate the most recent RMSCurrent reading in milliamps (mA).
A positive value represents current flowing into the server, while a negative value represents cur
rent flowing out of the server.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the RMS current cannot be measured, a value of null SHALL be returned.
2.13.6.14. RMSPower Attribute
This SHALL indicate the most recent RMSPower reading in milliwatts (mW).
A positive value represents power imported, while a negative value represents power exported.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the RMS power cannot be measured, a value of null SHALL be returned.
2.13.6.15. Frequency Attribute
This SHALL indicate the most recent Frequency reading in millihertz (mHz).
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the frequency cannot be measured, a value of null SHALL be returned.
2.13.6.16. HarmonicCurrents Attribute
This SHALL indicate a list of HarmonicMeasurementStruct values, with each HarmonicMeasure
mentStruct representing the harmonic current reading for the harmonic order specified by Order.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
2.13.6.17. HarmonicPhases Attribute
This SHALL indicate a list of HarmonicMeasurementStruct values, with each HarmonicMeasure
mentStruct representing the most recent phase of the harmonic current reading for the harmonic
order specified by Order.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
2.13.6.18. PowerFactor Attribute
This SHALL indicate the Power Factor ratio in +/- 1/100ths of a percent.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
2.13.6.19. NeutralCurrent Attribute
This SHALL indicate the most recent NeutralCurrent reading in milliamps (mA). Typically this is a
derived value, taking the magnitude of the vector sum of phase currents.
If the neutral current cannot be measured or derived, a value of null SHALL be returned.
A positive value represents an imbalance between the phase currents when power is imported.
A negative value represents an imbalance between the phase currents when power is exported.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.

## Events
This cluster SHALL support the following event:

_Table parsed from section 'Events':_

* The table row entry pertains to the "MeasurementPeriodRanges" event within the Electrical Power Measurement Cluster, categorized under the "Events" section. This event has an ID of '0' and is designated with a priority level of 'INFO', indicating it provides informational data. The access level is marked as 'V', which typically denotes that the event is visible or can be accessed in some manner. The conformance field is specified as 'Ranges', which suggests that the conformance requirements for this event are complex and detailed elsewhere in the documentation, rather than being expressed through a simple conformance tag or logical condition. This means that to fully understand when and how the "MeasurementPeriodRanges" event is required, one would need to refer to the specific section of the Matter specification that describes the conformance for 'Ranges'.

2.13.7.1. MeasurementPeriodRanges Event
If supported, this event SHALL be generated at the end of a measurement period. The start and end
times for measurement periods SHALL be determined by the server, and MAY represent overlap
ping periods.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event within the Electrical Power Measurement Cluster, specifically the "Ranges" event. This event is identified by the ID '0' and is of the type 'list[MeasurementRangeStruct]', indicating it involves a list of structures that define measurement ranges. The default value for this event is 'R V', though the specifics of this default are not detailed in the provided data. The conformance rule for this event is 'M', which stands for Mandatory. This means that the "Ranges" event is always required to be implemented in any device or application that supports the Electrical Power Measurement Cluster, without any conditions or exceptions.

2.13.7.1.1. Ranges Field
This SHALL indicate the value of the Ranges attribute at the time of event generation.
Chapter 3. Lighting
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter. References
to external documents are contained in Chapter 1 and are made using [Rn] notation.
3.1. General Description

## Introduction
The clusters specified in this document are for use typically in lighting applications, but MAY be
used in any application domain.

## Terms
Ballast Factor: A measure of the light output (lumens) of a ballast and lamp combination in com
parison to an ANSI standard ballast operated with the same lamp. Multiply the ballast factor by the
rated lumens of the lamp to get the light output of the lamp/ballast combination.
HSV: Hue, Saturation, Value. A color space, also known as HSB (Hue, Saturation, Brightness). This is
a well-known transformation of the RGB (Red, Green, Blue) color space. For more information see
e.g., http://en.wikipedia.org/wiki/HSV_color_space.
Illuminance: The density of incident luminous flux on a surface. Illuminance is the standard met
ric for lighting levels, and is measured in lux (lx).

## Cluster List
This section lists the lighting specific clusters as specified in this chapter.
Table 6. Overview of the Lighting Clusters

_Table parsed from section 'Cluster List':_

* The table row describes the "Color Control" cluster within the context of the Electrical Power Measurement Cluster's Cluster List. This cluster, identified by the Cluster ID '0x0300', includes attributes and commands specifically designed for managing the color settings of a light that is capable of color adjustments. The conformance rule for this cluster is not explicitly provided in the data you shared, but if we assume a typical scenario, it might involve conditions based on the presence of certain features or capabilities in the device. For example, if the conformance were something like `OO, O`, it would mean that the Color Control cluster is mandatory if the OnOff feature is supported; otherwise, it is optional. However, without the specific conformance string, we can only describe the general purpose and potential conditionality of the cluster's inclusion based on the Matter specification guidelines.

* The table row entry describes the "Ballast Configuration" cluster within the Electrical Power Measurement Cluster, identified by the Cluster ID '0x0301'. This cluster includes attributes and commands specifically for configuring a lighting ballast. The conformance rule for this cluster is not explicitly provided in the data you shared, but based on the context, it would typically indicate whether the inclusion of this cluster is mandatory, optional, or subject to certain conditions within a device's implementation. If the conformance rule were provided, it would specify under what conditions this cluster must be supported, using the conformance tags and expressions outlined in the Matter Conformance Interpretation Guide. For example, if the conformance were 'M', it would mean that the Ballast Configuration cluster is always required in devices implementing the Electrical Power Measurement Cluster.

