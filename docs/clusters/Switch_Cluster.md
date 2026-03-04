
# 1.13 Switch Cluster

This cluster exposes interactions with a switch device, for the purpose of using those interactions
by other devices.
Two types of switch devices are supported: latching switch (e.g. rocker switch) and momentary
switch (e.g. push button), distinguished with their feature flags.
Interactions with the switch device are exposed as attributes (for the latching switch) and as events
(for both types of switches).
An interested client MAY subscribe to these attributes/events and thus be informed of the interac
tions, and can perform actions based on this, for example by sending commands to perform an
action such as controlling a light or a window shade.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Switch Cluster, specifically the "NumberOfPositions" attribute. This attribute has an ID of '0x0000' and is of type 'uint8', with a constraint that it must have a minimum value of 2. It is marked with a quality of 'F', indicating it is a fundamental attribute, and has a default value of 2. The access level is 'R V', meaning it is readable and has a volatile nature. The conformance rule for this attribute is 'M', which signifies that the "NumberOfPositions" attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "CurrentPosition" within the Switch Cluster's Attributes section. It is identified by the ID '0x0001' and is of type 'uint8', with a constraint that its value must not exceed 'max NumberOfPositions-1'. The attribute is of normal quality ('N'), has a default value of '0', and can be accessed with read ('R') and view ('V') permissions. The conformance rule 'M' indicates that this attribute is mandatory, meaning it is always required to be implemented in any device or application using the Switch Cluster, without any conditions or exceptions.

* The table row describes an attribute named "MultiPressMax" within the Switch Cluster, identified by the ID '0x0002'. This attribute is of type 'uint8' and has a minimum constraint of 2, with a default value set to 2. It is accessible with read and view permissions ('R V'). The 'Quality' is marked as 'F', indicating a specific feature or quality requirement. The conformance rule 'MSM' indicates that the "MultiPressMax" attribute is mandatory under the condition that the feature 'MSM' is supported. If 'MSM' is not supported, the conformance rule does not specify an alternative, implying that the attribute is not required in that case.

1.13.5.1. NumberOfPositions Attribute
This attribute SHALL indicate the maximum number of positions the switch has. Any kind of switch
has a minimum of 2 positions. Also see Multi Position Details for the case NumberOfPositions>2.
1.13.5.2. CurrentPosition Attribute
This attribute SHALL indicate the position of the switch.
The valid range is zero to NumberOfPositions - 1.
CurrentPosition value 0 SHALL be assigned to the default position of the switch: for example the
"open" state of a rocker switch, or the "idle" state of a push button switch.
1.13.5.3. MultiPressMax Attribute
This attribute SHALL indicate how many consecutive presses can be detected and reported by a
momentary switch which supports multi-press (MSM feature flag set).
For example, a momentary switch supporting single press, double press and triple press, but not
quad press and beyond, would return the value 3.
When more than MultiPressMax presses are detected within a multi-press sequence:
<
• The server for cluster revision   2 SHOULD generate a MultiPressComplete event with the Total
NumberOfPressesCounted field set to the value of the MultiPressMax attribute, and avoid gener
ating any further InitialPress and MultiPressOngoing events until the switch has become fully
idle (i.e. no longer in the process of counting presses within the multipress).
>=
• The server for cluster revision   2 SHALL generate a MultiPressComplete event with the Total
NumberOfPressesCounted field set to zero (indicating an aborted sequence), and SHALL NOT
generate any further InitialPress and MultiPressOngoing events until the switch has become
fully idle (i.e. no longer in the process of counting presses within the multipress).
This approach avoids unintentionally causing intermediate actions where there is a very long
sequence of presses beyond MultiPressMax that MAY be taken in account specially by switches (e.g.
to trigger special behavior such as factory reset for which generating events towards the client is
not appropriate).

## Events

_Table parsed from section 'Events':_

* The table row describes an event within the Switch Cluster, specifically the "SwitchLatched" event, which has an ID of '0x00' and a priority level of 'INFO'. The access level for this event is 'V', indicating it is viewable. The conformance rule for this event is 'LS', which means that the "SwitchLatched" event is mandatory if the feature 'LS' is supported. If the feature 'LS' is not supported, the event is not required. This conformance rule ensures that the event is implemented only when relevant to the supported features of the device.

