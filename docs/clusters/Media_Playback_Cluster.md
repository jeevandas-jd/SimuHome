
# 6.10 Media Playback Cluster

This cluster provides an interface for controlling Media Playback (PLAY, PAUSE, etc) on a media
device such as a TV, Set-top Box, or Smart Speaker.
This cluster server would be supported on Video Player devices or endpoints that provide media
playback, such as a Content App. This cluster provides an interface for controlling Media Playback.

## Data Types
6.10.5.1. PlaybackStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Media Playback Cluster, under the Data Types section, the table row describes a data type with the value '0' and the name 'Playing'. This data type indicates that the media is currently playing, which includes states such as fast forward (FF) and rewind (REW). The conformance rule for this entry is 'M', meaning that this data type is mandatory. It is always required to be implemented in any device or application that supports the Media Playback Cluster, ensuring that the 'Playing' state is consistently recognized and handled across all compliant devices.

* In the Media Playback Cluster, under the Data Types section, the table row describes a data type with the value '1' named 'Paused', which indicates that the media is currently paused. The conformance rule for this entry is 'M', meaning that this element is mandatory. It must always be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the context of the Media Playback Cluster, the table row describes a data type with the value '2', named 'NotPlaying', which indicates that media is not currently playing. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that within the Media Playback Cluster, the 'NotPlaying' data type must always be implemented and supported, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the table row describes a data type with the value '3', named 'Buffering'. This data type indicates that media is not currently buffering and playback will commence once the buffer is adequately filled. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Buffering' data type is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

6.10.5.2. StatusEnum Type
Status Data Type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Media Playback Cluster, under the Data Types section, the table row describes a data type with the value '0', named 'Success', which summarizes the outcome as 'Succeeded'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Success' data type must always be implemented and supported within the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the entry for 'InvalidStateForCommand' with a value of '1' indicates a specific condition where a requested playback command is deemed invalid due to the current playback state. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'InvalidStateForCommand' data type must always be implemented and supported in any device or application that conforms to the Matter specification for the Media Playback Cluster. There are no conditions or exceptions to this requirement; it is an essential element that must be present.

* In the Media Playback Cluster, under the Data Types section, the entry with the value '2' is named 'NotAllowed'. This entry signifies a scenario where a requested playback command cannot be executed due to the current playback state, such as trying to fast-forward during a commercial. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'NotAllowed' data type must always be implemented and supported in any device or application that adheres to the Matter specification for the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the table row entry describes a data type with the value '3' named 'NotActive'. The summary indicates that this data type signifies that the endpoint is not currently active for playback. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'NotActive' data type is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* The table row pertains to the "Media Playback Cluster" within the "Data Types" section, specifically describing a value labeled "SpeedOutOfRange" with a value of '4'. This entry indicates a condition where a FastForward or Rewind command is issued, but the media is already playing at the maximum speed supported by the server in that direction. The conformance rule for this entry is 'VS', which is not directly explained in the provided conformance guide. However, typically in Matter specifications, 'VS' might refer to a vendor-specific condition, suggesting that the implementation of this feature is dependent on the specific vendor's design and is not universally mandated or optional across all implementations. Therefore, the presence and behavior of this feature may vary depending on the vendor's implementation of the Media Playback Cluster.

* In the Media Playback Cluster, under the Data Types section, the entry for 'SeekOutOfRange' with a value of '5' indicates a specific condition where the Seek Command was issued with a position value outside the permissible seek range of the media. The conformance rule 'AS' implies that this element is mandatory when the feature or condition represented by 'AS' is supported. If 'AS' is not supported, the conformance rule does not apply, and the element is not required. This ensures that the system appropriately handles seek commands that exceed the media's allowed range when the relevant feature is active.

6.10.5.3. CharacteristicEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Media Playback Cluster, under the Data Types section, the entry for 'ForcedSubtitles' has a value of '0' and is described as textual information intended for display when no other text representation is selected. This feature is used to clarify dialogue, alternate languages, texted graphics, or location/person IDs not covered in the dubbed or localized audio. The conformance rule for 'ForcedSubtitles' is marked as 'M', which means it is mandatory. This indicates that the 'ForcedSubtitles' feature is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the entry 'DescribesVideo' is identified by the value '1'. It represents a media component that provides a textual or audio description of a visual component, intended for audio synthesis or as an audio description. The conformance rule for 'DescribesVideo' is marked as 'M', which means it is mandatory. This indicates that the 'DescribesVideo' feature is always required to be implemented in any device or application that supports the Media Playback Cluster, ensuring that such descriptions are consistently available across all compliant implementations.

* In the Media Playback Cluster, under the Data Types section, the entry for 'EasyToRead' with a value of '2' represents a feature that provides simplified or reduced captions, as specified in the United States Code Title 47 CFR 79.103(c)(9). The conformance rule 'M' indicates that this feature is mandatory, meaning it is always required to be implemented in any device or application that supports the Media Playback Cluster. This ensures that all compliant devices provide this accessibility feature, enhancing usability for users who benefit from simplified captions.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the Media Playback Cluster within the Data Types section, specifically describing a media characteristic named "FrameBased" with a value of '3'. This characteristic indicates that a track selection option includes frame-based content. The conformance rule for "FrameBased" is marked as 'M', which stands for Mandatory. This means that the "FrameBased" characteristic is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the entry with the value '4' and the name 'MainProgram' refers to the main media component(s) that are intended for presentation when no other information is provided. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'MainProgram' element is always required and must be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row entry pertains to the Media Playback Cluster within the context of Data Types. It describes a data type named "OriginalContent," which is identified by the value '5'. This data type signifies a media characteristic that indicates a track or media selection option contains original content. The conformance rule for "OriginalContent" is marked as 'M', meaning it is mandatory. This indicates that the "OriginalContent" data type is always required to be implemented in any system or device that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row entry pertains to the "VoiceOverTranslation" data type within the Media Playback Cluster, specifically under the Data Types section. This data type is characterized by the value '6' and is summarized as a media feature that indicates a track or media selection option includes a language translation and verbal interpretation of spoken dialogue. The conformance rule for "VoiceOverTranslation" is marked as 'M', which stands for Mandatory. This means that the feature is always required to be implemented in any device or application that supports the Media Playback Cluster, ensuring that the capability to handle media with voice-over translations is consistently available.

