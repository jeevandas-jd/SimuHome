
# 2.11 Smoke CO Alarm Cluster

This cluster provides an interface for observing and managing the state of smoke and CO alarms.

## Data Types
2.11.5.1. AlarmStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, within the Data Types section, the table row describes a data type with the value '0' named 'Normal'. This represents the nominal state of the device, indicating that it is not in an alarming condition. The conformance rule for this entry is marked as 'M', meaning that this element is mandatory. This implies that the 'Normal' state must always be supported and implemented in any device using this cluster, as it is a fundamental requirement of the specification.

* In the Smoke CO Alarm Cluster, within the Data Types section, the table row describes an entry with the 'Value' of '1' and the 'Name' of 'Warning', which signifies a 'Warning state'. The 'Conformance' field for this entry is marked as 'O', indicating that this element is optional. This means that the 'Warning' state is not required to be implemented in devices or systems using this specification, and there are no dependencies or conditions that alter this optional status. Implementers have the discretion to include or exclude this feature based on their specific needs or preferences.

* In the Smoke CO Alarm Cluster, under the Data Types section, there is an entry with the value '2' named 'Critical', which represents a 'Critical state'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Critical' state must always be implemented and supported in any device or system utilizing this cluster, without any conditions or exceptions. It is an essential component of the Smoke CO Alarm Cluster, ensuring that the critical state is consistently recognized and handled across all implementations.

2.11.5.1.1. Normal Value
This value SHALL indicate that this alarm is not alarming.
2.11.5.1.2. Warning Value
This value SHALL indicate that this alarm is in a warning state. Alarms in this state SHOULD be sub
ject to being muted via physical interaction.
2.11.5.1.3. Critical Value
This value SHALL indicate that this alarm is in a critical state. Alarms in this state SHALL NOT be
subject to being muted via physical interaction.
2.11.5.2. SensitivityEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry for a data type named "High," which has a value of '0' and is summarized as representing "High sensitivity." The conformance rule for this entry is marked as 'O,' indicating that the "High" sensitivity data type is optional. This means that while it is available for implementation, it is not required and does not depend on any other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this data type based on their specific needs or product design without any obligation.

* In the Smoke CO Alarm Cluster, under the Data Types section, there is an entry for a data type named "Standard" with a value of '1', which is summarized as "Standard Sensitivity." The conformance rule for this entry is marked as 'M', indicating that this data type is mandatory. This means that the "Standard" sensitivity level must always be implemented and supported in any device or application that conforms to the Smoke CO Alarm Cluster specification. There are no conditions or exceptions to this requirement; it is an essential element of the specification.

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry with the value '2' named 'Low', which indicates a 'Low sensitivity' setting. The conformance rule for this entry is 'O', meaning that this 'Low sensitivity' setting is optional. It is not required to be implemented and does not depend on any other features or conditions within the Matter specification. This allows manufacturers the flexibility to include or exclude this setting based on their design preferences or product requirements.

2.11.5.3. ExpressedStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes a data type with the value '0' named 'Normal'. This represents the nominal state of the device, indicating that it is not in an alarming condition. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Normal' state is always required to be implemented in any device that conforms to this specification. There are no conditions or dependencies affecting its requirement; it must be present in all compliant devices.

* The table row describes an entry within the Smoke CO Alarm Cluster, specifically in the Data Types section. The entry is for a data type named "SmokeAlarm," which represents the state of a smoke alarm. The conformance rule for this entry is "SMOKE," indicating that the SmokeAlarm data type is mandatory if the feature or condition represented by "SMOKE" is supported. In other words, if the device or system includes the SMOKE feature, the SmokeAlarm data type must be implemented. If the SMOKE feature is not supported, the conformance rule does not apply, and the data type is not required.

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes an entry with the value '2', named 'COAlarm', which summarizes the state of a carbon monoxide (CO) alarm. The conformance rule 'CO' indicates that this element is mandatory if the feature 'CO' is supported. This means that if the device or system includes the capability to detect carbon monoxide, the 'COAlarm' data type must be implemented to represent the CO alarm state. If the 'CO' feature is not supported, the conformance rule does not apply, and the element is not required.

