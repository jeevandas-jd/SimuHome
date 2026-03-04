
# 8.2 Temperature Control Cluster

This cluster provides an interface to the setpoint temperature on devices such as washers, refriger
ators, and water heaters. The setpoint temperature is the temperature to which a device using this
cluster would attempt to control to. This cluster does not provide access to the actual or physical
temperature associated with any device using this cluster. Access to the physical temperature asso
ciated with a device using this cluster would be provided by other clusters as part of that devices
device type definition.
The values and constraints of the attributes communicated to clients SHOULD match the controls
on any physical interface on a device implementing this server. For example, the value of the Step
attribute SHOULD match the incremental value by which the temperature setpoint can be changed
on the physical device.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Temperature Control Cluster, specifically the "TemperatureSetpoint" attribute. This attribute is identified by the ID '0x0000' and is of the type 'temperature'. It is constrained to values between 'MinTemperature' and 'MaxTemperature'. The access level is 'R V', indicating it is readable and possibly volatile. The conformance rule 'TN' suggests that the attribute's inclusion is conditional based on the support of the feature 'TN'. If the feature 'TN' is supported, the attribute is mandatory; otherwise, its inclusion is not required. This means that the presence of the 'TemperatureSetpoint' attribute depends on whether the 'TN' feature is implemented in the device.

* The table row describes an attribute within the Temperature Control Cluster, specifically the "MinTemperature" attribute, which has an ID of '0x0001' and is of type 'temperature'. This attribute is constrained to be a maximum of one unit less than the "MaxTemperature" attribute, as indicated by the constraint 'max (MaxTemperature - 1)*'. The quality 'F' suggests a specific fidelity or precision requirement, while the access 'R V' indicates that this attribute is readable and possibly volatile. The conformance 'TN' implies that the attribute is mandatory if the feature 'TN' is supported. If 'TN' is not supported, the conformance rule does not specify an alternative, which typically means the attribute is not required in that case.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "MaxTemperature" within the Temperature Control Cluster. This attribute has an ID of '0x0002' and is of the 'temperature' type. The 'Constraint' is described elsewhere in the documentation, as indicated by 'desc'. The 'Quality' is marked as 'F', and the 'Access' is 'R V', meaning it is readable and volatile. The 'Conformance' field is marked as 'TN', which does not directly match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. Therefore, it likely refers to a specific condition or feature code that is defined elsewhere in the documentation. In this context, 'TN' would need to be interpreted based on additional documentation or context provided in the Matter specification.

* In the Temperature Control Cluster, under the Attributes section, the entry for the attribute 'Step' with ID '0x0003' is of type 'temperature' and is constrained by the maximum difference between 'MaxTemperature' and 'MinTemperature'. It has a quality designation of 'F', indicating a specific quality level, and its access is marked as 'R V', meaning it is readable and has volatile characteristics. The conformance rule 'STEP' suggests that the requirement for this attribute is determined by a condition or feature named 'STEP'. According to the Matter Conformance Interpretation Guide, this means the 'Step' attribute is mandatory if the 'STEP' feature is supported. If the 'STEP' feature is not supported, the conformance of this attribute is not specified in this entry and would need further context or documentation to determine its status.

* The table row describes an attribute named "SelectedTemperatureLevel" within the Temperature Control Cluster. This attribute has an ID of '0x0004' and is of type 'uint8', with a constraint that its maximum value is 31. It has read and view access, as indicated by 'R V'. The conformance rule 'TL' means that the attribute is mandatory if the feature 'TL' (Temperature Level) is supported. In this context, if a device supports the Temperature Level feature, it must include the 'SelectedTemperatureLevel' attribute. Otherwise, the conformance rule does not apply, and the attribute is not required.

* The table row describes an attribute named "SupportedTemperatureLevels" within the Temperature Control Cluster. This attribute has an ID of '0x0005' and is of the type 'list[string]', with a constraint allowing a maximum of 32 strings, each up to 16 characters long. The access level is 'R V', indicating that it is readable and has a volatile nature, meaning its value can change without a write operation. The conformance rule 'TL' specifies that this attribute is mandatory if the feature 'TL' (Temperature Levels) is supported. If the feature 'TL' is not supported, the attribute is not required. This ensures that devices supporting temperature level features must include this attribute to list the supported temperature levels.

