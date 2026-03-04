
# 6.6 Channel Cluster

This cluster provides an interface for controlling the current Channel on a device or endpoint.
This cluster server would be supported on Video Player devices or endpoints that allow Channel
control such as a Content App. This cluster provides a list of available channels and provides com
mands for absolute and relative channel changes. Some of these commands and/or their responses
MAY be large (see Large Message Quality under Data Model section in [MatterCore]), but they do
L
not have the Large quality indicator ( ) because they can also be transferred over MRP (see Mes
sage Reliability Protocol in [MatterCore]) in pages that fit within the MRP MTU limit. However, an
implementation MAY leverage a transport like TCP that allows large payloads, if available, to mini
mize the number of messages required to transfer the corresponding payload.
The cluster server for Channel is implemented by an endpoint that controls the current Channel.

## Data Types
6.6.5.1. RecordingFlagBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row describes a data type with the bit position '0', named 'Scheduled'. This data type indicates that a program is scheduled for recording, as summarized in its description. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Scheduled' data type is always required to be implemented within the Channel Cluster, without any conditions or exceptions.

* In the Channel Cluster's Data Types section, the table row describes a data element with the bit value '1' named 'RecordSeries'. This element indicates that a program series is scheduled for recording. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Channel Cluster. There are no conditions or dependencies affecting its requirement status; it must be included as part of the implementation.

* In the Channel Cluster's Data Types section, the table row describes a data type with the bit position '2', named 'Recorded'. This data type indicates that a program is recorded and available for playback. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Recorded' data type is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

6.6.5.2. LineupInfoTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row entry describes a data type with the value '0' and the name 'MSO', which stands for 'Multi System Operator'. The summary indicates that this data type is associated with multi-system operators. The conformance rule for this entry is 'M', which means that the 'MSO' data type is mandatory. This implies that it is a required element within the Channel Cluster and must always be implemented according to the Matter IoT specification. There are no conditions or exceptions to this requirement, making it an essential component of the specification.

6.6.5.3. StatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row describes an entry with the 'Value' of '0', named 'Success', which indicates that a command has succeeded. The 'Conformance' field is marked as 'M', meaning this entry is mandatory. This implies that the 'Success' status must always be included and supported within the Channel Cluster's implementation, as it is a fundamental requirement of the Matter specification for this context.

* The table row entry pertains to the "Channel Cluster" within the "Data Types" section and describes a data type named "MultipleMatches," which has a value of '1'. The summary indicates that this data type is used when there is more than one equal match for the ChannelInfoStruct passed in. The conformance rule for "MultipleMatches" is marked as 'M', which stands for Mandatory. This means that the "MultipleMatches" data type is always required to be implemented in any context where the Channel Cluster is used, without any conditions or exceptions.

* In the Channel Cluster's Data Types section, the table row describes an entry with the name "NoMatches," which has a value of '2' and a summary stating "No matches for the ChannelInfoStruct passed in." The conformance rule for this entry is 'M,' which stands for Mandatory. This means that the "NoMatches" element is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

6.6.5.4. ChannelTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row describes a data type with the value '0', named 'Satellite'. This data type indicates that the channel is sourced from a satellite provider. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Satellite' data type is always required to be supported within the Channel Cluster, without any conditions or dependencies.

* In the Channel Cluster's Data Types section, the table row describes a data type with the name "Cable" and a value of '1'. This data type represents a channel that is sourced from a cable provider. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Cable" data type is always required to be supported in any implementation of the Channel Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Channel Cluster's Data Types section, the table row describes a data type with the name "Terrestrial," which has a value of '2' and signifies that the channel is sourced from a terrestrial provider. The conformance rule for this entry is marked as 'M,' indicating that this element is mandatory. This means that the "Terrestrial" data type must always be included and supported in any implementation of the Channel Cluster, without any conditions or exceptions.

* In the context of the Channel Cluster's Data Types, the table row describes an element named "OTT" with a value of '3'. This element signifies that the channel is sourced from an Over-The-Top (OTT) provider. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "OTT" element is always required to be implemented according to the Matter IoT specification, without any conditions or exceptions.

6.6.5.5. ChannelInfoStruct Type
This indicates a channel in a channel lineup.
While the major and minor numbers in the ChannelInfoStruct support use of ATSC channel format,
a lineup MAY use other formats which can map into these numeric values.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Channel Cluster's Data Types section, specifically for an element named "MajorNumber." This element is of the type `uint16`, which indicates it is a 16-bit unsigned integer. The constraint "all" suggests that this data type is applicable universally within its context. The conformance rule for "MajorNumber" is marked as "M," which stands for Mandatory. This means that the "MajorNumber" element is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* The table row describes an entry within the Channel Cluster's Data Types section, specifically for an element named "MinorNumber." This element is of the data type `uint16`, which indicates it is a 16-bit unsigned integer. The constraint "all" suggests that this element is applicable across all relevant scenarios within its context. The conformance rule for "MinorNumber" is marked as "M," meaning it is a Mandatory element. This implies that "MinorNumber" must always be implemented and supported in any device or application utilizing the Channel Cluster, without any exceptions or conditional requirements.

* The table row describes an entry within the Channel Cluster's Data Types section, specifically for an element named "Name" with an ID of '2'. This element is of the type 'string' and has a default value of 'empty'. The conformance rule for this element is 'O', which means it is optional. This indicates that the "Name" element is not required to be implemented and has no dependencies on other features or conditions. Implementers can choose to include this element in their design, but it is not mandatory according to the Matter specification.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '3' named 'CallSign', which is of type 'string' and has a default value of 'empty'. The conformance for 'CallSign' is marked as 'O', indicating that this element is optional. This means that the 'CallSign' attribute is not required to be implemented and has no dependencies on other features or conditions. Implementers have the flexibility to include or exclude this element in their Matter-compliant devices without affecting compliance.