* In the Smoke CO Alarm Cluster, under the Data Types section, there is an entry for a data type named "BatteryAlert," which has a value of '3' and represents the "Battery Alert State." The conformance rule for this entry is marked as 'M,' which stands for Mandatory. This means that the "BatteryAlert" data type is a required element in the Smoke CO Alarm Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes an entry with the value '4' named 'Testing', which summarizes as 'Test in Progress'. The conformance rule for this entry is 'M', indicating that this element is Mandatory. This means that the 'Testing' data type is always required to be implemented in any device or application that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* In the Smoke CO Alarm Cluster, within the Data Types section, the table row describes an element named "HardwareFault" with a value of '5', which represents the "Hardware Fault Alert State." The conformance rule for this element is marked as 'M', indicating that it is mandatory. This means that the "HardwareFault" element is always required to be implemented in any device or system that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry for a data type named 'EndOfService', which has a value of '6' and is summarized as representing the 'End of Service Alert State'. The conformance rule for this entry is marked as 'M', indicating that this element is mandatory. This means that the 'EndOfService' data type must always be implemented in any device or application that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* In the Smoke CO Alarm Cluster, under the Data Types section, the entry for 'InterconnectSmoke' with a value of '7' represents the state of an interconnected smoke alarm. The conformance rule for this entry is 'O', which means that the 'InterconnectSmoke' element is optional. This indicates that while the element can be included in implementations of the Smoke CO Alarm Cluster, it is not required and does not have any dependencies or conditions that must be met for its inclusion.

* In the Smoke CO Alarm Cluster, under the Data Types section, the entry for 'InterconnectCO' with a value of '8' represents the state of an interconnected carbon monoxide (CO) alarm. The 'Summary' indicates that this data type is used to convey the status of interconnected CO alarms within a system. The 'Conformance' field is marked as 'O', which means that the inclusion of this data type is optional. It is not required for compliance with the Matter specification and does not depend on any other features or conditions. This allows manufacturers the flexibility to implement this feature based on their product design and market needs without it being a mandatory requirement.

2.11.5.3.1. Normal Value
This value SHALL indicate that this alarm is not alarming.
2.11.5.3.2. SmokeAlarm Value
This value SHALL indicate that this alarm is currently expressing visual indication of Smoke Alarm.
This value SHALL indicate that the alarm is currently expressing audible indication of Smoke
Alarm unless the DeviceMuted attribute is supported and set to Muted.
2.11.5.3.3. COAlarm Value
This value SHALL indicate that this alarm is currently expressing visual indication of CO Alarm.
This value SHALL indicate that the alarm is currently expressing audible indication of CO Alarm
unless the DeviceMuted attribute is supported and set to Muted.
2.11.5.3.4. BatteryAlert Value
This value SHALL indicate that this alarm is currently expressing visual indication of Critical Low
Battery. This value SHALL indicate that the alarm is currently expressing audible indication of Criti
cal Low Battery unless the DeviceMuted attribute is supported and set to Muted.
2.11.5.3.5. Testing Value
This value SHALL indicate that this alarm is currently expressing visual and audible indication of
SelfTest.
2.11.5.3.6. HardwareFault Value
This value SHALL indicate that this alarm is currently expressing visual indication of Hardware
Fault. This value SHALL indicate that the alarm is currently expressing audible indication of Hard
ware Fault unless the DeviceMuted attribute is supported and set to Muted.
2.11.5.3.7. EndOfService Value
This value SHALL indicate that this alarm is currently expressing visual indication of End Of Ser
vice. This value SHALL indicate that the alarm is currently expressing audible indication of End of
Service unless the DeviceMuted attribute is supported and set to Muted.
2.11.5.3.8. InterconnectSmoke Value
This value SHALL indicate that this alarm is currently expressing visual indication of Smoke Alarm
caused by Interconnect. This value SHALL indicate that the alarm is currently expressing audible
indication of Smoke Alarm caused by Interconnect unless the DeviceMuted attribute is supported
and set to Muted.
2.11.5.3.9. InterconnectCO Value
This value SHALL indicate that this alarm is currently expressing visual indication of CO Alarm
caused by Interconnect. This value SHALL indicate that the alarm is currently expressing audible
indication of CO Alarm caused by Interconnect unless the DeviceMuted attribute is supported and
set to Muted.
2.11.5.4. MuteStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry for a value labeled 'NotMuted', which corresponds to the state 'Not Muted' with a value of '0'. The conformance rule for this entry is marked as 'M', indicating that it is a Mandatory element. This means that the 'NotMuted' state must always be supported and implemented in any device or system that conforms to this specification. There are no conditions or exceptions; the presence of this element is required without any dependencies or optionality.

