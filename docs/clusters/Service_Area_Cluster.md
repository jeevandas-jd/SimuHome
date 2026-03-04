
# 1.17 Service Area Cluster

This cluster provides an interface for controlling the areas where a device should operate, for
reporting the status at each area, and for querying the current area.
The device MAY operate at one area at a time, as in the case of a mobile device, such as a robot.
Other devices MAY operate at (service) multiple areas simultaneously, as in the case of a sensor that
can monitor multiple areas. This cluster specification uses the term "operate" to describe both the
operating and servicing actions, regardless of the device type.
The cluster allows the client to select one or more areas on the server, to indicate where the device
SHOULD attempt to operate. An area is one of a list of options that MAY be presented by a client for
a user choice, or understood by the client, via the semantic data of the area.
The area semantic data is a combination of semantic tags, indicating one or more of the following:
the building floor, area type, landmark, and relative position.

## Data Types
1.17.5.1. LandmarkInfoStruct Type
The data from this structure indicates a landmark and position relative to the landmark.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the "Service Area Cluster" under the "Data Types" section, specifically for an element named "LandmarkTag" with an ID of '0'. The type of this element is specified as 'tag', and it has a constraint labeled 'all', indicating that it applies universally within its context. The conformance rule for "LandmarkTag" is 'M', which stands for Mandatory. This means that the "LandmarkTag" element is always required to be implemented in any system or device that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section, identified as 'RelativePositionTag'. This element is of type 'tag' and applies to all constraints, with a quality designation of 'X', indicating it is explicitly disallowed in some contexts. The conformance rule for 'RelativePositionTag' is marked as 'M', meaning it is mandatory. This implies that within the context of the Matter specification, the 'RelativePositionTag' must always be included and implemented as part of the Service Area Cluster's data types, without any conditional exceptions or dependencies.

1.17.5.1.1. LandmarkTag Field
This field SHALL indicate that the area is associated with a landmark.
This field SHALL be the ID of a landmark semantic tag, located within the Common Landmark
Namespace. For example, this tag MAY indicate that the area refers to an area next to a table.
1.17.5.1.2. RelativePositionTag Field
This field SHALL identify the position of the area relative to a landmark. This is a static description
of a zone known to the server, and this field never reflects the device’s own proximity or position
relative to the landmark, but that of the zone.
This field SHALL be the ID of a relative position semantic tag, located within the Common Relative
Position Namespace.
If the RelativePositionTag field is null, this field indicates proximity to the landmark. Otherwise, the
RelativePositionTag field indicates the position of the area relative to the landmark indicated by the
LandmarkTag field. For example, this tag, in conjunction with the LandmarkTag field, MAY indicate
that the area refers to a zone under a table.
1.17.5.2. AreaInfoStruct Type
The data from this structure indicates the name and/or semantic data describing an area, as
detailed below.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section, with the ID '0' and the name 'LocationInfo'. This element is of the type 'locationdesc' and is constrained to apply universally ('all'). The quality of this element is marked as 'X', indicating that it is explicitly disallowed in terms of quality considerations. The conformance rule for 'LocationInfo' is 'M', meaning that this element is mandatory and always required within the specified context of the Matter IoT specification. This means that any implementation of the Service Area Cluster must include the 'LocationInfo' element as a necessary component.

* The table row describes an entry within the Service Area Cluster, specifically under the Data Types section. The entry, identified by ID '1', is named 'LandmarkInfo' and is of the type 'LandmarkInfoStruct'. It has a constraint labeled 'all', and its quality is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The conformance rule for 'LandmarkInfo' is 'M', meaning that this element is mandatory and always required within the context of the Matter specification. This implies that regardless of any other conditions or features, the 'LandmarkInfo' element must be implemented as part of the Service Area Cluster.

This data type includes the LocationInfo field, with the following fields: LocationName, FloorNum
ber, AreaType. Additional semantic data MAY be available in the LandmarkInfo field.
For an area description to be meaningful, it SHALL have at least one of the following:
• a non-empty name (LocationInfo’s LocationName field)
OR
• some semantic data (one or more of these: FloorNumber, AreaType or LandmarkTag)
The normative text from the remainder of this section describes these constraints.
If the LocationInfo field is null, the LandmarkInfo field SHALL NOT be null.
If the LandmarkInfo field is null, the LocationInfo field SHALL NOT be null.
If LocationInfo is not null, and its LocationName field is an empty string, at least one of the follow
ing SHALL NOT be null:
• LocationInfo’s FloorNumber field
• LocationInfo’s AreaType field
• LandmarkInfo field
If all three of the following are null, LocationInfo’s LocationName field SHALL NOT be an empty
string:
• LocationInfo’s FloorNumber field
• LocationInfo’s AreaType field
• LandmarkInfo field
1.17.5.2.1. LocationInfo Field
This field SHALL indicate the name of the area, floor number and/or area type.
A few examples are provided below.
• An area can have LocationInfo’s LocationName field set to "blue room", and the AreaType field
set to the ID of a "Living Room" semantic tag. Clients wishing to direct the device to operate in
(or service) the living room can use this area.
• An area can have LocationInfo set to null, the LandmarkInfo’s LandmarkTag field set to the ID
of the "Table" landmark semantic tag, and the RelativePositionTag field set to the ID of the
"Under" position semantic tag. With such an area indication, the client can request the device to
operate in (or service) the area located under the table.
1.17.5.2.2. LandmarkInfo Field
This field SHALL indicate an association with a landmark. A value of null indicates that the infor
mation is not available or known. For example, this may indicate that the area refers to a zone next
to a table.
If this field is not null, that indicates that the area is restricted to the zone where the landmark is
located, as indicated by the LandmarkTag and, if not null, by the RelativePositionTag fields, rather
than to the entire room or floor where the landmark is located, if those are indicated by the Loca
tionInfo field.
1.17.5.3. MapStruct Type
This is a struct representing a map.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Service Area Cluster's Data Types section, specifically detailing the 'MapID' attribute. This attribute is identified by the ID '0' and is of the type 'uint32', with a default value of 'MS'. The conformance rule for 'MapID' is marked as 'M', indicating that this attribute is mandatory. This means that the 'MapID' attribute is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. This element is identified by the ID '1' and is named 'Name'. It is of the type 'string' with a constraint that limits its maximum length to 64 characters. The default value for this element is 'MS'. The conformance rule for this element is 'M', which means it is mandatory. This indicates that the 'Name' element must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

1.17.5.3.1. MapID Field
This field SHALL represent the map’s identifier.
1.17.5.3.2. Name Field
This field SHALL represent a human understandable map description.
For example: "Main Floor", or "Second Level".
1.17.5.4. AreaStruct Type
This is a struct representing an area known to the server.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. The element is named "AreaID" and is of type `uint32`, which is a 32-bit unsigned integer. The default value for this element is specified as "MS." According to the conformance rule, the 'Conformance' field is marked as "M," indicating that the "AreaID" is a mandatory element. This means that it is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. The element is identified as 'MapID', which is of type 'uint32'. The 'Constraint' for this element is described elsewhere in the documentation, as indicated by 'desc'. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality. The 'Default' value is 'MS'. The 'Conformance' for 'MapID' is marked as 'M', which means that this element is mandatory and always required within the context of the Matter specification. This implies that any implementation of the Service Area Cluster must include the 'MapID' element.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section, identified as 'AreaInfo' with an ID of '2'. This element is of the type 'AreaInfoStruct' and has a default value of 'MS'. According to the conformance rule 'M', the 'AreaInfo' element is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. There are no conditions or dependencies affecting its necessity, ensuring that 'AreaInfo' must be present in all relevant implementations.

