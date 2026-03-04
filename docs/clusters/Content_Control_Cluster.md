
# 6.13 Content Control Cluster

This cluster is used for managing the content control (including "parental control") settings on a
media device such as a TV, or Set-top Box.
This cluster allows to configure content control settings by clients with the Management privilege.
It is responsibility of the end product to enforce appropriate right access (for example, to prevent a
child from disabling this feature).
NOTE Support for Content Control cluster is provisional.

## Data Types
6.13.5.1. DayOfWeekBitmap type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Content Control Cluster under the Data Types section, the table row describes a data element named "Sunday," which is represented by the bit value '0'. The summary also labels it as "Sunday." However, the conformance rule for this entry is not explicitly provided in the data given. Typically, the conformance rule would specify whether this element is mandatory, optional, provisional, deprecated, or disallowed, or it might involve a more complex condition based on the presence of certain features. Without a specific conformance string, we cannot determine the exact requirement status of this element within the Matter specification.

* In the Content Control Cluster, under the Data Types section, there is an entry for the 'Monday' data type, represented by the bit '1'. This entry is named 'Monday' and is summarized simply as 'Monday'. The conformance rule for this entry is not explicitly provided in the given data, so we cannot directly interpret its conformance status using the provided guide. However, typically in such contexts, a bit representing a day of the week like 'Monday' might be used in a bitmap to indicate the presence or absence of a feature or setting related to that day. Without a specific conformance string, we assume that its inclusion is standard for the context, possibly implying a default mandatory or optional status depending on the broader specification requirements.

* In the Content Control Cluster, under the Data Types section, the table entry for 'Bit' 2 is named 'Tuesday' and is summarized as 'Tuesday'. The conformance rule for this entry is not explicitly provided in the data you shared, so I cannot directly interpret its conformance status. However, if a conformance string were provided, it would dictate whether the 'Tuesday' element is mandatory, optional, provisional, deprecated, or disallowed based on the conditions outlined in the Matter Conformance Interpretation Guide. Without this information, we can only acknowledge that 'Tuesday' is a defined data type within the cluster, potentially used to represent or control features related to the day of the week.

* In the Content Control Cluster, under the Data Types section, the table row entry for 'Bit' 3 is named 'Wednesday' and is summarized as 'Wednesday'. The conformance rule for this entry is not explicitly provided in the data, but based on the context and typical usage of such entries, it likely indicates that the 'Wednesday' bit is part of a bitmask or enumeration used to represent days of the week. Without a specific conformance string, we can infer that its inclusion is likely standard for representing days in a week, but the exact requirement (mandatory, optional, etc.) would depend on the broader context of the specification or any additional documentation that describes the conformance for this particular bit.

* In the Content Control Cluster, under the Data Types section, the table entry for 'Bit' 4 is named 'Thursday' and is summarized as 'Thursday'. The conformance rule for this entry is not explicitly provided in the data you shared, so we cannot determine its specific requirements or conditions based on the conformance guide. Typically, such an entry would specify whether the 'Thursday' bit is mandatory, optional, provisional, deprecated, or disallowed, or it might involve a conditional expression based on other features or elements. Without the conformance string, we can only acknowledge that this entry represents a bit associated with the day 'Thursday' within the cluster's data types.

* In the Content Control Cluster, under the Data Types section, there is an entry for the 'Friday' element, which is represented by the bit '5'. This entry is part of a table that likely outlines various days of the week, each associated with a specific bit. The 'Conformance' field for this entry is not explicitly provided in the data, but based on the context and typical usage in such tables, it might imply that the 'Friday' element is either mandatory or optional depending on the specific implementation requirements of the Content Control Cluster. If a conformance rule were provided, it would dictate whether the 'Friday' element is required, optional, or subject to other conditions as specified by the Matter IoT specification.

* In the Content Control Cluster, under the Data Types section, the table row entry for 'Bit' 6 is named 'Saturday' and summarized as 'Saturday'. This entry likely represents a data type or feature related to the day of the week, specifically Saturday. The conformance rule for this entry is not explicitly provided in the data, but if we assume a typical scenario where days of the week might be optional or conditional based on certain features, the conformance could imply that the inclusion of 'Saturday' is dependent on specific conditions or features being supported. Without a specific conformance string, we cannot definitively state its requirement status, but it might be optional or conditional based on the broader context of the Content Control Cluster's implementation.

6.13.5.2. RatingNameStruct Type

_Table parsed from section 'Data Types':_

* In the Content Control Cluster, under the Data Types section, the table entry for 'RatingName' is identified by the ID '0'. It is a data type of type 'string' with a constraint that limits its maximum length to 8 characters. The conformance rule for 'RatingName' is marked as 'M', which means it is a Mandatory element. This indicates that 'RatingName' is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Content Control Cluster, specifically in the Data Types section. The element is identified by the ID '1' and is named 'RatingNameDesc'. It is of the type 'string' with a constraint that limits its maximum length to 64 characters. The conformance rule for 'RatingNameDesc' is marked as 'O', which means that this element is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status. Implementers of the Matter specification can choose to include this element, but it is not mandatory for compliance.

6.13.5.2.1. RatingName Field
This field SHALL indicate the name of the rating level of the applied rating system. The applied rat
ing system is dependent upon the region or country where the Node has been provisioned, and may
vary from one country to another.
6.13.5.2.2. RatingNameDesc Field
This field SHALL specify a human readable (displayable) description for RatingName.
6.13.5.3. BlockChannelStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Content Control Cluster, specifically in the Data Types section. The entry is identified by the ID '0' and is named 'BlockChannelIndex'. It is of type 'uint16', which indicates it is a 16-bit unsigned integer. The 'Constraint' field is marked as 'all', suggesting that this data type applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in some contexts, although this does not affect its conformance status here. The 'Conformance' is marked as 'M', which means that the 'BlockChannelIndex' is a mandatory element. This implies that it is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes an entry within the Content Control Cluster, specifically in the Data Types section. The entry is identified by the ID '1' and is named 'MajorNumber'. It is of the data type 'uint16', which is a 16-bit unsigned integer, and it has a constraint labeled 'all', indicating that it applies universally within its context. The conformance rule for 'MajorNumber' is 'M', which stands for Mandatory. This means that the 'MajorNumber' element is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes an entry within the Content Control Cluster, specifically under the Data Types section. The entry is identified by the ID '2' and is named 'MinorNumber'. It is of the data type 'uint16', which is an unsigned 16-bit integer, and it has a constraint labeled as 'all', indicating that it applies universally within its context. The conformance rule for 'MinorNumber' is marked as 'M', which stands for Mandatory. This means that the 'MinorNumber' element is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* In the Content Control Cluster, under the Data Types section, the table entry for 'Identifier' with ID '3' is of type 'string' and has a constraint labeled 'all'. The conformance rule for this entry is 'O', which means that the 'Identifier' element is optional. This indicates that the inclusion of the 'Identifier' element is not required and does not depend on any specific conditions or features being supported. It can be included at the discretion of the implementer without any mandatory obligation.