* The table row describes an element within the Channel Cluster's Data Types section, specifically the 'AffiliateCallSign' attribute. This attribute is identified by the ID '4' and is of the 'string' type, with a default value of 'empty'. According to the conformance rule 'O', the 'AffiliateCallSign' is an Optional element. This means that its implementation is not required and there are no dependencies or conditions that mandate its inclusion in the specification. Implementers have the discretion to include or exclude this attribute based on their specific needs or use cases.

* The table row describes an entry within the Channel Cluster, specifically under the Data Types section. The entry is identified by the ID '5' and is named 'Identifier'. It is of the data type 'string' and has a default value of 'empty'. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'Identifier' element is not required to be implemented in devices or systems that utilize the Channel Cluster, and there are no dependencies or conditions that alter this status. Implementers have the discretion to include or exclude this element based on their specific needs or preferences.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '6', named 'Type', which is of the data type 'ChannelTypeEnum' and has a default value of 'empty'. The conformance rule for this element is 'O', which means that the 'Type' element is optional. This indicates that the inclusion of this element is not required and it does not depend on any specific conditions or features being supported. Therefore, implementers have the discretion to include or omit this element in their implementations of the Channel Cluster.

6.6.5.5.1. MajorNumber Field
This field SHALL indicate the channel major number value (for example, using ATSC format). When
the channel number is expressed as a string, such as "13.1" or "256", the major number would be 13
or 256, respectively. This field is required but SHALL be set to 0 for channels such as over-the-top
channels that are not represented by a major or minor number.
6.6.5.5.2. MinorNumber Field
This field SHALL indicate the channel minor number value (for example, using ATSC format). When
the channel number is expressed as a string, such as "13.1" or "256", the minor number would be 1
or 0, respectively. This field is required but SHALL be set to 0 for channels such as over-the-top
channels that are not represented by a major or minor number.
6.6.5.5.3. Name Field
This field SHALL indicate the marketing name for the channel, such as “The CW" or "Comedy Cen
tral". This field is optional, but SHOULD be provided when known.
6.6.5.5.4. CallSign Field
This field SHALL indicate the call sign of the channel, such as "PBS". This field is optional, but
SHOULD be provided when known.
6.6.5.5.5. AffiliateCallSign Field
This field SHALL indicate the local affiliate call sign, such as "KCTS". This field is optional, but
SHOULD be provided when known.
6.6.5.5.6. Identifier Field
This SHALL indicate the unique identifier for a specific channel. This field is optional, but SHOULD
be provided when MajorNumber and MinorNumber are not available.
6.6.5.5.7. Type Field
This SHALL indicate the type or grouping of a specific channel. This field is optional, but SHOULD
be provided when known.
6.6.5.6. LineupInfoStruct Type
The Lineup Info allows references to external lineup sources like Gracenote. The combination of
OperatorName, LineupName, and PostalCode MUST uniquely identify a lineup.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Channel Cluster, specifically in the Data Types section. The element is identified by the ID '0' and is named 'OperatorName', which is of the data type 'string'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'OperatorName' string must always be included and supported in any implementation of the Channel Cluster according to the Matter IoT specification. There are no conditions or exceptions; it is a required component.

* The table row describes an entry within the Channel Cluster, specifically in the Data Types section, for an element named 'LineupName'. This element is of type 'string' and has a default value of 'empty'. The conformance rule for 'LineupName' is marked as 'O', which stands for Optional. This means that the 'LineupName' element is not required to be implemented and has no dependencies on other features or conditions. Implementers of the Channel Cluster can choose to include this element at their discretion, but it is not mandatory for compliance with the Matter specification.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '2' named 'PostalCode'. This element is of the 'string' type and has a default value of 'empty'. According to the conformance rule 'O', the 'PostalCode' element is optional, meaning it is not required and has no dependencies on other features or conditions. This allows implementers the flexibility to include or exclude the 'PostalCode' element in their implementation of the Channel Cluster without any mandatory obligation.

* The table row describes an element within the Channel Cluster, specifically under the Data Types section. The element is identified by the ID '3' and is named 'LineupInfoType', which is of the type 'LineupInfoTypeEnum'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'LineupInfoType' is marked as 'M', which stands for Mandatory. This means that the 'LineupInfoType' element is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

6.6.5.6.1. OperatorName Field
This field SHALL indicate the name of the operator, for example “Comcast”.
6.6.5.6.2. LineupName Field
This field SHALL indicate the name of the provider lineup, for example "Comcast King County". This
field is optional, but SHOULD be provided when known.
6.6.5.6.3. PostalCode Field
This field SHALL indicate the postal code (zip code) for the location of the device, such as "98052".
This field is optional, but SHOULD be provided when known.
6.6.5.6.4. LineupInfoType Field
This field SHALL indicate the type of lineup. This field is optional, but SHOULD be provided when
known.
6.6.5.7. ProgramStruct Type
This indicates a program within an electronic program guide (EPG).

_Table parsed from section 'Data Types':_

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '0', named 'Identifier', which is of the type 'string' and has a constraint of a maximum length of 255 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Identifier' element is always required in the implementation of the Channel Cluster, with no conditions or exceptions. It must be included to comply with the Matter specification for this cluster.

* The table row describes an entry within the Channel Cluster, specifically under the Data Types section. The entry is identified by the ID '1' and is named 'Channel', with a type designated as 'ChannelInfoStruct'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Channel' element, defined as a 'ChannelInfoStruct', is always required to be implemented in any device or application that supports the Channel Cluster according to the Matter specification. There are no conditions or exceptions to this requirement, making it a fundamental component of the Channel Cluster.