* In the Media Playback Cluster, under the Data Types section, the entry for 'Caption' is identified by the value '7'. This entry represents a textual media component designed to provide transcriptions of spoken dialogue and auditory cues, such as sound effects and music, specifically for the hearing impaired. The conformance rule for 'Caption' is marked as 'M', which means it is a mandatory element. This indicates that the 'Caption' feature is always required to be implemented in any device or application that supports the Media Playback Cluster, ensuring accessibility for users who are hearing impaired.

* In the Media Playback Cluster, under the Data Types section, the entry for 'Subtitle' with a value of '8' represents the feature that provides textual transcriptions of spoken dialog. The conformance rule for this entry is marked as 'M', which means that the 'Subtitle' feature is mandatory. This indicates that any implementation of the Media Playback Cluster must include support for subtitles, ensuring that this feature is always available and cannot be omitted.

* In the Media Playback Cluster, under the Data Types section, the entry describes a data type named "Alternate" with a value of '9'. This data type represents a textual media component that includes transcriptions of spoken dialogue and auditory cues, such as sound effects and music, specifically designed for the hearing impaired. The conformance rule for this entry is 'M', which means that the "Alternate" data type is mandatory. This indicates that it is always required to be implemented in any device or application that supports the Media Playback Cluster, ensuring accessibility features for users with hearing impairments.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Media Playback Cluster, specifically in the context of Data Types. The entry is identified by the name "Supplementary" and is assigned the value "10". It represents a media content component that is supplementary to another media content component of a different type. The conformance rule for this entry is marked as "M", which stands for Mandatory. This means that the "Supplementary" data type is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, there is an entry for a data type named "Commentary" with a value of '11'. This data type represents an experience that includes commentary, such as a director's commentary, which is typically audio. The conformance rule for this entry is 'M', indicating that the "Commentary" data type is mandatory. This means that any implementation of the Media Playback Cluster must include support for this data type, as it is always required according to the Matter specification.

* The table row entry pertains to the "Media Playback Cluster" within the "Data Types" section, specifically focusing on a data type named "DubbedTranslation." This data type is identified by the value '12' and is summarized as an experience that includes elements presented in a different language than the original, such as dubbed audio or translated captions. The conformance rule for "DubbedTranslation" is marked as 'M', which stands for Mandatory. This means that within the context of the Matter specification, the "DubbedTranslation" data type is always required to be implemented in any device or application that supports the Media Playback Cluster. There are no conditions or exceptions to this requirement, making it an essential component for compliance with the specification.

* In the Media Playback Cluster, under the Data Types section, the entry for 'Description' with a value of '13' represents a media component that provides a textual or audio description. This description is intended for audio synthesis or to describe a visual component, enhancing accessibility for users. The conformance rule 'M' indicates that this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Media Playback Cluster. This ensures that all implementations provide this essential accessibility feature.

* The table row entry describes a data type within the Media Playback Cluster, specifically named "Metadata," which has a value of '14'. This data type serves as a media component designed to hold information that application-specific elements can process. The conformance rule for this entry is marked as 'M', indicating that the "Metadata" element is mandatory. This means it is always required to be implemented in any system or application that uses the Media Playback Cluster, without any conditions or exceptions.

* The table row describes a data type within the Media Playback Cluster, specifically named "EnhancedAudioIntelligibility," which is identified by the value '15'. This data type is designed to enhance the intelligibility of dialogue in media playback, improving the listening experience. According to the conformance rule 'M', this feature is mandatory, meaning it is always required to be implemented in any device or application that supports the Media Playback Cluster. There are no conditions or dependencies affecting its requirement status; it must be included in all relevant implementations.

_Table parsed from section 'Data Types':_

* In the Media Playback Cluster, under the Data Types section, there is an entry for a value labeled 'Emergency' with a numerical identifier of '16'. This entry describes an experience designed to convey crucial information about an ongoing emergency, aiming to protect life, health, safety, and property, and may include vital instructions on responding to the emergency. The conformance rule for this entry is 'M', indicating that the 'Emergency' feature is mandatory. This means it is a required element within the Media Playback Cluster and must be implemented in all devices or systems that support this cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, there is an entry for a data type named "Karaoke" with a value of '17'. This data type provides a textual representation of a song's lyrics, typically in the same language as the song, as specified by the SMPTE ST 2067-2 standard. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Karaoke" data type is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

6.10.5.4. PlaybackPositionStruct Type
This structure defines a playback position within a media stream being played.

_Table parsed from section 'Data Types':_

* The table row entry describes an element within the Media Playback Cluster, specifically under the Data Types section. The element is identified by the ID '0' and is named 'UpdatedAt'. It is of the type 'epoch-us', which likely refers to a timestamp format in microseconds since the epoch. The 'Constraint' is listed as 'all', indicating that this element applies universally within its context. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'UpdatedAt' element is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'Position', which is of type 'uint64' and has a constraint labeled 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', meaning that the 'Position' element is mandatory and always required within this context. This implies that any implementation of the Media Playback Cluster must include the 'Position' element as a necessary component, regardless of any other conditions or features.

6.10.5.4.1. UpdatedAt Field
This field SHALL indicate the time when the position was last updated.
6.10.5.4.2. Position Field
This field SHALL indicate the associated discrete position within the media stream, in milliseconds
from the beginning of the stream, being associated with the time indicated by the UpdatedAt field.
The Position SHALL NOT be greater than the duration of the media if duration is specified. The Posi
tion SHALL NOT be greater than the time difference between current time and start time of the
media when start time is specified.
A value of null SHALL indicate that playback position is not applicable for the current state of the
media playback (For example : Live media with no known duration and where seek is not sup
ported).
6.10.5.5. TrackStruct Type
This structure defines a uniquely identifiable Text Track or Audio Track.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Media Playback Cluster, specifically under the Data Types section. The element is identified by the ID '0' and is named 'ID'. It is of the type 'string' with a constraint that limits its maximum length to 32 characters. The conformance rule for this element is 'M', which means it is mandatory. This indicates that the 'ID' element is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row entry pertains to the Media Playback Cluster, specifically within the Data Types section, and describes an element named 'TrackAttributes' with an ID of '1'. This element is of the type 'TrackAttributesStruct' and is constrained to apply to 'all', indicating it is relevant in all contexts within this cluster. The conformance rule for 'TrackAttributes' is marked as 'M', which stands for Mandatory. This means that the 'TrackAttributes' element is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

