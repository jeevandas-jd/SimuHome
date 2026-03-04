
# 1.14 Operational State Cluster

This cluster supports remotely monitoring and, where supported, changing the operational state of
any device where a state machine is a part of the operation.
This cluster defines common states, scoped to this cluster (e.g. Stopped, Running, Paused, Error). A
derived cluster specification may define more states scoped to the derivation. Manufacturer spe
cific states are supported in this cluster and any derived clusters thereof. When defined in a
derived instance, such states are scoped to the derivation.
Actual state transitions are dependent on both the implementation, and the requirements that may
additionally be imposed by a derived cluster.
An implementation that supports remotely starting its operation can make use of this cluster’s Start
command to do so. A device that supports remote pause or stop of its currently selected operation
can similarly make use of this cluster’s Pause and Stop commands to do so. The ability to remotely
pause or stop is independent of how the operation was started (for example, an operation started
by using a manual button press can be stopped by using a Stop command if the device supports
remotely stopping the operation).
Additionally, this cluster provides events for monitoring the operational state of the device.

## Data Types
1.14.4.1. OperationalStateEnum Type
This type defines the set of known operational state values, and is derived from enum8. The follow
ing table defines the applicable ranges for values that are defined within this type. All values that
are undefined SHALL be treated as reserved. As shown by the table, states that may be specific to a
certain Device Type or other modality SHALL be defined in a derived cluster of this cluster.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "GeneralStates" data type within the Operational State Cluster's Data Types section. This data type encompasses values ranging from 0x00 to 0x3F and is used to represent generally applicable states as defined in the specification. The conformance rule for "GeneralStates" is not explicitly provided in the given data, but based on the context, it is likely that this data type is a fundamental component of the Operational State Cluster. Therefore, it is reasonable to infer that "GeneralStates" is a mandatory element, meaning it must always be implemented within this cluster to ensure consistent representation of general states across devices.

* The table row entry pertains to the "Operational State Cluster" within the "Data Types" section, specifically focusing on the data type named "DerivedClusterStates," which encompasses values ranging from '0x40 to 0x7F'. This data type represents states that are defined by the cluster itself. The conformance rule for this entry is not explicitly provided in the data, but if it were, it would dictate the conditions under which the "DerivedClusterStates" data type is required, optional, or otherwise specified according to the Matter Conformance Interpretation Guide. Without a specific conformance string, we cannot determine its mandatory or optional status, but typically, such entries would be evaluated based on the presence of certain features or conditions in the device's implementation.

* The table row entry describes a data type within the Operational State Cluster, specifically focusing on 'ManufacturerStates', which are vendor-specific states represented by the value range '0x80 to 0xBF'. This entry indicates that these states are defined by manufacturers to represent specific conditions or statuses unique to their devices. The conformance rule for 'ManufacturerStates' is not explicitly provided in the given data, but based on the context of the Matter specification, such vendor-specific states are typically optional, allowing manufacturers the flexibility to define and implement them as needed without being mandatory for all devices. This optionality ensures that while the standard provides a framework, manufacturers can extend functionality to suit their unique product requirements.

The derived cluster-specific state definitions SHALL NOT duplicate any general state definitions.
That is, a derived cluster specification of this cluster cannot define states with the same semantics
as the general states defined below.
A manufacturer-specific state definition SHALL NOT duplicate the general state definitions or
derived cluster state definitions. That is, a manufacturer-defined state defined for this cluster or a
derived cluster thereof cannot define a state with the same semantics as the general states defined
below or states defined in a derived cluster. Such manufacturer-specific state definitions SHALL be
scoped in the context of the Vendor ID present in the Basic Information cluster.
The following table defines the generally applicable states.

_Table parsed from section 'Data Types':_

* In the context of the Operational State Cluster, specifically within the Data Types section, the table row describes a data type with the value '0x00' and the name 'Stopped', which indicates that the device is in a stopped state. The conformance rule for this entry is 'M', meaning that the 'Stopped' state is a mandatory element. This implies that any implementation of the Operational State Cluster must include support for this 'Stopped' state, as it is always required according to the Matter specification.

* In the context of the Operational State Cluster, specifically within the Data Types section, the table row describes a data type with the value '0x01' named 'Running'. This data type indicates that the device is currently operating, as summarized by "The device is operating." The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Running' data type is a required element in the specification and must always be implemented in any device or system that supports the Operational State Cluster. There are no conditions or exceptions to this requirement; it is an essential part of the cluster's functionality.

