
# 1.4 Scenes Management Cluster

The Scenes Management cluster provides attributes and commands for setting up and recalling
scenes. Each scene corresponds to a set of stored values of specified attributes for one or more clus
ters on the same end point as the Scenes Management cluster.
In most cases scenes are associated with a particular group identifier. Scenes MAY also exist with
out a group, in which case the value 0 replaces the group identifier. Note that extra care is required
in these cases to avoid a scene identifier collision, and that commands related to scenes without a
group MAY only be unicast, i.e., they SHALL NOT be multicast or broadcast.
NOTE Support for Scenes Management cluster is provisional.

## Dependencies
Any endpoint that implements the Scenes Management server cluster SHALL also implement the
Groups server cluster.
Note that the RemoveGroup command and the RemoveAllGroups command of the Groups cluster
also remove scenes.

## Handling of fabric-scoping
Attributes and commands for this cluster are scoped to the accessing fabric and SHALL only affect
or reflect data related to the accessing fabric, with the exception of the SceneValid Field of the Fab
ricSceneInfo attribute.
The following constraints apply in addition to any other stated requirements in individual data
model elements:
• Any attribute read, attribute write or command invoked on the server when no accessing fabric
is available SHALL fail with a status code of UNSUPPORTED_ACCESS returned to the client.
• When accessing scene information, implementations SHALL ensure that scenes with identical
Group ID and Scene ID across fabrics will only access the data for the accessing fabric, so that
the same identifier values used by different accessing fabrics do not cause mixing or overwrit
ing of another fabric’s scenes.
• Upon leaving a fabric with the RemoveFabric command of the Operational Credentials Cluster,
all scenes data for the associated fabric SHALL be removed from the Scene Table.
• The Scene Table capacity for a given fabric SHALL be less than half (rounded down towards 0)
of the Scene Table entries (as indicated in the SceneTableSize attribute), with a maximum of 253
entries (to allow expressing it in the GetSceneMembershipResponse command). If the Scene Ta
ble capacity is about to be exceeded by adding or storing a scene, then the resource exhaustion
behavior of the associated command SHALL apply.

## Data Types
1.4.7.1. CopyModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Scenes Management Cluster, under the Data Types section, the entry for 'Bit' 0 is named 'CopyAllScenes' and is summarized as the capability to copy all scenes in the scene table. The conformance rule for this entry is not explicitly provided in the table row data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which the 'CopyAllScenes' feature is required, optional, provisional, deprecated, or disallowed. Without a specific conformance string, we assume that the feature's inclusion is determined by the broader context of the specification or described elsewhere in the documentation. Thus, the 'CopyAllScenes' feature's implementation depends on the specific requirements and conditions outlined in the full Matter specification for the Scenes Management Cluster.

1.4.7.2. SceneInfoStruct Type

_Table parsed from section 'Data Types':_

* The table row pertains to the "Scenes Management Cluster" within the "Data Types" section, focusing on an element identified as 'Access Qua'. This element is associated with the 'ID', 'lity: Fabric', 'Name', and 'Scoped' attributes. The conformance rule for this element is not explicitly provided in the data snippet, but based on the context, it would typically specify whether the element is mandatory, optional, provisional, deprecated, or disallowed. If a conformance expression were included, it would determine the conditions under which the element is required or optional, using logical operators and feature codes. Without the specific conformance string, we cannot definitively interpret its requirement status, but it would generally guide implementers on how to handle this element within the Scenes Management Cluster.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section. It describes a data type with the label "SceneCount," which is scoped as a `uint8` (an unsigned 8-bit integer). The conformance rule for this entry is indicated by the string '0', which does not directly match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. This suggests that the conformance for this data type might be described elsewhere in the documentation or could be a placeholder for a more detailed explanation. Therefore, the specific requirements or optionality of this data type within the Scenes Management Cluster are not explicitly defined in this row and would need to be referenced from additional documentation for clarity.

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on the attribute labeled "CurrentScene." This attribute is of the data type `uint8`, indicating it is an unsigned 8-bit integer. The conformance rule for this attribute is expressed as 'Access Qua': '1', 'lity: Fabric': 'CurrentScene', 'Scoped': 'uint8'. This suggests that the attribute is mandatory within the context of the Scenes Management Cluster, meaning it must always be implemented and supported by any device or application that utilizes this cluster. The conformance does not specify any conditional logic or optionality, reinforcing its mandatory status across all implementations.

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on an element with the label 'Access Qua'. The conformance rule for this element is not explicitly provided in the row data, but based on the context and the Matter Conformance Interpretation Guide, we can infer its significance. The 'Access Qua' likely refers to an access quality or qualifier related to the management of scenes, with a specific focus on the 'Fabric' and 'Scoped' attributes. The 'Fabric' is set to 'CurrentGroup', indicating that the element is relevant to the current group context within a fabric, and 'Scoped' is associated with 'group-id', suggesting that the element's applicability or behavior is determined by its association with a specific group identifier. Without a direct conformance string, we assume the element's inclusion or behavior is contextually defined by its association with these attributes, potentially implying a conditional or described conformance that would be detailed elsewhere in the documentation

* The table row pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically describing an element related to "Access Quality: Fabric" with a type of "SceneValid" and a scope of "bool." The conformance rule for this element is not explicitly provided in the data given, but if we assume a typical conformance string might be associated, it would dictate the conditions under which this element is required, optional, or otherwise. For instance, if the conformance were "M," it would mean this element is always mandatory. If it were "O," it would be optional. Without a specific conformance string provided, we cannot definitively interpret the requirement status of this element. However, understanding the conformance rules allows us to determine how such an element would be treated based on the presence or absence of certain features or conditions in a Matter implementation.

* The table row entry pertains to the Scenes Management Cluster within the Data Types section, specifically describing an attribute or element labeled 'RemainingCapacity' with a data type of 'uint8'. The 'Access Qua' value of '4' likely indicates a specific access level or permissions associated with this attribute, although the exact meaning is not detailed here. The 'Conformance' field is not explicitly provided in the row data, but if we were to interpret a typical conformance expression, it would dictate when this attribute is required or optional based on certain conditions or feature support. For example, if the conformance were 'M', it would mean 'RemainingCapacity' is always mandatory. If it were 'AB, O', it would mean 'RemainingCapacity' is mandatory if feature 'AB' is supported, otherwise optional. Since the conformance is not specified, we cannot determine the exact requirement status without additional context.