* In the Smoke CO Alarm Cluster, under the Data Types section, there is an entry with the value '1' named 'Muted', which is summarized as 'Muted'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Muted' data type must always be implemented and supported in any device or application that conforms to the Matter specification for this cluster. There are no conditions or exceptions; it is a required element.

2.11.5.4.1. NotMuted Value
This value SHALL indicate that the device is not muted.
2.11.5.4.2. Muted Value
This value SHALL indicate that the device is muted.
2.11.5.5. EndOfServiceEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes a data type with the value '0' named 'Normal', which indicates that the device has not expired. The conformance rule for this entry is 'M', meaning that this data type is mandatory. It is always required to be implemented in any device that supports the Smoke CO Alarm Cluster, without any conditions or exceptions. This ensures that all compliant devices can consistently report when they are in a normal, non-expired state.

* In the Smoke CO Alarm Cluster, under the Data Types section, there is an entry with the name "Expired" and a value of '1'. This entry signifies that the device has reached its end of service. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "Expired" data type is always required to be implemented in any device that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

2.11.5.5.1. Expired Value
This value SHALL indicate that the device has reached its end of service, and needs to be replaced.
2.11.5.5.2. Normal Value
This value SHALL indicate that the device has not yet reached its end of service, and does not need
to be imminently replaced.
2.11.5.6. ContaminationStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes a data type with the value '0' named 'Normal'. This represents the nominal state of the sensor, indicating that it is not contaminated. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Normal' state is a required element in the specification and must always be implemented in any device or system that adheres to the Matter specification for this cluster.

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry for a data type with the value '1', named 'Low', which summarizes a state of 'Low contamination'. The conformance rule for this entry is 'O', indicating that this element is optional. This means that the inclusion of this data type is not required and does not depend on any other conditions or features being supported. Devices implementing this cluster may choose to support this data type, but they are not obligated to do so under the Matter specification.

* In the Smoke CO Alarm Cluster, within the Data Types section, there is an entry with the value '2' named 'Warning', which represents a 'Warning state'. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'Warning' state is not a required element within the Smoke CO Alarm Cluster. Implementers of the Matter specification can choose to include this feature, but there are no dependencies or conditions that mandate its inclusion.

* In the Smoke CO Alarm Cluster, under the Data Types section, the table row describes a data type with the value '3', named 'Critical'. This state indicates a critical condition that will trigger nuisance alarms. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Critical' state is a required element in the specification and must be implemented in any device or system that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

2.11.5.6.1. Normal Value
This value SHALL indicate that the smoke sensor has nominal contamination levels, no customer
action is required.
2.11.5.6.2. Low Value
This value SHALL indicate that the smoke sensor has detectable contamination levels, but the cont
amination is too low to cause a visible or audible alarm.
2.11.5.6.3. Warning Value
This value SHALL indicate that the smoke sensor has contamination levels in a warning state. At
this level, the contamination may cause a visible or audible alarm. User intervention is suggested.
2.11.5.6.4. Critical Value
This value SHALL indicate that the smoke sensor has contamination levels in a critical state. At this
level, the contamination should cause a visible or audible alarm. User intervention is required. Crit
ical contamination of the sensor SHALL also be reflected as a HardwareFault.

## Attributes

_Table parsed from section 'Attributes':_

