
# 2.3 Temperature Measurement Cluster

This cluster provides an interface to temperature measurement functionality, including configura
tion and provision of notifications of temperature measurements.

## Attributes

_Table parsed from section 'Attributes':_

* In the Temperature Measurement Cluster, the attribute 'MeasuredValue' with ID '0x0000' is of type 'temperature' and is constrained to values between 'MinMeasuredValue' and 'MaxMeasuredValue'. It is marked with a quality of 'XP', indicating specific quality characteristics, and has access permissions 'R V', meaning it can be read and is volatile. The conformance rule for 'MeasuredValue' is 'M', which means this attribute is mandatory and must always be implemented in any device that supports the Temperature Measurement Cluster. This ensures that the 'MeasuredValue' attribute is consistently available across all compliant devices, providing a standard way to report temperature measurements.

* In the Temperature Measurement Cluster, the attribute 'MinMeasuredValue' is identified by the ID '0x0001' and is of the 'temperature' type, with a valid range constrained between -27315 and 32766. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed from having any quality-related features. The 'Access' field is 'R V', meaning it is readable and volatile. The 'Conformance' field is marked as 'M', which means that the 'MinMeasuredValue' attribute is mandatory and must always be implemented in any device that supports the Temperature Measurement Cluster, without any conditional requirements or exceptions.

* The table row describes an attribute within the Temperature Measurement Cluster, specifically the 'MaxMeasuredValue'. This attribute is identified by the ID '0x0002' and is of the 'temperature' type. It has a constraint that it must be at least one unit greater than the 'MinMeasuredValue'. The 'Quality' field is marked as 'X', indicating that this attribute is explicitly disallowed from having any quality-related features. The 'Access' field 'R V' suggests that the attribute is readable and has a volatile nature, meaning it can change frequently. The 'Conformance' field is marked as 'M', which means that the 'MaxMeasuredValue' attribute is mandatory and must always be implemented in any device or application that supports the Temperature Measurement Cluster.

* In the Temperature Measurement Cluster, the attribute with ID '0x0003' is named 'Tolerance'. It is of type 'uint16', constrained to a maximum value of 2048, and has a default value of 0. The access level for this attribute is 'R V', indicating it can be read and is volatile. The conformance rule for 'Tolerance' is 'O', meaning that this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions. This allows developers the flexibility to include or exclude this attribute based on their specific application needs without affecting compliance with the Matter specification.

2.3.4.1. MeasuredValue Attribute
This attribute SHALL indicate the measured temperature.
The null value indicates that the temperature is unknown.
2.3.4.2. MinMeasuredValue Attribute
This attribute SHALL indicate the minimum value of MeasuredValue that is capable of being mea
sured. See Measured Value for more details.
The null value indicates that the value is not available.
2.3.4.3. MaxMeasuredValue Attribute
This attribute indicates the maximum value of MeasuredValue that is capable of being measured.
See Measured Value for more details.
The null value indicates that the value is not available.
2.3.4.4. Tolerance Attribute
See Measured Value.