6.13.5.3.1. BlockChannelIndex Field
This field SHALL indicate a unique index value for a blocked channel. This value may be used to
indicate one selected channel which will be removed from BlockChannelList attribute.
6.13.5.3.2. MajorNumber Field
This field SHALL indicate the channel major number value (for example, using ATSC format). When
the channel number is expressed as a string, such as "13.1" or "256", the major number would be 13
or 256, respectively. This field is required but SHALL be set to 0 for channels such as over-the-top
channels that are not represented by a major or minor number.
6.13.5.3.3. MinorNumber Field
This field SHALL indicate the channel minor number value (for example, using ATSC format). When
the channel number is expressed as a string, such as "13.1" or "256", the minor number would be 1
or 0, respectively. This field is required but SHALL be set to 0 for channels such as over-the-top
channels that are not represented by a major or minor number.
6.13.5.3.4. Identifier
This field SHALL indicate the unique identifier for a specific channel. This field is optional, but
SHOULD be provided when MajorNumber and MinorNumber are not available.
6.13.5.4. AppInfoStruct Type

_Table parsed from section 'Data Types':_

* In the Content Control Cluster, under the Data Types section, the entry for 'CatalogVendorID' is identified with an ID of '0' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The constraint 'all' indicates that this data type applies universally within its context. The conformance rule 'M' signifies that the 'CatalogVendorID' is a mandatory element. This means it is always required to be implemented in any device or application that supports the Content Control Cluster, with no exceptions or conditions.

* In the Content Control Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'ApplicationID', which is of the type 'string' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'ApplicationID' is a required element in the specification and must always be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

6.13.5.4.1. CatalogVendorID Field
This field SHALL indicate the CSA-issued vendor ID for the catalog. The DIAL registry SHALL use
value 0x0000.
Content App Platform providers will have their own catalog vendor ID (set to their own Vendor ID)
and will assign an ApplicationID to each Content App.
6.13.5.4.2. ApplicationID field
This field SHALL indicate the application identifier, expressed as a string, such as "PruneVideo" or
"Company X". This field SHALL be unique within a catalog.
6.13.5.5. TimeWindowStruct Type

_Table parsed from section 'Data Types':_

* The table row describes an element within the Content Control Cluster, specifically in the Data Types section, named "TimeWindowIndex." This element has an ID of '0' and is of type 'uint16', with a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed for use in certain contexts or implementations. The 'Conformance' is marked as 'M', which indicates that the "TimeWindowIndex" is a mandatory element. This means it is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* In the Content Control Cluster, under the Data Types section, the entry with ID '1' is named 'DayOfWeek' and is of the type 'DayOfWeekBitmap'. The 'Constraint' for this entry is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' for this entry is marked as 'M', which means that the 'DayOfWeek' element is mandatory. This implies that it is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Content Control Cluster, specifically in the Data Types section, with the ID '2' and the name 'TimePeriod'. This element is of the type 'list[TimePeriodStruct]', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this element is 'M', which means it is mandatory. This implies that the 'TimePeriod' element must always be implemented and supported in any device or application that uses the Content Control Cluster, without any conditions or exceptions.

6.13.5.5.1. TimeWindowIndex Field
This field SHALL indicate a unique index of a specific time window. This value may be used to indi
cate a selected time window which will be removed from the BlockContentTimeWindow attribute.
6.13.5.5.2. DayOfWeek Field
This field SHALL indicate a day of week.
6.13.5.5.3. TimePeriod Field
This field SHALL indicate one or more discrete time periods.
6.13.5.6. TimePeriodStruct type

_Table parsed from section 'Data Types':_

* In the Content Control Cluster, under the Data Types section, the table row describes an element named "StartHour" with an ID of '0'. This element is of type 'uint8', which means it is an unsigned 8-bit integer, and it has a constraint that limits its value to a range from 0 to 23, likely representing the hours of a day. The conformance rule for "StartHour" is marked as 'M', indicating that this element is mandatory. This means that "StartHour" is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* In the Content Control Cluster, under the Data Types section, the table row describes an element with the ID '1' named 'StartMinute'. This element is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint that limits its value to a range from 0 to 59. The conformance rule for 'StartMinute' is 'M', which stands for Mandatory. This means that the 'StartMinute' element is always required to be implemented in any device or application that supports the Content Control Cluster, with no exceptions or conditions.

* In the Content Control Cluster, under the Data Types section, the entry for 'EndHour' is identified by ID '2' and is of type 'uint8', with a constraint that limits its value between 0 and 23. The conformance rule for 'EndHour' is marked as 'M', which means that this element is mandatory. It is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions. This ensures that the 'EndHour' attribute is consistently available across all implementations that adhere to this specification.

* The table row describes an element within the Content Control Cluster, specifically under the Data Types section. The element is named "EndMinute" and is of type `uint8`, which is an unsigned 8-bit integer. It has a constraint that limits its value to a range from 0 to 59, likely representing the minutes in an hour. The conformance rule for "EndMinute" is marked as "M," which stands for Mandatory. This means that the "EndMinute" element is always required to be implemented in any device or application that supports the Content Control Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement status; it must be present in all relevant implementations.

6.13.5.6.1. StartHour Field
This field SHALL indicate the starting hour.
6.13.5.6.2. StartMinute Field
This field SHALL indicate the starting minute.
6.13.5.6.3. EndHour Field
This field SHALL indicate the ending hour. EndHour SHALL be equal to or greater than StartHour
6.13.5.6.4. EndMinute Field
This field SHALL indicate the ending minute. If EndHour is equal to StartHour then EndMinute
SHALL be greater than StartMinute. If the EndHour is equal to 23 and the EndMinute is equal to 59,
all contents SHALL be blocked until 23:59:59.

## Status Codes
6.13.6.1. StatusCodeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Status Codes':_

* In the Content Control Cluster, under the Status Codes section, the entry with the value '0x02' is named 'InvalidPINCode'. This status code indicates that the provided PIN code does not match the current PIN code. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context of the Matter specification, it would typically be a mandatory status code for any device or application implementing PIN-based access control. This means that any implementation of the Content Control Cluster that involves PIN verification must support this status code to indicate an invalid PIN entry.

* The table row entry pertains to the "Content Control Cluster" under the "Status Codes" section and describes a specific status code with the value `0x03`, named "InvalidRating." This status code indicates that the provided rating is not within the acceptable range of the corresponding rating list. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it would typically define when this status code must be implemented or recognized by devices supporting the Content Control Cluster. Without a specific conformance string, we can infer that the implementation of this status code might be mandatory or optional depending on the broader requirements of the cluster, but further details would be found in the full specification documentation.