1.17.5.4.1. AreaID Field
This field SHALL represent the identifier of the area.
1.17.5.4.2. MapID Field
This field SHALL indicate the map identifier which the area is associated with. A value of null indi
cates that the area is not associated with a map.
If the SupportedMaps attribute is not empty, this field SHALL match the MapID field of an entry
from the SupportedMaps attribute’s list. If the SupportedMaps attribute is empty, this field SHALL
be null.
1.17.5.4.3. AreaInfo Field
This field SHALL contain data describing the area.
This SHOULD be used by clients to determine the name and/or the full, or the partial, semantics of a
certain area.
If any entries on the SupportedAreas attribute’s list have the AreaInfo field missing
NOTE
the semantic data, the client MAY remind the user to assign the respective data.
1.17.5.5. ProgressStruct Type
This is a struct indicating the progress.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. The element is identified as 'AreaID', which is of type 'uint32', indicating it is a 32-bit unsigned integer. The default value for this element is 'MS'. According to the conformance rule 'M', the 'AreaID' is mandatory, meaning it is always required to be implemented in any device or application that supports the Service Area Cluster. This mandatory status ensures that 'AreaID' is consistently available across all implementations, facilitating uniformity and interoperability within the Matter IoT specification.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. The element is identified by the ID '1' and is named 'Status'. It is of the type 'OperationalStatusEnum' and has a default value of 'MS'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Status' element is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row entry describes an element within the Service Area Cluster, specifically in the Data Types section, with the ID '2' and the name 'TotalOperationalTime'. This element is of the type 'elapsed-s', indicating it measures elapsed time in seconds. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Default' value is 'MS', which might refer to a default setting or measurement standard, though it's not elaborated here. The 'Conformance' is marked as 'O', which means that the 'TotalOperationalTime' element is optional. It is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an element within the Service Area Cluster, specifically under the Data Types section. The element is identified by the ID '3' and is named 'InitialTimeEstimate'. It is of the type 'elapsed-s', which likely indicates a measurement in elapsed seconds. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Default' value is 'MS', though the context of this default is not specified in the row. The 'Conformance' is marked as 'O', which means that the 'InitialTimeEstimate' element is optional. This indicates that the element is not required and has no dependencies, allowing implementers the flexibility to include or exclude it based on their specific needs or preferences.

1.17.5.5.1. AreaID Field
This field SHALL indicate the identifier of the area, and the identifier SHALL be an entry in the Sup
portedAreas attribute’s list.
1.17.5.5.2. Status Field
This field SHALL indicate the operational status of the device regarding the area indicated by the
AreaID field.
1.17.5.5.3. TotalOperationalTime Field
This field SHALL indicate the total operational time, in seconds, from when the device started to
operate at the area indicated by the AreaID field, until the operation finished, due to completion or
due to skipping, including any time spent while paused.
A value of null indicates that the total operational time is unknown.
There MAY be cases where the total operational time exceeds the maximum value that can be con
veyed by this attribute, and in such instances this attribute SHALL be populated with null.
This attribute SHALL be null if the Status field is not set to Completed or Skipped.
1.17.5.5.4. InitialTimeEstimate Field
This field SHALL indicate the estimated time for the operation, in seconds, from when the device
will start operating at the area indicated by the AreaID field, until the operation completes, exclud
ing any time spent while not operating in the area.
A value of null indicates that the estimated time is unknown. If the estimated time is unknown, or if
it exceeds the maximum value that can be conveyed by this attribute, this attribute SHALL be null.
After initializing the ProgressStruct instance, the server SHOULD NOT change the value of this field,
except when repopulating the entire instance, to avoid excessive reporting of the Progress attribute
changes.
1.17.5.6. OperationalStatusEnum Type
This data type is derived from enum8.
The following table defines the status values.

_Table parsed from section 'Data Types':_

* In the context of the Service Area Cluster's Data Types, the table row describes a data entry with the name "Pending" and a value of '0x00'. This entry indicates that a device has not yet started or has not finished operating in a specified area, although it is not currently active in that area. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Pending" status is a required element in the specification and must always be implemented in any device or system that adheres to the Matter specification for this cluster.

_Table parsed from section 'Data Types':_

* In the Service Area Cluster, under the Data Types section, the table row describes a data element with the name "Operating" and a value of '0x01'. This element indicates that the device is currently operating within the specified area. The conformance rule for this element is 'M', which stands for Mandatory. This means that the "Operating" element is always required to be implemented in any device or system that supports the Service Area Cluster, without any conditions or exceptions.

* In the Service Area Cluster's Data Types section, the table row describes a data type with the value '0x02' named 'Skipped'. This data type indicates that a device has bypassed a specific area either before or during operation. This could be due to a SkipArea command, an out-of-band command from a vendor's application, a vendor-specific reason like a time limit, or an unsuccessful operation. The conformance rule 'M' signifies that this data type is mandatory, meaning it is always required to be implemented in any device or system that adheres to this specification.

* In the Service Area Cluster, under the Data Types section, the table row describes a data type with the name "Completed" and a hexadecimal value of '0x03'. This data type signifies that a device has finished its operation in a specified area. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Completed" data type is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

1.17.5.6.1. SelectAreasStatus Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the Service Area Cluster, specifically the 'Success' value, which is represented by the hexadecimal code '0x00'. This value indicates that operations in the areas specified by the NewAreas field are permitted and feasible, and that the SelectedAreas attribute will be updated to match the NewAreas field. The conformance rule for this entry is 'M', meaning that the 'Success' value is mandatory. This implies that it is a required element in the specification and must be implemented in any system or device that supports the Service Area Cluster, ensuring consistent behavior across all compliant devices.

* In the Service Area Cluster, under the Data Types section, the entry for 'UnsupportedArea' with a value of '0x01' indicates a scenario where at least one of the entries in the NewAreas field does not correspond to any entries in the SupportedAreas attribute. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'UnsupportedArea' element is always required to be implemented, without any conditions or exceptions. It is a fundamental part of the specification that must be supported in all implementations of this cluster.

_Table parsed from section 'Data Types':_

* In the Service Area Cluster, under the Data Types section, the entry for 'InvalidInMode' with a value of '0x02' indicates a specific condition where a received request cannot be processed due to the device's current mode. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'InvalidInMode' element is always required to be implemented in any device or application that adheres to this section of the Matter specification. There are no conditions or exceptions; it must be supported universally.

* In the context of the Service Area Cluster's Data Types, the table row describes an entry with the name "InvalidSet," identified by the value '0x03'. This entry is summarized as representing a scenario where the set of values is invalid, such as areas on different floors that a robot cannot reach independently. The conformance rule for "InvalidSet" is marked as 'M', indicating that this element is mandatory. This means that the "InvalidSet" must always be included and supported within the implementation of the Service Area Cluster, without any conditions or exceptions.

1.17.5.6.2. SkipAreaStatus Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Service Area Cluster" within the "Data Types" section, specifically describing a data type with the value '0x00' and the name 'Success'. This entry summarizes that skipping the area is permissible and feasible, or that the device has ceased operation at the last available area. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Success' data type is a required element in the Matter specification for any implementation of the Service Area Cluster. It must always be included and supported without exception.

* In the Service Area Cluster, under the Data Types section, the entry for 'InvalidAreaList' with a value of '0x01' indicates a specific condition where the 'SelectedAreas' attribute is empty. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'InvalidAreaList' element is always required to be implemented in any device or application that supports this cluster, without any conditions or exceptions. This ensures that the system consistently recognizes and handles situations where no areas have been selected.

