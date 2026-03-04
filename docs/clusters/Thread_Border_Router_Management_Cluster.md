
# 10.3 Thread Border Router Management Cluster

This cluster provides an interface for managing a Thread Border Router and the Thread network
that it belongs to. Privileged nodes within the same fabric as a Thread Border Router can use these
interfaces to request and set credentials information to the Thread network.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "BorderRouterName" within the Thread Border Router Management Cluster. This attribute has an ID of '0x0000' and is of type 'string', with a constraint that its length must be between 1 and 63 characters. The access level for this attribute is 'R V', indicating it can be read and is viewable. The conformance rule for "BorderRouterName" is 'M', which means this attribute is mandatory. It is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Thread Border Router Management Cluster, specifically the 'BorderAgentID'. This attribute has an ID of '0x0001' and is of type 'octstr' with a constraint of 16, indicating it is an octet string with a length of 16 bytes. The access permissions for this attribute are 'R V', meaning it can be read and is volatile. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the 'BorderAgentID' attribute is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Thread Border Router Management Cluster, specifically the "ThreadVersion" attribute. This attribute has an ID of '0x0002' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that it applies universally without specific limitations. The 'Quality' is marked as 'F', and the 'Default' value is 'MS', though these terms are not further defined in the provided context. The 'Access' is 'R V', suggesting that the attribute is readable and possibly has a volatile or variable nature. The 'Conformance' is marked as 'M', which, according to the Matter Conformance Interpretation Guide, means that this attribute is mandatory. It is always required to be implemented in any device that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

* The table row describes an attribute named "InterfaceEnabled" within the Thread Border Router Management Cluster, specifically under the Attributes section. This attribute has an ID of '0x0003' and is of the boolean type, meaning it can be either true or false. The constraint 'all' suggests it applies universally within its context, and its default value is set to 'false'. The access level 'R V' indicates that this attribute can be read and verified. The conformance rule 'M' signifies that the "InterfaceEnabled" attribute is mandatory, meaning it is always required to be implemented in any device or system that supports the Thread Border Router Management Cluster.

* The table row describes an attribute named "ActiveDatasetTimestamp" within the Thread Border Router Management Cluster. This attribute has an ID of '0x0004' and is of type 'uint64', meaning it is a 64-bit unsigned integer. The constraint 'all' indicates that this attribute applies universally within its context. The quality 'XN' suggests specific quality characteristics, though these are not detailed in the provided data. The default value for this attribute is '0', and it has read and view access ('R V'), meaning it can be read and viewed by authorized entities. The conformance rule 'M' signifies that the "ActiveDatasetTimestamp" attribute is mandatory, meaning it is always required to be implemented in any device or application supporting the Thread Border Router Management Cluster.

* The table row describes an attribute named "PendingDatasetTimestamp" within the Thread Border Router Management Cluster, identified by the ID '0x0005'. This attribute is of type 'uint64' and applies to all constraints. It has a quality designation of 'XN', a default value of '0', and access permissions of 'R V', indicating it can be read and viewed. The conformance rule 'M' signifies that the "PendingDatasetTimestamp" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster.

