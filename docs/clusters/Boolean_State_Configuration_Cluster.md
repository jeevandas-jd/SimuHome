
# 1.8 Boolean State Configuration Cluster

This cluster is used to configure a boolean sensor, including optional state change alarm features
and configuration of the sensitivity level associated with the sensor.

## Data Types
1.8.5.1. AlarmModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Boolean State Configuration Cluster, under the Data Types section, the table row describes a feature named "Visual," which is associated with the bit '0' and summarized as "Visual alarming." The conformance rule for this feature is 'VIS.' According to the Matter Conformance Interpretation Guide, this indicates that the "Visual" feature is mandatory if the 'VIS' feature is supported. In other words, if the device or system supports the 'VIS' feature, then it must also support the "Visual alarming" capability. If 'VIS' is not supported, the conformance rule does not apply, and the feature is not required.

* In the context of the Boolean State Configuration Cluster, under the Data Types section, the table row describes a data type with the bit position '1', named 'Audible', which is summarized as 'Audible alarming'. The conformance rule for this entry is 'AUD'. According to the Matter Conformance Interpretation Guide, this means that the 'Audible' feature is mandatory if the 'AUD' feature is supported. If the 'AUD' feature is not supported, the conformance rule does not specify any alternative conditions, implying that the 'Audible' feature is not required. Thus, the presence of the 'Audible' feature is contingent upon the support of the 'AUD' feature within the device or application context.

1.8.5.2. SensorFaultBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the context of the Boolean State Configuration Cluster, within the Data Types section, the table row describes a data type with the bit position '0' named 'GeneralFault'. This entry indicates that an unspecified fault has been detected. The conformance rule for 'GeneralFault' is marked as 'M', which stands for Mandatory. This means that the 'GeneralFault' element is always required to be implemented in any device or application that supports this cluster, with no conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "CurrentSensitivityLevel" within the Boolean State Configuration Cluster. This attribute has an ID of '0x0000' and is of type 'uint8', with a constraint that it must not exceed the value of 'max (SupportedSensitivityLevels - 1)'. The quality is marked as 'N', indicating it is not nullable, and it has a default value of 'MS'. The access level is 'RW VO', meaning it is readable and writable, with value-only access. The conformance rule 'SENSLVL' indicates that the attribute is mandatory if the feature 'SENSLVL' is supported. In other words, if the device or system supports the sensitivity level feature, this attribute must be implemented; otherwise, it is not required.

* The table row describes an attribute named "SupportedSensitivityLevels" within the Boolean State Configuration Cluster. This attribute has an ID of '0x0001' and is of type 'uint8', with a constraint that its value must be between 2 and 10. The quality is marked as 'F', and it has a default value of 'MS'. The access level is 'R V', indicating it is readable and viewable. The conformance rule 'SENSLVL' indicates that the attribute is mandatory if the feature 'SENSLVL' is supported. In other words, if the device or implementation supports the 'SENSLVL' feature, the "SupportedSensitivityLevels" attribute must be included; otherwise, its inclusion is not required.

* The table row describes an attribute named "DefaultSensitivityLevel" within the Boolean State Configuration Cluster. This attribute has an ID of '0x0002' and is of type 'uint8'. It is constrained to a maximum value of 'SupportedSensitivityLevels - 1', indicating that its value must be less than the total number of supported sensitivity levels. The attribute has a quality of 'F', a default value of 'MS', and access permissions of 'R V', meaning it can be read and is volatile. The conformance rule '[SENSLVL]' specifies that the "DefaultSensitivityLevel" attribute is optional if the feature 'SENSLVL' is supported. This means that the presence of this attribute is not mandatory but can be included if the device supports the sensitivity level feature.

* In the Boolean State Configuration Cluster, within the Attributes section, the entry for 'AlarmsActive' is identified by the ID '0x0003' and is of the type 'AlarmModeBitmap'. This attribute has a constraint of 'all', a default value of '0', and access permissions denoted as 'R V', meaning it is readable and has volatile characteristics. The conformance rule 'VIS | AUD' indicates that the 'AlarmsActive' attribute is mandatory if either the 'VIS' (Visual) or 'AUD' (Audible) feature is supported. In simpler terms, if a device supports visual or audible alarm features, it must include the 'AlarmsActive' attribute.