* In the Service Area Cluster, under the Data Types section, the table row describes a data type named "InvalidInMode" with a value of '0x02'. This data type indicates that a received request cannot be processed due to the device's current mode, such as when the CurrentArea attribute is null or the device is not operational. The conformance rule for "InvalidInMode" is marked as 'M', meaning it is mandatory. This indicates that the "InvalidInMode" data type must always be implemented and supported in any device or system using this specification, without any conditions or exceptions.

* In the Service Area Cluster, under the Data Types section, the entry for 'InvalidSkippedArea' with a value of '0x03' indicates a specific condition where the SkippedArea field does not correspond to any entry in the SupportedAreas list. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'InvalidSkippedArea' element is always required to be implemented in any device or application that adheres to this specification. There are no conditions or dependencies that alter its mandatory status, ensuring consistent handling of this specific error condition across all implementations.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "SupportedAreas" within the Service Area Cluster, identified by the ID '0x0000'. This attribute is of the type 'list[AreaStruct]' and can contain a maximum of 255 entries. Its default value is 'MS', and it has read and view access permissions ('R V'). The conformance rule for this attribute is 'M', meaning it is mandatory and must always be implemented in any device or application that supports this cluster. There are no conditions or dependencies affecting its requirement status; it is a fundamental part of the cluster's specification.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "SupportedMaps" within the Service Area Cluster's Attributes section. This attribute has an ID of '0x0001' and is of the type 'list[MapStruct]', with a constraint allowing a maximum of 255 entries. The default value for this attribute is 'MS', and it has read and view access permissions ('R V'). The conformance rule 'MAPS' indicates that the "SupportedMaps" attribute is mandatory if the feature 'MAPS' is supported. If 'MAPS' is not supported, the attribute is not required. This conformance rule ensures that the attribute is included in implementations where the 'MAPS' feature is relevant, aligning with the Matter specification's requirements for feature-dependent elements.

* The table row describes an attribute within the Service Area Cluster, specifically named "SelectedAreas," which is identified by the ID '0x0002'. This attribute is of type 'list[uint32]', meaning it is a list composed of 32-bit unsigned integers. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The default value for this attribute is 'empty', suggesting that it starts as an empty list. The 'Access' is specified as 'R V', meaning the attribute can be read and is volatile, which typically implies it may change frequently or is not persistent. The 'Conformance' is marked as 'M', which stands for Mandatory. This means that the "SelectedAreas" attribute is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes an attribute named "CurrentArea" within the Service Area Cluster, identified by the ID '0x0003'. This attribute is of type 'uint32', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed in certain contexts. The default value for "CurrentArea" is 'null', and it has read and view access permissions, denoted by 'R V'. The 'Conformance' is also marked as 'desc', indicating that the rules governing when this attribute is required are too complex for a simple expression and are described in another section of the documentation. This suggests that the conditions under which "CurrentArea" must be implemented are detailed elsewhere, likely involving complex dependencies or conditions.

* The table row describes an attribute named "EstimatedEndTime" within the Service Area Cluster, specifically under the Attributes section. This attribute has an ID of '0x0004' and is of type 'epoch-s', which likely represents a timestamp in seconds since a defined epoch. The 'Quality' field indicates 'X Q', suggesting that the attribute is disallowed in some contexts and may have additional quality considerations. It has a default value of 'null', and its access is marked as 'R V', meaning it is readable and possibly volatile. The conformance rule '[CurrentArea]' indicates that the "EstimatedEndTime" attribute is optional if the 'CurrentArea' feature is supported. This means that the attribute is not required unless the specific condition of supporting 'CurrentArea' is met, in which case it becomes optional.

* The table row describes an attribute named "Progress" within the Service Area Cluster, specifically under the Attributes section. This attribute has an ID of '0x0005' and is of the type 'list[ProgressStruct]', with a constraint allowing a maximum of 255 entries. Its default state is 'empty', and it has read and view access permissions ('R V'). The conformance rule for this attribute is 'PROG', which indicates that the attribute is mandatory if the feature 'PROG' is supported. If the 'PROG' feature is not supported, the attribute is not required. This means that the inclusion of the "Progress" attribute is conditional based on the presence of the 'PROG' feature within the device or implementation context.

