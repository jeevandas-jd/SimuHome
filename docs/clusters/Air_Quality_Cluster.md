
# 2.9 Air Quality Cluster

This cluster provides an interface to air quality classification using distinct levels with human-read
able labels.

## Data Types
2.9.5.1. AirQualityEnum Type
This data type is derived from enum8.
The AirQualityEnum provides a representation of the quality of the analyzed air. It is up to the
device manufacturer to determine the mapping between the measured values and their corre
sponding enumeration values.

_Table parsed from section 'Data Types':_

* In the Air Quality Cluster, under the Data Types section, the entry for 'Value' 0 is named 'Unknown' and is summarized as indicating that the air quality is unknown. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Unknown' data type is always required to be implemented in any system or device that supports the Air Quality Cluster, ensuring that there is a standard way to represent situations where the air quality cannot be determined.

* In the context of the Air Quality Cluster, specifically within the Data Types section, the table row describes an entry with the name "Good," which has a value of '1'. This entry summarizes that the air quality is good. The conformance rule for this entry is marked as 'M', indicating that it is mandatory. This means that the "Good" air quality status must always be included and supported in any implementation of the Air Quality Cluster, without any conditions or exceptions.

* In the context of the Air Quality Cluster's Data Types, the table entry describes a data type with the value '2', named 'Fair', which indicates that the air quality is fair. The conformance rule 'FAIR' suggests that this element is mandatory if the feature or condition 'FAIR' is supported. If the 'FAIR' condition is true, then this data type must be included in the implementation of the Air Quality Cluster. The conformance rule does not specify any alternative conditions or optionality, implying a straightforward requirement based on the presence of the 'FAIR' feature.

* In the Air Quality Cluster, under the Data Types section, the entry with the value '3' is named 'Moderate' and summarizes that the air quality is moderate. The conformance rule 'MOD' indicates that this element is Mandatory, Optional, and Deprecated. This means that the 'Moderate' air quality status is always required (Mandatory) in some contexts, not required but available (Optional) in others, and considered obsolete (Deprecated) in yet other contexts. The specific application of each conformance status would depend on additional context or conditions not provided in this row.

* In the context of the Air Quality Cluster's Data Types, the table row describes an entry with the value '4', named 'Poor', which summarizes the air quality as poor. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that within the Air Quality Cluster, the 'Poor' air quality designation must always be included and supported as part of the implementation, without any conditions or exceptions.

* In the Air Quality Cluster, under the Data Types section, the entry for 'VeryPoor' with a value of '5' indicates that this data type represents a condition where the air quality is very poor. The summary succinctly describes this state. The conformance rule 'VPOOR' implies that the inclusion or requirement of this data type is contingent upon the support of a feature or condition labeled 'VPOOR'. According to the conformance interpretation guide, since 'VPOOR' is not enclosed in brackets, it means that the 'VeryPoor' data type is mandatory if the 'VPOOR' feature is supported. If 'VPOOR' is not supported, the conformance of this data type is not specified in this entry.

* In the Air Quality Cluster, under the Data Types section, the entry for 'ExtremelyPoor' with a value of '6' indicates a condition where the air quality is extremely poor. The conformance rule 'XPOOR' specifies that this element is disallowed if the feature 'XPOOR' is supported. In other words, if the system or device supports the 'XPOOR' feature, the 'ExtremelyPoor' data type should not be included or used. This rule ensures that the presence of the 'XPOOR' feature explicitly prohibits the use of this particular air quality indicator.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Air Quality Cluster, specifically the 'AirQuality' attribute. This attribute is identified by the ID '0x0000' and is of the type 'AirQualityEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The default value for this attribute is '0', and it has 'R V' access, meaning it is readable and has a volatile nature. The 'Conformance' is marked as 'M', which means that this attribute is mandatory and must always be implemented in any device or application that supports the Air Quality Cluster.

2.9.6.1. AirQuality Attribute
This attribute SHALL indicate a value from AirQualityEnum that is indicative of the currently mea
sured air quality.
2.10. Concentration Measurement Clusters
The server cluster provides an interface to concentration measurement functionality.
This cluster SHALL to be used via an alias to a specific substance (see Cluster IDs).

## Cluster IDs
The table below is a list of Cluster IDs that conform to this specification.

_Table parsed from section 'Cluster IDs':_

