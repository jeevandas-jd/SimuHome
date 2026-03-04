
# 6.7 Content Launcher Cluster

This cluster provides an interface for launching content on a Video Player device such as a Stream
ing Media Player, Smart TV or Smart Screen.
This cluster would be supported on a Video Player device or devices that can playback content,
such as a Streaming Media Player, Smart TV or Smart Screen. This cluster supports playing back
content referenced by URL. It supports finding content by type and global identifier, and either
playing the content or displaying the search results.
The cluster server for Content Launcher is implemented by an endpoint that can launch content,
such as a Video Player, or an endpoint representing a Content App on such a device.
When this cluster is implemented for an Content App Endpoint (Endpoint with type “Content App”
and having an Application Basic cluster), the Video Player device SHALL launch the application
when a client invokes the LaunchContent or LaunchURL commands.

## Data Types
6.7.5.1. SupportedProtocolsBitmap Type
This data type is derived from map32.

_Table parsed from section 'Data Types':_

* In the context of the Content Launcher Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '0' and named 'DASH'. This feature indicates that the device supports Dynamic Adaptive Streaming over HTTP (DASH), a protocol for streaming media over the internet. The conformance rule for this feature is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate whether the DASH feature is mandatory, optional, provisional, deprecated, or disallowed, possibly with conditions based on other supported features. Since no conformance string is given, further documentation would need to be consulted to determine the specific requirements for implementing DASH in this context.

Device supports Dynamic Adap

_Table parsed from section 'Data Types':_

* The table row entry describes a feature within the Content Launcher Cluster, specifically under the Data Types section. It identifies a feature named "HLS," which indicates that the device supports HTTP Live Streaming (HLS). The 'Bit' value of '1' suggests that this feature is represented by a specific bit in a data structure, likely a bitmap or flag indicating support for HLS. However, the conformance rule for this entry is not explicitly provided in the data. Therefore, without a specific conformance string, we cannot determine the exact requirements or conditions under which this feature must be supported. Typically, such a feature would be marked as Mandatory, Optional, or subject to other conditions as described in the conformance interpretation guide, but this information is missing in the provided data.

6.7.5.2. StatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the table entry describes a data type with the value '0' named 'Success', which indicates that a command has succeeded. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that the 'Success' data type must always be implemented and supported in any device or application that utilizes the Content Launcher Cluster, as it is a fundamental requirement of the Matter specification.

* In the Content Launcher Cluster, under the Data Types section, the entry with the value '1' is named 'URLNotAvailable'. This entry indicates that the requested URL could not be reached by the device. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'URLNotAvailable' data type is a required element in the specification and must always be implemented in any device or application that utilizes the Content Launcher Cluster. There are no conditions or dependencies affecting its mandatory status.

* In the Content Launcher Cluster, under the Data Types section, the table row describes an entry with the value '2' and the name 'AuthFailed'. This entry indicates that a requested URL has returned a 401 error code, which typically signifies an authentication failure. The conformance rule for this entry is marked as 'M', meaning that the 'AuthFailed' data type is mandatory. This implies that any implementation of the Content Launcher Cluster must include this data type, as it is a required element of the specification.

* The table row entry pertains to the "Content Launcher Cluster" within the "Data Types" section, specifically focusing on a value labeled '3' named 'TextTrackNotAvailable'. This entry indicates a scenario where the requested text track, as specified in PlaybackPreferences, is not available. The conformance rule 'TT' implies that this element is mandatory if the feature 'TT' (presumably representing a Text Track-related feature) is supported. In essence, if the device or implementation supports the 'TT' feature, then the 'TextTrackNotAvailable' value must be included and recognized as part of the system's capabilities.

* In the Content Launcher Cluster, under the Data Types section, the entry with the value '4' is named 'AudioTrackNotAvailable'. This entry indicates that the requested audio track specified in PlaybackPreferences is not available. The conformance rule for this entry is 'AT', meaning it is mandatory if the feature 'AT' is supported. If the feature 'AT' is not supported, this entry is not required. This conformance condition ensures that the 'AudioTrackNotAvailable' status is included in implementations where the 'AT' feature is present, reflecting its relevance in those contexts.

6.7.5.3. ParameterEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the table row describes a data type with the value '0' and the name 'Actor'. This data type represents an actor credited in video media content, such as "Gaby Hoffman". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Actor' data type is always required to be implemented in any system or application that conforms to the Matter specification for this cluster. There are no conditions or exceptions; it must be included as part of the implementation.