* The table row describes an element within the Channel Cluster, specifically under the Data Types section. The element is identified by the ID '2' and is named 'StartTime'. It is of the type 'epoch-s', which likely refers to a timestamp format representing seconds since a defined epoch. The conformance rule for 'StartTime' is marked as 'M', indicating that this element is mandatory. This means that the 'StartTime' data type must always be implemented and supported within the Channel Cluster, with no conditions or exceptions.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '3' named 'EndTime', which is of the type 'epoch-s'. The conformance rule for 'EndTime' is marked as 'M', indicating that this element is mandatory. This means that the 'EndTime' data type must always be implemented and supported within the Channel Cluster, without any conditions or exceptions. It is a required element in the specification, ensuring that any implementation of the Channel Cluster includes this data type.

* The table row describes an element within the Channel Cluster, specifically in the context of Data Types. The element is identified by the ID '4' and is named 'Title'. It is of the 'string' type and has a constraint that limits its maximum length to 255 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Title' element is always required to be implemented in any device or application that supports the Channel Cluster according to the Matter specification. There are no conditions or exceptions to this requirement; it must be present in all cases.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '5', named 'Subtitle'. This element is of the 'string' type and is constrained to a maximum length of 255 characters, with a default value of 'empty'. The conformance rule for 'Subtitle' is marked as 'O', indicating that this element is optional. This means that the inclusion of the 'Subtitle' element is not required and there are no dependencies or conditions that mandate its presence in the implementation.

* The table row describes an attribute within the Channel Cluster, specifically under the Data Types section. The attribute is identified by the ID '6' and is named 'Description'. It is of the type 'string' and has a constraint that limits its maximum length to 8192 characters. The default value for this attribute is an empty string. The conformance rule for this attribute is 'O', which means it is optional. This indicates that the 'Description' attribute is not required to be implemented and does not depend on any other features or conditions within the Matter specification.

* The table row describes an entry for the "AudioLanguages" attribute within the Channel Cluster's Data Types section. This attribute is a list of strings, constrained to a maximum of 10 entries, with each entry being a string of up to 50 characters. The default value for this attribute is an empty list. According to the conformance rule 'O', the "AudioLanguages" attribute is optional, meaning it is not required to be implemented and has no dependencies on other features or conditions. Implementers of the Channel Cluster can choose to include this attribute, but it is not mandatory for compliance with the Matter specification.

* The table row describes an element within the Channel Cluster's Data Types, specifically an attribute named "Ratings." This attribute is a list of strings, with a constraint limiting the list to a maximum of 255 entries. By default, this list is empty. The conformance rule for "Ratings" is marked as "O," indicating that this attribute is optional. This means that the implementation of this attribute is not required and has no dependencies on other features or conditions within the Matter specification. Implementers can choose to include or exclude this attribute based on their specific needs or use cases without affecting compliance with the specification.

* The table row entry describes a data type within the Channel Cluster, specifically the 'ThumbnailUrl'. This data type is a string with a constraint that limits its maximum length to 8192 characters. By default, the 'ThumbnailUrl' is set to an empty string. The conformance rule for this entry is marked as 'O', which means that the 'ThumbnailUrl' is an optional element. It is not required for implementation and has no dependencies on other features or conditions. This allows developers the flexibility to include or exclude this element based on their specific application needs without affecting compliance with the Matter specification.

* The table row describes an attribute named "PosterArtUrl" within the Channel Cluster's Data Types section. This attribute is of the type "string" and has a constraint limiting its maximum length to 8192 characters. Its default value is an empty string. The conformance rule for "PosterArtUrl" is marked as "O," which means this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

* The table row describes a data type within the Channel Cluster, specifically the 'DvbiUrl' attribute. This attribute is of type 'string' and has a constraint limiting its length to a maximum of 8192 characters. Its default value is an empty string. The conformance rule for 'DvbiUrl' is marked as 'O', indicating that this attribute is optional. This means that while it is not required to be implemented in every instance of the Channel Cluster, it can be included at the discretion of the implementer without any dependencies or conditions.

* The table row describes an attribute within the Channel Cluster, specifically in the Data Types section. The attribute is identified by the ID '12' and is named 'ReleaseDate'. It is of the type 'string' and has a constraint that limits its maximum length to 30 characters. The default value for this attribute is 'empty'. The conformance rule for 'ReleaseDate' is marked as 'O', which means this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would alter its optional status.

* The table row describes an entry within the Channel Cluster's Data Types section, specifically for an element named "ParentalGuidanceText." This element is of the type "string" and is constrained to a maximum length of 255 characters, with a default value of an empty string. The conformance rule for "ParentalGuidanceText" is marked as "O," indicating that this element is optional. This means that while it is not required for implementation, it can be included at the discretion of the developer or manufacturer without any dependencies or conditions needing to be met.

* The table row describes an element within the Channel Cluster, specifically in the Data Types section, identified by the ID '14' and named 'RecordingFlag'. This element is of the type 'RecordingFlagBitmap'. The conformance rule for this element is 'RP', which indicates that the 'RecordingFlag' is currently in a provisional state, meaning its status is temporary. The 'P' following the 'R' suggests that while it is provisional now, it is intended to become mandatory in the future. This implies that developers should be aware of its potential future requirement and consider its implementation in anticipation of its mandatory status.

* The table row describes an element within the Channel Cluster, specifically under the Data Types section. The element is identified by the ID '15' and is named 'SeriesInfo', with a type of 'SeriesInfoStruct'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The 'Default' value is 'null', suggesting that there is no default value assigned. The 'Conformance' is labeled as 'O', meaning that the 'SeriesInfo' element is optional and not required, with no dependencies or conditions affecting its inclusion. This means that while it can be included in implementations, there is no obligation to do so, and it is not restricted by any other feature or condition.