* The table row entry pertains to the Air Quality Cluster, specifically within the context of Cluster IDs, and it describes a feature named "Carbon Monoxide Concentration Measurement" with an ID of '0x040C' and a PICS (Protocol Implementation Conformance Statement) code of 'CMOCONC'. The conformance rule for this feature is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, the conformance would typically indicate whether this feature is mandatory, optional, provisional, deprecated, or disallowed, or if its requirement depends on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirement status of this feature, but it would be interpreted according to the rules outlined in the guide, such as being mandatory if a certain feature is supported or optional under specific conditions.

* The table row describes an entry within the Air Quality Cluster, specifically focusing on the "Carbon Dioxide Concentration Measurement" with the ID '0x040D' and PICS code 'CDOCONC'. The conformance rule for this entry is not explicitly provided in the data you shared, but if we assume a typical conformance scenario, it might be something like "M" for mandatory, indicating that this measurement feature is always required for devices implementing the Air Quality Cluster. If the conformance rule were more complex, such as involving conditional expressions or dependencies on other features, it would specify under what conditions the feature is mandatory, optional, or otherwise. Without the specific conformance string, we can only infer that this entry is a key component of the Air Quality Cluster, likely essential for monitoring carbon dioxide levels in an IoT environment.

* The table row entry pertains to the "Nitrogen Dioxide Concentration Measurement" within the Air Quality Cluster, identified by the ID '0x0413'. The PICS (Protocol Implementation Conformance Statement) code for this feature is 'NDOCONC'. The conformance rule for this entry is not explicitly provided in the data given, but if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would specify the conditions under which this feature is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the Nitrogen Dioxide Concentration Measurement is a mandatory feature for any implementation of the Air Quality Cluster. If it were 'O', it would be optional, meaning it could be included at the implementer's discretion without any dependencies. The actual conformance string would provide specific guidance on how this feature should be implemented in accordance with the Matter specification.

* The table row entry for the Air Quality Cluster under the section "Cluster IDs" describes an element with the ID `0x0415`, named "Ozone Concentration Measurement," and associated with the PICS (Protocol Implementation Conformance Statement) code `OZCONC`. The conformance rule for this element is not explicitly provided in the data, so we cannot directly interpret its conformance status using the guide. However, typically, such entries would specify whether the element is mandatory, optional, or subject to certain conditions based on the presence or absence of specific features. In this context, the "Ozone Concentration Measurement" likely pertains to the capability of a device to measure ozone levels, and its inclusion in a device's implementation would depend on the conformance rules outlined in the Matter specification, which are not detailed here.

* The table row describes an element within the Air Quality Cluster, specifically the "PM2.5 Concentration Measurement" identified by the ID '0x042A'. This element is associated with the PICS (Protocol Implementation Conformance Statement) code 'PMICONC'. The conformance rule for this element is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, we can infer that its inclusion in a device's implementation depends on specific conditions or requirements outlined elsewhere in the documentation. If the conformance string were provided, it would define whether this measurement is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on other features or elements. Without the conformance string, we assume that further details are described in the documentation or that it follows a default conformance rule for the cluster.

* The table row describes an element within the Air Quality Cluster, specifically the "Formaldehyde Concentration Measurement" with an ID of '0x042B' and a PICS (Protocol Implementation Conformance Statement) code of 'FLDCONC'. The conformance rule for this element is not explicitly provided in the row data, but based on the context of the Matter Conformance Interpretation Guide, it would typically specify the conditions under which this measurement is required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the Formaldehyde Concentration Measurement is always mandatory for devices implementing this cluster. If the conformance were a more complex expression, it would define specific conditions under which the measurement is required or optional, using logical operators and feature codes. Without the specific conformance string, we can only infer that this entry is part of the Air Quality Cluster and involves measuring formaldehyde concentration, which is crucial for assessing air

* The table row describes an element within the Air Quality Cluster, specifically the "PM1 Concentration Measurement" with an ID of '0x042C'. This element is identified by the PICS code 'PMHCONC'. The conformance rule for this element is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, we would interpret any given conformance string to determine when this element is required. For example, if the conformance were 'M', it would mean that the PM1 Concentration Measurement is always mandatory. If it were 'O', it would be optional with no dependencies. Without a specific conformance string provided, we can only describe the element and its context, but not its specific conformance requirements.

