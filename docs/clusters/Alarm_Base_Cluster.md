
# 1.15 Alarm Base Cluster

This cluster is a base cluster from which clusters for particular alarms for a device type can be
derived. Each derivation SHALL define the values for the AlarmBitmap data type used in this clus
ter. Each derivation SHALL define which alarms are latched.

## Data Types
1.15.5.1. AlarmBitmap Type
This data type SHALL be a map32 with values defined by the derived cluster. The meaning of each
bit position SHALL be consistent for all attributes in a derived cluster. That is, if bit 0 is defined for
an alarm, the Latch, State, and Supported information for that alarm are also bit 0.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Alarm Base Cluster, specifically the "Mask" attribute, which has an ID of '0x0000'. This attribute is of the type 'AlarmBitmap' and is constrained to 'all', meaning it applies universally within its context. The default value for this attribute is '0', and it has read and view access permissions, as indicated by 'R V'. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "Mask" attribute is always required to be implemented in any device or application that supports the Alarm Base Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Alarm Base Cluster, specifically the "Latch" attribute, which has an ID of '0x0001'. This attribute is of type 'AlarmBitmap' and has a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'F', suggesting a specific quality or characteristic defined elsewhere in the specification. The default value for this attribute is '0', and it has 'Read' and 'Volatile' access permissions, denoted by 'R V'. The conformance rule for this attribute is 'RESET', which is not directly explained by the provided conformance interpretation guide. This suggests that the conformance condition for 'RESET' is likely described in more detail elsewhere in the documentation, possibly indicating a specific behavior or requirement related to the reset functionality within the cluster.

* The table row describes an attribute within the Alarm Base Cluster, specifically the "State" attribute, identified by the ID `0x0002`. This attribute is of type `AlarmBitmap`, with a constraint of "all," meaning it applies universally within its context. The default value for this attribute is `0`, and it has read and view access permissions, denoted by `R V`. The conformance rule for this attribute is `M`, which indicates that it is mandatory. This means that the "State" attribute must always be implemented and supported in any device or application using the Alarm Base Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Alarm Base Cluster, specifically the 'Supported' attribute, which has an ID of '0x0003'. This attribute is of type 'AlarmBitmap' and is constrained to include all possible values. It is marked with a quality of 'F', indicating it is a fundamental attribute, and has a default value of '0'. The access level is 'R V', meaning it is readable and volatile. The conformance rule for this attribute is 'M', which signifies that it is mandatory. This means that the 'Supported' attribute must always be implemented in any device or application that uses the Alarm Base Cluster, with no conditions or exceptions.

1.15.6.1. Mask Attribute
This attribute SHALL indicate a bitmap where each bit set in the Mask attribute corresponds to an
alarm that SHALL be enabled.
1.15.6.2. Latch Attribute
This attribute SHALL indicate a bitmap where each bit set in the Latch attribute SHALL indicate
that the corresponding alarm will be latched when set, and will not reset to inactive when the
underlying condition which caused the alarm is no longer present, and so requires an explicit reset
using the Reset command.
1.15.6.3. State Attribute
This attribute SHALL indicate a bitmap where each bit SHALL represent the state of an alarm. The
value of true means the alarm is active, otherwise the alarm is inactive.
1.15.6.4. Supported Attribute
This attribute SHALL indicate a bitmap where each bit SHALL represent whether or not an alarm is
supported. The value of true means the alarm is supported, otherwise the alarm is not supported.
If an alarm is not supported, the corresponding bit in Mask, Latch, and State SHALL be false.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Alarm Base Cluster, specifically the "Reset" command, which is identified by the ID '0x00'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'RESET', which is not a standard conformance tag or expression as per the provided guide. This suggests that the conformance for the "Reset" command is described elsewhere in the documentation, under a section specifically detailing the conditions or requirements for the 'RESET' conformance. Therefore, to fully understand the conformance requirements for this command, one would need to refer to the additional documentation where 'RESET' is explained.

* The table row describes a command within the Alarm Base Cluster, specifically the "ModifyEnabledAlarms" command, which is directed from the client to the server. This command requires a response from the server, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', suggesting that access to this command is optional. The 'Conformance' field is also marked 'O', meaning that the implementation of this command is optional and not required by the Matter specification. This implies that while the command can be implemented, there are no dependencies or mandatory requirements for its inclusion in a device's functionality.

1.15.7.1. Reset Command
This command resets active and latched alarms (if possible). Any generated Notify event SHALL
contain fields that represent the state of the server after the command has been processed.

_Table parsed from section 'Commands':_

* In the context of the Alarm Base Cluster, specifically within the Commands section, the table row describes an element with the ID '0' named 'Alarms'. This element is of the type 'AlarmBitmap' and has a constraint labeled 'all', with a default value of '0'. The conformance rule for this element is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'Alarms' command is always required to be implemented in any device or application that supports the Alarm Base Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

