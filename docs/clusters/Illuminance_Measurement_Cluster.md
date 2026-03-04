
# 2.2 Illuminance Measurement Cluster

The Illuminance Measurement cluster provides an interface to illuminance measurement function
ality, including configuration and provision of notifications of illuminance measurements.

## Data Types
2.2.4.1. LightSensorTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Illuminance Measurement Cluster" within the "Data Types" section and describes a data type with the value '0', named 'Photodiode'. This entry indicates that the sensor type is a photodiode, which is used to measure illuminance. The conformance rule for this entry is 'M', meaning that the inclusion of this data type is mandatory. Therefore, any implementation of the Illuminance Measurement Cluster must include support for the photodiode sensor type, as it is a required element according to the Matter specification.

* The table row describes an entry within the Illuminance Measurement Cluster, specifically in the context of Data Types. The entry is for a data type with the value '1', named 'CMOS', which indicates a CMOS sensor type. The conformance rule for this entry is 'M', meaning that the inclusion of this data type is mandatory. This implies that any implementation of the Illuminance Measurement Cluster must include support for the CMOS sensor type, as it is a required element without any conditions or exceptions.

* The table row pertains to the Illuminance Measurement Cluster within the Data Types section and describes a data type named 'MS', which is reserved for manufacturer-specific light sensor types. The 'Value' range for this data type is from 64 to 254. The 'Conformance' field is marked as 'O', indicating that this element is Optional. This means that the inclusion of this data type is not required and does not depend on any other features or conditions. Manufacturers can choose to implement this data type if they have specific light sensor types that fall within this reserved range, but there is no obligation to do so according to the Matter specification.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Illuminance Measurement Cluster, specifically the "MeasuredValue" attribute. This attribute has an ID of '0x0000' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The value of this attribute is constrained to be between '0' and the range defined by 'MinMeasuredValue' to 'MaxMeasuredValue'. The 'Quality' field is marked as 'PX', indicating it has provisional quality with an expectation of becoming mandatory in the future. The default value for this attribute is '0', and it has read (R) and volatile (V) access permissions, meaning it can be read and may change without a write operation. The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device that supports the Illuminance Measurement Cluster.

* The table row describes an attribute within the Illuminance Measurement Cluster, specifically the "MinMeasuredValue" attribute. This attribute has an ID of '0x0001' and is of type 'uint16', meaning it is a 16-bit unsigned integer. It has a constraint that limits its values between 1 and 65533. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality considerations. The 'Access' field is 'R V', which means the attribute is readable and has a volatile nature, suggesting it can change frequently. The 'Conformance' field is marked as 'M', which signifies that the "MinMeasuredValue" attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Illuminance Measurement Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Illuminance Measurement Cluster, specifically the 'MaxMeasuredValue' attribute. This attribute has an ID of '0x0002' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The value of this attribute is constrained to be at least one unit greater than the 'MinMeasuredValue' attribute. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed from having certain qualities, though the specific qualities are not detailed here. The 'Access' field is marked as 'R V', meaning the attribute is readable and has a volatile nature, which implies it may change frequently or unpredictably. The 'Conformance' field is marked as 'M', which means that the 'MaxMeasuredValue' attribute is mandatory and must always be implemented in any device that supports the Illuminance Measurement Cluster.

* In the Illuminance Measurement Cluster, under the Attributes section, the table row describes an attribute with the ID '0x0003', named 'Tolerance'. This attribute is of type 'uint16' and has a constraint that its maximum value is 2048. It has an access level of 'R V', meaning it is readable and can be viewed. The conformance rule for this attribute is 'O', indicating that it is optional. This means that the 'Tolerance' attribute is not required to be implemented and does not have any dependencies or conditions that would make it mandatory.

* The table row describes an attribute within the Illuminance Measurement Cluster, specifically the "LightSensorType" attribute. This attribute has an ID of '0x0004' and is of the type 'LightSensorTypeEnum'. It is constrained to 'all', meaning it applies universally within its context. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'O', meaning that the inclusion of the "LightSensorType" attribute is optional and not required by any dependencies or conditions. This allows implementers the flexibility to include or exclude this attribute based on their specific needs or preferences without affecting compliance with the Matter specification.

2.2.5.1. MeasuredValue Attribute
This attribute SHALL indicate the illuminance in Lux (symbol lx) as follows:
• MeasuredValue = 10,000 x log (illuminance) + 1,
10
<= <=
where 1 lx   illuminance   3.576 Mlx, corresponding to a MeasuredValue in the range 1 to 0xFFFE.
The MeasuredValue attribute can take the following values:
• 0 indicates a value of illuminance that is too low to be measured,
<= <=
• MinMeasuredValue   MeasuredValue   MaxMeasuredValue under normal circumstances,
• null indicates that the illuminance measurement is invalid.
The MeasuredValue attribute is updated continuously as new measurements are made.
2.2.5.2. MinMeasuredValue Attribute
This attribute SHALL indicate the minimum value of MeasuredValue that can be measured. A value
of null indicates that this attribute is not defined. See Measured Value for more details.
2.2.5.3. MaxMeasuredValue Attribute
This attribute SHALL indicate the maximum value of MeasuredValue that can be measured. A value
of null indicates that this attribute is not defined. See Measured Value for more details.
2.2.5.4. Tolerance Attribute
See Measured Value.
2.2.5.5. LightSensorType Attribute
This attribute SHALL indicate the electronic type of the light sensor. This attribute SHALL be set to
one of the non-reserved values listed in LightSensorTypeEnum or null in case the sensor type is
unknown.