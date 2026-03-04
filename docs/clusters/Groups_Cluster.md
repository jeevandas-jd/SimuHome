
# 1.3 Groups Cluster

The Groups cluster manages, per endpoint, the content of the node-wide Group Table that is part of
the underlying interaction layer.
In a network supporting fabrics, group IDs referenced by attributes or other elements of this cluster
are scoped to the accessing fabric.
The Groups cluster is scoped to the endpoint. Groups cluster commands support discovering the
endpoint membership in a group, adding the endpoint to a group, removing the endpoint from a
group, removing endpoint membership from all groups. All commands defined in this cluster
SHALL only affect groups scoped to the accessing fabric.
When group names are supported, the server stores a name string, which is set by the client for
each assigned group and indicated in response to a client request.
Note that configuration of group addresses for outgoing commands is achieved using the Message
Layer mechanisms where the Group Table is not involved. Hence this cluster does not play a part in
that.

## Data Types
1.3.5.1. NameSupportBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Groups Cluster under the Data Types section, the table row describes a feature identified by the bit '7', named 'GroupNames'. This feature allows for the storage of a name associated with a group. According to the conformance rule 'M', this feature is mandatory, meaning it is always required to be implemented in any device or application that supports the Groups Cluster. There are no conditions or dependencies affecting this requirement, ensuring that the ability to store a name for a group is consistently available across all implementations.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Groups Cluster, specifically the "NameSupport" attribute, which is identified by the ID '0x0000' and is of the type 'NameSupportBitmap'. The attribute is constrained by a description provided elsewhere in the documentation, and it has a default value of '0'. It is marked with a quality of 'F', indicating it is a fundamental attribute, and its access is read-only and viewable ('R V'). The conformance rule for this attribute is 'M', meaning it is mandatory and must always be implemented in any device that supports the Groups Cluster. This requirement ensures that the "NameSupport" attribute is consistently available across all compliant devices, facilitating interoperability and standard functionality within the Matter IoT ecosystem.

1.3.6.1. NameSupport Attribute
This attribute provides legacy, read-only access to whether the Group Names feature is supported.
The most significant bit, bit 7 (GroupNames), SHALL be equal to bit 0 of the FeatureMap attribute
(GN Feature). All other bits SHALL be 0.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the "AddGroup" command, which is directed from the client to the server. The command has an associated response called "AddGroupResponse" and requires mandatory access control, indicated by 'M F'. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "AddGroup" command must always be implemented in any device that supports the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "ViewGroup" command, which is directed from the client to the server. The command is identified by the ID '0x01' and expects a response in the form of 'ViewGroupResponse'. The access level for this command is marked as 'O F', indicating it is optional and possibly subject to further conditions or features not detailed here. The conformance rule for the "ViewGroup" command is marked as 'M', meaning it is mandatory. This indicates that any implementation of the Groups Cluster must support the "ViewGroup" command, ensuring it is always available and functional in compliant devices.

