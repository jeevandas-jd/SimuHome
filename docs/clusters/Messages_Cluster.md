
# 1.16 Messages Cluster

This cluster provides an interface for passing messages to be presented by a device.

## Data Types
1.16.5.1. MessageID Type
This data type is an octstr of fixed length 16, containing the binary encoding of a UUID as specified
in RFC 4122.
1.16.5.2. MessageControlBitmap Type
This data type is derived from map16, and indicates control information related to a message.

_Table parsed from section 'Data Types':_

* In the context of the Messages Cluster under the Data Types section, the table row describes a data type with the bit position '0', named 'ConfirmationRequired'. This data type indicates whether a message requires confirmation from the user. The conformance rule for 'ConfirmationRequired' is specified as 'CONF'. According to the Matter Conformance Interpretation Guide, this means that the presence of this element is mandatory if the feature or condition represented by 'CONF' is supported. If 'CONF' is not supported, the element is not required. This ensures that the 'ConfirmationRequired' attribute is only implemented when the relevant feature or condition is applicable, maintaining consistency and relevance within the Messages Cluster.

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes a data type with the bit position '1' named 'ResponseRequired'. This data type indicates that a message necessitates a response from the user. The conformance rule 'RESP' implies that the requirement for this element is conditional based on the support of the feature or element 'RESP'. If the feature 'RESP' is supported, then the 'ResponseRequired' element is mandatory. If 'RESP' is not supported, the conformance rule does not specify an alternative, suggesting that the element may not be applicable or required in such cases.

* In the context of the Messages Cluster, under the Data Types section, the table entry describes a data type with the bit position '2' named 'ReplyMessage'. This data type indicates that a message supports a reply message from the user. The conformance rule for 'ReplyMessage' is specified as 'RPLY'. According to the Matter Conformance Interpretation Guide, this means that the 'ReplyMessage' feature is mandatory if the feature code 'RPLY' is supported. If 'RPLY' is not supported, the conformance of this element is not explicitly defined in this entry, implying that it may not be required or applicable.

* In the context of the Messages Cluster's Data Types, the table row describes a data element identified by the bit position '3', named 'MessageConfirmed'. This element indicates whether a message has already been confirmed, as summarized by its name. The conformance rule for 'MessageConfirmed' is specified as 'CONF'. According to the Matter Conformance Interpretation Guide, this suggests that the presence or requirement of this element is contingent upon the support of a feature or condition labeled 'CONF'. If the 'CONF' feature is supported, the 'MessageConfirmed' element is mandatory; otherwise, its inclusion is not required. The specific details of what 'CONF' entails would be described elsewhere in the documentation.

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes a data type with the bit position '4', named 'MessageProtected'. This data type indicates whether a message requires PIN or password protection. The conformance rule for 'MessageProtected' is 'PROT', which suggests that the presence of this feature is contingent upon the support of a feature or condition labeled 'PROT'. According to the conformance interpretation guide, since 'PROT' is not enclosed in brackets, it implies that the 'MessageProtected' element is mandatory if the 'PROT' feature is supported. If 'PROT' is not supported, the conformance of 'MessageProtected' is not explicitly defined in this entry, which typically means it is not required.

1.16.5.2.1. ConfirmationRequired Bit
This bit SHALL indicate that the message originator requests a confirmation of receipt by the user.
If confirmation is required, the device SHOULD present the message until it is either confirmed by
the user selecting a confirmation option, or the message expires.
1.16.5.2.2. ResponseRequired Bit
This  bit  SHALL  indicate  that  a  MessagePresented  event  SHOULD  be  generated  based  on  the
response of the user to the message.
1.16.5.2.3. ReplyMessage Bit
This bit SHALL indicate that a free-form user reply is to be included in the confirmation of receipt.
1.16.5.2.4. MessageConfirmed Bit
This bit SHALL indicate the current confirmation state of a message, which is useful in the event
that there are multiple Messages cluster client devices on a network.
1.16.5.2.5. MessageProtected Bit
This bit SHALL indicate that user authentication (e.g. by password or PIN) is required before view
ing a message.
1.16.5.3. FutureMessagePreferenceEnum Type
This data type is derived from enum8.
A display device MAY include this preference in the MessageComplete event as a hint to clients
about how to handle future similar messages.