* In the Content Launcher Cluster, under the Data Types section, there is an entry with the value '1' named 'Channel'. This entry represents the identifying data for a television channel, such as "PBS". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Channel' data type is always required in any implementation of the Content Launcher Cluster according to the Matter specification. There are no conditions or dependencies affecting its necessity; it must be included in all cases.

* In the Content Launcher Cluster, under the Data Types section, the table row describes an element with the name "Character" and a value of '2'. This element represents a character depicted in video media content, such as "Snow White". The conformance rule for this element is 'M', which stands for Mandatory. This means that the "Character" element is always required to be implemented in any system or application that adheres to the Matter specification for this cluster. There are no conditions or exceptions; it must be included as part of the implementation.

* In the Content Launcher Cluster, under the Data Types section, the table row describes an entry with the value '3' and the name 'Director'. This entry represents a data type used to specify the director of video media content, such as "Spike Lee". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Director' data type is always required in any implementation of the Content Launcher Cluster according to the Matter specification. There are no conditions or exceptions; it must be included to comply with the standard.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster's Data Types section, the table row describes a data type with the value '4' named 'Event'. This data type represents a reference to various types of events, such as sports or music, and is used in contexts like searching for specific event entities, such as "Football games." The conformance rule for this entry is 'M', which means that the 'Event' data type is mandatory. It is always required to be implemented in any system or application that adheres to the Matter specification for this cluster, ensuring that event-related functionalities are consistently supported.

* The table row describes a data type within the Content Launcher Cluster, specifically named "Franchise," which is assigned the value '5'. This data type represents a video entity that can encompass a collection of related video content, such as movies or TV shows, under a common franchise, like the fictional "Intergalactic Wars." This allows for user requests to search for all content related to a franchise rather than a single title. The conformance rule 'M' indicates that this data type is mandatory, meaning it is always required to be supported within the Content Launcher Cluster according to the Matter IoT specification.

* The table row entry pertains to the "Content Launcher Cluster" within the "Data Types" section and describes a data type named "Genre," which is represented by the value '6'. This data type is used to specify the genre of video media content, such as action, drama, or comedy. The conformance rule for "Genre" is marked as 'M', which stands for Mandatory. This means that the "Genre" data type is always required to be implemented in any device or application that supports the Content Launcher Cluster, with no exceptions or conditions.

* In the Content Launcher Cluster, under the Data Types section, the table row describes a data type with the value '7' named 'League'. This data type is used to represent categorical information related to a sporting league, such as "NCAA". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'League' data type is always required to be implemented in any system or device that supports the Content Launcher Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, within the Data Types section, there is an entry for a data type named "Popularity," which is represented by the value '8'. This data type is summarized as indicating whether the user is asking for popular content. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Content Launcher Cluster. There are no conditions or exceptions to this requirement, making "Popularity" an essential component of the cluster's functionality.

* In the Content Launcher Cluster, under the Data Types section, the entry for 'Provider' with a value of '9' refers to the media service provider (MSP) that a user selects for media playback, such as "Netflix." The conformance rule for this entry is 'M,' which means that the 'Provider' element is mandatory. This indicates that it is always required to be implemented within the Content Launcher Cluster, ensuring that the system can specify the desired media service provider for content playback.

* In the Content Launcher Cluster, under the Data Types section, the entry for 'Sport' with a value of '10' represents categorical information related to sports, such as football. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Sport' data type is always required to be implemented within the Content Launcher Cluster, with no conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, the table entry for 'SportsTeam' with a value of '11' represents categorical information about a professional sports team, such as "University of Washington Huskies." The conformance rule for this entry is 'M,' which stands for Mandatory. This means that the 'SportsTeam' data type is always required to be implemented in any system or device that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, the entry for 'Type' with a value of '12' specifies the type of content being requested. The supported content types include "Movie", "MovieSeries", "TVSeries", "TVSeason", "TVEpisode", "Trailer", "SportsEvent", "LiveEvent", and "Video". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Type' data element is always required and must be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, there is an entry for a data type named 'Video', which is identified by the value '13'. This data type is used to represent the identifying data for a specific piece of video content, such as the title "Manchester by the Sea". The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Video' data type is always required in any implementation of the Content Launcher Cluster, with no exceptions or conditions.

* In the Content Launcher Cluster, under the Data Types section, the entry for 'Season' with a value of '14' represents the specific season number within a TV series. The conformance rule for this entry is 'O', which means that the 'Season' element is optional. This indicates that while the element can be included in implementations, it is not required and has no dependencies on other features or conditions. Implementers have the flexibility to decide whether or not to include this element in their applications.