* In the Switch Cluster, the event identified by ID `0x01` is named `InitialPress`, which has an informational priority and requires view access (`V`). The conformance rule for this event is `MS`, indicating that it is mandatory when the feature `MS` is supported. This means that if the `MS` feature is present in the implementation, the `InitialPress` event must be included as part of the Switch Cluster's functionality. If `MS` is not supported, the conformance rule does not specify any requirement for the event, implying it may not be included.

* The table row describes an event within the Switch Cluster, specifically the "LongPress" event, identified by the ID `0x02`. This event has an informational priority level and requires view access, as indicated by the 'Access' field marked with 'V'. The 'Conformance' field is marked as 'MSL', which does not directly match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. This suggests that 'MSL' might be a shorthand or a specific condition described elsewhere in the documentation, possibly indicating a complex conformance requirement that cannot be simplified into the basic tags or expressions provided. Therefore, to fully understand the conformance requirements for the "LongPress" event, one would need to refer to additional documentation where 'MSL' is defined.

* The table row describes an event within the Switch Cluster, specifically the "ShortRelease" event, which has an ID of '0x03'. This event is categorized with a priority level of 'INFO' and has an access level denoted by 'V', which typically indicates that it is visible or can be accessed in some manner. The conformance rule for this event is 'MSR'. According to the Matter Conformance Interpretation Guide, 'MSR' implies that the "ShortRelease" event is Mandatory (M) when the feature or condition 'SR' is supported. In this context, 'SR' likely refers to a specific feature or condition related to the Switch Cluster. Therefore, if the 'SR' feature is present, the "ShortRelease" event must be implemented.

* The table row describes an event named "LongRelease" within the Switch Cluster, identified by the ID '0x04'. This event has a priority level of 'INFO' and an access level of 'V', indicating it is visible. The conformance rule for "LongRelease" is specified as 'MSL'. According to the Matter Conformance Interpretation Guide, 'MSL' is not a standard conformance tag or expression. However, if we interpret 'MSL' as a potential typo or shorthand, it could imply a combination of conditions or a specific conformance status described elsewhere in the documentation. Without additional context or correction, the precise conformance requirement for "LongRelease" cannot be definitively determined from the provided information.

* The table row entry pertains to the "MultiPressOngoing" event within the Switch Cluster, identified by the ID '0x05'. This event is categorized with an 'INFO' priority level and has 'V' access, indicating it is visible. The conformance rule 'MSM & !AS' specifies that the "MultiPressOngoing" event is mandatory if the device supports the 'MSM' feature and does not support the 'AS' feature. In other words, for devices that include the 'MSM' feature but exclude the 'AS' feature, this event must be implemented. If either condition is not met (i.e., if 'MSM' is not supported or 'AS' is supported), the event is not required.

* In the Switch Cluster, under the Events section, the table row describes an event with the ID `0x06` named `MultiPressComplete`. This event has an informational priority level (`INFO`) and requires view access (`V`). The conformance rule for this event is `MSM`, which indicates that the `MultiPressComplete` event is mandatory in all contexts. The conformance string does not include any conditional expressions or additional dependencies, meaning that this event must always be implemented in devices supporting the Switch Cluster, without exceptions or future changes anticipated.

1.13.6.1. SwitchLatched Event
This event SHALL be generated, when the latching switch is moved to a new position.
It MAY have been delayed by debouncing within the switch.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, under the Events section, the table row describes an event with the ID '0' named 'NewPosition'. This event is of type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that limits its value to a range from 0 to one less than the value of 'NumberOfPositions'. The conformance rule for this event is marked as 'M', indicating that it is mandatory. This means that the 'NewPosition' event must always be implemented and supported in any device or application that uses the Switch Cluster, without any conditions or exceptions.

1.13.6.1.1. NewPosition Field
This field SHALL indicate the new value of the CurrentPosition attribute, i.e. after the move.
1.13.6.2. InitialPress Event
This event SHALL be generated, when the momentary switch starts to be pressed (after debounc
ing).
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, under the Events section, the table row describes an event named "NewPosition" with an ID of '0'. This event is of type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that its value must be between 0 and one less than the total number of positions (i.e., '0 to NumberOfPositions-1'). The conformance rule for this event is marked as 'M', indicating that the "NewPosition" event is mandatory. This means that any implementation of the Switch Cluster must include this event, as it is always required according to the Matter specification.