_Table parsed from section 'Data Types':_

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '0' and the 'Name' of 'Allowed'. This entry indicates that similar messages are permitted, as summarized by the 'Summary' field. The 'Conformance' field is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the feature or element described by this entry is always required and must be implemented in any device or application that supports the Messages Cluster. There are no conditions or dependencies affecting this requirement, making it an essential component of the specification.

* In the context of the Messages Cluster, specifically within the Data Types section, the table entry describes a data type with the name "Increased" and a value of '1'. The summary indicates that this data type is used when similar messages should be sent more frequently. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Increased" data type is always required to be implemented in any device or system that supports the Messages Cluster, without any conditions or exceptions.

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes a data type with the name "Reduced" and a value of '2'. The summary indicates that this data type is used to signify that similar messages should be sent less frequently. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Reduced" data type is always required to be implemented within the Messages Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status; it must be supported in all implementations of this cluster.

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes an element with the name "Disallowed," which has a value of '3'. The summary indicates that similar messages should not be sent. The conformance rule for this element is marked as 'M', meaning it is mandatory. This implies that within the Messages Cluster, the element "Disallowed" must always be implemented and adhered to, ensuring that similar messages are not sent, as it is a required part of the specification without any conditions or exceptions.

* In the Messages Cluster, under the Data Types section, the table entry describes a data type with the name "Banned" and a value of '4'. The summary indicates that when this data type is used, it signifies that no further messages should be sent. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Banned" data type is a required element within the Messages Cluster and must always be implemented according to the Matter specification.

1.16.5.4. MessagePriorityEnum Type
This data type is derived from enum8.
Priority SHOULD be used to decide which messages to show when the number of eligible messages
is larger than the device’s capacity to present them.

_Table parsed from section 'Data Types':_

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes a data type with the value '0', named 'Low'. This data type represents a message that is to be transferred with a low level of importance. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Low' importance level for messages is always required to be supported within the Messages Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the context of the Messages Cluster, specifically within the Data Types section, the table row describes a data type with the value '1' named 'Medium'. This data type represents a message that is to be transferred with a medium level of importance. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Medium' data type is always required to be implemented in any system or device that supports the Messages Cluster, without any conditions or exceptions.

* In the Messages Cluster, under the Data Types section, the table entry describes a data type named "High" with a value of '2'. This data type is used to indicate that a message should be transferred with a high level of importance. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "High" data type is always required to be implemented in any system or device that supports the Messages Cluster, ensuring that messages can be prioritized with high importance as part of the standard functionality.

* In the Messages Cluster under the Data Types section, the table row describes an entry with the name "Critical" and a value of '3'. This entry signifies a message that must be transferred with a critical level of importance. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "Critical" message type is always required to be supported within the Messages Cluster, with no conditions or exceptions.

1.16.5.5. MessageStruct Type
This represents a single message.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element identified as 'Access Qua'. The conformance rule for this element is not explicitly provided in the row data, but based on the context given, it likely involves interpreting the conformance string according to the Matter Conformance Interpretation Guide. If we assume a typical conformance string, it might specify conditions under which 'Access Qua' is required, optional, or otherwise. For example, if the conformance were `M`, it would mean 'Access Qua' is always mandatory. If it were `O`, it would be optional with no dependencies. Without a specific conformance string provided, we can only infer that the element's inclusion or behavior is determined by the rules outlined in the guide, potentially involving logical conditions or dependencies on other features or elements within the Messages Cluster.