1.17.6.1. SupportedAreas Attribute
This attribute SHALL contain the list of areas that can be included in the SelectedAreas attribute’s
list. Each item in this list represents a unique area, as indicated by the AreaID field of AreaStruct.
Each entry in this list SHALL have a unique value for the AreaID field.
If the SupportedMaps attribute is not empty, each entry in this list SHALL have a unique value for
the combination of the MapID and AreaInfo fields.
If the SupportedMaps attribute is empty, each entry in this list SHALL have a unique value for the
AreaInfo field and SHALL have the MapID field set to null.
An empty value indicates that the device is currently unable to provide the list of supported areas.
due to the maximum size of this list and to the fact that the entries MAY include
strings (see LocationName), care must be taken by implementers to avoid creating a
NOTE
data structure that is overly large, which can result in significant latency in access
ing this attribute.
The value of this attribute MAY change at any time via an out-of-band interaction outside of the
server, such as interactions with a user interface, or due to internal device changes.
When removing entries in the SupportedAreas attribute list the server SHALL adjust the values of
the SelectedAreas, CurrentArea, and Progress attributes such that they only reference valid entries
in the updated SupportedAreas attribute list. These changes to the SelectedAreas, CurrentArea, and
Progress attributes MAY result in the server setting some or all of them to empty (for SelectedAreas
and Progress) or null (for CurrentArea), or updating them with data that matches the constraints
from the description of the respective attributes. These actions are required to ensure having a con
sistent representation of the maps and locations available to the clients.
The SupportedAreas attribute list changes mentioned above SHOULD NOT be allowed while the
device is operating, to reduce the impact on the clients, and the potential confusion for the users.
A few examples are provided below.
Valid list of areas:
• AreaID=0, LocationName="yellow bedroom", MapID=null
• AreaID=1, LocationName="orange bedroom", MapID=null
Valid list of areas:
• AreaID=5, LocationName="hallway", MapID=1
• AreaID=3, LocationName="hallway", MapID=2
1.17.6.2. SupportedMaps Attribute
This attribute SHALL contain the list of supported maps.
A map is a full or a partial representation of a home, known to the device. For example:
• a single level home MAY be represented using a single map
• a two level home MAY be represented using two maps, one for each level
• a single level home MAY be represented using two maps, each including a different set of
rooms, such as "map of living room and kitchen" and "map of bedrooms and hallway"
• a single level home MAY be represented using one map for the indoor areas (living room, bed
rooms etc.) and one for the outdoor areas (garden, swimming pool etc.)
Each map includes one or more areas - see the SupportedAreas attribute. In the context of this clus
ter specification, a map is effectively a group label for a set of areas, rather than a graphical repre
sentation that the clients can display to the users. The clients that present the list of available areas
for user selection (see the SelectAreas command) MAY choose to filter the SupportedAreas list based
on the associated map. For example, the clients MAY allow the user to indicate that the device is to
operate on the first floor, and allow the user to choose only from the areas situated on that level.
If empty, that indicates that the device is currently unable to provide this information.
Each entry in this list SHALL have a unique value for the MapID field.
Each entry in this list SHALL have a unique value for the Name field.
due to the maximum size of this list and to the fact that the entries MAY include
strings (see the Name field of the MapStruct data type), care must be taken by imple
NOTE
menters to avoid creating a data structure that is overly large, which can result in
significant latency in accessing this attribute.
The value of this attribute MAY change at any time via an out-of-band interaction outside of the
server, such as interactions with a user interface.
When updating the SupportedMaps attribute list by deleting entries, or by setting the attribute to an
empty list, the SupportedLocations attribute SHALL be updated such that all entries in that list meet
the constraints indicated in the description of the SupportedLocations attribute. This MAY result in
the  server  removing  entries  from  the  SupportedAreas  attribute  list.  See  the  SupportedAreas
attribute description for the implications of changing that attribute.
The SupportedMaps attribute list changes mentioned above SHOULD NOT be allowed while the
device is operating, to reduce the impact on the clients, and the potential confusion for the users.
1.17.6.3. SelectedAreas Attribute
This attribute SHALL indicate the set of areas where the device SHOULD attempt to operate.
The mobile devices MAY travel without operating across any areas while attempting to reach the
areas indicated by the SelectedAreas attribute. For example, a robotic vacuum cleaner MAY drive
without cleaning when traveling without operating.
If this attribute is empty, the device is not constrained to operate in any specific areas.
If this attribute is not empty:
• each item in this list SHALL match the AreaID field of an entry in the SupportedAreas attribute’s
list
• each entry in this list SHALL have a unique value
1.17.6.4. CurrentArea Attribute
If the device is mobile, this attribute SHALL indicate the area where the device is currently located,
regardless of whether it is operating or not, such as while traveling between areas.
If the device is not mobile and can operate at multiple areas sequentially, this attribute SHALL indi
cate the area which is currently being serviced, or the area which is currently traversed by the
device. For example, a camera device MAY use this attribute to indicate which area it currently
takes video of (serviced area) or which area it currently has in view but not taking video of (e.g. an
area which is traversed while panning).
A  device  MAY  traverse  an  area  regardless  of  the  status  of  the  area  (pending,
NOTE
skipped, or completed).
If a device can simultaneously operate at multiple areas, such as in the case of a sensor that can
monitor multiple areas at the same time, the CurrentArea attribute SHALL NOT be implemented,
since it doesn’t apply. Else this attribute SHALL be optionally implemented.
A null value indicates that the device is currently unable to provide this information. For example,
the device is traversing an unknown area, or the SupportedAreas attribute was updated and the
area where the device is located was removed from that list.
If not null, the value of this attribute SHALL match the AreaID field of an entry on the SupportedAr
eas attribute’s list.
1.17.6.5. EstimatedEndTime Attribute
This attribute SHALL represent the estimated Epoch time for completing operating at the area indi
cated by the CurrentArea attribute, in seconds.
A value of 0 means that the operation has completed.
When this attribute is null, that represents that there is no time currently defined until operation
completion. This MAY happen, for example, because no operation is in progress or because the
completion time is unknown.
This attribute SHALL be null if the CurrentArea attribute is null.
If the Progress attribute is available, and it contains an entry matching CurrentArea, the server
MAY use the time estimate provided in the InitialTimeEstimate field of that entry to compute the
EstimatedEndTime attribute.
The value of this attribute SHALL only be reported in the following cases:
• when it changes to or from 0
• when it decreases
• when it changes to or from null
If the device is capable of pausing its operation, this attribute MAY be set to null, to
NOTE indicate that completion time is unknown, or increment the value while being in
the paused state.
1.17.6.6. Progress Attribute
This attribute SHALL indicate the operating status at one or more areas.
Each entry in this list SHALL have a unique value for the AreaID field.
For each entry in this list, the AreaID field SHALL match an entry on the SupportedAreas attribute’s
list.
When this attribute is empty, that represents that no progress information is currently available.
If the SelectedAreas attribute is empty, indicating the device is not constrained to operate in any
specific areas, the Progress attribute list MAY change while the device operates, due to the device
adding new entries dynamically, when it determines which ones it can attempt to operate at.
If the SelectedAreas attribute is not empty, and the device starts operating:
• the Progress attribute list SHALL be updated so each entry of SelectedAreas has a matching
Progress list entry, based on the AreaID field
• the length of the Progress and SelectedAreas list SHALL be the same
• the entries in the Progress list SHALL be initialized by the server, by having their status set to
Pending or Operating, and the TotalOperationalTime field set to null
When the device ends operation unexpectedly, such as due to an error, the server SHALL update all
Progress list entries with the Status field set to Operating or Pending to Skipped.
When  the  device  finishes  operating,  successfully  or  not,  it  SHALL  NOT  change  the  Progress
attribute, except in the case of an unexpected end of operation as described above, or due to
changes  to  the  SupportedMaps  or  SupportedAreas  attributes,  so  the  clients  can  retrieve  the
progress information at that time.
if the device implements the Operational Status cluster, or a derivation of it, in case
the device fails to service any locations in the SelectedAreas list before ending the
operation, it SHOULD use the Operational Status cluster to indicate that the device
NOTE was unable to complete the operation (see the UnableToCompleteOperation error
from  that  cluster  specification).  The  clients  SHOULD  then  read  the  Progress
attribute, and indicate which areas have been successfully serviced (marked as
completed).

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Service Area Cluster, specifically the "SelectAreas" command, which is directed from the client to the server and expects a "SelectAreasResponse" in return. The access level for this command is optional, meaning it is not required for all implementations. However, the conformance rule for this command is marked as "M," indicating that it is mandatory. This means that, regardless of any other conditions or features, the "SelectAreas" command must be implemented in any device that supports the Service Area Cluster.

* The table row describes a command within the Service Area Cluster, specifically the "SelectAreasResponse" command, which is communicated from the server to the client. The command does not require a response, as indicated by 'Response': 'N'. The access level for this command is optional ('Access': 'O'), meaning it is not required for all implementations. However, the conformance rule for this command is 'M', which signifies that the "SelectAreasResponse" command is mandatory. This means that any implementation of the Service Area Cluster must support this command, making it a required element in the specification.

* The table row describes a command named "SkipArea" within the Service Area Cluster, which is directed from the client to the server and expects a response called "SkipAreaResponse." The access level for this command is optional, indicated by 'O'. The conformance rule for this command is marked as 'desc', meaning that the conditions under which this command is required or optional are too complex to be captured by a simple conformance expression. Instead, these conditions are detailed elsewhere in the documentation. This suggests that the implementation of the "SkipArea" command may depend on specific scenarios or configurations that are elaborated in the accompanying documentation.

* The table row describes a command named "SkipAreaResponse" within the Service Area Cluster, specifically under the Commands section. This command is identified by the ID '0x03' and is directed from the server to the client, as indicated by the "client ⇐ server" direction. The command does not require a response, as denoted by 'Response': 'N'. The access level is optional ('Access': 'O'), meaning it is not required for all implementations. The conformance rule 'SkipArea' indicates that the "SkipAreaResponse" command is mandatory if the feature or condition represented by 'SkipArea' is supported. If the 'SkipArea' feature is not supported, the command is not required.

1.17.7.1. SelectAreas Command
This command is used to select a set of device areas, where the device is to operate.
On receipt of this command the device SHALL respond with a SelectAreasResponse command.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command named "NewAreas" within the Service Area Cluster, specifically under the Commands section. This command has an ID of '0' and is of the type 'list[uint32]', indicating it involves a list of unsigned 32-bit integers. The constraint for this command is marked as 'desc', suggesting that the specific constraints are detailed elsewhere in the documentation. The conformance rule for "NewAreas" is 'M', which means this command is mandatory. It is always required to be implemented in any device or application that supports the Service Area Cluster, with no conditions or exceptions.