10.3.5.1. BorderRouterName Attribute
This attribute SHALL indicate a user-friendly name identifying the device model or product of the
Border Router in MeshCOP (DNS-SD service name) as defined in the Thread specification, and has
<VendorName> <ProductName>._meshcop._udp
the following recommended format:  . An example name
ACME Border Router (74be)._meshcop._udp
would be  .
10.3.5.2. BorderAgentID Attribute
This attribute SHALL indicate a 16-byte globally unique ID for a Thread Border Router device. This
ID is manufacturer-specific, and it is created and managed by the border router’s implementation.
10.3.5.3. ThreadVersion Attribute
This attribute SHALL indicate the Thread version supported by the Thread interface configured by
the cluster instance.
The format SHALL match the value mapping defined in the "Version TLV" section of the Thread
specification. For example, Thread 1.3.0 would have ThreadVersion set to 4.
10.3.5.4. InterfaceEnabled Attribute
This attribute SHALL indicate whether the associated IEEE 802.15.4 Thread interface is enabled or
disabled.
10.3.5.5. ActiveDatasetTimestamp Attribute
This attribute SHALL be null if the Thread Border Router has no dataset configured, otherwise it
SHALL be the timestamp value extracted from the Active Dataset value configured by the Thread
Node to which the border router is connected. This attribute SHALL be updated when a new Active
dataset is configured on the Thread network to which the border router is connected.
10.3.5.6. PendingDatasetTimestamp Attribute
This attribute SHALL be null if the Thread Border Router has no Pending dataset configured, other
wise it SHALL be the timestamp value extracted from the Pending Dataset value configured by the
Thread Node to which the border router is connected. This attribute SHALL be updated when a
new Pending dataset is configured on the Thread network to which the border router is connected.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "GetActiveDatasetRequest" command. This command is initiated by the client and directed to the server, expecting a "DatasetResponse" in return. The access level for this command is marked as "Mandatory" (M), indicating that it must always be implemented and supported in any device or application using this cluster. The conformance rule for this command is also "Mandatory" (M), reinforcing that its implementation is required without any conditions or exceptions. This means that any implementation of the Thread Border Router Management Cluster must include support for the "GetActiveDatasetRequest" command.

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "GetPendingDatasetRequest" command. This command is initiated by a client and directed towards a server, and it expects a "DatasetResponse" in return. The access level for this command is marked as "M," indicating that it is mandatory for the client to have access to execute this command. The conformance rule for this command is also "M," which means that the "GetPendingDatasetRequest" command is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "DatasetResponse" command. This command is identified by the ID '0x02' and is directed from the server to the client, as indicated by the direction 'client ⇐ server'. The 'Response' field marked as 'N' suggests that this command does not require an additional response. The 'Conformance' field is marked with 'M', which means that the "DatasetResponse" command is mandatory. This implies that any implementation of the Thread Border Router Management Cluster must include this command as a required element, ensuring its presence and functionality in all compliant devices or systems.

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "SetActiveDatasetRequest" command. This command is identified by the ID '0x03' and is directed from the client to the server, with a response expected ('Y'). The access level for this command is marked as 'M T', indicating that it is mandatory and requires a specific access privilege or role. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "SetActiveDatasetRequest" command must always be implemented in any device or application that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "SetPendingDatasetRequest" command, which is directed from the client to the server. The command requires a response, as indicated by the 'Response' field marked 'Y'. The 'Access' field 'M T' suggests that the command has mandatory access requirements, possibly related to specific roles or permissions. The 'Conformance' field is marked as 'PC', which according to the Matter Conformance Interpretation Guide, indicates that the command is currently provisional. This means that its status is temporary and it may become mandatory in the future. This provisional status suggests that while the command is not yet required, it is anticipated to be an essential part of the specification in upcoming versions.

10.3.6.1. GetActiveDatasetRequest Command
This command SHALL be used to request the active operational dataset of the Thread network to
which the border router is connected.
If the command is not executed via a CASE session, the command SHALL fail with a status code of
UNSUPPORTED_ACCESS.
If an internal error occurs, then this command SHALL fail with a FAILURE status code sent back to
the initiator.
Otherwise, this SHALL generate a DatasetResponse command.
10.3.6.2. GetPendingDatasetRequest Command
This command SHALL be used to request the pending dataset of the Thread network to which the
border router is connected.
If the command is not executed via a CASE session, the command SHALL fail with a status code of
UNSUPPORTED_ACCESS.
If an internal error occurs, then this command SHALL fail with a FAILURE status code sent back to
the initiator.
Otherwise, this SHALL generate a DatasetResponse command.
10.3.6.3. DatasetResponse Command
This command is sent in response to GetActiveDatasetRequest or GetPendingDatasetRequest com
mand. The data for this command SHALL be as follows:

_Table parsed from section 'Commands':_

* In the context of the Thread Border Router Management Cluster, the table row describes a command named "Dataset" with an ID of '0'. This command is of type 'octstr' (octet string) and is constrained to a maximum length of 254 bytes. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Dataset" command is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