* The table row describes an attribute named "AlarmsSuppressed" within the Boolean State Configuration Cluster, identified by the ID '0x0004'. This attribute is of the type 'AlarmModeBitmap' and is constrained to apply to 'all' instances, with a default value of '0'. It has an access level of 'R V', indicating it can be read and is volatile. The conformance rule for "AlarmsSuppressed" is 'SPRS', which, according to the Matter Conformance Interpretation Guide, is not a standard conformance expression. However, if we consider typical interpretations, 'SPRS' could imply a specific, possibly complex or described elsewhere, conformance condition. Without a direct match in the guide, it suggests that the conformance of this attribute might be detailed in another section of the documentation, requiring further consultation to fully understand its requirements and conditions.

* The table row describes an attribute named "AlarmsEnabled" within the Boolean State Configuration Cluster, specifically in the context of attributes. This attribute has an ID of '0x0005' and is of the type 'AlarmModeBitmap', with a constraint of 'all', indicating it applies universally within its context. The 'Quality' is marked as 'N', and it has a default value of 'MS'. The access level is 'R V', meaning it is readable and can be viewed. The conformance rule '[VIS | AUD]' indicates that the "AlarmsEnabled" attribute is optional if either the 'VIS' (Visual) or 'AUD' (Audio) feature is supported. If neither of these features is supported, the attribute is not required.

* The table row describes an attribute named "AlarmsSupported" within the Boolean State Configuration Cluster, specifically in the Attributes section. This attribute has an ID of '0x0006' and is of the type 'AlarmModeBitmap'. It is constrained to 'all', has a quality of 'F', a default value of '0', and access rights of 'R V' (Read and View). The conformance rule 'VIS | AUD' indicates that the "AlarmsSupported" attribute is mandatory if either the VIS (Visual) or AUD (Auditory) feature is supported. In simpler terms, this attribute must be implemented if the device supports visual or auditory alarm modes.

_Table parsed from section 'Attributes':_

* In the Boolean State Configuration Cluster, within the Attributes section, the entry for 'SensorFault' is identified by the ID '0x0007' and is of the type 'SensorFaultBitmap'. This attribute has a constraint of 'all', a default value of '0', and access permissions denoted as 'R V', which typically means it is readable and may have vendor-specific access conditions. The conformance for 'SensorFault' is marked as 'O', indicating that this attribute is optional. This means that the implementation of this attribute is not required and there are no dependencies or conditions that mandate its inclusion in a device or system.

1.8.6.1. CurrentSensitivityLevel Attribute
This attribute SHALL indicate the currently selected sensitivity level.
If a write interaction to this attribute contains an unsupported sensitivity value, a CONSTRAINT_ER
ROR status SHALL be returned.
1.8.6.2. SupportedSensitivityLevels Attribute
This attribute SHALL indicate the number of supported sensitivity levels by the device.
These supported sensitivity levels SHALL be ordered by sensitivity, where a value of 0 SHALL be
considered the lowest sensitivity level (least sensitive) and the highest supported value SHALL be
considered the highest sensitivity level.
The number of supported sensitivity levels SHOULD represent unique sensitivity levels supported
by the device.
1.8.6.3. DefaultSensitivityLevel Attribute
This attribute SHALL indicate the default sensitivity level selected by the manufacturer.
1.8.6.4. AlarmsActive Attribute
This attribute SHALL indicate which specific alarm modes on the server are currently active. When
the sensor is no longer triggered, this attribute SHALL be set to the inactive state, by setting the bit
to 0, for all supported alarm modes.
If an alarm mode is not supported, the bit indicating this alarm mode SHALL always be 0.
A bit SHALL indicate whether the alarm mode inactive or not:
• 0 = Inactive
• 1 = Active
1.8.6.5. AlarmsSuppressed Attribute
This attribute SHALL indicate which specific alarm modes on the server are currently suppressed.
When the sensor is no longer triggered, this attribute SHALL be set to the unsuppressed state, by
setting the bit to 0, for all supported alarm modes.
If an alarm mode is not supported, the bit indicating this alarm mode SHALL always be 0.
A bit SHALL indicate whether the alarm mode is suppressed or not:
• 0 = Not suppressed
• 1 = Suppressed
1.8.6.6. AlarmsEnabled Attribute
This attribute SHALL indicate the alarm modes that will be emitted if the sensor is triggered.
If an alarm mode is not supported, the bit indicating this alarm mode SHALL always be 0.
A bit SHALL indicate whether the alarm mode is enabled or disabled:
• 0 = Disabled
• 1 = Enabled
1.8.6.7. AlarmsSupported Attribute
This attribute SHALL indicate the alarms supported by the sensor.
A bit SHALL indicate whether the alarm mode is supported:
• 0 = Not supported
• 1 = Supported
1.8.6.8. SensorFault Attribute
This attribute SHALL indicate any faults registered by the device.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command named "SuppressAlarm" within the Boolean State Configuration Cluster, specifically in the context of commands. This command is identified by the ID '0x00' and is directed from the client to the server, with a response expected ('Response': 'Y'). The access level for this command is optional ('Access': 'O'), meaning it is not required and has no dependencies. The conformance rule 'SPRS' indicates that the conformance status is described elsewhere in the documentation, suggesting that the conditions or requirements for this command are too complex to be captured by a simple tag or expression. Therefore, to fully understand when and how this command should be implemented, one would need to refer to the detailed description provided in the relevant section of the Matter specification.