* In the Smoke CO Alarm Cluster, within the Attributes section, the table row describes an attribute with the ID '0x0000' named 'Expressed State'. This attribute is of the type 'ExpressedStateEnum' and is constrained to apply to all instances. The 'Quality' is marked as 'N', indicating a specific quality characteristic, while the 'Access' is defined as 'R V', meaning it is readable and volatile. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the 'Expressed State' attribute must always be implemented in any device or application that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* The table row describes an attribute named "SmokeState" within the Smoke CO Alarm Cluster, identified by the ID '0x0001'. This attribute is of the type 'AlarmStateEnum' and applies to all instances of the cluster. It is marked with a quality of 'N', indicating it is a non-volatile attribute, and has access permissions of 'R V', meaning it is readable and can be viewed. The conformance rule 'SMOKE' indicates that the "SmokeState" attribute is mandatory if the feature or condition represented by 'SMOKE' is supported. In other words, if the device or implementation includes the 'SMOKE' feature, then the "SmokeState" attribute must be present and implemented.

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the 'COState' attribute, which is identified by the ID '0x0002' and is of the type 'AlarmStateEnum'. This attribute is constrained to apply to all instances ('Constraint': 'all') and is marked with a quality of 'N', indicating it is non-volatile. The access level is 'R V', meaning it is readable and volatile. The conformance rule 'CO' indicates that the 'COState' attribute is mandatory if the feature 'CO' is supported. In other words, if a device supports the 'CO' feature, it must implement the 'COState' attribute.

* In the Smoke CO Alarm Cluster, within the Attributes section, the table row describes an attribute named "BatteryAlert" with an ID of '0x0003'. This attribute is of the type 'AlarmStateEnum' and has a constraint labeled 'all', indicating it applies universally within its context. The 'Quality' is marked as 'N', which typically denotes a specific quality or characteristic, though not detailed here. The 'Access' is specified as 'R V', meaning it is readable and possibly volatile, suggesting that its value can change frequently. The 'Conformance' is marked as 'M', which means that the "BatteryAlert" attribute is mandatory. This implies that any implementation of the Smoke CO Alarm Cluster must include this attribute, as it is essential for the cluster's functionality.

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the "DeviceMuted" attribute, which is identified by the ID `0x0004`. This attribute is of the type `MuteStateEnum` and applies to all instances of the cluster, as indicated by the constraint "all." The quality is marked as "N," and the access level is "R V," meaning it is readable and viewable. The conformance rule for this attribute is "O," which signifies that the "DeviceMuted" attribute is optional. This means that while it is not required for every implementation of the Smoke CO Alarm Cluster, it can be included at the discretion of the developer, with no dependencies or conditions affecting its inclusion.

* In the Smoke CO Alarm Cluster, within the Attributes section, there is an attribute identified by the ID '0x0005' named 'TestInProgress'. This attribute is of the boolean type and is constrained to apply universally ('all'). It has read and view access permissions ('R V'). The conformance rule for 'TestInProgress' is marked as 'M', which means it is a mandatory attribute. This indicates that the 'TestInProgress' attribute must always be implemented in any device or application that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the "HardwareFaultAlert" attribute. This attribute is identified by the ID '0x0006' and is of the boolean type, meaning it can hold a true or false value. The 'Constraint' field indicates that this attribute applies universally ('all'), and the 'Quality' field marked as 'N' suggests it does not have any special quality requirements. The 'Access' field 'R V' denotes that the attribute is readable and can be volatile. The 'Conformance' field is marked as 'M', which means that the "HardwareFaultAlert" attribute is mandatory. This implies that any implementation of the Smoke CO Alarm Cluster must include this attribute, ensuring that the device can alert users to any hardware faults.

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the "EndOfServiceAlert" attribute. This attribute is identified by the ID '0x0007' and is of the type 'EndOfServiceEnum'. It applies to all instances ('Constraint': 'all') and is of normal quality ('Quality': 'N'). The access permissions for this attribute are 'R V', indicating it is readable and can be viewed. The conformance rule for this attribute is 'M', which means it is mandatory. This implies that the "EndOfServiceAlert" attribute must always be implemented in any device or application that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the "InterconnectSmokeAlarm" attribute. This attribute is identified by the ID '0x0008' and is of the type 'AlarmStateEnum', which suggests it represents various states of an alarm. The 'Constraint' field indicates that this attribute applies universally ('all'), and the 'Access' field 'R V' denotes that it is readable and can be viewed. The 'Conformance' field is marked as 'O', meaning that the inclusion of this attribute is optional and does not depend on any specific conditions or features. Therefore, manufacturers can choose to implement this attribute, but it is not required for compliance with the Matter specification.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Smoke CO Alarm Cluster, specifically the 'InterconnectCOAlarm' attribute, which is identified by the ID '0x0009' and is of the type 'AlarmStateEnum'. This attribute has a constraint labeled as 'all', indicating it applies universally within its context. The access permissions are 'R V', meaning it is readable and can be viewed. The conformance rule for this attribute is 'O', which signifies that the 'InterconnectCOAlarm' attribute is optional. This means that while it is not required to be implemented, it can be included without any dependencies or conditions.

