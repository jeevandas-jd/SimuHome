
# 10.4 Thread Network Directory Cluster

This cluster stores a list of Thread networks (including the credentials required to access each net
work), as well as a designation of the user’s preferred network, to facilitate the sharing of Thread
networks across fabrics.

## Data Types
10.4.4.1. ThreadNetworkStruct Type
Represents the data associated with a Thread Network.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Thread Network Directory Cluster, specifically under the Data Types section. The entry is for an element named "ExtendedPanID," which is of type "octstr" (octet string) and has a constraint of 8, indicating it is expected to be 8 octets in length. The conformance for this element is marked as "M," meaning that the ExtendedPanID is a mandatory element. This implies that it is always required to be implemented and supported within the Thread Network Directory Cluster, with no conditions or exceptions.

* In the Thread Network Directory Cluster, under the Data Types section, the entry for 'NetworkName' is identified by the ID '1' and is of the type 'string'. It has a constraint that limits its length to between 1 and 16 characters. The conformance rule for 'NetworkName' is marked as 'M', which means it is a mandatory element. This indicates that the 'NetworkName' must always be included and supported within any implementation of the Thread Network Directory Cluster, without any conditions or exceptions.

* In the context of the Thread Network Directory Cluster, specifically within the Data Types section, the table row describes an element with the ID '2', named 'Channel'. This element is of the type 'uint16', indicating it is a 16-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Channel' element is always required to be implemented in any device or application that supports the Thread Network Directory Cluster, without any conditions or exceptions.

* The table row describes an entry within the Thread Network Directory Cluster, specifically under the Data Types section. The entry is for an element named 'ActiveTimestamp', which is of type 'uint64' and has a constraint labeled as 'all'. The conformance rule for 'ActiveTimestamp' is marked as 'M', indicating that this element is mandatory. This means that the 'ActiveTimestamp' must always be included and supported in any implementation of the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.4.1.1. ExtendedPanID Field
This field SHALL indicate the Extended PAN ID from the OperationalDataset for the given Thread
network.
10.4.4.1.2. NetworkName Field
This field SHALL indicate the Network Name from the OperationalDataset for the given Thread net
work.
10.4.4.1.3. Channel Field
This field SHALL indicate the Channel from the OperationalDataset for the given Thread network.
10.4.4.1.4. ActiveTimestamp Field
This field SHALL indicate the Active Timestamp from the OperationalDataset for the given Thread
network.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "PreferredExtendedPanID" within the Thread Network Directory Cluster, identified by the ID '0x0000'. This attribute is of type 'octstr' with a constraint of 8, meaning it is expected to be an octet string of length 8. The 'Quality' field marked as 'XN' indicates that this attribute is explicitly disallowed in certain contexts, though the specifics are not detailed here. The default value for this attribute is 'null', and it has 'RW VM' access, meaning it can be read and written, and is subject to certain access restrictions or conditions (VM typically stands for Viewable and Modifiable). The 'Conformance' field is marked as 'M', which means that this attribute is mandatory and must always be implemented in devices supporting this cluster, without any conditional dependencies or exceptions.

* In the context of the Thread Network Directory Cluster, the attribute with ID '0x0001' is named 'ThreadNetworks' and is of type 'list[Thread NetworkStruct]'. This attribute is constrained by the maximum size defined by 'ThreadNetworkTableSize'. It is marked with a quality of 'N', indicating it is a non-volatile attribute, and has an access level of 'R V', meaning it is readable and can be viewed. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the 'ThreadNetworks' attribute must always be implemented and supported in any device or application that uses the Thread Network Directory Cluster, without any conditional exceptions.

