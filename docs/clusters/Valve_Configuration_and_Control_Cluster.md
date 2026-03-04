
# 4.6 Valve Configuration and Control Cluster

This cluster is used to configure a valve.

## Data Types
4.6.5.1. ValveFaultBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the Valve Configuration and Control Cluster, under the Data Types section, the table row describes a data element named "GeneralFault," which is associated with bit '0'. The summary indicates that this element represents an unspecified fault detected within the system. The conformance rule for "GeneralFault" is marked as 'M', which stands for Mandatory. This means that the "GeneralFault" element is always required to be implemented in any device or system that conforms to this specification. There are no conditions or dependencies that alter its mandatory status, ensuring that it is a fundamental part of the Valve Configuration and Control Cluster.

* In the Valve Configuration and Control Cluster, under the Data Types section, the table row describes a data element with the bit position '1', named 'Blocked', which indicates that the valve is blocked. The conformance rule for this element is 'M', meaning it is mandatory. This implies that the 'Blocked' data element must always be implemented and supported in any device or application using this cluster, without any conditions or exceptions.

* In the Valve Configuration and Control Cluster, under the Data Types section, the table row describes a data element with the bit position '2', named 'Leaking'. This element indicates whether the valve has detected a leak. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'Leaking' data element is always required to be implemented in any device or system that conforms to this specification. There are no conditions or dependencies associated with this requirement; it must be present in all cases.

* In the Valve Configuration and Control Cluster, under the Data Types section, there is a table entry for a bit labeled 'NotConnected' with a value of '3'. This bit indicates that no valve is connected to the controller. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'NotConnected' bit is a required element in the specification and must always be implemented in any device or system using this cluster. There are no conditions or exceptions; it is an essential part of the Valve Configuration and Control Cluster's functionality.

* In the Valve Configuration and Control Cluster, within the Data Types section, there is an entry for a data type named "ShortCircuit," which is represented by bit 4. This entry indicates that the system can detect a short circuit condition. The conformance rule for "ShortCircuit" is marked as "M," which stands for Mandatory. This means that the detection of a short circuit is a required feature for any implementation of this cluster, and it must always be supported without any conditions or exceptions.

* In the Valve Configuration and Control Cluster, under the Data Types section, the entry for 'Bit' 5 is named 'CurrentExceeded'. This entry indicates that the available current has been exceeded. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'CurrentExceeded' element is always required to be implemented in any device or system that supports this cluster, without any conditions or exceptions.

4.6.5.2. ValveStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Valve Configuration and Control Cluster, under the Data Types section, the table row describes a data entry with the value '0', named 'Closed', which indicates that the valve is in a closed position. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that the 'Closed' state must always be supported and implemented in any device or system utilizing this cluster, without any conditions or exceptions.

* In the Valve Configuration and Control Cluster, under the Data Types section, the table row describes a data type with the name "Open," which has a value of '1' and indicates that the valve is in an open position. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "Open" data type is always required to be implemented in any device or system that conforms to this specification. There are no conditions or dependencies affecting its mandatory status; it must be supported in all cases.

* In the Valve Configuration and Control Cluster, under the Data Types section, the entry for 'Transitioning' with a value of '2' indicates that this data type represents the state of a valve transitioning between closed and open positions or between different levels. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. This ensures that the transitioning state is consistently recognized and handled across all implementations using this specification.

## Status Codes
4.6.6.1. StatusCodeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Status Codes':_

* In the Valve Configuration and Control Cluster, under the Status Codes section, the entry with the value '0x02' is named 'FailureDueToFault'. This status code indicates that the requested action could not be performed because of a fault on the valve. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'FailureDueToFault' status code is always required to be implemented in any device or system that supports the Valve Configuration and Control Cluster, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "OpenDuration" within the Valve Configuration and Control Cluster, specifically in the context of attributes. This attribute has an ID of '0x0000' and is of type 'elapsed-s', indicating it measures elapsed time in seconds. The attribute has a constraint that requires a minimum value of 1. The 'Quality' is marked as 'X', meaning it is explicitly disallowed in certain contexts, although this does not affect its conformance. The default value for this attribute is 'null', and it has 'R V' access, which typically means it is readable and possibly volatile. The conformance rule 'M' indicates that the "OpenDuration" attribute is mandatory, meaning it is always required to be implemented in any device that supports the Valve Configuration and Control Cluster.