* The table row describes an entry within the Channel Cluster's Data Types section, specifically for an element named "CategoryList." This element is a list of type `ProgramCategoryStruct` with a constraint allowing a maximum of 255 entries, and it defaults to being empty. The conformance rule for "CategoryList" is marked as "O," indicating that this element is optional. This means that while the "CategoryList" can be included in implementations of the Channel Cluster, it is not required and has no dependencies or conditions that mandate its inclusion.

_Table parsed from section 'Data Types':_

* The table row describes an entry for the "CastList" within the Channel Cluster's Data Types section. The "CastList" is identified by the ID '17' and is a data type defined as a list of "ProgramCastStruct" with a maximum constraint of 255 entries. By default, this list is empty. The conformance rule for "CastList" is marked as 'O', which means that this element is optional. It is not required to be implemented and has no dependencies on other features or conditions. This allows implementers the flexibility to include or exclude the "CastList" based on their specific application needs without affecting compliance with the Matter specification.

* The table row describes an element within the Channel Cluster's Data Types section, specifically an attribute named "ExternalIDList." This attribute is a list of type "AdditionalInfoStruct" with a constraint allowing a maximum of 255 entries. By default, this list is empty. The conformance rule for "ExternalIDList" is marked as "O," indicating that this attribute is optional. This means that the attribute is not required to be implemented and does not have any dependencies or conditions that would make it mandatory. Implementers have the flexibility to include or exclude this attribute based on their specific needs or use cases.

6.6.5.7.1. Identifier Field
This field SHALL indicate a unique identifier for a program within an electronic program guide list.
The identifier SHALL be unique across multiple channels.
6.6.5.7.2. Channel Field
This field SHALL indicate the channel associated to the program.
6.6.5.7.3. StartTime Field
This field SHALL indicate an epoch time in seconds indicating the start time of a program, as a UTC
time. This field can represent a past or future value.
6.6.5.7.4. EndTime Field
This field SHALL indicate an epoch time in seconds indicating the end time of a program, as a UTC
time. This field can represent a past or future value but SHALL be greater than the StartTime.
6.6.5.7.5. Title Field
This field SHALL indicate the title or name for the specific program. For example, “MCIS: Los Ange
les”.
6.6.5.7.6. Subtitle Field
This field SHALL indicate the subtitle for the specific program. For example, “Maybe Today" which
is an episode name for “MCIS: Los Angeles”. This field is optional but SHALL be provided if applica
ble and known.
6.6.5.7.7. Description Field
This field SHALL indicate the brief description for the specific program. For example, a description
of an episode. This field is optional but SHALL be provided if known.
6.6.5.7.8. AudioLanguages Field
This field SHALL indicate the audio language for the specific program. The value is a string contain
ing one of the standard Tags for Identifying Languages RFC 5646. This field is optional but SHALL
be provided if known.
6.6.5.7.9. Ratings Field
This field SHALL be used for indicating the level of parental guidance recommended for of a partic
ular program. This can be any rating system used in the country or region where the program is
broadcast. For example, in the United States “TV-PG” may contain material that parents can find not
suitable for younger children but can be accepted in general for older children. This field is
optional but SHALL be provided if known.
6.6.5.7.10. ThumbnailUrl Field
This field SHALL represent a URL of a thumbnail that clients can use to render an image for the
program. The syntax of this field SHALL follow the syntax as specified in RFC 1738 and SHALL use
https
the   scheme.
6.6.5.7.11. PosterArtUrl Field
This field SHALL represent a URL of a poster that clients can use to render an image for the pro
gram on the detail view. The syntax of this field SHALL follow the syntax as specified in RFC 1738
https
and SHALL use the   scheme.
6.6.5.7.12. DvbiUrl Field
This field SHALL represent the DVB-I URL associated to the program. The syntax of this field SHALL
https
follow the syntax as specified in RFC 1738 and SHALL use the   scheme.
6.6.5.7.13. ReleaseDate Field
This field SHALL be a string, in ISO 8601 format, representing the date on which the program was
released. This field is optional but when provided, the year SHALL be provided as part of the string.
6.6.5.7.14. ParentalGuidanceText Field
This field SHALL represent a string providing additional information on the parental guidance. This
field is optional.
6.6.5.7.15. RecordingFlag Field
This field SHALL represent the recording status of the program. This field is required if the Record
Program feature is set.
6.6.5.7.16. SeriesInfo Field
This field SHALL represent the information of a series such as season and episode number. This
field is optional but SHOULD be provided if the program represents a series and this information is
available.
6.6.5.7.17. CategoryList Field
This field SHALL represent the category of a particular program. This field is optional but SHALL be
provided if known.
6.6.5.7.18. CastList Field
This field SHALL represent a list of the cast or the crew on the program. A single cast member may
have more than one role. This field is optional but SHALL be provided if known.
6.6.5.7.19. ExternalIDList Field
This field SHALL indicate the list of additional external content identifiers.
6.6.5.8. ProgramCategoryStruct Type
This object defines the category associated to a program.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Channel Cluster's Data Types section, specifically focusing on an element named "Category." This element is of the type "string" and is constrained to a maximum length of 256 characters. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Category" element is always required to be implemented in any system or device that supports the Channel Cluster, without any conditions or exceptions.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '1' named 'SubCategory'. This element is of the 'string' type and has a constraint limiting its maximum length to 256 characters. Its default value is specified as 'empty'. The conformance rule for 'SubCategory' is marked as 'O', indicating that this element is optional. This means that while it is not required to be implemented, it can be included at the discretion of the developer without any dependencies or conditions.

