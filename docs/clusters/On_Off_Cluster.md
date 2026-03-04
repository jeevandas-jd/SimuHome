
# 1.5 On/Off Cluster

Attributes and commands for turning devices on and off.

## Data Types
1.5.5.1. OnOffControlBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the On/Off Cluster, under the Data Types section, the table row describes a feature named 'AcceptOnlyWhenOn', which is represented by the bit '0'. This feature indicates that a command is only accepted when the device is in the On state. The conformance rule for 'AcceptOnlyWhenOn' is marked as 'M', meaning it is mandatory. This implies that the feature must always be implemented and supported in any device or application that adheres to this specification, without any conditions or exceptions.

1.5.5.2. StartUpOnOffEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the On/Off Cluster's Data Types, the table row describes an entry with the value '0', named 'Off', which is used to set the OnOff attribute to FALSE. The conformance rule for this entry is marked as 'M', indicating that this element is mandatory. This means that the ability to set the OnOff attribute to FALSE using the 'Off' value is a required feature for any implementation of the On/Off Cluster, with no conditions or exceptions.

* In the context of the On/Off Cluster's Data Types, the table row describes an element with the name "On," which is associated with the value "1" and is summarized as setting the OnOff attribute to TRUE. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "On" element is always required to be implemented in any device or application that supports the On/Off Cluster, without any conditions or exceptions.

* In the On/Off Cluster, under the Data Types section, the entry for 'Toggle' with a value of '2' describes a functionality that changes the state of the OnOff attribute: if the current state is FALSE, it switches to TRUE, and vice versa. The conformance rule 'M' indicates that this 'Toggle' feature is mandatory, meaning it is always required to be implemented in any device or application that supports the On/Off Cluster according to the Matter specification. This ensures consistent behavior across all compliant devices.

1.5.5.3. EffectIdentifierEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the On/Off Cluster within the Matter IoT specification, specifically under the Data Types section. It describes a data type with the value '0x00' and the name 'DelayedAllOff', summarized as 'Delayed All Off'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'DelayedAllOff' data type is always required to be implemented in any device or application that supports the On/Off Cluster, without any conditions or exceptions.

* In the On/Off Cluster, under the Data Types section, the table row describes an element with the value `0x01`, named `DyingLight`, which is summarized as "Dying Light." The conformance rule for this element is marked as `M`, indicating that it is mandatory. This means that the `DyingLight` element is always required to be implemented in any device or system that supports the On/Off Cluster, without any conditions or exceptions.

1.5.5.4. DelayedAllOffEffectVariantEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the On/Off Cluster, under the Data Types section, the table row describes a feature with the name 'DelayedOffFastFade', which is identified by the value '0x00'. This feature provides the functionality to fade to off in 0.8 seconds. According to the conformance rule 'M', this feature is mandatory, meaning it is always required to be implemented in any device or application that supports the On/Off Cluster. There are no conditions or dependencies that alter this requirement, making it an essential part of the cluster's functionality.

* In the context of the On/Off Cluster's Data Types, the table row describes an entry with the value `0x01`, named `NoFade`, which has a summary indicating "No fade." The conformance rule for this entry is marked as `M`, which stands for Mandatory. This means that the `NoFade` element is always required to be implemented in any device or application that supports the On/Off Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement status, making it an essential component of the cluster's functionality.

* In the context of the On/Off Cluster's Data Types, the table row describes a feature named "DelayedOffSlowFade" with a value of '0x02'. This feature provides a functionality where the light dims down to 50% over 0.8 seconds and then fades to off over 12 seconds. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the "DelayedOffSlowFade" feature is always required to be implemented in any device or application that supports the On/Off Cluster, according to the Matter IoT specification.

1.5.5.5. DyingLightEffectVariantEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the On/Off Cluster within the Data Types section and describes a specific feature named "DyingLightFadeOff," which is identified by the value '0x00'. This feature provides a lighting effect where the light dims up to 20% brightness in 0.5 seconds and then fades to off in 1 second. The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that any implementation of the On/Off Cluster must include the "DyingLightFadeOff" feature as a required element, without any conditions or exceptions.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the On/Off Cluster, specifically the "OnOff" attribute, which is identified by the ID '0x0000'. This attribute is of type 'bool', meaning it can hold a boolean value, and it applies to all instances of the cluster as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'SN', which typically refers to specific quality characteristics like 'Scene' or 'Notification'. The default value for this attribute is 'FALSE', and it has 'R V' access, meaning it is readable and can be viewed. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the OnOff attribute is always required to be implemented in any device or application that supports the On/Off Cluster, with no conditions or exceptions.

* The table row describes an attribute within the On/Off Cluster, specifically the "GlobalSceneControl" attribute. This attribute has an ID of '0x4000', is of type 'bool', and is constrained to 'all', meaning it applies universally within its context. The default value for this attribute is 'TRUE', and it has read and view access ('R V'). The conformance rule 'LT' indicates that this attribute is mandatory if the feature 'LT' is supported. In other words, if a device supports the 'LT' feature, it must implement the GlobalSceneControl attribute; otherwise, the conformance rule does not apply, and the attribute's inclusion is not required.

* The table row describes an attribute within the On/Off Cluster, specifically the 'OnTime' attribute. This attribute has an ID of '0x4001' and is of type 'uint16', meaning it is a 16-bit unsigned integer. It is constrained to apply to all relevant contexts within the cluster, has a default value of '0', and its access is defined as 'RW VO', indicating it is readable and writable, with volatile access. The conformance rule 'LT' suggests that the 'OnTime' attribute is mandatory if the feature 'LT' (likely representing a specific feature or condition within the Matter specification) is supported. If 'LT' is not supported, the attribute is not required. This conformance rule implies that the presence of the 'OnTime' attribute is conditional upon the support of the 'LT' feature.

* The table row describes an attribute within the On/Off Cluster, specifically the 'OffWaitTime' attribute, which has an ID of '0x4002'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally without specific constraints ('all'). The default value for 'OffWaitTime' is '0', and it has read-write access with volatile and optional characteristics ('RW VO'). The conformance rule 'LT' indicates that the presence of this attribute is mandatory if the feature or condition represented by 'LT' is supported. If 'LT' is not supported, the attribute is not required. The conformance rule does not specify any alternative conditions or fallback options, implying a straightforward dependency on the 'LT' feature.

* The table row describes an attribute named "StartUpOnOff" within the On/Off Cluster, identified by the ID '0x4003'. This attribute is of the type 'StartUpOnOffEnum' and has a constraint described elsewhere in the documentation. The quality is marked as 'XN', indicating it is not allowed in certain contexts. The default value is 'MS', and it has read-write and viewable/manageable access ('RW VM'). The conformance rule 'LT' suggests that the attribute is mandatory if the feature 'LT' is supported. If 'LT' is not supported, the conformance rule does not specify an alternative, implying that the attribute might not be required or its status is not defined in this context.