* The table row describes an attribute named "DefaultOpenDuration" within the Valve Configuration and Control Cluster, identified by the ID '0x0001'. This attribute is of type 'elapsed-s', indicating it measures elapsed time in seconds, with a minimum constraint of 1 second. The quality is marked as 'XN', meaning it is not allowed to be null. The default value is 'null', and it has read-write access with volatile (VO) quality, suggesting that changes to this attribute might not persist across resets. The conformance rule 'M' signifies that this attribute is mandatory, meaning it is always required to be implemented in any device supporting this cluster.

* The table row entry describes an attribute named "AutoCloseTime" within the Valve Configuration and Control Cluster. This attribute has an ID of '0x0002' and is of type 'epoch-us', which indicates it represents a time value in microseconds since the epoch. The constraint 'all' suggests that this attribute is applicable to all instances of the cluster. The quality 'X' indicates that the attribute is explicitly disallowed, meaning it should not be implemented or used in any device conforming to the current Matter specification. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule 'TS' is not directly explained in the provided conformance interpretation guide, suggesting that the conformance condition might be described elsewhere in the documentation or is a placeholder for a more detailed explanation. Overall, this entry specifies an attribute that is not permitted for use in compliant devices, with its conformance details potentially requiring further clarification from additional documentation.

* The table row describes an attribute named "RemainingDuration" within the Valve Configuration and Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x0003' and is of type 'elapsed-s', indicating it measures elapsed time in seconds. The 'Constraint' is marked as 'all', suggesting it applies universally within its context. The 'Quality' is noted as 'X Q', meaning it is disallowed and has a quality constraint. The default value for this attribute is 'null', and its access is defined as 'R V', indicating it is readable and volatile. The 'Conformance' is marked as 'M', which means this attribute is mandatory and must always be implemented in devices that support this cluster.

* The table row describes an attribute named "CurrentState" within the Valve Configuration and Control Cluster, specifically in the Attributes section. This attribute has an ID of '0x0004' and is of the type 'ValveStateEnum', which likely enumerates the possible states of a valve. The 'Constraint' is listed as 'all', suggesting that this attribute applies universally within the context of the cluster. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed from having any quality-related features. The 'Default' value is 'null', meaning it does not have a predefined default state. The 'Access' is 'R V', which implies that the attribute is readable and possibly volatile, meaning its value can change without external intervention. The 'Conformance' is 'M', which means that this attribute is mandatory and must always be implemented in any device that supports the Valve Configuration and Control Cluster.

* In the Valve Configuration and Control Cluster, within the Attributes section, the table row describes the 'TargetState' attribute. This attribute has an ID of '0x0005' and is of the type 'ValveStateEnum', with a constraint of 'all', meaning it applies universally within its context. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed from certain quality-related considerations. The default value is 'null', and it has an access level of 'R V', which means it is readable and can be verified. The conformance rule for 'TargetState' is 'M', signifying that this attribute is mandatory and must always be implemented in any device that supports the Valve Configuration and Control Cluster.

* The table row describes an attribute named "CurrentLevel" within the Valve Configuration and Control Cluster, identified by the ID '0x0006'. This attribute is of the type 'percent' and applies to all constraints. Its quality is marked as 'X', meaning it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule 'LVL' indicates that the attribute is mandatory if the feature 'LVL' is supported. If 'LVL' is not supported, the attribute is not required. This entry specifies that the "CurrentLevel" attribute should be implemented only when the specific condition related to 'LVL' is met, otherwise, it should not be included.