* In the Smoke CO Alarm Cluster, within the Attributes section, the entry for 'ContaminationState' with ID '0x000A' is of type 'ContaminationStateEnum' and has a constraint of 'all', meaning it applies universally within its context. The access level 'R V' indicates that this attribute is readable and can be viewed. The conformance rule '[SMOKE]' specifies that the 'ContaminationState' attribute is optional if the 'SMOKE' feature is supported. This means that if a device supports the 'SMOKE' feature, it may include the 'ContaminationState' attribute, but it is not required to do so.

* In the Smoke CO Alarm Cluster, within the Attributes section, the entry for 'SmokeSensitivityLevel' with ID '0x000B' is of type 'SensitivityEnum' and has a constraint of 'all', indicating it applies universally within the cluster. The access level 'RW VM' signifies that this attribute can be read and written, and it is visible to management. The conformance rule '[SMOKE]' indicates that the 'SmokeSensitivityLevel' attribute is optional and should be included if the feature 'SMOKE' is supported. If the 'SMOKE' feature is not supported, this attribute is not required.

* In the Smoke CO Alarm Cluster, within the Attributes section, the table row describes an attribute with the ID '0x000C' named 'ExpiryDate'. This attribute is of type 'epoch-s', indicating it represents a time value in epoch seconds, and it applies to all instances of the cluster as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'F', and the 'Access' is defined as 'R V', meaning it is readable and can be viewed. The 'Conformance' for this attribute is 'O', which signifies that the 'ExpiryDate' attribute is optional. This means that while it is not required for the implementation of the Smoke CO Alarm Cluster, it can be included at the discretion of the developer, and there are no dependencies or conditions that affect its optional status.

2.11.6.1. ExpressedState Attribute
This attribute SHALL indicate the visibly- and audibly-expressed state of the alarm. When multiple
alarm conditions are being reflected in the server, this attribute SHALL indicate the condition with
the highest priority. Priority order of conditions is determined by the manufacturer and SHALL be
supplied as a part of certification procedure. If the value of ExpressedState is not Normal, the
attribute corresponding to the value SHALL NOT be Normal. For example, if the ExpressedState is
set to SmokeAlarm, the value of the SmokeState will indicate the severity of the alarm (Warning or
Critical). Clients SHOULD also read the other attributes to be aware of further alarm conditions
beyond the one indicated in ExpressedState.
Visible expression is typically a LED light pattern. Audible expression is a horn or speaker pattern.
Audible expression SHALL BE suppressed if the DeviceMuted attribute is supported and set to
Muted.
2.11.6.2. SmokeState Attribute
This attribute SHALL indicate whether the device’s smoke sensor is currently triggering a smoke
alarm.
2.11.6.3. COState Attribute
This attribute SHALL indicate whether the device’s CO sensor is currently triggering a CO alarm.
2.11.6.4. BatteryAlert Attribute
This attribute SHALL indicate whether the power resource fault detection mechanism is currently
triggered at the device. If the detection mechanism is triggered, this attribute SHALL be set to Warn
ing or Critical, otherwise it SHALL be set to Normal. The battery state SHALL also be reflected in the
Power Source cluster representing the device’s battery using the appropriate supported attributes
and events.
2.11.6.5. DeviceMuted Attribute
This attribute SHALL indicate the whether the audible expression of the device is currently muted.
Audible expression is typically a horn or speaker pattern.
2.11.6.6. TestInProgress Attribute
This attribute SHALL indicate whether the device self-test is currently activated. If the device self-
test is activated, this attribute SHALL be set to True, otherwise it SHALL be set to False.
2.11.6.7. HardwareFaultAlert Attribute
This attribute SHALL indicate whether the hardware fault detection mechanism is currently trig
gered. If the detection mechanism is triggered, this attribute SHALL be set to True, otherwise it
SHALL be set to False.
2.11.6.8. EndOfServiceAlert Attribute
This attribute SHALL indicate whether the end-of-service has been triggered at the device. This
attribute SHALL be set to Expired when the device reaches the end-of-service.
2.11.6.9. InterconnectSmokeAlarm Attribute
This attribute SHALL indicate whether the interconnected smoke alarm is currently triggering by
branching devices. When the interconnected smoke alarm is being triggered, this attribute SHALL
be set to Warning or Critical, otherwise it SHALL be set to Normal.
2.11.6.10. InterconnectCOAlarm Attribute
This attribute SHALL indicate whether the interconnected CO alarm is currently triggering by
branching devices. When the interconnected CO alarm is being triggered, this attribute SHALL be
set to Warning or Critical, otherwise it SHALL be set to Normal.
2.11.6.11. ContaminationState Attribute
This attribute SHALL indicate the contamination level of the smoke sensor.
2.11.6.12. SmokeSensitivityLevel Attribute
This attribute SHALL indicate the sensitivity level of the smoke sensor configured on the device.
2.11.6.13. ExpiryDate Attribute
This attribute SHALL indicate the date when the device reaches its stated expiry date. After the
ExpiryDate has been reached, the EndOfServiceAlert SHALL start to be triggered. To account for
better customer experience across time zones, the EndOfServiceAlert MAY be delayed by up to 24
hours after the ExpiryDate. Similarly, clients MAY delay any actions based on the ExpiryDate by up
to 24 hours to best align with the local time zone.