* In the context of the Operational State Cluster, specifically within the Data Types section, the table entry describes a data type with the value '0x02' and the name 'Paused'. This entry indicates that the device is in a paused state during an operation. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Paused' state is a required element in the specification and must be implemented in all devices that support the Operational State Cluster. There are no conditions or dependencies affecting this requirement, making it an essential part of the cluster's functionality.

* In the context of the Operational State Cluster, specifically within the Data Types section, the table entry for 'Value' 0x03, named 'Error', indicates that this data type represents a state where the device is experiencing an error. The 'Summary' clarifies that this state signifies the device is in an error condition. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'Error' state is a required element within the Operational State Cluster and must always be implemented according to the Matter specification. There are no conditions or dependencies affecting this requirement; it is an essential part of the cluster's functionality.

1.14.4.2. OperationalStateStruct Type
The OperationalStateStruct is used to indicate a possible state of the device.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Operational State Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'OperationalStateID'. It is of the type 'OperationalStateEnum' and has a constraint labeled as 'all', meaning it applies universally without specific limitations. The default value for this entry is '0'. The conformance rule for 'OperationalStateID' is marked as 'M', which stands for Mandatory. This indicates that the 'OperationalStateID' element is always required to be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

* The table row describes an element within the Operational State Cluster, specifically a data type called 'OperationalStateLabel'. This element is a string with a maximum length constraint of 64 characters. The 'Conformance' field for this element is marked as 'desc', indicating that the conformance requirements for 'OperationalStateLabel' are too complex to be expressed with a simple tag or logical condition. Instead, the specific rules and conditions under which this element is required or optional are detailed elsewhere in the documentation. This means that to fully understand when and how 'OperationalStateLabel' should be implemented, one must refer to the additional descriptive information provided in the relevant section of the Matter specification.

1.14.4.2.1. OperationalStateID Field
This SHALL be populated with a value from the OperationalStateEnum.
1.14.4.2.2. OperationalStateLabel Field
This field SHALL be present if the OperationalStateID is from the set reserved for Manufacturer
Specific States, otherwise it SHALL NOT be present. If present, this SHALL contain a human-read
able description of the operational state.
1.14.4.3. ErrorStateEnum Type
This type defines the set of known operational error values, and is derived from enum8. The follow
ing table defines the applicable ranges for values that are defined within this type. All values that
are undefined SHALL be treated as reserved. As shown by the table, errors that may be specific to a
certain Device Type or other modality SHALL be defined in a derived cluster of this cluster.

_Table parsed from section 'Data Types':_

* The table row entry describes a data type within the Operational State Cluster, specifically focusing on the 'GeneralErrors' category. This data type encompasses values ranging from '0x00 to 0x3F' and is intended to represent generally applicable error values as defined in the specification. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage of such error codes, it is likely that these values are mandatory for devices implementing the Operational State Cluster to ensure consistent error reporting across different implementations. This means that any device supporting this cluster should recognize and handle these error values as part of its standard operation.

* The table row entry pertains to the "DerivedClusterErrors" within the Operational State Cluster's Data Types section. This entry is associated with the value range '0x40 to 0x7F' and represents errors that are specifically defined by the cluster itself. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves a condition where these derived errors are either mandatory or optional depending on the presence or absence of certain features or conditions within the cluster. Without a specific conformance string, it is implied that further documentation should be consulted to understand the precise conditions under which these errors are required or optional.

* The table row entry describes a data type within the Operational State Cluster, specifically a range of values from `0x80` to `0xBF` named `ManufacturerError`. This data type is used to represent vendor-specific errors, allowing manufacturers to define their own error codes within this range. The conformance rule for `ManufacturerError` is not explicitly provided in the given data, but based on the context, it likely follows a standard conformance pattern such as Optional (`O`) or Described (`desc`), indicating that its usage is either not mandatory and has no dependencies, or its conformance is detailed elsewhere in the documentation. This flexibility allows manufacturers to implement custom error codes while adhering to the Matter specification.

The derived cluster-specific error definitions SHALL NOT duplicate the general error definitions.
That is, a derived cluster specification of this cluster cannot define errors with the same semantics
as the general errors defined below.
The manufacturer-specific error definitions SHALL NOT duplicate the general error definitions or
derived cluster-specific error definitions. That is, a manufacturer-defined error defined for this
cluster or a derived cluster thereof cannot define errors with the same semantics as the general
errors defined below or errors defined in a derived cluster. Such manufacturer-specific error defin
itions SHALL be scoped in the context of the Vendor ID present in the Basic Information cluster.
The set of ErrorStateID field values defined in each of the generic or derived Operational State clus
ter specifications is called ErrorState.
1.14.4.3.1. ErrorStateEnum GeneralErrors Range
The following table defines the generally applicable ErrorState values.