* The table row describes an attribute named "TargetLevel" within the Valve Configuration and Control Cluster, identified by ID '0x0007'. This attribute is of type 'percent' and has a constraint labeled 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', meaning it is explicitly disallowed in terms of quality considerations. The default value for this attribute is 'null', and it has access permissions 'R V', which typically means it is readable and possibly volatile. The conformance rule 'LVL' indicates that the presence of this attribute is mandatory if the feature 'LVL' is supported. If 'LVL' is not supported, the attribute is not required.

* The table row describes an attribute named "DefaultOpenLevel" within the Valve Configuration and Control Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0008' and is of the type 'percent', constrained to values between 1 and 100. It has a default value of 100 and is accessible with read-write (RW) and view-only (VO) permissions. The 'Quality' is marked as 'N', indicating no special quality requirements. The conformance rule '[LVL]' indicates that the "DefaultOpenLevel" attribute is optional if the condition 'LVL' is true, meaning that the attribute is not required unless the specific feature or condition represented by 'LVL' is supported.

* In the Valve Configuration and Control Cluster, under the Attributes section, the entry for 'ValveFault' with ID '0x0009' is defined. This attribute is of type 'ValveFaultBitmap', which indicates it is a bitmap used to represent various fault conditions of a valve. The 'Constraint' is set to 'all', meaning it can represent all possible fault states. The default value for this attribute is '0', suggesting that no faults are present by default. The 'Access' is marked as 'R V', indicating that the attribute is readable and volatile, meaning its value can change without a write operation. The 'Conformance' is 'O', which means that the 'ValveFault' attribute is optional. It is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an attribute named "LevelStep" within the Valve Configuration and Control Cluster, specifically under the Attributes section. This attribute has an ID of '0x000A' and is of type 'uint8', constrained to values between 1 and 50, with a default value of 1. It has a quality designation of 'F' and access permissions of 'R V', indicating it can be read and is volatile. The conformance rule '[LVL]' means that the "LevelStep" attribute is optional and should be implemented if the feature or condition represented by 'LVL' is supported. If 'LVL' is not supported, the attribute is not required.