6.10.5.5.1. ID Field
This field SHALL indicate the Identifier for the Track which is unique within the Track catalog. The
Track catalog contains all the Text/Audio tracks corresponding to the main media content.
6.10.5.5.2. TrackAttributes Field
This field SHALL indicate the Attributes associated to the Track, like languageCode.
6.10.5.6. TrackAttributesStruct Type
This structure includes the attributes associated with a Text/Audio Track

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Media Playback Cluster, specifically in the context of Data Types. The entry is identified by the ID '0' and is named 'LanguageCode'. It is of the type 'string' and has a constraint that limits its maximum length to 32 characters. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'LanguageCode' element is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'Characteristics'. This element is of the type 'list[CharacteristicEnum]', which implies it is a list composed of enumerated characteristics. The constraint 'all' suggests that all items in the list must adhere to certain unspecified conditions. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed from having a quality attribute. The default value for this element is 'null', meaning it does not have a predefined default state. The conformance rule for 'Characteristics' is 'O', which signifies that this element is optional and not required to be implemented, with no dependencies on other features or conditions.

* In the Media Playback Cluster, under the Data Types section, the table row describes an element with the ID '2' named 'DisplayName'. This element is of type 'string' and is constrained to a maximum length of 256 characters. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The default value for 'DisplayName' is 'null'. The conformance rule for this element is 'O', which means that the 'DisplayName' is optional; it is not required and has no dependencies in the current specification.

6.10.5.6.1. LanguageCode Field
The value is a String containing one of the standard Tags for Identifying Languages RFC 5646,
which identifies the primary language used in the Track.
6.10.5.6.2. Characteristics Field
This is a list of enumerated CharacteristicEnum values that indicate a purpose, trait or feature asso
ciated with the Track. A value of null SHALL indicate that there are no Characteristics correspond
ing to the Track.
6.10.5.6.3. DisplayName Field
The value is a String containing a user displayable name for the Track. A value of null SHALL indi
cate that there is no DisplayName corresponding to the Track.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Media Playback Cluster, specifically the 'CurrentState' attribute, identified by the ID '0x0000'. This attribute is of the type 'PlaybackStateEnum', which likely enumerates various playback states such as playing, paused, or stopped. The 'Constraint' is marked as 'desc', indicating that the specific constraints or conditions for this attribute are detailed elsewhere in the documentation. The 'Access' is specified as 'R V', meaning the attribute is readable and possibly volatile, suggesting it can change frequently. The 'Conformance' is marked as 'M', indicating that the 'CurrentState' attribute is mandatory. This means it is a required element within the Media Playback Cluster and must be implemented in any device or application that supports this cluster.

* The table row describes an attribute named "StartTime" within the Media Playback Cluster, identified by the ID '0x0001'. This attribute is of type 'epoch-us', which likely represents a timestamp in microseconds. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. The quality is marked as 'X', meaning this attribute is explicitly disallowed. The default value is 'null', and it has read and view access, denoted by 'R V'. The conformance rule 'AS' suggests that the attribute is mandatory if the feature 'AS' is supported. However, since the quality is 'X', this attribute is not allowed in the current specification, regardless of the conformance condition.

* The table row describes an attribute named "Duration" within the Media Playback Cluster. This attribute has an ID of '0x0002' and is of type 'uint64', with constraints described elsewhere in the documentation. It is marked with a quality of 'X', indicating that it is explicitly disallowed. The default value is 'null', and it has read and view access permissions ('R V'). The conformance rule 'AS' implies that the "Duration" attribute is mandatory if the feature or condition represented by 'AS' is supported. If 'AS' is not supported, the conformance rule does not specify an alternative, which means the attribute would not be required.

* The table row describes an attribute named "SampledPosition" within the Media Playback Cluster, identified by the ID '0x0003'. This attribute is of the type 'PlaybackPositionStruct' and has a constraint described elsewhere in the documentation. The quality of this attribute is marked as 'X', indicating it is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule for "SampledPosition" is 'AS', which means this attribute is mandatory if the feature 'AS' is supported. If 'AS' is not supported, the attribute is not required.

* The table row describes an attribute named "PlaybackSpeed" within the Media Playback Cluster. This attribute has an ID of '0x0004' and is of type 'single', with constraints described elsewhere in the documentation. Its default value is '0', and it has read and view access ('R V'). The conformance rule 'AS' indicates that the attribute is mandatory if the feature 'AS' is supported. If 'AS' is not supported, the conformance of this attribute is not explicitly defined in this entry, implying that it may not be required.

* The table row describes an attribute named "SeekRangeEnd" within the Media Playback Cluster, identified by the ID '0x0005'. It is of type 'uint64', and its constraints are detailed elsewhere in the documentation. The attribute is marked with a quality of 'X', indicating it is explicitly disallowed. The default value is 'null', and it has read and view access ('R V'). The conformance rule 'AS' suggests that the attribute is mandatory if the feature 'AS' is supported. However, since the quality is 'X', this attribute is not allowed in the current specification, regardless of the 'AS' feature's support.

* The table row describes an attribute named "SeekRangeStart" within the Media Playback Cluster. This attribute has an ID of '0x0006' and is of type 'uint64'. The constraints for this attribute are described elsewhere in the documentation, as indicated by 'desc'. The quality of this attribute is marked as 'X', meaning it is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access ('R V'). The conformance rule 'AS' suggests that the attribute is mandatory if the feature 'AS' is supported. However, since the quality is 'X', this attribute is not permitted in the current specification, regardless of the conformance condition.

* The table row describes an attribute named "ActiveAudioTrack" within the Media Playback Cluster, identified by the ID '0x0007'. This attribute is of the type 'TrackStruct' and has a constraint described elsewhere in the documentation. Its quality is marked as 'X', indicating that it is explicitly disallowed. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule 'AT' signifies that the attribute is mandatory if the feature 'AT' is supported. If 'AT' is not supported, the attribute is not required. This means that the presence of the "ActiveAudioTrack" attribute depends on whether the 'AT' feature is implemented in the device.

* The table row describes an attribute within the Media Playback Cluster, specifically the "AvailableAudioTracks" attribute. This attribute is identified by the ID '0x0008' and is of the type 'list[TrackStruct]', which indicates it holds a list of track structures. The 'Constraint' is marked as 'desc', suggesting that the constraints are detailed elsewhere in the documentation. The 'Quality' is 'X', meaning this attribute is explicitly disallowed, and its default value is 'null'. The 'Access' is 'R V', indicating it is readable and viewable. The 'Conformance' is 'AT', which implies that the attribute is mandatory if the feature or condition represented by 'AT' is supported. If 'AT' is not supported, the attribute is not required.