_Table parsed from section 'Data Types':_

* In the Operational State Cluster, under the Data Types section, the entry for 'Value' 0x00 is named 'NoError' and is summarized as indicating that the device is not in an error state. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'NoError' state is a required element in the specification and must always be implemented in any device or application that adheres to this cluster's guidelines. There are no conditions or exceptions to this requirement, making it an essential part of the operational state functionality.

* In the context of the Operational State Cluster's Data Types, the entry for 'UnableToStartOrResume' with a value of '0x01' indicates a specific operational state where the device is unable to start or resume its operation. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'UnableToStartOrResume' state is a required element within the specification and must be implemented in all devices that support this cluster. There are no conditions or dependencies affecting this requirement, making it an essential part of the device's operational state reporting capabilities.

* The table row entry pertains to the "Operational State Cluster" within the "Data Types" section, specifically describing a data type with the name "UnableToCompleteOperation" and a value of '0x02'. This data type indicates that a device was unable to complete its current operation. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "UnableToCompleteOperation" data type is always required to be implemented in any device or system that supports the Operational State Cluster, without any conditions or exceptions.

* In the context of the Operational State Cluster, specifically within the Data Types section, the entry for 'CommandInvalidInState' with a value of '0x03' indicates a specific condition where a device cannot process a command due to its current state. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'CommandInvalidInState' data type is always required to be implemented in any device that supports the Operational State Cluster, without any conditions or exceptions. This ensures that all devices can consistently report when a command cannot be processed due to the device's operational state.

1.14.4.4. ErrorStateStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Operational State Cluster, specifically under the Data Types section. The entry is identified by the ID '0' and is named 'ErrorStateID'. It is of the type 'ErrorStateEnum', with a constraint labeled as 'all', and has a default value of '0'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'ErrorStateID' element is always required to be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

* The table row describes an element within the Operational State Cluster, specifically under the Data Types section. The element is identified by the ID '1' and is named 'ErrorStateLabel'. It is of the type 'string' with a constraint that limits its maximum length to 64 characters. The default value for this element is an empty string. The conformance for 'ErrorStateLabel' is marked as 'desc', indicating that the rules governing when this element is required or optional are too complex to be expressed with simple tags or expressions. Instead, the specific conditions and requirements for its implementation are detailed elsewhere in the documentation.

* The table row describes an entry within the Operational State Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'ErrorStateDetails'. It is of the type 'string' with a constraint that limits its maximum length to 64 characters. The default value for this entry is an empty string. The conformance rule for 'ErrorStateDetails' is marked as 'O', which means that this element is optional. It is not required to be implemented and does not have any dependencies or conditions that affect its optional status.

1.14.4.4.1. ErrorStateID Field
This SHALL be populated with a value from the ErrorStateEnum.
1.14.4.4.2. ErrorStateLabel Field
This field SHALL be present if the ErrorStateID is from the set reserved for Manufacturer Specific
Errors, otherwise it SHALL NOT be present. If present, this SHALL contain a human-readable
description  of  the  ErrorStateID;  e.g.  for  a  manufacturer  specific  ErrorStateID  of  "0x80"  the
ErrorStateLabel MAY contain "My special error".
1.14.4.4.3. ErrorStateDetails Field
This SHALL be a human-readable string that provides details about the error condition. As an
example,  if  the  ErrorStateID  indicates  that  the  device  is  a  Robotic  Vacuum  that  is  stuck,  the
ErrorStateDetails contains "left wheel blocked".

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "PhaseList" within the Operational State Cluster. This attribute has an ID of '0x0000' and is of the type 'list[string]', with a constraint allowing a maximum of 32 strings, each up to 64 characters long. The quality of this attribute is marked as 'X', indicating it is explicitly disallowed. The default value is 'MS', and it has read and view access permissions ('R V'). The conformance rule for "PhaseList" is 'M', meaning this attribute is mandatory and must always be included in implementations of the Operational State Cluster.