NOTE * See temperature data type, in the data model, for encoding units.
8.2.5.1. TemperatureSetpoint Attribute
This attribute SHALL represent the desired Temperature Setpoint on the device.
8.2.5.2. MinTemperature Attribute
This  attribute  SHALL  represent  the  minimum  temperature  to  which  the  TemperatureSetpoint
attribute MAY be set.
8.2.5.3. MaxTemperature Attribute
This attribute SHALL represent the maximum temperature to which the TemperatureSetpoint
attribute MAY be set.
If the Step attribute is supported, this attribute SHALL be such that MaxTemperature = MinTemper
ature + Step * n, where n is an integer and n > 0. If the Step attribute is not supported, this attribute
>
SHALL be such that MaxTemperature   MinTemperature.
8.2.5.4. Step Attribute
This attribute SHALL represent the discrete value by which the TemperatureSetpoint attribute can
be changed via the SetTemperature command.
For example, if the value of MinTemperature is 25.00C (2500) and the Step value is 0.50C (50),
valid values of the TargetTemperature field of the SetTemperature command would be 25.50C
(2550), 26.00C (2600), 26.50C (2650), etc.
8.2.5.5. SelectedTemperatureLevel Attribute
This attribute SHALL represent the currently selected temperature level setting of the server. This
attribute SHALL be the positional index of the list item in the SupportedTemperatureLevels list that
represents the currently selected temperature level setting of the server.
8.2.5.6. SupportedTemperatureLevels Attribute
This attribute SHALL represent the list of supported temperature level settings that may be selected
via the TargetTemperatureLevel field in the SetTemperature command. Each string is readable text
that describes each temperature level setting in a way that can be easily understood by humans.
For example, a washing machine can have temperature levels like "Cold", "Warm", and "Hot". Each
string is specified by the manufacturer.
Each item in this list SHALL represent a unique temperature level. Each entry in this list SHALL
have a unique value. The entries in this list SHALL appear in order of increasing temperature level
with list item 0 being the setting with the lowest temperature level.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Temperature Control Cluster, specifically the "SetTemperature" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'), indicating that the server must acknowledge or act upon receiving this command. The access level is marked as 'O', meaning it is optional for the client to implement this command. However, the conformance rule for this command is 'M', which signifies that it is mandatory for the server to support this command within the Temperature Control Cluster. This means that any implementation of the server side of this cluster must include the capability to process the "SetTemperature" command.

8.2.6.1. SetTemperature Command
The SetTemperature command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* In the Temperature Control Cluster, under the Commands section, there is an entry for a command named "TargetTemperature" with an ID of '0' and a type of 'temperature'. The 'Constraint' for this command is marked as 'desc', indicating that the constraints or conditions for this command are detailed elsewhere in the documentation and are too complex to be summarized simply. The 'Conformance' field is labeled as 'TN', which does not match any of the standard conformance tags or expressions outlined in the Matter Conformance Interpretation Guide. This suggests that 'TN' might be a typographical error or a placeholder, and further clarification from the documentation or specification would be necessary to accurately interpret its conformance requirements.

* The table row describes a command within the Temperature Control Cluster, specifically the "TargetTemperatureLevel" command, which is of type `uint8`. The constraint for this command is described elsewhere in the documentation, as indicated by "desc." The conformance rule for this command is "TL," meaning it is mandatory if the feature "TL" (presumably a feature related to temperature level control) is supported. If the feature "TL" is not supported, the command is not required. This indicates that the inclusion of the "TargetTemperatureLevel" command is contingent upon the presence of the "TL" feature within the device or system implementing the Temperature Control Cluster.

8.2.6.1.1. TargetTemperature Field
This field SHALL specify the desired temperature setpoint that the server is to be set to.
The TargetTemperature SHALL be from MinTemperature to MaxTemperature inclusive. If the Step
attribute is supported, TargetTemperature SHALL be such that (TargetTemperature - MinTempera
ture) % Step == 0.
8.2.6.1.2. TargetTemperatureLevel Field
This field SHALL specify the index of the list item in the SupportedTemperatureLevels list that rep
resents the desired temperature level setting of the server. The value of this field SHALL be
between 0 and the length of the SupportedTemperatureLevels list -1.
8.2.6.1.3. Effect on Receipt
If the TargetTemperature or TargetTemperatureLevel fields of the command meet all constraints
but the server is unable to execute the command at the time the command is received by the server
(e.g. due to the design of a device it cannot accept a change in its temperature setting after it has
begun operation), then the server SHALL respond with a status code of INVALID_IN_STATE, and dis
card the command.
If the TN feature is supported, on receipt of this command,
• If the value of the TargetTemperature field meets all constraints, the server SHALL set the Tem
peratureSetpoint attribute to the value of the TargetTemperature field and the response SHALL
have a status code of SUCCESS.
• Otherwise (e.g. if the value of the TargetTemperature field falls outside of the constraints of the
TemperatureSetpoint attribute or if the Step attribute is supported in the server and the value
of the TargetTemperature field is such that (TargetTemperature - MinTemperature) % Step != 0),
the status of the response SHALL be CONSTRAINT_ERROR and the value of the TemperatureSet
point attribute SHALL remain unchanged.
If the TL feature is supported, on receipt of this command,
• If value of the TargetTemperatureLevel field meets all constraints, the server SHALL set its
SelectedTemperatureLevel attribute to the value of TargetTemperatureLevel field and respond
with status SUCCESS.
• Otherwise (e.g. if the value of the TargetTemperatureLevel field is out of bounds of the Support
edTemperatureLevels list), the status of the response SHALL be CONSTRAINT_ERROR, and the
value of SelectedTemperatureLevel SHALL remain unchanged.