* The table row describes an attribute within the Thread Network Directory Cluster, specifically the "ThreadNetworkTableSize" attribute. This attribute has an ID of '0x0002' and is of type 'uint8', which means it is an 8-bit unsigned integer. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. It has a quality of 'F', a default value of 10, and access permissions of 'R V', meaning it can be read and viewed. The conformance rule for this attribute is 'M', indicating that it is mandatory. This means that the "ThreadNetworkTableSize" attribute must always be implemented and supported in any device or application that uses the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.5.1. PreferredExtendedPanID Attribute
This attribute SHALL represent the Thread Extended PAN ID value for the Thread network desig
nated by the user to be their preferred network for commissioning of Thread devices. If not null,
the value of this attribute SHALL match the ExtendedPanID of a network in the ThreadNetworks
attribute. A write operation with a non-null value that does not match any network in the Thread
Networks list SHALL be rejected with a status of CONSTRAINT_ERROR.
The purpose of designating one Thread network as preferred is to help a commissioner to select a
Thread network when a Thread device is within suitable range of more than one Thread network
which appears in the ThreadNetworks list. A value of null indicates that there is no current pre
ferred network: All networks MAY be treated as equally preferred by a commissioner with access to
this cluster.
This attribute MAY be automatically set to the ExtendedPanID of the first Thread network added to
the ThreadNetworks list.
A client SHALL obtain user consent before changing the value of this attribute from a non-null
value.
On a factory reset this attribute SHALL be reset to null.
10.4.5.2. ThreadNetworks Attribute
This attribute SHALL indicate the list of Thread Networks known about by this cluster. If the node
hosting this cluster includes a Thread Border Router, then an entry for its Thread Network SHALL
be included in this list.
The list can be modified via the AddNetwork and RemoveNetwork commands.
For each entry in the list, the cluster server also stores a Thread Operational Dataset. Clients use the
GetOperationalDataset command to obtain the Operational Dataset for an entry in this list.
On a factory reset this list SHALL be cleared, and any Thread Operational datasets previously
stored SHALL be removed from the Node.
10.4.5.3. ThreadNetworkTableSize Attribute
This attribute SHALL indicate the maximum number of entries that can be held in the ThreadNet
works list; it SHALL be at least 2 times the number of SupportedFabrics advertised in the Opera
tional Credentials Cluster on the root endpoint of this node.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Network Directory Cluster, specifically the "AddNetwork" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'). The access level for this command is marked as 'M T', indicating it is mandatory and requires certain access privileges. The conformance rule for this command is 'M', meaning it is mandatory and must always be implemented in any device or application that supports this cluster. There are no conditions or exceptions to this requirement, making the "AddNetwork" command a fundamental part of the Thread Network Directory Cluster's functionality.

* The table row describes a command within the Thread Network Directory Cluster, specifically the "RemoveNetwork" command, which is directed from the client to the server. The command has an ID of '0x01' and requires a response ('Y'), indicating that the server must acknowledge the command upon receipt. The access level is marked as 'M T', suggesting that specific access controls or roles are mandatory for this command. The conformance rule for this command is 'M', meaning that the "RemoveNetwork" command is mandatory and must always be implemented in any device or application that supports this cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Network Directory Cluster, specifically the "GetOperationalDataset" command. This command is directed from the client to the server and expects a response in the form of an "OperationalDatasetResponse." The access level for this command is marked as "Mandatory" (M), indicating that it is always required to be implemented. The conformance rule for this command is also "Mandatory" (M), meaning that regardless of any conditions or features, the "GetOperationalDataset" command must be supported and implemented in all devices that include the Thread Network Directory Cluster. There are no conditional or optional scenarios for this command; it is a fundamental requirement.

* The table row describes a command within the Thread Network Directory Cluster, specifically the "OperationalDatasetResponse" command, which is identified by the ID '0x03'. This command is directed from the server to the client and does not expect a response ('Response': 'N'). The conformance rule for this command is 'M', indicating that it is mandatory. This means that the "OperationalDatasetResponse" command must always be implemented and supported in any device or application that uses the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.6.1. AddNetwork Command
Adds an entry to the ThreadNetworks attribute with the specified Thread Operational Dataset.
If there is an existing entry with the Extended PAN ID then the Thread Operational Dataset for that
entry is replaced. As a result, changes to the network parameters (e.g. Channel, Network Name,
PSKc, …) of an existing entry with a given Extended PAN ID can be made using this command.

_Table parsed from section 'Commands':_