* The table row describes an attribute named "CurrentPhase" within the Operational State Cluster. This attribute has an ID of '0x0001' and is of type 'uint8'. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. The quality of this attribute is marked as 'X', meaning it is explicitly disallowed in certain contexts. The default value is 'MS', and it has read and view access permissions, denoted by 'R V'. The conformance rule for "CurrentPhase" is 'M', which means that this attribute is mandatory and must always be implemented in any device or application that supports the Operational State Cluster.

* The table row describes an attribute named "CountdownTime" within the Operational State Cluster. This attribute has an ID of '0x0002' and is of type 'elapsed-s', with a constraint that its maximum value can be 259200. The quality of this attribute is marked as 'X Q', indicating it is disallowed and has some quality considerations. Its default value is 'null', and it has read and view access permissions ('R V'). The conformance rule for this attribute is 'O', meaning that the "CountdownTime" attribute is optional. It is not required to be implemented and has no dependencies on other features or conditions.

* The table row describes an attribute named "OperationalStateList" within the Operational State Cluster. This attribute has an ID of '0x0003' and is of type 'list[OperationalStateStruct]', indicating it is a list composed of structures that define operational states. The 'Constraint' is marked as 'desc', suggesting that the constraints are detailed elsewhere in the documentation. The default value is 'MS', and the access level is 'R V', meaning it is readable and possibly volatile. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the "OperationalStateList" attribute is always required to be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Operational State Cluster, specifically the 'OperationalState' attribute. It is identified by the ID '0x0004' and is of the type 'OperationalStateEnum'. The 'Constraint' field indicates that this attribute applies universally ('all'), and the 'Access' field specifies that it is readable and viewable ('R V'). The 'Conformance' field is marked as 'M', which means that the 'OperationalState' attribute is mandatory. This implies that it is always required to be implemented in any device or application using the Operational State Cluster, without any conditions or exceptions.

* The table row describes an attribute named "OperationalError" within the Operational State Cluster, identified by the ID '0x0005'. This attribute is of the type 'ErrorStateStruct' and has constraints that are described elsewhere in the documentation, as indicated by 'desc'. The access permissions for this attribute are 'R V', meaning it is readable and viewable. The conformance rule for "OperationalError" is marked as 'M', which signifies that this attribute is mandatory. This means that the "OperationalError" attribute must always be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

1.14.5.1. PhaseList Attribute
This attribute SHALL indicate a list of names of different phases that the device can go through for
the selected function or mode. The list may not be in sequence order. For example in a washing
machine this could include items such as "pre-soak", "rinse", and "spin". These phases are manufac
turer specific and may change when a different function or mode is selected.
A null value indicates that the device does not present phases during its operation. When this
attribute’s value is null, the CurrentPhase attribute SHALL also be set to null.
1.14.5.2. CurrentPhase Attribute
This attribute represents the current phase of operation being performed by the server. This SHALL
be the positional index representing the value from the set provided in the PhaseList Attribute,
where the first item in that list is an index of 0. Thus, this attribute SHALL have a maximum value
that is "length(PhaseList) - 1".
This attribute SHALL be null if the PhaseList attribute is null or if the PhaseList attribute is an
empty list.
1.14.5.3. CountdownTime Attribute
This attribute SHALL represent the estimated time left before the operation is completed, in sec
onds.
A value of 0 (zero) means that the operation has completed.
A value of null represents that there is no time currently defined until operation completion. This
MAY happen, for example, because no operation is in progress or because the completion time is
unknown.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• If it has changed due to a change in the CurrentPhase or OperationalState attributes, or
• When it changes from 0 to any other value and vice versa, or
• When it changes from null to any other value and vice versa, or
• When it increases, or
• When there is any increase or decrease in the estimated time remaining that was due to pro
gressing insight of the server’s control logic, or
• When it changes at a rate significantly different from one unit per second.
Changes to this attribute merely due to the normal passage of time with no other dynamic change
of device state SHALL NOT be reported.
As this attribute is not being reported during a regular countdown, clients SHOULD NOT rely on the
reporting of this attribute in order to keep track of the remaining duration.
1.14.5.4. OperationalStateList Attribute
This attribute describes the set of possible operational states that the device exposes. An opera
tional state is a fundamental device state such as Running or Error. Details of the phase of a device
when, for example, in a state of Running are provided by the CurrentPhase attribute.
All devices SHALL, at a minimum, expose the set of states matching the commands that are also
supported by the cluster instance, in addition to Error. The set of possible device states are defined
in the OperationalStateEnum. A device type requiring implementation of this cluster SHALL define
the set of states that are applicable to that specific device type.
1.14.5.5. OperationalState Attribute
This attribute specifies the current operational state of a device. This SHALL be populated with a
valid OperationalStateID from the set of values in the OperationalStateList Attribute.
1.14.5.6. OperationalError Attribute
This attribute SHALL specify the details of any current error condition being experienced on the
device when the OperationalState attribute is populated with Error. Please see ErrorStateStruct for
general requirements on the population of this attribute.
When there is no error detected, this SHALL have an ErrorStateID of NoError.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Operational State Cluster, specifically the "Pause" command, which is directed from the client to the server and expects an "OperationalCommandResponse" in return. The access level for this command is optional, indicated by 'O'. The conformance rule "Resume, O" specifies that the "Pause" command is mandatory if the "Resume" feature is supported. If the "Resume" feature is not supported, the "Pause" command is optional. This means that the implementation of the "Pause" command depends on the presence of the "Resume" feature, ensuring that if a device can resume operations, it must also be able to pause them.