* In the Content Control Cluster, under the Status Codes section, the entry for 'InvalidChannel' with a value of '0x04' indicates a status code used to signify that the provided channel(s) is invalid. The conformance rule for this entry is not explicitly provided in the table row data, but if we were to interpret a typical conformance string, it would dictate when this status code must be implemented or supported. For instance, if the conformance were 'M', it would mean that the 'InvalidChannel' status code is mandatory and must always be supported by devices implementing this cluster. If it were 'O', it would be optional, allowing implementers to choose whether to support it. Without a specific conformance string provided, we can only infer that the status code is a defined part of the cluster's specification, and its implementation would depend on the specific conformance rules applicable to the Content Control Cluster as a whole.

* In the Content Control Cluster, under the Status Codes section, the entry with the value '0x05' is named 'ChannelAlreadyExist'. This status code indicates that the channel(s) being provided already exist. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context of the Matter specification, this status code would typically be used to inform the system or user that an attempt to add or configure a channel has failed because the channel is already present. The absence of a specific conformance expression suggests that the usage of this status code is likely standard within the cluster's operations, meaning it should be implemented as part of the basic functionality of the Content Control Cluster.

_Table parsed from section 'Status Codes':_

* The table row entry pertains to the "Content Control Cluster" within the "Status Codes" section and describes a status code with the value `0x06`, named "ChannelNotExist". This status code indicates that the provided channel(s) do not exist in the BlockChannelList attribute. The conformance rule for this entry is not explicitly provided in the data, but typically, such status codes are integral to the functionality of a cluster, suggesting that their presence is likely mandatory for any implementation of the Content Control Cluster. However, without a specific conformance string, we cannot definitively categorize it under the rules provided. Therefore, it is assumed to be a standard part of the cluster's operation, essential for handling scenarios where a non-existent channel is referenced.

* In the Content Control Cluster, under the Status Codes section, the entry with the value `0x07` is named `UnidentifiableApplication`. This status code indicates that the provided application(s) could not be identified. The conformance rule for this entry is not explicitly provided in the table row data, which implies that its conformance might be described elsewhere in the documentation or follows a default rule not specified here. Typically, in such cases, the conformance could be considered as mandatory or optional based on the broader context of the specification. Without a specific conformance expression, it is essential to refer to the overall guidelines or additional documentation for precise implementation requirements.

* In the Content Control Cluster, under the Status Codes section, the entry with the value '0x08' is named 'ApplicationAlreadyExist'. This status code indicates that the provided application(s) already exist. The conformance rule for this entry is not explicitly provided in the table row data, which suggests that additional context or documentation is needed to determine its conformance status. Typically, such a status code would be used to inform a client that an operation cannot proceed because the application in question is already present, but without specific conformance information, we cannot definitively state whether this status code is mandatory, optional, or subject to any conditions.

* In the Content Control Cluster, under the Status Codes section, the entry with the value '0x09' is named 'ApplicationNotExist'. This status code indicates that the specified application(s) do not exist within the BlockApplicationList attribute. The conformance rule for this entry is not explicitly provided in the table row data, but based on the context, it would typically be interpreted as a mandatory status code that must be implemented to ensure proper error handling when an application is referenced that does not exist in the specified list. This ensures that devices can accurately report and handle situations where an application is missing, maintaining the integrity and reliability of the system's operation.

* The table row entry describes a status code within the Content Control Cluster, specifically under the Status Codes section. The status code has a value of '0x0A' and is named 'TimeWindowAlreadyExist'. This code indicates that the provided time window already exists in the BlockContentTimeWindow attribute. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely follows the general rules for status codes in the Matter specification. Typically, such status codes are mandatory (M) as they are essential for communicating specific conditions or errors within the cluster. Therefore, this status code is likely required to be implemented to ensure proper functionality and error handling within the Content Control Cluster.

* The table row entry for the Content Control Cluster, specifically within the Status Codes section, describes a status code with the value `0x0B` named `TimeWindowNotExist`. This status code indicates that the provided time window does not exist in the `BlockContentTimeWindow` attribute. The conformance rule for this entry is not explicitly provided in the data, but based on the context of the guide, it would typically specify when this status code must be implemented or recognized by devices supporting the Content Control Cluster. If a conformance rule were provided, it would dictate whether the implementation of this status code is mandatory, optional, or subject to certain conditions, as outlined by the conformance interpretation guide.

exists in BlockContentTimeWin

## Attributes

_Table parsed from section 'Attributes':_

* In the Content Control Cluster, within the Attributes section, there is an attribute identified by the ID '0x0000' and named 'Enabled'. This attribute is of the boolean type and applies to all constraints, with access rights specified as 'R V', meaning it can be read and verified. The conformance rule for this attribute is 'M', which indicates that it is mandatory. This means that the 'Enabled' attribute is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes an attribute named "OnDemandRatings" within the Content Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0001' and is of the type 'list[RatingNameStruct]', indicating it is a list structure containing rating names. The constraint 'all' suggests that all elements within this list must adhere to a specific condition or rule, though the exact nature of this constraint is not detailed here. The access level 'R V' implies that this attribute is readable and possibly volatile, meaning it might change frequently or require special handling. The conformance rule 'OCR' indicates that the attribute is Optional ('O') and has no dependencies, but it is also subject to a more complex conformance description elsewhere in the documentation ('CR'). This suggests that while the attribute is not mandatory, there are additional considerations or conditions that might affect its implementation or usage, which are detailed in another part of the specification.

* The table row describes an attribute named "OnDemandRatingThreshold" within the Content Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0002' and is of type 'string' with a maximum constraint of 8 characters. It has an access level of 'R V', indicating it is readable and can be viewed. The conformance rule for this attribute is 'OCR', which means it is Optional ('O') and has no dependencies, allowing it to be included at the implementer's discretion. The 'C' and 'R' in 'OCR' do not correspond to any specific conformance tags in the provided guide, suggesting they might be placeholders or context-specific indicators not detailed in the guide. Overall, the attribute is not required but can be implemented if desired, with no additional conditions or future mandatory status indicated.

* The table row describes an attribute named "ScheduledContentRatings" within the Content Control Cluster, identified by the ID '0x0003'. This attribute is of the type 'list[RatingNameStruct]', indicating it is a list composed of structures named RatingNameStruct. The constraint 'all' suggests that all elements in this list must adhere to certain unspecified conditions. The access level 'R V' implies that this attribute is readable and possibly has some vendor-specific access permissions. The conformance rule 'SCR' indicates that the attribute's requirement status is determined by the support of the feature or condition labeled 'SCR'. If the 'SCR' feature is supported, the attribute is mandatory; otherwise, its status is not explicitly defined in this entry.