4.6.7.1. OpenDuration Attribute
This attribute SHALL indicate the total duration, in seconds, for which the valve will remain open
for this current opening.
A value of null SHALL indicate the duration is not set, meaning that the valve will remain open
until closed by the user or some other automation.
4.6.7.2. DefaultOpenDuration Attribute
This attribute SHALL indicate the default duration, in seconds, for which the valve will remain
open, if the OpenDuration field is not present in the Open command.
A value of null SHALL indicate the duration is not set, meaning that the valve will remain open
until closed by the user or some other automation.
4.6.7.3. AutoCloseTime Attribute
This attribute SHALL indicate the UTC time when the valve will close, depending on value of the
OpenDuration attribute.
This attribute SHALL be null:
• When OpenDuration is null, or
• When the valve does not have a synchronized UTCTime in the Time Synchronization cluster, or
• When the valve is closed.
When the value of this attribute is earlier or equal to the current UTC time, the valve SHALL auto
matically transition to its closed position. The behavior of transitioning to the closed position,
SHALL match the behavior described in the Close command.
If this attribute is not null and the Time Synchronization cluster receives a SetUTCTime command,
modifying the current UTC time of the device, the value of this attribute SHALL be adjusted to
match the new UTC time plus the value of the RemainingDuration attribute.
4.6.7.4. RemainingDuration Attribute
This attribute SHALL indicate the remaining duration, in seconds, until the valve closes.
This attribute SHALL be null:
• When OpenDuration is null, or
• When the valve is closed.
The value of this attribute SHALL only be reported in the following cases:
• When it changes from null to any other value and vice versa, or
• When it changes to 0, or
• When it increases, or
• When the closing time changes.
Meaning that clients SHOULD NOT rely on the reporting of this attribute in order to keep track of
the remaining duration, due to this attribute not being reported during regular countdown.
When reading this attribute it SHALL return the remaining duration, in seconds, until the valve
closes.
When the value of this attribute counts down to 0, the valve SHALL automatically transition to its
closed position. The behavior of transitioning to the closed position SHALL match the behavior
described in the Close command.
4.6.7.5. CurrentState Attribute
This attribute SHALL indicate the current state of the valve.
A value of null SHALL indicate that the current state is not known.
4.6.7.6. TargetState Attribute
This attribute SHALL indicate the target state, while changing the state, of the valve.
A value of null SHALL indicate that no target position is set, since the change in state is either done
or failed.
4.6.7.7. CurrentLevel Attribute
This attribute SHALL indicate the current level of the valve as a percentage value, between fully
closed and fully open. During a transition from one level to another level, the valve SHOULD keep
this attribute updated to the best of its ability, in order to represent the actual level of the valve dur
ing the movement.
A value of 100 percent SHALL indicate the fully open position.
A value of 0 percent SHALL indicate the fully closed position.
A value of null SHALL indicate that the current state is not known.
4.6.7.8. TargetLevel Attribute
This attribute SHALL indicate the target level of the valve as a percentage value, between fully
closed and fully open.
The interpretation of the percentage value is the same as for the CurrentLevel attribute.
A value of null SHALL indicate that no target position is set, since the change of level is either done
or failed.
4.6.7.9. DefaultOpenLevel Attribute
This attribute SHALL indicate the default value used for the TargetLevel attribute, when a valve
transitions from the closed to the open state, caused by an Open command, if a TargetLevel field is
not present in the Open command.
If the LevelStep attribute is present and the value of a write interaction to this attribute field is not
100, the value SHALL be a supported value as defined by the LevelStep attribute, such that (Value
received in the write interaction) % (Value of LevelStep attribute) equals 0. If the resulting value is
not 0, the requested DefaultOpenLevel value is considered an unsupported value and a CON
STRAINT_ERROR status SHALL be returned.
4.6.7.10. ValveFault Attribute
This attribute SHALL indicate any faults registered by the valve.
4.6.7.11. LevelStep Attribute
This attribute SHALL indicate the step size the valve can support.
The step size defined by this attribute is counted from 0 and the final step towards 100 MAY be dif
ferent than what is defined in this attribute. For example, if the value of this attribute is 15, it
results in these target values being supported; 0, 15, 30, 45, 60, 75, 90 and 100.
The values of 0 and 100 SHALL always be supported, regardless of the value of this attribute.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Valve Configuration and Control Cluster, specifically the "Open" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'M', indicating that it is mandatory. This means that the "Open" command must always be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* The table row describes a command within the Valve Configuration and Control Cluster, specifically the "Close" command, which is identified by the ID '0x01'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The 'Access' is marked as 'O', meaning it is optional for access control purposes. The 'Conformance' is labeled as 'M', which means that the "Close" command is mandatory. This indicates that any implementation of the Valve Configuration and Control Cluster must include this command, ensuring that the functionality to close the valve is always supported.

4.6.8.1. Open Command
This command is used to set the valve to its open position.

_Table parsed from section 'Commands':_

* In the Valve Configuration and Control Cluster, under the Commands section, the table row describes a command with the ID '0' named 'OpenDuration'. This command is of type 'elapsed-s', which likely refers to a duration measured in seconds, with a constraint that the minimum value must be 1. The 'Quality' is marked as 'X', indicating that this command is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'O', which means that the 'OpenDuration' command is optional. This implies that the implementation of this command is not required and has no dependencies, allowing for flexibility in its inclusion within a device's functionality.

* In the Valve Configuration and Control Cluster, within the Commands section, the entry for the command named "TargetLevel" is identified by ID '1' and is of the type 'percent', with a constraint specifying a minimum value of 1. The conformance rule for this command is '[LVL]', which means that the "TargetLevel" command is optional if the feature 'LVL' is supported. If 'LVL' is not supported, the command is not required, and there are no further conditions or requirements specified for its inclusion.