## Commands

_Table parsed from section 'Commands':_

* In the Smoke CO Alarm Cluster, within the Commands section, the table row describes the 'SelfTestRequest' command, identified by the ID '0x00'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required to be implemented and has no dependencies. The conformance rule for 'SelfTestRequest' is also 'O', which signifies that the implementation of this command is entirely optional. There are no conditions or dependencies that mandate its inclusion, allowing developers the flexibility to decide whether or not to support this command in their devices.

2.11.7.1. SelfTestRequest Command
This command SHALL initiate a device self-test. The return status SHALL indicate whether the test
was successfully initiated. Only one SelfTestRequest may be processed at a time. When the value of
the ExpressedState attribute is any of SmokeAlarm, COAlarm, Testing, InterconnectSmoke, Inter
connectCO, the device SHALL NOT execute the self-test, and SHALL return status code BUSY.
Upon successful acceptance of SelfTestRequest, the TestInProgress attribute SHALL be set to True
and ExpressedState attribute SHALL be set to Testing. Any faults identified during the test SHALL
be reflected in the appropriate attributes and events. Upon completion of the self test procedure,
the SelfTestComplete event SHALL be generated, the TestInProgress attribute SHALL be set to False
and ExpressedState attribute SHALL be updated to reflect the current state of the server.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "SmokeAlarm" event, which has an ID of '0x00' and is categorized with a 'CRITICAL' priority. The 'Access' field marked as 'V' indicates that this event is visible or can be accessed in some way. The 'Conformance' field is labeled as 'SMOKE', which, according to the Matter Conformance Interpretation Guide, implies that the presence of this event is mandatory if the 'SMOKE' feature is supported by the device. In simpler terms, if a device supports the 'SMOKE' feature, it must implement the 'SmokeAlarm' event as part of its functionality.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "COAlarm" event, which has an ID of '0x01' and is categorized with a 'CRITICAL' priority. The 'Access' field is marked as 'V', indicating that this event is visible or accessible in some manner. The 'Conformance' field is specified as 'CO', meaning that the "COAlarm" event is mandatory if the feature or condition represented by 'CO' is supported. In other words, if the device or system includes the 'CO' feature, then it must implement the "COAlarm" event; otherwise, the conformance rule does not apply.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "LowBattery" event. This event has an ID of '0x02' and is categorized with a priority level of 'INFO', indicating it provides informational alerts. The 'Access' field is marked as 'V', which typically denotes visibility or read access. The 'Conformance' field is marked as 'M', meaning that the "LowBattery" event is mandatory. This implies that any implementation of the Smoke CO Alarm Cluster must include this event, as it is always required according to the Matter specification.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "HardwareFault" event. This event is identified by the ID '0x03' and is categorized with a priority level of 'INFO', indicating it provides informational messages. The 'Access' field is marked as 'V', which typically denotes visibility or read access to the event. The 'Conformance' field is marked as 'M', meaning that the "HardwareFault" event is mandatory. This implies that any implementation of the Smoke CO Alarm Cluster must include this event, as it is always required according to the Matter specification.