* The table row describes an attribute named "ScheduledContentRatingThreshold" within the Content Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0004' and is of type 'string', with a constraint limiting its maximum length to 8 characters. The access level is 'R V', indicating it is readable and has a volatile nature. The conformance rule 'SCR' implies that the attribute is mandatory if the feature or condition represented by 'SCR' is supported. If 'SCR' is not supported, the attribute is not required. This conformance condition suggests that the attribute's necessity is directly tied to the presence of the 'SCR' feature within the device or system implementing the Matter specification.

* The table row describes an attribute within the Content Control Cluster, specifically the "ScreenDailyTime" attribute. This attribute has an ID of '0x0005' and is of type 'elapsed-s', which likely represents elapsed time in seconds. It has a constraint of a maximum value of 86400, which corresponds to the number of seconds in a day. The access permissions are 'R V', indicating that the attribute is readable and possibly volatile. The conformance rule 'ST' means that the attribute is mandatory if the feature 'ST' is supported. If 'ST' is not supported, the conformance rule does not specify an alternative, implying that the attribute is not required in such cases.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "RemainingScreenTime" within the Content Control Cluster, identified by the ID '0x0006'. This attribute is of type 'elapsed-s', indicating it measures elapsed time in seconds, with a constraint that its maximum value is 86,400 seconds (equivalent to 24 hours). The access permissions are 'R V', meaning it is readable and volatile. The conformance rule 'ST' implies that the attribute is mandatory when the feature or condition represented by 'ST' is supported. If 'ST' is not supported, the attribute is not required. This rule indicates that the presence of the "RemainingScreenTime" attribute is contingent upon the support of a specific feature or condition denoted by 'ST'.

* The table row describes an attribute named "BlockUnrated" within the Content Control Cluster, identified by the ID '0x0007'. This attribute is of type 'bool', meaning it holds a boolean value, and it has a constraint labeled 'all', indicating it applies universally within its context. The access level 'R V' suggests that the attribute is readable and possibly has additional access characteristics defined by 'V'. The conformance rule 'BU' indicates that the "BlockUnrated" attribute is mandatory if the feature 'BU' is supported. If the feature 'BU' is not supported, the conformance rule does not specify an alternative, implying that the attribute is not required in such cases.

* The table row describes an attribute within the Content Control Cluster, specifically the 'BlockChannelList' attribute, identified by the ID '0x0008'. This attribute is of type 'list[BlockChannelStruct]' and is constrained to include all elements. It has read (R) and view (V) access permissions. The conformance rule 'BC' indicates that the 'BlockChannelList' attribute is mandatory if the feature or condition represented by 'BC' is supported. In other words, if the 'BC' feature is part of the implementation, this attribute must be included.

* The table row describes an attribute within the Content Control Cluster, specifically the 'BlockApplicationList' attribute. This attribute is identified by the ID '0x0009' and is of the type 'list[AppInfoStruct]', which implies it holds a list of application information structures. The 'Constraint' is set to 'all', indicating that all entries in the list must meet certain criteria, though these criteria are not specified in the row. The 'Access' is 'R V', meaning the attribute is readable and has a volatile nature, which suggests that its value may change frequently or is not persistent. The 'Conformance' field is 'BA', which, according to the Matter Conformance Interpretation Guide, means that the 'BlockApplicationList' attribute is mandatory if the feature 'BA' is supported. In simpler terms, if the device or system supports the 'BA' feature, then it must include the 'BlockApplicationList' attribute as part of its implementation.

* The table row describes an attribute named "BlockContentTimeWindow" within the Content Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x000A' and is of the type 'list[TimeWindowStruct]', with a constraint limiting it to a maximum of 7 entries. The access level for this attribute is 'R V', indicating it is readable and possibly volatile. The conformance rule 'BTW' indicates that the attribute is mandatory if the feature 'BTW' (Block Time Window) is supported. If 'BTW' is not supported, the attribute is not required. This means that the presence of this attribute depends on the implementation of the 'BTW' feature within the device or system.

6.13.7.1. Enabled Attribute
This attribute SHALL indicate whether the Content Control feature implemented on a media device
is turned off (FALSE) or turned on (TRUE).
6.13.7.2. OnDemandRatings Attribute
This attribute SHALL provide the collection of ratings that are currently valid for this media device.
The items should honor the metadata of the on-demand content (e.g. Movie) rating system for one
country or region where the media device has been provisioned. For example, for the MPAA sys
tem, RatingName may be one value out of "G", "PG", "PG-13", "R", "NC-17".
The media device SHALL have a way to determine which rating system applies for the on-demand
content and then populate this attribute. For example, it can do it through examining the Location
attribute in the Basic Information cluster, and then determining which rating system applies.
The ratings in this collection SHALL be in order from a rating for the youngest viewers to the one
for the oldest viewers. Each rating in the list SHALL be unique.
6.13.7.3. OnDemandRatingThreshold Attribute
This attribute SHALL indicate a threshold rating as a content filter which is compared with the rat
ing for on-demand content. For example, if the on-demand content rating is greater than or equal to
OnDemandRatingThreshold, for a rating system that is ordered from lower viewer age to higher
viewer age, then on-demand content is not appropriate for the User and the Node SHALL prevent
the playback of content.
This attribute SHALL be set to one of the values present in the OnDemandRatings attribute.
When this attribute changes, the device SHOULD make the user aware of any limits of this feature.
For example, if the feature does not control content within apps, then the device should make this
clear to the user when the attribute changes.
6.13.7.4. ScheduledContentRatings Attribute
This attribute SHALL indicate a collection of ratings which ScheduledContentRatingThreshold can
be set to. The items should honor metadata of the scheduled content rating system for the country
or region where the media device has been provisioned.
The media device SHALL have a way to determine which scheduled content rating system applies
and then populate this attribute. For example, this can be done by examining the Location attribute
in Basic Information cluster, and then determining which rating system applies.
The ratings in this collection SHALL be in order from a rating for the youngest viewers to the one
for the oldest viewers. Each rating in the list SHALL be unique.
6.13.7.5. ScheduledContentRatingThreshold Attribute
This attribute SHALL indicate a threshold rating as a content filter which is used to compare with
the rating for scheduled content. For example, if the scheduled content rating is greater than or
equal to ScheduledContentRatingThreshold for a rating system that is ordered from lower viewer
age to higher viewer age, then the scheduled content is not appropriate for the User and SHALL be
blocked.
This attribute SHALL be set to one of the values present in the ScheduledContentRatings attribute.
When this attribute changes, the device SHOULD make the user aware of any limits of this feature.
For example, if the feature does not control content within apps, then the device should make this
clear to the user when the attribute changes.
6.13.7.6. ScreenDailyTime Attribute
This attribute SHALL indicate the amount of time (in seconds) which the User is allowed to spend
watching TV within one day when the Content Control feature is activated.
6.13.7.7. RemainingScreenTime Attribute
This attribute SHALL indicate the remaining screen time (in seconds) which the User is allowed to
spend watching TV for the current day when the Content Control feature is activated. When this
value equals 0, the media device SHALL terminate the playback of content.
This attribute SHALL be updated when the AddBonusTime command is received and processed suc
cessfully (with the correct PIN).
6.13.7.8. BlockUnrated Attribute
This attribute SHALL indicate whether the playback of unrated content is allowed when the Con
tent Control feature is activated. If this attribute equals FALSE, then playback of unrated content
SHALL be permitted. Otherwise, the media device SHALL prevent the playback of unrated content.
When this attribute changes, the device SHOULD make the user aware of any limits of this feature.
For example, if the feature does not control content within apps, then the device should make this
clear to the user when the attribute changes.
6.13.7.9. BlockChannelList Attribute
This attribute SHALL indicate a set of channels that SHALL be blocked when the Content Control
feature is activated.
6.13.7.10. BlockApplicationList Attribute
This attribute SHALL indicate a set of applications that SHALL be blocked when the Content Control
feature is activated.
6.13.7.11. BlockContentTimeWindow Attribute
This attribute SHALL indicate a set of periods during which the playback of content on media
device SHALL be blocked when the Content Control feature is activated. The media device SHALL
reject any request to play content during one period of this attribute. If it is entering any one period
of this attribute, the media device SHALL block content which is playing and generate an event
EnteringBlockContentTimeWindow. There SHALL NOT be multiple entries in this attribute list for
the same day of week.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command named "UpdatePIN" within the Content Control Cluster, specifically in the Commands section. This command is identified by the ID '0x00' and is directed from the client to the server, with a required response indicated by 'Y'. The access level for this command is marked as 'M T', suggesting it is mandatory and possibly tied to a specific access tier or condition. The conformance rule 'PM' indicates that the "UpdatePIN" command is currently in a provisional state, meaning its status is temporary. However, it is intended to become mandatory in the future, signifying that while it is not yet a permanent requirement, it is expected to be essential in upcoming iterations of the specification.