* The table row describes an attribute named "ActiveTextTrack" within the Media Playback Cluster, identified by the ID '0x0009'. This attribute is of the type 'TrackStruct' and has a constraint described elsewhere in the documentation. It is disallowed for quality purposes, meaning it cannot be used in contexts where quality is a consideration. The default value for this attribute is 'null', and it has read and view access permissions, indicated by 'R V'. The conformance rule 'TT' specifies that this attribute is mandatory if the feature 'TT' is supported. In summary, "ActiveTextTrack" is a mandatory attribute when the 'TT' feature is present, but it is not allowed in quality-sensitive contexts.

* The table row describes an attribute named "AvailableTextTracks" within the Media Playback Cluster, identified by the ID '0x000A'. This attribute is of the type 'list[TrackStruct]', indicating it holds a list of track structures, and its constraints are detailed elsewhere in the documentation. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed. The default value is 'null', and it has read and view access ('R V'). The conformance rule 'TT' indicates that this attribute is mandatory if the feature 'TT' (presumably representing a specific feature related to text tracks) is supported. If 'TT' is not supported, the attribute is not required.

6.10.6.1. CurrentState Attribute
This attribute SHALL indicate the current playback state of media.
During fast-forward, rewind, and other seek operations; this attribute SHALL be set to PLAYING.
6.10.6.2. StartTime Attribute
This attribute SHALL indicate the start time of the media, in case the media has a fixed start time
(for example, live stream or television broadcast), or null when start time does not apply to the cur
rent media (for example, video-on-demand). This time is a UTC time. The client needs to handle con
version to local time, as required, taking in account time zone and possible local DST offset.
6.10.6.3. Duration Attribute
This attribute SHALL indicate the duration, in milliseconds, of the current media being played back
or null when duration is not applicable (for example, in live streaming content with no known
duration). This attribute SHALL never be 0.
6.10.6.4. SampledPosition Attribute
This attribute SHALL indicate the position of playback (Position field) at the time (UpdateAt field)
specified in the attribute. The client MAY use the SampledPosition attribute to compute the current
position within the media stream based on the PlaybackSpeed, PlaybackPositionStruct.UpdatedAt
and PlaybackPositionStruct.Position fields. To enable this, the SampledPosition attribute SHALL be
updated whenever a change in either the playback speed or the playback position is triggered out
side the normal playback of the media. The events which MAY cause this to happen include:
• Starting or resumption of playback
• Seeking
• Skipping forward or backward
• Fast-forwarding or rewinding
• Updating of playback speed as a result of explicit request, or as a result of buffering events
6.10.6.5. PlaybackSpeed Attribute
This attribute SHALL indicate the speed at which the current media is being played. The new Play
backSpeed SHALL be reflected in this attribute whenever any of the following occurs:
• Starting of playback
• Resuming of playback
• Fast-forwarding
• Rewinding
The PlaybackSpeed SHALL reflect the ratio of time elapsed in the media to the actual time taken for
the playback assuming no changes to media playback (for example buffering events or requests to
pause/rewind/forward).
• A value for PlaybackSpeed of 1 SHALL indicate normal playback where, for example, playback
for 1 second causes the media to advance by 1 second within the duration of the media.
• A value for PlaybackSpeed which is greater than 0 SHALL indicate that as playback is happen
ing the media is currently advancing in time within the duration of the media.
• A value for PlaybackSpeed which is less than 0 SHALL indicate that as playback is happening
the media is currently going back in time within the duration of the media.
• A value for PlaybackSpeed of 0 SHALL indicate that the media is currently not playing back.
When the CurrentState attribute has the value of PAUSED, NOT_PLAYING or BUFFERING, the
PlaybackSpeed SHALL be set to 0 to reflect that the media is not playing.
Following examples illustrate the PlaybackSpeed attribute values in various conditions.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Media Playback Cluster, specifically focusing on the playback details of media content. The attribute in question is 'Seconds of Media Played', which records the duration of media that has been played, with a value of '2' seconds. The 'Actual Time Taken in Seconds' is also '2', indicating that the playback occurred in real-time without any delays or speed adjustments. The 'Direction of playback' is 'Forward', and the 'PlaybackSpeed' is '1.0', confirming that the media is playing at normal speed. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it would typically be mandatory (M) or optional (O) depending on the specific conditions or features supported by the device. If the conformance were to be described using the guide, it would specify under what conditions this attribute is required or optional, ensuring that the implementation aligns with the Matter specification's requirements for media playback features

* The table row entry pertains to the "Seconds of Media Played" attribute within the Media Playback Cluster, specifically under the Attributes section. The conformance rule for this attribute is not explicitly provided in the data you've shared, but based on the context, it would typically indicate the conditions under which this attribute is required or optional. For instance, if the conformance were something like `M`, it would mean that the "Seconds of Media Played" attribute is always mandatory for any implementation of the Media Playback Cluster. If it were `O`, it would be optional, meaning implementations could choose whether or not to include it without any dependencies. Without the specific conformance string, we can only infer that this attribute is related to tracking the duration of media that has been played, which is crucial for functionalities like playback progress tracking and user interface updates. The other data points, such as "Actual Time Taken in Seconds," "Direction of playback," and "PlaybackSpeed," provide additional context for how media playback is being

* The table row entry pertains to the "Seconds of Media Played" attribute within the Media Playback Cluster, specifically under the Attributes section. The conformance rule for this attribute is indicated by the number '1', which, based on the Matter Conformance Interpretation Guide, suggests that this attribute is mandatory. This means that the "Seconds of Media Played" attribute is always required to be implemented in any device or application that supports the Media Playback Cluster. The attribute tracks the duration of media that has been played, and its presence is essential for the proper functioning and compliance of the media playback feature within the Matter IoT specification.

* The table row entry pertains to the "Media Playback Cluster" within the "Attributes" section, specifically focusing on the attribute related to the playback of media in reverse at a speed of -1.0. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the context, it likely involves conditions under which this attribute is required or optional. If we assume a conformance string like `AB, O`, it would mean that the attribute is mandatory if a certain feature `AB` is supported; otherwise, it is optional. However, without the exact conformance string, we can only infer that the attribute is related to tracking the seconds of media played in reverse and the actual time taken, which might be conditionally required based on specific features or configurations within the Media Playback Cluster.