* In the Content Launcher Cluster, under the Data Types section, the entry for 'Episode' with a value of '15' represents a specific episode number within a season of a TV series. The conformance rule for this entry is 'O', which means that the 'Episode' element is optional. This indicates that while the element can be included in implementations, it is not required and has no dependencies on other features or conditions. Therefore, developers have the flexibility to include or exclude this element based on their specific application needs without affecting compliance with the Matter specification.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the entry with the value '16' and the name 'Any' represents a data type that allows for a search text input across various parameter types, including those not explicitly defined within the existing parameter types. The conformance rule for this entry is 'O', which means that the 'Any' data type is optional. It is not required for implementation and does not have any dependencies or conditions that affect its inclusion. This provides flexibility for developers to include this data type if it suits their application needs, but it is not a mandatory component of the specification.

6.7.5.4. MetricTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the table row describes a data type with the value '0' named 'Pixels'. This data type is summarized as defining dimensions in terms of a number of pixels. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Pixels' data type is always required to be implemented in any system or device that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, the table row entry describes a data type named "Percentage," which is used to define dimensions as a percentage. The conformance rule for this entry is marked as "M," indicating that this data type is mandatory. This means that the "Percentage" data type is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

6.7.5.4.1. Pixels Value
This value is used for dimensions defined in a number of Pixels.
6.7.5.4.2. Percentage Value
This value is for dimensions defined as a percentage of the overall display dimensions. For exam
ple, if using a Percentage Metric type for a Width measurement of 50.0, against a display width of
1920 pixels, then the resulting value used would be 960 pixels (50.0% of 1920) for that dimension.
Whenever a measurement uses this Metric type, the resulting values SHALL be rounded ("floored")
towards 0 if the measurement requires an integer final value.
6.7.5.5. AdditionalInfoStruct Type
This object defines additional name=value pairs that can be used for identifying content.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, there is an entry with the ID '0' named 'Name', which is of the type 'string' and has a constraint of a maximum length of 256 characters. The conformance rule for this entry is 'M', which means that the 'Name' attribute is mandatory. This implies that it is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, there is an entry with the ID '1' named 'Value', which is of type 'string' and has a constraint of a maximum length of 8192 characters. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Value' attribute is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

6.7.5.5.1. Name Field
This field SHALL indicate the name of external id, ex. "musicbrainz".
6.7.5.5.2. Value Field
This field SHALL indicate the value for external id, ex. "ST0000000666661".
6.7.5.6. ParameterStruct Type
This object defines inputs to a search for content for display or playback.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, there is an entry for an element with the ID '0' named 'Type', which is of the 'ParameterEnum' type and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Type' element is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions. The 'all' constraint suggests that this parameter can take any value within its defined enumeration.

* In the Content Launcher Cluster, under the Data Types section, there is an entry for an element with the ID '1' named 'Value'. This element is of the type 'string' and has a constraint that limits its maximum length to 1024 characters. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Value' element is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* The table row describes an element within the Content Launcher Cluster, specifically under the Data Types section. The element is identified by the ID '2' and is named 'ExternalIDList'. It is of the type 'list[AdditionalInfoStruct]', indicating that it is a list composed of structures defined as 'AdditionalInfoStruct'. The constraint 'all' suggests that all entries in this list must adhere to certain unspecified conditions, and its default state is 'empty', meaning it starts with no entries. The conformance rule for 'ExternalIDList' is marked as 'O', which means this element is optional. It is not required for the implementation of the Content Launcher Cluster and has no dependencies or conditions that would mandate its inclusion.

6.7.5.6.1. Type Field
This field SHALL indicate the entity type.
6.7.5.6.2. Value Field
This field SHALL indicate the entity value, which is a search string, ex. “Manchester by the Sea”.
6.7.5.6.3. ExternalIDList Field
This field SHALL indicate the list of additional external content identifiers.
6.7.5.7. ContentSearchStruct Type
This object defines inputs to a search for content for display or playback.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Content Launcher Cluster, specifically in the Data Types section. The entry is for an element named "ParameterList," which is of the type "list[ParameterStruct]" and has a constraint labeled as "all," with a default value of "0." The conformance rule for this element is "M," indicating that "ParameterList" is a mandatory element. This means that it is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