6.6.5.8.1. Category Field
This field SHALL represent the category or genre of the program. Ex. News.
6.6.5.8.2. SubCategory Field
This field SHALL represent the sub-category or sub-genre of the program. Ex. Local.
6.6.5.9. SeriesInfoStruct Type
This object provides the episode information related to a program.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row describes an element with the ID '0' named 'Season', which is of the type 'string' and is constrained to a maximum length of 256 characters. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'Season' data type must always be implemented and supported within the Channel Cluster, without any conditions or exceptions.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '1' named 'Episode'. This element is of the 'string' type and has a constraint that limits its maximum length to 256 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Episode' element is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

6.6.5.9.1. Season Field
This field SHALL represent the season of the series associated to the program.
6.6.5.9.2. Episode Field
This field SHALL represent the episode of the program.
6.6.5.10. ProgramCastStruct Type
This object provides the cast information related to a program.

_Table parsed from section 'Data Types':_

* In the context of the Channel Cluster's Data Types, the table row describes an element with the ID '0', named 'Name', which is of the type 'string' and has a constraint of a maximum length of 256 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Name' element is always required to be implemented in any device or application that uses the Channel Cluster according to the Matter specification. There are no conditions or exceptions; it must be present and adhere to the specified constraints.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '1' named 'Role', which is of type 'string' and has a constraint limiting its maximum length to 256 characters. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'Role' element must always be implemented and supported in any device or application using the Channel Cluster, without any conditions or exceptions.

6.6.5.10.1. Name Field
This field SHALL represent the name of the cast member.
6.6.5.10.2. Role Field
This field SHALL represent the role of the cast member. Ex. Actor, Director.
6.6.5.11. PageTokenStruct Type
This object defines the pagination structure.

_Table parsed from section 'Data Types':_

* In the Channel Cluster's Data Types section, the table row describes an element named "Limit" with an ID of '0'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint labeled as 'all', indicating it applies universally within its context. The default value for "Limit" is '0'. The conformance rule for this element is 'O', which stands for Optional. This means that the "Limit" element is not required to be implemented and has no dependencies or conditions that would necessitate its inclusion in the specification.

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '1', named 'After', which is of type 'string' and has a constraint of a maximum length of 8192 characters. The default value for this element is an empty string. The conformance rule for this element is 'O', meaning it is optional. This indicates that the 'After' element is not required to be implemented and has no dependencies on other features or conditions within the Matter specification. Implementers have the flexibility to include or exclude this element as they see fit, without affecting compliance with the specification.

* In the context of the Channel Cluster's Data Types, the table row describes an element with the ID '2', named 'Before'. It is of the type 'string' and has a constraint that limits its maximum length to 8192 characters. The default value for this element is 'empty'. The conformance rule for 'Before' is marked as 'O', which means that this element is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status according to the Matter specification.

6.6.5.11.1. Limit Field
This field SHALL indicate the maximum number of entries that should be retrieved from the pro
gram guide in a single response. It allows clients to specify the size of the paginated result set based
on their needs.
6.6.5.11.2. After Field
This field SHALL indicate the cursor that pinpoints the start of the upcoming data page. In a Cursor-
based pagination system, the field acts as a reference point, ensuring the set of results corresponds
directly to the data following the specified cursor. In a Offset-based pagination system, the field,
along with limit, indicate the offset from which entries in the program guide will be retrieved.
6.6.5.11.3. Before Field
This field SHALL indicate the cursor that pinpoints the end of the upcoming data page. In a Cursor-
based pagination system, the field acts as a reference point, ensuring the set of results corresponds
directly to the data preceding the specified cursor. In a Offset-based pagination system, the field,
along with limit, indicate the offset from which entries in the program guide will be retrieved.
6.6.5.12. ChannelPagingStruct Type
This object defines the paging structure that includes the previous and next pagination tokens.

_Table parsed from section 'Data Types':_

* In the Channel Cluster's Data Types section, the table row describes an element with the ID '0' named 'PreviousToken', which is of the type 'PageTokenStruct'. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed within the current specification. The 'Default' value is 'null', suggesting that if it were allowed, it would default to null. The 'Conformance' field is marked as 'O', meaning that under normal circumstances, this element would be optional, with no dependencies or conditions requiring its inclusion. However, given the 'Quality' is 'X', the element is not permitted in any implementation of the specification.

* The table row describes an element within the Channel Cluster, specifically in the Data Types section, with the ID '1' and the name 'NextToken'. This element is of the type 'PageTokenStruct' and has a default value of 'null'. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed. The 'Conformance' field is marked as 'O', meaning that the 'NextToken' element is optional and not required to be implemented, with no dependencies or conditions affecting its optional status. Therefore, while it can be included in implementations, it is not necessary to do so.

6.6.5.12.1. PreviousToken Field
This field SHALL indicate the token to retrieve the preceding page. Absence of this field denotes the
response as the initial page.
6.6.5.12.2. NextToken Field
This field SHALL indicate the token to retrieve the next page. Absence of this field denotes the
response as the last page.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Channel Cluster, specifically the "ChannelList" attribute. This attribute is identified by the ID '0x0000' and is of the type 'list[ChannelInfoStruct]', with a default value of 'empty'. It has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'CL', which means that the attribute is mandatory if the feature 'CL' (likely representing a specific capability or condition within the Channel Cluster) is supported. If the 'CL' feature is not supported, the attribute is not required. This conformance rule ensures that the "ChannelList" attribute is only included when relevant to the device's capabilities.

* The table row describes an attribute named "Lineup" within the Channel Cluster's Attributes section. This attribute has an ID of '0x0001' and is of the type 'LineupInfoStruct'. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is marked as 'X', meaning that this attribute is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The 'Conformance' field is marked as 'LI', which implies that the attribute is mandatory if the feature 'LI' (Lineup) is supported. In summary, the "Lineup" attribute is not allowed in the current specification, and its conformance is contingent upon the support of the 'LI' feature.