* The table row pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element related to the 'Access Quality: Fabric' and 'Scoped' attributes, both associated with 'MessageID'. The conformance rule for this element is not explicitly provided in the given data, but based on the context, it seems to be a fundamental part of the Messages Cluster. The absence of a specific conformance tag or expression suggests that this element might be inherently required or assumed as a standard part of the cluster's functionality. If a conformance rule were provided, it would dictate the conditions under which this element is mandatory, optional, or otherwise, as per the Matter Conformance Interpretation Guide.

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element labeled as 'Access Qua'. This element has a conformance rule of '1', indicating that it is mandatory and must always be implemented according to the Matter specification. The 'lity: Fabric' field is set to 'Priority', suggesting that this element is related to prioritizing messages within the context of a fabric, which is a network of devices. The 'Scoped' field is defined as 'MessagePriorityEnum', meaning that the element is scoped or categorized under the enumeration of message priorities. In summary, this entry mandates the implementation of a priority-related data type within the Messages Cluster, ensuring that message handling respects the defined priority levels in a Matter-compliant network.

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Access Qua' with a quality of 'Fabric'. This element is associated with the 'MessageControl' and is scoped as 'MessageControlBitmap'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves a condition where the element's requirement is dependent on the presence or absence of certain features or conditions within the Messages Cluster. Without a specific conformance string, we can infer that the element's inclusion or behavior is determined by its relationship to the 'MessageControl' and 'MessageControlBitmap', potentially indicating that it is mandatory or optional based on the support of these features.

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Access Qua' with a value of '3', which likely denotes a specific access level or quality requirement. The 'lity: Fabric' field is associated with 'StartTime', indicating that this data type or attribute is related to the start time within the context of a fabric, which in IoT terms often refers to a network or group of devices. The 'Scoped' field is set to 'epoch-s', suggesting that the time is measured in seconds since the epoch (a standard time reference point). The conformance rule for this entry is not explicitly provided in the data given, but based on the context, it would typically define when this data type is required or optional within the Messages Cluster. Without a specific conformance string, we cannot apply the detailed rules from the guide, but generally, this entry describes a time-related attribute that is relevant to the operation or

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically describing a data type with the name "Access Quality: Fabric Duration," which is of type `uint64`. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage, it likely indicates how this data type should be implemented or supported within the Messages Cluster. Since the conformance rule is not detailed here, it would typically be found in the broader documentation or specification. Generally, this data type is used to represent a duration associated with fabric access quality, and its implementation would depend on the specific conformance conditions outlined elsewhere in the Matter specification.

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Access Qua'. This element is associated with a quality level of '5', and it is scoped to the 'Fabric' context, with a data type of 'MessageText', which is a 'string'. The conformance rule for this element is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, if there were a conformance string, it would dictate when this element is required or optional. For example, if the conformance were 'M', it would mean the element is always mandatory. If it were 'O', it would be optional. Without a specific conformance string, we cannot determine the exact requirement status of this element.

* The table row entry pertains to the "Messages Cluster" within the "Data Types" section, specifically focusing on a data type called 'Access Qua'. This data type has an access quality level of '6', indicating a certain level of priority or requirement within the system. The 'lity: Fabric' field is set to 'Responses', suggesting that this data type is related to handling or processing responses within the fabric of the network. The 'Scoped' field indicates that this data type is a list of 'MessageResponseOptionStruct', which likely defines the structure or format of the response options. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage, it could imply that the presence and structure of this data type are conditionally required or optional depending on specific features or conditions within the Messages Cluster. Without a specific conformance string, further details would be described elsewhere in the documentation.

1.16.5.5.1. MessageID Field
This field SHALL indicate a globally unique ID for this message.
1.16.5.5.2. Priority Field
This field SHALL indicate the priority level for this message.
1.16.5.5.3. MessageControl Field
This field SHALL indicate control information related to the message.
1.16.5.5.4. StartTime Field
This field SHALL indicate the time in UTC at which the message becomes available to be presented.
A null value SHALL indicate "now."
1.16.5.5.5. Duration Field
This field SHALL indicate the amount of time, in milliseconds, after the StartTime during which the
message is available to be presented. A null value SHALL indicate "until changed".
1.16.5.5.6. MessageText Field
This field SHALL indicate a string containing the message to be presented.
1.16.5.5.7. Responses Field
This field SHALL indicate a list of potential responses to the message. The entries in this list SHALL
have unique values of MessageResponseID.
If the ResponseRequired bit is set on the message but this list is empty, the device SHALL provide a
generic acknowledgement button, e.g. "OK".
If the ResponseRequired bit is not set on the message, this list SHALL be ignored.
1.16.5.6. MessageResponseOptionStruct Type
This represents a possible response to a message.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Messages Cluster, specifically in the Data Types section, identified as 'MessageResponseID'. This element is of type 'uint32', meaning it is a 32-bit unsigned integer, and it has a constraint that requires its value to be at least 1. The conformance rule for 'MessageResponseID' is 'M', which stands for Mandatory. This means that the 'MessageResponseID' element is always required to be implemented in any device or application that supports the Messages Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement status; it must be present in all relevant implementations.