1.17.7.1.1. NewAreas Field
This field indicates which areas the device is to operate at.
If this field is empty, that indicates that the device is to operate without being constrained to any
specific areas, and the operation will not allow skipping using the SkipArea Command, otherwise
the field SHALL be a list of unique values that match the AreaID field of entries on the Support
edAreas list.
1.17.7.1.2. Effect on Receipt
If the NewAreas field contains any duplicated entries, the device SHALL operate on only the first
instance of an entry in the list.
[1, 2, 2, 3, 2]
For example, if the list   were received, the device would ignore the duplicated
2 [1, 2, 3]
instances of   in the list and operate as if the list   had been received instead.
If the device determines that it can’t operate at all areas from the list, the SelectAreasResponse com
mand’s Status field SHALL indicate InvalidSet.
If at least one entry on the NewAreas field doesn’t match the AreaID field of any entry of the Sup
portedAreas  list,  the  SelectAreasResponse  command’s  Status  field  SHALL  indicate  Unsupport
edArea.
If the current state of the device doesn’t allow for the areas to be selected, the SelectAreasResponse
command SHALL have the Status field set to InvalidInMode.
Unless the SelectWhileRunning feature indicates that selecting areas is allowed while the device is
in a non-idle state, such as operating or paused, the SelectAreasResponse command SHALL have
the Status field set to InvalidInMode if this restriction prevents changing the selected areas.
Otherwise, if the device accepts the request, the server will attempt to operate at the areas indi
cated by the entries of the NewArea field, the SelectAreasResponse command SHALL have the Sta
tus field set to Success, and the SelectedAreas attribute SHALL be set to the value of the NewAreas
field.
The device MAY start to operate immediately or wait until specifically requested to
NOTE
operate. The behavior of the device is manufacturer specific.
If the NewAreas field is the same as the value of the SelectedAreas attribute the SelectAreasRe
sponse command SHALL have the Status field set to Success and the StatusText field MAY be sup
plied with a human readable string or include an empty string.
1.17.7.2. SelectAreasResponse Command
This command is sent by the device on receipt of the SelectAreas command. This command SHALL
have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Service Area Cluster, specifically the "Status" command, which is of the type "SelectAreasStatus" and applies to all constraints. The conformance rule for this command is marked as "M," which stands for Mandatory. This means that the "Status" command is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes a command within the Service Area Cluster, specifically identified as 'StatusText'. This command is of the type 'string' and is constrained to a maximum length of 256 characters. The conformance rule for 'StatusText' is marked as 'M', which stands for Mandatory. This means that the 'StatusText' command is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

1.17.7.2.1. Status Field
If the Status field is set to Success or UnsupportedArea, the server MAY use a non-empty string for
the StatusText field to provide additional information. For example, if Status is set to Unsupport
edArea, the server MAY use StatusText to indicate which areas are unsupported.
If the Status field is not set to Success, or UnsupportedArea, the StatusText field SHALL include a
vendor-defined error description which can be used to explain the error to the user. For example, if
the Status field is set to InvalidInMode, the StatusText field SHOULD indicate why the request is not
allowed, given the current mode of the device, which MAY involve other clusters.
1.17.7.3. SkipArea Command
This command is used to skip the given area, and to attempt operating at other areas on the Sup
portedAreas attribute list.
This command SHALL NOT be implemented if the CurrentArea attribute and the Progress attribute
are both not implemented. Else, this command SHALL be optionally implemented.
On receipt of this command the device SHALL respond with a SkipAreaResponse command.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Service Area Cluster, specifically identified as 'SkippedArea' with an ID of '0'. This command is of type 'uint32', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', meaning it is mandatory. This implies that the 'SkippedArea' command must always be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

1.17.7.3.1. SkippedArea Field
The SkippedArea field indicates the area to be skipped.
The SkippedArea field SHALL match an entry in the SupportedAreas list.
1.17.7.3.2. Effect on Receipt
If the SelectedAreas attribute is empty, the SkipAreaResponse command’s Status field SHALL indi
cate InvalidAreaList.
If the SkippedArea field does not match an entry in the SupportedAreas attribute, the SkipAreaRe
sponse command’s Status field SHALL indicate InvalidSkippedArea.
If the SkipArea command can not be handled by the device, e.g. due to the current state, the
SkipAreaResponse command’s Status field SHALL indicate InvalidInMode.
Otherwise, if the device accepts the request, the device SHALL return a SkipAreaResponse with the
Status field set to Success and:
• If the device is currently operating at the area identified by SkippedArea, as indicated by either
the CurrentArea or the Progress attributes, if implemented, the device SHALL stop operating at
that area.
• If the Progress attribute is implemented, the entry corresponding to SkippedArea SHALL be
updated to indicate that the area was skipped.
• The device SHALL attempt to operate only at the areas in the SelectedAreas attribute list where
operating has not been skipped or completed, using a vendor defined order.
• If the device has either skipped or completed operating at all areas on the SelectedAreas
attribute list, the server SHALL stop operating.
1.17.7.4. SkipAreaResponse Command
This command is sent by the device on receipt of the SkipArea command.
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* In the Service Area Cluster, under the Commands section, there is a command identified as 'Status' with an ID of '0' and a type of 'SkipAreaStatus'. The 'Constraint' for this command is listed as 'all', indicating it applies universally within its context. The 'Conformance' for this command is marked as 'M', which stands for Mandatory. This means that the 'Status' command is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* In the Service Area Cluster, under the Commands section, the table row describes a command named "StatusText" with an ID of '1'. This command is of the type 'string' and is constrained to a maximum length of 256 characters. The conformance rule for "StatusText" is marked as 'M', which stands for Mandatory. This means that the "StatusText" command is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

1.17.7.4.1. Status Field
If the Status field is set to Success or InvalidAreaList, the server MAY use a non-empty string for the
StatusText field to provide additional information. For example, if Status is set to InvalidAreaList,
the server MAY use StatusText to indicate why this list is invalid.
If the Status field is not set to Success or InvalidAreaList, the StatusText field SHALL include a ven
dor defined error description which can be used to explain the error to the user. For example, if the
Status field is set to InvalidInMode, the StatusText field SHOULD indicate why the request is not
allowed, given the current mode of the device, which MAY involve other clusters.
Chapter 2. Measurement and Sensing
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter. References
to external documents are contained in Chapter 1 and are made using [Rn] notation.
2.1. General Description

## Introduction
The clusters specified in this document are generic measurement and sensing interfaces that are
sufficiently general to be of use across a wide range of application domains.

## Cluster List
This section lists the measurement and sensing clusters as specified in this chapter.
Table 5. Overview of the Measurement and Sensing Clusters

_Table parsed from section 'Cluster List':_

* The table row describes the "Illuminance Measurement" cluster within the "Service Area Cluster" context, identified by the Cluster ID '0x0400'. This cluster encompasses attributes and commands essential for configuring and reporting illuminance measurements. The conformance rule for this cluster is not explicitly provided in the given data, but based on the Matter Conformance Interpretation Guide, if it were to be specified, it would indicate whether the cluster is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions. For instance, if the conformance were 'M', it would mean that the Illuminance Measurement cluster is always required in any implementation. If it were 'O', it would be optional with no dependencies. The absence of a specific conformance string in the provided data suggests that further documentation or context is needed to determine the precise conformance requirements for this cluster.

* The table row describes the "Temperature Measurement" cluster within the "Service Area Cluster" context, identified by the Cluster ID '0x0402'. This cluster encompasses attributes and commands essential for configuring and reporting temperature measurements. The conformance rule for this cluster is not explicitly provided in the data snippet, but if it were, it would dictate the conditions under which this cluster is required, optional, or otherwise specified, based on the Matter Conformance Interpretation Guide. The guide outlines how to interpret such rules, which could involve mandatory inclusion, optional support, or conditional requirements based on the presence or absence of certain features or conditions.

* The table row describes the "Pressure Measurement" cluster, identified by the Cluster ID '0x0403', within the Service Area Cluster's Cluster List. This cluster encompasses attributes and commands necessary for configuring and reporting pressure measurements. The conformance rule for this cluster is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, it would typically specify whether the cluster is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirements for implementing this cluster, but it would generally dictate when and how the Pressure Measurement cluster should be integrated into a Matter-compliant device or system.