6.7.5.7.1. ParameterList Field
This field SHALL indicate the list of parameters comprising the search. If multiple parameters are
provided, the search parameters SHALL be joined with 'AND' logic. e.g. action movies with Tom
Cruise will be represented as [{Actor: 'Tom Cruise'}, {Type: 'Movie'}, {Genre: 'Action'}]
6.7.5.8. DimensionStruct Type
This object defines dimension which can be used for defining Size of background images.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Content Launcher Cluster's Data Types section, specifically for an element named "Width." This element is of the type "double" and has a default value labeled as "MS." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Width" element is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* The table row entry describes an attribute named "Height" within the Content Launcher Cluster, specifically under the Data Types section. The attribute is of the type "double" and has a default value labeled as "MS." The conformance rule for this attribute is marked as "M," which stands for Mandatory. This means that the "Height" attribute is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, the table entry with ID '2' refers to an element named 'Metric', which is of the type 'MetricTypeEnum'. The conformance rule for this element is marked as 'M', indicating that it is mandatory. This means that the 'Metric' element is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

6.7.5.8.1. Width Field
This field SHALL indicate the width using the metric defined in Metric
6.7.5.8.2. Height Field
This field SHALL indicate the height using the metric defined in Metric
6.7.5.8.3. Metric Field
This field SHALL indicate metric used for defining Height/Width.
6.7.5.9. StyleInformationStruct Type
This object defines style information which can be used by content providers to change the Media
Player’s style related properties.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the entry for 'ImageURL' is a data type with an ID of '0'. It is defined as a string with a maximum constraint of 8192 characters and a default value of 'MS'. The conformance for 'ImageURL' is marked as 'O', indicating that this element is optional. This means that the 'ImageURL' attribute is not required to be implemented and does not have any dependencies or conditions that would make it mandatory in any context. Implementers have the discretion to include this attribute based on their specific needs or use cases.

* In the Content Launcher Cluster, under the Data Types section, there is an entry for an attribute named "Color" with an ID of '1'. This attribute is of the type 'string' and has a constraint that limits its length to between 7 and 9 characters. The default value for this attribute is 'MS'. According to the conformance rule, the attribute "Color" is marked as 'O', which means it is optional. This indicates that the implementation of this attribute is not required and does not depend on any other features or conditions. Implementers have the flexibility to include or exclude this attribute based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the Content Launcher Cluster, under the Data Types section, there is an entry for an attribute named "Size" with an ID of '2'. This attribute is of the type 'DimensionStruct' and has a default value of 'MS'. According to the conformance rule, the 'Size' attribute is marked as 'O', which means it is optional. This indicates that the inclusion of the 'Size' attribute is not required and there are no dependencies or conditions that mandate its presence in the implementation of the Content Launcher Cluster.

6.7.5.9.1. ImageURL Field
This field SHALL indicate the URL of image used for Styling different Video Player sections like
Logo, Watermark etc. The syntax of this field SHALL follow the syntax as specified in RFC 1738 and
https
SHALL use the   scheme.
6.7.5.9.2. Color Field
This field SHALL indicate the color, in RGB or RGBA, used for styling different Video Player sections
like Logo, Watermark, etc. The value SHALL conform to the 6-digit or 8-digit format defined for CSS
sRGB hexadecimal color notation [ ]. Examples:
https://www.w3.org/TR/css-color-4/#hex-notation
• #76DE19 for R=0x76, G=0xDE, B=0x19, A absent
• #76DE1980 for R=0x76, G=0xDE, B=0x19, A=0x80
6.7.5.9.3. Size Field
This field SHALL indicate the size of the image used for Styling different Video Player sections like
Logo, Watermark etc.
6.7.5.10. BrandingInformationStruct Type
This object defines Branding Information which can be provided by the client in order to customize
the skin of the Video Player during playback.

_Table parsed from section 'Data Types':_

* In the Content Launcher Cluster, under the Data Types section, the table row describes an element with the ID '0' named 'ProviderName'. This element is of the type 'string' and has a constraint that limits its maximum length to 256 characters. The conformance rule for 'ProviderName' is marked as 'M', which means it is a Mandatory element. This indicates that the 'ProviderName' attribute must always be implemented and supported in any device or application that uses the Content Launcher Cluster, without any conditions or exceptions.

* The table row describes an element within the Content Launcher Cluster, specifically in the Data Types section. The element is identified by the ID '1' and is named 'Background'. It is of the type 'StyleInformationStruct' and has a default value of 'MS'. The conformance rule for this element is 'O', which means it is optional. This indicates that the 'Background' element is not required to be implemented and has no dependencies on other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this element based on their specific needs or preferences.

* In the Content Launcher Cluster, within the Data Types section, there is an entry for an element named "Logo" with an ID of '2'. This element is of the type 'StyleInformationStruct' and has a default value of 'MS'. According to the conformance rule specified as 'O', the "Logo" element is optional. This means that it is not required to be implemented and has no dependencies on other features or conditions. Implementers have the flexibility to include or exclude this element in their design without affecting compliance with the Matter specification.