1.13.6.2.1. NewPosition Field
This field SHALL indicate the new value of the CurrentPosition attribute, i.e. while pressed.
1.13.6.3. LongPress Event
This event SHALL be generated when the momentary switch has been pressed for a "long" time.
The time interval constituting a "long" time is manufacturer-determined, since it depends on the
switch physics.
• When the AS feature flag is set, this event:
◦ SHALL NOT be generated during a multi-press sequence (since a long press is a separate
cycle from any multi-press cycles);
◦ SHALL only be generated after the first InitialPress following a MultiPressComplete when a
long press is detected after the idle time.
• Else, when the MSM feature flag is set, this event:
◦ SHALL NOT be generated during a multi-press sequence (since a long press is a separate
cycle from any multi-press cycles);
◦ SHALL only be generated after the first InitialPress following a MultiPressComplete when a
long press is detected after the idle time;
◦ SHALL NOT be generated after a MultiPressOngoing event without an intervening Multi
PressComplete event.
The above constraints imply that for a given activity detection cycle of a switch having MSM and/or
MSL feature flags set, the entire activity is either a single long press detection cycle of (InitialPress,
LongPress, LongRelease), or a single multi-press detection cycle (ending in MultiPressComplete),
where presses that would otherwise be reported as long presses are instead reported as a counted
press in the MultiPressComplete event, and as InitialPress/ShortRelease pairs otherwise (where
applicable).
The rationale for this constraint is the ambiguity of interpretation of events when mixing long
presses and multi-press events.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, under the Events section, there is an entry for an event named "NewPosition" with an ID of '0'. This event is of type 'uint8' and has a constraint that its value must be between '0' and 'NumberOfPositions-1'. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "NewPosition" event is always required to be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

1.13.6.3.1. NewPosition Field
This field SHALL indicate the new value of the CurrentPosition attribute, i.e. while pressed.
1.13.6.4. ShortRelease Event
If the server has the Action Switch (AS) feature flag set, this event SHALL NOT be generated at all,
since setting the Action Switch feature flag forbids the Momentary Switch ShortRelease (MSR) fea
ture flag from being set. Otherwise, the following paragraphs describe the situations where this
event is generated.
This event SHALL be generated, when the momentary switch has been released (after debouncing).
• If the server has the Momentary Switch LongPress (MSL) feature flag set, then this event SHALL
be generated when the switch is released if no LongPress event had been generated since the
previous InitialPress event.
• If the server does not have the Momentary Switch LongPress (MSL) feature flag set, this event
SHALL be generated when the switch is released - even when the switch was pressed for a long
time.
• Also see Section 1.13.7, “Sequence of generated events”.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, under the Events section, the table row describes an event named "PreviousPosition" with an ID of '0'. This event is of type 'uint8', which means it is an unsigned 8-bit integer, and it has a constraint that limits its value to a range from 0 to one less than the total number of positions, specified as 'NumberOfPositions-1'. The conformance rule for this event is 'M', indicating that it is mandatory. This means that the "PreviousPosition" event must always be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

1.13.6.4.1. PreviousPosition Field
This field SHALL indicate the previous value of the CurrentPosition attribute, i.e. just prior to
release.
1.13.6.5. LongRelease Event
This event SHALL be generated, when the momentary switch has been released (after debouncing)
and after having been pressed for a long time, i.e. this event SHALL be generated when the switch
is released if a LongPress event has been generated since the previous InitialPress event. Also see
Section 1.13.7, “Sequence of generated events”.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster's Events section, the table row describes an event named "PreviousPosition" with an ID of '0'. This event is of type 'uint8' and is constrained to values ranging from '0' to 'NumberOfPositions-1'. The conformance rule for this event is 'M', which stands for Mandatory. This means that the "PreviousPosition" event is always required to be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

1.13.6.5.1. PreviousPosition Field
This field SHALL indicate the previous value of the CurrentPosition attribute, i.e. just prior to
release.
1.13.6.6. MultiPressOngoing Event
If the server has the Action Switch (AS) feature flag set, this event SHALL NOT be generated at all.
Otherwise, the following paragraphs describe the situations where this event is generated.
This event SHALL be generated to indicate how many times the momentary switch has been
pressed in a multi-press sequence, during that sequence. See Multi Press Details below.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, within the Events section, the table row describes an event named "NewPosition" with an ID of '0'. This event is of type 'uint8', which means it is an 8-bit unsigned integer. The value of "NewPosition" is constrained to be within the range from 0 to one less than the value of "NumberOfPositions". The conformance rule for "NewPosition" is marked as 'M', indicating that this event is mandatory. This means that the "NewPosition" event must always be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