* The table row entry describes the "Flow Measurement" cluster within the Service Area Cluster context, identified by the Cluster ID '0x0404'. This cluster encompasses attributes and commands essential for configuring and reporting flow measurements and flow rates. The conformance rule for this cluster is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate when this cluster's features are required, optional, provisional, deprecated, or disallowed. For instance, if the conformance were 'M', it would mean that the Flow Measurement cluster is always mandatory. If it were 'O', the cluster would be optional with no dependencies. The absence of a specific conformance string in the provided data suggests that further documentation should be consulted to determine the exact conformance requirements for this cluster.

* The table row describes the "Relative Humidity Measurement" cluster, identified by the Cluster ID '0x0405', within the Service Area Cluster's Cluster List. This cluster supports the configuration and reporting of relative humidity measurements, specifically focusing on the humidity of water in the air. The conformance rule for this cluster is not explicitly provided in the data, but based on the context, it would typically indicate whether the inclusion of this cluster is mandatory, optional, or subject to certain conditions within a device's implementation. Without a specific conformance string, we assume that the cluster's inclusion depends on the broader requirements of the device or application context within the Matter specification.

* The table row entry describes the "Occupancy Sensing" cluster, identified by the Cluster ID '0x0406', within the Service Area Cluster's Cluster List. This cluster encompasses attributes and commands essential for configuring occupancy sensing and reporting occupancy status. The conformance rule for this cluster is not explicitly provided in the data snippet, so we cannot directly interpret it using the conformance guide. However, typically, if the conformance were specified, it would indicate whether the "Occupancy Sensing" cluster is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features being supported. Without the specific conformance string, we can only infer that this cluster plays a role in managing occupancy-related functionalities within an IoT ecosystem.

_Table parsed from section 'Cluster List':_

* The table row entry describes a cluster within the Service Area Cluster context, specifically named "Resource Monitoring." This cluster encompasses attributes and commands designed to report on the conditions of various resources. The 'Cluster ID' is listed as 'various,' indicating that this cluster may apply to multiple identifiers depending on the specific implementation or resource being monitored. The conformance rules for this entry are not explicitly provided in the data, but based on the context, it likely involves a combination of mandatory and optional elements depending on the specific features or conditions present in the implementation. The description suggests that the cluster's elements are essential for monitoring resource conditions, but without a specific conformance string, we cannot determine the exact requirements or optionality of its components.

* The table row describes the "Air Quality Measurement" cluster, identified by the Cluster ID `0x005B`, within the Service Area Cluster's Cluster List. This cluster is responsible for attributes that report air quality classification. The conformance rule for this cluster is not explicitly provided in the data snippet, but if it were, it would dictate the conditions under which the cluster's features are required, optional, provisional, deprecated, or disallowed. For example, if the conformance was `M`, it would mean that the Air Quality Measurement cluster is always mandatory. If it were `AB, O`, it would mean the cluster is mandatory if feature `AB` is supported, otherwise optional. Understanding the conformance rule is crucial for implementing the cluster correctly in a Matter-compliant device.

* The table row entry pertains to the "Concentration Measurement" cluster within the Service Area Cluster's Cluster List. This cluster is identified by various Cluster IDs and encompasses attributes and aliases related to concentration measurements. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically specify when the features or attributes of this cluster are required, optional, or subject to other conditions as per the Matter specification. Without a specific conformance string, one can infer that the cluster's inclusion and the implementation of its features depend on the broader requirements and conditions outlined in the Matter specification for the Service Area Cluster.

* The table row describes a cluster within the Matter IoT specification, specifically identified by the Cluster ID `0x005C` and named "Smoke and CO Alarm." This cluster serves as an interface for smoke and carbon monoxide alarms, facilitating communication and control within a smart home ecosystem. The conformance rule for this cluster is not explicitly provided in the data you shared, but typically, it would dictate when and how this cluster must be implemented in devices. For instance, if the conformance were `M`, it would mean that the Smoke and CO Alarm cluster is mandatory for all devices that support the relevant service area. If the conformance were `O`, it would be optional, allowing manufacturers to include it at their discretion. Without the specific conformance string, we can only infer that this cluster plays a crucial role in enhancing safety by integrating smoke and CO alarms into the Matter-enabled network.

* The table row describes the "Electrical Energy Measurement" cluster within the Service Area Cluster, identified by the Cluster ID '0x0091'. This cluster encompasses attributes and commands specifically designed for measuring electrical energy. The conformance rule for this cluster is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, it would typically indicate whether the cluster is mandatory, optional, provisional, deprecated, or disallowed, or if its inclusion depends on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirements for this cluster, but it would generally dictate when and how this cluster should be implemented in devices supporting the Matter specification.

* The table row describes the "Electrical Power Measurement" cluster within the Service Area Cluster context, identified by the Cluster ID '0x0090'. This cluster includes attributes and commands specifically designed for measuring electrical power. The conformance rule for this cluster is not explicitly provided in the data given, but based on the Matter Conformance Interpretation Guide, it would typically specify whether the cluster is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions. For example, if the conformance were 'M', it would mean that the Electrical Power Measurement cluster is always required in any implementation. If it were 'O', it would be optional, meaning it could be included at the implementer's discretion without any dependencies. If a more complex expression were provided, it would detail specific conditions under which the cluster is required or optional, using logical operators and feature codes to define these conditions.

## Measured Value
This section provides requirements on the attributes MeasuredValue, MinMeasuredValue, MaxMea
suredValue. Accuracy of MeasuredValue is discussed in the following section.
2.1.3.1. Constraint
Where MinMeasuredValue or MaxMeasuredValue attributes are mandatory the null value MAY be
used to indicate that a limit is unknown.
For any measurement cluster with MeasuredValue, MinMeasuredValue and MaxMeasuredValue
attributes, the following SHALL be always be true:
• If  MinMeasuredValue  and  MaxMeasuredValue  are  both  known,  then  MaxMeasuredValue
SHALL be greater than MinMeasuredValue.
• If MaxMeasuredValue is known, then MeasuredValue SHALL be less than or equal to MaxMea
suredValue.
• If MinMeasuredValue is known, then MeasuredValue SHALL be greater than or equal to Min
MeasuredValue.

## Measurement Accuracy
Measurement clusters MAY express the accuracy of their measurements with a Tolerance attribute
expressing a simple magnitude of error, or with a MeasurementAccuracyStruct expressing magni
tude or percentage ranges of error for different ranges of measured values.
2.1.4.1. Tolerance Attribute
For any measurement cluster with a MeasuredValue and Tolerance attribute, when Tolerance is
implemented the following SHALL always be true:
• The Tolerance attribute SHALL indicate the magnitude of the possible error that is associated
with MeasuredValue attribute, using the same units and resolution. The true value SHALL be in
the range (MeasuredValue – Tolerance) to (MeasuredValue + Tolerance).
• If known, the true value SHALL never be outside the possible physical range. Some examples:
◦ a temperature SHALL NOT be below absolute zero
◦ a concentration SHALL NOT be negative
2.1.4.2. MeasurementTypeEnum Type
This data type is derived from enum16.

_Table parsed from section 'Measurement Accuracy':_

* In the context of the Service Area Cluster, specifically within the Measurement Accuracy section, the table row describes an entry with the 'Name' "Unspecified" and a 'Value' of "0". The 'Conformance' field for this entry is marked as "M", which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "Unspecified" element is always required in any implementation of this cluster. There are no conditions or dependencies that alter its mandatory status, making it a fundamental component that must be included in all relevant implementations.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "Voltage," which represents the voltage measured in millivolts (mV). The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "Voltage" element is always required to be implemented in any device or application that adheres to this specification. There are no conditions or dependencies affecting its mandatory status, ensuring that it must be consistently included across all relevant implementations.