* The table row entry describes an attribute within the Media Playback Cluster, specifically focusing on the playback of media in reverse at a speed of -2.0. The 'Seconds of Media Played' is 2, indicating the duration of playback in reverse, while the 'Actual Time Taken in Seconds' is 1, suggesting that the playback occurs at twice the normal speed. The 'Direction of playback' is specified as 'Reverse', which aligns with the negative playback speed. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context and typical usage, it would likely involve conditions related to the support of reverse playback and variable playback speeds. If the conformance rule were provided, it would dictate whether this attribute is mandatory, optional, provisional, deprecated, or disallowed based on the presence or absence of certain features or conditions, as outlined in the Matter Conformance Interpretation Guide.

* The table row pertains to the "Media Playback Cluster" within the "Attributes" section, focusing on a specific attribute related to media playback. The attribute in question, "Seconds of Media Played," is associated with a conformance rule that is not explicitly provided in the row data. However, based on the context, this attribute likely tracks the duration of media that has been played in seconds. The conformance rule would determine whether this attribute is mandatory, optional, or subject to other conditions based on the presence or absence of certain features or conditions. For example, if the conformance rule were `M`, it would mean that the "Seconds of Media Played" attribute is always required. If it were `O`, it would be optional. Without the specific conformance string, we can only infer that this attribute is crucial for tracking media playback progress, especially in scenarios involving reverse playback at a speed of -0.5, as indicated by the "Direction of playback" and "PlaybackSpeed" fields

6.10.6.6. SeekRangeStart Attribute
This attribute SHALL indicate the earliest valid position to which a client MAY seek back, in mil
liseconds from start of the media. A value of Nas SHALL indicate that seeking backwards is not
allowed.
6.10.6.7. SeekRangeEnd Attribute
This attribute SHALL indicate the furthest forward valid position to which a client MAY seek for
This attribute SHALL indicate the furthest forward valid position to which a client MAY seek forward,
in milliseconds from the start of the media. When the media has an associated StartTime, a
value of null SHALL indicate that a seek forward is valid only until the current time within the
media, using a position computed from the difference between the current time offset and Start
Time, in milliseconds from start of the media, truncating fractional milliseconds towards 0. A value
of Nas when StartTime is not specified SHALL indicate that seeking forward is not allowed.
6.10.6.8. ActiveAudioTrack Attribute
ActiveTrack refers to the Audio track currently set and being used for the streaming media. A value
of null SHALL indicate that no Audio Track corresponding to the current media is currently being
played.
6.10.6.9. AvailableAudioTracks Attribute
AvailableAudioTracks refers to the list of Audio tracks available for the current title being played. A
value of null SHALL indicate that no Audio Tracks corresponding to the current media are selec
table by the client.
6.10.6.10. ActiveTextTrack Attribute
ActiveTrack refers to the Text track currently set and being used for the streaming media. This can
be nil. A value of null SHALL indicate that no Text Track corresponding to the current media is cur
rently being displayed.
6.10.6.11. AvailableTextTracks Attribute
AvailableTextTracks refers to the list of Text tracks available for the current title being played. This
can be an empty list. A value of null SHALL indicate that no Text Tracks corresponding to the cur
rent media are selectable by the client.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "Play" command, which is identified by the ID '0x00'. This command is directed from the client to the server and expects a response in the form of 'PlaybackResponse'. The access level for this command is marked as 'Optional' (O), indicating that the command can be implemented but is not required for access control purposes. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "Play" command must be implemented in any device that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row describes a command within the Media Playback Cluster, specifically the "Pause" command, which is directed from the client to the server. The command is identified by the ID '0x01' and expects a response of type 'PlaybackResponse'. The access level for this command is marked as 'Optional' (O), meaning it is not required to be implemented by default. However, the conformance rule for this command is 'M', indicating that the "Pause" command is mandatory. This means that any implementation of the Media Playback Cluster must include support for this command, regardless of other conditions or features.

* The table row describes a command within the Media Playback Cluster, specifically the "Stop" command, which is identified by the ID '0x02'. This command is directed from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as 'O', indicating that access is optional. The conformance rule for this command is 'M', meaning that the "Stop" command is mandatory and must always be implemented in any device or application that supports the Media Playback Cluster. There are no conditional expressions or dependencies affecting this requirement, making it a straightforward mandatory element.

* The table row describes a command within the Media Playback Cluster, specifically the "StartOver" command, which is identified by the ID `0x03`. This command is directed from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as "O", indicating that access is optional. The conformance rule for this command is also "O", meaning that the implementation of the "StartOver" command is optional and not required by default. There are no additional conditions or dependencies affecting its optional status, allowing implementers the flexibility to include or exclude this command based on their specific needs or preferences.

* The table row describes a command within the Media Playback Cluster, specifically the "Previous" command, which is identified by the ID '0x04'. This command is directed from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as 'O', indicating that it is optional for the client to implement. The conformance rule for this command is also 'O', meaning that the implementation of the "Previous" command is entirely optional and does not depend on any other features or conditions. Therefore, devices supporting the Media Playback Cluster may choose to implement this command, but they are not required to do so.

* The table row describes a command within the Media Playback Cluster, specifically the "Next" command, which is identified by the ID `0x05`. This command is sent from the client to the server and expects a response in the form of a "PlaybackResponse." The access level for this command is marked as optional (`O`), meaning that it is not required for implementation and has no dependencies on other features or conditions. The conformance rule for this command is also `O`, indicating that the inclusion of the "Next" command in a device's implementation is entirely optional and not mandated by the Matter specification. This allows manufacturers the flexibility to decide whether to support this command based on their specific product requirements and use cases.

* The table row describes a command within the Media Playback Cluster, specifically the "Rewind" command, which is identified by the ID '0x06'. This command is directed from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as 'O', indicating that it is optional and not required for all implementations. The conformance rule for this command is 'VS', which does not directly match any basic conformance tags or logical conditions outlined in the guide. This suggests that the conformance for the "Rewind" command is described elsewhere in the documentation under a specific condition or context not covered by the basic tags, implying that its implementation may depend on certain vendor-specific or situational factors.

* The table row describes a command within the Media Playback Cluster, specifically the "FastForward" command, which is identified by the ID '0x07'. This command is sent from the client to the server and expects a "PlaybackResponse" in return. The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance field is marked as 'VS', which, according to the Matter Conformance Interpretation Guide, implies that the conformance is described elsewhere in the documentation. Therefore, the specific conditions or requirements for this command's implementation are detailed in another section of the specification, and it cannot be simply categorized as mandatory, optional, or otherwise based on the provided conformance tags.