* In the Switch Cluster, under the Events section, the entry for 'CurrentNumberOfPressesCounted' is identified by ID '1' and is of type 'uint8'. This attribute tracks the number of button presses, constrained between 2 and the value defined by 'MultiPressMax'. The conformance rule 'M' indicates that this attribute is Mandatory, meaning it is always required to be implemented in any device or application that supports the Switch Cluster. There are no conditions or dependencies affecting its requirement status; it must be included as specified.

1.13.6.6.1. NewPosition Field
This field SHALL indicate the new value of the CurrentPosition attribute, i.e. while pressed.
1.13.6.6.2. CurrentNumberOfPressesCounted Field
This field SHALL contain:
• a value of 2 when the second press of a multi-press sequence has been detected,
• a value of 3 when the third press of a multi-press sequence has been detected,
th
• a value of N when the N  press of a multi-press sequence has been detected.
1.13.6.7. MultiPressComplete Event
This event SHALL be generated to indicate how many times the momentary switch has been
pressed in a multi-press sequence, after it has been detected that the sequence has ended. See Multi
Press Details.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Switch Cluster, under the Events section, the table row describes an event named "PreviousPosition" with an ID of '0'. This event is of type 'uint8', meaning it is an unsigned 8-bit integer, and it has a constraint that its value must range from 0 to one less than the total number of positions, as defined by 'NumberOfPositions'. The conformance rule for this event is 'M', which stands for Mandatory. This means that the "PreviousPosition" event is always required to be implemented in any device or application that supports the Switch Cluster, without any conditions or exceptions.

* In the context of the Switch Cluster, the table row describes an event named "TotalNumberOfPressesCounted" with an ID of '1'. This event is of type 'uint8', which is an unsigned 8-bit integer, and it has a constraint defined as 'max MultiPressMax', indicating that the value of this event cannot exceed the maximum value specified by 'MultiPressMax'. The conformance rule for this event is 'M', which means it is mandatory. This implies that the "TotalNumberOfPressesCounted" event must always be implemented and supported in any device or application that uses the Switch Cluster, without any conditions or exceptions.

The PreviousPosition field SHALL indicate the previous value of the CurrentPosition attribute, i.e.
just prior to release.
The TotalNumberOfPressesCounted field SHALL contain:
• a value of 0 when there was an aborted multi-press sequence, where the number of presses
goes beyond MultiPressMax presses,
• a value of 1 when there was exactly one press in a multi-press sequence (and the sequence has
ended), i.e. there was no double press (or more),
• a value of 2 when there were exactly two presses in a multi-press sequence (and the sequence
has ended),
• a value of 3 when there were exactly three presses in a multi-press sequence (and the sequence
has ended),
• a value of N when there were exactly N presses in a multi-press sequence (and the sequence has
ended).
0
The  introduction  of  TotalNumberOfPressesCounted  supporting  the  value    MAY
impact clients of switches using cluster revision 1 since such servers would not use
this  value  of  TotalNumberOfPressesCounted  to  indicate  an  aborted  sequence.
NOTE
Clients SHOULD always act using the TotalNumberOfPressesCounted field taken
into account since for values from 1 to MultiPressMax, the user action that led to the
event was different depending on the count.

