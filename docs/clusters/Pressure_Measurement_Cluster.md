
# 2.4 Pressure Measurement Cluster

This cluster provides an interface to pressure measurement functionality, including configuration
and provision of notifications of pressure measurements.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Pressure Measurement Cluster, specifically the 'MeasuredValue' attribute. This attribute has an ID of '0x0000' and is of type 'int16', meaning it is a 16-bit integer. The value of this attribute is constrained between 'MinMeasuredValue' and 'MaxMeasuredValue', ensuring it stays within a defined range. The 'Quality' field indicates 'XP', suggesting that the attribute has specific quality considerations, possibly related to precision or reliability. The 'Access' field 'R V' denotes that the attribute is readable and has a volatile nature, meaning it can change frequently. The 'Conformance' field is marked as 'M', which means that the 'MeasuredValue' attribute is mandatory and must always be implemented in any device or application using this cluster, according to the Matter specification.

* The table row describes an attribute within the Pressure Measurement Cluster, specifically the "MinMeasuredValue" attribute. This attribute has an ID of '0x0001' and is of type 'int16', with a constraint that its maximum value can be 32766. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed for quality-related purposes. The 'Access' is 'R V', meaning it is readable and has a volatile nature. The conformance rule 'M' signifies that the "MinMeasuredValue" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Pressure Measurement Cluster.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Pressure Measurement Cluster, specifically the "MaxMeasuredValue" attribute. This attribute is identified by the ID '0x0002' and is of type 'int16', meaning it is a 16-bit integer. The value of this attribute is constrained to be between one unit greater than the "MinMeasuredValue" and 32767. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed from having any quality-related features. The 'Access' field specifies 'R V', meaning the attribute is readable and has a volatile nature, which typically implies that its value can change frequently. The 'Conformance' field is marked as 'M', which stands for Mandatory, indicating that the "MaxMeasuredValue" attribute is always required to be implemented in any device supporting the Pressure Measurement Cluster.

* The table row describes an attribute within the Pressure Measurement Cluster, specifically the "Tolerance" attribute. This attribute has an ID of '0x0003' and is of type 'uint16', with a constraint that its maximum value can be 2048. The default value for this attribute is '0', and it has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'O', which means it is optional. This indicates that the implementation of the "Tolerance" attribute is not required and does not depend on any other features or conditions. Implementers can choose to include this attribute in their devices, but it is not mandatory according to the Matter specification.

* The table row describes an attribute named "ScaledValue" within the Pressure Measurement Cluster, identified by the ID '0x0010'. This attribute is of type 'int16' and is constrained to values between 'MinScaledValue' and 'MaxScaledValue'. It has a default value of '0' and can be accessed with read ('R') and view ('V') permissions. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'EXT', which is not a standard conformance tag according to the provided guide, suggesting that the conformance of this attribute is described elsewhere in the documentation or may be an external specification. This means that the specific conditions under which this attribute is required or optional are not directly expressed in the table and need to be referenced from additional documentation.

* The table row describes an attribute named "MinScaledValue" within the Pressure Measurement Cluster. This attribute has an ID of '0x0011' and is of type 'int16', with a constraint that its maximum value can be 32766. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed. The default value for this attribute is '0', and it has read and view access permissions ('R V'). The 'Conformance' field is marked as 'EXT', which is not a standard conformance tag or expression as per the provided guide. Therefore, it likely indicates a special or extended condition that is not covered by the basic conformance tags or expressions, and its specific meaning would be described elsewhere in the documentation. In summary, the "MinScaledValue" attribute is not allowed in the current specification, and its conformance condition requires further clarification from additional documentation.

* The table row describes an attribute named "MaxScaledValue" within the Pressure Measurement Cluster, identified by the ID '0x0012'. This attribute is of type 'int16' and must have a value constrained between one more than the 'MinScaledValue' and 32767. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in terms of quality. The default value for this attribute is '0', and it has read and volatile access permissions, denoted by 'R V'. The conformance rule for "MaxScaledValue" is 'EXT', which is not directly explained by the provided conformance interpretation guide. However, it suggests that the conformance is described elsewhere in the documentation, likely under a section detailing extended or external conditions for this attribute. This means that the specific requirements or conditions under which "MaxScaledValue" is applicable or required are complex and need to be referenced from additional documentation.

* The table row describes an attribute named "ScaledTolerance" within the Pressure Measurement Cluster. This attribute has an ID of '0x0013' and is of type 'uint16', with a constraint that its maximum value can be 2048. The default value for this attribute is '0', and it has read and view access ('R V'). The conformance rule '[EXT]' indicates that the "ScaledTolerance" attribute is optional if the condition 'EXT' is true, meaning it is only required if the 'EXT' feature is supported. If 'EXT' is not supported, the attribute is not required.

* The table row describes an attribute named "Scale" within the Pressure Measurement Cluster, identified by the ID '0x0014'. This attribute is of type 'int8', with a constraint of a minimum value of -127 and a default value of 0. It has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'EXT', which is not explicitly defined in the provided conformance interpretation guide. However, based on typical IoT specification practices, 'EXT' could imply that the attribute is intended for extended or external use, possibly outside the standard conformance rules. This suggests that the attribute might be used in specialized implementations or extensions beyond the core specification, but without further documentation, its precise conformance status remains unclear.

2.4.5.1. MeasuredValue Attribute
This attribute SHALL represent the pressure in kPa as follows:
MeasuredValue = 10 x Pressure [kPa]
The null value indicates that the value is not available.
2.4.5.2. MinMeasuredValue Attribute
This attribute SHALL indicate the minimum value of MeasuredValue that can be measured. See
Measured Value for more details.
The null value indicates that the value is not available.
2.4.5.3. MaxMeasuredValue Attribute
This attribute SHALL indicate the maximum value of MeasuredValue that can be measured. See
Measured Value for more details.
The null value indicates that the value is not available.
2.4.5.4. Tolerance Attribute
See Measured Value.
2.4.5.5. ScaledValue Attribute
This attribute SHALL represent the pressure in Pascals as follows:
Scale
ScaledValue = 10  x Pressure [Pa]
The null value indicates that the value is not available.
2.4.5.6. MinScaledValue Attribute
This attribute SHALL indicate the minimum value of ScaledValue that can be measured.
The null value indicates that the value is not available.
2.4.5.7. MaxScaledValue Attribute
This attribute SHALL indicate the maximum value of ScaledValue that can be measured.
The null value indicates that the value is not available.
2.4.5.8. ScaledTolerance Attribute
This attribute SHALL indicate the magnitude of the possible error that is associated with Scaled
Value. The true value is located in the range
(ScaledValue – ScaledTolerance) to (ScaledValue + ScaledTolerance).
2.4.5.9. Scale Attribute
This attribute SHALL indicate the base 10 exponent used to obtain ScaledValue (see ScaledValue).