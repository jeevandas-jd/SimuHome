
# 6.11 Target Navigator Cluster

This cluster provides an interface for UX navigation within a set of targets on a device or endpoint.
This cluster would be supported on Video Player devices or devices with navigable user interfaces.
This cluster would also be supported on endpoints with navigable user interfaces such as a Content
App. It supports listing a set of navigation targets, tracking and changing the current target.
The cluster server for Target Navigator is implemented by endpoints on a device that support UX
navigation.
When this cluster is implemented for a Content App endpoint, the Video Player device containing
the endpoint SHALL launch the Content App when a client invokes the NavigateTarget command.

## Data Types
6.11.4.1. StatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Target Navigator Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '0' and the 'Name' of 'Success', which indicates that a command has succeeded. The 'Conformance' field for this entry is marked as 'M', meaning that this element is Mandatory. This implies that the 'Success' data type must always be implemented and supported in any device or application that conforms to the Matter specification for this cluster. There are no conditions or exceptions; it is a required element without any dependencies or provisional status.

* In the Target Navigator Cluster, under the Data Types section, the entry for 'TargetNotFound' with a value of '1' signifies a specific condition where the requested target is not found in the TargetList. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any system or device that supports the Target Navigator Cluster. This ensures that the system can consistently handle situations where a target is not found, providing a standardized response across all implementations.

* In the Target Navigator Cluster, under the Data Types section, the entry for 'NotAllowed' with a value of '2' signifies a state where a target request is not permitted due to the current conditions. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. This ensures that the system consistently recognizes and handles situations where a target request cannot be processed, maintaining robust and predictable behavior across all implementations.

6.11.4.2. TargetInfoStruct Type
This indicates an object describing the navigable target.

_Table parsed from section 'Data Types':_

* In the Target Navigator Cluster, under the Data Types section, the table row describes an element named 'Identifier' with an ID of '0'. This element is of type 'uint8', which is an unsigned 8-bit integer, and it has a constraint that its maximum value can be 254. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Identifier' element is always required to be implemented in any device or application that supports the Target Navigator Cluster, with no exceptions or conditions.

* In the Target Navigator Cluster, under the Data Types section, there is an entry with the ID '1' named 'Name', which is of the type 'string'. The conformance rule for this entry is marked as 'M', indicating that it is a Mandatory element. This means that the 'Name' attribute is always required to be implemented in any device or application that supports the Target Navigator Cluster, without any conditions or exceptions.

6.11.4.2.1. Identifier Field
This field SHALL contain an unique id within the TargetList.
6.11.4.2.2. Name Field
This field SHALL contain a name string for the TargetInfoStruct.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "TargetList" within the Target Navigator Cluster, specifically under the Attributes section. This attribute has an ID of '0x0000' and is of the type 'list[TargetInfoStruct]', indicating it is a list composed of structures defined as TargetInfoStruct. The access level for this attribute is 'R V', meaning it is readable and can be viewed. The conformance rule for "TargetList" is 'M', which stands for Mandatory. This means that the "TargetList" attribute is always required to be implemented in any device or application that supports the Target Navigator Cluster, with no conditions or exceptions.

* The table row describes an attribute named "CurrentTarget" within the Target Navigator Cluster. This attribute has an ID of '0x0001' and is of type 'uint8'. Its constraints are described elsewhere in the documentation, as indicated by 'desc'. The default value for "CurrentTarget" is '0xFF', and it has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'O', meaning that the "CurrentTarget" attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

6.11.5.1. TargetList Attribute
This attribute SHALL represent a list of targets that can be navigated to within the experience pre
sented to the user by the Endpoint (Video Player or Content App). The list SHALL NOT contain any
entries with the same Identifier in the TargetInfoStruct object.
6.11.5.2. CurrentTarget Attribute
This attribute SHALL represent the Identifier for the target which is currently in foreground on the
corresponding Endpoint (Video Player or Content App), or 0xFF to indicate that no target is in the
foreground.
When not 0xFF, the CurrentTarget SHALL be an Identifier value contained within one of the Target
InfoStruct objects in the TargetList attribute.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Target Navigator Cluster, specifically the "NavigateTarget" command. This command is initiated by a client and directed towards a server, and it expects a response in the form of "NavigateTargetResponse." The access level for this command is marked as "Optional" (O), indicating that the command may not be accessible in all implementations. However, the conformance rule for this command is marked as "Mandatory" (M), meaning that the "NavigateTarget" command must always be implemented and supported in any device or application that includes the Target Navigator Cluster, regardless of any other conditions or features.

* The table row describes a command within the Target Navigator Cluster, specifically the "NavigateTargetResponse" command. This command is identified by the ID '0x01' and is directed from the server to the client, as indicated by the direction 'client ⇐ server'. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked with 'M', which means that this command is mandatory. It must always be implemented and supported in any device or application that uses the Target Navigator Cluster, without any conditions or exceptions.