* The table row describes a command within the Operational State Cluster, specifically the "Stop" command, which is directed from the client to the server and expects an "OperationalCommandResponse" in return. The access level for this command is optional, indicated by 'O'. The conformance rule "Start, O" means that the "Stop" command is mandatory if the "Start" feature is supported; otherwise, it is optional. This implies that the presence of the "Start" feature directly influences the requirement status of the "Stop" command, making it a necessary part of the implementation when "Start" is available, but not required if "Start" is absent.

* The table row describes a command within the Operational State Cluster, specifically the "Start" command, which is identified by the ID '0x02'. This command is directed from the client to the server and expects a response in the form of an "OperationalCommandResponse". The access level for this command is marked as 'O', indicating that it is optional. The conformance rule for this command is also 'O', meaning that the inclusion of this command in a device's implementation is not required and has no dependencies. In essence, the "Start" command is an optional feature that manufacturers can choose to implement based on their specific device requirements or use cases.

* The table row describes a command within the Operational State Cluster, specifically the "Resume" command, which is directed from the client to the server and expects an "OperationalCommandResponse" in return. The access level for this command is optional ('O'), meaning it is not required for all implementations. The conformance rule 'Pause, O' indicates that the "Resume" command is mandatory if the "Pause" feature is supported; otherwise, it remains optional. This means that if a device supports the "Pause" functionality, it must also support the "Resume" command to ensure consistent operational control. If "Pause" is not supported, implementing the "Resume" command is optional.

* The table row describes a command named "OperationalCommandResponse" within the Operational State Cluster, which is directed from the server to the client. This command does not require a response and has optional access. The conformance rule "Pause | Stop | Start | Resume" indicates that the command is mandatory if any of the features "Pause," "Stop," "Start," or "Resume" are supported. In other words, if a device supports any of these operational states, it must also support the "OperationalCommandResponse" command. If none of these features are supported, the command is not required.

Note that it is entirely possible due to regulatory or other reasons for an instance of this cluster to
expose no possible commands. When that occurs, this cluster does not provide any ability to actu
ate the device, instead it provides readable (and by extension, can be subscribed to) information as
to the state of the device only. The commands that are supported SHALL be exposed by the device
in the AcceptedCommandList global attribute.
1.14.6.1. Pause Command
This command SHALL be supported if the device supports remotely pausing the operation. If this
command is supported, the Resume command SHALL also be supported.
On receipt of this command, the device SHALL pause its operation if it is possible based on the cur
rent function of the server. For example, if it is at a point where it is safe to do so and/or permitted,
but can be restarted from the point at which pause occurred.
If this command is received when already in the Paused state the device SHALL respond with an
OperationalCommandResponse command with an ErrorStateID of NoError but take no further
action.
A device that receives this command in any state which is not Pause-compatible SHALL respond
with an OperationalCommandResponse command with an ErrorStateID of CommandInvalidInState
and SHALL take no further action.
States are defined as Pause-compatible as follows:
• For states defined in this cluster specification, in Table 3, “Pause Compatibility”.
• For states defined by derived cluster specifications, in the corresponding specifications.
• For manufacturer-specific states, by the manufacturer.
A device that is unable to honor the Pause command for whatever reason SHALL respond with an
OperationalCommandResponse  command  with  an  ErrorStateID  of  CommandInvalidInState  but
take no further action.
Otherwise, on success:
• The OperationalState attribute SHALL be set to Paused.
• The  device  SHALL  respond  with  an  OperationalCommandResponse  command  with  an
ErrorStateID of NoError.
The following table defines the compatibility of this cluster’s states with the Pause command.
Table 3. Pause Compatibility