* In the Content Launcher Cluster, under the Data Types section, there is an entry for a data type named 'ProgressBar' with an ID of '3'. This data type is of the type 'StyleInformationStruct' and has a default value of 'MS'. The conformance rule for 'ProgressBar' is marked as 'O', which means that this element is optional. It is not required to be implemented and does not have any dependencies or conditions that would change its optional status. Therefore, developers have the discretion to include or exclude this element in their implementation of the Content Launcher Cluster without affecting compliance with the Matter specification.

* In the Content Launcher Cluster, under the Data Types section, the table row with ID '4' refers to an element named 'Splash', which is of the type 'StyleInformationStruct' and has a default value of 'MS'. The conformance rule for this element is marked as 'O', indicating that it is optional. This means that the 'Splash' element is not required to be implemented and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this element in their Matter-compliant devices without affecting compliance.

* The table row describes an entry for the "WaterMark" attribute within the Content Launcher Cluster, specifically under the Data Types section. This attribute is of the type "StyleInformationStruct" and has a default value of "MS." The conformance rule for this attribute is marked as "O," which means it is optional. This indicates that the "WaterMark" attribute is not required to be implemented and does not have any dependencies or conditions that would make it mandatory. Implementers have the discretion to include this attribute in their devices or applications, but it is not a necessity according to the Matter specification.

6.7.5.10.1. ProviderName Field
This field SHALL indicate name of the provider for the given content.
6.7.5.10.2. Background Field
This field SHALL indicate background of the Video Player while content launch request is being
processed by it. This background information MAY also be used by the Video Player when it is in
idle state.
6.7.5.10.3. Logo Field
This field SHALL indicate the logo shown when the Video Player is launching. This is also used
when the Video Player is in the idle state and Splash field is not available.
6.7.5.10.4. ProgressBar Field
This field SHALL indicate the style of progress bar for media playback.
6.7.5.10.5. Splash Field
This field SHALL indicate the screen shown when the Video Player is in an idle state. If this prop
erty is not populated, the Video Player SHALL default to logo or the provider name.
6.7.5.10.6. Watermark Field
This field SHALL indicate watermark shown when the media is playing.
6.7.5.11. PlaybackPreferencesStruct Type
PlaybackPreferencesStruct defines the preferences sent by the client to the receiver in the Content
Launcher LaunchURL or LaunchContent commands.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Content Launcher Cluster, specifically under the Data Types section. The entry is for an element named "PlaybackPosition," which is of type `uint64`. The "Quality" field is marked as "X," indicating that this element is explicitly disallowed and should not be implemented or used. The "Conformance" field is labeled as "AS," which does not directly match any of the basic conformance tags or logical conditions outlined in the guide. Therefore, the conformance rule for "PlaybackPosition" is not clearly defined within the provided guide, suggesting that further documentation or context is needed to fully understand its intended use or restrictions. However, given the "Quality" is "X," it is clear that "PlaybackPosition" is not permitted in this context.

* The table row entry pertains to the "TextTrack" element within the "Content Launcher Cluster" under the "Data Types" section. It is identified by the ID '1' and is of the type 'TrackPreferenceStruct'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The 'Conformance' field is specified as 'TT', which means that the element is mandatory if the feature 'TT' is supported. In this context, the 'TextTrack' element is required only when the 'TT' feature is present; otherwise, it is not applicable due to its disallowed status.

* In the Content Launcher Cluster, under the Data Types section, the entry with ID '2' is named 'AudioTracks' and is of the type 'list[TrackPreferenceStruct]'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The 'Conformance' field is labeled 'AT', meaning that the presence of the 'AudioTracks' element is mandatory if the feature 'AT' is supported. If 'AT' is not supported, this element is not required. This entry specifies that the 'AudioTracks' list is only applicable when the 'AT' feature is part of the device's capabilities, and otherwise, it should not be included.