* The table row entry pertains to the "ActiveCurrent" attribute within the Service Area Cluster, specifically under the Measurement Accuracy section. This attribute represents the active current measured in milliamps (mA). According to the conformance rule indicated by 'M', this attribute is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. There are no conditions or dependencies affecting its necessity; it must be included as part of the standard implementation.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "ReactiveCurrent," which measures reactive current in milliamps (mA) with a value of '3'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the ReactiveCurrent element is always required to be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "ApparentCurrent," which represents the apparent current measured in milliamps (mA). The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "ApparentCurrent" element is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "ActivePower," which represents the active power measured in milliwatts (mW) with a value of '5'. The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "ActivePower" element is always required to be implemented in this context, without any conditions or exceptions.

* The table row entry describes an element named "ReactivePower" within the "Service Area Cluster" under the "Measurement Accuracy" section. This element represents the measurement of reactive power, expressed in millivolt-amps reactive (mVAR). According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Service Area Cluster. There are no conditions or exceptions to this requirement, ensuring that the ReactivePower measurement is consistently available across all relevant implementations.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "ApparentPower," which represents the apparent power measured in millivolt-amps (mVA). The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the ApparentPower attribute is always required to be implemented in any device or application that conforms to this specification, without any conditions or exceptions.

* The table row entry pertains to the "Service Area Cluster" within the "Measurement Accuracy" section and describes an element named "RMSVoltage" with a value of '8'. This element represents the root mean squared voltage measured in millivolts (mV). The conformance rule for "RMSVoltage" is marked as 'M', indicating that this element is mandatory. This means that the RMSVoltage measurement must always be implemented and supported in any device or application that adheres to this particular Matter IoT specification. There are no conditions or dependencies affecting its requirement; it is a fundamental and essential component of the specification.

* The table row entry pertains to the "RMSCurrent" attribute within the "Service Area Cluster" under the "Measurement Accuracy" section. This attribute represents the root mean squared current measured in milliamps (mA). The conformance rule for "RMSCurrent" is marked as "M," which stands for Mandatory. This means that the inclusion of the "RMSCurrent" attribute is always required in any implementation of this cluster, with no conditions or exceptions. It is an essential element that must be supported to comply with the Matter specification for this context.

* The table row entry pertains to the "RMSPower" attribute within the "Service Area Cluster" under the "Measurement Accuracy" section. This attribute represents the root mean squared power measured in milliwatts (mW), with a specified value of '10'. The conformance rule for this attribute is marked as 'M', which stands for Mandatory. This means that the "RMSPower" attribute is always required to be implemented in any device or application that adheres to this section of the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental and non-negotiable element of the specification.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element named "Frequency," which represents the AC frequency measured in millihertz (mHz). The conformance rule for this element is marked as "M," indicating that it is a mandatory feature. This means that the "Frequency" element is always required to be implemented in any device or application that adheres to this part of the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the cluster.

* The table row describes an element within the Service Area Cluster, specifically in the context of Measurement Accuracy. The element is named "PowerFactor" and represents the Power Factor ratio, expressed in increments of +/- 1/100ths of a percent. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the PowerFactor element is always required to be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

_Table parsed from section 'Measurement Accuracy':_

* The table row entry describes an element named "NeutralCurrent" within the "Service Area Cluster" under the "Measurement Accuracy" section. This element represents the alternating current (AC) neutral current measured in milliamps (mA), with a specific value of '13'. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that adheres to this specification. There are no conditions or exceptions; the inclusion of the "NeutralCurrent" element is compulsory.

* The table row entry pertains to the "Service Area Cluster" within the "Measurement Accuracy" section, specifically focusing on the attribute named "ElectricalEnergy." This attribute represents the measurement of electrical energy in milliwatt-hours (mWh) and is identified by the value '14'. The conformance rule for this attribute is marked as 'M', which stands for Mandatory. This means that the "ElectricalEnergy" attribute is always required to be implemented in any device or application that adheres to this part of the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it a fundamental component of the specification.

2.1.4.3. MeasurementAccuracyRangeStruct Type
This struct represents the accuracy of a measurement for a range of measurement values. Accuracy
SHALL be expressed as a maximum +/- percentage of the true value, a maximum +/- fixed value of
the true value, or both.

_Table parsed from section 'Measurement Accuracy':_

* The table row describes an element within the Service Area Cluster, specifically under the Measurement Accuracy section. The element is identified by the ID '0' and is named 'RangeMin'. It is of type 'int64', meaning it is a 64-bit integer, and it has a constraint that limits its value between -262 and 262. The 'Quality' is marked as 'F', which typically indicates a specific quality or characteristic defined elsewhere in the documentation. The 'Access' is 'R', signifying that this element is read-only. The 'Conformance' is marked as 'M', which means that the 'RangeMin' element is mandatory and must always be implemented in any device or application that supports this cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the specification for this context.

* The table row describes an attribute named "RangeMax" within the "Service Area Cluster" under the "Measurement Accuracy" section. This attribute is of type `int64` and has a constraint that limits its values between -262 and 262. The "Quality" is marked as 'F', indicating a specific quality characteristic, and the "Access" is 'R', meaning it is read-only. The "Conformance" is marked as 'M', which means that the "RangeMax" attribute is mandatory. It is always required to be implemented in any device or application that supports this cluster, with no conditions or exceptions.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row with ID '2' refers to an element named 'PercentMax'. This element is of the type 'percent100ths', indicating it measures values in hundredths of a percent. It applies universally, as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'F', and it has 'Read' access, denoted by 'R'. The conformance rule 'O.a+' suggests that the element is optional, with the possibility of additional conditions or future changes not specified in the provided context. This means that currently, the inclusion of 'PercentMax' is not required and does not depend on other features or conditions, but there may be further details or updates elsewhere in the documentation.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element with the ID '3', named 'PercentMin'. This element is of the type 'percent100ths' and has a constraint that it must not exceed 'PercentTypical'. It is a feature of quality 'F', with read-only access ('R'). The conformance rule '[PercentMax]' indicates that the 'PercentMin' element is optional if the feature 'PercentMax' is supported. If 'PercentMax' is not supported, there is no requirement for 'PercentMin' to be included.

* The table row describes an attribute named "PercentTypical" within the "Service Area Cluster" under the "Measurement Accuracy" section. This attribute is of the type "percent100ths" and is constrained between "PercentMin" and "PercentMax." It has a quality designation of "F" and is read-only, as indicated by the access type "R." The conformance rule for "PercentTypical" is `[PercentMin]`, which means that this attribute is optional and should be included if the "PercentMin" feature is supported. If "PercentMin" is not supported, the inclusion of "PercentTypical" is not required.

* The table row entry describes an element within the Service Area Cluster, specifically under the Measurement Accuracy section. The element is identified by the ID '5' and is named 'FixedMax'. It is of type 'uint64', with a constraint indicating that its maximum value is 262 - 1. The 'Quality' is marked as 'F', and it has 'Read' (R) access. The conformance rule 'O.a+' indicates that this element is Optional, with additional conditions or descriptions likely provided elsewhere in the documentation. This means that while the element is not required by default, there may be specific scenarios or additional criteria under which it could become relevant or necessary, as detailed in the broader specification.