_Table parsed from section 'Commands':_

* The table row entry pertains to the "Operational State Cluster" within the "Commands" section, specifically describing a state with the value '0x00' and the name 'Stopped'. The 'Pause-Compatible' field is marked as 'N', indicating that this state is not compatible with a pause function. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage, it can be inferred that the 'Stopped' state is likely a fundamental state within the cluster, possibly implying a mandatory status. However, without a specific conformance string, we cannot definitively categorize it under the provided conformance rules. Thus, it is essential to refer to the broader documentation for any additional conditions or descriptions that might apply to this state.

* In the Operational State Cluster, under the Commands section, the table row describes a command with the 'State Value' of '0x01', which corresponds to the 'State Name' 'Running'. The 'Pause-Compatible' field is marked as 'Y', indicating that this state is compatible with a pause command. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage, it suggests that the 'Running' state is a standard operational state that is likely mandatory for devices implementing the Operational State Cluster. The 'Pause-Compatible' attribute being 'Y' implies that when a device is in the 'Running' state, it must support the ability to pause, aligning with the typical requirements for operational states in IoT devices.

* The table row describes a command within the Operational State Cluster, specifically the 'Paused' state, identified by the state value '0x02'. The 'Pause-Compatible' field is marked 'Y', indicating that this state is compatible with devices or features that support a pause functionality. The conformance rule for this entry is not explicitly provided in the row data, but based on the context and typical usage, if the 'Pause-Compatible' feature is supported, the 'Paused' state would likely be mandatory. If not, the state might be optional or not applicable. This ensures that devices capable of pausing operations can appropriately utilize this state, aligning with the Matter specification's goal of interoperability and flexibility.

* The table row entry pertains to the "Operational State Cluster" within the "Commands" section, specifically describing a state with the value '0x03' and the state name 'Error'. The 'Pause-Compatible' field is marked as 'N', indicating that this state is not compatible with any pause functionality. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically define whether the 'Error' state is mandatory, optional, or subject to other conditions within the implementation of the Operational State Cluster. Without a specific conformance string, we cannot apply the detailed rules from the guide, but generally, an 'Error' state is often a critical part of operational states, potentially making it mandatory or conditionally mandatory depending on the presence of certain features or conditions.

1.14.6.2. Stop Command
This command SHALL be supported if the device supports remotely stopping the operation.
On receipt of this command, the device SHALL stop its operation if it is at a position where it is safe
to do so and/or permitted. Restart of the device following the receipt of the Stop command SHALL
require attended operation unless remote start is allowed by the device type and any jurisdiction
governing remote operation of the device.
If this command is received when already in the Stopped state the device SHALL respond with an
OperationalCommandResponse command with an ErrorStateID of NoError but take no further
action.
A device that is unable to honor the Stop command for whatever reason SHALL respond with an
OperationalCommandResponse  command  with  an  ErrorStateID  of  CommandInvalidInState  but
take no further action.
Otherwise, on success:
• The OperationalState attribute SHALL be set to Stopped.
• The  device  SHALL  respond  with  an  OperationalCommandResponse  command  with  an
ErrorStateID of NoError.
1.14.6.3. Start Command
This command SHALL be supported if the device supports remotely starting the operation. If this
command is supported, the 'Stop command SHALL also be supported.
On receipt of this command, the device SHALL start its operation if it is safe to do so and the device
is in an operational state from which it can be started. There may be either regulatory or manufac
turer-imposed safety and security requirements that first necessitate some specific action at the
device before a Start command can be honored. In such instances, a device SHALL respond with a
status code of CommandInvalidInState if a Start command is received prior to the required on-
device action.
If this command is received when already in the Running state the device SHALL respond with an
OperationalCommandResponse command with an ErrorStateID of NoError but take no further
action.
A device that is unable to honor the Start command for whatever reason SHALL respond with an
OperationalCommandResponse  command  with  an  ErrorStateID  of  UnableToStartOrResume  but
take no further action.
Otherwise, on success:
• The OperationalState attribute SHALL be set to Running.
• The  device  SHALL  respond  with  an  OperationalCommandResponse  command  with  an
ErrorStateID of NoError.
1.14.6.4. Resume Command
This command SHALL be supported if the device supports remotely resuming the operation. If this
command is supported, the Pause command SHALL also be supported.
On receipt of this command, the device SHALL resume its operation from the point it was at when
it received the Pause command, or from the point when it was paused by means outside of this clus
ter (for example by manual button press).
If this command is received when already in the Running state the device SHALL respond with an
OperationalCommandResponse command with an ErrorStateID of NoError but take no further
action.
A device that receives this command in any state which is not Resume-compatible SHALL respond
with an OperationalCommandResponse command with an ErrorStateID of CommandInvalidInState
and SHALL take no further action.
States are defined as Resume-compatible as follows:
• For states defined in this cluster specification, in Table 4, “Resume Compatibility”.
• For states defined by derived cluster specifications, in the corresponding specifications.
• For manufacturer-specific states, by the manufacturer.
The following table defines the compatibility of this cluster’s states with the Resume command.
Table 4. Resume Compatibility