* In the Messages Cluster, under the Data Types section, there is an entry for an element with the ID '1' named 'Label'. This element is of the 'string' type and has a constraint that limits its maximum length to 32 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Label' element is always required to be implemented in any device or application that supports the Messages Cluster, without any conditions or exceptions.

1.16.5.6.1. MessageResponseID Field
This field SHALL indicate a unique unsigned 32-bit number identifier for this message response
option.
1.16.5.6.2. Label Field
This field SHALL indicate the text for this option; e.g. "Yes", "No", etc.

## Attributes

_Table parsed from section 'Attributes':_

* In the Messages Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0000' named 'Messages'. This attribute is of the type 'list[MessageStruct]', constrained to a maximum of 8 entries, and defaults to being empty. It has access permissions denoted by 'R V F', indicating it can be read, verified, and is fabric-scoped. The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device or application using the Messages Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Messages Cluster, specifically the "ActiveMessageIDs" attribute. This attribute is identified by the ID `0x0001` and is of the type `list[MessageID]`, with a constraint allowing a maximum of 8 entries. By default, this list is empty. The access level for this attribute is read-only and viewable (`R V`). The conformance rule for "ActiveMessageIDs" is marked as `M`, which means this attribute is mandatory and must always be implemented in any device or application that supports the Messages Cluster.

1.16.6.1. Messages Attribute
This attribute SHALL indicate a list of queued messages.
In addition to filtering based upon fabric, to preserve user privacy, the server MAY further limit the
set of messages returned in a read request. At minimum, the server SHALL return to a client those
messages that the client itself created/submitted.
1.16.6.2. ActiveMessageIDs Attribute
This attribute SHALL indicate a list of the MessageIDs of the Messages currently being presented. If
this list is empty, no messages are currently being presented.
This list SHALL NOT be fabric-scoped; it SHALL contain MessageIDs for all Messages being pre
sented, no matter what fabric the client that queued them is on.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Messages Cluster, specifically the "PresentMessagesRequest" command, which is identified by the ID '0x00'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level is marked as 'O F', which typically denotes optional access with some form of additional condition or feature. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "PresentMessagesRequest" command must always be implemented and supported in any device or application that utilizes the Messages Cluster, without any conditions or exceptions.

* The table row describes a command within the Messages Cluster, specifically the "CancelMessagesRequest" command, which is directed from the client to the server. The command has an ID of '0x01' and requires a response ('Y'). The access level is marked as 'O F', indicating optional access with some form of restriction or condition. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "CancelMessagesRequest" command must always be implemented and supported in any device or application that uses the Messages Cluster, without any conditions or exceptions.

1.16.7.1. PresentMessagesRequest Command
Upon receipt, this SHALL cause the message in the passed fields to be appended to the Messages
attribute.
If appending the message would cause the number of messages to be greater than the capacity of
the list, the device SHALL NOT append any message to Messages, and SHALL return a status code of
RESOURCE_EXHAUSTED.
When displaying a message in response to this command, an indication (ex. visual) of the origin
node of the command SHALL be provided. This could be in the form of a friendly name label which
uniquely identifies the node to the user. This friendly name label is typically assigned by the Matter
Admin at the time of commissioning and, when it’s a device, is often editable by the user. It might
be a combination of a company name and friendly name, for example, ”Acme” or “Acme Streaming
Service on Alice’s Phone”.
It is currently not specified where the friendly name label can be found on the
node, meaning that clients SHOULD NOT rely on a certain method they happen to
NOTE
observe in a particular server instance, since other instances could employ a differ
ent method.
The device SHOULD make it possible for the user to view which nodes have access to this cluster
and to individually remove privileges for each node.

_Table parsed from section 'Commands':_

* The table row describes an element within the Messages Cluster, specifically under the Commands section. The element is identified by the ID '0' and is named 'MessageID', with a type also specified as 'MessageID'. The constraint for this element is 'all', indicating it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'MessageID' command is always required to be implemented in any device or application that supports the Messages Cluster, with no exceptions or conditional dependencies.