* The table row entry pertains to the Air Quality Cluster, specifically focusing on the 'PM10 Concentration Measurement' with the ID '0x042D' and PICS code 'PMKCONC'. This entry represents a feature within the Matter IoT specification that deals with measuring the concentration of PM10 particles in the air. The conformance rule for this feature is not explicitly provided in the row data, but based on the context and typical usage, it would likely be described elsewhere in the documentation. Generally, this means that the conformance of the 'PM10 Concentration Measurement' feature is complex and requires additional documentation to fully understand when and how it should be implemented, potentially involving conditional requirements based on other features or device capabilities.

* The table row describes an entry within the Air Quality Cluster, specifically focusing on the "Total Volatile Organic Compounds Concentration Measurement" with the ID '0x042E' and PICS code 'TVOCCONC'. The conformance rule for this entry is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string to determine the conditions under which this measurement is required or optional. If the conformance string were, for example, 'M', it would mean that this measurement is mandatory for all devices implementing the Air Quality Cluster. If it were 'O', it would be optional, allowing implementers to choose whether to include it. Without the specific conformance string, we cannot definitively state its requirement status, but the guide provides a framework for understanding how such rules are applied.

* The table row describes an element within the Air Quality Cluster, specifically the "Radon Concentration Measurement" with the ID '0x042F' and PICS code 'RNCONC'. The conformance rule for this element is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we can infer that the conformance of this element would be determined by additional context or documentation not included here. Typically, such an element could be marked as Mandatory (M), Optional (O), or subject to more complex conditions involving logical expressions or dependencies on other features. Without the specific conformance string, we cannot definitively state its requirement status, but it would be essential to refer to the full documentation to understand its role and necessity within the Air Quality Cluster.

## Data Types
2.10.5.1. MeasurementUnitEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Air Quality Cluster, specifically within the Data Types section, the table row describes an entry with the name "PPM," which stands for "Parts per Million (10^6)." This entry is associated with a value of '0' and is used to represent air quality measurements in terms of parts per million. The conformance rule for this entry is 'MEA,' which indicates that the PPM data type is mandatory when the MEA (Measurement) feature is supported. This means that if the Air Quality Cluster supports the measurement feature, the PPM data type must be implemented as part of the cluster's functionality.

* In the Air Quality Cluster's Data Types section, the table row describes a data type with the name "PPB," which stands for "Parts per Billion (10^9)." This data type is represented by the value '1' and is used to quantify air quality measurements in terms of parts per billion. The conformance rule for this data type is specified as "MEA." According to the Matter Conformance Interpretation Guide, this means that the "PPB" data type is mandatory (M) if the feature or condition represented by "MEA" is supported. If "MEA" is not supported, the conformance of "PPB" is not explicitly defined in this entry, implying that it might not be required or that further documentation should be consulted for additional context.

* In the context of the Air Quality Cluster's Data Types, the table entry describes a data type named "PPT," which stands for "Parts per Trillion (10^12)." The 'Value' assigned to this data type is '2'. The conformance rule for this entry is 'MEA', which, according to the Matter Conformance Interpretation Guide, indicates that the data type is Mandatory ('M') when the condition 'EA' is true. This means that if the feature or condition represented by 'EA' is supported, the 'PPT' data type must be implemented. If 'EA' is not supported, the conformance of 'PPT' is not specified in this entry, implying it may not be required.

* In the Air Quality Cluster's Data Types section, the table row describes a data type with the value '3', named 'MGM3', which stands for 'Milligram per m3'. This data type is used to represent air quality measurements in terms of milligrams per cubic meter. The conformance rule for this entry is 'MEA', which, according to the Matter Conformance Interpretation Guide, indicates that this element is mandatory when the MEA feature is supported. Therefore, if the MEA feature is part of the implementation, the 'MGM3' data type must be included.

* In the context of the Air Quality Cluster's Data Types, the table row describes an entry with the value '4', named 'UGM3', which stands for 'Microgram per m3'. This entry represents a unit of measurement used to quantify air quality data. The conformance rule 'MEA' indicates that this element is mandatory when the MEA (Measurement) feature is supported. This means that if the device or system supports the Measurement feature, it must include the 'UGM3' unit of measurement as part of its implementation.