1.4.7.2.1. SceneCount Field
This field SHALL indicate the number of scenes currently used in the server’s Scene Table on the
endpoint where the Scenes Management cluster appears.
This only includes the count for the associated fabric.
1.4.7.2.2. CurrentScene Field
This field SHALL indicate the scene identifier of the scene last invoked on the associated fabric. If
no scene has been invoked, the value of this field SHALL be 0xFF, the undefined scene identifier.
1.4.7.2.3. CurrentGroup Field
This field SHALL indicate the group identifier of the scene last invoked on the associated fabric, or 0
if the scene last invoked is not associated with a group.
1.4.7.2.4. SceneValid Field
This field SHALL indicate whether the state of the server corresponds to that associated with the
CurrentScene and CurrentGroup fields of the SceneInfoStruct they belong to. TRUE indicates that
these fields are valid, FALSE indicates that they are not valid.
This field SHALL be set to False for all other fabrics when an attribute with the Scenes ("S") designa
tion in the Quality column of another cluster present on the same endpoint is modified or when the
current scene is modified by a fabric through the RecallScene or StoreScene commands, regardless
of the fabric-scoped access quality of the command.
In the event where the SceneValid field is set to False for a fabric, the CurrentScene and Current
Group fields SHALL be the last invoked scene and group for that fabric. In the event where no
scene was previously invoked for that fabric, the CurrentScene and CurrentGroup fields SHALL be
their default values.
1.4.7.2.5. RemainingCapacity Field
This field SHALL indicate the remaining capacity of the Scene Table on this endpoint for the access
ing fabric. Note that this value may change between reads, even if no entries are added or deleted
on the accessing fabric, due to other clients associated with other fabrics adding or deleting entries
that impact the resource usage on the device.
1.4.7.3. AttributeValuePairStruct Type
This data type indicates a combination of an identifier and the value of an attribute.

_Table parsed from section 'Data Types':_

* In the Scenes Management Cluster, under the Data Types section, the table row describes an element with the ID '0' named 'AttributeID', which is of the type 'attribute-id' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'AttributeID' is a required element in the Scenes Management Cluster and must always be implemented, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Data Types section, the entry with ID '1' and Name 'ValueUnsigned8' is of type 'uint8'. The conformance rule for this entry is 'O.a', which indicates that the 'ValueUnsigned8' data type is optional. The 'O' tag signifies that this element is not required and has no dependencies, meaning it can be included or omitted based on the implementation's needs or preferences without affecting compliance with the Matter specification. The '.a' suffix does not alter the basic optional nature of this conformance.

* In the Scenes Management Cluster, under the Data Types section, the table row with ID '2' refers to an element named 'ValueSigned8', which is of type 'int8'. The conformance rule for this element is 'O.a', indicating that 'ValueSigned8' is optional. This means that its inclusion is not required and it has no dependencies on other features or conditions. The 'O.a' notation suggests that the optional status might be further elaborated or specified in a different part of the documentation, but based on the provided conformance guide, it is simply optional without additional conditions.

* The table row describes an element within the Scenes Management Cluster, specifically a data type named "ValueUnsigned16" with an ID of '3' and a type of 'uint16'. The conformance rule for this element is 'O.a', indicating that it is optional. This means that the "ValueUnsigned16" data type is not required to be implemented and has no dependencies or conditions that would make it mandatory. It can be included at the discretion of the implementer, without any further obligations or restrictions as per the current Matter specification.

* In the Scenes Management Cluster, within the Data Types section, the entry with ID '4' is named 'ValueSigned16' and is of type 'int16'. The conformance rule for this entry is 'O.a', which indicates that the 'ValueSigned16' data type is optional. This means that its inclusion is not required and it has no dependencies on other features or conditions. The 'O.a' notation suggests that there might be additional context or a specific condition described elsewhere in the documentation that further clarifies its optional status. However, based on the information provided, 'ValueSigned16' is simply an optional element within this cluster.

* In the Scenes Management Cluster, under the Data Types section, the entry with ID '5' is named 'ValueUnsigned32' and is of type 'uint32'. The conformance rule for this entry is 'O.a', which indicates that the 'ValueUnsigned32' data type is optional. The 'O' tag signifies that this element is not required and does not have any dependencies, meaning it can be included at the discretion of the implementer without any mandatory conditions or complex dependencies.

* In the Scenes Management Cluster, under the Data Types section, the entry with ID '6' is named 'ValueSigned32' and is of type 'int32'. The conformance rule for this entry is 'O.a', indicating that 'ValueSigned32' is an optional element. This means that its inclusion is not required and it has no dependencies on other features or conditions. The 'O' tag signifies that implementers have the discretion to include or exclude this data type based on their specific needs or preferences, without any further conditions or future changes implied.

* In the context of the Scenes Management Cluster, the data type entry with ID '7' and name 'ValueUnsigned64' is of type 'uint64'. According to the conformance rule 'O.a', this element is classified as Optional. The 'O' indicates that the 'ValueUnsigned64' data type is not required and has no dependencies within the current specification. The '.a' suffix does not alter the basic interpretation of the 'O' tag, suggesting that any additional context or conditions related to this optional status are likely described elsewhere in the documentation. Therefore, this data type can be included at the implementer's discretion without any mandatory requirements.

* In the Scenes Management Cluster, under the Data Types section, the entry with ID '8' refers to a data type named 'ValueSigned64', which is of type 'int64'. The conformance rule for this entry is 'O.a', indicating that the 'ValueSigned64' data type is optional. This means that its inclusion is not required and it does not depend on any specific conditions or features being supported. As an optional element, it can be implemented at the discretion of the developer or manufacturer without any mandatory obligation.

1.4.7.3.1. AttributeID Field
This field SHALL be present for all instances in a given ExtensionFieldSetStruct.
Which Value* field is used SHALL be determined based on the data type of the attribute indicated
by AttributeID, as described in the Value* Fields subsection.
The AttributeID field SHALL NOT refer to an attribute without the Scenes ("S") designation in the
Quality column of the cluster specification.
1.4.7.3.2. ValueUnsigned8, ValueSigned8, ValueUnsigned16, ValueSigned16, ValueUnsigned32, ValueSigned32,
ValueUnsigned64, ValueSigned64 Fields
These fields SHALL indicate the attribute value as part of an extension field set, associated with a
given AttributeID under an ExtensionFieldSetStruct’s ClusterID. Which of the fields is used SHALL
be determined by the type of the attribute indicated by AttributeID as follows:
• Data types bool, map8, and uint8 SHALL map to ValueUnsigned8.
• Data types int8 SHALL map to ValueSigned8.
• Data types map16 and uint16 SHALL map to ValueUnsigned16.
• Data types int16 SHALL map to ValueSigned16.
• Data types map32, uint24, and uint32 SHALL map to ValueUnsigned32.
• Data types int24 and int32 SHALL map to ValueSigned32.
• Data types map64, uint40, uint48, uint56 and uint64 SHALL map to ValueUnsigned64.
• Data types int40, int48, int56 and int64 SHALL map to ValueSigned64.
• For derived types, the mapping SHALL be based on the base type. For example, an attribute of
type percent SHALL be treated as if it were of type uint8, whereas an attribute of type per
cent100ths SHALL be treated as if it were of type uint16.
• For boolean nullable attributes, any value that is not 0 or 1 SHALL be considered to have the
null value.
• For boolean non-nullable attributes, any value that is not 0 or 1 SHALL be considered to have
the value FALSE.
• For  non-boolean  nullable  attributes,  any  value  that  is  not  a  valid  numeric  value  for  the
attribute’s type after accounting for range reductions due to being nullable and constraints
SHALL be considered to have the null value for the type.
• For non-boolean non-nullable attributes, any value that is not a valid numeric value for the
attribute’s type after accounting for constraints SHALL be considered to be the valid attribute
value that is closest to the provided value.
◦ In the event that an invalid provided value is of equal numerical distance to the two closest
valid values, the lowest of those values SHALL be considered the closest valid attribute
value.
If the used field does not match the data type of the attribute indicated by AttributeID, the Attribut
eValuePairStruct SHALL be considered invalid.
Examples of processing are:
• ColorControl cluster CurrentX (AttributeID 0x0003) has a type of uint16 and is not nullable.
◦ ValueUnsigned16 of 0xAB12 would be used as-is, as it is in range.
◦ ValueUnsigned16 of 0xFF80 is outside of the range allowed for attribute CurrentX, and
would be saturated to the closest valid value, which is the maximum of the attribute’s con
straint range: 0xFEFF.
• LevelControl cluster CurrentLevel (AttributeID 0x0000) has a type of uint8 and is nullable.
◦ ValueUnsigned8 of 0xA1 would be used as-is, as it is in range.
◦ ValueUnsigned8 of 0xFF is outside the range allowed for nullable attribute CurrentLevel,
and would be considered as the null value.
1.4.7.4. ExtensionFieldSetStruct Type
This data type indicates for a given cluster a set of attributes and their values.