10.3.6.3.1. Dataset field
If no dataset (active or pending as requested) is configured, this field SHALL be set to empty.
Otherwise, this field SHALL contain the active or pending dataset of the Thread network to which
the Border Router is connected as an octet string containing the raw Thread TLV value of the
dataset, as defined in the Thread specification.
10.3.6.4. SetActiveDatasetRequest Command
This command SHALL be used to set the active Dataset of the Thread network to which the Border
Router is connected, when there is no active dataset already.

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Border Router Management Cluster, specifically the "ActiveDataset" command. This command is identified by the ID '0' and is of the type 'octstr', with a constraint that limits its maximum size to 254 bytes. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "ActiveDataset" command is always required to be implemented in any device or application that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

* The table row describes a command named "Breadcrumb" within the Thread Border Router Management Cluster. This command has an ID of '1' and is of type 'uint64', with a constraint applicable to all instances. The conformance rule for this command is 'O', which means it is optional. This indicates that the "Breadcrumb" command is not required to be implemented in all devices or systems using this cluster, and there are no dependencies or conditions that affect its optional status. It can be included at the discretion of the implementer without any mandatory obligation.

10.3.6.4.1. ActiveDataset Field
This field SHALL contain the active dataset to set of the Thread network to configure in the Border
Router as an octet string containing the raw Thread TLV value of the dataset, as defined in the
Thread specification.
10.3.6.4.2. Breadcrumb Field
See Breadcrumb Attribute section of General Commissioning Cluster in [MatterCore] for usage.
10.3.6.4.3. Effect on receipt
If the command is not executed via a CASE session, the command SHALL fail with a status code of
UNSUPPORTED_ACCESS.
If this command is received without a Fail Safe Context (see ArmFailSafe Command of General Com
missioning Cluster in [MatterCore]), then this command SHALL fail with a FAILSAFE_REQUIRED
status code sent back to the initiator.
If any of the parameters in the ActiveDataset is invalid, the command SHALL fail with a status code
of INVALID_COMMAND.
If this command is invoked when the ActiveDatasetTimestamp attribute is not null, the command
SHALL fail with a status code of INVALID_IN_STATE. The administrator MAY use the SetPending
DatasetRequest command to modify the future active dataset.
If this command is invoked and the ActiveDatasetTimestamp attribute is null, the Thread Border
Router SHALL configure and activate its active dataset using the ActiveDataset parameter.
The activation process SHALL be a time-bound process that completes before expiration of a fail-
safe timer. The fail-safe timer SHALL be set at the beginning of the activation process.
If the fail-safe timer expires prior to activation process completion, the command SHALL respond
with TIMEOUT, and the Border Router state SHALL revert to the configuration set prior to the fail-
safe timer being armed, see ArmFailSafe Command of General Commissioning Cluster in [Matter
Core].
After successfully creating or joining a Thread network with the new active dataset, the Inter
faceEnabled attribute SHALL be updated to TRUE, indicating that the associated Thread Interface is
active and functioning. The ActiveDatasetTimestamp attribute SHALL be updated with the Active
Dataset timestamp. If the Adjacent Infrastructure Link of the Border Router is connected, then the
device SHOULD also enable and operate Thread Border Routing functionality using the Thread and
Adjacent Infrastructure Link interfaces.
If this command is received during the activation process triggered by a previous SetActiveDatase
tRequest command, then the command SHALL fail with a status code of BUSY.
10.3.6.5. SetPendingDatasetRequest Command
This command SHALL be used to set or update the pending Dataset of the Thread network to which
the Border Router is connected, if the Border Router supports PAN Change.
If the command is not executed via a CASE session, the command SHALL fail with a status code of
UNSUPPORTED_ACCESS.

_Table parsed from section 'Commands':_

* In the context of the Thread Border Router Management Cluster, the table entry describes a command named "PendingDataset" with an ID of '0'. This command is of type 'octstr' and has a constraint limiting its maximum size to 254 bytes. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "PendingDataset" command is always required to be implemented in any device or system that supports the Thread Border Router Management Cluster, without any conditions or exceptions.

This PendingDataset field SHALL contain the pending dataset to which the Thread network should
be updated. The format of the data SHALL be an octet string containing the raw Thread TLV value
of the pending dataset, as defined in the Thread specification.
If any of the parameters in the PendingDataset is invalid, the command SHALL fail with a status of
INVALID_COMMAND.
Otherwise, this command SHALL configure the pending dataset of the Thread network to which the
Border Router is connected, with the value given in the PendingDataset parameter. The Border
Router will manage activation of the pending dataset as defined in the Thread specification.