1.5.6.1. Scene Table Extensions
If the Scenes Management server cluster is implemented on the same endpoint, the following
attribute SHALL be part of the ExtensionFieldSetStruct of the Scene Table.
• OnOff
1.5.6.2. OnOff Attribute
This attribute indicates whether the device type implemented on the endpoint is turned off or
turned on, in these cases the value of the OnOff attribute equals FALSE, or TRUE respectively.
1.5.6.3. GlobalSceneControl Attribute
In order to support the use case where the user gets back the last setting of a set of devices (e.g.
level settings for lights), a global scene is introduced which is stored when the devices are turned
off and recalled when the devices are turned on. The global scene is defined as the scene that is
stored with group identifier 0 and scene identifier 0.
This attribute is defined in order to prevent a second Off command storing the all-devices-off situa
tion as a global scene, and to prevent a second On command destroying the current settings by
going back to the global scene.
This attribute SHALL be set to TRUE after the reception of a command which causes the OnOff
attribute to be set to TRUE, such as a standard On command, a MoveToLevel(WithOnOff) command,
a RecallScene command or a OnWithRecallGlobalScene command.
This attribute is set to FALSE after reception of a OffWithEffect command.
These concepts are illustrated in Explanation of the Behavior of Store and Recall Global Scene func
tionality using a State Diagram.
OffWithEffect
store global scene
other
other
commands
commands
GlobalSceneControl GlobalSceneControl
:= TRUE := FALSE
On
1
recall global scene
OnWithRecallGlobalScene
Note 1: Any command which causes the OnOff attribute to be set to TRUE except OnWithRecallGlobalScene, e.g. On or Toggle.
Figure 1. Explanation of the Behavior of Store and Recall Global Scene functionality using a State Diagram
1.5.6.4. OnTime Attribute
This attribute specifies the length of time (in 1/10ths second) that the On state SHALL be maintained
before automatically transitioning to the Off state when using the OnWithTimedOff command. This
attribute can be written at any time, but writing a value only has effect when in the Timed On state.
See OnWithTimedOff for more details.
1.5.6.5. OffWaitTime Attribute
This attribute specifies the length of time (in 1/10ths second) that the Off state SHALL be guarded to
prevent another OnWithTimedOff command turning the server back to its On state (e.g., when leav
ing a room, the lights are turned off but an occupancy sensor detects the leaving person and
attempts to turn the lights back on). This attribute can be written at any time, but writing a value
only has an effect when in the Timed On state followed by a transition to the Delayed Off state, or in
the Delayed Off state. See OnWithTimedOff for more details.
1.5.6.6. StartUpOnOff Attribute
This attribute SHALL define the desired startup behavior of a device when it is supplied with power
and this state SHALL be reflected in the OnOff attribute. If the value is null, the OnOff attribute is
set to its previous value. Otherwise, the behavior is defined in the table defining StartUpOnOf
fEnum.
This behavior does not apply to reboots associated with OTA. After an OTA restart, the OnOff
attribute SHALL return to its value prior to the restart.

## Commands

_Table parsed from section 'Commands':_

* In the context of the On/Off Cluster, the table row describes a command with the ID '0x00' named 'Off', which is directed from the client to the server. This command requires a response ('Y') and has optional access ('O'). The conformance rule for this command is 'M', indicating that it is mandatory. This means that the 'Off' command must always be implemented and supported in any device or application that conforms to the Matter specification for the On/Off Cluster, without any conditions or exceptions.

* The table row describes a command within the On/Off Cluster, specifically the "On" command, which is directed from the client to the server. The command has an ID of '0x01' and requires a response ('Y'). The access level is optional ('O'), meaning it is not required to be implemented unless specified by other conditions. The conformance rule '!OFFONLY' indicates that this command is mandatory if the device does not exclusively support the "Off" feature. In other words, if the device supports any functionality beyond just turning off (i.e., it can also turn on), the "On" command must be implemented. If the device is strictly an "Off-only" device, this command is not required.

* The table row describes a command within the On/Off Cluster, specifically the "Toggle" command, which is identified by the ID '0x02'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented unless specified by other conditions. The conformance rule '!OFFONLY' indicates that the "Toggle" command is mandatory unless the device supports the 'OFFONLY' feature. In simpler terms, if a device does not exclusively support the 'OFFONLY' feature, it must implement the "Toggle" command; otherwise, it is not required.

* The table row describes a command within the On/Off Cluster, specifically the "OffWithEffect" command, which is identified by the ID '0x40'. This command is directed from the client to the server and requires a response, as indicated by 'Response': 'Y'. The access level is optional ('Access': 'O'), meaning it is not required and has no dependencies. The conformance rule 'LT' suggests that the command is mandatory if the feature or condition represented by 'LT' is supported. If 'LT' is not supported, the conformance status of the command is not explicitly defined in this entry, implying it might not be required or its status is described elsewhere.

* The table row describes a command named "OnWithRecallGlobalScene" within the On/Off Cluster, specifically in the context of commands sent from a client to a server. The command has an ID of '0x41' and requires a response ('Y'), with access designated as optional ('O'). The conformance rule 'LT' indicates that the command is mandatory if the feature 'LT' is supported. If 'LT' is not supported, the command is not required. This means that the implementation of this command depends on whether the 'LT' feature is part of the device's capabilities.