_Table parsed from section 'Data Types':_

* In the context of the Scenes Management Cluster, the table row describes a data type entry with the ID '0' and the name 'ClusterID', which is of the type 'cluster-id' and applies to all constraints. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'ClusterID' data type is always required to be implemented within the Scenes Management Cluster, without any conditions or exceptions. It is an essential element that must be supported according to the Matter specification.

* The table row describes an element within the Scenes Management Cluster, specifically under the Data Types section. The element is identified by the ID '1' and is named 'AttributeValueList'. It is of the type 'list[AttributeValuePairStruct]', indicating that it is a list composed of structures pairing attributes with their values. The 'Constraint' field is marked as 'desc', suggesting that the constraints applicable to this element are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M', signifying that the 'AttributeValueList' is a mandatory element within the Scenes Management Cluster. This means that it is always required to be implemented, without any conditions or exceptions.

1.4.7.4.1. ClusterID Field
This field SHALL indicate the cluster-id of the cluster whose attributes are in the AttributeValueList
field.
1.4.7.4.2. AttributeValueList Field
This field SHALL indicate a set of attributes and their values which are stored as part of a scene.
Attributes which do not have the Scenes ("S") designation in the Quality column of their cluster
specification SHALL NOT be used in the AttributeValueList field.
1.4.7.4.3. Form of ExtensionFieldSetStruct
The AttributeValuePairStructs in the AttributeValueList MAY be in any order.
The AttributeValueList SHOULD contain all the attributes with the Scenes ("S") quality as the specifi
cation of the cluster identified by ClusterID describes, but AttributeValuePairStruct MAY be omitted.
An example using the Color Control cluster:
• Attribute 0x0001, CurrentSaturation, S quality, optional, implemented
• Attribute 0x0003, CurrentX, S quality, optional based on feature, implemented
• Attribute 0x0004, CurrentY, S quality, optional based on feature, implemented
• Attribute 0x0007, ColorTemperatureMireds, S quality, optional based on feature, implemented
• Attribute 0x4000, EnhancedCurrentHue, S quality, optional based on feature, implemented
• Attribute 0x4001, EnhancedColorMode, S quality, mandatory, implemented
• Attribute 0x4002, ColorLoopActive, S quality, optional based on feature, NOT implemented
• Attribute 0x4003, ColorLoopDirection, S quality, optional based on feature, NOT implemented
• Attribute 0x4004, ColorLoopTime, S quality, optional based on feature, NOT implemented
An ExtensionFieldSetStruct containing an invalid AttributeValuePairStruct SHALL be considered
invalid.
1.4.7.5. Logical Scene Table
The Scene Table is used to store information for each scene capable of being invoked on the server.
Each scene is defined for a particular group. The Scene Table is defined here as a conceptual illus
tration to assist in understanding the underlying data to be stored when scenes are defined. Though
the Scene Table is defined here using the data model architecture rules and format, the design is
not normative.
The Scene table is logically a list of fabric-scoped structs. The logical fields of each Scene Table entry
struct are illustrated below. An ExtensionFieldSetStruct MAY be present for each Scenes-supporting
cluster implemented on the same endpoint.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Quality: Fa' with an identifier 'ID' and a scope named 'bric Scoped'. The conformance rule for this element is not explicitly provided in the row data, but based on the context of the Matter Conformance Interpretation Guide, it would typically specify when this element is required or optional. If a conformance string were provided, it would dictate whether 'Quality: Fa' is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on supported features or logical expressions. Without a specific conformance string, we cannot definitively state its requirement status, but it would be interpreted according to the rules outlined in the guide if such information were available.

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on an element identified as 'SceneGroupID'. The 'Conformance' field for this element is marked as '0', which, according to the Matter Conformance Interpretation Guide, indicates that this element is not required and has no dependencies, aligning with the 'Optional' (O) conformance tag. This means that the 'SceneGroupID' is an optional data type within the Scenes Management Cluster, and its inclusion is not mandatory for compliance with the Matter specification.

* The table row pertains to the "Scenes Management Cluster" within the "Data Types" section and describes a data type entry labeled 'Quality: Fa' with a 'bric Scoped' value of 'SceneID'. The conformance rule '1' indicates that this element is mandatory, meaning it is always required to be implemented within the context of the Scenes Management Cluster. The 'SceneID' likely refers to a specific identifier used within this cluster to manage scenes, and the mandatory conformance ensures that this identifier must be supported and implemented in any device or application utilizing this cluster.

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Quality: Fa' with a value of '2', and 'bric Scoped' as 'SceneName'. The conformance rule for this element is not explicitly provided in the row data, but based on the context given, we can infer that the conformance would need to be interpreted using the Matter Conformance Interpretation Guide. If we assume a typical conformance string format, it might specify conditions under which the 'SceneName' data type is required or optional. For instance, if the conformance were something like `M`, it would mean that the 'SceneName' is always required in the Scenes Management Cluster. However, without a specific conformance string provided, we can only describe the general context and potential implications based on typical usage within the Matter specification framework.

* The table row entry pertains to the "SceneTransitionTime" data type within the Scenes Management Cluster, specifically under the Data Types section. The conformance rule for this entry is described as 'Quality: Fa': '3', 'bric Scoped'. This indicates that the conformance of the "SceneTransitionTime" data type is described elsewhere in the documentation, as it is marked with 'desc' (Described). This means that the conformance cannot be easily expressed with a simple tag or logical condition and requires further detailed explanation in another part of the specification. Therefore, to fully understand the requirements and conditions under which "SceneTransitionTime" is applicable, one would need to refer to the specified section of the documentation where its conformance is elaborated.