* The table row describes a data type within the Air Quality Cluster, specifically for the unit "NGM3," which stands for "Nanogram per cubic meter." This unit is assigned a value of '5' and is used to represent air quality measurements in terms of nanograms per cubic meter. The conformance rule for this entry is 'MEA,' which indicates that the use of this data type is mandatory when the MEA (Measurement) feature is supported. In other words, if the Air Quality Cluster supports the MEA feature, then the NGM3 unit must be implemented as part of the system.

* The table row entry pertains to the Air Quality Cluster within the Data Types section, specifically focusing on a data type labeled 'PM3', which represents 'Particles per m3'. The 'Value' assigned to this data type is '6'. The 'Conformance' field for this entry is marked as 'MEA', which, according to the Matter Conformance Interpretation Guide, indicates that this element is Mandatory ('M') when the condition 'EA' is true. However, since 'EA' is not defined in the provided context, we interpret 'MEA' as a straightforward mandatory requirement, meaning that the 'PM3' data type is always required to be implemented in any device or application that supports the Air Quality Cluster.

_Table parsed from section 'Data Types':_

* In the Air Quality Cluster's Data Types section, the table entry describes a data type with the value '7', named 'BQM3', which represents the unit 'Becquerel per m3'. The conformance rule for this entry is 'MEA', which, according to the Matter Conformance Interpretation Guide, indicates that this element is Mandatory. This means that the 'BQM3' data type is always required to be implemented in any system or device that supports the Air Quality Cluster, ensuring consistent measurement and reporting of air quality in terms of Becquerel per cubic meter.

9 12
Where mentioned, Billion refers to 10 , Trillion refers to 10  (short scale).
2.10.5.2. MeasurementMediumEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Air Quality Cluster's Data Types, the table entry describes a data type with the value '0' and the name 'Air', which indicates that the measurement is being made in air. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the element is always required in any implementation of the Air Quality Cluster. There are no conditions or dependencies affecting its requirement; it must be included to conform to the Matter specification for this cluster.

* In the context of the Air Quality Cluster's Data Types, the table row describes an entry with the name "Water," which has a value of '1' and a summary indicating that the measurement is being made in water. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the element is always required in the specification. Therefore, any implementation of the Air Quality Cluster must include support for this data type, ensuring that measurements in water are consistently recognized and processed.

* In the Air Quality Cluster, under the Data Types section, there is an entry with the name "Soil," which has a value of '2'. This entry indicates that the measurement is being made in soil. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Soil" data type is always required to be supported in any implementation of the Air Quality Cluster, without any conditions or exceptions.

2.10.5.3. LevelValueEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Air Quality Cluster, under the Data Types section, the table row describes an entry with the name "Unknown" and a summary indicating that the level is unknown. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "Unknown" data type is a required element within the Air Quality Cluster specification and must always be implemented. There are no conditions or dependencies affecting its mandatory status, making it an essential part of the cluster's data types.

* In the Air Quality Cluster, under the Data Types section, there is an entry for a data type named "Low" with a value of '1'. This entry signifies that the air quality level is considered "Low." The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Low" data type is always required to be implemented in any device or application that supports the Air Quality Cluster, without any conditions or exceptions.

* In the Air Quality Cluster, under the Data Types section, the entry for 'Medium' with a value of '2' indicates that this level is considered to be of medium air quality. The conformance rule 'MED' suggests that the inclusion or requirement of this element is dependent on a condition or feature named 'MED'. According to the Matter Conformance Interpretation Guide, if the condition 'MED' is true, then this element is mandatory. However, without further context or description of 'MED', it is not possible to determine the specific conditions under which this element is required.

* In the context of the Air Quality Cluster's Data Types, the table row entry describes a data type with the value '3', named 'High', which indicates that the air quality level is considered high. The conformance rule for this entry is marked as 'M', meaning that this data type is mandatory. This implies that within the Air Quality Cluster, the 'High' level must always be implemented and supported, as it is a required element of the specification.