* In the context of the Messages Cluster, specifically within the Commands section, the table row describes a command identified by 'ID' 1, named 'Priority', which is of the type 'MessagePriorityEnum' and has a default value of '0'. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'Priority' command is always required to be implemented in any device or application that supports the Messages Cluster. There are no conditions or exceptions; it is a fundamental and non-negotiable part of the specification for this cluster.

* The table row describes a command within the Messages Cluster, specifically the "MessageControl" command, which is of the type "MessageControlBitmap" and has a default value of '0'. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the "MessageControl" command is always required to be implemented in any device or application that supports the Messages Cluster, without any conditions or exceptions.

* The table row describes a command within the Messages Cluster, specifically the "StartTime" command. This command has an ID of '3', is of the type 'epoch-s', and has a default value of '0'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', which means that the "StartTime" command is mandatory. This implies that the command must always be implemented and supported within the Messages Cluster, with no conditions or exceptions.

* In the Messages Cluster, within the Commands section, there is an entry for a command named "Duration" with an ID of '4'. This command is of type 'uint64' and applies to all constraints, with a default value of '0'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' for this command is marked as 'M', meaning it is mandatory. This implies that the "Duration" command must always be implemented and supported in any device or application that conforms to this specification, without any conditions or exceptions.

* The table row describes a command within the Messages Cluster, specifically the 'MessageText' command. This command has an ID of '5' and is of the 'string' type, with a constraint that limits its maximum length to 256 characters. The conformance rule for 'MessageText' is denoted by 'M', which means it is a Mandatory element. This implies that the 'MessageText' command is always required to be implemented in any device or application that supports the Messages Cluster, with no exceptions or conditions.

* The table row describes a command named "Responses" within the Messages Cluster, identified by ID '6'. This command is of the type 'list[MessageResponseOptionStruct]' and is constrained to a maximum of 4 entries, with a default state of being empty. The conformance rule for this command is 'RESP', indicating that its requirement status is conditional based on the support of a feature or condition labeled 'RESP'. If the feature 'RESP' is supported, the command becomes mandatory. If 'RESP' is not supported, the command is not required. The specific details of the 'RESP' condition would be defined elsewhere in the documentation.

1.16.7.1.1. MessageID Field
This field SHALL indicate a globally unique ID for this message. See MessageID.
1.16.7.1.2. Priority Field
This field SHALL indicate the priority level for this message. See Priority.
1.16.7.1.3. MessageControl Field
This field SHALL indicate control information related to the message. See MessageControl.
1.16.7.1.4. StartTime Field
This field SHALL indicate the time in UTC at which the message becomes available to be presented.
A null value SHALL indicate "now." See StartTime.
1.16.7.1.5. Duration Field
This field SHALL indicate the amount of time, in milliseconds, after the StartTime during which the
message is available to be presented. A null value SHALL indicate "until changed". See Duration.
1.16.7.1.6. MessageText Field
This field SHALL indicate a string containing the message to be presented. See MessageText.
1.16.7.1.7. Responses Field
This field SHALL indicate a list of potential responses to the message. The entries in this list SHALL
have unique values of MessageResponseID.
If the ResponseRequired bit is set on the message but this list is empty, the device SHALL provide a
generic acknowledgement button, e.g. "OK".
If the ResponseRequired bit is not set on the message, this list SHALL be ignored.
See Responses.
1.16.7.2. CancelMessagesRequest Command

_Table parsed from section 'Commands':_

* In the Messages Cluster, under the Commands section, the table row describes an element named "MessageIDs" with an ID of '0'. This element is of the type 'list[MessageID]' and is constrained to a maximum of 8 entries. The conformance rule for "MessageIDs" is marked as 'M', which stands for Mandatory. This means that the "MessageIDs" element is always required to be implemented in any device or application that supports the Messages Cluster, without any conditions or exceptions.