## Sequence of generated events
This section describes the sequence of events that will be generated by three types of momentary
switches (distinguished by their feature flags). For each switch type, we will define the sequence of
generated events for these three interactions:
1. Sequence for a switch which is pressed briefly.
2. Sequence for a switch pressed for a long time.
3. Sequence for a switch pressed for a very long time.
In the three interactions described in the subsections below, if the NumberOfPositions attribute is
equal to 2, the InitialPress and LongPress events have the NewPosition field set to 1 and the Short
Release and LongRelease events have the PreviousPosition field set to 1. For larger values of the
NumberOfPositions attribute, see Multi Position Details.
1.13.7.1. Switches with long-press detection support (MSL feature flag set)
This switch (with feature flags MS & MSL both set) SHALL generate either a sequence of two or
three (depending on how long the switch is pressed) events for one interaction cycle, in the order
given below and illustrated in the figure below.
• Upon a short press:
◦ Generate InitialPress
◦ If the MSR feature flag is set and the AS feature flag is NOT set, generate ShortRelease after
the previous event, when release is detected.
◦ If the MSM feature flag is set, generate MultiPressComplete(1) after the previous event(s).
• Upon a long press (or very long press):
◦ Generate InitialPress
◦ Generate LongPress after the previous event, when long press is detected
◦ Generate LongRelease (and NOT MultiPressComplete(1)) after the previous event, when
switch release is detected.
A LongPress event SHALL be generated exactly once for this case and SHALL NOT be repeated, irre
spective how long the switch is pressed.
The image shows a time representation of the state of the switch (low=not pressed, high=pressed)
with the colored dots indicating the various events generated at that moment in time.
Figure 3. Switch device with MSL feature flag set (single press case)
1.13.7.2. Switches without long-press detection support (MSL feature flag not set)
This switch (with feature flags states MS & !MSL) SHALL NOT generate LongPress and LongRelease
events and therefore it SHALL generate a sequence of two events for one interaction cycle, irre
spective of how long the switch is pressed, in the order given and illustrated below, based on
whether the MSM, AS and MSR flags are set.
• Any press length:
1. Generate InitialPress
2. If the MSR feature flag is set and the AS feature flag is NOT set, generate ShortRelease after
the previous event, when the release is detected.
3. If the MSM feature flag is set, generate MultiPressComplete(1) after the previous event(s).
Even after a "long" period being pressed, the release event is never LongRelease. A
NOTE device without the MSL feature flag SHALL NOT generate the LongPress and Lon
gRelease events.
Figure 4. Switch device without MSL feature flag not set (single press case)
1.13.7.3. Switches with most basic MS-only feature flag set, not (MSR | MSL | MSM | AS)
This switch (with feature flags states MS & !MSR & !MSL & !MSM & !AS) SHALL generate a single Ini
tialPress event for one interaction cycle, irrespective of how long the switch is pressed, as illus
trated in the figure below.
A device with this set of feature flags SHALL NOT generate any of the ShortRelease, LongPress and
LongRelease events.
Figure 5. Switch device delivering only 'InitialPress' events (single press case)