* The table row describes a command within the Groups Cluster, specifically the "GetGroupMembership" command, which is directed from the client to the server. This command is associated with the response "GetGroupMembershipResponse" and has an access level of "O F," indicating optional access with fabric scope. The conformance rule for this command is marked as "M," which means it is mandatory. This indicates that the "GetGroupMembership" command must always be implemented and supported in any device or application that conforms to the Matter specification for the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "RemoveGroup" command, which is identified by the ID '0x03'. This command is directed from the client to the server and expects a response in the form of "RemoveGroupResponse". The access level for this command is marked as 'M F', indicating that it is mandatory and requires fabric-level access. The conformance rule for this command is simply 'M', which means that the "RemoveGroup" command is always mandatory. This implies that any implementation of the Groups Cluster must support this command without exception.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the "RemoveAllGroups" command, which is directed from the client to the server. The command has an ID of '0x04' and requires a response, as indicated by 'Response: Y'. The 'Access' field specifies 'M F', suggesting mandatory access with some form of filtering or additional access control. The 'Conformance' field is marked as 'M', which means that the "RemoveAllGroups" command is mandatory. This implies that any implementation of the Groups Cluster must include this command as a required feature, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "AddGroupIfIdentifying" command, which is directed from the client to the server. The command has an identifier of '0x05' and requires a response ('Y'). The access level is marked as 'M F', indicating mandatory access with fabric-scoped permissions. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "AddGroupIfIdentifying" command must always be implemented in any device that supports the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "AddGroupResponse" command, which is identified by the ID '0x00'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The "Response" field marked as 'N' suggests that this command does not require an additional response. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "AddGroupResponse" command must always be implemented and supported in any device or application that utilizes the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "ViewGroupResponse" command, which is sent from the server to the client. The 'ID' for this command is '0x01', and it does not require a response ('Response': 'N'). The 'Conformance' field is marked as 'M', indicating that this command is mandatory. This means that in any implementation of the Groups Cluster, the "ViewGroupResponse" command must always be supported and implemented without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "GetGroupMembershipResponse" command, which is directed from the server to the client. The 'Response' field indicates that this command does not expect a response. The 'Conformance' field is marked as 'M', meaning this command is mandatory. This implies that any implementation of the Groups Cluster must include the "GetGroupMembershipResponse" command as a required feature, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "RemoveGroupResponse" command, which is identified by the ID '0x03'. This command is directed from the server to the client, as indicated by the direction "client ⇐ server". The 'Response' field is marked 'N', suggesting that this command does not expect a response. The 'Conformance' field is marked with 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "RemoveGroupResponse" command is always required to be implemented in any device or application that supports the Groups Cluster. There are no conditions or dependencies that alter this requirement, making it a fundamental part of the cluster's functionality.

1.3.7.1. AddGroup Command
The AddGroup command allows a client to add group membership in a particular group for the
server endpoint.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the 'GroupID' command. This command has an identifier of '0' and is of the type 'group-id', with a constraint that specifies a minimum value of 1. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the "GroupName" command, which is of type "string" and has a constraint of a maximum length of 16 characters. The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "GroupName" command is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

1.3.7.1.1. GroupID Field
This field SHALL be used to identify the group and any associated key material to which the server
endpoint is to be added.
1.3.7.1.2. GroupName Field
This field MAY be set to a human-readable name for the group. If the client has no name for the
group, the GroupName field SHALL be set to the empty string.
Support of group names is optional and is indicated by the FeatureMap and NameSupport attribute.
1.3.7.1.3. Effect on Receipt
If the server does not support group names, the GroupName field SHALL be ignored.
On receipt of the AddGroup command, the server SHALL perform the following procedure:
1. If the command fields are not within constraints, the status SHALL be CONSTRAINT_ERROR, and
the server continues from step 6.
2. If the receiving node requires security material to support the group ID and that material does
not exist for this group ID, the status SHALL be UNSUPPORTED_ACCESS and the server contin
ues from step 6.
3. If the server endpoint is a member of the group indicated by the GroupID, the group name
SHALL be updated (if supported) to GroupName, the status SHALL be SUCCESS, and the server
continues from step 6.
4. If there are no available resources to add the membership for the server endpoint, the status
SHALL be RESOURCE_EXHAUSTED, and the server continues from step 6.
5. The server SHALL add the server endpoint as a member of the group indicated by the GroupID,
the group name SHALL be updated (if supported) to GroupName, and the status SHALL be SUC
CESS.
a. If the GroupID had already been added to the Group Table because of a previous AddGroup
or AddGroupIfIdentifying command and a GroupName is provided and the server supports
GroupName storage, then the GroupName associated with the GroupID in the Group Table
SHALL be updated to reflect the new GroupName provided for the Group, such that subse
quent ViewGroup commands yield the same name for all endpoints which have a group
association to the given GroupID.
6. If  the  AddGroup  command  was  received  as  a  unicast,  the  server  SHALL  generate  an
AddGroupResponse command with the Status field set to the evaluated status. If the AddGroup
command was received as a groupcast, the server SHALL NOT generate an AddGroupResponse
command.
See AddGroupResponse for a description of the response command.
1.3.7.2. ViewGroup Command
The ViewGroup command allows a client to request that the server responds with a ViewGroupRe
sponse command containing the name string for a particular group.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the 'GroupID' command, which has an ID of '0' and is of the type 'group-id' with a constraint that requires a minimum value of 1. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