1.15.7.1.1. Alarms Field
This field SHALL indicate a bitmap where each bit set in this field corresponds to an alarm that
SHALL be reset to inactive in the State attribute unless the alarm definition requires manual inter
vention. If the alarms indicated are successfully reset, the response status code SHALL be SUCCESS,
otherwise, the response status code SHALL be FAILURE.
1.15.7.2. ModifyEnabledAlarms Command
This command allows a client to request that an alarm be enabled or suppressed at the server.

_Table parsed from section 'Commands':_

* In the Alarm Base Cluster, under the Commands section, the table row describes a command with the ID '0' named 'Mask', which is of the type 'AlarmBitmap'. The constraint for this command is 'all', and its default value is '0'. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Mask' command is always required to be implemented in any device or application that supports the Alarm Base Cluster, without any conditions or exceptions.

1.15.7.2.1. Mask Field
This field SHALL indicate a bitmap where each bit set in the this field corresponds to an alarm that
SHOULD be enabled or suppressed. A value of 1 SHALL indicate that the alarm SHOULD be enabled
while a value of 0 SHALL indicate that the alarm SHOULD be suppressed.
A server that receives this command with a Mask that includes bits that are set for unknown
alarms SHALL respond with a status code of INVALID_COMMAND.
A server that receives this command with a Mask that includes bits that are set for alarms which
are not supported, as indicated in the Supported attribute, SHALL respond with a status code of
INVALID_COMMAND.
A server that is unable to enable a currently suppressed alarm, or is unable to suppress a currently
enabled alarm SHALL respond with a status code of FAILURE; otherwise the server SHALL respond
with a status code of SUCCESS.
On a SUCCESS case, the server SHALL also change the value of the Mask attribute to the value of the
Mask field from this command. After that the server SHALL also update the value of its State
attribute to reflect the status of the new alarm set as indicated by the new value of the Mask
attribute.

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Alarm Base Cluster, specifically the "Notify" event, which has an ID of '0x00' and a priority level of 'INFO'. The 'Access' field is marked as 'V', indicating that this event is visible or accessible in some manner. The 'Conformance' field is marked as 'M', which means that the "Notify" event is mandatory. This implies that any implementation of the Alarm Base Cluster must include this event, as it is always required according to the Matter specification. There are no conditional or optional aspects to its inclusion; it is a fundamental component of the cluster.

1.15.8.1. Notify Event
This event SHALL be generated when one or more alarms change state, and SHALL have these
fields:

_Table parsed from section 'Events':_

* In the context of the Alarm Base Cluster, specifically within the Events section, the table row describes an element with the ID '1' named 'Active'. This element is of the type 'AlarmBitmap' and has a constraint labeled as 'all', with a default value set to '0'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'Active' element is always required to be implemented in any device or system that supports the Alarm Base Cluster, without any conditions or exceptions.

* In the context of the Alarm Base Cluster's Events section, the table row describes an event with the ID '2' named 'Inactive', which is of the type 'AlarmBitmap'. The constraint for this event is 'all', and it has a default value of '0'. The conformance rule for this event is 'M', which stands for Mandatory. This means that the 'Inactive' event is always required to be implemented in any device or application that supports the Alarm Base Cluster, without any conditions or exceptions.

* The table row describes an event within the Alarm Base Cluster, specifically the "State" event, which is identified by the ID '3'. This event is of the type 'AlarmBitmap', indicating it likely represents a bitmap of alarm states. The 'Constraint' is set to 'all', suggesting that this event applies universally within its context, and it has a default value of '0'. The 'Conformance' field is marked as 'M', which means that this event is mandatory. In other words, the "State" event must always be implemented and supported in any device or application that uses the Alarm Base Cluster, without any conditions or exceptions.

* In the context of the Alarm Base Cluster, specifically within the Events section, the table row describes an element with the ID '4' named 'Mask'. This element is of the type 'AlarmBitmap', with a constraint labeled as 'all', and it has a default value of '0'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Mask' element is always required to be implemented in any device or application that supports the Alarm Base Cluster, without any conditions or exceptions.

1.15.8.1.1. Active Field
This field SHALL indicate those alarms that have become active.
1.15.8.1.2. Inactive Field
This field SHALL indicate those alarms that have become inactive.
1.15.8.1.3. Mask Field
This field SHALL be a copy of the Mask attribute when this event was generated.
1.15.8.1.4. State Field
This field SHALL be a copy of the new State attribute value that resulted in the event being gener
ated. That is, this field SHALL have all the bits in Active set and SHALL NOT have any of the bits in
Inactive set.