## Sequence of events for MultiPress
Multi-press detection is a feature of momentary switches (indicated with feature flag MSM being
set, with optional AS feature flag set) that they can count and report sequences of press-release
cycles within a certain time frame, for example to indicate that the user has pressed the switch
once, twice or three (or even more) times in succession. The definition of the time window for this
detection is manufacturer-specific since it depends on the switch physics. The maximum number of
presses which can be detected and reported SHALL be indicated in attribute MultiPressMax. The
minimum value and default value for MultiPressMax are both 2.
A switch supporting MultiPress SHALL set feature flags MS & MSM, and MAY optionally, according
to conformance rules of each flag, set flags MSL, MSR, and AS.
The ActionSwitch (AS) feature flag is a behavior selector which, when set, reduces the number of
events generated by the switch.
A press cycle when MSM is set is either a long-press cycle (if MSL set), or a multi-press cycle.
• If the MSL feature flag is set and the cycle is deemed "long" during the first press cycle after Ini
tialPress, then the switch SHALL react as described in Section 1.13.7.1, “Switches with long-press
detection support (MSL feature flag set)”, and SHALL NOT consider this to be the start of a
multi-press sequence (see penultimate case illustrated in Figure 7, “Switch device with MSM and
!AS feature flags (multi-press case)”).
• If the MSL feature flag is not set or if the first button press cycle is short, then the switch SHALL
count presses until the switch becomes sufficiently idle, and SHALL NOT generate LongPress
and LongRelease events for intermediate presses within the multi-press cycle that are "long".
1.13.8.1. Multi-press behavior when ActionsSwitch (AS) feature flag is not set
A switch with the MSM feature flag set but the AS flag unset:
• SHALL generate an InitialPress event at the start of every button press within a button multi-
press cycle;
• SHALL generate a ShortRelease event at the end of every button press within a button multi-
press cycle if MSR is set;
• SHALL generate a MultiPressOngoing event after the InitialPress event of the second and subse
quent presses of a button multi-press cycle;
• SHALL  generate  a  MultiPressComplete  at  the  end  of  a  multi-press  cycle,  including  single
presses;
>= <
• SHALL NOT (for cluster revision  2) or SHOULD NOT (for cluster revision  2) generate any
LongPress and LongRelease events within the multi-press cycle.
The MultiPressOngoing event is provided for parties interested in keeping track of the actual
presses during the multi-press sequence. The MultiPressComplete event is provided for parties
interested in the outcome of the whole sequence: after the multi-press sequence has ended, they
will receive the MultiPressComplete event indicating how many times the switch was pressed.
In the figure below, several sequences of user interaction are indicated:
• Single press sequence: after the press and release moments, the InitialPress SHALL be gener
ated, and ShortRelease events SHALL be generated if the MSR feature flag is set. After some fur
ther time, when the switch has detected that there is no second press, it SHALL generate Multi
PressComplete(1) since it has detected that the sequence consisted of one press. No MultiPres
sOngoing event SHALL be generated for this case.
• Double press sequence: after each of the press and release moments, the InitialPress SHALL be
generated, and ShortRelease events SHALL be generated if the MSR feature flag is set. Addition
ally, when the switch is pressed for the second time, the MultiPressOngoing(2) event SHALL be
generated, as the switch has detected the second press. Note that this event coincides with the
second InitialPress event; both SHALL be generated. After some further time, when the switch
has detected that there is no third press, it SHALL generate MultiPressComplete(2) since it has
detected that the sequence consisted of two presses.
• Triple press sequence: after each press and release moments, the InitialPress SHALL be gener
ated, and ShortRelease events SHALL be generated if the MSR feature flag is set. Additionally,
when the switch is pressed for the second time, the MultiPressOngoing(2) event SHALL be gen
erated, as the switch has detected the second press. Note that this event coincides with the sec
ond InitialPress event; both SHALL be generated. Additionally, when the switch is pressed for
the third time, the MultiPressOngoing(3) event SHALL be generated, as the switch has detected
the third press. Note that this event coincides with the third InitialPress event; both SHALL be
generated. After some further time, when the switch has detected that there is no fourth press,
it SHALL generate MultiPressComplete(3) since it has detected that the sequence consisted of
three presses.
◦ This case specifically does NOT generate LongPress and LongRelease events within the
sequence (even though the figure below illustrates a longer press duration for the second
press in one of the cases), since multi-press sequences SHOULD/SHALL NOT generate Long
Press and LongRelease events within the sequence (see Section 1.13.6.3, “LongPress Event”
for more details).
• N presses starting with a long press (if MSL feature flag is set): this starts with a long press
sequence wish SHALL be considered according to Section 1.13.7.1, “Switches with long-press
detection support (MSL feature flag set)”. Then it is a sequence similar to triple press, with N
presses instead of 3.
For the above cases where multiple events need to be generated at the same time, the MultiPres
sOngoing event SHALL be generated directly after the InitialPress event.
The numbers in parentheses in the bulleted text above and in the figure below indi
NOTE cate the value of the CurrentNumberOfPressesCounted resp. TotalNumberOfPress
esCounted field in the event data.
As with the other figures, sufficient debounce time needs to be take into account for
NOTE the detection of press and release events. This is included in the figure, and has
been left out of the description above for readability, but SHALL be applied.
Several of the events require very low congestion and latency in the final system to
be usable for real-time control and use cases. Care must be taken during design not
NOTE
to  rely  on  very  low  latency  and  real-time  event  timestamps  if  the  low-latency
assumptions do not hold.
Figure 6. Switch device with MSM and !AS feature flags (multi-press case)
1.13.8.2. Multi-press behavior when ActionsSwitch (AS) feature flag is set
When the ActionSwitch feature flag is set, the behavior for all presses:
• The switch SHALL only generate an InitialPress event at the start of every button press cycle
(whether long or not);
• The switch SHALL NOT generate ShortRelease events;
• The switch SHALL NOT generate MultiPressOngoing events.
Because of these simplifications, clients can decide to act purely on the following to determine user
action:
• LongRelease (if MSL feature flag is set) to determine the end of a long press.
◦ InitialPress and LongPress (if MSL feature flag is set), if needed, to detect the start of the
press and long-press periods so that actions such as "do action X while long pressed and stop
on release" can be supported.
• MultiPressComplete to determine the end of a series of presses (0 .. MultiPressMax)
◦ Only the final count of presses detected by the switch is provided.
◦ The value of 0 indicates an aborted press (e.g. maybe too many presses in a row, button held
down for too long, etc).
◦ The value of 1 indicates a single press, 2 a double-press, etc.
Because of the omission of ShortRelease, MultiPressOngoing and the "inner" InitialPress events, less
network traffic is generated, while not missing the overall "action" intent from the end-user.
In the figure below, several sequences of user interaction are indicated:
• Single press sequence: after the initial press detection, the InitialPress event is generated. After
some further time, when the switch has detected that there is no second press, and the press is
not a long press (if MSL feature flag is set), it generates the MultiPressComplete(1) event since it
has detected that the sequence consisted of one press.
• Double press sequence: after the initial press detection, the InitialPress event is generated. After
some further time, when the switch has detected that there is no third press, it generates the
MultiPressComplete(2) event since it has detected that the sequence consisted of two presses.
• N-press sequence: after the initial press detection, the InitialPress event is generated. Addition
ally, when the switch is pressed for the second time, we note that the press is long, but there is
not a LongPress or LongRelease event, since long presses inside (not at the start) of a multi-press
sequence are treated as short presses. After some further time, when the switch has detected
that there are no further presses beyond N presses, it generates a MultiPressComplete(N) event
since it has detected that the sequence consisted of N presses.
• Long press sequence followed by N-press sequence:
◦ This case contains to two separate sequences, since a long press sequence is always an inde
pendent sequence, and does not get reported as "long" within multi-presses (see previous
example case).
◦ The first sequence is a Long Press sequence of: InitialPress, LongPress, and finally, LongRe
lease.
◦ The second sequence, whether immediate or not, is a N-press sequence of: InitialPress, and
finally, MultiPressComplete(N).
• N-press sequence with N > MultiPressMax: after the initial press detection, the InitialPress event
is generated. After some further time, when the switch has detected that there are no further
presses beyond N presses, it generates a MultiPressComplete(0) event since it has detected that
the multi-press sequence is done, but since there were more presses than MultiPressMax, the
sequence uses 0 for TotalNumberOfPressesCounted to indicate invalid complete sequence.
Figure 7. Switch device with MSM and !AS feature flags (multi-press case)