* The table row describes a command within the Media Playback Cluster, specifically the "SkipForward" command. This command is identified by the ID '0x08' and is directed from the client to the server, with an expected response of 'PlaybackResponse'. The access level for this command is marked as 'O', indicating it is optional. The conformance rule for this command is also 'O', meaning that the implementation of the "SkipForward" command is not required and has no dependencies. In essence, devices supporting the Media Playback Cluster may choose to implement this command, but it is not mandatory for compliance with the Matter specification.

* The table row describes a command within the Media Playback Cluster, specifically the "SkipBackward" command, identified by the ID '0x09'. This command is directed from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as 'O', indicating that it is optional for implementation. The conformance rule for "SkipBackward" is also 'O', meaning that this command is not required and can be implemented at the discretion of the device manufacturer without any dependencies or conditions. In essence, the "SkipBackward" command is an optional feature that manufacturers may choose to support in their devices, but it is not mandated by the Matter specification.

* The table row describes a command within the Media Playback Cluster, specifically the "PlaybackResponse" command, which is identified by the ID '0x0A'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' signifies that this command does not expect a response. The 'Conformance' field is marked with 'M', which stands for Mandatory. This means that the "PlaybackResponse" command is a required element in the Media Playback Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

* The table row describes a command within the Media Playback Cluster, specifically the "Seek" command, identified by the ID `0x0B`. This command is sent from the client to the server and expects a response in the form of a "PlaybackResponse". The access level for this command is marked as "Optional" (`O`), indicating that it is not required and has no dependencies. The conformance rule for this command is `AS`, which means it is mandatory if the feature or condition represented by `AS` is supported. If the condition `AS` is not met, the conformance rule does not specify an alternative, implying that the command may not be required. This entry outlines the conditions under which the "Seek" command must be implemented in devices supporting the Media Playback Cluster.

* The table row describes a command within the Media Playback Cluster, specifically the "ActivateAudioTrack" command, which is identified by the ID '0x0C'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required and has no dependencies. The conformance rule 'AT' specifies that the command is mandatory if the feature 'AT' (presumably representing an Audio Track feature) is supported. If the 'AT' feature is not supported, the command is not required. This entry outlines the conditions under which the "ActivateAudioTrack" command must be implemented in devices that support the Media Playback Cluster.

* The table row describes a command within the Media Playback Cluster, specifically the "ActivateTextTrack" command, which is identified by the ID '0x0D'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'TT' indicates that the command is mandatory if the feature 'TT' (likely representing a specific feature related to text tracks) is supported. If the 'TT' feature is not supported, the command is not mandatory. This ensures that the command is implemented only in contexts where the relevant feature is present, aligning with the capabilities of the device or application.

* The table row describes a command within the Media Playback Cluster, specifically the "DeactivateTextTrack" command. This command is identified by the ID '0x0E' and is directed from the client to the server, with a response expected ('Y'). The access level is marked as 'Optional' ('O'), meaning that implementing this command is not mandatory and has no dependencies. The conformance rule 'TT' indicates that the command is mandatory if the feature 'TT' (presumably related to text track functionality) is supported. In summary, the "DeactivateTextTrack" command must be implemented if the device supports the 'TT' feature; otherwise, it is not required.

6.10.7.1. Play Command
Upon receipt, this SHALL play media. If content is currently in a FastForward or Rewind state. Play
SHALL return media to normal playback speed.
6.10.7.2. Pause Command
Upon receipt, this SHALL pause playback of the media.
6.10.7.3. Stop Command
Upon receipt, this SHALL stop playback of the media. User-visible outcome is context-specific. This
MAY navigate the user back to the location from where the media was originally launched.
6.10.7.4. StartOver Command
Upon receipt, this SHALL Start Over with the current media playback item.
6.10.7.5. Previous Command
Upon receipt, this SHALL cause the handler to be invoked for "Previous". User experience is con
text-specific. This will often Go back to the previous media playback item.
6.10.7.6. Next Command
Upon receipt, this SHALL cause the handler to be invoked for "Next". User experience is context-
specific. This will often Go forward to the next media playback item.
6.10.7.7. Rewind Command
Upon receipt, this SHALL start playback of the media backward in case the media is currently play
ing in the forward direction or is not playing. If the playback is already happening in the back
wards direction receipt of this command SHALL increase the speed of the media playback back
wards.
Different "rewind" speeds MAY be reflected on the media playback device based upon the number
of sequential calls to this function and the capability of the device. This is to avoid needing to define
every speed (multiple fast, slow motion, etc). If the PlaybackSpeed attribute is supported it SHALL
be updated to reflect the new speed of playback. If the playback speed cannot be changed for the
media being played(for example, in live streaming content not supporting seek), the status of
NOT_ALLOWED SHALL be returned. If the playback speed has reached the maximum supported
speed for media playing backwards, the status of SPEED_OUT_OF_RANGE SHALL be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "AudioAdvanceUnmuted" command. This command is of the boolean type, applicable to all instances of the cluster, and has a default value of `false`. The conformance rule for this command is specified as `AA`, which, according to the Matter Conformance Interpretation Guide, means that the command is mandatory if the feature `AA` is supported. In simpler terms, if a device supports the `AA` feature, it must implement the "AudioAdvanceUnmuted" command; otherwise, the requirement does not apply.

6.10.7.7.1. AudioAdvanceUnmuted Field
This field SHALL indicate whether audio should be unmuted by the player during rewind.
A value of true does not guarantee that audio can be heard by the user since the speaker may be
muted, turned down to a low level and/or unplugged.
6.10.7.8. FastForward Command
Upon receipt, this SHALL start playback of the media in the forward direction in case the media is
currently playing in the backward direction or is not playing. If the playback is already happening
in the forward direction receipt of this command SHALL increase the speed of the media playback.
Different "fast-forward" speeds MAY be reflected on the media playback device based upon the
number of sequential calls to this function and the capability of the device. This is to avoid needing
to define every speed (multiple fast, slow motion, etc). If the PlaybackSpeed attribute is supported it
SHALL be updated to reflect the new speed of playback. If the playback speed cannot be changed
for the media being played(for example, in live streaming content not supporting seek), the status
of NOT_ALLOWED SHALL be returned. If the playback speed has reached the maximum supported
speed for media playing forward, the status of SPEED_OUT_OF_RANGE SHALL be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "AudioAdvanceUnmuted" command. This command is of type boolean, with a constraint applicable to all instances, and it defaults to a value of false. The conformance rule for this command is specified as "AA," which means that the command is mandatory if the feature "AA" is supported. In other words, if a device or implementation supports the "AA" feature, it must also support the "AudioAdvanceUnmuted" command. If the "AA" feature is not supported, the conformance rule does not apply, and the command is not required.