6.11.6.1. NavigateTarget Command
Upon receipt, this SHALL navigation the UX to the target identified.

_Table parsed from section 'Commands':_

* In the Target Navigator Cluster, under the Commands section, the table row describes a command with the ID '0', which has a field named 'Target'. This field is of type 'uint8', meaning it is an unsigned 8-bit integer, and it has a constraint labeled 'all', indicating that it can take any value within the range of an 8-bit unsigned integer. The conformance rule for this field is 'M', which stands for Mandatory. This means that the 'Target' field is always required to be implemented in any device or application that supports the Target Navigator Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* In the Target Navigator Cluster, within the Commands section, there is an entry for a command identified by 'ID' 1, which involves a field named 'Data'. This field is of the 'string' type and has a default value of 'MS'. The conformance rule for this entry is 'O', indicating that the 'Data' field is optional. This means that the inclusion of this field is not required and it does not depend on any other conditions or features. It can be implemented at the discretion of the developer, without any mandatory obligation.

6.11.6.1.1. Target Field
This field SHALL indicate the Identifier for the target for UX navigation. The Target SHALL be an
Identifier value contained within one of the TargetInfoStruct objects in the TargetList attribute.
6.11.6.1.2. Data Field
This field SHALL indicate Optional app-specific data.
6.11.6.2. NavigateTargetResponse Command
This command SHALL be generated in response to NavigateTarget command.

_Table parsed from section 'Commands':_

* In the Target Navigator Cluster, within the Commands section, there is an entry for a command identified by 'ID' 0, which pertains to the 'Status' field of type 'StatusEnum'. The 'Constraint' for this field is 'all', indicating it applies universally within this context. The 'Conformance' for this entry is marked as 'M', which means that the 'Status' field is mandatory. This implies that the 'Status' field must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

* In the Target Navigator Cluster, within the Commands section, there is an entry for a command with the ID '1', labeled as 'Data'. This command is of the type 'string' and can have any value as its constraint, with a default value of 'MS'. The conformance rule for this command is 'O', which means that this command is optional. It is not required for implementation and does not have any dependencies or conditions that would make it mandatory. Therefore, developers can choose whether or not to include this command in their implementation of the Target Navigator Cluster.

6.11.6.2.1. Status Field
This field SHALL indicate the of the command.
6.11.6.2.2. Data Field
This field SHALL indicate Optional app-specific data.

## Events

_Table parsed from section 'Events':_

* The table row describes an event named "TargetUpdated" within the Target Navigator Cluster, identified by the ID '0x00'. This event is categorized under the 'Events' section and has a priority level of 'INFO', indicating it provides informational updates. The 'Access' field is marked as 'V', which typically denotes that the event is visible or can be accessed in some manner. The 'Conformance' field is marked as 'O', meaning that the "TargetUpdated" event is optional. This indicates that the implementation of this event is not required and does not depend on any other features or conditions. Devices or applications implementing the Target Navigator Cluster can choose to include this event, but it is not mandatory for compliance with the Matter specification.

6.11.7.1. TargetUpdated Event
This event SHALL be generated when there is a change in either the active target or the list of avail
able targets or both. This event SHALL have the following data fields:

_Table parsed from section 'Events':_

* In the Target Navigator Cluster, within the Events section, there is an entry for an event named "TargetList" with an ID of '0'. This event is of the type 'list[TargetInfoStruct]', indicating that it consists of a list of structures, each representing target information. The conformance rule for this event is marked as 'O', which stands for Optional. This means that the "TargetList" event is not required to be implemented in all devices or scenarios; it can be included at the discretion of the developer or manufacturer, without any dependencies or conditions that must be met for its inclusion.

* In the Target Navigator Cluster, within the Events section, there is an entry for an event named "CurrentTarget" with an ID of '1'. This event is of type 'uint8', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The default value for this event is '0xFF'. According to the conformance rule 'O', the "CurrentTarget" event is optional, meaning it is not required to be implemented and has no dependencies on other features or conditions. This allows for flexibility in its inclusion within a device's implementation of the Target Navigator Cluster.

* In the Target Navigator Cluster, within the Events section, there is an entry with the ID '2' named 'Data'. This entry is of the type 'octstr', which stands for an octet string, and it has a constraint limiting its maximum size to 900 bytes. The conformance rule for this entry is marked as 'O', indicating that the 'Data' element is optional. This means that while the element can be included in implementations, it is not required and there are no dependencies or conditions that mandate its inclusion.

6.11.7.2. TargetList Field
This field SHALL indicate the updated target list as defined by the TargetList attribute if there is a
change in the list of targets. Otherwise this field can be omitted from the event.
6.11.7.3. CurrentTarget Field
This field SHALL indicate the updated target that is in foreground as defined by the CurrentTarget
attribute if supported (see CurrentTarget attribute for constraints).
6.11.7.4. Data Field
This field SHALL indicate Optional app-specific data.