6.7.5.11.1. PlaybackPosition Field
This field SHALL indicate the preferred position (in milliseconds) in the media to launch playback
from. In case the position falls in the middle of a frame, the server SHALL set the position to the
SampledPosition
beginning of that frame and set the   attribute on the MediaPlayback cluster accord
ingly. A value of null SHALL indicate that playback position is not applicable for the current state of
the media playback. (For example : Live media with no known duration and where seek is not sup
ported).
6.7.5.11.2. TextTrack Field
This field SHALL indicate the user’s preferred Text Track. A value of null SHALL indicate that the
user did not specify a preferred Text Track on the client. In such a case, the decision to display and
select a Text Track is up to the server.
6.7.5.11.3. AudioTracks Field
This field SHALL indicate the list of the user’s preferred Audio Tracks. If the list contains multiple
values, each AudioTrack must also specify a unique audioOutputIndex to play the track on. A value
of null SHALL indicate that the user did not specify a preferred Audio Track on the client. In such a
case, the decision to play and select an Audio Track is up to the server.
6.7.5.12. TrackPreferenceStruct Type
This structure defines Text/Audio Track preferences.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Content Launcher Cluster, specifically under the Data Types section. The entry is for an attribute named "LanguageCode," which is of the type "string" and has a constraint limiting its maximum length to 32 characters. The conformance rule for "LanguageCode" is marked as "M," indicating that this attribute is Mandatory. This means that the "LanguageCode" attribute is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Data Types section, the table row describes an element named "Characteristics" with an ID of '1'. This element is of the type 'list[CharacteristicEnum]', indicating it is a list composed of enumerated characteristic values. The 'Quality' is marked as 'X', which means this element is explicitly disallowed in terms of quality. The default value for this element is 'null'. The 'Conformance' for this element is 'O', which signifies that the "Characteristics" element is optional. This means that while it is not required to implement this element, it can be included without any dependencies or conditions.

* The table row entry describes an element within the Content Launcher Cluster, specifically in the Data Types section. The element is named 'AudioOutputIndex' and is of type 'uint8'. Its quality is marked as 'X', indicating that it is explicitly disallowed in the current specification. The conformance rule 'AT' suggests that the element is mandatory if the feature 'AT' is supported. However, since the quality is 'X', the element 'AudioOutputIndex' is not allowed regardless of any conditions or features, overriding any potential conformance rules.

6.7.5.12.1. LanguageCode Field
This field SHALL contain one of the standard Tags for Identifying Languages RFC 5646, which iden
tifies the primary language used in the Track.
6.7.5.12.2. Characteristics Field
This field SHALL contain a list of enumerated CharacteristicEnum values that indicate a purpose,
trait or feature associated with the Track. A value of null SHALL indicate that there are no Charac
teristics corresponding to the Track.
6.7.5.12.3. AudioOutputIndex Field
This field if present SHALL indicate the index of the OutputInfoStruct from the OutputList attribute
(from the AudioOutput cluster) and indicates which audio output the Audio Track should be played
on.
This field SHALL NOT be present if the track is not an audio track.
If the track is an audio track, this field MUST be present. A value of null SHALL indicate that the
server can choose the audio output(s) to play the Audio Track on.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "AcceptHeader" within the Content Launcher Cluster, identified by the ID '0x0000'. This attribute is a list of strings, with each string having a maximum length of 1024 characters, and the entire list can contain up to 100 entries. The "AcceptHeader" attribute is non-reportable (indicated by 'N' in the Quality field), has a default value of an empty list, and is accessible for reading and viewing (denoted by 'R V' in the Access field). The conformance rule 'UP' indicates that the attribute is currently provisional ('P'), meaning its status is temporary and subject to change. The 'U' part of the conformance is not defined in the provided guide, suggesting it might be a placeholder or specific to a particular context not covered in the basic rules. Therefore, the attribute is not yet mandatory but may become so in the future, depending on further specification updates.

* The table row describes an attribute within the Content Launcher Cluster, specifically the "SupportedStreamingProtocols" attribute. This attribute has an ID of '0x0001' and is of the type 'SupportedProtocolsBitmap'. It is marked with a quality of 'N', indicating it is non-reportable, and has a default value of '0'. The access level is 'R V', meaning it is readable and can be viewed. The conformance rule 'UP' indicates that the attribute is currently provisional, with the expectation that it will become mandatory in the future. This means that while it is not currently required, it is anticipated to be a necessary component in later versions of the specification.

6.7.6.1. AcceptHeader Attribute
This attribute SHALL provide a list of content types supported by the Video Player or Content App
in the form of entries in the HTTP "Accept" request header.
6.7.6.2. SupportedStreamingProtocols Attribute
This attribute SHALL provide information about supported streaming protocols.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Launcher Cluster, specifically the "LaunchContent" command, which is directed from the client to the server. The command's response is "LauncherResponse," and it has an access level marked as "Optional" (O), indicating that the command is not required and has no dependencies. The conformance rule for this command is "CS," which means it is mandatory if the feature or condition represented by "CS" is supported. In the context of the Matter specification, this implies that the "LaunchContent" command must be implemented if the specific feature or condition "CS" is present in the device or application. Otherwise, the command is not required.