4.6.8.1.1. OpenDuration Field
This field SHALL indicate the duration that the valve will remain open for this specific Open com
mand.
A value of null SHALL indicate the duration is not set, meaning that the valve will remain open
until closed by the user or some other automation.
4.6.8.1.2. TargetLevel Field
This field SHALL indicate the target level used for this specific Open command.
4.6.8.1.3. Effect on Receipt
If the device has registered a fault, that prevents it from performing the requested action, the com
mand SHALL be ignored and a FailureDueToFault status SHALL be returned.
The device SHALL set the TargetState attribute to the Open value and set the CurrentState attribute
to the Transitioning value.
If the OpenDuration field is present, the value of the OpenDuration attribute SHALL be set to the
value of the OpenDuration field.
If the OpenDuration field is not present, the value of OpenDuration attribute SHALL be set to the
value of the DefaultOpenDuration attribute.
If the OpenDuration attribute is null, it SHALL indicate that there is no auto close defined for the
current Open action and the device SHALL set the RemainingDuration attribute to null. If the
device supports the TimeSync feature, the device SHALL set the AutoCloseTime attribute to null.
If the OpenDuration attribute is not null, it indicates that an auto close duration is defined for the
current open action and the device SHALL set the value of the RemainingDuration attribute equal
to the value of the OpenDuration attribute. If the device supports the TimeSync feature, the device
SHALL set the AutoCloseTime attribute to the UTC value of the time when command was received
plus the value of the OpenDuration attribute.
If the LevelStep attribute and the TargetLevel field are both present and the value of the Tar
getLevel field is not 100, the value of the TargetLevel field SHALL be a supported value as defined
by the LevelStep attribute, such that (Value of TargetLevel field) % (Value of LevelStep attribute)
equals 0. If the resulting value is not 0, the requested TargetLevel value is considered an unsup
ported value and a CONSTRAINT_ERROR status SHALL be returned.
If the device supports the Level feature, the TargetLevel attribute SHALL be set to the value of the
TargetLevel field, if present. If the TargetLevel field is not present, the TargetLevel attribute SHALL
be set to the value of the DefaultOpenLevel attribute, if implemented. If the DefaultOpenLevel
attribute is not present, the TargetLevel attribute SHALL be set to 100.
When the relevant target and duration attributes have been set, the device SHALL start the move
ment towards the target value and start the countdown of the RemainingDuration attribute. If the
device supports the Level feature, the device SHALL update the CurrentLevel attribute at the start
of the movement, and SHOULD update it as appropriate during movement, especially if it is slow.
When the movement is complete, the device SHALL set the CurrentState attribute to the Open
value.
4.6.8.2. Close Command
This command is used to set the valve to its closed position.
4.6.8.2.1. Effect on Receipt
If the device has registered a fault that causes it to prevent the valve to perform the requested
action, the command SHALL be ignored and a FailureDueToFault status SHALL be returned.
The OpenDuration and RemainingDuration attribute SHALL be set to null.
If the device supports the TimeSync feature, the AutoCloseTime attribute SHALL be set to null.
The  device  SHALL  set  the  TargetState  attribute  to  the  Closed  value  and  set  the  CurrentState
attribute to the Transitioning value.
If the device supports the Level feature, it SHALL set the TargetLevel attribute to 0.
When the relevant target attributes have been set, the device SHALL start the movement towards
the target value. If the device supports the Level feature, the device SHALL update the CurrentLevel
attribute, accordingly during the movement. When the movement is complete, the device SHALL
set the CurrentState attribute to the Closed value.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Valve Configuration and Control Cluster, specifically the "ValveStateChanged" event, identified by the ID '0x00'. This event has an informational priority level and requires access level 'V'. The conformance rule for this event is marked as 'O', indicating that it is optional. This means that the implementation of the "ValveStateChanged" event is not required and has no dependencies on other features or conditions. Developers can choose to include this event in their implementation, but it is not mandatory according to the Matter specification.

* The table row describes an event within the Valve Configuration and Control Cluster, specifically the "ValveFault" event. This event is identified by the ID '0x01' and is categorized with an 'INFO' priority level, indicating it provides informational messages about the valve's status. The 'Access' field is marked as 'V', suggesting it is visible or accessible in some manner, likely to devices or systems interacting with the cluster. The 'Conformance' field is marked as 'O', which means the "ValveFault" event is optional. This implies that the implementation of this event is not required and does not depend on any other features or conditions. Developers or manufacturers can choose to include this event in their devices, but it is not mandatory for compliance with the Matter specification.