* The table row entry pertains to the "Scenes Management Cluster" within the "Data Types" section, specifically focusing on an element labeled 'Quality: Fa' with a value of '4', and 'bric Scoped' as 'ExtensionFields'. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves a conditional or complex conformance scenario. Given the absence of a direct conformance string, it suggests that the conformance for this element might be described elsewhere in the documentation, possibly under a 'desc' tag. This implies that the element's requirement status (mandatory, optional, etc.) is dependent on specific conditions or scenarios that are elaborated in another part of the specification. Therefore, to fully understand the conformance of this element, one would need to refer to the detailed description provided in the relevant section of the Matter specification.

1.4.7.5.1. SceneGroupID Field
This field is the group identifier for which this scene applies, or 0 if the scene is not associated with
a group.
1.4.7.5.2. SceneID Field
This field is unique within this group, which is used to identify this scene.
1.4.7.5.3. SceneName Field
The field is the name of the scene.
If scene names are not supported, any commands that write a scene name SHALL simply discard
the name, and any command that returns a scene name SHALL return an empty string.
1.4.7.5.4. SceneTransitionTime Field
This field is the amount of time, in milliseconds, it will take for a cluster to change from its current
state to the requested state.
1.4.7.5.5. ExtensionFields Field
See the Scene Table Extensions subsections of individual clusters. A Scene Table Extension SHALL
only use attributes with the Scene quality. Each ExtensionFieldSetStruct holds a set of values of
these attributes for a cluster implemented on the same endpoint where the Scene ("S") designation
appears in the quality column. A scene is the aggregate of all such fields across all clusters on the
endpoint.

## Attributes

_Table parsed from section 'Attributes':_

* In the Scenes Management Cluster, the attribute identified by ID `0x0000` is named `LastConfiguredBy` and is of type `node-id`. This attribute is applicable to all instances within its context and is marked with a quality of `X`, indicating it is explicitly disallowed. The default value for this attribute is `null`, and it has read and view access permissions (`R V`). The conformance rule for `LastConfiguredBy` is `O`, meaning it is optional. This indicates that the implementation of this attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Scenes Management Cluster, specifically the "SceneTableSize" attribute. This attribute has an ID of '0x0001' and is of type 'uint16', with a default value of 16. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'F', and the 'Access' is 'R V', meaning it is readable and can be viewed. The 'Conformance' is marked as 'M', which means that the "SceneTableSize" attribute is mandatory. This implies that any implementation of the Scenes Management Cluster must include this attribute, as it is always required according to the Matter specification.

* In the Scenes Management Cluster, under the Attributes section, the entry for 'FabricSceneInfo' with ID '0x0002' is defined as a list of 'SceneInfoStruct' type. The 'Constraint' is described elsewhere in the documentation, and the attribute has read (R), view (V), and fabric (F) access permissions. The 'Conformance' is marked as 'M', indicating that this attribute is mandatory. This means that the 'FabricSceneInfo' attribute must always be implemented and supported in any device or application that conforms to the Matter specification for the Scenes Management Cluster.

1.4.8.1. LastConfiguredBy Attribute
This attribute SHALL indicate the Node ID of the node that last configured the Scene Table.
The null value indicates that the server has not been configured, or that the identifier of the node
that last configured the Scenes Management cluster is not known.
The Node ID is scoped to the accessing fabric.
1.4.8.2. SceneTableSize Attribute
This attribute SHALL indicate the number of entries in the Scene Table on this endpoint. This is the
total across all fabrics; note that a single fabric cannot use all those entries (see Handling of fabric-
scoping). The minimum size of this table, (i.e., the minimum number of scenes to support across all
fabrics per endpoint) SHALL be 16, unless a device type in which this cluster is used, defines a
larger value in the device type definition.
1.4.8.3. FabricSceneInfo Attribute
This attribute SHALL indicate a list of fabric scoped information about scenes on this endpoint.
The number of list entries for this attribute SHALL NOT exceed the number of supported fabrics by
the device.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Scenes Management Cluster, specifically the "AddScene" command, which is directed from the client to the server. The command is identified by the ID '0x00' and expects a response in the form of 'AddSceneResponse'. The access level is specified as 'F M', indicating that it requires Fabric-scoped access and is mandatory. The conformance rule for this command is 'M', which means that the "AddScene" command is mandatory and must always be implemented in any device that supports the Scenes Management Cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

_Table parsed from section 'Commands':_

* The table row describes a command within the Scenes Management Cluster, specifically the "AddSceneResponse" command, which is identified by the ID '0x00'. This command is directed from the server to the client, as indicated by the direction "client ⇐ server". The response field is marked 'N', meaning that this command does not expect a response. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "AddSceneResponse" command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "ViewScene" command. This command is directed from the client to the server and expects a response in the form of "ViewSceneResponse." The access level is marked as "F O," indicating that it requires fabric-scoped access and is optional. The conformance rule for this command is "M," meaning it is mandatory. This indicates that the "ViewScene" command must always be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "ViewSceneResponse" command. This command is identified by the ID '0x01' and is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked with 'M', which means that the "ViewSceneResponse" command is mandatory. This implies that any implementation of the Scenes Management Cluster must include this command as a required element, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "RemoveScene" command, which is identified by the ID '0x02'. This command is directed from the client to the server and expects a response in the form of "RemoveSceneResponse". The access level for this command is marked as 'F M', indicating it requires Fabric-scoped access and is mandatory. The conformance rule for this command is 'M', meaning that the "RemoveScene" command is always mandatory within the Scenes Management Cluster. This implies that any implementation of this cluster must support the "RemoveScene" command without any conditional requirements or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "RemoveScene Response" command. This command is identified by the ID '0x02' and is communicated from the server to the client, as indicated by the direction "client ⇐ server." The 'Response' field marked 'N' suggests that this command does not expect a response. The 'Conformance' field is marked with 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "RemoveScene Response" command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "RemoveAllScenes" command. This command is directed from the client to the server and expects a response in the form of "RemoveAllScenesResponse." The access level for this command is marked as "F M," indicating that it requires specific access permissions. The conformance rule for this command is marked as "M," which means it is mandatory. This implies that the "RemoveAllScenes" command must always be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "RemoveAllScenesResponse" command. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The "Response" field marked as 'N' suggests that this command does not require a response. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "RemoveAllScenesResponse" command is always required to be implemented in any device that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "StoreScene" command, which is identified by the ID '0x04'. This command is directed from the client to the server and expects a response in the form of "StoreSceneResponse". The access level is marked as 'F M', indicating that it requires specific access permissions. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "StoreScene" command must always be implemented and supported in any device or application that utilizes the Scenes Management Cluster, without any conditional dependencies or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "StoreSceneResponse" command. This command is identified by the ID '0x04' and is directed from the server to the client, as indicated by the "client ⇐ server" direction. The "Response" field marked as 'N' suggests that this command does not require a response. The conformance rule 'M' signifies that the "StoreSceneResponse" command is mandatory, meaning it is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "RecallScene" command, which is identified by the ID '0x05'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level is marked as 'F O', suggesting it is accessible under specific conditions or configurations. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "RecallScene" command must always be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "GetSceneMembership" command, which is identified by the ID '0x06'. This command is directed from the client to the server and expects a response in the form of "GetSceneMembershipResponse". The access level for this command is 'F O', indicating it is accessible under certain conditions defined elsewhere. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the "GetSceneMembership" command must always be implemented and supported in any device or application that uses the Scenes Management Cluster, without any conditional exceptions or dependencies.