* The table row describes a command within the Content Launcher Cluster, specifically the "LaunchURL" command, which is directed from the client to the server and expects a "LauncherResponse" in return. The access level for this command is optional, indicated by 'O'. The conformance rule 'UP' signifies that the "LaunchURL" command is currently provisional, meaning its status is temporary and subject to change. The 'P' indicates that it is expected to become mandatory in the future, as denoted by the 'M' that typically follows a provisional status. Therefore, while it is not currently required, it is anticipated that support for this command will become mandatory in subsequent versions of the specification.

* The table row describes a command within the Content Launcher Cluster, specifically the "LauncherResponse" command, which is identified by the ID '0x02'. This command is directed from the server to the client, as indicated by the direction "client ⇐ server". The 'Response' field marked as 'N' suggests that this command does not require a response. The conformance rule 'CS | UP' indicates that the "LauncherResponse" command is mandatory if either the 'CS' feature or the 'UP' feature is supported. In simpler terms, if a device supports either the 'CS' or 'UP' feature, it must implement the "LauncherResponse" command; otherwise, it is not required.

6.7.7.1. LaunchContent Command
Upon receipt, this SHALL launch the specified content with optional search criteria.
This command returns a Launch Response.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Launcher Cluster, specifically the "Search" command, which is of the type "ContentSearchStruct." The "Constraint" field is marked as "desc," indicating that the constraints for this command are detailed elsewhere in the documentation. The "Conformance" field is marked as "M," meaning that the "Search" command is mandatory. This implies that any implementation of the Content Launcher Cluster must include the "Search" command as a required feature, with no conditions or exceptions.

* In the Content Launcher Cluster, under the Commands section, the table row describes a command with the ID '1' named 'AutoPlay'. This command is of the boolean type, and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'AutoPlay' is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Commands section, there is an entry for a command named "Data" with an ID of '2'. This command is of the type 'string' and has a default value of 'MS'. The conformance rule for this command is marked as 'O', which means it is Optional. This indicates that the "Data" command is not required to be implemented in all instances of the Content Launcher Cluster, and there are no specific dependencies or conditions that mandate its inclusion. Implementers have the discretion to include this command based on their specific needs or use cases.

* In the Content Launcher Cluster, under the Commands section, the table row describes a command with the ID '3' named 'PlaybackPreferences', which is of the type 'PlaybackPreferencesStruct'. The 'Constraint' is listed as 'all', indicating that this command applies universally within the specified context. The 'Default' value is 'MS', though its specific meaning is not detailed in the provided data. The 'Conformance' field is marked as 'O', which means that the 'PlaybackPreferences' command is optional. This indicates that implementing this command is not required and there are no dependencies or conditions that affect its optional status.

* The table row describes a command within the Content Launcher Cluster, specifically the "UseCurrentContext" command. This command is of type boolean and has a default value of TRUE, with its constraints described elsewhere in the documentation. The conformance rule for this command is marked as "O," indicating that it is optional. This means that the implementation of the "UseCurrentContext" command is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this command in their devices without affecting compliance with the Matter specification.

6.7.7.1.1. Search Field
This field SHALL indicate the content to launch.
6.7.7.1.2. AutoPlay Field
This field SHALL indicate whether to automatically start playing content, where:
• TRUE means best match should start playing automatically.
• FALSE means matches should be displayed on screen for user selection.
6.7.7.1.3. Data Field
This field, if present, SHALL indicate app-specific data.
6.7.7.1.4. PlaybackPreferences Field
This field, if present, SHALL indicate the user’s preferred Text/AudioTracks and playbackPosition
for the media, sent from the client to the server. If the server does not find an available track for
the title being played exactly matching a Track requested here, in the list of available tracks, it may
default to picking another track that closely matches the requested track. Alternately, it may go with
user preferences set on the server side (it will use this option if these PlaybackPreferences are not
specified). In the case of text tracks, that may mean that the subtitle text is not displayed at all. In
the cases where the preferred Text/AudioTracks are not available, the server SHALL return the
TextTrackNotAvailable and/or AudioTrackNotAvailable Status(es) in the LauncherResponse.
6.7.7.1.5. UseCurrentContext Field
This field, if present, SHALL indicate whether to consider the context of current ongoing activity on
the receiver to fulfill the request. For example if the request only includes data in ContentSearch
that specifies an Episode number, and UseCurrentContent is set to TRUE, if there is a TV series on
going, the request refers to the specific episode of the ongoing season of the TV series. TRUE means
current activity context MAY be considered FALSE means current activity context SHALL NOT be
considered
6.7.7.2. LaunchURL Command
Upon receipt, this SHALL launch content from the specified URL.
The content types supported include those identified in the AcceptHeader and SupportedStreaming
Protocols attributes.
A check SHALL be made to ensure the URL is secure (uses HTTPS).
When playing a video stream in response to this command, an indication (ex. visual) of the identity
of the origin node of the video stream SHALL be provided. This could be in the form of a friendly
name label which uniquely identifies the node to the user. This friendly name label is typically
assigned by the Matter Admin (ex. TV) at the time of commissioning and, when it’s a device, is often
editable by the user. It might be a combination of a company name and friendly name, for example,
”Acme” or “Acme Streaming Service on Alice’s Phone”.
This command returns a Launch Response.