* The table row entry pertains to the "EndOfService" event within the Smoke CO Alarm Cluster, specifically under the Events section. This event is identified by the ID '0x04' and has a priority level of 'INFO', indicating it provides informational messages. The access level is denoted as 'V', which typically refers to visibility or read access, allowing the event to be observed or logged. The conformance rule for this event is marked as 'M', meaning it is mandatory. This implies that the "EndOfService" event must be implemented and supported in any device or application that adheres to the Matter specification for the Smoke CO Alarm Cluster, without any conditions or exceptions.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "SelfTestComplete" event. This event has an ID of '0x05' and is categorized with an 'INFO' priority level. The 'Access' field is marked as 'V', indicating that this event is visible. The 'Conformance' field is labeled as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "SelfTestComplete" event is always required to be implemented in any device or system that supports the Smoke CO Alarm Cluster. There are no conditions or dependencies that alter this requirement, making it a fundamental component of the cluster's functionality.

* In the Smoke CO Alarm Cluster, within the Events section, the entry with ID '0x06' is named 'AlarmMuted' and has a priority level of 'INFO'. The access level is denoted as 'V', which typically indicates that the event is visible or can be accessed in some manner. The conformance rule for 'AlarmMuted' is marked as 'O', meaning that this event is optional. This indicates that the implementation of the 'AlarmMuted' event is not required and does not depend on any other features or conditions within the Matter specification. Implementers have the discretion to include or exclude this event based on their specific needs or design choices.

* The table row describes an event named "MuteEnded" within the Smoke CO Alarm Cluster, specifically under the Events section. This event has an ID of '0x07' and is categorized with a priority level of 'INFO', indicating it provides informational updates. The 'Access' is marked as 'V', which typically denotes visibility or access level, though the specific meaning would depend on the broader context of the specification. The 'Conformance' for "MuteEnded" is listed as 'O', meaning this event is optional. It is not required for implementation and does not have any dependencies or conditions that would alter its optional status. Thus, developers can choose to implement this event based on their specific needs or preferences without any obligation from the Matter specification.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "InterconnectSmokeAlarm" event, identified by the ID '0x08'. This event is categorized with a "CRITICAL" priority, indicating its high importance in the system. The "Access" field marked as 'V' suggests that this event is visible or can be accessed in some manner. The conformance rule '[SMOKE]' indicates that the "InterconnectSmokeAlarm" event is optional if the feature 'SMOKE' is supported. This means that the implementation of this event is not mandatory but can be included if the device or system supports the smoke detection feature.

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "InterconnectCOAlarm" event, which has an ID of '0x09' and is classified with a 'CRITICAL' priority. The 'Access' is marked as 'V', indicating that it is visible or can be accessed in some way. The 'Conformance' field is specified as '[CO]', which means that the "InterconnectCOAlarm" event is optional and should be implemented only if the feature 'CO' (likely referring to Carbon Monoxide detection capability) is supported by the device. If the device does not support the 'CO' feature, this event is not required to be implemented.

* In the Smoke CO Alarm Cluster, within the Events section, there is an event identified by the ID '0x0A' named 'AllClear'. This event has a priority level of 'INFO' and requires 'V' access, which typically indicates a specific type of access permission or visibility requirement. The conformance rule for this event is marked as 'M', meaning it is mandatory. This indicates that the 'AllClear' event is a required element in the implementation of the Smoke CO Alarm Cluster, and it must be supported without any conditions or exceptions.