## Summary of cases for MS feature flag
Given the variety of situations that may arise due to the different switch capabilities, the following
describes the edges that would unambiguously convey user action intents:
• MS & !MSR & !MSM: Every action cycle is only a single InitialPress event.
• MS & !MSM: Every action cycle ends on ShortRelease or LongRelease (if MSL feature flag is set),
depending on long or short press and whether MSR/MSL feature flags are set.
• MS & MSM: Every action cycle ends on either LongRelease (if MSL feature flag is set and first
press was long) or MultiPressComplete.
◦ The AS feature flag does not change the outcome of which events can be used for action
detection.
◦ The AS feature flag is backwards-compatible with previous revisions of this cluster.
◦ The AS feature flag primarily offers a reduction of events generated.
The above list is relevant for the case of a client which does not use the events indicating progress
during the action cycle (i.e. ShortRelease, MultiPressOngoing, repeated InitialPress) for its opera
tion.

## Multi Position Details
This section will discuss some archetypes of switch devices with more than 2 positions and how
they SHALL set attribute values and generate events matching their characteristics.
For the SwitchLatched, InitialPress, LongPress and MultiPressOngoing events, the field NewPosition
SHALL be set to the value corresponding to the new position to which the switch was moved. For
the ShortRelease, LongRelease and MultiPressComplete events, the field PreviousPosition SHALL be
set to the value corresponding to the position of the switch just preceding the (latest) release.
1.13.10.1. Latching Switch with N stable positions (N>2) with fixed sequence
With such a device, the user can move the switch from a position M to positions M-1 and M+1
(either with a wraparound between the end positions, or fixed stop at the end positions).
On each interaction with the switch device, it SHALL generate a SwitchLatched event with the New
Position field set to the value associated with the new position.
Due to the physical constraints, such an event will have a NewPosition field which is equal to the
previous NewPosition field plus or minus 1 (modulo NumPositions if the switch does not have end
stops).
In a first example, a switch has 3 positions, associated with values 0, 1 and 2. In this case, wrap
around is not possible: from position 0 it can only be moved to position 1.
B B B
C C C
A A
A
pos C => report 2
pos A => report 0
pos B => report 1
Figure 8. Rotary switch device with 3 positions
In another example, a switch has 8 positions, associated with values 0 through 7. In this case, the
physics of the switch allow wraparound: from position 0 it can be moved to position 1 or to position
7.
0
1
7
2
6
3
5
4
Figure 9. Rotary switch device with 8 positions and wraparound
1.13.10.2. Latching Switch with N stable positions (N>2) with random sequence (example:
radio buttons)
With such a device, the user can press any of the available buttons, so this switch does not show the
incrementing or decrementing behavior of NewPosition which we discussed for the latching switch
with fixed sequence. In the example in the figure below, the 5 buttons are labeled "A" through "E"
for the user and are associated with values 0 through 4. The user first presses the "A" button, and
the switch device generates a SwitchLatched event with NewPosition set to 0. Then the user first
presses the "D" button, and the switch device generates a SwitchLatched event with NewPosition set
to 4.

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

_Table parsed from section 'Multi Position Details':_