* In the Scenes Management Cluster, the command with ID '0x06', named 'GetSceneMembershipResponse', is a communication from the server to the client. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device that supports the Scenes Management Cluster. There are no conditions or dependencies affecting its requirement status, so it must be supported without exception. The 'Response' field marked as 'N' indicates that this command does not expect a response from the client.

* In the Scenes Management Cluster, the command identified by ID `0x40` is named `CopyScene` and is directed from the client to the server. It expects a response in the form of `CopySceneResponse`. The access level for this command is marked as `F M`, indicating it requires Fabric-scoped access and is mandatory in that context. The conformance rule for `CopyScene` is `O`, which means that this command is optional. There are no additional conditions or dependencies affecting its optional status, so its implementation is not required and can be decided by the manufacturer or developer based on their specific needs or use cases.

* The table row describes a command within the Scenes Management Cluster, specifically the "CopySceneResponse" command, which is identified by the ID '0x40'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The "Response" field marked as 'N' suggests that this command does not expect a response. The conformance rule for this command is specified as "CopyScene," which implies that the command is mandatory if the "CopyScene" feature is supported. If the "CopyScene" feature is not supported, the command is not required. This means that the presence and requirement of the "CopySceneResponse" command are conditional upon the support of the "CopyScene" feature within the device or application context.

1.4.9.1. Generic Usage Notes
The scene identifier 0, when used with group identifier 0, is reserved for the global scene used by
the On/Off cluster.
1.4.9.2. AddScene Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '0' and the name 'GroupID', which is of the type 'group-id' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'GroupID' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '1' named 'SceneID'. This element is of the type 'uint8', which is an unsigned 8-bit integer, and it has a constraint that limits its maximum value to 254. The conformance rule for 'SceneID' is marked as 'M', which stands for Mandatory. This means that the 'SceneID' element is always required to be implemented in any device or system that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint32' and has a constraint that limits its maximum value to 60,000,000. The conformance rule for 'TransitionTime' is marked as 'M', which means it is a Mandatory element. This indicates that 'TransitionTime' is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '3' named 'SceneName'. This element is of the type 'string' and is constrained to a maximum length of 16 characters. The conformance rule for 'SceneName' is marked as 'M', which stands for Mandatory. This means that the 'SceneName' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes an element within the Scenes Management Cluster, specifically a command named "ExtensionFieldSetStructs" with an ID of '4'. This command is of the type 'list[ExtensionFieldSetStruct]', indicating it involves a list of structures called ExtensionFieldSetStruct. The 'Constraint' is marked as 'desc', suggesting that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' is labeled as 'M', which means that this element is mandatory. It is always required to be implemented in any device or system that supports the Scenes Management Cluster, without any conditions or exceptions.

It is not mandatory for an extension field set to be included in the command for every cluster on
that endpoint that has a defined extension field set. Extension field sets MAY be omitted, including
the case of no extension field sets at all.
1.4.9.2.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.2.2. SceneID Field
This field SHALL indicate the scene identifier in the Scene Table.
1.4.9.2.3. TransitionTime Field
This field SHALL indicate the transition time of the scene, measured in milliseconds.
1.4.9.2.4. SceneName Field
This field SHALL indicate the name of the scene.
1.4.9.2.5. ExtensionFieldSetStructs Field
This field SHALL contains the list of extension fields.
1.4.9.2.6. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 5.
2. If the ExtensionFieldSetStructs list is formatted in a way deemed invalid according to the Exten
sionFieldSetStruct structure definition (see ExtensionFieldSetStruct), then the status SHALL be
INVALID_COMMAND in the AddSceneResponse, and the server continues from step 5.
3. If a scene already exists under the same group/scene identifier pair, in step 4 the already exist
ing scene entry SHALL be replaced with the new scene being added. Otherwise, if a scene can
not be created due to the lack of Scene Table capacity for the given fabric, the status SHALL be
RESOURCE_EXHAUSTED and the server continues from step 5.
4. The server adds the scene entry into its Scene Table with fields copied from the AddScene com
mand data fields and the status SHALL be SUCCESS.
a. Any ExtensionFieldSetStruct referencing a ClusterID that is not implemented on the end
point MAY be omitted during processing.
b. Any AttributeValuePairStruct referencing an AttributeID from the referenced cluster that is
not implemented on the endpoint MAY be omitted during processing.
c. If the ExtensionFieldSetStructs list has multiple entries listing the same ClusterID, the last
one within the list SHALL be the one recorded.
d. Within a single entry of the ExtensionFieldSetStructs list, if an ExtensionFieldSet contains
the same AttributeID more than once, the last one within the ExtensionFieldSet SHALL be
the one recorded.
5. If the AddScene command was received as a unicast, the server SHALL then generate an
AddSceneResponse command with the Status field set to the evaluated status.
The SceneTransitionTime field of the Scene Table SHALL be updated with the value of the Transi
tionTime.
1.4.9.3. AddSceneResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, there is an entry for a command named "Status" with an ID of '0' and a type labeled as 'status'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "Status" command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '1' named 'GroupID', which is of the type 'group-id' and has a constraint labeled 'all'. The conformance for this element is marked as 'M', which stands for Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '2' named 'SceneID'. This element is of type 'uint8' and has a constraint that limits its maximum value to 254. The conformance rule for 'SceneID' is marked as 'M', which stands for Mandatory. This means that the 'SceneID' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.3.1. Status Field
This field SHALL be set according to the Effect on Receipt section for AddScene command.
1.4.9.3.2. GroupID Field
The GroupID field SHALL be set to the corresponding field of the received AddScene command.
1.4.9.3.3. SceneID Field
The SceneID field SHALL be set to the corresponding field of the received AddScene command.
1.4.9.3.4. When Generated
This command is generated in response to a received AddScene command.
1.4.9.4. ViewScene Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '0' and the name 'GroupID', which is of the type 'group-id' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'GroupID' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, within the Commands section, the table row describes an element with the ID '1' named 'SceneID'. This element is of type 'uint8' and has a constraint that limits its maximum value to 254. The conformance rule for 'SceneID' is indicated by 'M', which means that this element is mandatory. It is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.4.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.4.2. SceneID Field
This field SHALL indicate the scene identifier in the Scene Table.
1.4.9.4.3. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 4.
2. The server verifies that the scene entry corresponding to the GroupID and SceneID fields exists
in its Scene Table. If there is no such entry in its Scene Table, the status SHALL be NOT_FOUND
and the server continues from step 4.
3. The server retrieves the requested scene entry from its Scene Table and the status SHALL be
SUCCESS.
4. If  the  ViewScene  command  was  received  as  a  unicast,  the  server  SHALL  then  generate  a
ViewSceneResponse command with the retrieved scene entry and the Status field set to the
evaluated status.
The order of attributes within the ExtensionFieldSetStruct MAY differ in implemen
NOTE
tation-defined ways from any potential order given in a prior AddScene.
1.4.9.5. ViewSceneResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes a command with the ID '0' and the name 'Status'. This command is of the type 'status', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the 'Status' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Scenes Management Cluster. There are no conditions or exceptions to this requirement; it is a fundamental part of the cluster's functionality.

