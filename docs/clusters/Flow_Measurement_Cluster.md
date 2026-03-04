
# 2.5 Flow Measurement Cluster

This cluster provides an interface to flow measurement functionality, including configuration and
provision of notifications of flow measurements.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Flow Measurement Cluster, specifically the 'MeasuredValue' attribute. This attribute has an ID of '0x0000' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The value of this attribute is constrained between 'MinMeasuredValue' and 'MaxMeasuredValue', ensuring it falls within a specified range. The 'Quality' field indicates 'XP', suggesting that this attribute is in a provisional state and may be disallowed in the future. The default value for 'MeasuredValue' is 'null', and it has read and view access ('R V'). The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device supporting the Flow Measurement Cluster.

* The table row describes an attribute within the Flow Measurement Cluster, specifically the "MinMeasuredValue" attribute. This attribute has an ID of '0x0001' and is of type 'uint16', with a constraint that its maximum value can be 65533. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality considerations. The 'Access' field is marked as 'R V', meaning it is readable and has a volatile nature. The 'Conformance' field is marked as 'M', which means that the "MinMeasuredValue" attribute is mandatory and must always be implemented in any device that supports the Flow Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Flow Measurement Cluster, specifically the "MaxMeasuredValue" attribute. This attribute has an ID of '0x0002' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The constraint for this attribute is that its value must be at least one unit greater than the 'MinMeasuredValue'. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in some contexts, although this does not affect its conformance. The 'Access' is 'R V', meaning it is readable and can have its value verified. The 'Conformance' is marked as 'M', which means that the 'MaxMeasuredValue' attribute is mandatory and must always be implemented in any device supporting the Flow Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute named "Tolerance" within the Flow Measurement Cluster, identified by the ID '0x0003'. This attribute is of type 'uint16', with a constraint that its maximum value can be 2048, and it has a default value of 0. The access level for this attribute is 'R V', indicating it is readable and has a volatile nature. The conformance rule for "Tolerance" is 'O', meaning this attribute is optional. It is not required for implementation and does not depend on any other features or conditions within the Matter specification.

2.5.4.1. MeasuredValue Attribute
3
This attribute SHALL indicate the flow in m /h as follows:
MeasuredValue = 10 x Flow
The null value indicates that the flow measurement is unknown, otherwise the range SHALL be as
described in Measured Value.
2.5.4.2. MinMeasuredValue Attribute
This attribute SHALL indicate the minimum value of MeasuredValue that can be measured. See
Measured Value for more details.
The null value indicates that the value is not available.
2.5.4.3. MaxMeasuredValue Attribute
This attribute SHALL indicate the maximum value of MeasuredValue that can be measured. See
Measured Value for more details.
The null value indicates that the value is not available.
2.5.4.4. Tolerance Attribute
See Measured Value.
2.6. Water Content Measurement Clusters
This is a base cluster. The server cluster provides an interface to water content measurement func
tionality. The measurement is reportable and may be configured for reporting. Water content mea
surements currently is, but are not limited to relative humidity.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Flow Measurement Cluster, specifically the 'MeasuredValue' attribute. This attribute has an ID of '0x0000' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The value of this attribute is constrained to lie between 'MinMeasuredValue' and 'MaxMeasuredValue'. The 'Quality' field indicates that this attribute is both experimental ('X') and provisional ('P'), suggesting it is still under evaluation and may change in future specifications. The 'Access' field specifies that the attribute is readable ('R') and can be reported via events ('V'). The 'Conformance' field is marked as 'M', indicating that the 'MeasuredValue' attribute is mandatory and must always be implemented in any device that supports the Flow Measurement Cluster.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Flow Measurement Cluster, specifically the "MinMeasuredValue" attribute. This attribute has an ID of '0x0001' and is of type 'uint16', with a constraint that its maximum value cannot exceed 9999. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality. The 'Access' permissions are 'R V', meaning it is readable and has volatile access characteristics. The 'Conformance' is marked as 'M', which means that the "MinMeasuredValue" attribute is mandatory and must always be implemented in any device or application that supports the Flow Measurement Cluster, without any conditions or exceptions.

* In the Flow Measurement Cluster, within the Attributes section, the table row describes the attribute 'MaxMeasuredValue' with an ID of '0x0002'. This attribute is of type 'uint16' and must have a value constrained between one unit greater than 'MinMeasuredValue' and 10,000. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality considerations. The 'Access' is defined as 'R V', meaning it is readable and volatile. The 'Conformance' is marked as 'M', which means that the 'MaxMeasuredValue' attribute is mandatory and must always be implemented in any device supporting the Flow Measurement Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Flow Measurement Cluster, specifically the "Tolerance" attribute. This attribute has an ID of '0x0003' and is of type 'uint16', with a constraint that its maximum value is 2048. The access level for this attribute is 'R V', indicating that it is readable and has a volatile nature, meaning its value can change frequently. The conformance rule for this attribute is 'O', which means it is optional. This implies that the implementation of the "Tolerance" attribute is not required and has no dependencies on other features or conditions within the Matter specification.

2.6.4.1. MeasuredValue Attribute
MeasuredValue represents the water content in % as follows:
MeasuredValue = 100 x water content
Where 0% < = water content < = 100%, corresponding to a MeasuredValue in the range 0 to 10000.
The maximum resolution this format allows is 0.01%.
MinMeasuredValue and MaxMeasuredValue define the range of the sensor.
The null value indicates that the measurement is unknown, otherwise the range SHALL be as
described in Measured Value.
MeasuredValue is updated continuously as new measurements are made.
2.6.4.2. MinMeasuredValue Attribute
The MinMeasuredValue attribute indicates the minimum value of MeasuredValue that can be mea
sured. The null value means this attribute is not defined. See Measured Value for more details.
2.6.4.3. MaxMeasuredValue Attribute
The MaxMeasuredValue attribute indicates the maximum value of MeasuredValue that can be mea
sured. The null value means this attribute is not defined. See Measured Value for more details.
2.6.4.4. Tolerance Attribute
See Measured Value.