1.16.7.2.1. MessageIDs Field
This field SHALL indicate the MessageIDs for the messages being cancelled.
Cancelling a message SHALL cause it to be removed from Messages, cause its MessageID to be
removed from ActiveMessageIDs and cause any active presentation of the message to cease.
Message IDs in this command that indicate messages that do not exist in Messages, or that are not
scoped to the fabric of the sender, SHALL be ignored.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Messages Cluster, specifically the "MessageQueued" event, which is identified by the ID '0x00'. This event has an informational priority level, indicated by 'INFO', and its access level is designated as 'V', which typically stands for viewable or visible. The conformance rule for this event is 'M', meaning it is mandatory. This implies that the "MessageQueued" event must always be implemented and supported in any device or application that utilizes the Messages Cluster, without any conditions or exceptions.

* The table row describes an event within the Messages Cluster, specifically the "MessagePresented" event, identified by the ID '0x01'. This event has an informational priority level and requires 'V' access, which typically denotes visibility or read access. The conformance rule for this event is 'M', meaning it is mandatory. This indicates that the "MessagePresented" event must always be implemented and supported in any device or application that includes the Messages Cluster, without any conditions or exceptions.

* The table row entry pertains to the "Messages Cluster" within the "Events" section, specifically describing an event named "MessageComplete" with an ID of '0x02'. This event is categorized with a priority level of "INFO" and has an access level denoted by 'V'. The conformance rule for "MessageComplete" is marked as 'M', which, according to the Matter Conformance Interpretation Guide, indicates that this event is mandatory. This means that the "MessageComplete" event must always be implemented and supported within the Messages Cluster, without any conditions or exceptions.

1.16.8.1. MessageQueued Event
This event SHALL be generated when a message is added to the messages attribute.

_Table parsed from section 'Events':_

* The table row describes an element within the "Messages Cluster" under the "Events" section. The element in question is identified by the 'Access Quali' with an 'ID', and it is associated with a 'Name' that is sensitive to the 'Type' of fabric. The conformance rule for this element is not explicitly provided in the data snippet, but based on the context, it likely involves conditions related to the fabric sensitivity and access qualifications. Without a specific conformance string, we can infer that the element's inclusion or behavior might depend on the fabric's sensitivity type or access qualifications, potentially involving mandatory, optional, or other conditional statuses as outlined in the Matter Conformance Interpretation Guide.

* The table row pertains to the "Messages Cluster" within the "Events" section and describes an element with the following attributes: 'Access Quali' is '0', and 'ty: Fabric-Sen' and 'sitive' are both 'MessageID'. The conformance rule for this element is not explicitly provided in the data snippet, but based on the context, it likely involves a condition or status related to the 'MessageID'. If we assume a conformance rule was intended but omitted, it would typically specify whether the element is mandatory, optional, or subject to conditions based on the presence or absence of certain features. For instance, if the conformance were 'M', it would mean the element is always required. If it were 'O', it would be optional. Without the specific conformance string, we can only infer that the element's inclusion or behavior might depend on the presence of certain features or conditions related to 'MessageID'.

1.16.8.1.1. MessageID Field
This field SHALL indicate the MessageID for newly added message.
1.16.8.2. MessagePresented Event
This event SHALL be generated when the message is presented to the user.

_Table parsed from section 'Events':_

* The table row pertains to the "Messages Cluster" within the "Events" section, focusing on an element identified by 'Access Quali' with an ID, 'ty: Fabric-Sen' with a Name, and 'sitive' with a Type. The conformance rule for this element is not explicitly provided in the row data, but based on the context and the Matter Conformance Interpretation Guide, we would interpret any conformance string associated with this element to determine its requirement status. If a conformance string were present, it would specify whether the element is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on supported features or logical expressions. Without a specific conformance string, we cannot definitively state the requirement status of this element.

* The table row pertains to the "Messages Cluster" within the "Events" section. The entry describes an element related to "Access Quali" with a value of '0', and it is associated with the attribute or identifier 'MessageID', which is marked as 'Fabric-Sensitive'. The conformance rule for this entry is not explicitly provided in the data snippet, but based on the context, it likely involves conditions related to the 'MessageID' being sensitive to the fabric context. This implies that the element's presence or behavior may depend on specific conditions or configurations within the Matter protocol, potentially involving security or privacy considerations due to its fabric-sensitive nature. Without a direct conformance string, we assume that the element's inclusion or behavior is contingent upon these contextual factors, possibly requiring further documentation for precise implementation details.