B C D E A B C E
button A pressed => report 0
button D pressed => report 4
Figure 10. Switch device with radio buttons
1.13.10.3. Momentary Switch with 2 or more non-stable positions
For a Momentary Switch with more than 1 stable position, it depends on the physics of the switch
device which sequence of events will be generated.
In this section we will mention only the InitialPress and ShortRelease events. The
switch device could also generate the other events defined above for a momentary
NOTE
switch, depending on the capabilities of the switch device and the interaction with
the switch device.
The first variant (figure below, example: up/down control for window blinds) shows a switch in
neutral position (left figure) which corresponds to CurrentPosition=0. The user can press the top
side (position value 1) or the bottom side (position value 2). It is not possible to go directly from
position 1 to position 2 or vice versa - the switch will always need to go through the neutral position
0.
So when the user presses the top side of the switch, the InitialPress (NewPosition=1) event will be
generated. When they release the top side, the ShortRelease (PreviousPosition=1) event will be gen
erated. The user continues to press the bottom side, and the event InitialPress (NewPosition=2) is
generated. Upon release of the bottom side, the event ShortRelease (PreviousPosition=2) is gener
ated.
top side pressed (1)
neutral position (0) bottom side pressed (2)
Figure 11. Up/down control switch device
Another variant (figure below, example: joystick) has a control handle with a neutral position in the
middle (left figure) which corresponds to CurrentPosition=0. The handle can be moved along the
dotted lines.
In the middle figure, the user moves the handle to the East position and then releases it (which
makes it return to the neutral middle position). This generates this sequence of events:
InitialPress (NewPosition=3)       // move to East
ShortRelease (PreviousPosition=3)  // back to middle (from East)
In the righthand figure, the user moves the handle to the SouthWest position, then to the South
position and then releases it (which makes it return to the neutral middle position). This generates
this sequence of events:
InitialPress (NewPosition=6)       // move to SouthWest
InitialPress (NewPosition=5)       // move to South
ShortRelease (PreviousPosition=5)  // back to middle (from South)
1 2
8
1 2 1 2 8
8

_Table parsed from section 'Multi Position Details':_

* In the context of the Switch Cluster, specifically within the Multi Position Details section, the table row provided indicates a specific element or feature with identifiers '7' and '0', corresponding to values '6' and '5', respectively. The conformance rule for this entry is not explicitly provided in the data snippet, but if we assume a typical conformance scenario, it might involve conditions based on the presence or absence of certain features or states within the Switch Cluster. For example, if a conformance rule were to be applied, it could dictate that the element is mandatory, optional, provisional, deprecated, or disallowed based on the logical conditions involving feature codes or other elements. Without explicit conformance data, we cannot definitively interpret the rule, but it would typically guide the implementation requirements for this element within the Matter specification.

_Table parsed from section 'Multi Position Details':_

* The table row entry pertains to the Switch Cluster, specifically within the Multi Position Details section. The conformance rule provided is '7': '6', '0 b': 'a 5'. This rule indicates that the element in question is mandatory if the condition represented by '7' is true. If '7' is not true, then the element is optional if the condition '6' is true. If neither '7' nor '6' are true, the element is deprecated if the condition '0 b' is true. Finally, if none of these conditions are met, the element is optional if the condition 'a 5' is true. This conformance rule outlines a hierarchy of conditions that determine the requirement status of the element, ensuring that it adapts to various feature support scenarios within the Switch Cluster.

_Table parsed from section 'Multi Position Details':_

* In the context of the Switch Cluster, specifically within the Multi Position Details section, the table row data indicates a conformance rule for an element identified as '7', which is associated with 'c 6', and '0', which is associated with 'e 5'. The conformance rule 'c 6' suggests that the element is conditionally mandatory based on the support of a feature or condition labeled '6'. This means that if the condition '6' is met, the element '7' is required to be implemented. Conversely, the element '0' is linked to 'e 5', indicating a different condition or feature '5' that influences its conformance. The exact nature of these conditions ('6' and '5') would be detailed elsewhere in the documentation, but they dictate when these elements are required or optional within the Switch Cluster's Multi Position Details.

3
3
3
4
4
4
d
(i) no interaction, stick in middle position
(iii) move to SouthWest, then to South,
(ii) move to East and release (to middle)
then release (to middle position)
Figure 12. Switch device with joystick
Therefore, in the "joystick" variation, there could be a succession of InitialPress events without an
intermediate ShortRelease events - unlike the "window blinds control" variation which will always
have such an intermediate ShortRelease event.