
# 2.12 Electrical Energy Measurement Cluster

This cluster provides a mechanism for querying data about the electrical energy imported or pro
vided by the server.

## Data Types
2.12.5.1. EnergyMeasurementStruct Type
This struct SHALL indicate the amount of energy measured during a given measurement period.
A server which does not have the ability to determine the time in UTC, or has not yet done so,
SHALL use the system time fields to specify the measurement period and observation times.
A server which has determined the time in UTC SHALL use the timestamp fields to specify the mea
surement period. Such a server MAY also include the systime fields to indicate how many seconds
had passed since boot for a given timestamp; this allows for client-side resolution of UTC time for
previous reports that only included systime.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Electrical Energy Measurement Cluster, specifically a data type named "Energy" with an ID of '0'. This element is of the type 'energy-mWh' and is constrained to values ranging from 0 to 262. The conformance rule for this element is 'M', which stands for Mandatory. This means that the "Energy" data type is always required to be implemented within the Electrical Energy Measurement Cluster, without any conditions or exceptions. It is a fundamental component that must be supported in any implementation of this cluster according to the Matter specification.

* The table row entry pertains to the "StartTimestamp" data type within the Electrical Energy Measurement Cluster, specifically under the Data Types section. The "StartTimestamp" is identified by the ID '1' and is of the type 'epoch-s', which likely represents a timestamp in seconds since the epoch (a common time representation in computing). The conformance for this entry is marked as 'desc', indicating that the rules governing when and how this data type is required are too complex to be captured by a simple conformance tag or expression. Instead, its conformance is detailed elsewhere in the documentation, suggesting that its usage might depend on various conditions or scenarios that require further explanation beyond the basic conformance tags and expressions.

* The table row describes an attribute named "EndTimestamp" within the Electrical Energy Measurement Cluster's Data Types section. This attribute is of the type "epoch-s," which likely refers to a timestamp in seconds since the epoch. It has a constraint that specifies it must be at least one second greater than the "StartTimestamp." The conformance for "EndTimestamp" is marked as "desc," indicating that its conformance requirements are too complex to be captured by a simple tag or expression and are instead detailed elsewhere in the documentation. This means that to fully understand when and how "EndTimestamp" should be implemented, one would need to refer to additional descriptive information provided in the specification.

* The table row entry pertains to the "StartSystime" data type within the Electrical Energy Measurement Cluster's Data Types section. The "StartSystime" is identified by the ID '3' and is of the type 'systime-ms'. The conformance for this data type is marked as 'desc', indicating that its conformance requirements are too complex to be captured by a simple tag or expression. Instead, the specific conditions and rules governing its implementation are detailed elsewhere in the documentation. This means that to fully understand when and how "StartSystime" should be implemented, one would need to refer to the additional descriptive information provided in the broader specification.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Electrical Energy Measurement Cluster, specifically under the Data Types section. The element is identified by the ID '4' and is named 'EndSystime'. It is of the type 'systime-ms', which likely refers to a system time measured in milliseconds. The constraint for this element is that it must be at least one millisecond greater than 'StartSystime', indicating a dependency on another element. The conformance for 'EndSystime' is marked as 'desc', meaning that its conformance requirements are too complex to be captured by a simple tag or expression and are detailed elsewhere in the documentation. This implies that users must refer to additional documentation to fully understand when and how 'EndSystime' should be implemented.