* The table row describes a command named "OnWithTimedOff" within the On/Off Cluster, which is directed from the client to the server. This command requires a response, as indicated by 'Response: Y', and has optional access, as shown by 'Access: O'. The conformance rule 'LT' specifies that the command is mandatory if the feature 'LT' is supported. In this context, 'LT' likely refers to a specific feature or condition within the Matter specification. If the feature 'LT' is not supported, the conformance rule does not apply, and the command would not be mandatory.

1.5.7.1. Off Command
1.5.7.1.1. Effect on Receipt
On receipt of the Off command, a server SHALL set the OnOff attribute to FALSE.
Additionally, when the OnTime attribute is supported, the server SHALL set the OnTime attribute to
0.
1.5.7.2. On Command
1.5.7.2.1. Effect on Receipt
If the OffOnly feature is supported, on receipt of the On command, an UNSUPPORTED_COMMAND
failure status response SHALL be sent. Otherwise, on receipt of the On command, a server SHALL
set the OnOff attribute to TRUE.
Additionally, when the OnTime and OffWaitTime attributes are both supported, if the value of the
OnTime attribute is equal to 0, the server SHALL set the OffWaitTime attribute to 0.
1.5.7.3. Toggle Command
1.5.7.3.1. Effect on Receipt
If the OffOnly feature is supported, on receipt of the Toggle command, an UNSUPPORTED_COM
MAND failure status response SHALL be sent. Otherwise, on receipt of the Toggle command, if the
value of the OnOff attribute is equal to FALSE, the server SHALL set the OnOff attribute to TRUE,
otherwise, the server SHALL set the OnOff attribute to FALSE.
Additionally, when the OnTime and OffWaitTime attributes are both supported, if the value of the
OnOff attribute is equal to FALSE and if the value of the OnTime attribute is equal to 0, the server
SHALL set the OffWaitTime attribute to 0. If the value of the OnOff attribute is equal to TRUE, the
server SHALL set the OnTime attribute to 0.
1.5.7.4. OffWithEffect Command
The OffWithEffect command allows devices to be turned off using enhanced ways of fading.
The OffWithEffect command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the On/Off Cluster, specifically the "EffectIdentifier" command, which is of the type "EffectIdentifierEnum." The constraint for this command is described elsewhere in the documentation, as indicated by "desc." The conformance rule for this command is marked as "M," meaning it is mandatory. This indicates that the "EffectIdentifier" command must always be implemented and supported in any device or application that utilizes the On/Off Cluster, without any conditions or exceptions.

* The table row describes a command within the On/Off Cluster, specifically the "EffectVariant" command, which is identified by the ID '1' and is of type 'enum8'. The 'Constraint' for this command is described elsewhere in the documentation, and it has a default value of '0'. The 'Conformance' field is marked as 'M', indicating that this command is mandatory. This means that the "EffectVariant" command is always required to be implemented in any device or application that supports the On/Off Cluster, without any conditions or exceptions.

1.5.7.4.1. EffectIdentifier Field
This field specifies the fading effect to use when turning the device off. This field SHALL contain
one of the non-reserved values listed in EffectIdentifierEnum.
1.5.7.4.2. EffectVariant Field
This field is used to indicate which variant of the effect, indicated in the EffectIdentifier field,
SHOULD be triggered. If the server does not support the given variant, it SHALL use the default
variant. This field is dependent on the value of the EffectIdentifier field and SHALL contain one of
the non-reserved values listed in either DelayedAllOffEffectVariantEnum or DyingLightEffectVari
antEnum.
1.5.7.4.3. Effect on Receipt
On receipt of the OffWithEffect command the server SHALL check the value of the GlobalSceneCon
trol attribute.
If the GlobalSceneControl attribute is equal to TRUE, the server SHALL store its settings in its global
scene then set the GlobalSceneControl attribute to FALSE, then set the OnOff attribute to FALSE and
if the OnTime attribute is supported set the OnTime attribute to 0.
If the GlobalSceneControl attribute is equal to FALSE, the server SHALL only set the OnOff attribute
to FALSE.
1.5.7.5. OnWithRecallGlobalScene Command
This command allows the recall of the settings when the device was turned off.
1.5.7.5.1. Effect on Receipt
On receipt of the OnWithRecallGlobalScene command, if the GlobalSceneControl attribute is equal
to TRUE, the server SHALL discard the command.
If the GlobalSceneControl attribute is equal to FALSE, the Scenes Management cluster server on the
same endpoint SHALL recall its global scene, updating the OnOff attribute accordingly. The OnOff
server SHALL then set the GlobalSceneControl attribute to TRUE.
Additionally, when the OnTime and OffWaitTime attributes are both supported, if the value of the
OnTime attribute is equal to 0, the server SHALL set the OffWaitTime attribute to 0.
1.5.7.6. OnWithTimedOff Command
This command allows devices to be turned on for a specific duration with a guarded off duration so
that SHOULD the device be subsequently turned off, further OnWithTimedOff commands, received
during this time, are prevented from turning the devices back on. Further OnWithTimedOff com
mands received while the server is turned on, will update the period that the device is turned on.
The OnWithTimedOff command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the On/Off Cluster, specifically the "OnOffControl" command. This command is identified by the ID '0' and is of the type 'OnOffControlBitmap', with a constraint indicating its value can range from 0 to 1. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "OnOffControl" command is always required to be implemented in any device or application that supports the On/Off Cluster, without any conditions or exceptions.