* In the Channel Cluster, under the Attributes section, the entry for 'CurrentChannel' with ID '0x0002' is of type 'ChannelInfoStruct'. The 'Constraint' is described elsewhere in the documentation, and the 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in certain contexts. The 'Default' value is 'null', and it has 'Read' and 'View' access permissions. The 'Conformance' is marked as 'O', meaning that the 'CurrentChannel' attribute is optional. This indicates that while it is not required to implement this attribute, it can be included at the discretion of the developer without any dependencies or conditions.

6.6.6.1. ChannelList Attribute
This attribute SHALL provide the list of supported channels.
6.6.6.2. Lineup Attribute
This attribute SHALL identify the channel lineup using external data sources.
6.6.6.3. CurrentChannel Attribute
This attribute SHALL contain the current channel. When supported but a channel is not currently
tuned to (if a content application is in foreground), the value of the field SHALL be null.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Channel Cluster, specifically the "ChangeChannel" command, which is directed from the client to the server and expects a "ChangeChannelResponse" in return. The access level for this command is optional, indicated by 'O'. The conformance rule 'CL | LI' specifies that the "ChangeChannel" command is mandatory if either the feature 'CL' (Channel List) or 'LI' (Lineup) is supported. In simpler terms, if a device supports either the Channel List or Lineup feature, it must implement the ChangeChannel command; otherwise, it is not required.

* The table row describes a command within the Channel Cluster, specifically the "ChangeChannelResponse" command, which is directed from the server to the client. The 'Response' field indicates that this command does not require a response. The 'Conformance' field, specified as 'CL | LI', means that the "ChangeChannelResponse" command is mandatory if either the 'CL' feature or the 'LI' feature is supported. In other words, the command must be implemented if the device supports either of these features, ensuring compatibility with devices that have channel-related functionalities or specific implementations that require this command.

* The table row describes a command within the Channel Cluster, specifically the "ChangeChannelByNumber" command. This command is directed from the client to the server, and it requires a response from the server, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', meaning that access to this command is optional. The 'Conformance' field is marked 'M', indicating that the "ChangeChannelByNumber" command is mandatory. This means that any implementation of the Channel Cluster must include this command, as it is a required element without any conditional dependencies or exceptions.

* In the context of the Channel Cluster's Commands section, the table row describes the "SkipChannel" command, identified by the ID '0x03'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level is optional ('Access: O'), meaning it is not required to be implemented by default. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "SkipChannel" command must always be implemented in any device that supports the Channel Cluster, without any conditions or exceptions.