2.12.5.1.1. Energy Field
This field SHALL be the reported energy.
If the EnergyMeasurementStruct represents cumulative energy, then this SHALL represent the
cumulative energy recorded at either the value of the EndTimestamp field or the value of the
EndSystime field, or both.
If the EnergyMeasurementStruct represents periodic energy, then this SHALL represent the energy
recorded during the period specified by either the StartTimestamp and EndTimestamp fields, the
period specified by the StartSystime and EndSystime fields, or both.
2.12.5.1.2. StartTimestamp Field
This field SHALL indicate the timestamp in UTC of the beginning of the period during which the
value of the Energy field was measured.
If this EnergyMeasurementStruct represents cumulative energy, this field SHALL be omitted.
Otherwise, if the server had determined the time in UTC at or before the beginning of the measure
ment period, this field SHALL be indicated.
Otherwise, if the server had not yet determined the time in UTC at or before the beginning of the
measurement period, or does not have the capability of determining the time in UTC, this field
SHALL be omitted.
2.12.5.1.3. EndTimestamp Field
This field SHALL indicate the timestamp in UTC of the end of the period during which the value of
the Energy field was measured.
If the server had determined the time in UTC by the end of the measurement period, this field
SHALL be indicated.
Otherwise, if the server had not yet determined the time in UTC by the end of the measurement
period, or does not have the capability of determining the time in UTC, this field SHALL be omitted.
2.12.5.1.4. StartSystime Field
This field SHALL indicate the time elapsed since boot at the beginning of the period during which
the value of the Energy field was measured.
If this EnergyMeasurementStruct represents cumulative energy, this field SHALL be omitted.
Otherwise, if the server had not yet determined the time in UTC at the start of the measurement
period, or does not have the capability of determining the time in UTC, this field SHALL be indi
cated.
Otherwise, if the server had determined the time in UTC at or before the beginning of the measure
ment period, this field MAY be omitted; if it is indicated, its value SHALL be the time elapsed since
boot at the UTC time indicated in StartTimestamp.
2.12.5.1.5. EndSystime Field
This field SHALL indicate the time elapsed since boot at the end of the period during which the
value of the Energy field was measured.
If the server had not yet determined the time in UTC by the end of the measurement period, or does
not have the capability of determining the time in UTC, this field SHALL be indicated.
Otherwise, if the server had determined the time in UTC by the end of the measurement period, this
field MAY be omitted; if it is indicated, its value SHALL be the time elapsed since boot at the UTC
time indicated in EndTimestamp.
2.12.5.2. CumulativeEnergyResetStruct Type
This struct SHALL represent the times at which cumulative measurements were last zero, either
due to initialization of the device, or an internal reset of the cumulative value.

_Table parsed from section 'Data Types':_

* In the context of the Electrical Energy Measurement Cluster, the data type entry for 'ImportedResetTimestamp' is identified by the ID '0' and is of the type 'epoch-s'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The default value for this data type is 'null'. The conformance rule '[IMPE]' specifies that the 'ImportedResetTimestamp' is optional if the feature 'IMPE' is supported. This means that if the 'IMPE' feature is present, the 'ImportedResetTimestamp' can be included, but it is not required. If 'IMPE' is not supported, the element is neither mandatory nor optional, as it is disallowed by the 'Quality' designation.

* The table row entry for the Electrical Energy Measurement Cluster within the Data Types section describes an element with the ID '1' named 'ExportedResetTimestamp'. This element is of the type 'epoch-s', indicating it represents a timestamp in epoch seconds. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality. The default value for this element is 'null', indicating it does not have a predefined value. The 'Conformance' field is specified as '[EXPE]', which means that the 'ExportedResetTimestamp' is optional if the feature 'EXPE' is supported. If 'EXPE' is not supported, the element is not required. This conformance rule allows for flexibility in implementation based on the presence of the 'EXPE' feature.

* The table row entry for the Electrical Energy Measurement Cluster under the Data Types section describes an element named 'ImportedResetSystime' with an ID of '2'. This element is of the type 'systime-ms' and has a quality designation of 'X', indicating that it is explicitly disallowed. The default value for this element is 'null'. The conformance rule '[IMPE]' specifies that the 'ImportedResetSystime' element is optional if the feature 'IMPE' is supported. This means that in implementations where the 'IMPE' feature is present, the 'ImportedResetSystime' element can be included but is not required. However, if 'IMPE' is not supported, the element should not be included, as indicated by its disallowed quality.

* The table row entry for the Electrical Energy Measurement Cluster, specifically within the Data Types section, describes an element named 'ExportedResetSystime' with an ID of '3'. This element is of the type 'systime-ms' and has a quality designation of 'X', indicating that it is explicitly disallowed. The default value for this element is 'null'. The conformance rule '[EXPE]' indicates that the 'ExportedResetSystime' element is optional if the feature 'EXPE' is supported. In summary, 'ExportedResetSystime' is not allowed by default, but if the 'EXPE' feature is present, it becomes an optional element within the cluster.