* The table row describes an attribute within the On/Off Cluster, specifically a command named "OnTime" with an ID of '1'. This command is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value is 0xFFFE. The conformance rule for "OnTime" is marked as 'M', which stands for Mandatory. This means that the "OnTime" command is always required to be implemented in any device or application that supports the On/Off Cluster, without any conditions or exceptions.

* The table row describes a command within the On/Off Cluster, specifically the "OffWaitTime" command, which is identified by the ID '2'. This command is of the type 'uint16' and has a constraint that its maximum value should not exceed 0xFFFE. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the "OffWaitTime" command must always be implemented and supported in any device or application that utilizes the On/Off Cluster, without any conditions or exceptions.

1.5.7.6.1. OnOffControl Field
This field contains information on how the server is to be operated.
1.5.7.6.1.1. AcceptOnlyWhenOn Bit
This bit specifies whether the OnWithTimedOff command is to be processed unconditionally or
only when the OnOff attribute is equal to TRUE. If this sub-field is set to 1, the OnWithTimedOff
command SHALL only be accepted if the OnOff attribute is equal to TRUE. If this sub-field is set to 0,
the OnWithTimedOff command SHALL be processed unconditionally.
1.5.7.6.2. OnTime Field
This field is used to adjust the value of the OnTime attribute.
1.5.7.6.3. OffWaitTime Field
This field is used to adjust the value of the OffWaitTime attribute.
1.5.7.6.4. Effect on Receipt
On receipt of this command, if the AcceptOnlyWhenOn sub-field of the OnOffControl field is set to 1,
and the value of the OnOff attribute is equal to FALSE, the command SHALL be discarded.
If the value of the OffWaitTime attribute is greater than zero and the value of the OnOff attribute is
equal to FALSE, then the server SHALL set the OffWaitTime attribute to the minimum of the
OffWaitTime attribute and the value specified in the OffWaitTime field.
In all other cases, the server SHALL set the OnTime attribute to the maximum of the OnTime
attribute and the value specified in the OnTime field, set the OffWaitTime attribute to the value
specified in the OffWaitTime field and set the OnOff attribute to TRUE.
If the values of the OnTime and OffWaitTime attributes are both not equal to 0xFFFF, the server
th
SHALL then update these attributes every 1/10  second until both the OnTime and OffWaitTime
attributes are equal to 0, as follows:
• If the value of the OnOff attribute is equal to TRUE and the value of the OnTime attribute is
greater than zero, the server SHALL decrement the value of the OnTime attribute. If the value of
the OnTime attribute reaches 0, the server SHALL set the OffWaitTime and OnOff attributes to 0
and FALSE, respectively.
• If the value of the OnOff attribute is equal to FALSE and the value of the OffWaitTime attribute
is greater than zero, the server SHALL decrement the value of the OffWaitTime attribute. If the
value of the OffWaitTime attribute reaches 0, the server SHALL terminate the update.