1.3.7.2.1. Effect on Receipt
On receipt of the ViewGroup command, the server SHALL perform the following procedure:
1. If the command fields are not within constraints, the status SHALL be CONSTRAINT_ERROR and
the server continues from step 4.
2. If the server endpoint is a member of the group indicated by the GroupID, the status SHALL be
SUCCESS, and the server continues from step 4.
3. Else the status SHALL be NOT_FOUND.
4. If the ViewGroup command was received as a unicast, the server SHALL generate a View
GroupResponse command for the group, and the Status field set to the evaluated status. If the
ViewGroup command was received as a groupcast, the server SHALL NOT generate a View
GroupResponse command.
See ViewGroupResponse for a description of the response command.
1.3.7.3. GetGroupMembership Command
The GetGroupMembership command allows a client to inquire about the group membership of the
server endpoint, in a number of ways.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the 'GroupList' command. This command is identified by the ID '0' and is of the type 'list[group-id]', which indicates it involves a list of group IDs. The constraint 'all[min 1]' suggests that the list must contain at least one group ID. The conformance rule 'M' signifies that the 'GroupList' command is mandatory, meaning it is always required to be implemented in any device or application that supports the Groups Cluster according to the Matter specification. There are no conditions or exceptions to this requirement, making it an essential component of the Groups Cluster functionality.

1.3.7.3.1. Effect on Receipt
On receipt of the GetGroupMembership command, the server SHALL respond with group member
ship information using the GetGroupMembershipResponse command as follows:
If the GroupList field is empty, the server SHALL respond with all group IDs indicating the groups
of which the server endpoint is a member.
If the GroupList field contains at least one group ID indicating a group of which the server endpoint
is a member, the server SHALL respond with each group ID indicating a group of which the server
endpoint is a member that matches a group in the GroupList field.
If the GroupList field contains one or more group IDs but does not contain any group ID indicating
a group of which the server endpoint is a member, the server SHALL only respond if the command
is unicast. The response SHALL return with an empty GroupList field.
1.3.7.4. RemoveGroup Command
The RemoveGroup command allows a client to request that the server removes the membership for
the server endpoint, if any, in a particular group.

_Table parsed from section 'Commands':_

* In the context of the Groups Cluster, under the Commands section, the table row describes an element with the ID '0' named 'GroupID', which is of type 'group-id' and has a constraint of 'minimum 1'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'GroupID' element is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions. The constraint 'min 1' indicates that the value for 'GroupID' must be at least 1, ensuring that it is a valid and usable identifier within the cluster's operations.

1.3.7.4.1. Effect on Receipt
On receipt of the RemoveGroup command, the server SHALL perform the following procedure:
1. If the command fields are not within constraints, the status SHALL be CONSTRAINT_ERROR and
the server continues from step 4.
2. If the server endpoint is a member of the group indicated by the GroupID, the server SHALL
remove the server endpoint membership in the group, the status SHALL be SUCCESS, and the
server continues from step 4.
3. Else the status SHALL be NOT_FOUND.
4. If the RemoveGroup command was received as a unicast, the server SHALL generate a Remove
GroupResponse command with the Status field set to the evaluated status. If the RemoveGroup
command was received as a groupcast, the server SHALL NOT generate a RemoveGroupRe
sponse command.
See RemoveGroupResponse for a description of the response command.
Additionally, if the Scenes Management cluster is supported on the same endpoint, scenes associ
ated with the indicated group SHALL be removed on that endpoint.
1.3.7.5. RemoveAllGroups Command
The RemoveAllGroups command allows a client to direct the server to remove all group associa
tions for the server endpoint.
1.3.7.5.1. Effect on Receipt
On receipt of this command, the server SHALL remove all group memberships for the server end
point from the Group Table. If the RemoveAllGroups command was received as unicast and a
response is not suppressed, the server SHALL generate a response with the Status field set to SUC
CESS.
Additionally, if the Scenes Management cluster is supported on the same endpoint, all scenes,
except for scenes associated with group ID 0, SHALL be removed on that endpoint.
1.3.7.6. AddGroupIfIdentifying Command
The AddGroupIfIdentifying command allows a client to add group membership in a particular
group for the server endpoint, on condition that the endpoint is identifying itself. Identifying func
tionality is controlled using the Identify cluster, (see Identify Cluster).
For correct operation of the AddGroupIfIdentifying command, any endpoint that supports the
Groups server cluster SHALL also support the Identify server cluster.
This command might be used to assist configuring group membership in the absence of a commis
sioning tool.