2.11.8.1. SmokeAlarm Event
This event SHALL be generated when SmokeState attribute changes to either Warning or Critical
state.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Smoke CO Alarm Cluster, within the Events section, the table row describes an event with the ID '0' named 'AlarmSeverityLevel'. This event is of the type 'AlarmStateEnum' and applies to all constraints. The conformance rule for 'AlarmSeverityLevel' is marked as 'M', which means it is mandatory. This indicates that the 'AlarmSeverityLevel' event is always required to be implemented in any device or system that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

2.11.8.1.1. AlarmSeverityLevel Field
This field SHALL indicate the current value of the SmokeState attribute.
2.11.8.2. COAlarm Event
This event SHALL be generated when COState attribute changes to either Warning or Critical state.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row entry pertains to the "AlarmSeverityLevel" event within the Smoke CO Alarm Cluster, specifically under the Events section. This event is characterized by the type "AlarmStateEnum" and applies universally, as indicated by the constraint "all." The conformance rule for this event is marked as "M," which stands for Mandatory. This means that the "AlarmSeverityLevel" event is a required element in the implementation of the Smoke CO Alarm Cluster, and it must always be included without exception.

2.11.8.2.1. AlarmSeverityLevel Field
This field SHALL indicate the current value of the COState attribute.
2.11.8.3. LowBattery Event
This event SHALL be generated when BatteryAlert attribute changes to either Warning or Critical
state.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "AlarmSeverityLevel" event. This event is characterized by the type "AlarmStateEnum" and applies universally, as indicated by the constraint "all." The conformance rule for this event is marked as "M," which means it is mandatory. This implies that the "AlarmSeverityLevel" event must always be implemented and supported in any device or system that utilizes the Smoke CO Alarm Cluster, without any conditions or exceptions.

2.11.8.3.1. AlarmSeverityLevel Field
This field SHALL indicate the current value of the BatteryAlert attribute.
2.11.8.4. HardwareFault Event
This event SHALL be generated when the device detects a hardware fault that leads to setting Hard
wareFaultAlert to True.
2.11.8.5. EndOfService Event
This event SHALL be generated when the EndOfServiceAlert is set to Expired.
2.11.8.6. SelfTestComplete Event
This event SHALL be generated when the SelfTest completes, and the attribute TestInProgress
changes to False.
2.11.8.7. AlarmMuted Event
This event SHALL be generated when the DeviceMuted attribute changes to Muted.
2.11.8.8. MuteEnded Event
This event SHALL be generated when DeviceMuted attribute changes to NotMuted.
2.11.8.9. InterconnectSmokeAlarm Event
This event SHALL be generated when the device hosting the server receives a smoke alarm from an
interconnected sensor.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row entry pertains to the "AlarmSeverityLevel" event within the Smoke CO Alarm Cluster, specifically under the Events section. The "AlarmSeverityLevel" is identified by the ID '0' and is of the type "AlarmStateEnum," with a constraint labeled as "all," indicating it applies universally within its context. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "AlarmSeverityLevel" event is a required element that must be implemented in any device or system that supports the Smoke CO Alarm Cluster, without any conditions or exceptions.

2.11.8.9.1. AlarmSeverityLevel Field
This field SHALL indicate the current value of the InterconnectSmokeAlarm attribute.
2.11.8.10. InterconnectCOAlarm Event
This event SHALL be generated when the device hosting the server receives a CO alarm from an
interconnected sensor.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event within the Smoke CO Alarm Cluster, specifically the "AlarmSeverityLevel" event. This event is identified by the ID '0' and is of the type 'AlarmStateEnum', which suggests it categorizes the severity of an alarm state. The constraint 'all' indicates that this event applies universally across all instances of the cluster. The conformance rule 'M' signifies that the "AlarmSeverityLevel" event is mandatory, meaning it is always required to be implemented in any device or application that supports the Smoke CO Alarm Cluster. There are no conditions or dependencies affecting this requirement, making it a fundamental component of the cluster's functionality.

2.11.8.10.1. AlarmSeverityLevel Field
This field SHALL indicate the current value of the InterconnectCOAlarm attribute.
2.11.8.11. AllClear Event
This event SHALL be generated when ExpressedState attribute returns to Normal state.