* The table row describes a command within the Channel Cluster, specifically the "GetProgramGuide" command, which is identified by the ID '0x04'. This command is directed from the client to the server and expects a response in the form of a "ProgramGuideResponse". The access level for this command is marked as optional ('O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'EG', indicating that the command is mandatory if the feature 'EG' is supported. If the feature 'EG' is not supported, the command is not required. This entry specifies the conditions under which the "GetProgramGuide" command must be implemented in a device that supports the Channel Cluster.

* The table row describes a command within the Channel Cluster, specifically the "ProgramGuide Response" command, which is identified by the ID '0x05'. This command is sent from the server to the client, as indicated by the direction "client ⇐ server". The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked as 'EG', which, according to the Matter Conformance Interpretation Guide, means that the command is mandatory if the feature 'EG' is supported. Therefore, if a device supports the 'EG' feature, it must implement the "ProgramGuide Response" command; otherwise, the command is not required.

* The table row describes a command named "RecordProgram" within the Channel Cluster, which is directed from the client to the server and requires a response. The access level for this command is optional, meaning it is not required and has no dependencies. The conformance rule "RP & EG" indicates that the "RecordProgram" command is mandatory if both the "RP" (Record Program) feature and the "EG" (Electronic Guide) feature are supported. If either of these features is not supported, the command is not mandatory. This conformance rule ensures that the command is only required in environments where both relevant features are available, aligning with the capabilities of the device or system implementing the Matter specification.

* The table row describes a command named "CancelRecordProgram" within the Channel Cluster, specifically in the context of commands exchanged from client to server. The command has an ID of '0x07' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'RP & EG' indicates that the "CancelRecordProgram" command is mandatory if both the features 'RP' and 'EG' are supported. In other words, the command must be implemented if the device supports both of these features, otherwise, it is not required.

6.6.7.1. ChangeChannel Command
Change the channel to the channel case-insensitive exact matching the value passed as an argu
ment.
The match priority order SHALL be: Identifier, AffiliateCallSign, CallSign, Name, Number. In the
match string, the Channel number should be presented in the "Major.Minor" format, such as "13.1".
Upon receipt, this SHALL generate a ChangeChannelResponse command.
Upon success, the CurrentChannel attribute, if supported, SHALL be updated to reflect the change.

_Table parsed from section 'Commands':_

* The table row describes a command named "Match" within the Channel Cluster's Commands section. The command has an ID of '0' and is of the type 'string'. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "Match" command is always required to be implemented in any device or application that supports the Channel Cluster, with no exceptions or conditional requirements.

6.6.7.1.1. Match Field
This field SHALL contain a user-input string to match in order to identify the target channel.
6.6.7.2. ChangeChannelResponse Command
This command SHALL be generated in response to a ChangeChannel command.

_Table parsed from section 'Commands':_

* In the Channel Cluster, under the Commands section, there is an entry for a command named "Status" with an ID of '0'. This command is of the type 'StatusEnum', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "Status" command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* In the context of the Channel Cluster's Commands section, the table row describes an element with the ID '1' named 'Data', which is of the type 'string' and has no specific constraints on its value ('any'). The conformance rule for this element is 'O', which means that the 'Data' command is optional. This indicates that the inclusion of this command is not required and does not depend on any other features or conditions. Devices implementing the Channel Cluster can choose to support this command, but they are not obligated to do so according to the Matter specification.

6.6.7.2.1. Status Field
This field SHALL indicate the status of the command which resulted in this response.
6.6.7.2.2. Data Field
This field SHALL indicate Optional app-specific data.
6.6.7.3. ChangeChannelByNumber Command
Change the channel to the channel with the given Number in the ChannelList attribute.

_Table parsed from section 'Commands':_

* In the Channel Cluster, under the Commands section, the table row describes an element with the ID '0' named 'MajorNumber'. This element is of type 'uint16', which means it is a 16-bit unsigned integer, and it has a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for 'MajorNumber' is 'M', which stands for Mandatory. This means that the 'MajorNumber' command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* In the context of the Channel Cluster's Commands section, the table row describes an element with the ID '1' named 'MinorNumber', which is of type 'uint16' and applies to all constraints. The conformance rule for 'MinorNumber' is denoted by 'M', which means that this element is mandatory. It is always required to be implemented according to the Matter specification, without any conditions or exceptions. This ensures that any device or implementation supporting the Channel Cluster must include the 'MinorNumber' command as a fundamental component.

6.6.7.3.1. MajorNumber Field
This field SHALL indicate the channel major number value (ATSC format) to which the channel
should change.
6.6.7.3.2. MinorNumber Field
This field SHALL indicate the channel minor number value (ATSC format) to which the channel
should change.
6.6.7.4. SkipChannel Command
This command provides channel up and channel down functionality, but allows channel index
jumps of size Count.
When the value of the increase or decrease is larger than the number of channels remaining in the
given direction, then the behavior SHALL be to return to the beginning (or end) of the channel list
and continue. For example, if the current channel is at index 0 and count value of -1 is given, then
the current channel should change to the last channel.

_Table parsed from section 'Commands':_

* In the Channel Cluster, under the Commands section, there is a command named "Count" with an ID of '0'. This command is of type 'int16' and applies universally, as indicated by the 'Constraint' being 'all'. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Count" command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

6.6.7.4.1. Count Field
This field SHALL indicate the number of steps to increase (Count is positive) or decrease (Count is
negative) the current channel.
6.6.7.5. GetProgramGuide Command
This command retrieves the program guide. It accepts several filter parameters to return specific
schedule and program information from a content app. The command shall receive in response a
ProgramGuideResponse. Standard error codes SHALL be used when arguments provided are not
valid. For example, if StartTime is greater than EndTime, the status code INVALID_ACTION SHALL
be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Channel Cluster, specifically the "StartTime" command. This command is identified by the ID '0' and is of the type 'epoch-s', which likely refers to a timestamp format. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "StartTime" command is always required to be implemented in any device or application that supports the Channel Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, indicating its fundamental role in the functionality of the Channel Cluster.

* The table row describes a command within the Channel Cluster, specifically the "EndTime" command. This command is identified by the ID '1' and is of the type 'epoch-s', which likely refers to a timestamp format. The conformance rule for this command is marked as 'M', meaning it is Mandatory. This indicates that the "EndTime" command is always required to be implemented in any device or application that supports the Channel Cluster, with no exceptions or conditions.

* The table row describes a command within the Channel Cluster, specifically the 'ChannelList' command, which is identified by ID '2'. This command is of the type 'list[ChannelInfoStruct]', meaning it consists of a list of structures that provide information about channels, with a constraint that the list can contain a maximum of 255 entries. By default, this list is empty. The conformance rule for 'ChannelList' is marked as 'O', indicating that this command is optional. This means that the implementation of this command is not required and has no dependencies on other features or conditions within the Matter specification.

* In the Channel Cluster, under the Commands section, the table entry describes a command named "PageToken" with an ID of '3' and a type of 'PageTokenStruct'. The 'Quality' of this command is marked as 'X', indicating that it is explicitly disallowed within the current specification. The 'Default' value for this command is 'null'. The 'Conformance' field is marked as 'O', which means that this command is optional and not required to be implemented, with no dependencies or conditions affecting its optional status. However, given the 'Quality' is 'X', this command should not be implemented as it is not allowed.

* The table row describes a command named "RecordingFlag" within the Channel Cluster, specifically in the Commands section. This command has an ID of '5' and is of the type 'RecordingFlagBitmap'. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed. The 'Default' value is 'null', meaning there is no default value specified. The 'Conformance' field is marked as 'O', which means that the "RecordingFlag" command is optional. This implies that the implementation of this command is not required and has no dependencies, allowing developers the flexibility to include it or not based on their specific application needs.

* In the Channel Cluster's Commands section, the table row describes the 'ExternalIDList' command, which is identified by ID '6'. This command is of the type 'list[AdditionalInfoStruct]' and is constrained to a maximum of 255 entries, with an empty list as its default value. The conformance rule for 'ExternalIDList' is marked as 'O', indicating that this command is optional. This means that implementing this command is not required and it has no dependencies on other features or conditions within the Matter specification.

* In the Channel Cluster's Commands section, the table row describes a command identified by ID '7', named 'Data', which is of type 'octstr' with a constraint of a maximum length of 8092. The default value for this command is 'MS'. The conformance rule for this command is 'O', indicating that it is optional. This means that the 'Data' command is not required to be implemented in devices supporting the Channel Cluster, and there are no dependencies or conditions that would make it mandatory. Devices can choose to implement this command based on their specific needs or use cases.

6.6.7.5.1. StartTime Field
This field SHALL indicate the beginning of the time window for which program guide entries are to
be retrieved, as a UTC time. Entries with a start time on or after this value will be included in the
results.
6.6.7.5.2. EndTime Field
This field SHALL indicate the end of the time window for which program guide entries are to be
retrieved, as a UTC time. Entries with an end time on or before this value will be included in the
results. This field can represent a past or future value but SHALL be greater than the StartTime.
6.6.7.5.3. ChannelList Field
This field SHALL indicate the set of channels for which program guide entries should be fetched. By
providing a list of channels in this field, the response will only include entries corresponding to the
specified channels.
6.6.7.5.4. PageToken Field
This field SHALL indicate the pagination token used for managing pagination progression.
6.6.7.5.5. RecordingFlag Field
This field SHALL indicate the flags of the programs for which entries should be fetched.
6.6.7.5.6. ExternalIDList Field
This field SHALL indicate the list of additional external content identifiers.
6.6.7.5.7. Data Field
This field SHALL indicate Optional app-specific data.
6.6.7.6. ProgramGuideResponse Command
This command is a response to the GetProgramGuide command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Channel Cluster, specifically the "Paging" command, which is identified by the ID '0' and is of the type 'ChannelPagingStruct'. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Paging" command is always required to be implemented in any device or application that supports the Channel Cluster according to the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental and non-negotiable part of the Channel Cluster's functionality.

* In the Channel Cluster, under the Commands section, the table row describes an element with the ID '1' named 'ProgramList'. This element is of the type 'list[ProgramStruct]' and has a default value of 'empty'. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Channel Cluster. There are no conditions or dependencies affecting its requirement status; it must be present in all cases.

6.6.7.6.1. Paging Field
This field SHALL indicate the necessary pagination attributes that define information for both the
succeeding and preceding data pages.
6.6.7.6.2. ProgramList Field
This field SHALL indicate the list of programs.
6.6.7.7. RecordProgram Command
Record a specific program or series when it goes live. This functionality enables DVR recording fea
tures.

_Table parsed from section 'Commands':_

* The table row describes a command within the Channel Cluster, specifically the "ProgramIdentifier" command. This command is of type "string" and is constrained to a maximum length of 255 characters. The conformance rule for this command is marked as "M," which means it is mandatory. This indicates that the "ProgramIdentifier" command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* The table row describes a command within the Channel Cluster, specifically named "ShouldRecordSeries," which is of the boolean type. According to the conformance rule 'M', this command is mandatory. This means that any implementation of the Channel Cluster must include the "ShouldRecordSeries" command as a required feature, with no exceptions or conditions. It is an essential part of the specification and must be supported in all cases.

* The table row describes a command named "ExternalIDList" within the Channel Cluster's Commands section. This command is of the type "list[AdditionalInfoStruct]" and is constrained to a maximum of 255 entries, with an empty list as its default value. The conformance rule for this command is marked as "O," indicating that it is Optional. This means that the "ExternalIDList" command is not required to be implemented and has no dependencies or conditions that would necessitate its inclusion. Implementers have the discretion to include this command based on their specific needs or use cases.

* The table row describes a command within the Channel Cluster, specifically identified by the ID '3' and named 'Data'. This command is of the type 'octstr', which indicates it is an octet string, and it has a constraint limiting its maximum size to 8092 octets. The default value for this command is 'MS'. According to the conformance rule 'O', this command is optional, meaning it is not required to be implemented and has no dependencies on other features or conditions. Therefore, developers have the discretion to include or exclude this command in their implementation of the Channel Cluster without any mandatory obligation.

6.6.7.7.1. ProgramIdentifier Field
This field SHALL indicate the program identifier for the program that should be recorded. This
value is provided by the identifier field in ProgramStruct.
6.6.7.7.2. ShouldRecordSeries Field
This field SHALL indicate whether the whole series associated to the program should be recorded.
For example, invoking record program on an episode with that flag set to true, the target should
schedule record the whole series.
6.6.7.7.3. ExternalIDList Field
This field, if present, SHALL indicate the list of additional external content identifiers.
6.6.7.7.4. Data Field
This field, if present, SHALL indicate app-specific data.
6.6.7.8. CancelRecordProgram Command
Cancel recording for a specific program or series.

_Table parsed from section 'Commands':_

* The table row describes a command within the Channel Cluster, specifically the "ProgramIdentifier" command. This command is of the type "string" and has a constraint that limits its maximum length to 255 characters. The conformance rule for this command is marked as "M," which stands for Mandatory. This means that the "ProgramIdentifier" command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* In the context of the Channel Cluster, specifically within the Commands section, the table row describes a command named "ShouldRecordSeries" with an ID of '1' and a data type of 'bool' (boolean). The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "ShouldRecordSeries" command is always required to be implemented in any device or application that supports the Channel Cluster, without any conditions or exceptions.

* The table row describes a command named "ExternalIDList" within the Channel Cluster's Commands section. This command is of the type "list[AdditionalInfoStruct]" and is constrained to a maximum of 255 entries, with an empty list as its default value. The conformance rule for "ExternalIDList" is marked as "O," which means this command is optional. It is not required to be implemented and has no dependencies on other features or conditions within the Matter specification.

* In the Channel Cluster's Commands section, the table row describes a command identified by ID '3' named 'Data'. This command is of type 'octstr', which indicates it is an octet string, and it has a constraint limiting its maximum size to 8092 bytes. The default value for this command is 'MS'. The conformance rule for this command is 'O', meaning it is optional. This indicates that the implementation of this command is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this command based on their specific needs or preferences.

6.6.7.8.1. ProgramIdentifier Field
This field SHALL indicate the program identifier for the program that should be cancelled from
recording. This value is provided by the identifier field in ProgramStruct.
6.6.7.8.2. ShouldRecordSeries Field
This field SHALL indicate whether the whole series associated to the program should be cancelled
from recording. For example, invoking record program on an episode with that flag set to true, the
target should schedule record the whole series.
6.6.7.8.3. ExternalIDList Field
This field, if present, SHALL indicate the list of additional external content identifiers.
6.6.7.8.4. Data Field
This field, if present, SHALL indicate app-specific data.