2.12.5.2.1. ImportedResetTimestamp Field
This field SHALL indicate the timestamp in UTC when the value of the Energy field on the Cumula
tiveEnergyImported attribute was most recently zero.
If the server had determined the time in UTC when the value of the Energy field on the Cumula
tiveEnergyImported attribute was most recently zero, this field SHALL be indicated.
Otherwise, if the server had not yet determined the time in UTC when the value of the Energy field
on the CumulativeEnergyImported attribute was most recently zero, or does not have the capability
of determining the time in UTC, this field SHALL be omitted.
If the timestamp in UTC when the value of the Energy field on the CumulativeEnergyImported
attribute  was  most  recently  zero  cannot  currently  be  determined,  a  value  of  null  SHALL  be
returned.
2.12.5.2.2. ExportedResetTimestamp Field
This field SHALL indicate the timestamp in UTC when the value of the Energy field on the Cumula
tiveEnergyExported attribute was most recently zero.
If the server had determined the time in UTC when the value of the Energy field on the Cumula
tiveEnergyExported attribute was most recently zero, this field SHALL be indicated.
Otherwise, if the server had not yet determined the time in UTC when the value of the Energy field
on the CumulativeEnergyExported attribute was most recently zero, or does not have the capability
of determining the time in UTC, this field SHALL be omitted.
If the timestamp in UTC when the value of the Energy field on the CumulativeEnergyExported
attribute  was  most  recently  zero  cannot  currently  be  determined,  a  value  of  null  SHALL  be
returned.
2.12.5.2.3. ImportedResetSystime Field
This field SHALL indicate the time elapsed since boot when the value of the Energy field on the
CumulativeEnergyImported attribute was most recently zero.
If the server had not yet determined the time in UTC when the value of the Energy field on the
CumulativeEnergyImported attribute was most recently zero, or does not have the capability of
determining the time in UTC, this field SHALL be indicated.
Otherwise, if the server had determined the time in UTC when the value of the Energy field on the
CumulativeEnergyImported attribute was most recently zero, this field MAY be omitted; if it is indi
cated, its value SHALL be the time elapsed since boot at the UTC time indicated in ImportedReset
Timestamp.
2.12.5.2.4. ExportedResetSystime Field
This field SHALL indicate the time elapsed since boot when the value of the Energy field on the
CumulativeEnergyExported attribute was most recently zero.
If the server had not yet determined the time in UTC when the value of the Energy field on the
CumulativeEnergyExported attribute was most recently zero, or does not have the capability of
determining the time in UTC, this field SHALL be indicated.
Otherwise, if the server had determined the time in UTC when the value of the Energy field on the
CumulativeEnergyExported attribute was most recently zero, this field MAY be omitted; if it is indi
cated, its value SHALL be the time elapsed since boot at the UTC time indicated in ImportedReset
Timestamp.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Electrical Energy Measurement Cluster, specifically the "Accuracy" attribute, which is identified by the ID '0x0000'. This attribute is of the type 'MeasurementAccuracyStruct' and has a quality designation of 'F'. It is accessible with read and view permissions, as indicated by 'R V'. The conformance rule for this attribute is 'M', meaning it is mandatory. This implies that the "Accuracy" attribute is always required to be implemented in any device or application that supports the Electrical Energy Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute named "CumulativeEnergyImported" within the Electrical Energy Measurement Cluster. This attribute has an ID of '0x0001' and is of the type 'EnergyMeasurementStruct'. The 'Quality' field indicates that this attribute is disallowed ('X') and has a quality of 'Q'. The 'Default' value is 'null', and it has read ('R') and volatile ('V') access permissions. The conformance rule 'IMPE & CUME' means that this attribute is mandatory if both the 'IMPE' and 'CUME' features are supported. If either of these features is not supported, the attribute is not required.