* The table row describes a command within the Content Control Cluster, specifically the "ResetPIN" command, which is directed from the client to the server and expects a "ResetPINResponse" in return. The access level for this command is denoted by 'A T', indicating specific access requirements. The conformance rule 'PM' signifies that the "ResetPIN" command is currently provisional, meaning its status is temporary and it is expected to become mandatory in the future. This implies that while it is not yet a required feature, it is anticipated to be essential in upcoming versions of the specification.

* The table row describes a command within the Content Control Cluster, specifically the "ResetPINResponse" command, which is sent from the server to the client. The command does not require a response, as indicated by 'Response': 'N'. The conformance rule 'PM' signifies that the "ResetPINResponse" command is currently provisional, meaning its status is temporary. However, it is intended to become mandatory in the future, indicating that while it is not yet required, it will be a required element in subsequent versions of the specification.

* In the Content Control Cluster, under the Commands section, the table row describes a command with the ID '0x03' named 'Enable', which is directed from the client to the server. This command requires a response, as indicated by 'Response: Y', and has an access level of 'M T', suggesting it is mandatory and possibly tied to a specific access tier or role. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the 'Enable' command must always be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* The table row describes a command named "Disable" within the Content Control Cluster, specifically in the Commands section. This command is identified by the ID '0x04' and is directed from the client to the server, requiring a response ('Y'). The access level for this command is marked as 'M T', indicating mandatory access with a specific access control requirement. The conformance rule for this command is 'M', which means that the "Disable" command is always mandatory. This implies that any implementation of the Content Control Cluster must support this command without exception, ensuring consistent functionality across devices that adhere to the Matter specification.

* The table row describes a command named "AddBonusTime" within the Content Control Cluster, specifically in the Commands section. This command is identified by the ID '0x05' and is directed from the client to the server, with a response expected ('Y'). The access level for this command is optional ('O'), indicating that it is not required and has no dependencies. The conformance rule 'ST' suggests that the command is mandatory if the feature or condition represented by 'ST' is supported. In summary, the "AddBonusTime" command must be implemented if the 'ST' feature is present; otherwise, it is not required.

* The table row describes a command named "SetScreenDailyTime" within the Content Control Cluster, which is directed from the client to the server. This command requires a response, as indicated by 'Response: Y', and it has mandatory access permissions ('Access: M'). The conformance rule 'ST' implies that the command is mandatory if the feature or condition represented by 'ST' is supported. In this context, 'ST' acts as a condition that, when true, makes the "SetScreenDailyTime" command a required element within the implementation of the Content Control Cluster. If 'ST' is not supported, the conformance rule does not specify an alternative, implying that the command is not required in such cases.

* The table row describes a command within the Content Control Cluster, specifically the "BlockUnratedContent" command, which is directed from the client to the server. The command has an ID of '0x07' and requires a response ('Y'). The access level for this command is marked as Mandatory ('M'), indicating that it must be implemented. The conformance rule 'BU' means that the "BlockUnratedContent" command is mandatory if the feature 'BU' is supported. If the feature 'BU' is not supported, the conformance rule does not specify an alternative, implying that the command is not required in such cases.

* The table row describes a command within the Content Control Cluster, specifically the "UnblockUnratedContent" command. This command is directed from the client to the server and requires a response, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'M', meaning that access to this command is mandatory. The 'Conformance' field is labeled 'BU', which, according to the conformance interpretation guide, indicates that the command is mandatory if the feature 'BU' is supported. If 'BU' is not supported, the conformance status of the command is not explicitly defined in this entry, implying it may not be required. Therefore, the command is essential for devices or implementations that support the 'BU' feature within the Content Control Cluster.

* The table row describes a command within the Content Control Cluster, specifically the "SetOnDemandRatingThreshold" command, which is directed from the client to the server. The command has an identifier of '0x09' and requires a response ('Y'). The access level for this command is mandatory ('M'), indicating that it must be implemented. The conformance rule 'OCR' suggests that the command is optional ('O') but has a conditional requirement based on the presence of certain features or conditions, which are not explicitly detailed in the provided data. This implies that while the command is generally optional, there may be specific scenarios or feature sets where its implementation becomes required.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically the "SetScheduledContentRatingThreshold" command, which is identified by the ID '0x0A'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning it must be implemented. The conformance rule 'SCR' indicates that the command is mandatory if the feature 'SCR' (Scheduled Content Rating) is supported by the device. If the device supports the SCR feature, it is required to implement this command; otherwise, the conformance rule does not apply.