* The table row describes a command within the Scenes Management Cluster, specifically the 'GroupID' command, which is of type 'group-id' and applies to all constraints. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '2' named 'SceneID'. This element is of type 'uint8', which is an unsigned 8-bit integer, and it has a constraint that limits its maximum value to 254. The conformance rule for 'SceneID' is marked as 'M', indicating that this element is mandatory. This means that the 'SceneID' must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the entry for 'TransitionTime' is identified by ID '3' and is of type 'uint32', with a constraint that its maximum value is 60,000,000. The 'Conformance' field is marked as 'desc', indicating that the conformance requirements for 'TransitionTime' are too complex to be expressed with a simple tag or logical condition. Instead, the specific conditions or rules governing its implementation are detailed elsewhere in the documentation. This means that to fully understand when and how 'TransitionTime' should be implemented, one must refer to the additional descriptive information provided in the specification.

* In the Scenes Management Cluster, under the Commands section, there is an entry for a command named "SceneName" with an ID of '4'. This command is of the type 'string' and is constrained to a maximum length of 16 characters. The conformance for this command is marked as 'desc', indicating that the rules governing when and how this command is required are too complex to be captured by a simple tag or expression. Instead, the detailed conformance requirements are described elsewhere in the documentation. This means that to fully understand the conditions under which the "SceneName" command must be implemented, one would need to refer to the additional documentation provided in the Matter specification.

* The table row entry pertains to the "ExtensionFieldSetStructs" command within the Scenes Management Cluster, specifically under the Commands section. This command is identified by the ID '5' and is of the type 'list[ExtensionFieldSetStruct]'. The conformance for this command is marked as 'desc', indicating that its conformance requirements are too complex to be captured by a simple tag or expression. Instead, the specific conditions or rules governing when this command is required or optional are detailed elsewhere in the documentation. This suggests that understanding the precise conformance of "ExtensionFieldSetStructs" necessitates consulting additional descriptive material provided in the Matter specification.

1.4.9.5.1. Status Field
This field SHALL be set according to the Effect on Receipt section for ViewScene command.
1.4.9.5.2. GroupID Field
The GroupID field SHALL be set to the corresponding field of the received ViewScene command.
1.4.9.5.3. SceneID Field
The SceneID field SHALL be set to the corresponding field of the received ViewScene command.
1.4.9.5.4. TransitionTime Field
If the status is SUCCESS, this field SHALL be copied from the corresponding field in the Scene Table
entry, otherwise it SHALL be omitted.
1.4.9.5.5. SceneName Field
If the status is SUCCESS, this field SHALL be copied from the corresponding field in the Scene Table
entry, otherwise it SHALL be omitted.
1.4.9.5.6. ExtensionFieldSetStructs Field
If the status is SUCCESS, this field SHALL be copied from the corresponding field in the Scene Table
entry, otherwise it SHALL be omitted.
1.4.9.5.7. When Generated
This command is generated in response to a received ViewScene command.
1.4.9.6. RemoveScene Command

_Table parsed from section 'Commands':_

* The table row describes an element within the Scenes Management Cluster, specifically under the Commands section. The element is identified by the ID '0' and is named 'GroupID', with a type specified as 'group-id' and a constraint labeled as 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'GroupID' command is a required element in the Scenes Management Cluster and must be implemented in all cases without exception.

* In the Scenes Management Cluster, within the Commands section, there is an entry for a command identified by 'ID' 1, named 'SceneID'. This command is of type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 254. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the 'SceneID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.6.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.6.2. SceneID Field
This field SHALL indicate the scene identifier in the Scene Table.
1.4.9.6.3. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 4.
2. The server verifies that the scene entry corresponding to the GroupID and SceneID fields exists
in its Scene Table. If there is no such entry in its Scene Table, the status SHALL be NOT_FOUND
and the server continues from step 4.
3. The server removes the requested scene entry from its Scene Table and the status SHALL be
SUCCESS.
4. If the RemoveScene command was received as a unicast, the server SHALL then generate a
RemoveSceneResponse command with the Status field set to the evaluated status.
1.4.9.7. RemoveSceneResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, within the Commands section, there is an entry for a command identified by the ID '0' and named 'Status'. This command is of the type 'status', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the 'Status' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Scenes Management Cluster. There are no conditions or exceptions to this requirement; it is an essential component of the cluster.

* In the Scenes Management Cluster, within the Commands section, the table row describes an element with the ID '1' and the Name 'GroupID', which is of the type 'group-id' and applies to all constraints. The conformance rule for this element is 'M', indicating that it is Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '2', named 'SceneID', which is of type 'uint8' and has a constraint of a maximum value of 254. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'SceneID' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.7.1. Status Field
This field SHALL be set according to the Effect on Receipt section for RemoveScene command.
1.4.9.7.2. GroupID Field
The GroupID field SHALL be set to the corresponding field of the received RemoveScene command.
1.4.9.7.3. SceneID Field
The SceneID field SHALL be set to the corresponding field of the received RemoveScene command.
1.4.9.7.4. When Generated
This command is generated in response to a received RemoveScene command.
1.4.9.8. RemoveAllScenes Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, within the Commands section, the table row describes an element with the ID '0' and the name 'GroupID', which is of the type 'group-id' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that the 'GroupID' is a Mandatory element. This means that it is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.8.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.8.2. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 3.
2. The server SHALL remove all scenes, corresponding to the value of the GroupID field, from its
Scene Table and the status SHALL be SUCCESS.
3. If the RemoveAllScenes command was received as a unicast, the server SHALL then generate a
RemoveAllScenesResponse command with the Status field set to the evaluated status.
1.4.9.9. RemoveAllScenesResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes a command with the ID '0' and the name 'Status'. The type of this command is 'status', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', which signifies that the 'Status' command is mandatory. This means that it is always required to be implemented in any device or application that supports the Scenes Management Cluster, with no conditions or exceptions.