4.6.9.1. ValveStateChanged Event
This event SHALL be generated when the valve state changed. For level changes, after the end of
movement, for state changes when the new state has been reached.

_Table parsed from section 'Events':_

* The table row describes an event within the Valve Configuration and Control Cluster, specifically the "ValveState" event. This event is identified by the ID '0' and is of the type 'ValveStateEnum', which suggests it enumerates different states a valve can be in. The 'Constraint' field indicates that this event applies universally ('all'), without any specific limitations or conditions. The 'Conformance' field is marked as 'M', meaning that the "ValveState" event is mandatory. This implies that any implementation of the Valve Configuration and Control Cluster must include this event, as it is a required component of the cluster's functionality according to the Matter specification.

* The table row entry describes an event named "ValveLevel" within the Valve Configuration and Control Cluster, specifically in the Events section. This event is of the type "percent" and applies to all constraints. The conformance rule for "ValveLevel" is specified as "LVL," which means that the event is mandatory if the feature or condition represented by "LVL" is supported. In other words, if the system or device includes the "LVL" feature, the "ValveLevel" event must be implemented. If "LVL" is not supported, the conformance rule does not apply, and the event is not required.

4.6.9.1.1. ValveState Field
This field SHALL indicate the new state of the valve.
4.6.9.1.2. ValveLevel Field
This field SHALL indicate the new level of the valve.
4.6.9.2. ValveFault Event
This event SHALL be generated when the valve registers or clears a fault, e.g. not being able to tran
sition to the requested target level or state.

_Table parsed from section 'Events':_

* The table row describes an event within the Valve Configuration and Control Cluster, specifically the "ValveFault" event. This event is identified by the ID '0' and is of the type 'ValveFaultBitmap', with a constraint labeled as 'all', indicating that it applies universally within its context. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "ValveFault" event is always required to be implemented in any device or system that supports the Valve Configuration and Control Cluster, without any conditions or exceptions.

4.6.9.2.1. ValveFault Field
This field SHALL indicate the value of the ValveFault attribute, at the time this event is generated.
Chapter 5. Closures
The Cluster Library is made of individual chapters such as this one. References between chapters
are made using a X.Y notation where X is the chapter and Y is the sub-section within that chapter.
5.1. General Description

## Introduction
The clusters specified in this document are for use typically in applications involving closures (e.g.,
shades, windows, doors), but MAY be used in any application domain.

## Cluster List
This section lists the closures specific clusters as specified in this chapter.
Table 10. Overview of the Closures Clusters

_Table parsed from section 'Cluster List':_

* The table row describes a cluster within the Valve Configuration and Control Cluster, specifically the "Door Lock" cluster, identified by the Cluster ID '0x0101'. This cluster provides an interface for a generic method to secure a door. The conformance rule for this cluster is not explicitly provided in the data given, but based on the context of the Matter Conformance Interpretation Guide, it would typically specify whether the inclusion of this cluster is mandatory, optional, provisional, deprecated, or disallowed, depending on certain conditions or features. Without the specific conformance string, we cannot determine the exact requirements for this cluster's implementation. However, generally, such a cluster would be crucial for devices that need to manage door security, and its conformance would dictate how essential it is for a device's functionality within the Matter ecosystem.

* The table row describes an entry within the Valve Configuration and Control Cluster, specifically detailing the "Window Covering" cluster, identified by the Cluster ID '0x0102'. This cluster encompasses commands and attributes necessary for controlling a window covering device. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance rule using the guide, it would specify the conditions under which the "Window Covering" cluster is required, optional, or otherwise categorized. For instance, if the conformance were 'M', it would mean the cluster is always required. If it were 'O', it would be optional with no dependencies. Without a specific conformance string, we cannot determine the exact requirements for this cluster in the context of the Valve Configuration and Control Cluster.