_Table parsed from section 'Commands':_

* The table row describes an element within the Groups Cluster, specifically in the context of Commands. The element is identified by the ID '0' and is named 'GroupID'. It is of the type 'group-id' and has a constraint that specifies a minimum value of 1. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'GroupID' element is always required in the implementation of the Groups Cluster commands, without any conditions or exceptions.

* The table row describes an element within the "Groups Cluster" under the "Commands" section, specifically an attribute or command named "GroupName" with an ID of '1'. This element is of type 'string' and has a constraint that limits its maximum length to 16 characters. The conformance rule for "GroupName" is marked as 'M', which stands for Mandatory. This means that the "GroupName" element is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

1.3.7.6.1. GroupID Field
This field SHALL be used to identify the group and any associated key material to which the server
endpoint is to be added.
1.3.7.6.2. GroupName Field
This field MAY be set to a human-readable name for the group. If the client has no name for the
group, the GroupName field SHALL be set to the empty string.
Support of group names is optional and is indicated by the FeatureMap and NameSupport attribute.
1.3.7.6.3. Effect on Receipt
If the server does not support group names, the GroupName field SHALL be ignored.
On receipt of the AddGroupIfIdentifying command, the server SHALL perform the following proce
dure:
1. The server verifies that it is currently identifying itself. If the server it not currently identifying
itself, the status SHALL be SUCCESS, and the server continues from step 7.
2. If the command fields are not within constraints, the status SHALL be CONSTRAINT_ERROR and
the server continues from step 7.
3. If the receiving node requires security material to support the group ID, and that material does
not exist for this group ID, the status SHALL be UNSUPPORTED_ACCESS and the server contin
ues from step 7.
4. If the server endpoint is a member of the group indicated by the GroupID, the status SHALL be
SUCCESS and the server continues from step 7.
5. If there are no available resources to add the membership for the server endpoint, the status
SHALL be RESOURCE_EXHAUSTED and the server continues from step 7.
6. The server SHALL add the server endpoint as a member of the group indicated by the GroupID,
the group name SHALL be updated (if supported) to GroupName, and the status SHALL be SUC
CESS.
a. If the GroupID had already been added to the Group Table because of a previous AddGroup
or AddGroupIfIdentifying command and a GroupName is provided and the server supports
GroupName storage, then the GroupName associated with the GroupID in the Group Table
SHALL be updated to reflect the new GroupName provided for the Group, such that subse
quent ViewGroup commands yield the same name for all endpoints which have a group
association to the given GroupID.
7. If the AddGroupIfIdentifying command was received as unicast and the evaluated status is not
SUCCESS, or if the AddGroupIfIdentifying command was received as unicast and the evaluated
status is SUCCESS and a response is not suppressed, the server SHALL generate a response with
the Status field set to the evaluated status.
1.3.7.7. AddGroupResponse Command
The AddGroupResponse is sent by the Groups cluster server in response to an AddGroup command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the "Status" command, which is of type `enum8`. The constraint for this command is described elsewhere in the documentation, as indicated by "desc". The conformance rule for this command is marked as "M", meaning that the "Status" command is mandatory. This implies that any implementation of the Groups Cluster must include this command, as it is always required according to the Matter specification.

* The table row describes an element within the Groups Cluster, specifically under the Commands section, with the ID '1' and the name 'GroupID'. This element is of the type 'group-id' and has a constraint that requires a minimum value of 1. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'GroupID' element is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

1.3.7.7.1. Status Field
This field is set according to the Effect on Receipt section of the AddGroup command.
1.3.7.7.2. GroupID Field
This field is set to the GroupID field of the received AddGroup command.
1.3.7.8. ViewGroupResponse Command
The ViewGroupResponse command is sent by the Groups cluster server in response to a ViewGroup
command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the "Status" command, which is of type `enum8`. The constraint for this command is described elsewhere in the documentation, as indicated by "desc". The conformance rule for this command is marked as "M", which stands for Mandatory. This means that the "Status" command is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