_Table parsed from section 'Commands':_

* The table row describes a command within the Operational State Cluster, specifically for the state value '0x00', which corresponds to the state name 'Stopped'. The 'Resume-Compatible' field is marked as 'N', indicating that this state is not compatible with resuming operations. The conformance rule for this entry is not explicitly provided in the row data, but based on the context of the Matter Conformance Interpretation Guide, if we were to interpret a conformance string, it would define when this 'Stopped' state command is required, optional, or otherwise. Since no specific conformance string is given, we can infer that the 'Stopped' state is a fundamental part of the Operational State Cluster, likely implying a mandatory status unless otherwise specified in the broader documentation.

* The table row describes a command within the Operational State Cluster, specifically related to the 'State Value' of '0x01', which corresponds to the 'State Name' of 'Running'. The 'Resume-Compatible' field is marked as 'Y', indicating that this state is compatible with resuming operations. However, the conformance rule for this entry is not explicitly provided in the data given. Assuming the conformance rule was included, it would dictate the conditions under which this command is required, optional, or otherwise, based on the presence or absence of certain features or conditions. In this context, the conformance rule would clarify whether the 'Running' state command is mandatory, optional, provisional, deprecated, or disallowed, and under what specific conditions these apply, using logical expressions and conditions as outlined in the Matter Conformance Interpretation Guide.

* In the context of the Operational State Cluster, specifically within the Commands section, the table row describes a command with the 'State Value' of '0x02', which corresponds to the 'State Name' 'Paused'. The 'Resume-Compatible' field is marked as 'Y', indicating that this state is compatible with a resume function. The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it suggests that the 'Paused' state is a recognized command within the cluster. If the conformance rule were included, it would specify under what conditions this command is mandatory, optional, provisional, deprecated, or disallowed, using the rules outlined in the Matter Conformance Interpretation Guide.

* In the context of the Operational State Cluster, specifically within the Commands section, the table row describes a command with a 'State Value' of '0x03' and a 'State Name' of 'Error'. The 'Resume-Compatible' field is marked as 'N', indicating that this command is not compatible with resume operations. The conformance rule for this entry is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, if there were a conformance string, it would dictate the conditions under which this command is required, optional, or otherwise. Since the conformance string is missing, we cannot determine its exact requirement status, but typically, such entries would be mandatory or optional based on the presence of specific features or conditions.

A device that is unable to honor the Resume command for any other reason SHALL respond with
an OperationalCommandResponse command with an ErrorStateID of UnableToStartOrResume but
take no further action.
Otherwise, on success:
• The OperationalState attribute SHALL be set to the most recent non-Error operational state
prior to entering the Paused state.
• The  device  SHALL  respond  with  an  OperationalCommandResponse  command  with  an
ErrorStateID of NoError.
1.14.6.5. OperationalCommandResponse Command
This command SHALL be supported by an implementation if any of the other commands defined by
this cluster are supported (i.e. listed in the AcceptedCommandList global attribute). This command
SHALL also be supported by an implementation of a derived cluster as a response to any com
mands that MAY be additionally defined therein.
This command SHALL be generated in response to any of the Start, Stop, Pause, or Resume com
mands. The data for this command SHALL be as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Operational State Cluster, specifically the 'CommandResponseState' command, which is identified by the ID '0x00' and is of the type 'ErrorStateStruct'. The 'Constraint' for this command is 'all', indicating that it applies universally across all relevant contexts or devices. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'CommandResponseState' command is always required to be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