* In the context of the Scenes Management Cluster, specifically within the Commands section, the table row describes an element with the ID '1' named 'GroupID', which is of the type 'group-id' and applies to all constraints. The conformance rule for 'GroupID' is marked as 'M', indicating that this element is mandatory. This means that the 'GroupID' command must always be implemented and supported in any device or application that utilizes the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.9.1. Status Field
This field SHALL be set according to the Effect on Receipt section for RemoveAllScenes command.
1.4.9.9.2. GroupID Field
The GroupID field SHALL be set to the corresponding field of the received RemoveAllScenes com
mand.
1.4.9.9.3. When Generated
This command is generated in response to a received RemoveAllScenes command.
1.4.9.10. StoreScene Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Scenes Management Cluster, specifically the 'GroupID' command. This command has an ID of '0' and is of the 'group-id' type, with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the "SceneID" command. This command is identified by the ID '1' and is of type 'uint8', with a constraint that limits its maximum value to 254. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "SceneID" command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.10.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.10.2. SceneID Field
This field SHALL indicate the scene identifier in the Scene Table.
1.4.9.10.3. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 4.
2. If a scene already exists under the same group/scene identifier pair, in step 3 the already exist
ing scene entry SHALL be used to store the current state.
If a scene cannot be created due to the lack of Scene Table capacity for the given fabric, the sta
tus SHALL be RESOURCE_EXHAUSTED and the server continues from step 4.
3. If a scene already exists under the same group/scene identifier pair, the ExtensionFieldSets of
the stored scene SHALL be replaced with the ExtensionFieldSets corresponding to the current
state of other clusters on the same endpoint and the other fields of the scene table entry SHALL
remain unchanged.
Otherwise, a new entry SHALL be added to the scene table, using the provided GroupID and
SceneID, with SceneTransitionTime set to 0, with SceneName set to the empty string, and with
ExtensionFieldSets corresponding to the current state of other clusters on the same endpoint.
The status SHALL be SUCCESS.
4. If the StoreScene command was received as a unicast, the server SHALL then generate a
StoreSceneResponse command with the Status field set to the evaluated status.
Note that if a scene to be stored requires a TransitionTime field and/or a SceneName field, these
must be set up by a prior AddScene command, e.g., with no scene extension field sets.
1.4.9.11. StoreSceneResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, there is an entry for a command identified by ID '0' with the name 'Status' and a type of 'status'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the 'Status' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically the 'GroupID' command, which is of the 'group-id' type and applies to all constraints. The conformance rule for this command is marked as 'M', indicating that it is Mandatory. This means that the 'GroupID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table entry for 'SceneID' with ID '2' is defined as a data type of 'uint8' with a constraint of a maximum value of 254. The conformance rule for 'SceneID' is marked as 'M', which stands for Mandatory. This means that the 'SceneID' element is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.11.1. Status Field
This field SHALL be set according to the Effect on Receipt section for StoreScene command.
1.4.9.11.2. GroupID Field
The GroupID field SHALL be set to the corresponding field of the received StoreScene command.
1.4.9.11.3. SceneID Field
The SceneID field SHALL be set to the corresponding field of the received StoreScene command.
1.4.9.11.4. When Generated
This command is generated in response to a received StoreScene command.
1.4.9.12. RecallScene Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table entry for 'GroupID' with ID '0' and type 'group-id' is described. The 'Constraint' is listed as 'all', indicating it applies universally within its context. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'GroupID' element is always required and must be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes an element within the Scenes Management Cluster, specifically a command identified by the ID '1' and named 'SceneID'. This command is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 254. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'SceneID' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, within the Commands section, the table row describes an element with the ID '2', named 'TransitionTime'. This element is of type 'uint32' and has a constraint that limits its maximum value to 60,000,000. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'O', which means that the 'TransitionTime' element is optional. It is not required and has no dependencies, allowing implementers the flexibility to include or exclude this element without affecting compliance with the Matter specification.

1.4.9.12.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.12.2. SceneID Field
This field SHALL indicate the scene identifier in the Scene Table.
1.4.9.12.3. TransitionTime Field
This field SHALL indicate the transition time of the scene, measured in milliseconds.
1.4.9.12.4. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 4.
2. The server verifies that the scene entry corresponding to the GroupID and SceneID fields exists
in its Scene Table. If there is no such entry in its Scene Table, the status SHALL be NOT_FOUND
and the server continues from step 4.
3. The server retrieves the requested scene entry from its Scene Table. For each other cluster
implemented on the endpoint, it SHALL retrieve any corresponding extension field sets from
the Scene Table and set the attributes and corresponding state of the cluster accordingly. If
there is no extension field set for a cluster, the state of that cluster SHALL remain unchanged. If
an extension field set omits the values of any attributes, the values of these attributes SHALL
remain unchanged. If an extension field set would cause an unknown or missing attribute to be
set for any reason, that attribute SHALL be skipped. The status SHALL be SUCCESS.
4. If the RecallScene command was received as a unicast, the server SHALL then generate a
response with the Status field set to the evaluated status.
If the TransitionTime data field is present in the command and its value is not equal to null, this
field SHALL indicate the transition time in milliseconds. In all other cases (command data field not
present or value equal to null), the SceneTransitionTime field of the Scene Table entry SHALL indi
cate the transition time. The transition time determines how long the transition takes from the old
cluster state to the new cluster state. It is recommended that, where possible (e.g., it is not possible
for attributes with Boolean data type), a gradual transition SHOULD take place from the old to the
new state over this time. However, the exact transition algorithm is implementation-defined.
1.4.9.13. GetSceneMembership Command
This command can be used to get the used scene identifiers within a certain group, for the endpoint
that implements this cluster.

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, the table row describes an element with the ID '0' named 'GroupID', which is of the type 'group-id' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that the 'GroupID' is a mandatory element. This means that within the context of the Scenes Management Cluster, the 'GroupID' must always be implemented and supported without any conditions or exceptions.

1.4.9.13.1. GroupID Field
This field SHALL indicate the group identifier in the Group Table.
1.4.9.13.2. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of the GroupID field is non-zero, the server verifies that the endpoint has an entry
for that GroupID in the Group Table. If there is no such entry in the Group Table, the status
SHALL be INVALID_COMMAND and the server continues from step 3.
2. The status SHALL be SUCCESS.
3. If the GetSceneMembership command was received as a unicast, the server SHALL then gener
ate a GetSceneMembershipResponse command with the Status field set to the evaluated status.
1.4.9.14. GetSceneMembershipResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, within the Commands section, there is an entry for a command identified as 'Status' with an ID of '0' and a type of 'status'. The 'Constraint' for this command is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' for this command is marked as 'M', which means that the 'Status' command is mandatory. This implies that it is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, the command identified by 'ID' 1, named 'Capacity', is of type 'uint8' and applies to all constraints. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', meaning that the 'Capacity' command is mandatory and must always be implemented in this context. This requirement is unconditional and does not depend on any other features or conditions.

* In the Scenes Management Cluster, under the Commands section, the table entry for 'GroupID' with ID '2' and type 'group-id' is specified. The 'Constraint' is listed as 'all', indicating that this command applies universally within its context. The 'Conformance' is marked as 'M', which stands for Mandatory. This means that the 'GroupID' command is a required element that must be implemented in all instances of the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, the command identified as 'SceneList' with an ID of '3' is of the type 'list[uint8]'. The conformance rule for this command is expressed as 'Status==Success'. This means that the 'SceneList' command is mandatory when the condition 'Status==Success' is true. In other words, if the feature or condition represented by 'Status' is equal to 'Success', then the 'SceneList' command must be implemented. If 'Status' does not equal 'Success', the conformance rule does not specify any requirement, implying that the command is not mandatory in those cases.