6.10.7.8.1. AudioAdvanceUnmuted Field
This field SHALL indicate whether audio should be unmuted by the player during fast forward.
A value of true does not guarantee that audio can be heard by the user since the speaker may be
muted, turned down to a low level and/or unplugged.
6.10.7.9. SkipForward Command
Upon receipt, this SHALL Skip forward in the media by the given number of milliseconds, using the
data as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "DeltaPositionMilliseconds" command. This command has an identifier (ID) of '0' and is of type 'uint64', indicating it expects a 64-bit unsigned integer value. The 'Constraint' field labeled as 'all' suggests that this command applies universally within its context. The 'Conformance' field is marked as 'M', which means that the "DeltaPositionMilliseconds" command is mandatory. This implies that any implementation of the Media Playback Cluster must include this command, as it is always required according to the Matter IoT specification.

6.10.7.9.1. DeltaPositionMilliseconds Field
This field SHALL indicate the duration of the time span to skip forward in the media, in millisec
onds. In case the resulting position falls in the middle of a frame, the server SHALL set the position
to the beginning of that frame and set the SampledPosition attribute on the cluster accordingly. If
the resultant position falls beyond the furthest valid position in the media the client MAY seek for
ward to, the position should be set to that furthest valid position. If the SampledPosition attribute is
supported it SHALL be updated on the cluster accordingly.
6.10.7.10. SkipBackward Command
Upon receipt, this SHALL Skip backward in the media by the given number of milliseconds, using
the data as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically identified by the ID '0' and named 'DeltaPositionMilliseconds'. This command is of the type 'uint64', indicating it uses a 64-bit unsigned integer to represent its data. The 'Constraint' field is marked as 'all', suggesting that there are no specific restrictions on its use across different implementations. The 'Conformance' field is marked with 'M', which stands for Mandatory. This means that the 'DeltaPositionMilliseconds' command is a required element for any implementation of the Media Playback Cluster, and it must be supported without exception.

6.10.7.10.1. DeltaPositionMilliseconds Field
This field SHALL indicate the duration of the time span to skip backward in the media, in millisec
onds. In case the resulting position falls in the middle of a frame, the server SHALL set the position
to the beginning of that frame and set the SampledPosition attribute on the cluster accordingly. If
the resultant position falls before the earliest valid position to which a client MAY seek back to, the
position should be set to that earliest valid position. If the SampledPosition attribute is supported it
SHALL be updated on the cluster accordingly.
6.10.7.11. Seek Command
Upon receipt, this SHALL change the playback position in the media to the given position using data
as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "Position" command, which is identified by the ID '0' and is of type 'uint64'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the "Position" command is a required element in the Media Playback Cluster and must be implemented in all devices or systems that support this cluster, without any conditions or exceptions.

6.10.7.11.1. Position Field
This field SHALL indicate the position (in milliseconds) in the media to seek to. In case the position
falls in the middle of a frame, the server SHALL set the position to the beginning of that frame and
set the SampledPosition attribute on the cluster accordingly. If the position falls before the earliest
valid position or beyond the furthest valid position to which a client MAY seek back or forward to
respectively, the status of SEEK_OUT_OF_RANGE SHALL be returned and no change SHALL be made
to the position of the playback.
6.10.7.12. PlaybackResponse Command
This command SHALL be generated in response to various Playback Commands. The data for this
command SHALL be as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the "Status" command, which is identified by the ID '0' and has a type of 'StatusEnum'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "Status" command must always be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* In the Media Playback Cluster, under the Commands section, there is an entry for a command identified as 'ID: 1' with the name 'Data'. This command is of the 'string' type and has no specific constraints on its value, as indicated by 'Constraint: any'. The conformance rule for this command is marked as 'O', which means it is optional. This implies that the implementation of this command is not required and does not depend on any other features or conditions. Devices or applications implementing the Media Playback Cluster can choose to include this command, but they are not obligated to do so according to the Matter specification.

6.10.7.12.1. Status Field
This field SHALL indicate the status of the command which resulted in this response.
6.10.7.12.2. Data Field
This field SHALL indicate Optional app-specific data.
6.10.7.13. ActivateAudioTrack Command
Upon receipt, the server SHALL set the active Audio Track to the one identified by the TrackID in
the Track catalog for the streaming media. If the TrackID does not exist in the Track catalog, OR
does not correspond to the streaming media OR no media is being streamed at the time of receipt of
this command, the server will return an error status of INVALID_ARGUMENT.

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Playback Cluster, specifically the 'TrackID' command. This command is identified by the ID '0' and is of the type 'string', with a constraint that limits its maximum length to 32 characters. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'TrackID' command is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row describes a command within the Media Playback Cluster, specifically the "AudioOutputIndex" command, which is identified by the ID '1' and is of type 'uint8'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Quality' field is marked as 'X', meaning this command is explicitly disallowed in the current specification. The 'Conformance' field is labeled 'AT', which, according to the conformance rules, suggests that the command is mandatory if the feature 'AT' is supported. However, since the 'Quality' is 'X', the command is not allowed regardless of the conformance condition.

6.10.7.13.1. TrackID Field
This field SHALL indicate the Audio Track to activate.
6.10.7.13.2. AudioOutputIndex Field
This  value  is  the  index  field  of  the  OutputInfoStruct  from  the  OutputList  attribute  (from  the
AudioOutput cluster) and indicates which audio output the Audio Track should be played on. This
field is absent for Text Tracks and only present for Audio Tracks. A value of null SHALL indicate
that the server can choose the audio output(s) to play the Audio Track on.
6.10.7.14. ActivateTextTrack Command
Upon receipt, the server SHALL set the active Text Track to the one identified by the TrackID in the
Track catalog for the streaming media. If the TrackID does not exist in the Track catalog, OR does
not correspond to the streaming media OR no media is being streamed at the time of receipt of this
command, the server SHALL return an error status of INVALID_ARGUMENT.

_Table parsed from section 'Commands':_

* In the context of the Media Playback Cluster, the table row describes a command with the ID '0' named 'TrackID', which is of type 'string' and has a constraint limiting its length to a maximum of 32 characters. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the 'TrackID' command is always required to be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