1.16.8.2.1. MessageID Field
This field SHALL indicate the MessageID for the message being presented.
1.16.8.3. MessageComplete Event
This event SHALL be generated when the message is confirmed by the user, or when the Duration
of the message has elapsed without confirmation.

_Table parsed from section 'Events':_

* The table row pertains to the "Messages Cluster" within the "Events" section, focusing on an element identified by 'Access Quali' with the ID, 'ty: Fabric-Sen' as the Name, and 'sitive' as the Type. The conformance rule for this element is not explicitly provided in the data snippet, but based on the context, it would typically describe the conditions under which this element is required or optional. If we were to interpret a typical conformance rule using the guide, it would specify whether the element is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on supported features or logical expressions. Since the conformance rule is missing, we cannot determine the specific requirements or conditions for this element without additional information.

* The table row pertains to the "Messages Cluster" within the "Events" section, focusing on an element related to the "MessageID." The 'Conformance' field is not explicitly provided in the data, but based on the context, we can infer that the 'Access Quali' is set to '0', which might indicate a default or base level access requirement. The 'ty: Fabric-Sen' and 'sitive' fields both reference 'MessageID', suggesting that this element is sensitive to the fabric context, possibly implying that it is crucial for identifying messages within a specific fabric. Without a specific conformance string, we cannot apply the detailed rules from the guide, but generally, this entry likely indicates that the 'MessageID' is a key element in the Messages Cluster, potentially with specific access or sensitivity considerations that are contextually important.

* The table row describes an element within the "Messages Cluster" under the "Events" section. This element is identified by the 'Access Quali' value of '1', which likely refers to a specific access level or requirement. The element is of type 'ResponseID' and is 'Fabric-Sensitive', meaning it is sensitive to the fabric (network) context in which it operates. The data type for this element is 'uint32', indicating it is a 32-bit unsigned integer. The conformance rule for this element is not explicitly provided in the row data, but based on the context, it would be necessary to refer to additional documentation to determine its exact conformance requirements. Without a specific conformance string, we assume that the element's inclusion and behavior are governed by the broader rules and conditions outlined in the Matter specification for events within the Messages Cluster.

* The table row pertains to the "Messages Cluster" within the "Events" section, focusing on an element described as 'Access Quali' with a value of '2', and 'ty: Fabric-Sen' with a value of 'Reply', and 'sitive' as 'string'. The conformance rule for this element is not explicitly provided in the row data, but based on the context, it likely involves a specific condition or requirement related to the access quality and sensitivity of the message events. The 'Access Quali' value of '2' might indicate a specific level of access required, while 'ty: Fabric-Sen' suggests that the element is sensitive to the fabric context, possibly affecting how replies are handled. Without a direct conformance string, we can infer that this element's inclusion or behavior might depend on specific conditions or configurations within the Matter specification, potentially involving mandatory or optional status based on certain features or contexts.

* The table row pertains to the "Messages Cluster" within the "Events" section, specifically focusing on an element labeled "FutureMessagesPreference" with an access qualifier of '3' and a sensitivity type of "FutureMessagePreferenceEnum." The conformance rule for this element is not explicitly provided in the given data, but based on the context and typical usage of conformance expressions, it likely involves conditions or future considerations for its implementation. In general, such entries describe how and when certain features or attributes should be implemented or supported within the Matter IoT specification. If a conformance expression were provided, it would dictate whether this element is mandatory, optional, provisional, deprecated, or disallowed, potentially based on the presence or absence of certain features or conditions.

1.16.8.3.1. MessageID Field
This field SHALL indicate the MessageID for the message being confirmed.
1.16.8.3.2. ResponseID Field
This field SHALL indicate the MessageResponseID selected by the user. If there was no response
before the Duration of the message has elapsed, this field SHALL be null.
1.16.8.3.3. Reply Field
This field SHALL indicate a user-provided reply to the message. If there was no reply, or the mes
sage did not have the ReplyRequired bit set, this field SHALL be null.
1.16.8.3.4. FutureMessagesPref Field
This field SHALL indicate a user-provided preference for the delivery of similar messages in the
future. A null value SHALL indicate no change in preference.