* In the Air Quality Cluster, within the Data Types section, there is an entry for a data type named "Critical," which has a value of '4' and is summarized as "The level is considered Critical." The conformance rule for this entry is 'CRI.' According to the Matter Conformance Interpretation Guide, 'CRI' is not a standard conformance tag or expression as outlined in the guide, suggesting that it might be a shorthand or specific code relevant to this particular context or documentation. Without additional context or a definition for 'CRI,' it is unclear how this conformance should be interpreted based on the provided rules. Therefore, further documentation or clarification would be needed to understand the specific requirements or conditions under which the "Critical" data type is applicable or required.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Air Quality Cluster, specifically the 'MeasuredValue' attribute, identified by the ID '0x0000'. This attribute is of type 'single' and its value is constrained between 'MinMeasuredValue' and 'MaxMeasuredValue'. The 'Quality' field indicates that this attribute is disallowed ('X') but also provisional ('P'), suggesting that while it is currently not allowed, its status may change in the future. The default value for this attribute is 'null', and it has read ('R') and volatile ('V') access permissions. The conformance rule 'MEA' indicates that the 'MeasuredValue' attribute is mandatory if the feature 'MEA' is supported. In summary, this attribute is required in the Air Quality Cluster when the 'MEA' feature is present, though its current quality status is provisional and disallowed.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Air Quality Cluster, specifically the "MinMeasuredValue" attribute. This attribute is identified by the ID '0x0001' and is of type 'single', which likely refers to a single precision floating-point number. The 'Constraint' field indicates that this attribute applies universally ('all'), and its 'Quality' is marked as 'X', meaning it is explicitly disallowed in some contexts. The default value for this attribute is 'null', and it has read ('R') and volatile ('V') access permissions, suggesting that it can be read and may change frequently. The 'Conformance' field is 'MEA', which, according to the conformance interpretation guide, means that the attribute is mandatory if the feature 'MEA' is supported. If 'MEA' is not supported, the conformance rule does not specify an alternative, implying that the attribute is not required in such cases.

* The table row describes an attribute named "MaxMeasuredValue" within the Air Quality Cluster, identified by the ID '0x0002'. This attribute is of type 'single' and has a constraint that it must be at least as large as the 'MinMeasuredValue'. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed from having a quality designation. The default value for this attribute is 'null', and it has read and view access permissions, as indicated by 'R V'. The conformance rule 'MEA' suggests that the attribute is mandatory if the feature 'MEA' is supported. If 'MEA' is not supported, the conformance of this attribute is not specified in this entry, implying it might not be required.

* In the Air Quality Cluster, the attribute 'PeakMeasuredValue' with ID '0x0003' is of type 'single' and is constrained to values between 'MinMeasuredValue' and 'MaxMeasuredValue'. The quality of this attribute is marked as 'X P', indicating it is disallowed but provisionally included, suggesting it might be reconsidered in the future. The default value for this attribute is 'null', and it has read and volatile access ('R V'). The conformance rule 'PEA' indicates that the attribute is mandatory if the condition 'PEA' is true. However, without additional context on what 'PEA' represents, it is understood as a condition that, when met, requires the attribute to be implemented.

* The table row describes an attribute named "PeakMeasuredValueWindow" within the Air Quality Cluster. This attribute has an ID of '0x0004' and is of type 'elapsed-s', with a constraint that its maximum value is 604800. It is marked with a quality of 'P', indicating a provisional status, and has a default value of '1'. The access level is 'R V', meaning it is readable and has volatile characteristics. The conformance rule 'PEA' indicates that this attribute is mandatory if the feature 'PEA' is supported. If the feature 'PEA' is not supported, the conformance of this attribute is not explicitly defined in this entry, implying it may not be required or its status is described elsewhere.

* The table row describes an attribute within the Air Quality Cluster, specifically the 'AverageMeasuredValue' with an ID of '0x0005'. This attribute is of type 'single' and its value is constrained between 'MinMeasuredValue' and 'MaxMeasuredValue'. The 'Quality' field indicates that this attribute is disallowed ('X') but also provisional ('P'), suggesting it is currently not permitted but may be reconsidered in the future. The default value for this attribute is 'null', and it has read ('R') and volatile ('V') access permissions, meaning it can be read and its value may change without notice. The 'Conformance' field specifies 'AVG', which implies that the attribute is mandatory if the feature or condition represented by 'AVG' is supported. If 'AVG' is not supported, the attribute is not required.

* The table row describes an attribute named "AverageMeasuredValueWindow" within the Air Quality Cluster. This attribute has an ID of '0x0006' and is of type 'elapsed-s', with a constraint that it cannot exceed 604800 seconds. It is marked with a quality of 'P', indicating a provisional status, and has a default value of '1'. The access level is 'R V', meaning it is readable and volatile. The conformance rule 'AVG' indicates that this attribute is mandatory if the feature 'AVG' is supported. If 'AVG' is not supported, the attribute is not required. This suggests that the attribute's necessity is contingent upon the presence of the 'AVG' feature within the implementation.