1.14.6.5.1. CommandResponseState Field
This SHALL indicate the success or otherwise of the attempted command invocation. On a success
ful invocation of the attempted command, the ErrorStateID SHALL be populated with NoError.
Please see the individual command sections for additional specific requirements on population.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Operational State Cluster, specifically the 'OperationalError' event. This event is identified by the ID '0x00' and is classified with a 'CRITICAL' priority, indicating its high importance in the system's operation. The 'Access' field marked as 'V' suggests that this event is visible or can be accessed in a certain manner, possibly for monitoring or logging purposes. The 'Conformance' field is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'OperationalError' event is always required to be implemented in any device or system that supports the Operational State Cluster. There are no conditions or dependencies that alter this requirement, making it a fundamental component of the cluster.

* The table row describes an event within the Operational State Cluster, specifically the "OperationCompletion" event, identified by the ID '0x01'. This event has a priority level of 'INFO' and requires 'V' access, which typically indicates that it is viewable or retrievable. The conformance rule for this event is 'O', meaning that the "OperationCompletion" event is optional. This indicates that the implementation of this event is not required and does not depend on any other features or conditions. Devices or systems implementing the Operational State Cluster can choose to include this event, but it is not mandatory for compliance with the Matter specification.

1.14.7.1. OperationalError Event
This event is generated when a reportable error condition is detected. A device that generates this
event SHALL also set the OperationalState attribute to Error, indicating an error condition.
This event SHALL contain the following fields:

_Table parsed from section 'Events':_

* The table row describes an event within the Operational State Cluster, specifically named "ErrorState," which is of the type "ErrorStateStruct" and applies to all constraints. The conformance rule for this entry is marked as "M," indicating that the "ErrorState" event is mandatory. This means that any implementation of the Operational State Cluster must include the "ErrorState" event without exception. The mandatory status ensures that this event is always present to report error states, providing consistent and reliable error handling across devices implementing this cluster.

1.14.7.2. OperationCompletion Event
This event SHOULD be generated when the overall operation ends, successfully or otherwise. For
example, the completion of a cleaning operation in a Robot Vacuum Cleaner, or the completion of a
wash cycle in a Washing Machine.
It is highly RECOMMENDED that appliances device types employing the Operational State cluster
support this event, even if it is optional. This assists clients in executing automations or issuing noti
fications at critical points in the device operation cycles.
This event SHALL contain the following fields:

_Table parsed from section 'Events':_

* The table row describes an element within the Operational State Cluster, specifically under the Events section. The element is identified by the ID '0' and is named 'CompletionErrorCode'. It is of the type 'enum8', indicating it is an 8-bit enumeration. The constraint 'all' suggests that this element applies universally within its context. The conformance rule 'M' signifies that the 'CompletionErrorCode' is a mandatory element. This means it is always required to be implemented in any device or application that supports the Operational State Cluster, without any conditions or exceptions.

* The table row describes an event within the Operational State Cluster, specifically identified as 'TotalOperationalTime' with an ID of '1'. This event is of type 'elapsed-s', indicating it measures elapsed time in seconds, and it applies universally as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is labeled as 'O', which means that the 'TotalOperationalTime' event is optional. This implies that while it can be implemented, there is no requirement or dependency mandating its inclusion in the system.

* The table row describes an event within the Operational State Cluster, specifically the "PausedTime" event, which is identified by ID '2' and is of the type 'elapsed-s', indicating it measures elapsed time in seconds. The 'Constraint' field is marked as 'all', suggesting that this event applies universally within its context. The 'Quality' is marked as 'X', meaning this event is explicitly disallowed in terms of quality considerations. The 'Conformance' field is marked as 'O', which means that the "PausedTime" event is optional. This indicates that while the event can be implemented, it is not required and does not depend on any specific conditions or features being supported.

1.14.7.2.1. CompletionErrorCode Field
This field provides an indication of the state at the end of the operation. This field SHALL have a
value from the ErrorStateEnum set. A value of NoError indicates success, that is, no error has been
detected.
1.14.7.2.2. TotalOperationalTime Field
The total operational time, in seconds, from when the operation was started via an initial Start com
mand or autonomous/manual starting action, until the operation completed. This includes any time
spent while paused. There may be cases whereby the total operational time exceeds the maximum
value that can be conveyed by this attribute, in such instances, this attribute SHALL be populated
with null.
1.14.7.2.3. PausedTime Field
The total time spent in the paused state, in seconds. There may be cases whereby the total paused
time exceeds the maximum value that can be conveyed by this attribute, in such instances, this
attribute SHALL be populated with null.