* The table row describes a command within the Content Control Cluster, specifically the "AddBlockChannels" command, which is directed from the client to the server. The command has an ID of '0x0B' and requires a response ('Y'). The access level for this command is mandatory ('M'), indicating that it must be implemented. The conformance rule 'BC' means that the implementation of this command is mandatory if the feature or condition represented by 'BC' is supported. In essence, if the system supports the 'BC' feature, then the "AddBlockChannels" command must be included in the implementation.

* The table row describes a command within the Content Control Cluster, specifically the "RemoveBlockChannels" command, which is directed from the client to the server and requires a response. The access level for this command is mandatory, meaning it must be implemented. The conformance rule "BC" indicates that the "RemoveBlockChannels" command is mandatory if the feature represented by "BC" is supported. In this context, "BC" acts as a condition that, when true, necessitates the inclusion of this command in the implementation. If "BC" is not supported, the conformance rule does not specify an alternative, implying that the command is not required in that case.

* The table row describes a command within the Content Control Cluster, specifically the "AddBlockApplications" command, which is identified by the ID '0x0D'. This command is directed from the client to the server and requires a response, as indicated by 'Response': 'Y'. The access level for this command is mandatory ('Access': 'M'), meaning it must be implemented. The conformance rule 'BA' indicates that the command is mandatory if the feature 'BA' is supported. In simpler terms, if a device supports the 'BA' feature, it must also support the "AddBlockApplications" command.

* The table row describes a command within the Content Control Cluster, specifically the "RemoveBlockApplications" command, which is identified by the ID '0x0E'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning it must be implemented. The conformance rule 'BA' indicates that the command is mandatory if the feature or condition represented by 'BA' is supported. In other words, if the 'BA' feature is present, the "RemoveBlockApplications" command must be implemented; otherwise, the conformance rule does not specify any other requirements, implying it may not be required if 'BA' is not supported.

* In the Content Control Cluster, under the Commands section, the table row describes the command 'SetBlockContentTimeWindow' with an ID of '0x0F'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is mandatory ('M'), indicating that it must be implemented. The conformance rule 'BTW' specifies that the command is mandatory if the feature 'BTW' (presumably a feature related to blocking content within a time window) is supported. If the 'BTW' feature is not supported, the command is not required. This ensures that the command is only implemented in devices where the relevant feature is applicable.

* The table row entry describes a command within the Content Control Cluster, specifically the "RemoveBlockContentTimeWindow" command, which is identified by the ID '0x10'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is mandatory ('Access: M'), meaning it must be implemented. The conformance rule 'BTW' specifies that the command is mandatory if the feature 'BTW' (presumably a feature related to blocking time windows) is supported. Therefore, if a device supports the 'BTW' feature, it must implement the "RemoveBlockContentTimeWindow" command.

6.13.8.1. UpdatePIN Command
The purpose of this command is to update the PIN used for protecting configuration of the content
control settings. Upon success, the old PIN SHALL no longer work.
The PIN is used to ensure that only the Node (or User) with the PIN code can make changes to the
Content Control settings, for example, turn off Content Controls or modify the ScreenDailyTime. The
PIN is composed of a numeric string of up to 6 human readable characters (displayable) .
Upon receipt of this command, the media device SHALL check if the OldPIN field of this command
is the same as the current PIN. If the PINs are the same, then the PIN code SHALL be set to NewPIN.
Otherwise a response with InvalidPINCode error status SHALL be returned.
The media device MAY provide a default PIN to the User via an out of band mechanism. For security
reasons, it is recommended that a client encourage the user to update the PIN from its default value
when performing configuration of the Content Control settings exposed by this cluster. The Reset
PIN command can also be used to obtain the default PIN.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, under the Commands section, the table row describes a command named "OldPIN" with an ID of '0'. This command is of the type 'string' and is constrained to a maximum length of 6 characters. The conformance rule for "OldPIN" is marked as 'M', which means it is mandatory. This indicates that the "OldPIN" command is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

* In the Content Control Cluster, under the Commands section, there is an entry for a command named "NewPIN" with an ID of '1'. This command is of the type 'string' and has a constraint that limits its maximum length to 6 characters. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "NewPIN" command is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.1.1. OldPIN Field
This field SHALL specify the original PIN. Once the UpdatePIN command is performed successfully,
it SHALL be invalid.
6.13.8.1.2. NewPIN Field
This field SHALL indicate a new PIN for the Content Control feature.
6.13.8.2. ResetPIN Command
The purpose of this command is to reset the PIN.
If this command is executed successfully, a ResetPINResponse command with a new PIN SHALL be
returned.
6.13.8.3. ResetPINResponse Command
This command SHALL be generated in response to a ResetPIN command. The data for this com
mand SHALL be as follows:

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically the "PINCode" command. This command is of the type "string" and is constrained to a maximum length of 6 characters. The conformance rule for this command is marked as "M," which stands for Mandatory. This means that the "PINCode" command is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.3.1. PINCode Field
This field SHALL indicate a new PIN of the Content Control feature.
6.13.8.4. Enable Command
The purpose of this command is to turn on the Content Control feature on a media device.
Upon receipt of the Enable command, the media device SHALL set the Enabled attribute to TRUE.
6.13.8.5. Disable Command
The purpose of this command is to turn off the Content Control feature on a media device.
On receipt of the Disable command, the media device SHALL set the Enabled attribute to FALSE.
6.13.8.6. AddBonusTime Command
The purpose of this command is to add the extra screen time for the user.
If a client with Operate privilege invokes this command, the media device SHALL check whether
the PINCode passed in the command matches the current PINCode value. If these match, then the
RemainingScreenTime attribute SHALL be increased by the specified BonusTime value.
If the PINs do not match, then a response with InvalidPINCode error status SHALL be returned, and
no changes SHALL be made to RemainingScreenTime.
If a client with Manage privilege or greater invokes this command, the media device SHALL ignore
the PINCode field and directly increase the RemainingScreenTime attribute by the specified Bonus
Time value.
A server that does not support the PM feature SHALL respond with InvalidPINCode to clients that
only have Operate privilege unless:
• It has been provided with the PIN value to expect via an out of band mechanism, and
• The client has provided a PINCode that matches the expected PIN value.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, within the Commands section, the table row describes a command identified by 'ID' 0, named 'PINCode', which is of the 'string' type with a constraint of a maximum length of 6 characters. The conformance rule for this command is 'O', indicating that the 'PINCode' command is optional. This means that it is not required for implementation and has no dependencies on other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this command based on their specific needs or preferences.