* In the Boolean State Configuration Cluster, under the Commands section, the command with ID '0x01' named 'EnableDisableAlarm' is directed from the client to the server and requires a response. The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'VIS | AUD' indicates that this command is mandatory if either the 'VIS' (Visual) feature or the 'AUD' (Audio) feature is supported. In other words, the command must be implemented if the device supports visual or audio features, ensuring that alarms can be enabled or disabled based on these capabilities.

1.8.7.1. SuppressAlarm Command

_Table parsed from section 'Commands':_

* The table row describes a command named "AlarmsToSuppress" within the Boolean State Configuration Cluster, specifically in the Commands section. This command is identified by the ID '0' and is of the type 'AlarmModeBitmap', with a constraint labeled as 'all'. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "AlarmsToSuppress" command is always required to be implemented in any device or application that supports the Boolean State Configuration Cluster, without any conditions or exceptions.

1.8.7.1.1. AlarmsToSuppress Field
This field SHALL indicate the alarm modes to suppress.
1.8.7.1.2. Effect on Receipt
If any of the requested alarm modes are not supported this command SHALL be ignored and the
server SHALL return an CONSTRAINT_ERROR status code.
If any of the requested alarm modes are not active, in case the sensor is not triggered or the alarm
mode is disabled/not supported, this command SHALL be ignored and the server SHALL return an
INVALID_IN_STATE status code.
In the case an alarm is already suppressed and the specific bit is set in the AlarmsSuppressed
attribute, the bit SHALL be ignored and the remaining bits SHALL be evaluated.
For the valid bits in the AlarmsToSuppress field, the device SHALL suppress the specified alarm
modes as requested in the AlarmsToSuppress field and set the AlarmsSuppressed attribute accord
ingly.
1.8.7.2. EnableDisableAlarm Command

_Table parsed from section 'Commands':_

* In the Boolean State Configuration Cluster, under the Commands section, the table row describes a command identified as 'AlarmsToEnableDisable' with an ID of '0'. This command is of the type 'AlarmModeBitmap' and is constrained to apply to 'all', indicating it is universally applicable within its context. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'AlarmsToEnableDisable' command is always required to be implemented in any device or application that supports the Boolean State Configuration Cluster, without any conditions or exceptions.

1.8.7.2.1. AlarmsToEnableDisable Field
This field SHALL indicate the alarm modes to either enable or disable depending on the bit status,
as specified for the AlarmsEnabled attribute.
1.8.7.2.2. Effect on Receipt
If any of the requested alarm modes are not supported this command SHALL be ignored and the
server SHALL return an CONSTRAINT_ERROR status code.
If all the bits are valid, the value of the AlarmsEnabled attribute SHALL be set to the value of the
AlarmsToEnableDisable field.
If an alarm mode is being enabled and the trigger condition is met, the device SHALL immediately
activate the alarm mode and set the associated bit in the AlarmsActive attribute.
If an alarm mode is being disabled, any alarm mode which is either in the active or suppressed
state SHALL be cleared and the alarm mode SHALL be considered not active.

