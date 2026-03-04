
# 6.12 Content App Observer Cluster

This cluster provides an interface for sending targeted commands to an Observer of a Content App
on a Video Player device such as a Streaming Media Player, Smart TV or Smart Screen.
The cluster server for Content App Observer is implemented by an endpoint that communicates
with a Content App, such as a Casting Video Client.
The cluster client for Content App Observer is implemented by a Content App endpoint.
A Content App is informed of the NodeId of an Observer when a binding is set on the Content App.
For a Content App Platform, the binding is set by the platform when a CastingVideoClient is granted
access to the Content App, and the CastingVideoClient supports the Content App Observer cluster.
The Content App can then send the ContentAppMessage to the Observer (server cluster), and the
Observer responds with a ContentAppMessageResponse.
The Data and EncodingHint fields of the ContentAppMessage and ContentAppMessageResponse
contain content app-specific values, the format and interpretation of which is defined by the Con
tent App vendor, analogous to the custom message features offered by other popular casting proto
cols. Standardized cluster and commands are used here rather than manufacturer-specific cluster
and commands because of the role that the Content App Platform plays in creating the ACLs and
Bindings on both sides of the communication between the Content App Observer endpoint and the
Content App endpoint.
By using standard cluster and commands:
1. The Content App Platform is able to easily determine that a binding is needed on the Content
App endpoint because it can recognize the Content App Observer cluster implemented by a
client node.
2. The Content App Platform is able to easily identify commands that are allowed to be sent by the
Content App to a client node because those commands use the Content App Observer cluster.
3. The Content App is able to easily determine that a node supports the Content App Observer clus
ter because it has received a binding which specifies the Content App Observer cluster.
4. The Casting Video Client is able to support a single cluster for receiving commands from any
Content App and does not need to explicitly list every Content App it understands.
A Content App Observer SHOULD ignore the Data and EncodingHint field values in commands from
a Content App it does not recognize. A Content App SHOULD ignore the Data field values in
responses when the EncodingHint value is blank or not recognized.

## Data Types
6.12.4.1. StatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Content App Observer Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '0' and the 'Name' of 'Success', which summarizes as 'Command succeeded'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Success' data type is always required to be implemented in any device or application that supports the Content App Observer Cluster, without any conditions or exceptions.

* In the Content App Observer Cluster, under the Data Types section, the entry for 'UnexpectedData' with a value of '1' indicates a data field in a command that was not understood by the Observer. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. This ensures that the system consistently recognizes and handles instances where data is not understood, maintaining robust communication and error handling within the IoT ecosystem.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Content App Observer Cluster, specifically the "ContentAppMessage" command. This command is sent from a client to a server and expects a response in the form of "ContentAppMessageResponse." The access level for this command is optional, meaning it is not required to be implemented by default. However, the conformance rule for this command is marked as "M," indicating that the "ContentAppMessage" command is mandatory. This means that, regardless of the optional access level, the command must be implemented in any device or application that supports the Content App Observer Cluster, ensuring consistent functionality across all compliant implementations.

* The table row describes a command within the Content App Observer Cluster, specifically the "ContentAppMessageResponse" command. This command is identified by the ID '0x01' and is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked with 'M', which means this command is mandatory. According to the Matter Conformance Interpretation Guide, a mandatory conformance ('M') indicates that this command is always required to be implemented in any device or application that supports the Content App Observer Cluster.

6.12.5.1. ContentAppMessage Command
Upon receipt, the data field MAY be parsed and interpreted. Message encoding is specific to the Con
tent App. A Content App MAY when possible read attributes from the Basic Information Cluster on
the Observer and use this to determine the Message encoding.
This command returns a ContentAppMessage Response.

_Table parsed from section 'Commands':_

* In the Content App Observer Cluster, under the Commands section, there is a command identified by ID '0' named 'Data'. This command is of the type 'string' and has a constraint that limits its maximum length to 500 characters. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Data' command is always required to be implemented in any device or application that supports the Content App Observer Cluster, without any conditions or exceptions.

* In the Content App Observer Cluster, under the Commands section, there is a command identified by ID '1' named 'EncodingHint'. This command is of type 'string' and has a constraint limiting its maximum length to 100 characters. The conformance rule for 'EncodingHint' is marked as 'O', which means it is optional. This indicates that the implementation of this command is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this command based on their specific needs or preferences without any mandatory obligation.

6.12.5.1.1. Data Field
This field SHALL indicate content app-specific data.
6.12.5.1.2. EncodingHint Field
This optional field SHALL indicate a content app-specific hint to the encoding of the data.
6.12.5.2. ContentAppMessageResponse Command
This command SHALL be generated in response to ContentAppMessage command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content App Observer Cluster, specifically the "Status" command, which is identified by the ID '0' and is of the type 'StatusEnum'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Conformance' field is marked as 'M', which means that the "Status" command is mandatory. This implies that any implementation of the Content App Observer Cluster must include this command without exception. The mandatory status ensures that this command is always present and functional in any device or application using this cluster, according to the Matter IoT specification.

* In the Content App Observer Cluster, under the Commands section, there is a command identified by ID '1' named 'Data'. This command is of type 'string' and has a constraint limiting its maximum length to 500 characters. According to the conformance rule 'O', this command is optional, meaning it is not required to be implemented and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this command based on their specific application needs.

* The table row describes a command named "EncodingHint" within the Content App Observer Cluster, specifically under the Commands section. This command has an ID of '2' and is of the type 'string', with a constraint that limits its maximum length to 100 characters. The conformance rule for "EncodingHint" is marked as 'O', which means that this command is optional. It is not required for implementation and has no dependencies on other features or conditions. Implementers of the Content App Observer Cluster can choose to include this command, but it is not mandatory to do so according to the Matter specification.

6.12.5.2.1. Status Field
This field SHALL indicate the status of the command which resulted in this response.
6.12.5.2.2. Data Field
This optional field SHALL indicate content app-specific data.
6.12.5.2.3. EncodingHint Field
This optional field SHALL indicate a content app-specific hint to the encoding of the data.