* In the Air Quality Cluster, within the Attributes section, the entry for the attribute 'Uncertainty' is identified by the ID '0x0007' and is of the type 'single'. It has a constraint and default value of 'MS', and its access is defined as 'R V', indicating it is readable and has a volatile nature. The conformance rule '[MEA]' specifies that this attribute is optional if the feature 'MEA' is supported. This means that the presence of the 'Uncertainty' attribute is not mandatory but can be included if the 'MEA' feature is part of the device's capabilities.

* The table row describes an attribute within the Air Quality Cluster, specifically the "MeasurementUnit" attribute. This attribute has an ID of '0x0008' and is of the type 'MeasurementUnitEnum'. It is marked with a quality of 'F', indicating a specific quality level, and has a default value of 'MS'. The access level 'R V' suggests that the attribute is readable and possibly has additional access characteristics. The conformance rule 'MEA' indicates that the "MeasurementUnit" attribute is mandatory if the feature 'MEA' is supported. If 'MEA' is not supported, the conformance of this attribute is not explicitly defined in this entry, implying it may not be required.

* In the Air Quality Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0009' named 'MeasurementMedium'. This attribute is of the type 'MeasurementMediumEnum' and has a default value of 'MS'. It is marked with a quality of 'F', indicating a specific quality characteristic, and has access permissions of 'R V', meaning it can be read and is viewable. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the 'MeasurementMedium' attribute must always be implemented in any device or application that supports the Air Quality Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Air Quality Cluster, specifically the 'LevelValue' attribute. This attribute is identified by the ID '0x000A' and is of the type 'LevelValueEnum', with a default value of '0'. It has read and view access permissions, indicated by 'R V'. The conformance rule 'LEV' implies that the 'LevelValue' attribute is mandatory if the feature or condition represented by 'LEV' is supported. If 'LEV' is not supported, the attribute's inclusion is not required. This conformance rule ensures that the attribute is included in implementations where the relevant feature or condition is applicable.

2.10.6.1. MeasuredValue Attribute
This attribute SHALL represent the most recent measurement as a single-precision floating-point
number. MeasuredValue’s unit is represented by MeasurementUnit.
A value of null indicates that the measurement is unknown or outside the valid range.
MinMeasuredValue and MaxMeasuredValue define the valid range for MeasuredValue.
2.10.6.2. MinMeasuredValue Attribute
This attribute SHALL represent the minimum value of MeasuredValue that is capable of being mea
sured. A MinMeasuredValue of null indicates that the MinMeasuredValue is not defined.
2.10.6.3. MaxMeasuredValue Attribute
This attribute SHALL represent the maximum value of MeasuredValue that is capable of being mea
sured. A MaxMeasuredValue of null indicates that the MaxMeasuredValue is not defined.
2.10.6.4. PeakMeasuredValue Attribute
This attribute SHALL represent the maximum value of MeasuredValue that has been measured
during the PeakMeasuredValueWindow. If this attribute is provided, the PeakMeasuredValueWin
dow attribute SHALL also be provided.
2.10.6.5. PeakMeasuredValueWindow Attribute
This attribute SHALL represent the window of time used for determining the PeakMeasuredValue.
The value is in seconds.
2.10.6.6. AverageMeasuredValue Attribute
This attribute SHALL represent the average value of MeasuredValue that has been measured dur
ing  the  AverageMeasuredValueWindow.  If  this  attribute  is  provided,  the  AverageMeasuredVal
ueWindow attribute SHALL also be provided.
2.10.6.7. AverageMeasuredValueWindow Attribute
This attribute SHALL represent the window of time used for determining the AverageMeasured
Value. The value is in seconds.
2.10.6.8. Uncertainty Attribute
This attribute SHALL represent the range of error or deviation that can be found in MeasuredValue
and PeakMeasuredValue. This is considered a +/- value and should be considered to be in Measure
mentUnit.
2.10.6.9. MeasurementUnit Attribute
This attribute SHALL represent the unit of MeasuredValue. See MeasurementUnitEnum.
2.10.6.10. MeasurementMedium Attribute
This attribute SHALL represent the medium in which MeasuredValue is being measured. See Mea
surementMediumEnum.
2.10.6.11. LevelValue Attribute
This attribute SHALL represent the level of the substance detected. See LevelValueEnum.