* The table row describes a command within the Groups Cluster, specifically the 'GroupID' command. This command is identified by the ID '1' and is of the type 'group-id', with a constraint that specifies a minimum value of 1. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Groups Cluster, with no conditions or exceptions. The mandatory status ensures that this command is consistently available across all implementations of the Groups Cluster.

* In the context of the Groups Cluster, within the Commands section, the table row describes an element with the ID '2' named 'GroupName'. This element is of the type 'string' and has a constraint that limits its maximum length to 16 characters. The conformance rule for 'GroupName' is denoted by 'M', which stands for Mandatory. This means that the 'GroupName' element is always required to be implemented according to the Matter specification, with no conditions or exceptions.

1.3.7.8.1. Status Field
This field is according to the Effect on Receipt section of the ViewGroup command.
1.3.7.8.2. GroupID Field
This field is set to the GroupID field of the received ViewGroup command.
1.3.7.8.3. GroupName Field
If the status is SUCCESS, and group names are supported, this field is set to the group name associ
ated with that group in the Group Table; otherwise it is set to the empty string.
1.3.7.9. GetGroupMembershipResponse Command
The GetGroupMembershipResponse command is sent by the Groups cluster server in response to a
GetGroupMembership command.
The GetGroupMembershipResponse command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* In the context of the Groups Cluster under the Commands section, the table row describes an element with the ID '0' named 'Capacity', which is of type 'uint8' and has a constraint labeled as 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', which means that the 'Capacity' command is mandatory and always required within the Groups Cluster. This implies that any implementation of the Groups Cluster must include the 'Capacity' command as a necessary component, without any conditional dependencies or exceptions.

* The table row describes an entry within the "Groups Cluster" under the "Commands" section, specifically for the command identified as "GroupList." This command is of the type "list[group-id]" and has a constraint indicating that it must include at least one item ("all[min 1]"). The conformance rule for this entry is marked as "M," which means that the "GroupList" command is mandatory. This implies that any implementation of the Groups Cluster must include this command without exception, ensuring that it is always present and functional in compliant devices.

1.3.7.9.1. Capacity Field
This field SHALL contain the remaining capacity of the Group Table of the node. The following val
ues apply:
• 0 - No further groups MAY be added.
• 0 < Capacity < 0xFE - Capacity holds the number of groups that MAY be added.
• 0xFE - At least 1 further group MAY be added (exact number is unknown).
• null - It is unknown if any further groups MAY be added.
1.3.7.9.2. GroupList Field
The GroupList field SHALL contain either the group IDs of all the groups in the Group Table for
which the server endpoint is a member of the group (in the case where the GroupList field of the
received GetGroupMembership command was empty), or the group IDs of all the groups in the
Group Table for which the server endpoint is a member of the group and for which the group ID
was included in the the GroupList field of the received GetGroupMembership command (in the case
where the GroupList field of the received GetGroupMembership command was not empty).
Zigbee: If the total number of groups will cause the maximum payload length of a frame to be
exceeded, then the GroupList field SHALL contain only as many groups as will fit.
1.3.7.10. RemoveGroupResponse Command
The RemoveGroupResponse command is generated by the server in response to the receipt of a
RemoveGroup command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Groups Cluster, specifically the "Status" command, which is identified by the ID '0' and has a data type of 'enum8'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this command are described in detail elsewhere in the documentation. The 'Conformance' field is marked with an 'M', which signifies that the "Status" command is mandatory. This means that any implementation of the Groups Cluster must include this command as a required element, with no conditions or exceptions.

* The table row describes an element within the Groups Cluster, specifically under the Commands section. The element is identified by the ID '1' and is named 'GroupID'. It is of the type 'group-id' and has a constraint specifying a minimum value of 1. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'GroupID' element is always required to be implemented in any device or application that supports the Groups Cluster, without any conditions or exceptions.

1.3.7.10.1. Status Field
This field is according to the Effect on Receipt section of the RemoveGroup command.
1.3.7.10.2. GroupID Field
This field is set to the GroupID field of the received RemoveGroup command.