_Table parsed from section 'Commands':_

* In the Content Launcher Cluster, within the Commands section, there is an entry for a command with the ID '0' named 'ContentURL'. This command is of the type 'string' and has no specific constraints on its value, indicated by 'any'. The conformance rule for this command is 'M', which means it is mandatory. This implies that the 'ContentURL' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Content Launcher Cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

* The table row describes a command named "DisplayString" within the Content Launcher Cluster, specifically in the Commands section. This command has an ID of '1' and is of the 'string' type with no specific constraints on its value, allowing any string input. The default value for this command is 'MS'. The conformance rule for "DisplayString" is marked as 'O', which means that this command is optional. It is not required to be implemented and does not have any dependencies or conditions that would change its optional status.

_Table parsed from section 'Commands':_

* The table row describes a command named "BrandingInformation" within the Content Launcher Cluster, specifically in the Commands section. This command has an ID of '2' and is of the type 'BrandingInformationStruct'. The 'Constraint' is listed as 'any', indicating there are no specific constraints on its use, and the 'Default' is 'MS'. The 'Conformance' for this command is marked as 'O', meaning it is optional. This indicates that the implementation of the "BrandingInformation" command is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this command in their devices without affecting compliance with the Matter specification.

* In the Content Launcher Cluster, under the Commands section, the table row describes a command with the ID '3' named 'PlaybackPreferences', which is of the type 'PlaybackPreferencesStruct'. The 'Constraint' is set to 'any', and the default value is 'MS'. The 'Conformance' for this command is marked as 'O', meaning it is optional. This indicates that the 'PlaybackPreferences' command is not required to be implemented and has no dependencies on other features or conditions. Implementers have the flexibility to include or exclude this command based on their specific needs or preferences without affecting compliance with the Matter specification.

6.7.7.2.1. ContentURL Field
This field SHALL indicate the URL of content to launch. The syntax of this field SHALL follow the
https
syntax as specified in RFC 1738 and SHALL use the   scheme.
6.7.7.2.2. DisplayString Field
This field, if present, SHALL provide a string that MAY be used to describe the content being
accessed at the given URL.
6.7.7.2.3. BrandingInformation Field
This field, if present, SHALL indicate the branding information that MAY be displayed when playing
back the given content.
6.7.7.2.4. PlaybackPreferences Field
This field, if present, SHALL indicate the user’s preferred Text/AudioTracks and playbackPosition
for the media, sent from the client to the server. If the server does not find an available track for
the title being played exactly matching a Track requested here, in the list of available tracks, it may
default to picking another track that closely matches the requested track. Alternately, it may go with
user preferences set on the server side (it will use this option if these PlaybackPreferences are not
specified). In the case of text tracks, that may mean that the subtitle text is not displayed at all. In
the cases where the preferred Text/AudioTracks are not available, the server SHALL return the
TextTrackNotAvailable and/or AudioTrackNotAvailable Status(es) in the LauncherResponse.
6.7.7.3. LauncherResponse Command
This command SHALL be generated in response to LaunchContent and LaunchURL commands.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Launcher Cluster, specifically the "Status" command. This command is identified by the ID '0' and is of the type 'StatusEnum', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Status" command is always required to be implemented in any device or application that supports the Content Launcher Cluster, without any conditions or exceptions.

* In the Content Launcher Cluster, under the Commands section, there is an entry for a command identified by 'ID' 1, named 'Data', which is of the 'string' type and has a default value of 'MS'. The conformance for this command is marked as 'O', meaning it is optional. This indicates that the 'Data' command is not required to be implemented and has no dependencies on other features or conditions. Implementers have the flexibility to include or exclude this command in their device's functionality without affecting compliance with the Matter specification.

6.7.7.3.1. Status Field
This field SHALL indicate the status of the command which resulted in this response.
6.7.7.3.2. Data Field
This field SHALL indicate Optional app-specific data.