* The table row entry pertains to the "OperationalDataset" command within the Thread Network Directory Cluster. This command is identified by the ID '0' and is of the type 'octstr', with a constraint that limits its size to a maximum of 254 bytes. The conformance rule for this command is denoted by 'M', indicating that it is mandatory. This means that the "OperationalDataset" command is always required to be implemented in any device or application that supports the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.6.1.1. OperationalDataset Field
This field SHALL represent the Operational Dataset for the network, using the encoding defined in
the Thread specification. It SHALL contain at least the following sub-TLVs: Active Timestamp, Chan
nel, Channel Mask, Extended PAN ID, Network Key, Network Mesh-Local Prefix, Network Name,
PAN ID, PSKc, and Security Policy.
10.4.6.1.2. Effect on Receipt
1. If the TLV structure of the Operational Dataset is invalid, or if any of the required sub-TLVs are
missing, the command SHALL be rejected with a status of CONSTRAINT_ERROR. However, inclu
sion of unknown sub-TLVs SHALL NOT be treated as an error, as future versions of the Thread
specification MAY define additional sub-TLVs.
2. If there is an existing ThreadNetworks entry with an Extended PAN ID matching the received
dataset, then that entry SHALL be replaced with the received dataset. However, if the received
dataset has an Active Timestamp that is less than or equal to that of the existing entry, then the
update SHALL be rejected with a status of INVALID_IN_STATE.
3. Otherwise, a new entry SHALL be added based on the received dataset. If this would cause the
size of the ThreadNetworks list to exceed the ThreadNetworkTableSize, then a RESOURCE_EX
HAUSTED status SHALL be returned.
10.4.6.2. RemoveNetwork Command
Removes the network with the given Extended PAN ID from the ThreadNetworks attribute.

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Network Directory Cluster, specifically the "ExtendedPanID" command. This command has an ID of '0' and is of the type 'octstr', with a constraint indicating it must be 8 bytes in length. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the "ExtendedPanID" command is always required to be implemented in any device or application that supports the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.6.2.1. Effect on Receipt
1. If no network with the given Extended PAN ID exists in the ThreadNetworks attribute, the com
mand SHALL be rejected with a status of NOT_FOUND.
2. If the given Extended PAN ID matches the PreferredExtendedPanID attribute, the command
SHALL be rejected with a status of CONSTRAINT_ERROR.
3. Otherwise, the network with the matching Extended PAN ID SHALL be removed from the
ThreadNetworks attribute.
10.4.6.3. GetOperationalDataset Command
Retrieves the Thread Operational Dataset with the given Extended PAN ID.

_Table parsed from section 'Commands':_

* The table row describes a command within the Thread Network Directory Cluster, specifically the 'ExtendedPanID' command. This command has an ID of '0' and is of type 'octstr', with a constraint indicating it must be 8 bytes in length. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the 'ExtendedPanID' command is always required to be implemented in any device or application that supports the Thread Network Directory Cluster, without any conditions or exceptions.

10.4.6.3.1. Effect on Receipt
1. If the command is not executed via a CASE session, the command SHALL be rejected with a sta
tus of UNSUPPORTED_ACCESS.
2. If no network with the given Extended PAN ID exists in the ThreadNetworks attribute, the com
mand SHALL be rejected with a status of NOT_FOUND.
3. Otherwise, an OperationalDatasetResponse command containing the operational dataset for the
requested network SHALL be generated.
10.4.6.4. OperationalDatasetResponse Command
Contains the Thread Operational Dataset for the Extended PAN specified in GetOperationalDataset.

_Table parsed from section 'Commands':_

* The table row entry pertains to the "OperationalDataset" command within the Thread Network Directory Cluster. This command is identified by the ID '0' and is of the type 'octstr', with a constraint limiting its maximum size to 254. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "OperationalDataset" command is always required to be implemented in any device or application that supports the Thread Network Directory Cluster, with no conditions or exceptions.

## Guidance for Fabrics / Commissioners
This cluster allows fabrics (via their Administrators or Nodes with Manage privilege) to collabora
tively share and manage a directory of ThreadNetworks, as well as a designation of one of those
networks as the user’s preferred network via the PreferredExtendedPanID attribute.
It is RECOMMENDED that fabrics only interact with instances of this cluster hosted on endpoints
that declare a device type that explicitly allows this cluster; currently this includes the Network
Infrastructure Manager and Thread Border Router device types. Networks from the ThreadNet
works list of any such directory instance, as well as the Active Dataset made available by any
Thread Border Router via the Thread Border Router Management Cluster, SHOULD be considered
as potentially available networks.
In determining the user’s preferred network, a directory instance on a Network Infrastructure
Manager device SHOULD take precedence over other instances. Where a fabric has access to multi
ple Network Infrastructure Manager devices, it MAY give precedence to the directory instance on
the Network Infrastructure Manager device considered to be acting as the primary Internet gate
way device for the network.
Due to the sensitive nature of Thread network credentials, it is RECOMMENDED that fabrics obtain
user consent before starting to contribute credentials to a particular directory instance. Contribu
tions to a directory instance SHOULD be restricted to those Thread networks that are likely to be
reachable from the infrastructure network to which the device hosting that directory is connected.