* In the Content Control Cluster, under the Commands section, the table row describes a command identified by ID '1' with the name 'BonusTime'. This command is of the type 'elapsed-s', which likely refers to a time duration measured in seconds. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The default value for this command is set to 300 seconds. The conformance rule for 'BonusTime' is marked as 'M', meaning it is a Mandatory element. This indicates that the 'BonusTime' command is always required to be implemented in any device or system that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.6.1. PINCode Field
This field SHALL indicate the PIN.
This field SHALL be optional for clients with Manage or greater privilege but SHALL be mandatory
for clients with Operate privilege. The PIN provided in this field SHALL be used to guarantee that a
client with Operate permission is allowed to invoke this command only if the PIN passed in this
command is equal to the current PIN value.
6.13.8.6.2. BonusTime Field
This field SHALL indicate the amount of extra time (in seconds) to increase RemainingScreenTime.
This field SHALL NOT exceed the remaining time of this day.
6.13.8.7. SetScreenDailyTime Command
The purpose of this command is to set the ScreenDailyTime attribute.
Upon receipt of the SetScreenDailyTime command, the media device SHALL set the ScreenDaily
Time attribute to the ScreenTime value.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, under the Commands section, the table row describes a command named "ScreenTime" with an ID of '0'. This command is of the type 'elapsed-s', which likely represents elapsed seconds, and it has a constraint that limits its maximum value to 86,400 seconds (equivalent to 24 hours). The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "ScreenTime" command is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.7.1. ScreenTime Field
This field SHALL indicate the time (in seconds) which the User is allowed to spend watching TV on
this media device within one day.
6.13.8.8. BlockUnratedContent Command
The purpose of this command is to specify whether programs with no Content rating must be
blocked by this media device.
Upon receipt of the BlockUnratedContent command, the media device SHALL set the BlockUnrated
attribute to TRUE.
6.13.8.9. UnblockUnratedContent Command
The purpose of this command is to specify whether programs with no Content rating must be
blocked by this media device.
Upon receipt of the UnblockUnratedContent command, the media device SHALL set the BlockUn
rated attribute to FALSE.
6.13.8.10. SetOnDemandRatingThreshold Command
The purpose of this command is to set the OnDemandRatingThreshold attribute.
Upon receipt of the SetOnDemandRatingThreshold command, the media device SHALL check if the
Rating field is one of values present in the OnDemandRatings attribute. If not, then a response with
InvalidRating error status SHALL be returned.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, under the Commands section, there is an entry for a command named "Rating" with an ID of '0'. This command is of the type 'string' and is constrained to a maximum length of 8 characters. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Rating" command is always required to be implemented in any device or application that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.10.1. Rating
This field indicates a threshold rating for filtering on-demand content. This field SHALL be set to
one of the values present in the OnDemandRatings attribute
6.13.8.11. SetScheduledContentRatingThreshold Command
The purpose of this command is to set ScheduledContentRatingThreshold attribute.
Upon  receipt  of  the  SetScheduledContentRatingThreshold  command,  the  media  device  SHALL
check if the Rating field is one of values present in the ScheduledContentRatings attribute. If not,
then a response with InvalidRating error status SHALL be returned.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, under the Commands section, there is a command identified by the ID '0' named 'Rating'. This command is of the type 'string' and is constrained to a maximum length of 8 characters. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Content Control Cluster. There are no conditions or dependencies affecting its requirement; it must be included as specified.

6.13.8.11.1. Rating
This field indicates a threshold rating for filtering scheduled content. This field SHALL be set to one
of the values present in the ScheduledContentRatings attribute.
6.13.8.12. AddBlockChannels command
The purpose of this command is to set BlockChannelList attribute.
Upon receipt of the AddBlockChannels command, the media device SHALL check if the channels
passed in this command are valid. If the channel is invalid, then a response with InvalidChannel
error Status SHALL be returned.
If there is at least one channel in Channels field which is not in the BlockChannelList attribute, the
media device SHALL process the request by adding these new channels into the BlockChannelList
attribute and return a successful Status Response. During this process, the media device SHALL
assign one unique index to BlockChannelIndex field for every channel passed in this command.
If all channels in Channel field already exist in the BlockChannelList attribute, then a response with
ChannelAlreadyExist error Status SHALL be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically named "Channels," which is of the type `list[BlockChannelStruct]` and has a constraint labeled as "all." The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "Channels" command must always be implemented and supported in any device or application that adheres to the Matter specification for the Content Control Cluster. There are no conditions or exceptions; it is a required element without any dependencies or optionality.

6.13.8.12.1. Channels Field
This field indicates a set of channels that SHALL be blocked when the Content Control feature is
activated. This field SHALL be set to values present in ChannelList attribute in the Channel cluster.
The BlockChannelIndex field passed in this command SHALL be NULL.
6.13.8.13. RemoveBlockChannels command
The purpose of this command is to remove channels from the BlockChannelList attribute.
Upon receipt of the RemoveBlockChannels command, the media device SHALL check if the chan
nels  indicated  by  ChannelIndexes  passed  in  this  command  are  present  in  BlockChannelList
attribute. If one or more channels indicated by ChannelIndexes passed in this command field are
not present in the BlockChannelList attribute, then a response with ChannelNotExist error Status
SHALL be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically the "ChannelIndexes" command. This command has an ID of '0' and is of the type 'list[uint16]', indicating it is a list composed of 16-bit unsigned integers. The constraint 'all' suggests that this command applies universally within its context. The conformance rule 'M' signifies that the "ChannelIndexes" command is mandatory, meaning it is always required to be implemented in any device or application that supports the Content Control Cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

6.13.8.13.1. ChannelIndexes Field
This field SHALL specify a set of indexes indicating Which channels SHALL be removed from the
BlockChannelList attribute.
6.13.8.14. AddBlockApplications Command
The purpose of this command is to set applications to the BlockApplicationList attribute.
Upon receipt of the AddBlockApplications command, the media device SHALL check if the Applica
tions passed in this command are installed. If there is an application in Applications field which is
not identified by media device, then a response with UnidentifiableApplication error Status MAY be
returned.
If there is one or more applications which are not present in BlockApplicationList attribute, the
media device SHALL process the request by adding the new application to the BlockApplicationList
attribute and return a successful Status Response.
If all applications in Applications field are already present in BlockApplicationList attribute, then a
response with ApplicationAlreadyExist error Status SHALL be returned.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, within the Commands section, there is a command identified by ID '0' named 'Applications'. This command is of the type 'list[AppInfoStruct]' and has a constraint labeled 'all', indicating that it applies universally within its context. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'Applications' command is always required to be implemented in any device or system that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.14.1. Applications Field
This field indicates a set of applications that SHALL be blocked when the Content Control feature is
activated.
6.13.8.15. RemoveBlockApplications Command
The purpose of this command is to remove applications from the BlockApplicationList attribute.
Upon receipt of the RemoveBlockApplications command, the media device SHALL check if the
applications passed in this command present in the BlockApplicationList attribute. If one or more
applications in Applications field which are not present in the BlockApplicationList attribute, then a
response with ApplicationNotExist error Status SHALL be returned.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically the "Applications" command, which is identified by the ID '0'. This command is of the type 'list[AppInfoStruct]', indicating that it involves a list of application information structures, with the constraint specified as 'all', meaning all elements in the list must adhere to this structure. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "Applications" command is always required to be implemented in any device or system that supports the Content Control Cluster, with no exceptions or conditions altering this requirement.