* The table row describes an attribute named "CumulativeEnergyExported" within the Electrical Energy Measurement Cluster. This attribute has an ID of '0x0002' and is of the type 'EnergyMeasurementStruct'. Its quality is marked as 'X Q', indicating that it is disallowed and possibly qualified in some way, and it has a default value of 'null'. The access level is 'R V', meaning it is readable and volatile. The conformance rule 'EXPE & CUME' specifies that this attribute is mandatory if both the 'EXPE' and 'CUME' features are supported. If either or both of these features are not supported, the attribute is not required. This logical AND condition ensures that the attribute is only implemented when both specified features are present, aligning with the specific needs of devices that support these features.

* The table row describes an attribute named "PeriodicEnergyImported" within the Electrical Energy Measurement Cluster. This attribute has an ID of '0x0003' and is of the type 'EnergyMeasurementStruct'. The 'Quality' is marked as 'X Q', indicating that it is disallowed and has some quality considerations. The 'Default' value is 'null', and the 'Access' is specified as 'R V', meaning it is readable and volatile. The 'Conformance' field is defined as 'IMPE & PERE', which means that the "PeriodicEnergyImported" attribute is mandatory if both the 'IMPE' and 'PERE' features are supported. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute within the Electrical Energy Measurement Cluster, specifically the 'PeriodicEnergyExported' attribute, identified by ID '0x0004'. This attribute is of the type 'EnergyMeasurementStruct' and has a default value of 'null'. The quality is marked as 'X Q', indicating it is disallowed and has some quality considerations. The access is 'R V', meaning it is readable and volatile. The conformance rule 'EXPE & PERE' indicates that the 'PeriodicEnergyExported' attribute is mandatory if both the 'EXPE' and 'PERE' features are supported. If either of these features is not supported, the attribute is not required.

* The table row describes an attribute named "CumulativeEnergyReset" within the Electrical Energy Measurement Cluster. This attribute has an ID of '0x0005' and is of the type 'CumulativeEnergyResetStruct'. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed. The 'Default' value is 'null', and the 'Access' is specified as 'R V', which typically denotes read and view permissions. The 'Conformance' field is '[CUME]', meaning that the attribute is optional if the condition 'CUME' is true. However, given the 'Quality' is 'X', the attribute is not allowed regardless of the conformance condition.

2.12.6.1. Accuracy Attribute
This attribute SHALL indicate the accuracy of energy measurement by this server. The value of the
MeasurementType field on this MeasurementAccuracyStruct SHALL be ElectricalEnergy.
2.12.6.2. CumulativeEnergyImported Attribute
This attribute SHALL indicate the most recent measurement of cumulative energy imported by the
server over the lifetime of the device, and the timestamp of when the measurement was recorded.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the cumulative energy imported cannot currently be determined, a value of null SHALL be
returned.
2.12.6.3. CumulativeEnergyExported Attribute
This attribute SHALL indicate the most recent measurement of cumulative energy exported by the
server over the lifetime of the device, and the timestamp of when the measurement was recorded.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the cumulative energy exported cannot currently be determined, a value of null SHALL be
returned.
2.12.6.4. PeriodicEnergyImported Attribute
This attribute SHALL indicate the most recent measurement of energy imported by the server and
the period during which it was measured.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the periodic energy imported cannot currently be determined, a value of null SHALL be returned.
2.12.6.5. PeriodicEnergyExported Attribute
This attribute SHALL indicate the most recent measurement of energy exported by the server and
the period during which it was measured.
The reporting interval of this attribute SHALL be manufacturer dependent. The server MAY choose
to omit publication of deltas considered not meaningful.
The server SHALL NOT mark this attribute ready for report if the last time this was done was more
recently than 1 second ago.
The server MAY delay marking this attribute ready for report for longer periods if needed, however
the server SHALL NOT delay marking this attribute as ready for report for longer than 60 seconds.
If the periodic energy exported cannot currently be determined, a value of null SHALL be returned.
2.12.6.6. CumulativeEnergyReset Attribute
This attribute SHALL indicate when cumulative measurements were most recently zero.

## Events
This cluster SHALL support these events:

_Table parsed from section 'Events':_

* The table row describes an event within the Electrical Energy Measurement Cluster, specifically the "CumulativeEnergyMeasured" event, which has an ID of '0'. This event is categorized with a priority level of 'INFO' and has an access level of 'V', indicating it is viewable. The conformance rule for this event is specified as 'CUME'. According to the Matter Conformance Interpretation Guide, 'CUME' is a feature code that determines the conditions under which this event is mandatory. If the feature 'CUME' is supported, the "CumulativeEnergyMeasured" event is required to be implemented. If 'CUME' is not supported, the event is not required. This conformance rule ensures that the event is only mandatory in contexts where the relevant feature is applicable.