6.10.7.14.1. TrackID Field
This field SHALL indicate the Text Track to activate.
6.10.7.15. DeactivateTextTrack Command
If a Text Track is active (i.e. being displayed), upon receipt of this command, the server SHALL stop
displaying it.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Media Playback Cluster, specifically the "StateChanged" event, identified by the ID '0x00'. This event has a priority level of 'INFO' and requires 'V' access, which typically means it is visible or can be accessed in some manner. The conformance rule for this event is 'O', indicating that the "StateChanged" event is optional. This means that the implementation of this event is not required and does not depend on any other features or conditions. It can be included at the discretion of the developer or manufacturer, but there is no obligation to do so according to the Matter specification.

6.10.8.1. StateChanged Event
If supported, this event SHALL be generated when there is a change in any of the supported attrib
utes of the Media Playback cluster. This event SHALL have the following data fields:

_Table parsed from section 'Events':_

* The table row describes an event within the Media Playback Cluster, specifically the "CurrentState" event, which is identified by the ID '0x0000'. This event is of the type 'PlaybackStateEnum', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this event is marked as 'M', which means it is mandatory. This implies that the "CurrentState" event must always be implemented in any device or application that supports the Media Playback Cluster, without any conditions or exceptions.

* The table row describes an event within the Media Playback Cluster, specifically identified by the ID `0x0001` and named `StartTime`. This event is of the type `epoch-us`, which likely refers to a timestamp format in microseconds since the epoch. The constraint for this event is marked as `desc`, indicating that the specific constraints are detailed elsewhere in the documentation. The conformance rule for this event is `AS`, which implies that the `StartTime` event is mandatory if the feature or condition represented by `AS` is supported. If `AS` is not supported, the conformance of this event is not explicitly defined in this entry, suggesting it may not be required or its status is determined by additional context not provided here.

* The table row describes an event within the Media Playback Cluster, specifically identified by the ID `0x0002` and named 'Duration'. This event is of type `uint64`, and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this event is 'AS', which means it is mandatory if the feature 'AS' is supported. If the feature 'AS' is not supported, the conformance rule does not specify any alternative, implying that the event may not be required.

* The table row describes an event within the Media Playback Cluster, specifically the "SampledPosition" event, identified by the ID `0x0003`. This event is of the type `PlaybackPositionStruct`, and its constraints are detailed elsewhere in the documentation, as indicated by the "desc" constraint. The conformance rule for this event is specified as `AS`, which, according to the Matter Conformance Interpretation Guide, suggests that the conformance is conditional based on the support of the feature or condition represented by `AS`. If the feature `AS` is supported, the "SampledPosition" event is mandatory; otherwise, the conformance is not explicitly defined in this entry and would require further context from the documentation.

* The table row entry pertains to the "PlaybackSpeed" event within the Media Playback Cluster, identified by the ID '0x0004'. This event is of type 'single', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule 'AS' suggests that the inclusion of this event is conditionally mandatory based on the support of a feature or condition represented by 'AS'. If the feature 'AS' is supported, then the "PlaybackSpeed" event is required to be implemented. The specific details of what 'AS' represents would be defined elsewhere in the Matter specification.

* The table row describes an event within the Media Playback Cluster, specifically the "SeekRangeEnd" event, which is identified by the ID `0x0005` and is of type `uint64`. The constraint for this event is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this event is 'AS', which implies that the event is mandatory if the feature 'AS' is supported. If 'AS' is not supported, the conformance rule does not specify an alternative, suggesting that the event may not be applicable or required in such cases.

* The table row entry pertains to the "SeekRangeStart" event within the Media Playback Cluster, identified by the ID '0x0006'. This event is of type 'uint64', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this event is 'AS', which implies that the event is mandatory if the feature or condition represented by 'AS' is supported. In the context of the Matter specification, this means that the "SeekRangeStart" event must be implemented if the device or system includes the 'AS' feature, ensuring that the event is available for use in scenarios where 'AS' is applicable.

* In the Media Playback Cluster, under the Events section, the table row describes an event with the ID '0x0007' named 'Data'. This event is of type 'octstr', which indicates it is an octet string, and it has a constraint that limits its maximum size to 900 bytes. The conformance rule for this event is 'O', meaning it is optional. This implies that the inclusion of the 'Data' event is not required for compliance with the Matter specification, and it can be implemented at the discretion of the device manufacturer without any dependencies or conditions.

* The table row describes an event within the Media Playback Cluster, specifically the "AudioAdvanceUnmuted" event, which is identified by the ID `0x0008`. This event is of the boolean type, meaning it can be either true or false, with a default value of false. The constraint for this event is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this event is `AA`, meaning that the event is mandatory if the feature `AA` is supported. In other words, if the device or implementation supports the `AA` feature, it must also support the "AudioAdvanceUnmuted" event.

6.10.8.1.1. CurrentState Field
This field SHALL indicate the updated playback state as defined by the CurrentState attribute, and
has the same constraint as that attribute.
6.10.8.1.2. StartTime Field
This field SHALL indicate the updated start time as defined by the StartTime attribute, and has the
same constraint as that attribute.
6.10.8.1.3. Duration Field
This field SHALL indicate the updated duration as defined by the Duration attribute, and has the
same constraint as that attribute.
6.10.8.1.4. SampledPosition Field
This field SHALL indicate the updated position of playback as defined by the SampledPosition
attribute, and has the same constraint as that attribute.
6.10.8.1.5. PlaybackSpeed Field
This field SHALL indicate the updated speed at which the current media is being played as defined
by the PlaybackSpeed attribute, and has the same constraint as that attribute.
6.10.8.1.6. SeekRangeStart Field
This field SHALL indicate the updated start of the seek range start as defined by the SeekRangeStart
attribute, and has the same constraint as that attribute.
6.10.8.1.7. SeekRangeEnd Field
This field SHALL indicate the updated start of the seek range end as defined by the SeekRangeEnd
attribute, and has the same constraint as that attribute.
6.10.8.1.8. Data Field
This field SHALL indicate Optional app-specific data.
6.10.8.1.9. AudioAdvanceUnmuted Field
This field SHALL indicate whether audio is unmuted by the player due to a FF or REW command.
This field is only meaningful when the PlaybackSpeed is present and not equal to 0 (paused) or 1
(normal playback). Typically the value will be false (muted), however, some players will play audio
during certain fast forward and rewind speeds, and in these cases, the value will be true (not
muted).
A value of true does not guarantee that audio can be heard by the user since the speaker may be
muted, turned down to a low level and/or unplugged.