* The table row describes an attribute named "FixedMin" within the Service Area Cluster, specifically under the Measurement Accuracy section. This attribute is of type `uint64` and is constrained to a maximum value defined by another attribute, "FixedMax." It has a quality designation of "F" and is read-only, as indicated by the access type "R." The conformance rule `[FixedMax` suggests that the "FixedMin" attribute is optional if the "FixedMax" feature is supported. This means that the inclusion of "FixedMin" is not mandatory unless the condition of having "FixedMax" is met, in which case it becomes an optional attribute.

* In the Service Area Cluster, under the Measurement Accuracy section, the table row describes an element with the ID '7' named 'FixedTypical'. This element is of type 'uint64' and is constrained between 'FixedMin' and 'FixedMax'. It has a quality designation of 'F' and read-only access ('R'). The conformance rule '[FixedMin]' indicates that the 'FixedTypical' element is optional if the feature 'FixedMin' is supported. If 'FixedMin' is not supported, there is no requirement for 'FixedTypical' to be present. This conformance condition allows for flexibility in implementation based on the presence of the 'FixedMin' feature.

[FixedMax]
[FixedMin]
• If both PercentMax and FixedMax are indicated, then for a given true value in the range
between RangeMin and RangeMax,
◦ the reported value SHALL be less than or equal to the sum of the true value, FixedMax and
PercentMax percent of the true value.
◦ the reported value SHALL be greater than or equal to the true value minus the sum of Fixed
Max and PercentMax percent of the true value.
• If only PercentMax is indicated, then for a given true value in the range between RangeMin and
RangeMax,
◦ the reported value SHALL be less than or equal to the sum of the true value and PercentMax
percent of the true value.
◦ the reported value SHALL be greater than or equal to the true value minus PercentMax per
cent of the true value.
• If only FixedMax is indicated, then for a given true value in the range between RangeMin and
RangeMax,
◦ the reported value SHALL be less than or equal to the sum of the true value and FixedMax.
◦ the reported value SHALL be greater than or equal to the true value minus FixedMax.
2.1.4.3.1. RangeMin Field
This field SHALL indicate the minimum measurement value for the specified level of accuracy.
The value of this field SHALL be greater than or equal to the value of the MinMeasuredValue field
on the encompassing MeasurementAccuracyStruct.
The value of this field SHALL be less than or equal to the value of the MaxMeasuredValue field on
the encompassing MeasurementAccuracyStruct.
2.1.4.3.2. RangeMax Field
This field SHALL indicate the maximum measurement value for the specified level of accuracy.
The value of this field SHALL be greater than the value of the RangeMin field.
The value of this field SHALL be greater than or equal to the value of the MinMeasuredValue field
on the encompassing MeasurementAccuracyStruct.
The value of this field SHALL be less than or equal to the value of the MaxMeasuredValue field on
the encompassing MeasurementAccuracyStruct.
2.1.4.3.3. PercentMax Field
This field SHALL indicate the maximum +/- percentage accuracy for the associated measurement.
2.1.4.3.4. PercentMin Field
This field SHALL indicate the minimum +/- percentage accuracy for the associated measurement.
2.1.4.3.5. PercentTypical Field
This field SHALL indicate the typical +/- percentage accuracy for the associated measurement.
2.1.4.3.6. FixedMax Field
This field SHALL indicate the maximum +/- fixed accuracy for the associated measurement, in the
unit indicated by MeasurementType.
2.1.4.3.7. FixedMin Field
This field SHALL indicate the minimum +/- fixed accuracy for the associated measurement, in the
unit indicated by MeasurementType.
2.1.4.3.8. FixedTypical Field
This field SHALL indicate the typical +/- fixed accuracy for the associated measurement, in the unit
indicated by MeasurementType.
2.1.4.4. MeasurementAccuracyStruct Type
This struct represents the set of accuracy ranges for a given measurement, the maximum and mini
mum values for the measurement, and whether the measurement is directly measured or just esti
mated from other information.

_Table parsed from section 'Measurement Accuracy':_

* The table row describes an element within the Service Area Cluster, specifically in the context of Measurement Accuracy. The element is identified by the ID '0' and is named 'MeasurementType'. It is of the type 'MeasurementTypeEnum', indicating it likely represents a set of predefined measurement types. The 'Quality' is marked as 'F', which could denote a specific quality attribute, and the 'Access' is 'R', meaning it is read-only. The 'Conformance' is marked as 'M', which, according to the Matter Conformance Interpretation Guide, means that this element is mandatory. Therefore, the 'MeasurementType' element must always be implemented in any device or application that supports this cluster, with no conditions or exceptions.

* The table row describes an element within the Service Area Cluster, specifically under the Measurement Accuracy section. The element is identified by the ID '1' and is named 'Measured'. It is of the boolean type ('bool'), with a default value of 'false', and its quality is marked as 'F'. The access level for this element is 'R', indicating it is read-only. The conformance rule for this element is 'M', which means it is mandatory. This indicates that the 'Measured' element is always required to be implemented in any device or application that adheres to this specification, without any conditions or exceptions.

* The table row describes an attribute named "MinMeasuredValue" within the "Measurement Accuracy" section of the "Service Area Cluster." This attribute has an ID of '2' and is of type 'int64', with a constraint that limits its value between -262 and 262. The 'Quality' is marked as 'F', and it has 'Read' ('R') access. The conformance rule for this attribute is 'M', which means it is mandatory. This indicates that the "MinMeasuredValue" attribute must always be implemented in any device or application that supports the Service Area Cluster, without any conditions or exceptions.

* The table row describes an attribute named "MaxMeasuredValue" within the "Measurement Accuracy" section of the "Service Area Cluster." This attribute is of type `int64` and has a constraint range from -262 to 262. It is marked with a quality of 'F' and has read-only ('R') access. The conformance rule for this attribute is 'M', which means it is mandatory. This indicates that the "MaxMeasuredValue" attribute must always be implemented and supported in any device or application that adheres to this section of the Matter specification, without any conditions or exceptions.

* The table row describes an element within the Service Area Cluster, specifically under the Measurement Accuracy section. The element, identified by 'ID' 4 and named 'AccuracyRanges', is a list of structures defined as 'MeasurementAccuracyRangeStruct'. It has a constraint indicating that the list must contain at least one item ('min 1'). The 'Quality' is marked as 'F', and the 'Access' is 'R', meaning it is read-only. The 'Conformance' is labeled as 'M', which, according to the Matter Conformance Interpretation Guide, means that this element is mandatory. Therefore, the 'AccuracyRanges' element must always be implemented in any device or application that supports this cluster, without any conditions or exceptions.

2.1.4.4.1. MeasurementType Field
This field SHALL indicate the type of measurement for the accuracy provided.
2.1.4.4.2. Measured Field
This field SHALL indicate whether the associated measurement was directly measured. If this field
is not set to true, then the associated measurement was estimated.
2.1.4.4.3. MinMeasuredValue Attribute
This field SHALL indicate the minimum value that can be measured.
2.1.4.4.4. MaxMeasuredValue Attribute
This field SHALL indicate the maximum value that can be measured.
2.1.4.4.5. AccuracyRanges Field
This field SHALL indicate a list of measurement ranges and their associated accuracies.
The value of the RangeMin field on the first MeasurementAccuracyRangeStruct in this list SHALL
be equal to the value of the MinMeasuredValue field.
The value of the RangeMax field on the last MeasurementAccuracyRangeStruct in this list SHALL be
less than or equal to the value of the MaxMeasuredValue field.
The value of the RangeMin field on each MeasurementAccuracyRangeStruct in this list other than
the first SHALL be one more the value of the RangeMax field on the previous MeasurementAccura
cyRangeStruct in this list (i.e. there SHALL be no gaps in the accuracy ranges, and the ranges SHALL
be in increasing order).