6.13.8.15.1. Applications Field
This  field  indicates  a  set  of  applications  which  SHALL  be  removed  from  BlockApplicationList
attribute.
6.13.8.16. SetBlockContentTimeWindow Command
The purpose of this command is to set the BlockContentTimeWindow attribute.
Upon receipt of the SetBlockContentTimeWindow command, the media device SHALL check if the
TimeWindowIndex field passed in this command is NULL. If the TimeWindowIndex field is NULL,
the media device SHALL check if there is an entry in the BlockContentTimeWindow attribute which
matches with the TimePeriod and DayOfWeek fields passed in this command. * If Yes, then a
response with TimeWindowAlreadyExist error status SHALL be returned. * If No, then the media
device SHALL assign one unique index for this time window and add it into the BlockContent
TimeWindow list attribute.
If the TimeWindowIndex field is not NULL and presents in the BlockContentTimeWindow attribute,
the media device SHALL replace the original time window with the new time window passed in this
command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Content Control Cluster, specifically the "TimeWindow" command, which is of the type "TimeWindowStruct." The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "TimeWindow" command is always required to be implemented in any device or system that supports the Content Control Cluster, without any conditions or exceptions.

6.13.8.16.1. TimeWindow Field
This  field  SHALL  indicate  a  time  window  requested  to  set  to  the  BlockContentTimeWindow
attribute.
6.13.8.17. RemoveBlockContentTimeWindow Command
The purpose of this command is to remove the selected time windows from the BlockContent
TimeWindow attribute.
Upon receipt of the RemoveBlockContentTimeWindow command, the media device SHALL check if
the  time  window  index  passed  in  this  command  presents  in  the  BlockContentTimeWindow
attribute.
If one or more time window indexes passed in this command are not present in BlockContent
TimeWindow  attribute,  then  a  response  with  TimeWindowNotExist  error  status  SHALL  be
returned.

_Table parsed from section 'Commands':_

* In the Content Control Cluster, under the Commands section, the entry for 'TimeWindowIndexes' is identified by the ID '0' and is of the type 'list[uint16]'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'TimeWindowIndexes' command is always required to be implemented in any device or application that supports the Content Control Cluster. There are no conditions or dependencies affecting its requirement; it must be present in all cases.

6.13.8.17.1. TimeWindowIndexes Field
This field SHALL specify a set of time window indexes indicating which time windows will be
removed from the BlockContentTimeWindow attribute.

## Events

_Table parsed from section 'Events':_

* The table row entry pertains to the "RemainingScreenTimeExpired" event within the Content Control Cluster, specifically under the Events section. This event is identified by the ID '0x00' and is categorized with an 'INFO' priority level, indicating it provides informational messages. The 'Access' field marked as 'V' suggests that this event is visible or can be accessed in some manner. The 'Conformance' field is denoted as 'ST', which, according to the Matter Conformance Interpretation Guide, implies that the conformance is described elsewhere in the documentation, as 'ST' does not match any of the basic conformance tags or logical conditions provided. Therefore, further reference to the specific documentation is necessary to understand the precise requirements or conditions under which this event is implemented or supported.

* The table row describes an event named "EnteringBlockContentTimeWindow" within the Content Control Cluster, identified by the ID '0x01'. This event has an informational priority level and requires view access ('V'). The conformance rule 'BTW' indicates that the presence of this event is mandatory if the feature 'BTW' (presumably a specific feature related to the Content Control Cluster) is supported. If 'BTW' is not supported, the event is not required. This means that the implementation of this event is conditional upon the support of the 'BTW' feature, making it a mandatory element only in that context.

6.13.9.1. RemainingScreenTimeExpired Event
This event SHALL be generated when the RemainingScreenTime equals 0.
6.13.9.2. EnteringBlockContentTimeWindow Event
This event SHALL be generated when entering a period of blocked content as configured in the
BlockContentTimeWindow attribute.
Chapter 7. Robots
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter.
7.1. General Description

## Introduction
The clusters specified in this section define the operation of robotic devices, such as Robotic Vac
uum Cleaners (RVCs).

## Cluster List
This section lists the RVC specific clusters as specified in this chapter.
Table 12. Overview of the RVC Clusters

_Table parsed from section 'Cluster List':_

* The table row describes the "RVC Run Mode" cluster within the Content Control Cluster, identified by the Cluster ID `0x0054`. This cluster encompasses commands and attributes specifically designed for managing the running mode of a Robotic Vacuum Cleaner (RVC) device. The conformance rule for this cluster is not explicitly provided in the data snippet, but if we were to interpret it using the Matter Conformance Interpretation Guide, we would need to know the specific conformance string associated with this cluster. Generally, the conformance string would dictate whether the "RVC Run Mode" cluster is mandatory, optional, provisional, deprecated, or disallowed, potentially based on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirements for this cluster, but it would typically involve assessing the necessity of implementing this cluster based on the presence or absence of certain features or conditions in the device's context.

* The table row describes the "RVC Clean Mode" cluster within the Content Control Cluster, identified by the Cluster ID '0x0055'. This cluster includes commands and attributes specifically designed for managing the cleaning mode of a robotic vacuum cleaner (RVC) device. The conformance rule for this cluster is not explicitly provided in the data snippet, but if it were, it would dictate the conditions under which the "RVC Clean Mode" cluster is required, optional, or otherwise specified according to the Matter specification. This would involve interpreting any logical conditions or dependencies that determine the cluster's implementation requirements, ensuring that devices adhere to the specified guidelines for functionality and interoperability within the Matter ecosystem.

* The table row describes the "RVC Operational State" cluster within the Content Control Cluster, identified by the Cluster ID '0x0061'. This cluster includes commands and attributes essential for monitoring and controlling the operational state of a Robotic Vacuum Cleaner (RVC) device. The conformance rule for this cluster is not explicitly provided in the data, but based on the context, it likely defines when the cluster's features are required or optional. If a conformance string were provided, it would specify conditions under which the cluster's elements are mandatory, optional, provisional, deprecated, or disallowed, using logical expressions and conditionality as outlined in the Matter Conformance Interpretation Guide. Without the specific conformance string, we can infer that the cluster is designed to be integrated into devices that need to manage the operational states of RVCs, with its inclusion being determined by the specific requirements and features supported by the device.