* The table row describes an event named "PeriodicEnergyMeasured" within the Electrical Energy Measurement Cluster, specifically under the Events section. This event has an ID of '1' and is classified with a priority level of 'INFO', indicating it provides informational updates. The access level is marked as 'V', suggesting it is visible or accessible in some manner. The conformance rule for this event is 'PERE', which, according to the Matter Conformance Interpretation Guide, indicates that the conformance is described elsewhere in the documentation. This means that the specific conditions or requirements for this event's implementation are too complex to be captured by a simple tag or expression and require further detailed explanation in the accompanying documentation.

2.12.7.1. CumulativeEnergyMeasured Event
This  event  SHALL  be  generated  when  the  server  takes  a  snapshot  of  the  cumulative  energy
imported by the server, exported from the server, or both, but not more frequently than the rate
mentioned in the description above of the related attribute.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event named "EnergyImported" within the Electrical Energy Measurement Cluster, identified by the ID '0' and structured as an "EnergyMeasurementStruct" type. The conformance rule for this event is expressed as "CUME & IMPE," indicating that the "EnergyImported" event is mandatory if both the CUME (Cumulative Energy) and IMPE (Imported Energy) features are supported. This means that for devices implementing this cluster, the "EnergyImported" event must be included if the device supports both of these specific energy measurement features. If either or both of these features are not supported, the event is not required.

* The table row describes an event named "EnergyExported" within the Electrical Energy Measurement Cluster, specifically under the Events section. This event is of the type "EnergyMeasurementStruct." The conformance rule for this event is expressed as "CUME & EXPE," which means that the "EnergyExported" event is mandatory if both the CUME (Cumulative Energy) feature and the EXPE (Exported Energy) feature are supported by the device. If either or both of these features are not supported, the event is not required. This conformance condition ensures that the event is only implemented when the device has the necessary capabilities to measure and report exported energy cumulatively.

2.12.7.1.1. EnergyImported Field
This field SHALL be the value of CumulativeEnergyImported attribute at the timestamp indicated in
its EndTimestamp field, EndSystime field, or both.
2.12.7.1.2. EnergyExported Field
This field SHALL be the value of CumulativeEnergyExported attribute at the timestamp indicated in
its EndTimestamp field, EndSystime field, or both.
2.12.7.2. PeriodicEnergyMeasured Event
This event SHALL be generated when the server reaches the end of a reporting period for imported
energy, exported energy, or both.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event named "EnergyImported" within the Electrical Energy Measurement Cluster, identified by ID '0' and structured as an "EnergyMeasurementStruct" type. The conformance rule 'PERE & IMP' indicates that the "EnergyImported" event is mandatory if both the PERE (Presumably a feature related to energy reporting) and IMP (Possibly a feature related to energy importation) features are supported. This means that the presence of this event is conditional upon the support of both these features, making it a required element in implementations where both conditions are met.

* The table row describes an event named "EnergyExported" within the Electrical Energy Measurement Cluster, specifically in the Events section. This event is of the type "EnergyMeasurementStruct." The conformance rule for "EnergyExported" is expressed as "PERE & EXPE." According to the Matter Conformance Interpretation Guide, this means that the "EnergyExported" event is mandatory if both the "PERE" and "EXPE" features are supported. If either or both of these features are not supported, the event is not required. The conformance does not specify any provisional, deprecated, or optional status outside of this condition, indicating that the presence of both features is crucial for the mandatory inclusion of this event.

PERE & IMPE
PERE & EXPE
2.12.7.2.1. EnergyImported Field
This field SHALL be the value of PeriodicEnergyImported attribute at the timestamp indicated in its
EndTimestamp field, EndSystime field, or both.
2.12.7.2.2. EnergyExported Field
This field SHALL be the value of PeriodicEnergyExported attribute at the timestamp indicated in its
EndTimestamp field, EndSystime field, or both.