1.4.9.14.1. Status Field
This field SHALL be set according to the Effect on Receipt section for GetSceneMembership com
mand.
1.4.9.14.2. Capacity Field
This field SHALL contain the remaining capacity of the Scene Table of the server (for all groups for
the accessing fabric). The following values apply:
• 0 - No further scenes MAY be added.
• 0 < Capacity < 0xFE - Capacity holds the number of scenes that MAY be added.
• 0xFE - At least 1 further scene MAY be added (exact number is unknown).
• null - It is unknown if any further scenes MAY be added.
1.4.9.14.3. GroupID Field
This field SHALL be set to the corresponding field of the received GetSceneMembership command.
1.4.9.14.4. SceneList Field
If the status is not SUCCESS then this field SHALL be omitted, else this field SHALL contain the iden
tifiers of all the scenes in the Scene Table with the corresponding Group ID.
1.4.9.14.5. When Generated
This command is generated in response to a received GetSceneMembership command.
1.4.9.15. CopyScene Command
This command allows a client to efficiently copy scenes from one group/scene identifier pair to
another group/scene identifier pair.

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, there is an entry for a command with the ID '0' named 'Mode', which is of the type 'CopyModeBitmap'. The 'Constraint' for this command is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' for this command is marked as 'M', meaning it is mandatory. This implies that the 'Mode' command must always be implemented and supported in any device or application that utilizes the Scenes Management Cluster, without any conditions or exceptions.

* In the context of the Scenes Management Cluster, specifically within the Commands section, the table row describes a command identified by ID '1' named 'GroupIdentifierFrom'. This command is of the 'group-id' type and applies to all constraints. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'GroupIdentifierFrom' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* The table row describes a command within the Scenes Management Cluster, specifically identified as 'SceneIdentifierFrom' with an ID of '2'. This command is of type 'uint8' and has a constraint that limits its maximum value to 254. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'SceneIdentifierFrom' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the entry for 'GroupIdentifierTo' with ID '3' and type 'group-id' is described. The 'Constraint' for this command is 'all', indicating it applies universally within its context. The 'Conformance' is marked as 'M', which stands for Mandatory. This means that the 'GroupIdentifierTo' command is always required to be implemented in any device or system that supports the Scenes Management Cluster, without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the entry for 'SceneIdentifierTo' is identified by the ID '4' and is of type 'uint8', with a constraint that its maximum value can be 254. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'SceneIdentifierTo' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.15.1. Mode Field
This field SHALL contain the information of how the scene copy is to proceed.
The CopyAllScenes bit of the Mode indicates whether all scenes are to be copied. If this value is set
to 1, all scenes are to be copied and the SceneIdentifierFrom and SceneIdentifierTo fields SHALL be
ignored. Otherwise this bit is set to 0.
1.4.9.15.2. GroupIdentifierFrom Field
This field SHALL indicate the identifier of the group from which the scene is to be copied. Together
with the SceneIdentifierFrom field, this field uniquely identifies the scene to copy from the Scene
Table.
1.4.9.15.3. SceneIdentifierFrom Field
This field SHALL indicate the identifier of the scene from which the scene is to be copied. Together
with the GroupIdentifierFrom field, this field uniquely identifies the scene to copy from the Scene
Table.
1.4.9.15.4. GroupIdentifierTo Field
This field SHALL indicate the identifier of the group to which the scene is to be copied. Together
with the SceneIdentifierTo field, this field uniquely identifies the scene to copy to the Scene Table.
1.4.9.15.5. SceneIdentifierTo Field
This field SHALL indicate the identifier of the scene to which the scene is to be copied. Together
with the GroupIdentifierTo field, this field uniquely identifies the scene to copy to the Scene Table.
1.4.9.15.6. Effect on Receipt
On receipt of this command, the server SHALL perform the following procedure:
1. If the value of either the GroupIdentifierFrom field or the Group Identifier To field is non-zero,
the server verifies that the endpoint has an entry for these non-zero group identifiers in the
Group Table. If there are no such entries in the Group Table, the status SHALL be INVALID_
COMMAND and the server continues from step 5.
2. If the CopyAllScenes sub-field of the Mode field is set to 0, the server verifies that the scene
entry corresponding to the GroupIdentifierFrom and SceneIdentifierFrom fields exists in its
Scene Table. If there is no such entry in its Scene Table, the status SHALL be NOT_FOUND and
the server continues from step 5.
3. If the CopyAllScenes sub-field of the Mode field is set to 1, the server SHALL copy all its avail
able scenes with group identifier equal to the GroupIdentifierFrom field under the group identi
fier specified in the GroupIdentifierTo field, leaving the scene identifiers the same. In this case,
the SceneIdentifierFrom and SceneIdentifierTo fields SHALL be ignored.
If the CopyAllScenes sub-field of the Mode field is set to 0, the server SHALL copy the Scene Ta
ble  entry  corresponding  to  the  GroupIdentifierFrom  and  SceneIdentifierFrom  fields  to  the
Scene Table entry corresponding to the GroupIdentifierTo and SceneIdentifierTo fields.
Regardless of the value of the CopyAllScenes subfield, if a scene already exists under the same
group/scene identifier pair, it SHALL be replaced with the scene being copied.
Regardless of the value of the CopyAllScenes subfield, if a scene cannot be copied due to the lack
of Scene Table capacity for the given fabric, the status SHALL be RESOURCE_EXHAUSTED and
the server continues from step 5. In this case, scenes already copied SHALL be kept.
4. The status SHALL be SUCCESS.
5. If the CopyScene command was received as a unicast, the server SHALL then generate a Copy
SceneResponse command with the Status field set to the evaluated status.
1.4.9.16. CopySceneResponse Command

_Table parsed from section 'Commands':_

* In the Scenes Management Cluster, under the Commands section, there is an entry for a command named "Status" with an ID of '0' and a type of 'status'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "Status" command is a required element within the Scenes Management Cluster and must be implemented according to the Matter specification without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the table row describes a command identified by the ID '1' and named 'GroupIdentifierFrom'. This command is of the 'group-id' type and applies to all constraints. The conformance rule for this command is marked as 'M', which means it is mandatory. Therefore, the 'GroupIdentifierFrom' command is a required element in the implementation of the Scenes Management Cluster, and it must always be supported without any conditions or exceptions.

* In the Scenes Management Cluster, under the Commands section, the entry for 'SceneIdentifierFrom' is identified by ID '2' and is of type 'uint8', with a constraint that its maximum value is 254. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'SceneIdentifierFrom' command is always required to be implemented in any device or application that supports the Scenes Management Cluster, without any conditions or exceptions.

1.4.9.16.1. Status Field
This field SHALL be set according to the Effect on Receipt section for the CopyScene command.
1.4.9.16.2. GroupIdentifierFrom Field
This field SHALL be set to the same values as in the corresponding fields of the received CopyScene
command.
1.4.9.16.3. SceneIdentifierFrom Field
This field SHALL be set to the same values as in the corresponding fields of the received CopyScene
command.
1.4.9.16.4. When Generated
The CopySceneResponse command is generated in response to a received CopyScene command.