## Events

_Table parsed from section 'Events':_

* The table row describes an event named "AlarmsStateChanged" within the Boolean State Configuration Cluster, specifically under the Events section. This event has an ID of '0x00' and is categorized with a priority level of 'INFO'. The access level is marked as 'V', indicating it is visible. The conformance rule 'VIS | AUD' specifies that the "AlarmsStateChanged" event is mandatory if either the VIS (Visual) feature or the AUD (Audio) feature is supported. In simpler terms, the event must be implemented if the device supports visual or audio capabilities, ensuring that changes in the alarm state are communicated through these modalities if available.

* The table row describes an event named "SensorFault" within the Boolean State Configuration Cluster, specifically under the Events section. This event has an ID of '0x01' and is categorized with a priority level of 'INFO', indicating it provides informational messages. The 'Access' field is marked as 'V', which typically denotes visibility or read access. The 'Conformance' field is labeled as 'O', meaning that the "SensorFault" event is optional. This implies that the implementation of this event is not required and does not depend on any specific conditions or features. Developers have the discretion to include or exclude this event based on their specific application needs or preferences.

1.8.8.1. AlarmsStateChanged Event
This event SHALL be generated after any bits in the AlarmsActive and/or AlarmsSuppressed attrib
utes change. This MAY occur in situations such as when internal processing by the server deter
mines that an alarm mode becomes active or inactive, or when the SuppressAlarm or EnableDis
ableAlarm commands are processed in a way that some alarm modes becomes suppressed, active
or inactive.
If several alarm modes change state at the same time, a single event combining multiple changes
MAY be emitted instead of multiple events each representing a single change.

_Table parsed from section 'Events':_

* In the Boolean State Configuration Cluster, under the Events section, the table row describes an event named "AlarmsActive" with an ID of '0'. This event is of the type "AlarmModeBitmap" and has a constraint labeled as "all," indicating it applies universally within its context. The conformance rule for "AlarmsActive" is marked as 'M', which means it is mandatory. This implies that the "AlarmsActive" event must always be implemented and supported in any device or application that uses the Boolean State Configuration Cluster, without any conditions or exceptions.

* In the Boolean State Configuration Cluster, under the Events section, the entry with ID '1' is named 'AlarmsSuppressed' and is of the type 'AlarmModeBitmap', with a constraint labeled as 'all'. The conformance rule for this entry is 'SPRS', which is not directly explained by the basic conformance tags or expressions provided in the guide. However, it suggests a specific conformance status that might be defined elsewhere in the Matter specification documentation, possibly indicating a specialized or complex condition for when this element is required. Typically, such a conformance string would imply that the element's requirement is described in detail in another section of the documentation, beyond the basic tags and expressions. Therefore, to fully understand the conformance of 'AlarmsSuppressed', one would need to refer to the specific section of the Matter specification where 'SPRS' is elaborated.

1.8.8.1.1. AlarmsActive Field
This  field  SHALL  indicate  the  state  of  active  alarm  modes,  as  indicated  by  the  AlarmsActive
attribute, at the time the event was generated.
1.8.8.1.2. AlarmsSuppressed Field
This field SHALL indicate the state of suppressed alarm modes, as indicated by the AlarmsSup
pressed attribute, at the time the event was generated.
1.8.8.2. SensorFault Event
This event SHALL be generated when the device registers or clears a fault.

_Table parsed from section 'Events':_

* The table row describes an event named "SensorFault" within the Boolean State Configuration Cluster, specifically under the Events section. The event is identified by the ID '0' and is of the type 'SensorFaultBitmap', with a constraint labeled as 'all'. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "SensorFault" event is always required to be implemented in any device or application that supports the Boolean State Configuration Cluster, without any conditions or exceptions.

1.8.8.2.1. SensorFault Field
This field SHALL indicate the value of the SensorFault attribute, at the time this event is generated.