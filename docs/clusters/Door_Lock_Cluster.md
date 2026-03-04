
# 5.2 Door Lock Cluster

The door lock cluster provides an interface to a generic way to secure a door. The physical object
that provides the locking functionality is abstracted from the cluster. The cluster has a small list of
mandatory attributes and functions and a list of optional features.
Figure 16. Typical Usage of the Door Lock Cluster

## Recommended steps for creating a new User
It is RECOMMENDED that the Administrator query the door lock for what users already exist in its
database to find an available UserIndex for creating a new User (see GetUser command).
1. Use SetUser command with an available UserIndex to set the user record fields as applicable.
2. Use SetCredential command with same UserIndex to add one or more credentials as applicable.
3. Use SetWeekDaySchedule command or SetYearDaySchedule command with same UserIndex to
add one or more schedule restrictions as applicable.

## Data Types
5.2.6.1. DaysMaskBitmap Type
This data type is derived from map8.
This bitmap SHALL indicate the days of the week the Week Day schedule applies for.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table row describes a feature related to scheduling, specifically indicating that the schedule is applied on Sunday. The 'Bit' value of '0' likely represents a specific position in a bitmask or similar data structure used to denote days of the week. The 'Name' of this feature is 'Sunday', and the 'Summary' clarifies that this bit is used to apply a schedule on Sundays. The 'Conformance' field is marked as 'M', which means that this feature is Mandatory. Therefore, any implementation of the Door Lock Cluster must include support for scheduling on Sundays, as it is a required element of the specification.

* In the Door Lock Cluster, under the Data Types section, the table row describes a feature named "Monday," which is associated with the bit value '1'. This feature indicates that a schedule is applied on Monday. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the "Monday" feature is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Data Types section, there is an entry for a bit labeled '2', named 'Tuesday'. This entry indicates that there is a feature related to scheduling that applies specifically to Tuesday. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the feature represented by this bit is always required to be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential part of the specification for ensuring that scheduling functionality for Tuesday is consistently supported.

* In the Door Lock Cluster's Data Types section, the table row describes a feature named "Wednesday," which is represented by the bit value '3'. This feature indicates that a schedule is applied on Wednesday. The conformance rule for this feature is marked as 'M', meaning it is mandatory. This indicates that the feature must always be implemented and supported in any device or application that conforms to this specification. There are no conditions or exceptions; the feature is required without any dependencies or optionality.

* In the context of the Door Lock Cluster's Data Types, the table row describes a feature named "Thursday," which is associated with the bit value '4'. This feature indicates that a schedule is applied on Thursday. The conformance rule for this feature is marked as 'M', meaning it is mandatory. This implies that the "Thursday" feature is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditional exceptions or dependencies.

* In the Door Lock Cluster's Data Types section, the table row describes a feature named "Friday," which is associated with bit 5. This feature indicates that a schedule is applied on Friday. The conformance rule for this feature is marked as "M," meaning it is mandatory. This implies that the "Friday" feature must always be implemented and supported in any device or application utilizing this Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster's Data Types section, the table row describes a feature named "Saturday," which is represented by bit 6. This feature indicates that a schedule is applied on Saturday. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or dependencies affecting its requirement status, ensuring that the "Saturday" schedule feature must be consistently available.

5.2.6.2. CredentialRulesBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes a feature named "Single," which is associated with the bit value '0'. The summary indicates that this feature means only one credential is required for lock operation. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the "Single" feature is always required to be implemented in any device or system that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions; it is a fundamental requirement.

* In the Door Lock Cluster, under the Data Types section, the table row describes a feature named "Dual," which is represented by the bit value '1'. The summary indicates that this feature requires any two credentials for lock operation, enhancing security by necessitating dual authentication. The conformance rule for this feature is marked as 'M', meaning it is mandatory. This implies that the "Dual" feature is always required to be implemented in any device or system that adheres to this specification, ensuring that dual credential verification is a standard feature for lock operations within the Matter protocol.

* In the Door Lock Cluster, under the Data Types section, there is an entry for a data type named 'Tri', which is represented by bit '2'. The summary indicates that this data type signifies that any three credentials are required for lock operation. The conformance rule for this entry is 'M', which means that the 'Tri' data type is mandatory. This implies that it is always required to be implemented in any device or system that adheres to this specification, without any conditions or exceptions.

5.2.6.3. OperatingModesBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes a feature named "Normal," which is associated with bit '0' and represents the "Normal operation mode." The conformance rule for this feature is marked as 'M,' which stands for Mandatory. This means that the "Normal" operation mode is a required element within the Door Lock Cluster specification and must be implemented in all devices that conform to this specification. There are no conditions or dependencies affecting this requirement, making it an essential feature for ensuring standard functionality across compliant devices.

* In the Door Lock Cluster, under the Data Types section, there is an entry for a feature named "Vacation," which is associated with bit '1' and summarized as "Vacation operation mode." The conformance rule for this feature is marked as 'O,' indicating that the "Vacation" operation mode is optional. This means that while the feature can be implemented, it is not required and does not depend on any other features or conditions within the Matter specification. Devices implementing the Door Lock Cluster may choose to support this feature, but they are not obligated to do so.

* In the context of the Door Lock Cluster's Data Types, the table row describes a feature named "Privacy," which is associated with bit 2 and represents a privacy operation mode. According to the conformance rule specified as "O," this feature is optional. This means that the implementation of the "Privacy" feature is not required and has no dependencies on other features or conditions. Devices or systems implementing the Door Lock Cluster can choose to include this feature, but it is not mandatory for compliance with the Matter specification.

* In the Door Lock Cluster's Data Types section, the table row describes a feature identified by the bit '3', named 'NoRemoteLockUnlock', which signifies a mode where remote lock and unlock operations are not allowed. The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that the 'NoRemoteLockUnlock' feature must always be implemented in any device or system that conforms to the Matter specification for the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster's Data Types section, the table row describes a data element named "Passage," which is associated with bit 4 and represents the "Passage operation mode." The conformance for this element is marked as "O," indicating that it is optional. This means that the "Passage" feature is not required to be implemented and does not have any dependencies on other features or conditions. Implementers of the Door Lock Cluster can choose to include or exclude this feature based on their specific needs or preferences, without affecting the compliance with the Matter specification.

5.2.6.4. ConfigurationRegisterBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Door Lock Cluster, specifically a data type related to the 'LocalProgramming' feature. This feature is represented by the bit '0' and pertains to the state of local programming functionality for the door lock. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'LocalProgramming' feature is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it a fundamental component of the cluster.

* The table row describes an element within the Door Lock Cluster, specifically in the Data Types section, concerning the 'KeypadInterface'. This element is identified by the bit '1' and is summarized as representing the state of the keypad interface. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'KeypadInterface' element is always required to be implemented in any device or application that supports the Door Lock Cluster, with no exceptions or conditions.

* In the context of the Door Lock Cluster's Data Types, the table row describes an element named "RemoteInterface," which is represented by bit 2. This element summarizes the state of the remote interface. According to the conformance rule 'M,' this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Door Lock Cluster. There are no conditions or dependencies affecting its requirement status, making it an essential component of the cluster's specification.

* In the Door Lock Cluster, within the Data Types section, there is an entry for a data type named 'SoundVolume', which is associated with bit '5'. The summary indicates that this data type is used to set the sound volume to a silent value. The conformance rule for 'SoundVolume' is marked as 'M', meaning it is mandatory. This implies that the 'SoundVolume' feature must always be implemented and supported in any device or application that conforms to this specification of the Door Lock Cluster. There are no conditions or exceptions; it is a required element.

* In the Door Lock Cluster, under the Data Types section, the entry for 'AutoRelockTime' at bit position 6 indicates a feature related to setting the auto relock time to 0. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'AutoRelockTime' feature is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Data Types section, the table row describes a feature named "LEDSettings" associated with bit 7. The summary indicates that this feature pertains to the disabling of LEDs. The conformance rule for "LEDSettings" is marked as "M," which stands for Mandatory. This means that the feature is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.6.4.1. LocalProgramming Bit
This bit SHALL indicate the state related to local programming:
• 0 = Local programming is disabled
• 1 = Local programming is enabled
5.2.6.4.2. KeypadInterface Bit
This bit SHALL indicate the state related to keypad interface:
• 0 = Keypad interface is disabled
• 1 = Keypad interface is enabled
5.2.6.4.3. RemoteInterface Bit
This bit SHALL indicate the state related to remote interface:
• 0 = Remote interface is disabled
• 1 = Remote interface is enabled
5.2.6.4.4. SoundVolume Bit
This bit SHALL indicate the state related to sound volume:
• 0 = Sound volume value is 0 (Silent)
• 1 = Sound volume value is equal to something other than 0
5.2.6.4.5. AutoRelockTime Bit
This bit SHALL indicate the state related to auto relock time:
• 0 = Auto relock time value is 0
• 1 = Auto relock time value is equal to something other than 0
5.2.6.4.6. LEDSettings Bit
This bit SHALL indicate the state related to LED settings:
• 0 = LED settings value is 0 (NoLEDSignal)
• 1 = LED settings value is equal to something other than 0
5.2.6.5. LocalProgrammingFeaturesBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, specifically within the Data Types section, there is an entry for a feature named "AddUsersCredentialsSchedules," which is represented by the bit '0'. This feature pertains to the capability of the device to add users, credentials, or schedules. The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that any implementation of the Door Lock Cluster must include this feature, as it is a required element without any conditions or exceptions.

* In the Door Lock Cluster, under the Data Types section, the entry for 'ModifyUsersCredentialsSchedules' with a bit value of '1' represents the capability to modify users, credentials, or schedules on the device. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the feature is always required to be implemented in any device that supports the Door Lock Cluster. There are no conditions or dependencies affecting this requirement; it is a fundamental aspect of the device's functionality.

* In the Door Lock Cluster's Data Types section, the entry for 'ClearUsersCredentialsSchedules' at bit position '2' describes the feature that indicates the device's capability to clear users, credentials, or schedules. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the ability to clear users, credentials, or schedules is a required feature for any device implementing this cluster, and it must always be supported without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the table row describes a feature named "AdjustSettings," which is represented by bit 3. This feature indicates the state of the ability to adjust settings on the device. The conformance rule for "AdjustSettings" is marked as 'M', which means it is mandatory. This implies that the "AdjustSettings" feature is always required to be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.6.5.1. AddUsersCredentialsSchedules Bit
This bit SHALL indicate whether the door lock is able to add Users/Credentials/Schedules locally:
• 0 = This ability is disabled
• 1 = This ability is enabled
5.2.6.5.2. ModifyUsersCredentialsSchedules Bit
This bit SHALL indicate whether the door lock is able to modify Users/Credentials/Schedules locally:
• 0 = This ability is disabled
• 1 = This ability is enabled
5.2.6.5.3. ClearUsersCredentialsSchedules Bit
This bit SHALL indicate whether the door lock is able to clear Users/Credentials/Schedules locally:
• 0 = This ability is disabled
• 1 = This ability is enabled
5.2.6.5.4. AdjustSettings Bit
This bit SHALL indicate whether the door lock is able to adjust lock settings locally:
• 0 = This ability is disabled
• 1 = This ability is enabled
5.2.6.6. AlarmMaskBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the entry for 'Bit' 0, named 'LockJammed', represents a data type that indicates when the locking mechanism is jammed. The 'Summary' provides a brief description of its purpose. The 'Conformance' field is marked as 'M', which means that this element is mandatory. According to the Matter Conformance Interpretation Guide, this indicates that the 'LockJammed' data type is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Data Types section, the entry for 'LockFactoryReset' with a bit value of '1' represents the feature that allows the lock to be reset to its factory defaults. The conformance rule for this feature is marked as 'O', which means it is optional. This indicates that the implementation of the 'LockFactoryReset' feature is not mandatory and does not depend on any other conditions or features. Manufacturers can choose whether or not to include this feature in their devices, but it is not required by the Matter specification.

* In the Door Lock Cluster, under the Data Types section, there is an entry for a data type named 'LockRadioPowerCycled', which is represented by the bit '3'. This data type is summarized as indicating when the RF Module has been power cycled. The conformance for 'LockRadioPowerCycled' is marked as 'O', which means it is optional. This indicates that the implementation of this data type is not required and does not depend on any other features or conditions. Devices implementing the Door Lock Cluster can choose to support this data type, but they are not obligated to do so according to the Matter specification.

* The table row describes an element within the Door Lock Cluster, specifically under the Data Types section, named "WrongCodeEntryLimit." This element is associated with a tamper alarm feature that triggers when a wrong code is entered too many times. The conformance rule "PIN | RID" indicates that the "WrongCodeEntryLimit" element is mandatory if either the PIN feature or the RID feature is supported by the device. In other words, if a device supports either of these features, it must also implement the "WrongCodeEntryLimit" element to comply with the Matter specification.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table row describes a data element named 'FrontEscutcheonRemoved', which is associated with bit 5. This element serves as a tamper alarm indicating that the front escutcheon has been removed from the main unit. The conformance rule for this element is marked as 'O', meaning it is optional. This indicates that the implementation of this feature is not required and does not depend on any other conditions or features. Devices supporting the Door Lock Cluster may choose to implement this feature, but it is not mandatory for compliance with the Matter specification.

* In the Door Lock Cluster, under the Data Types section, the entry for 'Bit' 6 is named 'DoorForcedOpen' and is summarized as indicating a "Forced Door Open under Door Locked Condition." The conformance rule for this entry is 'O', which means that the 'DoorForcedOpen' feature is optional. This indicates that the implementation of this feature is not required and has no dependencies on other features or conditions. Devices or systems implementing the Door Lock Cluster can choose to include this feature, but they are not obligated to do so according to the Matter specification.

5.2.6.7. AlarmCodeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the alarm type.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table entry describes a data type with the value '0' named 'LockJammed', which indicates that the locking mechanism is jammed. The conformance rule for this entry is 'M', meaning that the 'LockJammed' data type is mandatory. This implies that any implementation of the Door Lock Cluster must include this data type, as it is always required according to the Matter specification.

* The table row describes a data type within the Door Lock Cluster, specifically named "LockFactoryReset," which is associated with the action of resetting a lock to its factory defaults. The conformance rule for this data type is marked as "O," indicating that the "LockFactoryReset" feature is optional. This means that while the feature can be implemented, it is not required and does not depend on any other features or conditions to be included in a device's implementation of the Matter specification.

* In the Door Lock Cluster, under the Data Types section, there is an entry with the name "LockRadioPowerCycled" and a value of '3'. This entry represents a data type that indicates the event of the lock's radio power being cycled. The conformance rule for this entry is marked as 'O', which stands for Optional. This means that the "LockRadioPowerCycled" data type is not a required element within the specification and can be implemented at the discretion of the manufacturer or developer, without any dependencies or conditions that must be met.

* In the Door Lock Cluster, under the Data Types section, the entry for 'WrongCodeEntryLimit' with a value of '4' pertains to the feature that sets a tamper alarm threshold for incorrect code entries. The conformance rule '[USR]' indicates that this feature is optional, but only if the condition represented by 'USR' is true. This means that the 'WrongCodeEntryLimit' is not required by default, but it becomes an optional feature if the specific condition or feature 'USR' is supported within the implementation.

* In the Door Lock Cluster, under the Data Types section, the entry for 'FrontEsceutcheonRemoved' with a value of '5' represents a tamper alarm indicating that the front escutcheon has been removed from the main unit. The conformance rule for this entry is marked as 'O', which means that this feature is optional. It is not required for implementation and does not have any dependencies on other features or conditions. Therefore, manufacturers can choose whether or not to include this feature in their devices without any obligation.

* The table row entry pertains to the "DoorForcedOpen" data type within the Door Lock Cluster, specifically under the Data Types section. This entry represents a condition where a door is forced open while it is locked. The conformance rule for "DoorForcedOpen" is specified as `[DPS]`, which means that this element is optional if the condition `DPS` is true. In other words, the "DoorForcedOpen" data type is not required by default but can be included if the feature or condition represented by `DPS` is supported or applicable.

* In the Door Lock Cluster, under the Data Types section, the entry for 'DoorAjar' with a value of '7' represents a data type indicating that a door is ajar. The conformance rule '[DPS]' specifies that this element is optional if the condition 'DPS' is true. This means that the 'DoorAjar' data type is not required by default, but it becomes optional to implement if the feature or condition represented by 'DPS' is supported. If 'DPS' is not supported, there is no requirement to include this data type.

* In the Door Lock Cluster, under the Data Types section, there is an entry named 'ForcedUser' with a value of '8', which represents a feature related to a "Force User SOS alarm." The conformance rule for this entry is '[USR]', indicating that the 'ForcedUser' feature is optional if the condition 'USR' is true. This means that if the device or implementation supports the 'USR' feature, the 'ForcedUser' element can be included, but it is not mandatory. If 'USR' is not supported, the 'ForcedUser' element is not applicable.

5.2.6.8. CredentialRuleEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the credential rule that can be applied to a particular user.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes a data entry with the value '0' and the name 'Single', which indicates that only one credential is required for lock operation. The conformance rule 'USR' specifies that this element is mandatory if the feature 'USR' (likely representing a User-related feature) is supported. If 'USR' is not supported, the conformance of this element is not defined by this rule, implying it may not be required. This ensures that the 'Single' credential requirement is enforced only when the relevant user feature is present.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the entry with the name "Dual" and a value of "1" indicates that for lock operation, any two credentials are required. The conformance rule `[USR]` specifies that this feature is optional if the condition `USR` is true, meaning that if the feature or condition represented by `USR` is supported, the "Dual" credential requirement can be optionally implemented. If `USR` is not supported, the feature is not required.

* In the context of the Door Lock Cluster's Data Types, the table row describes a feature named "Tri" with a value of '2'. This feature indicates that any three credentials are required for lock operation. The conformance rule for this feature is `[USR]`, which means that the feature is optional if the condition `USR` is true. In other words, the "Tri" feature is not mandatory but can be included if the system supports the `USR` feature, allowing for flexibility in implementation based on the presence of the `USR` feature.

5.2.6.9. CredentialTypeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the credential type.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the entry for 'ProgrammingPIN' with a value of '0' represents a credential type specifically for a Programming PIN code. The conformance rule for this entry is 'O', which means that the 'ProgrammingPIN' is optional. This indicates that while the feature is available, it is not required to be implemented and does not have any dependencies on other features or conditions. Implementers of the Door Lock Cluster can choose to include or exclude this element based on their specific needs or design preferences.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the name "PIN," which represents a PIN code credential type. The conformance rule for this entry is simply "PIN," indicating that the presence of this data type is mandatory if the feature or condition identified as "PIN" is supported. This means that if the system or device includes support for the "PIN" feature, then the PIN code credential type must be implemented. If the "PIN" feature is not supported, the conformance rule does not apply, and the data type is not required.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '2', named 'RFID', which represents the RFID identifier credential type. The conformance rule for this entry is 'RID', which, according to the Matter Conformance Interpretation Guide, implies a condition that is not explicitly defined in the basic tags or expressions provided. However, it suggests that the RFID credential type is subject to specific conditions or requirements that are detailed elsewhere in the documentation. This means the inclusion or support of the RFID credential type depends on certain criteria or features that are not directly explained in the provided conformance string, indicating a need to refer to additional documentation for full understanding.

* In the Door Lock Cluster's Data Types section, the table row describes a data type with the name "Fingerprint," which is identified by the value '3' and serves as a fingerprint identifier credential type. The conformance rule for this entry is 'FGP', indicating that it is currently in a provisional state. This means that the status of the "Fingerprint" data type is temporary and may change in the future. The provisional status suggests that it might become mandatory or undergo other changes as the Matter specification evolves. For now, its implementation is not strictly required, but developers should be aware that its conformance status could be updated in future versions of the specification.

* In the Door Lock Cluster's Data Types section, the table entry describes a credential type named "FingerVein," identified by the value '4'. This credential type is summarized as a "finger vein identifier." The conformance rule for "FingerVein" is specified as 'FGP', which indicates that its status is provisional. This means that currently, the "FingerVein" credential type is in a temporary state and may be subject to change. The provisional status suggests that it might become mandatory in the future, but for now, it is not required.

* In the context of the Door Lock Cluster's Data Types, the table row describes a credential type with the name "Face" and a value of '5', which serves as a face identifier. The conformance rule for this entry is 'FACE', indicating that the inclusion of this element is mandatory if the feature or condition represented by 'FACE' is supported. If the system or device supports the 'FACE' feature, then the "Face" credential type must be implemented. If 'FACE' is not supported, the conformance rule does not apply, and the element is not required.

* The table row entry pertains to the Door Lock Cluster within the Data Types section and describes a data type named "AliroCredentialIssuerKey," which is a public key for a Credential Issuer as defined in the Aliro specification. The conformance rule for this data type is specified as "ALIRO," indicating that the inclusion of this element is mandatory if the feature or condition represented by "ALIRO" is supported. In other words, if the system or device supports the "ALIRO" feature, then the "AliroCredentialIssuerKey" must be implemented. If "ALIRO" is not supported, the requirement for this element does not apply.

* The table row describes an entry within the Door Lock Cluster's Data Types section, specifically focusing on the 'AliroEvictableEndpointKey'. This data type, identified by the value '7', represents an endpoint public key as defined in the Aliro specification, which can be evicted to make space for another endpoint key if necessary. The conformance rule 'ALIRO' indicates that this element is mandatory if the Aliro feature is supported. In other words, if the system or device implements the Aliro feature, it must include support for the 'AliroEvictableEndpointKey' data type.

* In the Door Lock Cluster's Data Types section, the entry for 'AliroNonEvictableEndpointKey' represents a data type with a value of '8'. This data type is used to store an endpoint public key as defined by the Aliro specification, ensuring that this key cannot be evicted to make space for another endpoint key. The conformance rule 'ALIRO' indicates that this element is mandatory if the feature or condition 'ALIRO' is supported. If the Aliro feature is implemented in the system, this data type must be included.

5.2.6.9.1. AliroCredentialIssuerKey Value
Credentials of this type SHALL be 65-byte uncompressed elliptic curve public keys as defined in sec
tion 2.3.3 of SEC 1.
Credentials of this type SHALL NOT be used to allow operating the lock. They SHALL be used, as
defined in [Aliro], to create new credentials of type AliroEvictableEndpointKey via a step-up trans
action.
When performing the step-up transaction, the lock SHALL request the data element with identifier
"matter1", and SHALL attempt to create a new credential of type AliroEvictableEndpointKey if and
only if the data element is returned and the Access Credential can be validated using the AliroCre
dentialIssuerKey.
When a new credential of type AliroEvictableEndpointKey is added in this manner, it SHALL be
associated with the same user record as the AliroCredentialIssuerKey credential that allowed the
new credential to be added.
If there are no available credential slots to add a new AliroEvictableEndpointKey credential (i.e.
either the NumberOfCredentialsSupportedPerUser or the NumberOfAliroEndpointKeysSupported
limit has been reached) but there exist credentials of type AliroEvictableEndpointKey associated
with the user record, the server SHALL remove one of those credentials using the same procedure
it would follow for the ClearCredential command before adding the new credential.
If there are no available credential slots to add a new AliroEvictableEndpointKey credential (i.e.
either the NumberOfCredentialsSupportedPerUser or the NumberOfAliroEndpointKeysSupported
limit has been reached) and there do not exist credentials of type AliroEvictableEndpointKey asso
ciated with the user record, a new AliroEvictableEndpointKey credential SHALL NOT be created.
If the step-up process results in addition of new credentials, the corresponding LockUserChange
event SHALL have OperationSource set to Aliro.
If the step-up process results in the lock state changing (e.g. locking or unlocking), the credential
associated with those changes in the LockOperation events SHALL be the newly provisioned AliroE
victableEndpointKey credential if one was created. If no new AliroEvictableEndpointKey credential
was created, the credential associated with the changes in the LockOperation events SHALL be the
AliroCredentialIssuerKey credential used for the step-up.
5.2.6.9.2. AliroEvictableEndpointKey Value
Credentials of this type SHALL be 65-byte uncompressed elliptic curve public keys as defined in sec
tion 2.3.3 of SEC 1.
5.2.6.9.3. AliroNonEvictableEndpointKey Value
Credentials of this type SHALL be 65-byte uncompressed elliptic curve public keys as defined in sec
tion 2.3.3 of SEC 1.
5.2.6.10. DataOperationTypeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the data operation performed.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster, within the Data Types section, the table row describes a data type with the value '0' and the name 'Add'. This data type signifies that data is either in the process of being added or has already been added, as summarized by its description. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Add' data type is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the name "Clear" and a value of "1," which indicates that data is being cleared or has been cleared. The conformance rule for this entry is marked as "M," meaning it is mandatory. This implies that the "Clear" data type must always be implemented and supported in any device or application that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or dependencies affecting this requirement, making it an essential component of the specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '2' and the name 'Modify'. This entry signifies that the data is being modified or has been modified, as summarized in the 'Summary' field. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Modify' data type is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.6.11. DoorStateEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the current door state.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes an element with the value '0' named 'DoorOpen', which indicates that the door state is open. The conformance rule for this element is 'DPS', which combines multiple conformance tags. The 'D' indicates that the element is Deprecated, meaning it is considered obsolete in the current specification and should not be used in new implementations. The 'P' suggests a Provisional status, indicating that its current deprecated status might change in the future, potentially becoming mandatory or optional. The 'S' is not a standard conformance tag according to the provided guide, so it might be a typographical error or an undocumented tag. Overall, this entry signifies that while the 'DoorOpen' state is defined, it is currently deprecated and should be used with caution, keeping in mind potential future changes to its status.

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '1', named 'DoorClosed', which indicates that the door state is closed. The conformance rule for this entry is 'DPS'. According to the Matter Conformance Interpretation Guide, 'D' stands for Deprecated, meaning this element is considered obsolete in the current specification. The 'P' indicates a Provisional status, suggesting that while the element is currently deprecated, there might be plans for it to become mandatory or optional in the future. The 'S' is not explicitly defined in the provided guide, but typically in such contexts, it might imply a special or specific condition that is described elsewhere in the documentation. Overall, this entry is currently not recommended for use, but its status may change in future updates of the specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '2', named 'DoorJammed', which indicates that the door state is jammed. The conformance rule '[DPS]' specifies that the 'DoorJammed' element is optional if the condition 'DPS' is true. This means that the inclusion of the 'DoorJammed' state is not mandatory and depends on whether the feature or condition represented by 'DPS' is supported. If 'DPS' is supported, then the 'DoorJammed' state can be optionally included in the implementation.

* In the context of the Door Lock Cluster's Data Types, the entry for 'DoorForcedOpen' with a value of '3' indicates a state where the door is currently forced open. The conformance rule '[DPS]' specifies that this element is optional if the condition 'DPS' is true. This means that the 'DoorForcedOpen' state is not mandatory and only needs to be implemented if the feature or condition represented by 'DPS' is supported. If 'DPS' is not supported, there is no requirement to include this element.

* In the Door Lock Cluster's Data Types section, the entry for 'DoorUnspecifiedError' with a value of '4' indicates a state where the door is invalid for an unspecified reason. The conformance rule '[DPS]' means that this element is optional if the feature 'DPS' is supported. In other words, the inclusion of 'DoorUnspecifiedError' is not mandatory but can be included if the specific condition related to 'DPS' is met, allowing for flexibility in implementation based on the presence of this feature.

* The table row entry pertains to the "DoorAjar" data type within the Door Lock Cluster's Data Types section. This entry indicates that the "DoorAjar" data type, which signifies that the door state is ajar, is conditionally optional. According to the conformance rule `[DPS]`, the "DoorAjar" data type is optional if the feature or condition represented by `DPS` is supported. If `DPS` is not supported, the "DoorAjar" data type is not required. This conditional optionality allows for flexibility in implementation, depending on whether the specific feature `DPS` is part of the device's supported features.

5.2.6.12. LockDataTypeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the data type that is being or has changed.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the entry with the 'Value' of '0' and 'Name' of 'Unspecified' refers to a data type that indicates unspecified or manufacturer-specific lock user data that has been added, cleared, or modified. The 'Conformance' field for this entry is marked as 'O', which means that this element is optional. It is not required for implementation and has no dependencies on other features or conditions. This allows manufacturers the flexibility to include or exclude this data type based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the Door Lock Cluster, under the Data Types section, the entry for 'ProgrammingCode' with a value of '1' signifies an event where a lock programming PIN code has been added, cleared, or modified. The 'Conformance' field for this entry is marked as 'O', indicating that the 'ProgrammingCode' element is optional. This means that while it is not required for implementation, it can be included at the discretion of the developer, and there are no dependencies or conditions that must be met for its inclusion.

* In the Door Lock Cluster, under the Data Types section, the entry for 'UserIndex' with a value of '2' signifies a data type that indicates when a lock user index has been added, cleared, or modified. The conformance rule for 'UserIndex' is marked as 'M', which means that this element is mandatory. It is always required to be implemented in any device or system that supports the Door Lock Cluster, ensuring that the functionality related to user index management is consistently available across all compliant implementations.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the Door Lock Cluster within the Data Types section, specifically focusing on the 'WeekDaySchedule' element. This element, identified by the value '3', is summarized as a feature that indicates when a lock user's weekday schedule has been added, cleared, or modified. The conformance rule 'WDSCH' implies that the 'WeekDaySchedule' element is mandatory if the feature code 'WDSCH' is supported by the device. In other words, if the device includes support for the weekday scheduling feature, then the 'WeekDaySchedule' element must be implemented as part of the Door Lock Cluster.

* The table row describes an entry within the Door Lock Cluster's Data Types section, specifically focusing on the 'YearDaySchedule' feature. This feature is identified by the value '4' and is summarized as a schedule related to the lock user's year day that can be added, cleared, or modified. The conformance rule 'YDSCH' indicates that the 'YearDaySchedule' feature is mandatory if the condition represented by 'YDSCH' is true. This means that if the system or device supports the 'YDSCH' feature, then the 'YearDaySchedule' must be implemented as part of the Door Lock Cluster. If 'YDSCH' is not supported, the feature is not required.

* The table row describes an entry within the Door Lock Cluster's Data Types, specifically concerning the 'HolidaySchedule' feature. This feature, identified by the value '5', is summarized as indicating when a lock's holiday schedule has been added, cleared, or modified. The conformance rule 'HDSCH' implies that the 'HolidaySchedule' feature is mandatory if the condition 'HDSCH' is true. This means that if the system or device supports the 'HDSCH' feature, then the 'HolidaySchedule' element must be implemented. If 'HDSCH' is not supported, the conformance rule does not specify an alternative, suggesting that the feature is not required in such cases.

* The table row entry pertains to the Door Lock Cluster within the Data Types section, specifically focusing on the element named 'PIN', which has a value of '6'. This element represents a lock user PIN code that can be added, cleared, or modified, as summarized in its description. The conformance rule for this element is simply 'PIN', indicating that the element is mandatory if the feature or condition identified as 'PIN' is supported. In other words, if the system or device supports the 'PIN' feature, this element must be implemented. There are no additional conditions or optional statuses associated with this conformance rule.

* In the Door Lock Cluster's Data Types section, the table entry describes a data type with the value '7' named 'RFID'. This entry summarizes that the RFID code for a lock user was added, cleared, or modified. The conformance rule for this entry is 'RID', which, according to the Matter Conformance Interpretation Guide, indicates that the element is mandatory if the feature 'RID' is supported. If 'RID' is not supported, the conformance status of this element is not explicitly defined in the provided context, suggesting it may not be required. Thus, the presence of this data type is contingent upon the support of the 'RID' feature within the implementation.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type named "Fingerprint" with a value of '8'. This data type is used to indicate that a lock user's fingerprint has been added, cleared, or modified. The conformance rule for this entry is 'FGP', which means it is provisional. This indicates that the inclusion of the "Fingerprint" data type is currently temporary and may be subject to change. The provisional status suggests that it might become mandatory in future versions of the specification, but for now, its implementation is not strictly required.

* In the Door Lock Cluster, under the Data Types section, the entry for 'FingerVein' with a value of '9' refers to the data type used to indicate that lock user finger-vein information has been added, cleared, or modified. The conformance rule 'FGP' suggests that the inclusion of this element is conditional. Specifically, it is provisional, meaning that its current status is temporary and may change in the future. The 'FGP' conformance indicates that this element is currently in a provisional state, and it is likely intended to become mandatory in the future, depending on the evolution of the specification or the support of certain features.

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '10' and the name 'Face'. This entry summarizes that the lock user face information was added, cleared, or modified. The conformance rule 'FACE' indicates that this element is mandatory if the feature 'FACE' is supported. If the device or implementation includes support for the 'FACE' feature, then this element must be included as part of the specification. If 'FACE' is not supported, the conformance rule does not apply, and the element is not required.

* In the context of the Door Lock Cluster's Data Types, the entry for 'AliroCredentialIssuerKey' with a value of '11' represents a specific type of credential related to the Aliro system, indicating that an Aliro credential issuer key has been added, cleared, or modified. The conformance rule 'ALIRO' implies that the presence of this element is mandatory if the feature or condition identified as 'ALIRO' is supported. If the system or device supports the 'ALIRO' feature, then the 'AliroCredentialIssuerKey' must be implemented; otherwise, it is not required.

* The table row describes a data type within the Door Lock Cluster, specifically named "AliroEvictableEndpointKey." This data type represents an Aliro endpoint key credential that can be evicted, indicating it was added, cleared, or modified. The conformance rule for this data type is "ALIRO," which means it is mandatory if the feature or condition identified as "ALIRO" is supported. If the "ALIRO" feature is not supported, this data type is not required. This conformance rule ensures that the presence of the "AliroEvictableEndpointKey" is conditional upon the support for the "ALIRO" feature within the device or system implementing the Matter specification.

* The table row describes a data type within the Door Lock Cluster, specifically named "AliroNonEvictableEndpointKey," which represents a credential for an Aliro endpoint key that cannot be evicted and has been added, cleared, or modified. The conformance rule for this data type is "ALIRO," indicating that the presence of this element is mandatory if the feature or condition represented by "ALIRO" is supported. In other words, if the system or device supports the ALIRO feature, this data type must be implemented; otherwise, it is not required.

5.2.6.13. LockOperationTypeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the type of Lock operation performed.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster, under the Data Types section, the table row describes an element with the 'Value' of '0' and the 'Name' of 'Lock', which summarizes the 'Lock operation'. The 'Conformance' field for this element is marked as 'M', indicating that it is mandatory. This means that the 'Lock' operation is a required feature for any implementation of the Door Lock Cluster according to the Matter specification. It must always be included and supported without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Data Types section, the table row describes an element with the name "Unlock," which represents an "Unlock operation" with a value of '1'. The conformance rule for this element is marked as 'M', indicating that it is mandatory. This means that the "Unlock" operation is a required feature that must be implemented in any device or application that supports the Door Lock Cluster according to the Matter IoT specification. There are no conditions or dependencies affecting its mandatory status; it is always required.

* The table row describes an element within the Door Lock Cluster, specifically under the Data Types section. The element is named "NonAccessUserEvent" and is identified by the value '2'. This event is triggered when a keypad entry is made for a user whose User Type is set to Non Access User. According to the conformance rule 'O', this element is optional, meaning it is not required for implementation and has no dependencies on other features or conditions. Implementers of the Matter specification can choose to include this element, but it is not mandatory for compliance.

* In the Door Lock Cluster's Data Types section, the entry for 'ForcedUserEvent' with a value of '3' indicates an event triggered when a user with the UserType set to 'Forced User' interacts with the system. The conformance rule for this entry is 'O', which means that the 'ForcedUserEvent' is optional. This implies that while the feature is available for implementation, it is not required and does not depend on any other conditions or features being supported. Implementers have the discretion to include or exclude this event based on their specific needs or use cases.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '4', named 'Unlatch', which pertains to the 'Unlatch operation'. The conformance rule for this entry is 'M', indicating that the 'Unlatch' operation is a mandatory element. This means that any implementation of the Door Lock Cluster must include support for the 'Unlatch' operation without exception. It is a required feature that must be present to comply with the Matter specification for this cluster.

5.2.6.14. OperationErrorEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the error cause of the Lock/Unlock operation performed.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '0' and the name 'Unspecified'. This data type is used to indicate a lock or unlock error caused by an unknown or unspecified source. The conformance rule for this entry is 'O', which means that the inclusion of this data type is optional. It is not required for implementation and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this data type based on their specific needs or preferences.

* In the Door Lock Cluster's Data Types section, the entry for 'InvalidCredential' with a value of '1' represents an error condition where a lock or unlock operation fails due to an invalid PIN, RFID, fingerprint, or other credential. The conformance rule 'USR' indicates that this element is mandatory if the feature or condition represented by 'USR' is supported. If 'USR' is not supported, the conformance of this element is not specified in this entry, implying it may not be required. This ensures that systems supporting the 'USR' feature must handle this specific error condition.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a specific value labeled 'DisabledUserDenied', which has a numerical value of '2'. This entry represents an error condition where a lock or unlock operation fails due to a user or credential being disabled. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'DisabledUserDenied' value must always be implemented and supported in any device or system that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions; it is a required element in all cases.

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '3', named 'Restricted'. This entry signifies a lock/unlock error caused by a schedule restriction. The conformance rule 'WDSCH | YDSCH' indicates that this element is mandatory if either the WDSCH feature (Weekday Schedule) or the YDSCH feature (Yearly Schedule) is supported. In simpler terms, the 'Restricted' status must be implemented if the device supports scheduling based on either weekdays or yearly schedules.

* In the Door Lock Cluster, under the Data Types section, the entry for 'InsufficientBattery' with a value of '4' represents a specific error condition where a lock or unlock operation fails due to insufficient battery power to safely actuate the lock. The conformance rule for this entry is 'O', indicating that the inclusion of this data type is optional. This means that while it is not required for compliance with the Matter specification, it can be implemented at the discretion of the manufacturer or developer without any dependencies or conditions.

5.2.6.15. OperatingModeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the lock operating mode.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the 'Value' of '0' and the 'Name' of 'Normal'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Normal' data type with a value of '0' is a required element in the Door Lock Cluster specification. It must be implemented in any device or application that conforms to this specification, without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Data Types section, the table row describes an element named 'Vacation' with a value of '1'. The conformance rule for this element is marked as 'O', which stands for Optional. This means that the 'Vacation' element is not required to be implemented in the Door Lock Cluster and has no dependencies or conditions that would necessitate its inclusion. Implementers have the discretion to include or exclude this element based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an element with the name "Privacy" and a value of "2." The conformance rule for this element is marked as "O," which stands for Optional. This means that the "Privacy" element is not required to be implemented in devices that support the Door Lock Cluster, and there are no dependencies or conditions that affect its optional status. Implementers have the discretion to include or exclude this element based on their specific needs or preferences without any mandatory obligation from the Matter specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '3' named 'NoRemoteLockUnlock'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'NoRemoteLockUnlock' feature is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter IoT specification. There are no conditions or exceptions; it is a fundamental requirement for compliance.

* In the context of the Door Lock Cluster's Data Types, the table row describes an element with the name "Passage" and a value of '4'. The conformance rule for this element is marked as 'O', which stands for Optional. This means that the "Passage" element is not required to be implemented in devices that support the Door Lock Cluster. There are no dependencies or conditions that affect its optional status, allowing manufacturers the flexibility to include or exclude this element based on their design preferences or product requirements.

The table below shows the operating mode and which interfaces are enabled, if supported, for each
mode.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row entry for 'Normal' indicates that this feature is associated with three capabilities: Keypad, Remote, and RFID, all marked with an asterisk and a 'Y', suggesting that these capabilities are relevant to the feature. However, the conformance rule for 'Normal' is not explicitly provided in the row data. If we assume that the conformance rule follows the typical patterns outlined in the guide, it would likely specify conditions under which 'Normal' is mandatory, optional, or otherwise. For instance, if 'Normal' were to be mandatory when any of the capabilities (Keypad, Remote, RFID) are supported, the conformance might be expressed as a logical OR condition involving these features. Without the specific conformance string, we can only infer that 'Normal' is a feature that interacts with these capabilities, and its requirement status would depend on the presence or absence of these features in a device's implementation.

* The table row entry pertains to the "Vacation" feature within the Door Lock Cluster's Data Types section. The conformance rule for this feature is not explicitly provided in the row data, but based on the context, we can infer that the "Vacation" feature is related to the control of the door lock system. The asterisks next to "Keypad," "Remote," and "RFID" suggest that these are specific conditions or capabilities relevant to the feature. Given that "Keypad" and "RFID" are marked with 'N' (No), and "Remote" is marked with 'Y' (Yes), it implies that the "Vacation" feature is only applicable or functional when controlled remotely, not via keypad or RFID. Without a specific conformance string, we cannot determine if the feature is mandatory, optional, or otherwise, but the context suggests that remote control is a key requirement for the "Vacation" feature's operation.

* The table row describes an element named "Privacy" within the Door Lock Cluster's Data Types section. The conformance rule for "Privacy" is not explicitly provided in the row data, but based on the context, it likely involves conditions related to the features "Keypad," "Remote," and "RFID," all marked with an asterisk and noted as 'N' (No). This suggests that the "Privacy" element is not directly tied to these features being supported. In the absence of a specific conformance string, we can infer that the "Privacy" element might be optional or have a more complex conformance condition described elsewhere in the documentation. The asterisks and 'N' indicators imply that the "Privacy" feature does not require the presence of Keypad, Remote, or RFID capabilities to be considered, aligning with a potential optional status or a described conformance condition.

* The table row entry for the 'NoRemoteLockUnlock' data type within the Door Lock Cluster's Data Types section indicates a specific feature related to the operation of door locks. The conformance rule for this entry is not explicitly provided in the data, but based on the context, it likely involves conditions related to the presence or absence of certain features. The 'Keypad*' is marked as 'Y', meaning the keypad feature is supported, while 'Remote*' is 'N', indicating the remote feature is not supported, and 'RFID*' is 'Y', showing RFID support. This suggests that the 'NoRemoteLockUnlock' feature is relevant in scenarios where remote operation is not available, but keypad and RFID functionalities are present. The conformance rule would dictate how this feature should be implemented based on these conditions, potentially making it mandatory or optional depending on the specific combination of supported features.

* The table row entry pertains to the "Passage" data type within the Door Lock Cluster's Data Types section. The conformance rule for "Passage" is not explicitly provided in the row data, which suggests that it may be described elsewhere in the documentation or is implicitly understood within the context of the specification. The "Passage" data type likely relates to a specific mode or feature of the door lock, such as allowing free passage without requiring authentication. The absence of specific conformance details, such as "Mandatory" or "Optional," indicates that the implementation of this data type might be subject to additional conditions or descriptions found in other parts of the Matter specification. The "Keypad," "Remote," and "RFID" fields marked as "N/A" suggest that these methods of interaction are not applicable or relevant to the "Passage" data type in this context.

*
Interface Operational: Yes, No or N/A
For modes that disable the remote interface, the door lock SHALL respond to Lock,
Unlock, Toggle, and Unlock with Timeout commands with a response status Failure
NOTE and not take the action requested by those commands. The door lock SHALL NOT
disable the radio or otherwise unbind or leave the network. It SHALL still respond
to all other commands and requests.
5.2.6.15.1. Normal Value
The lock operates normally. All interfaces are enabled.
5.2.6.15.2. Vacation Value
Only remote interaction is enabled. The keypad SHALL only be operable by the master user.
5.2.6.15.3. Privacy Value
This mode is only possible if the door is locked. Manual unlocking changes the mode to Normal
operating mode. All external interaction with the door lock is disabled. This mode is intended to be
used so that users, presumably inside the property, will have control over the entrance.
5.2.6.15.4. NoRemoteLockUnlock Value
This mode only disables remote interaction with the lock. This does not apply to any remote propri
etary means of communication. It specifically applies to the Lock, Unlock, Toggle, and Unlock with
Timeout Commands.
5.2.6.15.5. Passage Value
The lock is open or can be opened or closed at will without the use of a Keypad or other means of
user validation (e.g. a lock for a business during work hours).
5.2.6.16. OperationSourceEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate the source of the Lock/Unlock or user change operation per
formed.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table row describes a data entry with the value '0' and the name 'Unspecified'. This entry signifies that a lock or unlock operation originated from an unspecified source. The conformance rule for this entry is marked as 'O', which means it is optional. This indicates that the inclusion of this data entry is not required and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this entry based on their specific needs or preferences.

* In the Door Lock Cluster's Data Types section, the table row describes a feature with the 'Name' "Manual," which has a 'Value' of '1'. This feature indicates that a lock or unlock operation was initiated manually, such as through a key, thumbturn, or handle. The 'Conformance' for this feature is marked as 'O', meaning it is optional. This indicates that the implementation of this feature is not required and does not depend on any other conditions or features. Devices supporting the Door Lock Cluster may include this feature, but it is not mandatory for compliance with the Matter specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes a data type with the value '2' named 'ProprietaryRemote'. This data type indicates that a lock or unlock operation originated from a proprietary remote source, such as a vendor-specific application or cloud service. The conformance rule for this entry is 'O', which means that the 'ProprietaryRemote' data type is optional. It is not required for implementation and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this feature based on their specific needs or preferences.

* In the Door Lock Cluster, under the Data Types section, there is an entry with the value '3' named 'Keypad'. This entry indicates that a lock or unlock operation originated from a keypad. According to its conformance rule, which is marked as 'O', this feature is optional. This means that the implementation of this feature is not required and there are no dependencies or conditions that mandate its inclusion. Devices supporting the Door Lock Cluster can choose to implement this feature, but they are not obligated to do so.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '4' and the name 'Auto'. This entry summarizes a scenario where the lock or unlock operation is initiated automatically by the lock itself, such as through a relock timer. The conformance rule for this entry is 'O', which means that this feature is optional. It is not required for implementation and does not have any dependencies or conditions that must be met for it to be included in a device's functionality. Therefore, manufacturers can choose to implement this feature at their discretion.

* In the Door Lock Cluster's Data Types section, the table row describes a data type with the value '5', named 'Button'. This data type indicates that a lock or unlock operation was initiated via a lock button, such as a one-touch or physical button. The conformance rule for this entry is 'O', which means that the inclusion of this data type is optional. It is not required for compliance with the Matter specification and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this feature based on their specific product needs or design preferences.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type named "Schedule" with a value of '6'. This data type indicates that a lock or unlock operation was initiated by the lock itself due to a pre-set schedule. The conformance rule 'HDSCH' suggests that the inclusion of this data type is conditional based on the support of a specific feature or condition denoted by 'HDSCH'. If the feature 'HDSCH' is supported, then this data type is mandatory. The conformance expression does not provide further details on alternative conditions or options, implying that the presence of 'HDSCH' is the sole determinant for this data type's requirement.

* In the Door Lock Cluster's Data Types section, the table row describes a data type with the value '7', named 'Remote'. This data type indicates that a lock or unlock operation originated from a remote node. The conformance rule for this entry is 'M', which means that this element is mandatory. Therefore, any implementation of the Door Lock Cluster must include this data type to comply with the Matter specification. This ensures that the system can recognize and process lock or unlock commands that are initiated from a remote source.

* The table row describes an entry within the Door Lock Cluster's Data Types section, specifically focusing on a value labeled 'RFID' with a numerical identifier of '8'. This entry indicates that the lock or unlock operation originated from an RFID card. The conformance rule for this entry is 'RID', which, according to the Matter Conformance Interpretation Guide, suggests that the element is described elsewhere in the documentation due to its complexity. This means that the specific requirements or conditions under which the RFID feature is applicable or necessary are detailed in another part of the documentation, rather than being straightforwardly mandatory, optional, or otherwise.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the entry describes a value labeled 'Biometric' with a value of '9'. This indicates that the lock or unlock operation originated from a biometric source, such as facial recognition or fingerprint/fingervein scanning. The conformance rule '[USR]' signifies that the inclusion of this 'Biometric' value is optional, contingent upon the support of the 'USR' feature. If the 'USR' feature is supported, then the 'Biometric' value can be included; otherwise, it is not required.

* In the Door Lock Cluster's Data Types section, the entry with the value '10' is named 'Aliro'. It summarizes that the lock/unlock operation originated from an interaction defined in the Aliro system, or a user change operation involved step-up credential provisioning as specified by Aliro. The conformance rule 'ALIRO' indicates that this element is mandatory if the feature 'ALIRO' is supported. This means that if the Aliro feature is part of the system, the 'Aliro' data type must be implemented.

5.2.6.17. UserStatusEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate what the status is for a specific user ID.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the table entry describes a data type with the value '0' and the name 'Available', which indicates that the user ID is available. The summary provides a brief explanation of this data type's purpose. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Available' data type is always required to be implemented in any device or system that supports the Door Lock Cluster, with no exceptions or conditions.

* The table row entry pertains to the "OccupiedEnabled" data type within the Door Lock Cluster's Data Types section. This entry indicates that the "OccupiedEnabled" attribute signifies that a user ID is both occupied and enabled. The conformance rule for this attribute is marked as "M," which stands for Mandatory. This means that the "OccupiedEnabled" attribute is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Data Types section, the entry with the value '3' is named 'OccupiedDisabled'. This entry indicates that the user ID is both occupied and disabled. The conformance rule for this entry is 'O', which means it is optional. This implies that the 'OccupiedDisabled' data type is not required to be implemented and has no dependencies on other features or conditions. Implementers of the Door Lock Cluster can choose to include this data type, but it is not mandatory for compliance with the Matter specification.

5.2.6.18. UserTypeEnum Type
This data type is derived from enum8.
This enumeration SHALL indicate what the type is for a specific user ID.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '0' named 'UnrestrictedUser'. This data type signifies that the user ID type is unrestricted, meaning there are no limitations on the user ID's use or access. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This indicates that the 'UnrestrictedUser' data type is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an entry within the Door Lock Cluster, specifically under the Data Types section. The entry is named "YearDayScheduleUser" and has a value of '1'. It represents a user ID type that is associated with a schedule, as indicated by the summary "The user ID type is schedule." The conformance rule for this entry is 'O', which means that the "YearDayScheduleUser" is an optional element. This indicates that while it is not required for implementation, it can be included at the discretion of the developer or manufacturer without any dependencies or conditions.

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '2', named 'WeekDayScheduleUser', which indicates that the user ID type is associated with a schedule. The conformance rule for this entry is 'O', meaning it is optional. This implies that the 'WeekDayScheduleUser' element is not required to be implemented in devices supporting the Door Lock Cluster, and there are no dependencies or conditions that mandate its inclusion. Implementers have the discretion to include this feature based on their specific use case or product design.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '3' named 'ProgrammingUser', which signifies a user ID type related to programming. The conformance rule for this entry is 'O', indicating that the 'ProgrammingUser' data type is optional. This means that while the data type can be implemented within the Door Lock Cluster, it is not required and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this data type based on their specific needs or preferences without affecting the compliance with the Matter specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '4', named 'NonAccessUser', which signifies a user ID type that does not have access. The conformance rule for this entry is 'O', indicating that the 'NonAccessUser' element is optional. This means that while it is available for implementation, it is not required and does not depend on any other features or conditions to be included in a device's implementation of the Door Lock Cluster.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '5', named 'ForcedUser', which indicates a user ID type that is forced. The conformance rule '[USR]' specifies that the inclusion of this element is optional and depends on the support of the 'USR' feature. This means that if the 'USR' feature is supported, the 'ForcedUser' element can be included, but it is not mandatory. If the 'USR' feature is not supported, the 'ForcedUser' element does not need to be included.

* In the Door Lock Cluster's Data Types section, the entry describes a data type with the value '6' named 'DisposableUser', which signifies a user ID type that is disposable. The conformance rule '[USR]' indicates that this element is optional if the condition 'USR' is true. This means that if the feature or condition represented by 'USR' is supported, the 'DisposableUser' data type can be included, but it is not mandatory. If 'USR' is not supported, the inclusion of this data type is not applicable.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '7' and the name 'ExpiringUser', which indicates that the user ID type is expiring. The conformance rule '[USR]' specifies that this element is optional if the feature 'USR' is supported. This means that if the 'USR' feature is present in the implementation, the 'ExpiringUser' data type can be included, but it is not mandatory. If 'USR' is not supported, the 'ExpiringUser' data type is not applicable.

* In the context of the Door Lock Cluster's Data Types, the entry for 'ScheduleRestrictedUser' with a value of '8' indicates a user ID type that is restricted by a schedule. The conformance rule 'WDSCH | YDSCH' specifies that this element is mandatory if either the 'WDSCH' feature or the 'YDSCH' feature is supported. In simpler terms, the 'ScheduleRestrictedUser' type must be implemented if the device supports either of these scheduling features, ensuring that the user ID can be restricted based on a schedule when these features are available.

* The table row describes a data type within the Door Lock Cluster, specifically for a user ID type named "RemoteOnlyUser," which has a value of '9'. This type indicates that the user ID is designated for remote-only access. The conformance rule 'USR & COTA & PIN' means that the "RemoteOnlyUser" data type is mandatory if the device supports all three features: USR (User Management), COTA (Configuration Over-The-Air), and PIN (Personal Identification Number). In other words, this data type must be implemented if the device includes these specific capabilities, ensuring that remote-only user IDs are supported under these conditions.

5.2.6.18.1. UnrestrictedUser Value
This value SHALL indicate the user has access 24/7 provided proper PIN or RFID is supplied (e.g.,
owner).
5.2.6.18.2. YearDayScheduleUser Value
This value SHALL indicate the user has the ability to open lock within a specific time period (e.g.,
guest).
When UserType is set to YearDayScheduleUser, user access SHALL be restricted as follows:
• If no YearDaySchedules are set for the user, then access SHALL be denied
• If one or more YearDaySchedules are set, user access SHALL be granted if and only if the cur
rent time falls within at least one of the YearDaySchedules. If current time is not known, user
access SHALL NOT be granted.
5.2.6.18.3. WeekDayScheduleUser Value
This value SHALL indicate the user has the ability to open lock based on specific time period within
a reoccurring weekly schedule (e.g., cleaning worker).
When UserType is set to WeekDayScheduleUser, user access SHALL be restricted as follows:
• If no WeekDaySchedules are set for the user, then access SHALL be denied
• If one or more WeekDaySchedules are set, user access SHALL be granted if and only if the cur
rent time falls within at least one of the WeekDaySchedules. If current time is not known, user
access SHALL NOT be granted.
5.2.6.18.4. ProgrammingUser Value
This value SHALL indicate the user has the ability to both program and operate the door lock. This
user can manage the users and user schedules. In all other respects this user matches the unre
stricted (default) user. ProgrammingUser is the only user that can disable the user interface (key
pad, remote, etc…).
5.2.6.18.5. NonAccessUser Value
This value SHALL indicate the user is recognized by the lock but does not have the ability to open
the lock. This user will only cause the lock to generate the appropriate event notification to any
bound devices.
5.2.6.18.6. ForcedUser Value
This value SHALL indicate the user has the ability to open lock but a ForcedUser LockOpera
tionType and ForcedUser silent alarm will be emitted to allow a notified Node to alert emergency
services or contacts on the user account when used.
5.2.6.18.7. DisposableUser Value
This value SHALL indicate the user has the ability to open lock once after which the lock SHALL
change the corresponding user record UserStatus value to OccupiedDisabled automatically.
5.2.6.18.8. ExpiringUser Value
This value SHALL indicate the user has the ability to open lock for ExpiringUserTimeout attribute
minutes after the first use of the PIN code, RFID code, Fingerprint, or other credential. After
ExpiringUserTimeout minutes the corresponding user record UserStatus value SHALL be set to
OccupiedDisabled automatically by the lock. The lock SHALL persist the timeout across reboots
such that the ExpiringUserTimeout is honored.
5.2.6.18.9. ScheduleRestrictedUser Value
This value SHALL indicate the user access is restricted by Week Day and/or Year Day schedule.
When UserType is set to ScheduleRestrictedUser, user access SHALL be restricted as follows:
• If no WeekDaySchedules and no YearDaySchedules are set for the user, then access SHALL be
denied
• If one or more WeekDaySchedules are set, but no YearDaySchedules are set for the user, then
user access SHALL be equivalent to the WeekDayScheduleUser UserType
• If one or more YearDaySchedules are set, but no WeekDaySchedules are set for the user, then
user access SHALL be equivalent to the YearDayScheduleUser UserType
• If one or WeekDaySchedules are set AND one or more YearDaySchedules are set, then user
access SHALL be granted if and only if the current time falls within at least one of the Week
DaySchedules AND the current time falls within at least one of the YearDaySchedules.
5.2.6.18.10. RemoteOnlyUser Value
This value SHALL indicate the user access and PIN code is restricted to remote lock/unlock com
mands only. This type of user might be useful for regular delivery services or voice assistant
unlocking operations to prevent a PIN code credential created for them from being used at the key
pad. The PIN code credential would only be provided over-the-air for the lock/unlock commands.
5.2.6.19. LockStateEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Door Lock Cluster, under the Data Types section, the entry for 'NotFullyLocked' with a value of '0' indicates a lock state where the door is not fully locked. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'NotFullyLocked' state is a required element in the specification and must be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential part of the lock state definitions.

* In the Door Lock Cluster, under the Data Types section, the table row describes a data type with the value '1', named 'Locked', which indicates that the lock state is fully locked. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that the 'Locked' state must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions; the 'Locked' state is a required feature.

* In the context of the Door Lock Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '2' and the 'Name' of 'Unlocked'. This entry indicates that the lock state is fully unlocked, as summarized in the 'Summary' field. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'Unlocked' state is a required element in the Door Lock Cluster specification and must always be implemented in any device or system that adheres to this specification. There are no conditions or dependencies that alter this requirement; it is an essential part of the standard.

* In the Door Lock Cluster, under the Data Types section, the entry with the value '3' is named 'Unlatched'. This entry indicates that the lock state is fully unlocked and the latch is pulled. According to the conformance rule 'O', this element is optional, meaning it is not required for implementation and has no dependencies. Devices implementing the Door Lock Cluster can choose to support this 'Unlatched' state, but they are not obligated to do so according to the Matter specification.

5.2.6.20. LockTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes a data entry with the value '0', named 'DeadBolt', which signifies that the physical lock type is a dead bolt. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that any implementation of the Door Lock Cluster must include support for the 'DeadBolt' data type, as it is a required component of the specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes a data entry with the value '1', named 'Magnetic', which indicates that the physical lock type is magnetic. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that any implementation of the Door Lock Cluster must include support for the 'Magnetic' lock type, as it is a required feature according to the Matter specification.

* In the Door Lock Cluster, within the Data Types section, there is an entry with the value '2' named 'Other', which summarizes that the physical lock type is categorized as 'other'. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that the 'Other' lock type must always be supported and implemented in any device or system utilizing the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '3', named 'Mortise', which indicates that the physical lock type is a mortise lock. The conformance rule for this entry is 'M', meaning that this element is mandatory. This implies that any implementation of the Door Lock Cluster must include support for the 'Mortise' lock type, as it is a required component of the specification without any conditions or exceptions.

* In the Door Lock Cluster's Data Types section, the table row describes a data entry with the value '4', named 'Rim', which indicates that the physical lock type is a rim lock. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Rim' lock type is a required element in the specification and must be supported by any implementation of the Door Lock Cluster. There are no conditions or dependencies affecting this requirement; it is an absolute necessity for compliance with the Matter specification in this context.

* In the Door Lock Cluster, under the Data Types section, the table entry describes a data type with the name "LatchBolt," which has a value of '5' and represents a physical lock type that is a latch bolt. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the "LatchBolt" data type is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row entry pertains to the Door Lock Cluster within the Data Types section, specifically describing a data type with the value '6' named 'CylindricalLock'. This entry indicates that the physical lock type is a cylindrical lock. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'CylindricalLock' data type is always required to be supported in any implementation of the Door Lock Cluster according to the Matter IoT specification. There are no conditions or dependencies affecting this requirement; it is an essential element that must be included.

* In the Door Lock Cluster, under the Data Types section, the entry for 'TubularLock' with a value of '7' indicates that the physical lock type is a tubular lock. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the feature or element described by this entry is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter specification. There are no conditions or dependencies that alter this requirement; it is a fundamental part of the specification for this context.

* In the Door Lock Cluster, under the Data Types section, the entry for 'InterconnectedLock' with a value of '8' indicates that this data type represents a physical lock type that is an interconnected lock. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'InterconnectedLock' data type is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter specification. There are no conditions or exceptions to this requirement, making it an essential element for compliance.

* In the context of the Door Lock Cluster's Data Types, the table entry describes a data type with the value '9', named 'DeadLatch', which indicates that the physical lock type is a dead latch. The conformance rule for this entry is 'M', meaning that the 'DeadLatch' data type is mandatory. This implies that any implementation of the Door Lock Cluster must include support for the 'DeadLatch' type, as it is a required element within the specification.

* In the context of the Door Lock Cluster's Data Types, the table row describes an element with the value '10' named 'DoorFurniture', which indicates a physical lock type categorized as door furniture. The conformance rule for this element is 'M', meaning it is mandatory. This signifies that the 'DoorFurniture' element is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row entry describes a data type with the 'Value' of '11', named 'Eurocylinder', which indicates that the physical lock type is a euro cylinder. The 'Conformance' field is marked as 'M', meaning that this element is mandatory. This implies that within the Matter specification, the inclusion of the 'Eurocylinder' data type is always required for implementations that support the Door Lock Cluster. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the specification.

5.2.6.21. LEDSettingEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the Door Lock Cluster, specifically named "NoLEDSignal," which has a value of '0' and a summary indicating that it signifies "Never use LED for signalization." The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "NoLEDSignal" data type is a required element in the Door Lock Cluster and must always be implemented according to the Matter specification, without any conditions or exceptions.

* The table row pertains to the "NoLEDSignalAccessAllowed" data type within the Door Lock Cluster's Data Types section. This entry indicates that the feature involves using LED signalization except for access allowed events. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "NoLEDSignalAccessAllowed" feature is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row entry pertains to the "LEDSignalAll" data type within the Door Lock Cluster's Data Types section. This entry indicates that the "LEDSignalAll" feature is used for LED signalization for all events related to the door lock. The conformance rule for this feature is marked as "M," which stands for Mandatory. This means that the "LEDSignalAll" feature is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.6.22. SoundVolumeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the 'Value' of '0', named 'Silent', which represents the 'Silent Mode'. The 'Conformance' field is marked as 'M', indicating that this element is mandatory. This means that the Silent Mode feature must always be implemented and supported in any device or system that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or dependencies affecting this requirement; it is an absolute necessity for compliance.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the 'Value' of '1', named 'Low', which summarizes as 'Low Volume'. The 'Conformance' for this entry is marked as 'M', indicating that this element is Mandatory. This means that the 'Low Volume' data type must always be included and supported in any implementation of the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Data Types section, the table row describes an entry with the value '2', named 'High', which summarizes as 'High Volume'. The conformance rule for this entry is marked as 'M', indicating that it is mandatory. This means that the 'High' volume setting is a required element for any implementation of the Door Lock Cluster according to the Matter specification. It must be included and supported without exception, ensuring that the feature is consistently available across all compliant devices.

* In the context of the Door Lock Cluster's Data Types, the table row describes an entry with the value '3', named 'Medium', which has a summary of 'Medium Volume'. The conformance rule for this entry is 'M', indicating that it is a Mandatory element. This means that the 'Medium' volume setting must always be included and supported in any implementation of the Door Lock Cluster according to the Matter specification. There are no conditions or dependencies affecting its requirement; it is an essential part of the specification.

5.2.6.23. EventTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Door Lock Cluster's Data Types section, specifically focusing on an element named "Operation" with a value of '0'. This element is summarized as representing an event type related to operations. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the "Operation" element is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster's Data Types section, the table row describes an entry with the value '1', named 'Programming', which signifies an event type related to programming. The conformance rule for this entry is 'M', meaning it is mandatory. This indicates that the 'Programming' event type must always be implemented and supported within the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster's Data Types, the table row describes an element with the name "Alarm" and a value of "2," which signifies an event type categorized as an alarm. The conformance rule for this element is marked as "M," indicating that it is mandatory. This means that the "Alarm" event type must always be implemented and supported in any device or application that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions; the inclusion of this element is required without any dependencies or optionality.

5.2.6.24. CredentialStruct Type
This struct SHALL indicate the credential types and their corresponding indices (if any) for the
event or user record.

_Table parsed from section 'Data Types':_

* The table row describes an element within the Door Lock Cluster, specifically under the Data Types section. The element is identified by the ID '0' and is named 'CredentialType'. It is of the type 'CredentialTypeEnum' and has a constraint labeled as 'all', indicating that it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'CredentialType' element is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an element within the Door Lock Cluster, specifically a data type named "CredentialIndex." This element is identified by the ID '1' and is of the type 'uint16', meaning it is a 16-bit unsigned integer. The constraint 'all' suggests that this data type is applicable universally within its context. The default value for "CredentialIndex" is '0'. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Door Lock Cluster. There are no conditions or dependencies affecting its mandatory status.

5.2.6.24.1. CredentialType Field
This field SHALL indicate the credential field used to authorize the lock operation.
5.2.6.24.2. CredentialIndex Field
This field SHALL indicate the index of the specific credential used to authorize the lock operation in
the list of credentials identified by CredentialType (e.g. PIN, RFID, etc.). This field SHALL be set to 0
if CredentialType is ProgrammingPIN or does not correspond to a list that can be indexed into.

## Status Codes
5.2.7.1. StatusCodeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Status Codes':_

* In the Door Lock Cluster, under the Status Codes section, the entry with the value '0x02' is named 'DUPLICATE'. This status code indicates that an operation would result in a duplicate credential or ID, which is not permissible. The conformance rule for this entry is 'M', meaning that the 'DUPLICATE' status code is mandatory. This implies that any implementation of the Door Lock Cluster must include this status code, ensuring that systems can consistently handle scenarios where a duplicate credential or ID might be created.

* In the Door Lock Cluster, under the Status Codes section, the entry with the value '0x03' is named 'OCCUPIED' and is summarized as indicating that an entry would replace an occupied slot. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'OCCUPIED' status code is a required element in the implementation of the Door Lock Cluster, and it must always be supported without any conditions or exceptions.

5.2.7.2. DUPLICATE Code
The provided User ID, PIN or RFID code or other credential is a duplicate of an existing entry.
5.2.7.3. OCCUPIED Code
The provided User ID, Credential ID, or entry location is already occupied. The entry might need to
be deleted or a different ID or location chosen.

## PIN/RFID Code Format
The PIN/RFID codes defined in this specification are all octet strings.
All value in the PIN/RFID code SHALL be ASCII encoded regardless if the PIN/RFID codes are num
ber or characters. For example, code of “1, 2, 3, 4” SHALL be represented as 0x31, 0x32, 0x33, 0x34.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Door Lock Cluster, specifically the 'LockState' attribute. This attribute has an ID of '0x0000' and is of the type 'LockStateEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is noted as 'X P', suggesting that while the attribute is currently provisional, it is disallowed in some contexts. The 'Access' is 'R V', meaning it is readable and has volatile access characteristics. The 'Conformance' is marked as 'M', which means that the 'LockState' attribute is mandatory and must always be implemented in any device that supports the Door Lock Cluster.

* The table row describes an attribute within the Door Lock Cluster, specifically the "LockType" attribute. This attribute is identified by the ID '0x0001' and is of the type 'LockTypeEnum'. The constraint for this attribute is described elsewhere in the documentation, as indicated by 'desc'. It has an access level of 'R V', meaning it is readable and possibly has additional access constraints or visibility rules. The conformance rule 'M' signifies that the "LockType" attribute is mandatory, meaning it must always be implemented in any device that supports the Door Lock Cluster.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'ActuatorEnabled' attribute. This attribute has an ID of '0x0002' and is of type 'bool', meaning it represents a boolean value (true or false). The 'Constraint' field indicates that this attribute applies universally ('all'), and the 'Access' field 'R V' suggests that it can be read and is volatile. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'ActuatorEnabled' attribute is always required to be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'DoorState' attribute, identified by the ID '0x0003'. This attribute is of the type 'DoorStateEnum', and its constraints are described elsewhere in the documentation. The 'Quality' field indicates that the attribute is both disallowed ('X') and provisional ('P'), suggesting it is currently not allowed but may be reconsidered in the future. The 'Access' field specifies that the attribute is readable ('R') and volatile ('V'). The 'Conformance' field is marked as 'DPS', which implies a complex conformance status that is not straightforwardly expressed by the basic tags or logical conditions. This suggests that the attribute's conformance is described in detail elsewhere in the documentation, potentially involving a combination of deprecated, provisional, and other specific conditions.

* The table row describes an attribute within the Door Lock Cluster, specifically the "DoorOpen Events" attribute, which is identified by the ID `0x0004` and is of type `uint32`. This attribute is constrained to apply to all instances and has read-write access with a viewable and manageable (VM) access level. The conformance rule `[DPS]` indicates that the "DoorOpen Events" attribute is optional if the condition `DPS` is true. In other words, the attribute is not required unless the specific feature or condition represented by `DPS` is supported or applicable. If `DPS` is not supported, the attribute remains optional and is not mandatory.

* The table row describes an attribute named "DoorClosedEvents" within the Door Lock Cluster, identified by the ID '0x0005'. This attribute is of type 'uint32', indicating it stores a 32-bit unsigned integer, and it is constrained to 'all', meaning it applies universally within its context. The access level 'RW VM' suggests that the attribute can be read and written, and it is subject to verification and monitoring. The conformance rule '[DPS]' indicates that the "DoorClosedEvents" attribute is optional if the feature or condition 'DPS' is supported. If 'DPS' is not supported, the attribute is not required, and there are no further conditions or mandatory requirements specified.

* The table row describes an attribute named "OpenPeriod" within the Door Lock Cluster's attributes section. This attribute has an ID of '0x0006' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that there are no specific constraints limiting its use. The 'Access' is 'RW VM', which means the attribute can be read and written, and it is accessible to verified managers. The 'Conformance' field is '[DPS]', which indicates that the "OpenPeriod" attribute is optional if the condition 'DPS' is true. This means that if the feature or condition represented by 'DPS' is supported, the attribute is not required but can be included if desired.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfTotalUsersSupported" attribute. This attribute has an ID of '0x0011' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that this attribute applies universally within its context. The 'Quality' is 'F', and it has a default value of '0'. The 'Access' is 'R V', which means it is readable and can be viewed. The 'Conformance' field is 'USR', which implies that this attribute is mandatory if the feature 'USR' (likely representing a user-related feature) is supported. If 'USR' is not supported, the conformance of this attribute is not specified in this entry, suggesting it may not be required.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfPINUsersSupported" attribute, which has an ID of '0x0012' and is of type 'uint16'. This attribute indicates the number of PIN users that the door lock can support. It is constrained to apply to all instances of the cluster, with a default value of '0'. The attribute has read and view access, as indicated by 'R V'. The conformance rule 'PIN' means that this attribute is mandatory if the feature related to PIN support is implemented in the device. If the device supports PIN functionality, then it must include this attribute to specify how many PIN users can be accommodated.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfRFIDUsersSupported" attribute. This attribute has an ID of '0x0013' and is of type 'uint16', indicating it is a 16-bit unsigned integer. The 'Constraint' is 'all', meaning it applies universally within its context. The 'Quality' is 'F', which might refer to a specific quality or feature characteristic defined elsewhere in the specification. The default value for this attribute is '0', and it has 'R V' access, meaning it can be read and possibly verified. The 'Conformance' field is 'RID', which, according to the Matter Conformance Interpretation Guide, indicates that this attribute is deprecated ('D'). This means that while it is still present in the current specification, it is considered obsolete and may be removed in future versions.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfWeekDaySchedulesSupportedPerUser" attribute. This attribute has an ID of '0x0014' and is of type 'uint8', with a constraint that its maximum value can be '0xFD'. The quality is marked as 'F', indicating a specific quality requirement, and it has a default value of '0'. The access level is 'R V', meaning it is readable and has a volatile nature. The conformance rule 'WDSCH' indicates that this attribute is mandatory if the feature 'WDSCH' (Week Day Schedule) is supported by the device. If the device does not support the 'WDSCH' feature, the attribute is not required. This conformance rule ensures that the attribute is only implemented when relevant to the device's capabilities.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfYearDaySchedulesSupportedPerUser" attribute. This attribute has an ID of '0x0015' and is of type 'uint8', with a maximum constraint value of '0xFD'. It is a feature-related attribute, indicated by the quality 'F', and has a default value of '0'. The access level is 'R V', meaning it is readable and can be viewed. The conformance rule 'YDSCH' suggests that the attribute is mandatory if the feature 'YDSCH' (likely a feature code related to Year Day Schedules) is supported. If 'YDSCH' is not supported, the attribute is not required. This means that the attribute's presence is conditional upon the support of the Year Day Schedules feature within the device's implementation.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfHolidaySchedulesSupported" attribute. This attribute has an ID of '0x0016' and is of type 'uint8', with a constraint that its maximum value can be '0xFD'. The quality is marked as 'F', and it has a default value of '0'. The access level for this attribute is 'R V', meaning it is readable and has volatile access. The conformance rule 'HDSCH' indicates that this attribute is mandatory if the feature or condition represented by 'HDSCH' is supported. If 'HDSCH' is not supported, the attribute is not required. This conformance rule implies that the attribute's necessity is contingent upon the presence of a specific feature or condition within the device's implementation.

* The table row describes an attribute within the Door Lock Cluster, specifically the "MaxPINCodeLength" attribute, which is identified by the ID '0x0017'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally ('Constraint': 'all'). The attribute is marked with a 'Quality' of 'F', indicating a specific quality characteristic, and has a default value of 'MS'. It has 'Access' permissions of 'R V', meaning it can be read and is volatile. The 'Conformance' field is specified as 'PIN', which implies that the attribute is mandatory if the feature or condition represented by 'PIN' is supported. In this context, if the Door Lock Cluster supports the 'PIN' feature, the 'MaxPINCodeLength' attribute must be implemented.

* The table row describes an attribute within the Door Lock Cluster, specifically the "MinPINCodeLength" attribute, identified by the ID '0x0018'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies to all instances of the cluster as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'F', and the default value is 'MS'. The access level is 'R V', which means it is readable and can be viewed. The conformance rule for this attribute is 'PIN', which implies that the attribute is mandatory if the feature or condition represented by 'PIN' is supported. If the 'PIN' feature is not supported, the attribute is not required. This rule ensures that the attribute is only included when relevant to the device's functionality.

* The table row describes an attribute within the Door Lock Cluster, specifically the "MaxRFIDCodeLength" attribute. This attribute has an ID of '0x0019' and is of type 'uint8', indicating it holds an 8-bit unsigned integer value. The 'Constraint' is 'all', meaning it applies universally within the context. The 'Quality' is marked as 'F', and the 'Default' value is 'MS'. The 'Access' is 'R V', which suggests that the attribute is readable and possibly volatile. The 'Conformance' is specified as 'RID', which according to the Matter Conformance Interpretation Guide, indicates that the attribute is deprecated ('D'). This means that the "MaxRFIDCodeLength" attribute is considered obsolete in the current specification and is not recommended for use in new implementations.

* The table row describes an attribute within the Door Lock Cluster, specifically the "MinRFIDCodeLength" attribute, identified by the ID '0x001A'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally ('Constraint': 'all'). The 'Quality' is marked as 'F', and it has a default value of 'MS'. The 'Access' is specified as 'R V', indicating it is readable and possibly volatile. The 'Conformance' field is 'RID', which, according to the Matter Conformance Interpretation Guide, means this attribute is currently deprecated ('D'). This implies that while it exists in the current specification, it is considered obsolete and may be removed in future versions.

* The table row describes an attribute within the Door Lock Cluster, specifically the "CredentialRulesSupport" attribute. This attribute is identified by the ID '0x001B' and is of the type 'CredentialRulesBitmap'. It has a constraint labeled as 'all', a quality of 'F', a default value of '1', and access permissions of 'R V', indicating it is readable and viewable. The conformance rule 'USR' is not directly explained by the provided conformance guide, suggesting it might be a specific feature code or condition unique to the Door Lock Cluster context. In general, the conformance rule would dictate when this attribute is required, optional, or otherwise, based on the presence or absence of certain features or conditions. However, without further context on what 'USR' specifically represents, it is unclear whether this attribute is mandatory, optional, or subject to other conditions.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfCredentialsSupportedPerUser" attribute, identified by the ID '0x001C'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally ('Constraint': 'all'). The attribute has a default value of '0' and is accessible for reading and viewing ('Access': 'R V'). The conformance rule 'USR' indicates that this attribute is mandatory if the feature or condition represented by 'USR' is supported. If 'USR' is not supported, the attribute is not required. This means that the presence of this attribute is contingent upon the support of the 'USR' feature within the device's implementation.

* The table row describes an attribute within the Door Lock Cluster, specifically the "Language" attribute, which is identified by the ID '0x0021'. This attribute is of type 'string' with a maximum constraint of 3 characters, and it has a default value of 'MS'. The quality of this attribute is provisional ('P'), indicating that its status may change in future specifications. The access level is 'R[W] VM', meaning it is readable and optionally writable, with the 'VM' indicating it is accessible via a specific method or context. The conformance rule for this attribute is 'O', which means it is optional and not required to be implemented, with no dependencies on other features or conditions.

* The table row describes an attribute named "LEDSettings" within the Door Lock Cluster's Attributes section. This attribute has an ID of '0x0022' and is of the type 'LEDSettingEnum', with a constraint of 'all', indicating it applies universally within its context. The quality is marked as 'P', suggesting that its status is provisional, and it has a default value of '0'. The access level is 'R[W] VM', meaning it is readable and optionally writable, with VM indicating it is accessible by the View and Manage roles. The conformance rule for "LEDSettings" is 'O', which means this attribute is optional and not required to be implemented, with no dependencies or conditions affecting its optional status.

* The table row describes an attribute within the Door Lock Cluster, specifically the "AutoRelockTime" attribute, which has an ID of '0x0023' and is of type 'uint32'. This attribute is constrained to be applicable in all contexts ('Constraint': 'all') and is provisionally marked ('Quality': 'P'), indicating its status might change in the future. The default value is 'MS', and it has read and optional write access ('Access': 'R[W] VM'). The conformance rule 'O' signifies that the "AutoRelockTime" attribute is optional, meaning it is not required to be implemented and has no dependencies on other features or conditions.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'SoundVolume' attribute, identified by the ID '0x0024'. This attribute is of the type 'SoundVolumeEnum' and is constrained to apply universally ('all'). It has a provisional quality status, indicating that its current status is temporary and may change in the future. The default value for this attribute is '0', and it has read and write access, with the access being restricted to verified members ('R[W] VM'). The conformance rule for 'SoundVolume' is marked as 'O', meaning that this attribute is optional and does not have any dependencies or conditions that would make it mandatory. In summary, the 'SoundVolume' attribute is an optional feature in the Door Lock Cluster, allowing for the adjustment of sound volume settings, but its implementation is not required by the Matter specification.

* The table row describes an attribute within the Door Lock Cluster, specifically the "OperatingMode" attribute, which is identified by the ID '0x0025' and is of the type 'OperatingModeEnum'. The attribute has a constraint described elsewhere in the documentation, and its quality is provisional, indicating that its status may change in the future. The default value for this attribute is '0', and it has read and optional write access, as indicated by 'R[W] VM'. The conformance rule for this attribute is 'M', meaning it is mandatory and must always be implemented in any device supporting the Door Lock Cluster, without any conditional dependencies or exceptions.

* The table row describes an attribute within the Door Lock Cluster, specifically the "SupportedOperatingModes" attribute. This attribute has an ID of '0x0026' and is of the type 'OperatingModesBitmap', which suggests it is a bitmap representing various operating modes that the door lock can support. The 'Constraint' is listed as 'all', indicating that all possible values within the bitmap are valid. The 'Quality' is marked as 'F', which typically denotes a specific quality or feature level, though the exact meaning would depend on the broader context of the specification. The default value for this attribute is '0xFFF6', and it has 'R V' access, meaning it can be read and possibly verified. The conformance rule 'M' indicates that this attribute is mandatory, meaning it must always be implemented in any device that supports the Door Lock Cluster. This ensures that all compliant devices will have this attribute available, providing a consistent feature set across different implementations.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Door Lock Cluster, specifically the "DefaultConfigurationRegister" attribute. This attribute has an ID of '0x0027' and is of the type 'ConfigurationRegisterBitmap'. It is constrained to apply to 'all' instances, has a quality status of 'Provisional', and a default value of '0'. The access level is 'R V', indicating it is readable and can be viewed. The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the inclusion of the "DefaultConfigurationRegister" attribute is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Door Lock Cluster, specifically the "EnableLocalProgramming" attribute. This attribute has an ID of '0x0028' and is of type 'bool', meaning it can hold a true or false value. The constraint 'all' indicates that this attribute applies universally within its context. It has a quality status of 'P', suggesting that its current status is provisional and may change in future specifications. The default value for this attribute is '1', indicating that local programming is enabled by default. The access level 'R[W] VA' means it is readable and optionally writable, with additional access control considerations. The conformance rule 'O' signifies that the "EnableLocalProgramming" attribute is optional, meaning it is not required and has no dependencies within the current specification.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'EnableOneTouchLocking' attribute. This attribute is identified by the ID '0x0029' and is of type 'bool', meaning it can hold a boolean value (true or false). The attribute applies to all instances of the cluster ('Constraint': 'all') and is of provisional quality ('Quality': 'P'), suggesting its status may change in future specifications. The default value for this attribute is '0', indicating it is initially set to false. The access level is 'RW VM', meaning it can be read and written by the device manufacturer. The conformance rule 'O' indicates that this attribute is optional, meaning it is not required and has no dependencies. Therefore, manufacturers can choose whether to implement this attribute in their devices.

* The table row describes an attribute named "EnableInsideStatusLED" within the Door Lock Cluster's Attributes section. This attribute has an ID of '0x002A' and is of type 'bool', meaning it can hold a boolean value (true or false). The 'Constraint' is set to 'all', indicating that it applies universally within its context. The 'Quality' is marked as 'P', suggesting that its status is provisional and may change in the future. The default value for this attribute is '0', and it has 'RW VM' access, meaning it can be read and written, and is visible to management applications. The 'Conformance' is marked as 'O', indicating that the "EnableInsideStatusLED" attribute is optional, meaning it is not required and has no dependencies within the current specification.

* The table row describes an attribute within the Door Lock Cluster, specifically the "EnablePrivacyModeButton" attribute. This attribute has an ID of '0x002B' and is of type 'bool', meaning it can hold a true or false value. The 'Constraint' is 'all', indicating it applies universally within the context. The 'Quality' is 'P', suggesting it is provisional, and its default value is '0', meaning the privacy mode button is initially disabled. The 'Access' is 'RW VM', which means it is readable and writable, with the VM indicating it may have specific access restrictions or conditions. The 'Conformance' is marked as 'O', which means the attribute is optional and not required to be implemented, with no dependencies or conditions affecting its inclusion.

* The table row describes an attribute within the Door Lock Cluster, specifically the "LocalProgrammingFeatures" attribute. This attribute is identified by the ID '0x002C' and is of the type 'LocalProgrammingFeaturesBitmap'. It is constrained to 'all', indicating that all bits in the bitmap are relevant. The quality of this attribute is marked as 'P', suggesting that its status is provisional and may change in the future. The default value for this attribute is '0', and it has an access level of 'R[W] VA', meaning it is readable and optionally writable with value access. The conformance rule for this attribute is 'O', which means it is optional and not required for implementation, with no dependencies or conditions affecting its optional status.

* The table row describes an attribute within the Door Lock Cluster, specifically the "WrongCodeEntryLimit" attribute. This attribute has an ID of '0x0030' and is of type 'uint8', with a constraint that its value must be between 1 and 255. The attribute is provisionally qualified ('P'), indicating that its status is temporary and may change in future specifications. The default value is 'MS', and it has read and optionally write access ('R[W]') with value access ('VA'). The conformance rule 'PIN | RID' means that the "WrongCodeEntryLimit" attribute is mandatory if either the 'PIN' feature or the 'RID' feature is supported. If neither feature is supported, the attribute is not required.

* The table row describes an attribute within the Door Lock Cluster, specifically the "UserCodeTemporaryDisableTime" attribute. This attribute is identified by the ID '0x0031' and is of type 'uint8', meaning it is an 8-bit unsigned integer with a constraint range from 1 to 255. The quality of this attribute is marked as 'Provisional' (P), indicating that its status is temporary and may change in future specifications. The default value is 'MS', and it has read and optional write access, as indicated by 'R[W] VA'. The conformance rule 'PIN | RID' means that this attribute is mandatory if either the 'PIN' feature or the 'RID' feature is supported. If neither feature is supported, the attribute is not required. This rule ensures that the attribute is included in implementations where either of these features is present, reflecting its relevance in those contexts.

* The table row describes an attribute within the Door Lock Cluster, specifically the "SendPINOverTheAir" attribute, which is a boolean type. This attribute is provisionally included, indicated by its quality 'P', and has a default value of '0'. It is accessible for reading and conditionally for writing, as denoted by 'R[W] VA'. The conformance rule '[!USR & PIN]' means that the attribute is optional if the condition '!USR & PIN' is true. In plain terms, this attribute is optional if the USR feature is not supported and the PIN feature is supported. If these conditions are not met, the attribute does not need to be included.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'RequirePINforRemoteOperation' attribute, which is a boolean type. This attribute is provisionally included, indicated by the 'P' in the Quality field, suggesting it is temporarily in place and may become mandatory in the future. The default value for this attribute is '0', meaning that, by default, a PIN is not required for remote operation. The Access field 'R[W] VA' indicates that the attribute is readable and optionally writable, with access restricted to verified administrators. The Conformance field 'COTA & PIN' specifies that this attribute is mandatory if both the 'COTA' (presumably a feature related to over-the-air updates) and 'PIN' features are supported. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'SecurityLevel' attribute, identified by the ID '0x0034'. This attribute has a default value of '0' and access permissions denoted by 'R V', indicating it is readable and possibly volatile. The 'Conformance' field is marked as 'D', which means the 'SecurityLevel' attribute is deprecated in the current Matter specification. This indicates that the attribute is considered obsolete and should not be used in new implementations, as it may be removed in future versions of the specification.

* The table row describes an attribute within the Door Lock Cluster, specifically the "ExpiringUserTimeout" attribute. This attribute is identified by the ID `0x0035` and is of type `uint16`, with a constraint that its value must be between 1 and 2880. It has a quality of `P`, indicating it is provisional, and a default value of `MS`. The access level is `R[W] VA`, meaning it is readable and optionally writable, with additional access constraints or conditions possibly specified elsewhere. The conformance rule `[USR]` indicates that the "ExpiringUserTimeout" attribute is optional if the condition `USR` is true, meaning it is only required if the specific feature or condition represented by `USR` is supported. Otherwise, it is not mandatory.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Door Lock Cluster, specifically the "AlarmMask" attribute, which is identified by the ID `0x0040` and is of the type `AlarmMaskBitmap`. The attribute is constrained to 'all', indicating it applies universally within its context. It has a quality status of 'P', suggesting it is provisional, and its default value is set to `0xFFFF`. The access level is 'RW VA', meaning it is readable and writable with additional access control. The conformance rule for this attribute is 'O', indicating that the "AlarmMask" attribute is optional. This means that while it is not required for implementation, it can be included without any dependencies or conditions.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'AliroReaderVerificationKey'. This attribute is identified by the ID '0x0080' and is of type 'octstr' with a constraint of 65, meaning it likely has a maximum length of 65 bytes. The attribute has a default value of 'null' and access permissions of 'R A', indicating it can be read and accessed. The 'Quality' is marked as 'X', which means this attribute is explicitly disallowed. The 'Conformance' field contains the expression 'ALIRO', which implies that the attribute is mandatory if the feature or condition 'ALIRO' is supported. If 'ALIRO' is not supported, the attribute is not required. This entry suggests that the 'AliroReaderVerificationKey' is a specialized attribute relevant only in contexts where the 'ALIRO' feature is applicable.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'AliroReaderGroupIdentifier'. This attribute has an ID of '0x0081' and is of type 'octstr' with a constraint of 16, meaning it can hold an octet string up to 16 bytes in length. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has 'R A' access, meaning it can be read and accessed. The 'Conformance' field is set to 'ALIRO', which implies that the attribute is mandatory if the feature or condition 'ALIRO' is supported. If 'ALIRO' is not supported, the attribute is not required.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'AliroReaderGroupSubIdentifier'. This attribute has an ID of '0x0082' and is of type 'octstr' with a constraint of 16, indicating it is an octet string with a maximum length of 16 bytes. The quality 'F' suggests it is a feature-specific attribute, and the access 'R A' indicates it can be read and is accessible. The conformance rule 'ALIRO' implies that this attribute is mandatory if the feature 'ALIRO' is supported. If the feature 'ALIRO' is not supported, the attribute is not required. This conformance condition ensures that the attribute is only implemented when relevant to the specific feature set of the device.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'AliroExpeditedTransactionSupportedProtocolVersions'. This attribute is identified by the ID '0x0083' and is of type 'list[octstr]', constrained to a maximum of 16 entries, each with a maximum length of 2 octets. The attribute is of quality 'F', has a default value of 'empty', and its access is restricted to read ('R') and administer ('A'). The conformance rule 'ALIRO' indicates that this attribute is mandatory if the feature 'ALIRO' is supported. If the feature 'ALIRO' is not supported, the attribute is not required. This means that the presence and implementation of this attribute depend on whether the 'ALIRO' feature is part of the device's supported features.

* In the Door Lock Cluster, under the Attributes section, the entry for 'AliroGroupResolvingKey' is identified by the ID '0x0084' and is of type 'octstr' with a constraint of 16. The quality of this attribute is marked as 'X', indicating that it is explicitly disallowed in the current specification. The default value for this attribute is 'null', and it has read and attribute access permissions ('R A'). The conformance rule 'ALBU' suggests that the attribute is mandatory if the feature 'ALBU' is supported. However, given the 'X' quality marking, it is not allowed regardless of the conformance condition, meaning it should not be implemented or used in any scenario.

* The table row describes an attribute within the Door Lock Cluster, specifically named "AliroSupportedBLEUWBP rotocolVersions," identified by the ID '0x0085'. This attribute is a list of octet strings, constrained to a maximum of 16 entries, each with a maximum length of 2 octets. It is a feature attribute (indicated by 'F'), with a default value of an empty list, and it has read and attribute access permissions ('R A'). The conformance rule 'ALBU' implies that this attribute is mandatory if the feature 'ALBU' is supported. If the feature 'ALBU' is not supported, the attribute is not required. This means that the presence of this attribute is conditional upon the support of the 'ALBU' feature within the device's implementation.

* The table row describes an attribute within the Door Lock Cluster, specifically the 'AliroBLEAdvertisingVersion'. This attribute is identified by the ID '0x0086' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is set to 'all', indicating that there are no specific limitations on its value beyond the type constraint. The 'Quality' is marked as 'F', which typically denotes a feature-related quality, and it has a default value of '0'. The 'Access' is specified as 'R A', meaning the attribute is readable and can be accessed administratively. The 'Conformance' field is 'ALBU', which implies that the attribute is mandatory if the feature 'ALBU' is supported. If 'ALBU' is not supported, the conformance rule does not specify any alternative, suggesting that the attribute may not be applicable or required in such cases.

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfAliroCredentialIssuerKeysSupported" attribute. This attribute has an ID of '0x0087' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that there are no specific constraints on its value beyond the type's inherent limits. The 'Quality' is marked as 'F', which typically denotes a feature or characteristic of the attribute, though the exact meaning would depend on the broader context of the specification. The default value for this attribute is '0', and it has 'R V' access, meaning it can be read and possibly verified. The 'Conformance' is specified as 'ALIRO', indicating that this attribute is mandatory if the feature or condition 'ALIRO' is supported. If 'ALIRO' is not supported, this attribute is not required.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Door Lock Cluster, specifically the "NumberOfAliroEndpointKeys Supported" attribute, identified by the ID '0x0088'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally ('Constraint': 'all'). The attribute has a default value of '0' and is accessible for reading and viewing ('Access': 'R V'). The 'Conformance' field is specified as 'ALIRO', indicating that this attribute is mandatory if the feature 'ALIRO' is supported. If the 'ALIRO' feature is not supported, the attribute is not required. This entry ensures that devices supporting the 'ALIRO' feature must implement this attribute to specify the number of endpoint keys supported.

5.2.9.1. LockState Attribute
This attribute may be NULL if the lock hardware does not currently know the status of the locking
mechanism. For example, a lock may not know the LockState status after a power cycle until the
first lock actuation is completed.
The Not Fully Locked value is used by a lock to indicate that the state of the lock is somewhere
between Locked and Unlocked so it is only partially secured. For example, a deadbolt could be par
tially extended and not in a dead latched state.
5.2.9.2. LockType Attribute
This attribute SHALL indicate the type of door lock as defined in LockTypeEnum.
5.2.9.3. ActuatorEnabled Attribute
This attribute SHALL indicate if the lock is currently able to (Enabled) or not able to (Disabled)
process remote Lock, Unlock, or Unlock with Timeout commands.
This attribute has the following possible values:

_Table parsed from section 'Attributes':_

* In the context of the Door Lock Cluster's attributes, the table row describes an attribute with the name 'Boolean Value' and a default value of '0', which indicates that the feature is 'Disabled' by default. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if we assume a conformance string was present, it would dictate the conditions under which this attribute is required, optional, or otherwise. For instance, if the conformance string were `M`, it would mean the attribute is always mandatory. If it were `O`, it would be optional with no dependencies. Without a specific conformance string, we can only infer that the attribute's default state is 'Disabled', and its necessity would depend on the broader context and specific conformance rules applied to the Door Lock Cluster in the Matter specification.

* The table row entry pertains to the "Door Lock Cluster" within the "Attributes" section, specifically focusing on an attribute labeled "Boolean Value" with a value of '1' and a summary description of "Enabled." The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the context, if we assume a conformance string like `M`, it would mean that this attribute is mandatory for any implementation of the Door Lock Cluster. This implies that any device or application implementing this cluster must include the "Boolean Value" attribute as part of its configuration. If the conformance were different, such as `O`, it would indicate that the attribute is optional, meaning it could be included at the discretion of the implementer without any requirement.

5.2.9.4. DoorState Attribute
This attribute SHALL indicate the current door state as defined in DoorStateEnum.
This attribute SHALL be null only if an internal error prevents the retrieval of the current door
state.
5.2.9.5. DoorOpenEvents Attribute
This attribute SHALL hold the number of door open events that have occurred since it was last
zeroed.
5.2.9.6. DoorClosedEvents Attribute
This attribute SHALL hold the number of door closed events that have occurred since it was last
zeroed.
5.2.9.7. OpenPeriod Attribute
This attribute SHALL hold the number of minutes the door has been open since the last time it tran
sitioned from closed to open.
5.2.9.8. NumberOfTotalUsersSupported Attribute
This attribute SHALL indicate the number of total users supported by the lock.
5.2.9.9. NumberOfPINUsersSupported Attribute
This attribute SHALL indicate the number of PIN users supported.
5.2.9.10. NumberOfRFIDUsersSupported Attribute
This attribute SHALL indicate the number of RFID users supported.
5.2.9.11. NumberOfWeekDaySchedulesSupportedPerUser Attribute
This attribute SHALL indicate the number of configurable week day schedule supported per user.
5.2.9.12. NumberOfYearDaySchedulesSupportedPerUser Attribute
This attribute SHALL indicate the number of configurable year day schedule supported per user.
5.2.9.13. NumberOfHolidaySchedulesSupported Attribute
This attribute SHALL indicate the number of holiday schedules supported for the entire door lock
device.
5.2.9.14. MaxPINCodeLength Attribute
This attribute SHALL indicate the maximum length in bytes of a PIN Code on this device.
5.2.9.15. MinPINCodeLength Attribute
This attribute SHALL indicate the minimum length in bytes of a PIN Code on this device.
5.2.9.16. MaxRFIDCodeLength Attribute
This attribute SHALL indicate the maximum length in bytes of a RFID Code on this device. The
value depends on the RFID code range specified by the manufacturer, if media anti-collision identi
fiers (UID) are used as RFID code, a value of 20 (equals 10 Byte ISO 14443A UID) is recommended.
5.2.9.17. MinRFIDCodeLength Attribute
This attribute SHALL indicate the minimum length in bytes of a RFID Code on this device. The value
depends on the RFID code range specified by the manufacturer, if media anti-collision identifiers
(UID) are used as RFID code, a value of 8 (equals 4 Byte ISO 14443A UID) is recommended.
5.2.9.18. CredentialRulesSupport Attribute
This attribute SHALL contain a bitmap with the bits set for the values of CredentialRuleEnum sup
ported on this device.
5.2.9.19. NumberOfCredentialsSupportedPerUser Attribute
This attribute SHALL indicate the number of credentials that could be assigned for each user.
Depending on the value of NumberOfRFIDUsersSupported and NumberOfPINUsersSupported it
may not be possible to assign that number of credentials for a user.
For example, if the device supports only PIN and RFID credential types, NumberOfCredentialsSup
portedPerUser is set to 10, NumberOfPINUsersSupported is set to 5 and NumberOfRFIDUsersSup
ported is set to 3, it will not be possible to actually assign 10 credentials for a user because maxi
mum number of credentials in the database is 8.
5.2.9.20. Language Attribute
This attribute SHALL indicate the language for the on-screen or audible user interface using a 2-
byte language code from ISO-639-1.
5.2.9.21. LEDSettings Attribute
This attribute SHALL indicate the settings for the LED support, as defined by LEDSettingEnum.
5.2.9.22. AutoRelockTime Attribute
This attribute SHALL indicate the number of seconds to wait after unlocking a lock before it auto
matically locks again. 0=disabled. If set, unlock operations from any source will be timed. For one
time unlock with timeout use the specific command.
5.2.9.23. SoundVolume Attribute
This attribute SHALL indicate the sound volume on a door lock as defined by SoundVolumeEnum.
5.2.9.24. OperatingMode Attribute
This attribute SHALL indicate the current operating mode of the lock as defined in OperatingMod
eEnum.
5.2.9.25. SupportedOperatingModes Attribute
This attribute SHALL contain a bitmap with all operating bits of the OperatingMode attribute sup
ported by the lock. All operating modes NOT supported by a lock SHALL be set to one. The value of
the OperatingMode enumeration defines the related bit to be set.
5.2.9.26. DefaultConfigurationRegister Attribute
This attribute SHALL represent the default configurations as they are physically set on the device
(example: hardware dip switch setting, etc…) and represents the default setting for some of the
attributes within this cluster (for example: LED, Auto Lock, Sound Volume, and Operating Mode
attributes).
This is a read-only attribute and is intended to allow clients to determine what changes MAY need
to be made without having to query all the included attributes. It MAY be beneficial for the clients
to know what the device’s original settings were in the event that the device needs to be restored to
factory default settings.
If the Client device would like to query and modify the door lock server’s operating settings, it
SHOULD send read and write attribute requests to the specific attributes.
For example, the Sound Volume attribute default value is Silent Mode. However, it is possible that
the current Sound Volume is High Volume. Therefore, if the client wants to query/modify the cur
rent Sound Volume setting on the server, the client SHOULD read/write to the Sound Volume
attribute.
5.2.9.26.1. LocalProgramming Bit
This bit SHALL indicate the default value of the EnableLocalProgramming attribute.
5.2.9.26.2. KeypadInterface Bit
This bit SHALL indicate the default state of the keypad interface.
5.2.9.26.3. RemoteInterface Bit
This bit SHALL indicate the default state of the remote interface.
5.2.9.26.4. SoundVolume Bit
This bit SHALL indicate the default value of SoundVolume attribute.
5.2.9.26.5. AutoRelockTime Bit
This bit SHALL indicate the default value of AutoRelockTime attribute.
5.2.9.26.6. LEDSettings Bit
This bit SHALL indicate the default value of LEDSettings attribute.
5.2.9.27. EnableLocalProgramming Attribute
This attribute SHALL enable/disable local programming on the door lock of certain features (see
LocalProgrammingFeatures  attribute).  If  this  value  is  set  to  TRUE  then  local  programming  is
enabled on the door lock for all features. If it is set to FALSE then local programming is disabled on
the door lock for those features whose bit is set to 0 in the LocalProgrammingFeatures attribute.
Local programming SHALL be enabled by default.
5.2.9.28. EnableOneTouchLocking Attribute
This attribute SHALL enable/disable the ability to lock the door lock with a single touch on the door
lock.
5.2.9.29. EnableInsideStatusLED Attribute
This attribute SHALL enable/disable an inside LED that allows the user to see at a glance if the door
is locked.
5.2.9.30. EnablePrivacyModeButton Attribute
This attribute SHALL enable/disable a button inside the door that is used to put the lock into pri
vacy mode. When the lock is in privacy mode it cannot be manipulated from the outside.
5.2.9.31. LocalProgrammingFeatures Attribute
This attribute SHALL indicate the local programming features that will be disabled when EnableLo
calProgramming attribute is set to False. If a door lock doesn’t support disabling one aspect of local
programming it SHALL return CONSTRAINT_ERROR during a write operation of this attribute. If
the EnableLocalProgramming attribute is set to True then all local programming features SHALL be
enabled regardless of the bits set to 0 in this attribute.
The features that can be disabled from local programming are defined in LocalProgrammingFea
turesBitmap.
5.2.9.32. WrongCodeEntryLimit Attribute
This attribute SHALL indicate the number of incorrect Pin codes or RFID presentment attempts a
user is allowed to enter before the lock will enter a lockout state. The value of this attribute is com
pared to all failing forms of credential presentation, including Pin codes used in an Unlock Com
mand when RequirePINforRemoteOperation is set to true. Valid range is 1-255 incorrect attempts.
The  lockout  state  will  be  for  the  duration  of  UserCodeTemporaryDisableTime.  If  the  attribute
accepts writes and an attempt to write the value 0 is made, the device SHALL respond with CON
STRAINT_ERROR.
The lock MAY reset the counter used to track incorrect credential presentations as required by
internal logic, environmental events, or other reasons. The lock SHALL reset the counter if a valid
credential is presented.
5.2.9.33. UserCodeTemporaryDisableTime Attribute
This attribute SHALL indicate the number of seconds that the lock shuts down following wrong
code entry. Valid range is 1-255 seconds. Device can shut down to lock user out for specified amount
of time. (Makes it difficult to try and guess a PIN for the device.) If the attribute accepts writes and
an attempt to write the attribute to 0 is made, the device SHALL respond with CONSTRAINT_ERROR.
5.2.9.34. SendPINOverTheAir Attribute
This attribute SHALL indicate the door locks ability to send PINs over the air. If the attribute is True
it is ok for the door lock server to send PINs over the air. This attribute determines the behavior of
the server’s TX operation. If it is false, then it is not ok for the device to send PIN in any messages
over the air.
The PIN field within any door lock cluster message SHALL keep the first octet unchanged and
masks the actual code by replacing with 0xFF. For example (PIN "1234" ): If the attribute value is
True, 0x04 0x31 0x32 0x33 0x34 SHALL be used in the PIN field in any door lock cluster message
payload. If the attribute value is False, 0x04 0xFF 0xFF 0xFF 0xFF SHALL be used.
5.2.9.35. RequirePINForRemoteOperation Attribute
This attribute SHALL indicate if the door lock requires an optional PIN. If this attribute is set to
True, the door lock server requires that an optional PINs be included in the payload of remote lock
operation events like Lock, Unlock, Unlock with Timeout and Toggle in order to function.
5.2.9.36. ExpiringUserTimeout Attribute
This attribute SHALL indicate the number of minutes a PIN, RFID, Fingerprint, or other credential
associated with a user of type ExpiringUser SHALL remain valid after its first use before expiring.
When the credential expires the UserStatus for the corresponding user record SHALL be set to
OccupiedDisabled.
5.2.9.37. AlarmMask Attribute
This attribute is only supported if the Alarms cluster is on the same endpoint. The alarm mask is
used to turn on/off alarms for particular functions. Alarms for an alarm group are enabled if the
associated alarm mask bit is set. Each bit represents a group of alarms. Entire alarm groups can be
turned on or off by setting or clearing the associated bit in the alarm mask.
This mask DOES NOT apply to the Events mechanism of this cluster.

_Table parsed from section 'Attributes':_

* The table row entry for the Door Lock Cluster under the Attributes section describes an attribute related to the 'Alarm Code Value' with an 'AlarmMaskBitmap Bit' set to '0'. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context and typical usage of conformance expressions, it can be inferred that this attribute is likely mandatory or optional depending on specific conditions related to the 'AlarmMaskBitmap Bit'. If the 'AlarmMaskBitmap Bit' is '0', it might indicate a default or baseline requirement for the attribute, suggesting that the attribute is either always required (mandatory) or conditionally required based on other features or settings within the Door Lock Cluster. Without additional context or a specific conformance expression, the exact requirement cannot be fully determined, but the attribute's presence suggests it plays a role in the alarm functionality of the door lock system.

* In the context of the Door Lock Cluster's attributes, the table row entry for 'Alarm Code Value' with an 'AlarmMaskBitmap Bit' of '1' indicates a specific attribute related to the alarm functionality of a door lock. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if we assume a conformance string was provided, it would dictate the conditions under which this attribute is required or optional. For example, if the conformance string were `M`, it would mean that the 'Alarm Code Value' attribute is always mandatory. If it were `O`, it would be optional with no dependencies. Without a specific conformance string, we can only infer that the attribute is related to the alarm system of the door lock and that its presence or requirement would depend on the specific conformance rules outlined in the complete Matter specification document.

* In the context of the Door Lock Cluster's attributes, the table row entry for 'Alarm Code Value' with a value of '2' and 'AlarmMaskBitmap Bit' of '2' describes a specific attribute related to the alarm functionality of a door lock device. The conformance rule for this attribute is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, if the conformance string were included, it would dictate when this attribute is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean that the 'Alarm Code Value' attribute is mandatory for all implementations of the Door Lock Cluster. If it were 'O', the attribute would be optional, allowing manufacturers to decide whether to implement it. The absence of a conformance string in the provided data means that further documentation or context is needed to determine the exact requirements for this attribute.

* In the context of the Door Lock Cluster's Attributes, the table row entry for 'Alarm Code Value' with a value of '3' and 'AlarmMaskBitmap Bit' of '3' pertains to a specific attribute related to alarm functionalities within a door lock system. The conformance rule for this attribute is not explicitly provided in the data given, but based on the Matter Conformance Interpretation Guide, if we were to interpret a typical conformance expression, it would dictate whether this attribute is mandatory, optional, provisional, deprecated, or disallowed under certain conditions. For instance, if the conformance were something like `AB, O`, it would mean that the attribute is mandatory if the feature `AB` is supported; otherwise, it is optional. However, without a specific conformance string provided, we can only infer that this attribute is part of the alarm management features in the Door Lock Cluster, potentially influencing how alarms are configured or triggered based on the 'Alarm Code Value' and 'Alarm

* The table row entry pertains to the "Alarm Code Value" attribute within the Door Lock Cluster's Attributes section. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, we can infer that it involves specific conditions related to the "AlarmMaskBitmap Bit" with a value of '4'. This suggests that the attribute's requirement is conditional, likely depending on the presence or configuration of certain features or settings within the Door Lock Cluster. If the conformance rule were provided, it would specify whether the "Alarm Code Value" is mandatory, optional, provisional, deprecated, or disallowed, possibly contingent on the state of the "AlarmMaskBitmap Bit" or other related features. Without the explicit conformance string, a detailed interpretation cannot be made, but the attribute's inclusion indicates its relevance to the alarm functionality of the door lock system.

* In the context of the Door Lock Cluster's attributes, the table row entry for 'Alarm Code Value' with a value of '5' and 'AlarmMaskBitmap Bit' set to '5' pertains to a specific feature or attribute related to the alarm system of a door lock. The conformance rule for this entry is not explicitly provided in the data snippet, but if we were to interpret a typical conformance expression, it might specify conditions under which this attribute is required, optional, or otherwise. For instance, if the conformance were something like `M`, it would mean that this attribute is mandatory for all implementations of the Door Lock Cluster. If it were `O`, it would be optional, and so on. Without a specific conformance string provided, we can only infer that this attribute is associated with the alarm functionality of the door lock, potentially indicating a specific alarm condition or configuration setting.

* In the context of the Door Lock Cluster, specifically within the Attributes section, the table row entry for 'Alarm Code Value' with a value of '6' and 'AlarmMaskBitmap Bit' of '6' pertains to a specific attribute related to alarm functionalities. The conformance rule for this attribute is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which this attribute is required, optional, or otherwise. For instance, if the conformance were `M`, it would mean the attribute is always mandatory. If it were `O`, it would be optional with no dependencies. Without a specific conformance string, we can only infer that this attribute is part of the alarm system configuration within the Door Lock Cluster, potentially indicating a specific alarm condition or setting that can be enabled or disabled based on the 'AlarmMaskBitmap Bit' value.

5.2.9.38. AliroReaderVerificationKey Attribute
This attribute SHALL indicate the verification key component of the Reader’s key pair as defined in
[Aliro]. The value, if not null, SHALL be an uncompressed elliptic curve public key as defined in sec
tion 2.3.3 of SEC 1.
This attribute SHALL be null if no Reader key pair has been configured on the lock. See SetAliroRe
aderConfig.
5.2.9.39. AliroReaderGroupIdentifier Attribute
This attribute SHALL indicate the reader_group_identifier as defined in [Aliro].
This attribute SHALL be null if no reader_group_identifier has been configured on the lock. See
SetAliroReaderConfig.
5.2.9.40. AliroReaderGroupSubIdentifier Attribute
This attribute SHALL indicate the reader_group_sub_identifier as defined in [Aliro].
5.2.9.41. AliroExpeditedTransactionSupportedProtocolVersions Attribute
This attribute SHALL indicate the list of protocol versions supported for expedited transactions as
defined in [Aliro].
5.2.9.42. AliroGroupResolvingKey Attribute
This attribute SHALL indicate the Group Resolving Key as defined in [Aliro].
This attribute SHALL be null if no group resolving key has been configured on the lock. See
SetAliroReaderConfig.
5.2.9.43. AliroSupportedBLEUWBProtocolVersions Attribute
This attribute SHALL indicate the list of protocol versions supported for the Bluetooth LE + UWB
Access Control Flow as defined in [Aliro].
5.2.9.44. AliroBLEAdvertisingVersion Attribute
This attribute SHALL indicate the version of the Bluetooth LE advertisement as defined in [Aliro].
5.2.9.45. NumberOfAliroCredentialIssuerKeysSupported
This attribute SHALL indicate the maximum number of AliroCredentialIssuerKey credentials that
can be stored on the lock.
5.2.9.46. NumberOfAliroEndpointKeysSupported
This attribute SHALL indicate the maximum number of endpoint key credentials that can be stored
on the lock. This limit applies to the sum of the number of AliroEvictableEndpointKey credentials
and the number of AliroNonEvictableEndpointKey credentials.
The credential indices used for these two credential types are independent of each
other,  similar  to  all  other  credential  types.  As  long  as  NumberOfAliroEnd
pointKeysSupported is at least 2 a client could add a credential of type AliroE
NOTE
victableEndpointKey at any index from 1 to NumberOfAliroEndpointKeysSupported
and also add a credential of type AliroNonEvictableEndpointKey at the same index,
and both credentials would exist on the server.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "LockDoor" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response, as indicated by 'Response: Y'. The access level is specified as 'O T', which typically refers to access control requirements, though further context would be needed to interpret these specific codes. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "LockDoor" command must always be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UnlockDoor" command, which is sent from a client to a server. The command requires a response, as indicated by 'Response: Y', and has an access level of 'O T', which typically refers to specific access control requirements. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "UnlockDoor" command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "Toggle" command, which is identified by the ID '0x02'. This command is intended to be sent from a client to a server, as indicated by the direction "client ⇒ server". The command requires a response, as denoted by 'Response': 'Y'. The access level is marked as 'O T', which typically refers to specific access control requirements, though these are not detailed in the provided data. The conformance rule for this command is 'X', meaning it is explicitly disallowed within the current Matter specification. This indicates that the "Toggle" command should not be implemented or used in any compliant Matter device within the Door Lock Cluster.

* In the Door Lock Cluster, under the Commands section, the table row describes the command 'UnlockWithTimeout' with an ID of '0x03'. This command is directed from the client to the server and requires a response. The access level is marked as 'O T', indicating specific access requirements or conditions that are not detailed here. The conformance rule for this command is 'O', meaning it is optional. This indicates that the implementation of the 'UnlockWithTimeout' command is not required and has no dependencies on other features or conditions. Therefore, manufacturers have the discretion to include or exclude this command in their devices without affecting compliance with the Matter specification.

* The table row describes a command within the Door Lock Cluster, specifically the "SetPINCode" command, which is identified by the ID '0x05'. This command is directed from the client to the server and requires a response ('Y'). The access level is indicated as 'A T', which typically refers to specific access control requirements. The conformance rule for this command is '!USR & PIN', which means that the command is mandatory if the feature 'USR' is not supported and the feature 'PIN' is supported. In simpler terms, the "SetPINCode" command must be implemented if the device does not support the 'USR' feature but does support the 'PIN' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "GetPINCode" command, which is directed from the client to the server and expects a "GetPINCodeResponse" in return. The access level for this command is denoted as 'A'. The conformance rule '!USR & PIN' indicates that the "GetPINCode" command is mandatory if the feature 'USR' is not supported and the feature 'PIN' is supported. In other words, this command must be implemented in devices where the 'USR' feature is absent, but the 'PIN' feature is present.

* The table row describes a command within the Door Lock Cluster, specifically the "GetPINCodeResponse" command, which is identified by the ID '0x06'. This command is directed from the server to the client, as indicated by the direction 'client ⇐ server'. The 'Response' field marked as 'N' suggests that this command does not expect a response. The conformance rule '!USR & PIN' means that the "GetPINCodeResponse" command is mandatory if the feature 'USR' is not supported and the feature 'PIN' is supported. In other words, this command must be implemented when the device does not support the 'USR' feature but does support the 'PIN' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearPINCode" command, which is directed from the client to the server. The command has an ID of '0x07' and requires a response ('Y'). The access level is denoted as 'A T', indicating specific access requirements. The conformance rule '!USR & PIN' specifies that the "ClearPINCode" command is mandatory if the device does not support the 'USR' feature but does support the 'PIN' feature. In other words, the command must be implemented if the device lacks user management capabilities but includes PIN code functionality.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearAllPINCodes" command, which is identified by the ID '0x08'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access control for this command is denoted by 'A T', suggesting specific access requirements. The conformance rule '!USR & PIN' indicates that the "ClearAllPINCodes" command is mandatory if the feature 'USR' is not supported and the feature 'PIN' is supported. In other words, this command must be implemented in devices that do not support the 'USR' feature but do support the 'PIN' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "SetUserStatus" command, which is directed from the client to the server. This command requires a response and has an access level denoted by 'A'. The conformance rule for this command is expressed as `!USR & (PIN | RID | FGP)`. This means that the "SetUserStatus" command is mandatory if the feature `USR` is not supported, and at least one of the features `PIN`, `RID`, or `FGP` is supported. In simpler terms, the command must be implemented if the system does not support the `USR` feature but does support any of the `PIN`, `RID`, or `FGP` features.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUserStatus" command, which is identified by the ID '0x0A'. This command is directed from the client to the server and expects a response in the form of "GetUserStatusResponse". The access level for this command is denoted by 'A'. The conformance rule '!USR & (PIN | RID | FGP)' indicates that the "GetUserStatus" command is mandatory under specific conditions: it must be implemented if the feature 'USR' is not supported and at least one of the features 'PIN', 'RID', or 'FGP' is supported. In simpler terms, this command is required when user support is not available, but there is support for either PIN codes, RFID, or fingerprint features.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUserStatusResponse" command, which is identified by the ID '0x0A'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The conformance rule '!USR' indicates that the "GetUserStatusResponse" command is mandatory if the feature 'USR' is not supported. In other words, this command must be implemented unless the 'USR' feature is present, in which case it is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "SetWeekDaySchedule" command, which is identified by the ID '0x0B'. This command is directed from the client to the server and requires a response ('Y'). It has an access level of 'A', indicating a certain level of permission is needed to execute it. The conformance rule 'WDSCH' suggests that the command is mandatory if the feature or condition represented by 'WDSCH' is supported. Without additional context on what 'WDSCH' specifically refers to, it implies that the command must be implemented in devices that support the 'WDSCH' feature, ensuring that the scheduling functionality is available when this feature is present.

* The table row describes a command within the Door Lock Cluster, specifically the "GetWeekDaySchedule" command, which is identified by the ID '0x0C'. This command is sent from a client to a server and expects a response in the form of "GetWeekDayScheduleResponse". The access level for this command is denoted by 'A', which typically indicates a certain level of access control, such as administrator-level access. The conformance rule 'WDSCH' implies that the command is mandatory if the feature code 'WDSCH' (likely representing a Week Day Schedule feature) is supported by the device. If the device supports this feature, it must implement the "GetWeekDaySchedule" command; otherwise, the command is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "GetWeekDayScheduleResponse" command, which is sent from the server to the client. The command does not require a response from the client, as indicated by 'Response': 'N'. The conformance rule for this command is 'WDSCH', meaning it is mandatory if the feature 'WDSCH' (likely representing "Week Day Schedule") is supported by the device. If the device supports the 'WDSCH' feature, it must implement this command; otherwise, the command is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearWeekDaySchedule" command, which is identified by the ID '0x0D'. This command is directed from the client to the server, and it requires a response ('Y'). The access level is marked as 'A', indicating a specific access requirement. The conformance rule for this command is 'WDSCH', which means that the command is mandatory if the feature 'WDSCH' (likely representing a Week Day Schedule feature) is supported by the device. If the device supports the 'WDSCH' feature, it must implement the "ClearWeekDaySchedule" command; otherwise, the command is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "SetYearDaySchedule" command, which is identified by the ID '0x0E'. This command is directed from the client to the server, and it requires a response ('Y'). The access level is denoted as 'A', which typically indicates a specific access requirement or permission level. The conformance rule 'YDSCH' indicates that the command is mandatory if the feature or condition 'YDSCH' is supported. In this context, 'YDSCH' likely refers to a specific feature or capability related to scheduling within the Door Lock Cluster. If the device supports this feature, the "SetYearDaySchedule" command must be implemented.

* The table row describes a command within the Door Lock Cluster, specifically the "GetYearDaySchedule" command, which is sent from a client to a server. The command expects a response in the form of "GetYearDayScheduleResponse" and requires access level 'A'. The conformance rule for this command is "YDSCH", indicating that the command is mandatory if the feature "YDSCH" (Year Day Schedule) is supported by the device. If the device does not support the "YDSCH" feature, the command is not required. This means that the implementation of this command is contingent upon the presence of the Year Day Schedule feature in the device's capabilities.

* The table row describes a command within the Door Lock Cluster, specifically the "GetYearDayScheduleResponse" command, which is identified by the ID '0x0F'. This command is directed from the server to the client, as indicated by the direction "client ⇐ server". The 'Response' field marked as 'N' suggests that this command does not expect a response. The conformance rule 'YDSCH' indicates that the command is mandatory if the feature 'YDSCH' (likely representing a Year Day Schedule feature) is supported. If the device supports the Year Day Schedule feature, then this command must be implemented; otherwise, it is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearYearDaySchedule" command, which is directed from the client to the server. The command has an ID of '0x10' and requires a response ('Y'). The access level is denoted as 'A', indicating a specific access requirement. The conformance rule 'YDSCH' implies that the command is mandatory if the feature 'YDSCH' is supported. In this context, 'YDSCH' likely refers to a specific feature or condition related to the Door Lock Cluster, and if this feature is present, the command must be implemented. If 'YDSCH' is not supported, the conformance rule does not specify an alternative, suggesting that the command is not required in such cases.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "SetHolidaySchedule" command, which is identified by the ID '0x11'. This command is directed from the client to the server, and it requires a response ('Y'). The access level is denoted as 'A', which typically refers to a specific access control requirement. The conformance rule for this command is 'HDSCH', indicating that its implementation is mandatory if the feature or condition represented by 'HDSCH' is supported. If 'HDSCH' is not supported, the command is not required. This means that the necessity of implementing the "SetHolidaySchedule" command depends on the presence of the 'HDSCH' feature within the device's capabilities.

* The table row describes a command within the Door Lock Cluster, specifically the "GetHolidaySchedule" command, which is directed from the client to the server. This command expects a response in the form of "GetHolidayScheduleResponse" and requires access level 'A'. The conformance rule for this command is specified as "HDSCH". According to the Matter Conformance Interpretation Guide, "HDSCH" is a feature code that determines the command's requirement status. If the feature "HDSCH" is supported, the "GetHolidaySchedule" command is mandatory. If "HDSCH" is not supported, the command is not required. This indicates that the command's necessity is contingent upon the support of the "HDSCH" feature within the implementation.

* The table row describes a command within the Door Lock Cluster, specifically the "GetHolidayScheduleResponse" command, which is identified by the ID '0x12'. This command is sent from the server to the client, as indicated by the direction "client ⇐ server". The response field marked 'N' suggests that this command does not expect a response. The conformance rule 'HDSCH' implies that the command is mandatory if the feature or condition represented by 'HDSCH' is supported. If the feature 'HDSCH' is not supported, the command is not required. This means that the inclusion of this command depends on the support for the 'HDSCH' feature within the implementation of the Door Lock Cluster.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearHolidaySchedule" command. This command is identified by the ID '0x13' and is directed from the client to the server, with a response expected ('Y'). The access level is denoted as 'A', which typically refers to a specific access privilege required to execute the command. The conformance rule 'HDSCH' indicates that the command's requirement is conditional based on the support of the feature or condition represented by 'HDSCH'. According to the Matter Conformance Interpretation Guide, if the feature 'HDSCH' is supported, then the "ClearHolidaySchedule" command is mandatory. If 'HDSCH' is not supported, the command is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "SetUserType" command, identified by the ID '0x14'. This command is sent from the client to the server, and it requires a response. The access level is denoted as 'A'. The conformance rule '!USR & (PIN | RID | FGP)' indicates that the "SetUserType" command is mandatory under specific conditions: it must be implemented if the feature 'USR' is not supported and at least one of the features 'PIN', 'RID', or 'FGP' is supported. This means that the command is required when user support is not available, but there is support for either Personal Identification Number (PIN), Radio Identification (RID), or Fingerprint (FGP) features.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUserType" command, which is identified by the ID '0x15'. This command is sent from the client to the server and expects a response in the form of "GetUserTypeResponse". The access level for this command is denoted by 'A'. The conformance rule '!USR & (PIN | RID | FGP)' specifies that the "GetUserType" command is mandatory if the feature 'USR' is not supported and at least one of the features 'PIN', 'RID', or 'FGP' is supported. In simpler terms, the command must be implemented if the system does not support the 'USR' feature but does support any of the 'PIN', 'RID', or 'FGP' features.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUserTypeResponse" command, which is identified by the ID '0x15'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The conformance rule '!USR' indicates that the "GetUserTypeResponse" command is mandatory only if the feature 'USR' (likely representing a specific user-related feature) is not supported. In other words, this command must be implemented unless the 'USR' feature is present, in which case it is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "SetRFIDCode" command, which is identified by the ID '0x16'. This command is directed from the client to the server, and it requires a response ('Response': 'Y'). The access control for this command is denoted by 'A T', indicating specific access requirements. The conformance rule '!USR & RID' means that the "SetRFIDCode" command is mandatory if the feature 'USR' is not supported and the feature 'RID' is supported. In essence, this command must be implemented if the system does not support the 'USR' feature but does support the 'RID' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "GetRFIDCode" command, which is identified by the ID '0x17'. This command is sent from the client to the server, and it expects a response in the form of "GetRFIDCodeResponse". The access level is denoted as 'A', which typically indicates some form of access control or permission is required. The conformance rule '!USR & RID' specifies that the "GetRFIDCode" command is mandatory only if the feature 'USR' is not supported and the feature 'RID' is supported. In simpler terms, the command must be implemented if the system does not support the 'USR' feature but does support the 'RID' feature. If both conditions are not met, the command is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "GetRFIDCodeResponse" command, which is identified by the ID '0x17'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction, and it does not expect a response, as denoted by 'Response': 'N'. The conformance rule '!USR & RID' means that the "GetRFIDCodeResponse" command is mandatory only if the feature 'USR' is not supported and the feature 'RID' is supported. In other words, for this command to be required, the absence of the 'USR' feature and the presence of the 'RID' feature must both be true.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearRFIDCode" command, which is identified by the ID '0x18'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level is denoted by 'A T', which typically refers to specific access control requirements. The conformance rule '!USR & RID' means that the "ClearRFIDCode" command is mandatory if the feature 'USR' is not supported and the feature 'RID' is supported. In other words, this command must be implemented in devices that do not support the 'USR' feature but do support the 'RID' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearAllRFIDCodes" command, which is directed from the client to the server and requires a response. The access level for this command is indicated by 'A T', suggesting specific access requirements. The conformance rule '!USR & RID' means that the "ClearAllRFIDCodes" command is mandatory if the feature 'USR' is not supported and the feature 'RID' is supported. In other words, this command must be implemented in devices that do not support the 'USR' feature but do support the 'RID' feature.

* The table row describes a command within the Door Lock Cluster, specifically the "SetUser" command, which is identified by the ID '0x1A'. This command is directed from the client to the server and requires a response ('Y'). The access control for this command is denoted by 'A T', indicating specific access requirements. The conformance rule 'USR' means that the "SetUser" command is mandatory if the feature or condition represented by 'USR' is supported. In other words, if the system or device supports the 'USR' feature, then implementing the "SetUser" command is required. If 'USR' is not supported, the conformance rule does not apply, and the command may not be necessary.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUser" command, which is identified by the ID '0x1B'. This command is directed from the client to the server and expects a response in the form of "GetUserResponse". The access level for this command is denoted by 'A', which typically refers to a specific access control requirement. The conformance rule for this command is 'USR', indicating that the command is mandatory if the feature 'USR' (likely representing a User Management feature) is supported. If the 'USR' feature is not supported, the command is not required. This means that the implementation of the "GetUser" command is contingent upon the presence of the 'USR' feature within the device's capabilities.

* The table row describes a command within the Door Lock Cluster, specifically the "GetUserResponse" command, which is identified by the ID '0x1C'. This command is sent from the server to the client, as indicated by the direction 'client ⇐ server'. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked as 'USR', which means that the "GetUserResponse" command is mandatory if the feature or condition 'USR' is supported. In this context, 'USR' likely refers to a specific feature or capability related to user management within the Door Lock Cluster. If the 'USR' feature is implemented, the command must be supported; otherwise, it is not required.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearUser" command, which is identified by the ID '0x1D'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access control for this command is denoted by 'A T', which typically refers to specific access privileges or roles required to execute the command. The conformance rule 'USR' indicates that the command is mandatory if the feature 'USR' (likely representing a User Management feature) is supported. If the 'USR' feature is not supported, the conformance of this command is not explicitly defined in this entry, implying it may not be applicable or required.

* The table row describes a command within the Door Lock Cluster, specifically the "SetCredential" command, which is identified by the ID '0x22'. This command is sent from the client to the server and expects a response in the form of "SetCredentialResponse". The access control for this command is denoted by 'A T', indicating specific access requirements. The conformance rule 'USR' implies that the command is mandatory if the feature 'USR' is supported. If the 'USR' feature is not supported, the conformance of this command is not specified in this entry, suggesting that it might not be applicable or required in such cases.

* The table row describes a command within the Door Lock Cluster, specifically the "SetCredentialResponse" command, which is identified by the ID '0x23'. This command is directed from the server to the client, as indicated by the direction "client ⇐ server". The 'Response' field marked as 'N' suggests that this command does not require a response. The 'Conformance' field is marked as 'USR', which, according to the Matter Conformance Interpretation Guide, implies that the command is mandatory if the feature 'USR' (likely representing a specific user-related feature) is supported. If the 'USR' feature is not supported, the conformance of this command is not specified in this entry, suggesting it may not be required.

* The table row describes a command within the Door Lock Cluster, specifically the "GetCredentialStatus" command, which is identified by the ID '0x24'. This command is directed from the client to the server and expects a response in the form of "GetCredentialStatusResponse". The access level for this command is denoted as 'A', which typically refers to a specific access control requirement. The conformance rule for this command is 'USR', indicating that it is mandatory if the feature 'USR' (likely representing a specific user-related feature within the Door Lock Cluster) is supported. If 'USR' is not supported, the conformance of this command is not specified in this entry, implying it may not be required.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "GetCredentialStatusResponse" command, which is identified by the ID '0x25'. This command is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked as 'USR', which, according to the Matter Conformance Interpretation Guide, implies that the command is mandatory if the feature 'USR' is supported. In this context, 'USR' likely refers to a specific feature or condition related to user management or credential status within the Door Lock Cluster. Therefore, the "GetCredentialStatusResponse" command must be implemented if the 'USR' feature is present in the device's configuration.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearCredential" command, which is identified by the ID '0x26'. This command is directed from the client to the server, and it requires a response ('Y' indicates a response is expected). The access control for this command is denoted by 'A T', which typically refers to specific access requirements or roles needed to execute the command. The conformance rule for this command is 'USR', which, according to the Matter Conformance Interpretation Guide, suggests a specific condition or feature code that determines its requirement status. However, 'USR' does not match any basic conformance tags or logical conditions provided in the guide, indicating that it might be a feature code or condition described elsewhere in the documentation. Therefore, the requirement for this command is contingent upon the support of the 'USR' feature or condition, which would need to be referenced in the broader Matter specification documentation for a complete understanding.

* The table row describes a command within the Door Lock Cluster, specifically the "UnboltDoor" command, which is identified by the ID '0x27'. This command is directed from the client to the server and requires a response ('Y'). The access level is marked as 'O T', indicating optional access with some specific conditions or roles (such as "Timed" or "Owner" access, depending on the specification context). The conformance rule for this command is 'UBOLT', which means that the command is mandatory if the feature 'UBOLT' is supported. If 'UBOLT' is not supported, the command is not required. This conformance rule ensures that the "UnboltDoor" command is implemented in devices that support the unbolting feature, maintaining consistency and functionality across compliant devices.

* The table row describes a command within the Door Lock Cluster, specifically the "SetAliroReaderConfig" command, which is identified by the ID '0x28'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level is denoted as 'A T', suggesting specific access requirements. The conformance rule for this command is 'ALIRO', which means that the command is mandatory if the feature 'ALIRO' is supported. If the feature 'ALIRO' is not supported, the command is not required. This conformance condition ensures that the command is implemented only in contexts where the 'ALIRO' feature is applicable.

* The table row describes a command within the Door Lock Cluster, specifically the "ClearAliroReaderConfig" command, which is identified by the ID '0x29'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access control for this command is specified as 'A T', which typically denotes certain access requirements or permissions. The conformance rule 'ALIRO' implies that the command is mandatory if the feature 'ALIRO' is supported. In other words, if a device supports the 'ALIRO' feature, it must implement the "ClearAliroReaderConfig" command. If 'ALIRO' is not supported, the command is not required.

5.2.10.1. LockDoor Command
This command causes the lock device to lock the door. This command includes an optional code for
the lock. The door lock MAY require a PIN depending on the value of the RequirePINForRemoteOp
eration attribute.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes a command identified by 'ID' 0, named 'PINCode', which is of type 'octstr' (octet string). The conformance rule '[COTA & PIN]' indicates that the 'PINCode' command is optional and should be implemented only if both the 'COTA' (presumably a feature related to over-the-air updates) and 'PIN' features are supported by the device. If either or both of these features are not supported, the 'PINCode' command is not required. This conditional optionality allows for flexibility in implementation based on the specific capabilities of the device.

5.2.10.1.1. PINCode Field
If the RequirePINforRemoteOperation attribute is True then PINCode field SHALL be provided and
the door lock SHALL NOT grant access if it is not provided.
If the PINCode field is provided, the door lock SHALL verify PINCode before granting access regard
less of the value of RequirePINForRemoteOperation attribute.
When the PINCode field is provided an invalid PIN will count towards the WrongCodeEntryLimit
and the UserCodeTemporaryDisableTime will be triggered if the WrongCodeEntryLimit is exceeded.
The lock SHALL ignore any attempts to lock/unlock the door until the UserCodeTemporaryDisable
Time expires.
5.2.10.2. UnlockDoor Command
This command causes the lock device to unlock the door. This command includes an optional code
for the lock. The door lock MAY require a code depending on the value of the RequirePINForRemo
teOperation attribute.
If the attribute AutoRelockTime is supported the lock will transition to the locked
NOTE
state when the auto relock time has expired.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "PINCode" command, which is of type "octstr" (octet string). The conformance rule for this command is `[COTA & PIN`, indicating that the command is optional if both the COTA (presumably a feature related to over-the-air updates) and PIN features are supported. This means that the implementation of the "PINCode" command is not mandatory but can be included if the device supports both these features. The use of brackets around the expression `[COTA & PIN` specifies that the optionality is conditional upon the presence of these features.

[COTA & PIN]
5.2.10.2.1. PINCode Field
See PINCode field.
5.2.10.3. UnlockWithTimeout Command
This command causes the lock device to unlock the door with a timeout parameter. After the time
in seconds specified in the timeout field, the lock device will relock itself automatically. This time
out parameter is only temporary for this message transition and overrides the default relock time
as specified in the AutoRelockTime attribute. If the door lock device is not capable of or does not
want to support temporary Relock Timeout, it SHOULD NOT support this optional command.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "Timeout" command, which is identified by the ID '0' and is of the type 'uint16'. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Door Lock Cluster. There are no conditions or dependencies affecting its requirement status, indicating that it must be consistently available as part of the cluster's functionality.

* The table row entry describes a command within the Door Lock Cluster, specifically the "PINCode" command, which is of type "octstr" (octet string). The conformance rule for this command is `[COTA & PIN`, indicating that it is conditionally optional. According to the conformance guide, the presence of brackets around the expression `[COTA & PIN` means that the "PINCode" command is optional if both the COTA (presumably a feature related to over-the-air updates) and PIN features are supported. If these conditions are not met, the command is not required. This allows for flexibility in implementation, depending on the specific features supported by the device.

[COTA & PIN]
5.2.10.3.1. Timeout Field
This field SHALL indicate the timeout in seconds to wait before relocking the door lock. This value
is independent of the AutoRelockTime attribute value.
5.2.10.3.2. PINCode Field
See PINCode field.
5.2.10.4. SetPINCode Command
Set a PIN Code into the lock.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' for this element is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' field is marked as 'M', which means that the 'UserID' element is mandatory. This implies that the 'UserID' command is always required to be implemented in any device or system that supports the Door Lock Cluster, with no conditions or exceptions.

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '1' named 'UserStatus', which is of the type 'UserStatusEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality. The default value for 'UserStatus' is 'OccupiedEnabled'. The 'Conformance' is marked as 'M', which means that the 'UserStatus' command is mandatory and always required to be implemented in this context. This ensures that any implementation of the Door Lock Cluster must include the 'UserStatus' command as a fundamental component.

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes a command identified by the ID '2', named 'UserType', which is of the type 'UserTypeEnum'. The constraint 'all' suggests that this command applies universally within its context. The quality 'X' indicates that this command is explicitly disallowed, meaning it should not be implemented or used. The default value for this command is 'UnrestrictedUser'. The conformance rule 'M' signifies that, despite being disallowed, the 'UserType' command is considered mandatory according to the specification. This means that, under normal circumstances, it would be required, but the quality 'X' takes precedence, rendering it not permissible in practice.

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes a command identified by the ID '3', named 'PIN', which is of the type 'octstr' (octet string). The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'PIN' command is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter IoT specification. There are no conditions or exceptions; the inclusion of this command is obligatory for compliance.

Return status is a global status code or a cluster-specific status code from the Status Codes table and
SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry describes a command named "SUCCESS" within the Door Lock Cluster, specifically under the Commands section. This command indicates that setting a PIN code was successful. The conformance rule for this command is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if we assume a typical conformance scenario, it could be mandatory (M) if the feature it relates to is supported. For example, if the Door Lock Cluster supports PIN code management, the "SUCCESS" command might be mandatory to implement. However, without a specific conformance string provided, this explanation remains speculative. The conformance rule would dictate whether the command must be implemented, is optional, or has any other status based on the conditions outlined in the guide.

* The table row entry pertains to the "FAILURE" command within the Door Lock Cluster, specifically in the context of commands. The summary indicates that this command is used to signify that setting a PIN code has failed. The conformance rule for this command is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string to determine when this command is required, optional, or otherwise. If the conformance string were, for example, "M," it would mean that the "FAILURE" command is mandatory and must always be implemented in devices supporting the Door Lock Cluster. If it were "O," the command would be optional, meaning it could be implemented at the discretion of the device manufacturer. Without the specific conformance string, we cannot definitively describe its requirement status, but the guide provides a framework for interpreting such strings when available.

* The table row entry describes a command named "CONSTRAINT_ERROR" within the Door Lock Cluster, specifically under the Commands section. This command is used to indicate that an attempt to set a PIN code has failed because the User ID requested was out of range. The conformance rule for this command is not explicitly provided in the data snippet, but if we were to interpret it using the Matter Conformance Interpretation Guide, we would need to know the specific conformance string associated with this command. Generally, if a conformance string like "M" were present, it would mean the command is mandatory and must always be implemented. If it were "O," it would be optional, meaning it could be implemented at the discretion of the manufacturer. Without the specific conformance string, we can only describe the command's purpose and potential implications based on the context provided.

* The table row entry pertains to the "Door Lock Cluster" within the "Commands" section, specifically addressing the command named "DUPLICATE." This command is summarized as a failure scenario where setting a PIN code is unsuccessful due to the creation of a duplicate PIN code. The conformance rule for this command is not explicitly provided in the data, but based on the context, it likely indicates a condition or response that the system must handle when attempting to set a PIN code that already exists. If the conformance were specified, it would detail whether this command is mandatory, optional, or subject to specific conditions based on the presence or absence of certain features or states within the system.

5.2.10.4.1. UserID Field
This field SHALL indicate the user ID. The value of the UserID field SHALL be between 0 and the
value of the NumberOfPINUsersSupported attribute.
5.2.10.4.2. UserStatus Field
This field SHALL indicate the user status. Only the values 1 (Occupied/Enabled) and 3 (Occu
pied/Disabled) are allowed for UserStatus.
5.2.10.5. GetPINCode Command
Retrieve a PIN Code.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' for this element is marked as 'desc', indicating that the specific constraints are detailed elsewhere in the documentation. The 'Conformance' for 'UserID' is marked as 'M', meaning that this element is mandatory. This implies that the 'UserID' command must always be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.5.1. UserID Field
This field SHALL indicate the user ID. The value of the UserID field SHALL be between 0 and the
value of the NumberOfPINUsersSupported attribute.
5.2.10.6. GetPINCodeResponse Command
Returns the PIN for the specified user ID.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster's commands, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' field is marked as 'M', meaning that the 'UserID' element is mandatory. This implies that the 'UserID' command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserStatus" command, which is of the type "UserStatusEnum." The "Constraint" field is marked as "desc," indicating that the constraints for this command are detailed elsewhere in the documentation. The "Quality" is marked as "X," meaning that this command is explicitly disallowed in certain contexts, though the specifics are not provided here. The "Default" value for this command is "Available." The "Conformance" field is marked with "M," indicating that the "UserStatus" command is mandatory. This means that in any implementation of the Door Lock Cluster, the "UserStatus" command must always be included and supported, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'UserType' command, which is of the type 'UserTypeEnum'. The 'Constraint' is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Quality' is marked as 'X', meaning this command is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', which signifies that the 'UserType' command is mandatory. This means that within the context of the Door Lock Cluster, the 'UserType' command must always be implemented according to the Matter specification.

* The table row describes a command within the Door Lock Cluster, specifically the 'PINCode' command. This command is identified by the ID '3' and is of the type 'octstr', which indicates it is an octet string. The 'Quality' is marked as 'X', meaning that the use of this command is explicitly disallowed in the current specification. The 'Default' value is specified as 'empty', indicating that if the command were to be used, it would default to an empty value. The 'Conformance' is marked as 'M', which means that under normal circumstances, this command would be mandatory. However, given the 'Quality' is 'X', the command is not permitted for use despite its mandatory conformance status.

If the requested UserID is valid and the Code doesn’t exist, Get RFID Code Response SHALL have the
following format:
UserID = requested User ID
UserStatus = 0 (Available)
UserType = Null (Not supported)
PINCode = 0 (zero length)
If the requested UserID is invalid, send Default Response with an error status. The error status
SHALL be equal to CONSTRAINT_ERROR when User_ID is less than the max number of users sup
ported, and NOT_FOUND if greater than or equal to the max number of users supported.
5.2.10.7. ClearPINCode Command
Clear a PIN code or all PIN codes.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'PINSlotIndex' command. This command has an ID of '0' and is of type 'uint16', which indicates it is a 16-bit unsigned integer. The constraint for this command specifies that its value must be between 1 and the number of PIN users supported by the device, or it can be the special value 0xFFFE. The conformance rule for 'PINSlotIndex' is marked as 'M', meaning this command is mandatory. It is always required to be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

For each PIN Code cleared whose user doesn’t have a RFID Code or other credential type, then cor
responding user record’s UserStatus value SHALL be set to Available, and UserType value SHALL be
set to UnrestrictedUser and all schedules SHALL be cleared.
5.2.10.7.1. PINSlotIndex Field
This field SHALL specify a valid PIN code slot index or 0xFFFE to indicate all PIN code slots SHALL
be cleared.
5.2.10.8. ClearAllPINCodes Command
Clear out all PINs on the lock.
On the server, the clear all PIN codes command SHOULD have the same effect as the
NOTE ClearPINCode command with respect to the setting of user status, user type and
schedules.
5.2.10.9. SetUserStatus Command
Set the status of a user ID.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', which means that the 'UserID' command is mandatory. This implies that the 'UserID' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Door Lock Cluster.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'UserStatus' command, which is of the type 'UserStatusEnum'. The 'Constraint' for this command is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' for this command is labeled as 'M', meaning it is mandatory. This implies that the 'UserStatus' command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.9.1. UserID Field
This field SHALL indicate the user ID. The value of the UserID field SHALL be between 0 and the
value of the NumberOfPINUsersSupported attribute.
5.2.10.9.2. UserStatus Field
UserStatus value of Available is not allowed. In order to clear a user id, the ClearUser Command
SHALL be used. For user status value please refer to UserStatusEnum.
5.2.10.10. GetUserStatus Command
Get the status of a user.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', meaning that the 'UserID' element is mandatory. This implies that the 'UserID' must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster.

5.2.10.10.1. UserID Field
This field SHALL indicate the user ID. The value of the UserID field SHALL be between 0 and the
value of the NumberOfPINUsersSupported attribute.
5.2.10.11. GetUserStatusResponse Command
Returns the user status for the specified user ID.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, there is an entry for a command identified by 'ID' 0, named 'UserID', which is of type 'uint16'. The 'Constraint' for this entry is described elsewhere in the documentation, as indicated by 'desc'. The 'Conformance' for this command is marked as 'M', meaning it is mandatory. This implies that the 'UserID' command is a required element in the Door Lock Cluster and must be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '1' named 'UserStatus', which is of the type 'UserStatusEnum' and applies to all constraints. The conformance rule for 'UserStatus' is marked as 'M', indicating that this command is mandatory. This means that the 'UserStatus' command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.11.1. UserID Field
This field SHALL indicate the user ID provided in the request.
5.2.10.11.2. UserStatus Field
This field SHALL indicate the current status of the requested user ID.
5.2.10.12. SetWeekDaySchedule Command
Set a weekly repeating schedule for a specified user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'WeekDayIndex' command. This command is identified by the ID '0' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The value of 'WeekDayIndex' is constrained to be between 1 and the value of 'NumberOfWeekDaySchedulesSupportedPerUser', which indicates the range of valid indices for weekday schedules. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'WeekDayIndex' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '1' named 'UserIndex'. This element is of type 'uint16' and is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. The conformance rule for 'UserIndex' is marked as 'M', which means it is a Mandatory element. This indicates that the 'UserIndex' command must always be implemented and supported in any device or application that utilizes the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '2', named 'DaysMask', which is of the type 'DaysMaskBitmap'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'DaysMask' command is a required component of the Door Lock Cluster and must be implemented in any device or system that supports this cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '3' named 'StartHour'. This element is of type 'uint8' and has a constraint that its maximum value is 23. The conformance rule for 'StartHour' is marked as 'M', which stands for Mandatory. This means that the 'StartHour' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster's Commands section, the table row describes an element with the ID '4', named 'StartMinute', which is of type 'uint8' and has a constraint that its value must not exceed 59. The conformance rule for 'StartMinute' is marked as 'M', indicating that this element is mandatory. This means that the 'StartMinute' command must always be implemented and supported in any device or system that adheres to the Matter specification for the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster's commands, the table row describes an element with the ID '5', named 'EndHour', which is of type 'uint8' and has a constraint of a maximum value of 23. The conformance rule for 'EndHour' is marked as 'M', indicating that this element is mandatory. This means that the 'EndHour' command must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster. The mandatory status ensures that this command is consistently available across all implementations, facilitating interoperability and standard functionality.

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '6' named 'EndMinute'. This element is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 59. The conformance rule for 'EndMinute' is marked as 'M', which stands for Mandatory. This indicates that the 'EndMinute' element is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

The associated UserType MAY be changed to ScheduleRestrictedUser by the lock when a Week Day
schedule is set.
Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry for the Door Lock Cluster under the Commands section describes a command named "SUCCESS," which indicates that setting a Week Day schedule was successful. The conformance rule for this command is not explicitly provided in the data you shared. However, based on the Matter Conformance Interpretation Guide, if a conformance string were provided, it would specify when this command is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were "M," it would mean that the "SUCCESS" command is always required in the implementation of the Door Lock Cluster. If it were "O," the command would be optional, meaning it could be included at the implementer's discretion without any dependencies. If further details or a specific conformance string were available, it would be interpreted according to the rules outlined in the guide.

* The table row entry for the Door Lock Cluster under the Commands section describes a command named "FAILURE," which is used to indicate that an unexpected internal error occurred while setting a Week Day schedule. The conformance rule for this command is not explicitly provided in the data, which suggests that additional context or documentation is needed to determine its conformance status. Typically, such a command might be associated with error handling and could be optional or mandatory depending on the specific implementation requirements of the Door Lock Cluster. Without a specific conformance string, it is assumed that the command's inclusion is determined by the broader context of the cluster's error management strategy.

* The table row describes a command named "INVALID_COMMAND" within the Door Lock Cluster's Commands section. This command is used to indicate that one or more fields in a request violate constraints or are invalid. The conformance for this command is not explicitly provided in the data, suggesting that additional context or documentation is needed to determine its status. Typically, such commands might be described elsewhere in the specification, especially if their conformance is complex or conditional. Therefore, the conformance might be categorized under "desc," meaning the specifics of when this command is required or optional are detailed in another part of the documentation.

Some unexpected internal error occurred setting
is
5.2.10.12.1. WeekDayIndex Field
This field SHALL indicate the index of the Week Day schedule.
5.2.10.12.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.12.3. DaysMask Field
This field SHALL indicate which week days the schedule is active.
5.2.10.12.4. StartHour Field
This field SHALL indicate the starting hour for the Week Day schedule.
5.2.10.12.5. StartMinute Field
This field SHALL indicate the starting minute for the Week Day schedule.
5.2.10.12.6. EndHour Field
This field SHALL indicate the ending hour for the Week Day schedule. EndHour SHALL be equal to
or greater than StartHour.
5.2.10.12.7. EndMinute Field
This field SHALL indicate the ending minute for the Week Day schedule. If EndHour is equal to Star
tHour then EndMinute SHALL be greater than StartMinute.
If the EndHour is equal to 23 and the EndMinute is equal to 59 the Lock SHALL grant access to the
user up until 23:59:59.
5.2.10.13. GetWeekDaySchedule Command
Retrieve the specific weekly schedule for the specific user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'WeekDayIndex' command. This command is identified by the ID '0' and is of type 'uint8'. The value for this command must fall within the constraint range of 1 to the value specified by 'NumberOfWeekDaySchedulesSupportedPerUser'. The conformance rule for 'WeekDayIndex' is marked as 'M', which means this command is mandatory. It is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically focusing on the 'UserIndex' element. This element is identified by the ID '1' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'UserIndex' is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported', which indicates it must fall within this range to be valid. The conformance for 'UserIndex' is marked as 'M', which stands for Mandatory. This means that the 'UserIndex' command is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.14. GetWeekDayScheduleResponse Command
Returns the weekly repeating schedule data for the specified schedule index.

_Table parsed from section 'Commands':_

* The table row pertains to the "WeekDayIndex" command within the Door Lock Cluster's Commands section. This command is identified by the ID '0' and is of type 'uint8'. It has a constraint that limits its values from 1 to the number specified by the "NumberOfWeekDaySchedulesSupportedPerUser" attribute. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the "WeekDayIndex" command must always be implemented and supported in any device or application that adheres to the Matter specification for the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, the table row describes a command with the ID '1' named 'UserIndex', which is of type 'uint16'. The 'UserIndex' command is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. According to the conformance rule 'M', this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Door Lock Cluster. This ensures that the 'UserIndex' command is consistently available across all implementations, facilitating uniform functionality and interoperability within the Matter IoT specification.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster's Commands, the table entry describes an element with the ID '2' named 'Status', which is of type 'enum8'. The constraint for this element is described elsewhere in the documentation, and its default value is 'SUCCESS'. The conformance rule for this element is marked as 'M', which means that the 'Status' command is mandatory. This indicates that the 'Status' command must always be implemented and supported in any device or application that utilizes the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Commands section, the entry with ID '3' is named 'DaysMask' and is of the type 'DaysMaskBitmap'. According to the conformance rule 'O', this element is classified as Optional. This means that the 'DaysMask' command is not required to be implemented in all devices supporting the Door Lock Cluster, and there are no specific dependencies or conditions that mandate its inclusion. Devices can choose to implement this command based on their design or functionality requirements, but it is not a compulsory feature according to the current Matter specification.

* The table row describes a command named "StartHour" within the Door Lock Cluster, specifically in the Commands section. This command has an ID of '4' and is of type 'uint8', with a constraint that its maximum value can be 23. The conformance rule for "StartHour" is marked as 'O', which means that this command is optional. It is not required for implementation and does not have any dependencies or conditions that affect its optional status. Implementers of the Door Lock Cluster can choose to include this command, but it is not mandatory for compliance with the Matter specification.

* The table row describes a command within the Door Lock Cluster, specifically the 'StartMinute' command. This command is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 59. The conformance rule for 'StartMinute' is marked as 'O', which stands for Optional. This means that the inclusion of the 'StartMinute' command is not required for compliance with the Matter specification; it can be implemented at the discretion of the device manufacturer without any dependencies or conditions.

* The table row describes a command within the Door Lock Cluster, specifically the 'EndHour' command, which is identified by the ID '6'. This command is of type 'uint8' and has a constraint that limits its maximum value to 23, likely representing the hours in a day. The conformance rule for 'EndHour' is marked as 'O', which means that this command is optional. It is not required for implementation and has no dependencies on other features or conditions. Implementers have the discretion to include or exclude this command based on their specific needs or preferences without affecting compliance with the Matter specification.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '7' named 'EndMinute'. This element is of type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 59. The conformance rule for 'EndMinute' is 'O', indicating that this element is Optional. This means that the 'EndMinute' command is not required to be implemented in devices supporting the Door Lock Cluster, and there are no dependencies or conditions that alter its optional status.

5.2.10.14.1. WeekDayIndex Field
This field SHALL indicate the index of the Week Day schedule.
5.2.10.14.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.14.3. Status Field
Status SHALL be one of the following values:
• SUCCESS if both WeekDayIndex and UserIndex are valid and there is a corresponding schedule
entry.
• INVALID_COMMAND if either WeekDayIndex and/or UserIndex values are not within valid
range
• NOT_FOUND if no corresponding schedule entry found for WeekDayIndex.
• NOT_FOUND if no corresponding user entry found for UserIndex.
If this field is SUCCESS, the optional fields for this command SHALL be present. For other (error)
status values, only the fields up to the status field SHALL be present.
5.2.10.14.4. StartHour Field
This field SHALL indicate the starting hour for the Week Day schedule.
5.2.10.14.5. StartMinute Field
This field SHALL indicate the starting minute for the Week Day schedule.
5.2.10.14.6. EndHour Field
This field SHALL indicate the ending hour for the Week Day schedule. EndHour SHALL be equal to
or greater than StartHour.
5.2.10.14.7. EndMinute Field
This field SHALL indicate the ending minute for the Week Day schedule. If EndHour is equal to Star
tHour then EndMinute SHALL be greater than StartMinute.
5.2.10.15. ClearWeekDaySchedule Command
Clear the specific weekly schedule or all weekly schedules for the specific user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "WeekDayIndex" command. This command is identified by the ID '0' and is of type 'uint8'. The value of this command is constrained to be between 1 and the value defined by "NumberOfWeekDaySchedulesSupportedPerUser," with an additional special value of 0xFE. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "WeekDayIndex" command must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '1' named 'UserIndex'. This element is of type 'uint16' and is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. The conformance rule for 'UserIndex' is marked as 'M', which means it is a Mandatory element. This indicates that the 'UserIndex' must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster. There are no conditions or dependencies affecting its mandatory status, making it an essential component of the command structure within this cluster.

Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row describes a command named "SUCCESS" within the Door Lock Cluster's Commands section. This command indicates that the action of clearing a requested WeekDaySchedule was successful. The conformance rule for this command is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if it were to follow a typical pattern, it might be mandatory (M) if it is a standard response to a command execution. However, without a specific conformance string given, we can only infer that this command is likely a standard part of the Door Lock Cluster's functionality, expected to be implemented to confirm successful schedule clearing operations.

* The table row describes a command named "FAILURE" within the Door Lock Cluster, specifically under the Commands section. This command is associated with the occurrence of an unexpected internal error when attempting to clear a Week Day schedule. The conformance rule for this command is not explicitly provided in the data given, so we cannot determine its exact requirement status (e.g., Mandatory, Optional, etc.) based on the information available. Typically, such a command might be used to signal an error condition to the user or system when a specific operation fails, but without the conformance string, we cannot specify its necessity or conditions under which it should be implemented.

* In the Door Lock Cluster, under the Commands section, the entry for 'INVALID_COMMAND' indicates a command that is used when one or more fields violate constraints or are invalid. The conformance rule for this entry is not explicitly provided in the table row data. However, based on the Matter Conformance Interpretation Guide, if a conformance string were provided, it would dictate the conditions under which this command is required, optional, provisional, deprecated, or disallowed. Without a specific conformance string, we cannot determine its exact status, but typically, such a command would be essential for error handling in a robust system, potentially making it a candidate for mandatory implementation.

5.2.10.15.1. WeekDayIndex Field
This field SHALL indicate the Week Day schedule index to clear or 0xFE to clear all Week Day
schedules for the specified user.
5.2.10.15.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.16. SetYearDaySchedule Command
Set a time-specific schedule ID for a specified user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "YearDayIndex" command. This command is identified by the ID '0' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The value of this command is constrained to be between 1 and the number specified by the attribute "NumberOfYearDaySchedulesSupportedPerUser," which indicates the maximum number of year-day schedules that can be supported per user. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "YearDayIndex" command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserIndex" command. This command is identified by the ID '1' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The value of "UserIndex" must fall within the range from 1 to the value specified by "NumberOfTotalUsersSupported", which is a constraint ensuring that the index is valid within the total number of users the door lock can support. The conformance rule for "UserIndex" is marked as 'M', indicating that this command is mandatory. This means that the "UserIndex" command must always be implemented and supported in any device or application that uses the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes an element with the ID '2' named 'LocalStartTime'. This element is of the type 'epoch-s', which indicates it is represented as an epoch time in seconds. The constraint 'all' suggests that this element applies universally within its context. The conformance rule 'M' signifies that the 'LocalStartTime' command is mandatory, meaning it is always required to be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* The table row describes a command within the Door Lock Cluster, specifically identified as 'LocalEndTime' with an ID of '3'. This command is of the type 'epoch-s', indicating it uses epoch seconds as its data format. The 'Constraint' field is marked as 'all', suggesting that there are no specific limitations or conditions on its use across different implementations. The 'Conformance' field is marked as 'M', which means that the 'LocalEndTime' command is mandatory. This implies that any implementation of the Door Lock Cluster must include this command, as it is a required element of the specification without any conditional or optional status.

The associated UserType MAY be changed to ScheduleRestrictedUser by the lock when a Year Day
schedule is set.
Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry pertains to the Door Lock Cluster within the Commands section, specifically focusing on the command named "SUCCESS," which indicates that setting a Year Day schedule was successful. The conformance rule for this command is not explicitly provided in the data snippet, but based on the context and typical usage, it likely follows a standard pattern for success responses in command protocols. Generally, such a command would be considered mandatory (M) if the feature it supports is implemented, ensuring that devices can communicate successful operations. If the conformance were to include conditional expressions or other tags, it would specify under what circumstances the command is required or optional. Without additional conformance details, it is assumed that the "SUCCESS" command is a fundamental part of the Door Lock Cluster's command set, ensuring interoperability and consistent feedback across devices implementing this cluster.

* The table row entry pertains to the "FAILURE" command within the Door Lock Cluster's Commands section. This command is used to indicate that an unexpected internal error occurred while setting a Year Day schedule. The conformance rule for this command is not explicitly provided in the data, but based on the context and typical usage in Matter specifications, it would likely be categorized under a basic conformance tag such as "M" for Mandatory, meaning it is always required, or "O" for Optional, indicating it is not required and has no dependencies. Without a specific conformance string, we assume the command's inclusion is essential for handling error scenarios related to scheduling within the Door Lock Cluster.

* The table row entry for the Door Lock Cluster under the Commands section describes a command named "INVALID_COMMAND," which is used when one or more fields violate constraints or are invalid. The conformance rule for this command is not explicitly provided in the data, but based on the context and typical usage of such commands, it is likely intended to handle error conditions. In the absence of a specific conformance string, it is reasonable to assume that the command might be optional or described elsewhere in the documentation. This means that its implementation could depend on additional conditions or requirements not detailed in the provided data.

Some unexpected internal error occurred setting
5.2.10.16.1. YearDayIndex Field
This field SHALL indicate the index of the Year Day schedule.
5.2.10.16.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.16.3. LocalStartTime Field
This field SHALL indicate the starting time for the Year Day schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
5.2.10.16.4. LocalEndTime Field
This field SHALL indicate the ending time for the Year Day schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
LocalEndTime SHALL be greater than LocalStartTime.
5.2.10.17. GetYearDaySchedule Command
Retrieve the specific year day schedule for the specific schedule and user indexes.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '0' named 'YearDayIndex'. This element is of the type 'uint8' and is constrained to values ranging from 1 to the value specified by 'NumberOfYearDaySchedulesSupportedPerUser'. The conformance rule for 'YearDayIndex' is marked as 'M', which means it is a Mandatory element. This indicates that the 'YearDayIndex' must always be implemented and supported in any device or application that conforms to this specification, without any conditions or exceptions.

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '1' named 'UserIndex'. This element is of type 'uint16' and is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. The conformance rule for 'UserIndex' is marked as 'M', which stands for Mandatory. This means that the 'UserIndex' element is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.18. GetYearDayScheduleResponse Command
Returns the year day schedule data for the specified schedule and user indexes.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'YearDayIndex', which is of type 'uint8'. The 'YearDayIndex' is constrained to values ranging from 1 to the number specified by 'NumberOfYearDaySchedulesSupportedPerUser'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'YearDayIndex' command must always be implemented and supported in any device or application that adheres to this specification for the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'UserIndex' command. This command is identified by the ID '1' and is of the type 'uint16', which means it is a 16-bit unsigned integer. The value of 'UserIndex' is constrained to be between 1 and the 'NumberOfTotalUsersSupported', indicating that it refers to a specific user within the range of users supported by the door lock. The conformance rule for 'UserIndex' is 'M', which stands for Mandatory. This means that the 'UserIndex' command is always required to be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically identified by the ID '2' and named 'Status'. This command is of type 'enum8', which indicates it uses an 8-bit enumeration to represent its values. The 'Constraint' field is marked as 'desc', suggesting that the constraints for this command are detailed elsewhere in the documentation. The default value for this command is 'SUCCESS'. The 'Conformance' field is marked with 'M', which means that this command is mandatory. It is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, within the Commands section, there is an entry for a command named "LocalStartTime" with an ID of '2'. This command is of the type 'epoch-s', which indicates it uses epoch seconds as its data format. The constraint 'all' suggests that this command applies universally within its context. The conformance rule for "LocalStartTime" is marked as 'O', meaning it is optional. This indicates that the implementation of this command is not required and has no dependencies on other features or conditions. It is up to the implementer to decide whether to include this command in their device or application.

* In the Door Lock Cluster, under the Commands section, the entry for 'LocalEndTime' with ID '3' is of type 'epoch-s' and applies to all constraints. The conformance rule for 'LocalEndTime' is marked as 'O', which means this command is optional. It is not required for implementation and does not depend on any other features or conditions. Implementers have the flexibility to include or exclude this command based on their specific needs or preferences without affecting compliance with the Matter specification.

5.2.10.18.1. YearDayIndex Field
This field SHALL indicate the index of the Year Day schedule.
5.2.10.18.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.18.3. Status Field
Status SHALL be one of the following values:
• SUCCESS if both YearDayIndex and UserIndex are valid and there is a corresponding schedule
entry.
• INVALID_COMMAND if either YearDayIndex and/or UserIndex values are not within valid range
• NOT_FOUND if no corresponding schedule entry found for YearDayIndex.
• NOT_FOUND if no corresponding user entry found for UserIndex.
If this field is SUCCESS, the optional fields for this command SHALL be present. For other (error)
status values, only the fields up to the status field SHALL be present.
5.2.10.18.4. LocalStartTime Field
This field SHALL indicate the starting time for the Year Day schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
This SHALL be null if the schedule is not set for the YearDayIndex and UserIndex provided.
5.2.10.18.5. LocalEndTime Field
This field SHALL indicate the ending time for the Year Day schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
LocalEndTime SHALL be greater than LocalStartTime. This SHALL be null if the schedule is not set
for the YearDayIndex and UserIndex provided.
5.2.10.19. ClearYearDaySchedule Command
Clears the specific year day schedule or all year day schedules for the specific user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "YearDayIndex" command. This command is identified by the ID '0' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The constraint for this command specifies that its value must be between 1 and the value of "NumberOfYearDaySchedulesSupportedPerUser," or it can be 0xFE. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "YearDayIndex" command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'UserIndex' command. This command is identified by the ID '1' and is of type 'uint16'. It has a constraint that its value must be between 1 and the 'NumberOfTotalUsersSupported', indicating it is used to reference a specific user within the total number of users that the door lock can support. The conformance rule for 'UserIndex' is marked as 'M', which stands for Mandatory. This means that the 'UserIndex' command is always required to be implemented in any device that supports the Door Lock Cluster, with no conditions or exceptions.

Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry pertains to the "SUCCESS" command within the Door Lock Cluster, specifically under the Commands section. This command indicates that the action of clearing a requested YearDaySchedule has been successfully completed. The conformance rule for this command is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if it were to be described, it would detail the conditions under which this command is required, optional, or otherwise. For instance, if the conformance were "M," it would mean that the SUCCESS command is always mandatory for devices implementing the Door Lock Cluster. If it were "O," it would be optional, allowing manufacturers the choice to implement it based on their device's capabilities or intended use cases. Without the specific conformance string, we can only infer that the command's inclusion is significant for the successful operation of the YearDaySchedule feature within the Door Lock Cluster.

_Table parsed from section 'Commands':_

* The table row describes a command named "FAILURE" within the Door Lock Cluster's Commands section. This command is used to indicate that an unexpected internal error occurred while attempting to clear a Year Day schedule. The conformance rule for this command is not explicitly provided in the data you shared, but if we assume a typical conformance scenario, it might be described as "M" (Mandatory), "O" (Optional), or another conformance expression based on the context of the Door Lock Cluster. Without the specific conformance string, we cannot definitively state its requirement status. However, if it were "M," it would mean the command must always be implemented. If "O," it would be optional and not required unless specified by other conditions. If a complex expression were provided, it would determine the conditions under which the command is required or optional, following the rules outlined in the Matter Conformance Interpretation Guide.

* The table row describes a command named "INVALID_COMMAND" within the Door Lock Cluster, specifically under the Commands section. This command is used when one or more fields violate constraints or are invalid. The conformance rule for this command is not explicitly provided in the data given, but based on the Matter Conformance Interpretation Guide, it would typically specify whether this command is mandatory, optional, provisional, deprecated, or disallowed. Since the conformance string is missing, we cannot determine its exact requirement status. However, if it were present, it would indicate the conditions under which this command must be implemented or can be omitted, using the logical conditions and expressions outlined in the guide.

5.2.10.19.1. YearDayIndex Field
This field SHALL indicate the Year Day schedule index to clear or 0xFE to clear all Year Day sched
ules for the specified user.
5.2.10.19.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.20. SetHolidaySchedule Command
Set the holiday Schedule by specifying local start time and local end time with respect to any Lock
Operating Mode.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically identified by the ID '0' and named 'HolidayIndex'. This command is of the type 'uint8' and is constrained to values ranging from 1 to the number of holiday schedules supported by the device. The conformance rule for 'HolidayIndex' is marked as 'M', which means it is mandatory. This indicates that the 'HolidayIndex' command must always be implemented and supported by any device that includes the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'LocalStartTime' command. This command is identified by the ID '1' and is of the type 'epoch-s', which likely refers to a timestamp format. The 'Constraint' field indicates that this command applies to all instances of the Door Lock Cluster. The 'Conformance' field is marked with 'M', meaning that the 'LocalStartTime' command is mandatory. This implies that every implementation of the Door Lock Cluster must include this command without exception.

* In the context of the Door Lock Cluster, specifically within the Commands section, the table entry for 'LocalEndTime' with ID '2' and type 'epoch-s' is described. The 'Constraint' is listed as 'all', indicating that this command applies universally without specific limitations. The 'Conformance' for 'LocalEndTime' is marked as 'M', which means it is a Mandatory element. This implies that the 'LocalEndTime' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* The table row describes a command within the Door Lock Cluster, specifically the "OperatingMode" command, which is of the type "OperatingModeEnum" and applies to all constraints. The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "OperatingMode" command must always be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry pertains to the "SUCCESS" command within the Door Lock Cluster's Commands section, which indicates that setting a holiday schedule was successful. The conformance rule for this command is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, we can infer that if a conformance string were present, it would dictate the conditions under which this command is required or optional. For instance, if the conformance were "M," the command would be mandatory, meaning it must always be implemented. If it were "O," it would be optional, allowing for implementation at the developer's discretion without any dependencies. If the conformance were more complex, involving logical conditions or conditional expressions, it would specify under what circumstances the command becomes mandatory or optional based on the support of certain features or conditions. Without a specific conformance string, the default assumption would be that the command's implementation is subject to the overall requirements of the Door Lock Cluster as defined elsewhere in the Matter specification

* In the context of the Door Lock Cluster's Commands section, the table row entry for the command named "FAILURE" indicates that this command is used to signal that an unexpected internal error occurred while setting a Holiday schedule. The conformance rule for this entry is not explicitly provided in the data, but if we were to interpret it using the Matter Conformance Interpretation Guide, we would need additional information from the 'Conformance' column to determine whether this command is mandatory, optional, provisional, deprecated, disallowed, or described elsewhere. Without a specific conformance string, we cannot definitively state the requirement level for implementing this command, but it is likely a crucial part of error handling within the Door Lock Cluster.

* The table row describes a command named "INVALID_COMMAND" within the Door Lock Cluster's Commands section. This command is used to indicate that one or more fields in a request violate constraints or are invalid. The conformance rule for this command is not explicitly provided in the row data, which suggests that additional context or documentation is needed to determine its conformance status. Typically, such a command would be used to handle error conditions, but without a specific conformance string, we cannot definitively state whether it is mandatory, optional, or subject to other conditions. Therefore, it is essential to refer to the broader documentation or specification for further details on its implementation requirements.

5.2.10.20.1. HolidayIndex Field
This field SHALL indicate the index of the Holiday schedule.
5.2.10.20.2. LocalStartTime Field
This field SHALL indicate the starting time for the Holiday Day schedule in Epoch Time in Seconds
with local time offset based on the local timezone and DST offset on the day represented by the
value.
5.2.10.20.3. LocalEndTime Field
This field SHALL indicate the ending time for the Holiday Day schedule in Epoch Time in Seconds
with local time offset based on the local timezone and DST offset on the day represented by the
value. LocalEndTime SHALL be greater than LocalStartTime.
5.2.10.20.4. OperatingMode Field
This field SHALL indicate the operating mode to use during this Holiday schedule start/end time.
5.2.10.21. GetHolidaySchedule Command
Get the holiday schedule for the specified index.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command with the ID '0' named 'HolidayIndex', which is of type 'uint8'. The 'HolidayIndex' command is constrained to values ranging from 1 to the number of holiday schedules supported by the device. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'HolidayIndex' command is always required to be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.22. GetHolidayScheduleResponse Command
Returns the Holiday Schedule Entry for the specified Holiday ID.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command with the ID '0' named 'HolidayIndex', which is of type 'uint8'. The value of 'HolidayIndex' is constrained to be between 1 and the number specified by 'NumberOfHolidaySchedulesSupported'. The conformance rule for this command is marked as 'M', indicating that it is mandatory. This means that the 'HolidayIndex' command must always be implemented and supported in any device or application that conforms to the Matter specification for the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

* The table row describes a command within the Door Lock Cluster, specifically identified by the ID '1' and named 'Status'. This command is of type 'enum8', indicating it uses an 8-bit enumeration to represent its values. The 'Constraint' is marked as 'desc', suggesting that the constraints for this command are detailed elsewhere in the documentation. The default value for this command is 'SUCCESS'. The 'Conformance' field is marked as 'M', which means this command is mandatory. It is always required to be implemented in any device or application that supports the Door Lock Cluster, with no conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically identified as 'LocalStartTime' with an ID of '2'. This command is of the type 'epoch-s', which likely refers to a time format based on seconds since a specific epoch. The 'Constraint' field is marked as 'all', indicating that this command applies universally within its context. The 'Quality' is marked as 'X', meaning this command is explicitly disallowed in the current specification. The 'Conformance' is labeled as 'O', signifying that the 'LocalStartTime' command is optional. This means that while it is not required for compliance with the Matter specification, it can be implemented at the discretion of the device manufacturer without any dependencies or conditions.

* In the context of the Door Lock Cluster's commands, the table row describes an element with the ID '3' named 'Local End Time', which is of the type 'epoch-s' and applies to all constraints. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'O', meaning that the 'Local End Time' command is optional. This implies that while the command can be implemented, it is not required and has no dependencies on other features or conditions within the Matter specification.

* The table row describes a command within the Door Lock Cluster, specifically the "OperatingMode" command, which is of the type "OperatingModeEnum" and applies to all constraints. The quality of this command is marked as "X," indicating that it is explicitly disallowed. The conformance rule for this command is "O," meaning that it is optional. In this context, "optional" signifies that the "OperatingMode" command is not required to be implemented and has no dependencies that would necessitate its inclusion in a device's functionality. However, given the quality "X," it is important to note that despite being optional, this command is explicitly not allowed to be implemented in the current specification.

5.2.10.22.1. HolidayIndex Field
This field SHALL indicate the index of the Holiday schedule.
5.2.10.22.2. Status Field
Status SHALL be one of the following values:
• FAILURE if the attribute NumberOfHolidaySchedulesSupported is zero.
• SUCCESS if the HolidayIndex is valid and there is a corresponding schedule entry.
• INVALID_COMMAND if the HolidayIndex is not within valid range
• NOT_FOUND if the HolidayIndex is within the valid range, however, there is not corresponding
schedule entry found.
If this field is SUCCESS, the optional fields for this command SHALL be present. For other (error)
status values, only the fields up to the status field SHALL be present.
5.2.10.22.3. LocalStartTime Field
This field SHALL indicate the starting time for the Holiday schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
This SHALL be null if the schedule is not set for the HolidayIndex provided.
5.2.10.22.4. LocalEndTime Field
This field SHALL indicate the ending time for the Holiday schedule in Epoch Time in Seconds with
local time offset based on the local timezone and DST offset on the day represented by the value.
LocalEndTime SHALL be greater than LocalStartTime. This SHALL be null if the schedule is not set
for the HolidayIndex provided.
5.2.10.22.5. OperatingMode Field
This field SHALL indicate the operating mode to use during this Holiday schedule start/end time.
This SHALL be null if the schedule is not set for the HolidayIndex provided.
5.2.10.23. ClearHolidaySchedule Command
Clears the holiday schedule or all holiday schedules.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '0' named 'HolidayIndex'. This element is of type 'uint8' and has a constraint that specifies its value must be between 1 and the number of holiday schedules supported, or it can be 0xFE. The conformance rule for 'HolidayIndex' is marked as 'M', which means it is mandatory. This indicates that the 'HolidayIndex' command must always be implemented and supported in any device using the Door Lock Cluster, without any conditions or exceptions.

5.2.10.23.1. HolidayIndex Field
This field SHALL indicate the Holiday schedule index to clear or 0xFE to clear all Holiday schedules.
5.2.10.24. SetUserType Command
Set the user type for a specified user.
For user type value please refer to User Type Value.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically identified as 'UserID'. This command is of type 'uint16', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'UserID' is marked as 'M', meaning it is a Mandatory element. This indicates that the 'UserID' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserType" command, which is of the type "UserTypeEnum" and applies to all constraints. The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "UserType" command is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry pertains to the "SUCCESS" command within the Door Lock Cluster, specifically under the Commands section. This command indicates that the action of setting a user type was successful. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance string using the Matter Conformance Interpretation Guide, it would specify under what conditions this command is required, optional, or otherwise. For instance, if the conformance were "M," it would mean the "SUCCESS" command is always mandatory for devices implementing this cluster. If it were "O," it would be optional, meaning devices could implement it but are not required to. Without the specific conformance string, we cannot determine the exact requirements for this command, but it plays a crucial role in confirming successful operations within the Door Lock Cluster.

* The table row describes a command named "FAILURE" within the Door Lock Cluster, specifically under the Commands section. This command is used to indicate that an unexpected internal error occurred while setting the User Type. The conformance rule for this command is not explicitly provided in the data, which suggests that additional context or documentation is needed to determine its conformance status. Without a specific conformance string, it is unclear whether this command is mandatory, optional, provisional, deprecated, or disallowed. Therefore, further reference to the Matter specification documentation would be necessary to understand the exact requirements or recommendations for implementing this command.

* The table row entry for the 'INVALID_COMMAND' within the Door Lock Cluster's Commands section describes a command that is used when one or more fields violate constraints or are invalid, specifically when the door lock cannot transition from a restricted to an unrestricted user state, such as needing to clear schedules before switching. The conformance rule for this entry is not explicitly provided in the data given, but if it were, it would dictate the conditions under which this command is required, optional, or otherwise specified according to the Matter Conformance Interpretation Guide. Without a specific conformance string, we cannot determine its mandatory or optional status, but typically, such a command would be implemented to handle error states or invalid operations within the door lock's functionality.

Some unexpected internal error occurred setting
is
Door lock is unable to switch from restricted to
unrestricted user (e.g. need to clear schedules to
5.2.10.24.1. UserID Field
This field SHALL indicate the user ID.
5.2.10.24.2. UserType Field
This field SHALL indicate the user type.
5.2.10.25. GetUserType Command
Retrieve the user type for a specific user.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'UserID' command. This command has an identifier of '0' and is of type 'uint16'. The 'Constraint' for this command is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' for this command is labeled as 'M', which means it is mandatory. This implies that the 'UserID' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.26. GetUserTypeResponse Command
Returns the user type for the specified user ID. If the requested User ID is invalid, send Default
Response with an error status equal to FAILURE.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' for this command is marked as 'desc', indicating that the specific constraints are detailed elsewhere in the documentation. The 'Conformance' for this command is marked as 'M', meaning that it is mandatory. This implies that the 'UserID' command is a required element in the Door Lock Cluster and must be implemented in all devices that support this cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, the table row describes a command with the ID '1' named 'UserType', which is of the type 'UserTypeEnum' and applies to all constraints. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'UserType' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.10.27. SetRFIDCode Command
Set an ID for RFID access into the lock.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster's Commands section, the table row describes an element with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', meaning that the 'UserID' element is mandatory. This implies that the 'UserID' command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserStatus" command, which is of the type "UserStatusEnum." The "Constraint" for this command is described elsewhere in the documentation, indicating complexity beyond a simple constraint. The "Quality" is marked as "X," meaning this element is explicitly disallowed in certain contexts. The default value for this command is "OccupiedEnabled." The "Conformance" is marked as "M," which means that the "UserStatus" command is mandatory and must always be implemented in any device or system using the Door Lock Cluster, without any conditional exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserType" command, which is of the type "UserTypeEnum." The constraint for this command is described elsewhere in the documentation, indicating that its constraints are complex. The quality of this command is marked as "X," meaning it is explicitly disallowed in some contexts. The default value for this command is "UnrestrictedUser." The conformance rule for this command is "M," which means it is mandatory and always required to be implemented in any device or system that supports the Door Lock Cluster. This ensures that the "UserType" command is consistently available across all implementations of this cluster.

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes an element with the ID '3' named 'RFIDCode', which is of type 'octstr' (octet string). The conformance rule for this element is marked as 'M', indicating that it is Mandatory. This means that the 'RFIDCode' command must always be implemented and supported in any device or application that adheres to this specification for the Door Lock Cluster. There are no conditions or dependencies affecting this requirement; it is an absolute necessity for compliance.

Return status is a global status code or a cluster-specific status code from the Status Codes table and
SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry pertains to the "SUCCESS" command within the Door Lock Cluster, specifically under the Commands section. This command indicates that setting an RFID code was successful. The conformance rule for this entry is not explicitly provided in the data you shared, but typically, such a command would be associated with a conformance tag or expression that dictates when it must be implemented. If the conformance were, for example, "M," it would mean that the "SUCCESS" command is mandatory and must always be implemented in any device supporting the Door Lock Cluster. If it were "O," the command would be optional, allowing implementers to choose whether to include it. Without the specific conformance string, we can only infer that this command is likely crucial for confirming successful operations related to RFID code settings, ensuring users receive feedback on their actions.

* The table row entry describes a command named "FAILURE" within the Door Lock Cluster, specifically related to the scenario where setting an RFID code fails. The conformance rule for this command is not explicitly provided in the data snippet, so we cannot directly interpret its conformance status using the provided guide. However, if we assume a typical conformance scenario, the command might be optional or conditional based on certain features or conditions within the Door Lock Cluster. Without a specific conformance string, we can only infer that this command is part of the command set for handling RFID code setting failures, and its implementation may depend on additional context or conditions described elsewhere in the Matter specification documentation.

* The table row entry pertains to the "CONSTRAINT_ERROR" command within the Door Lock Cluster's Commands section. This command is used to indicate that an attempt to set an RFID code has failed because the User ID specified was out of the acceptable range. The conformance rule for this entry is not explicitly provided in the data you shared, but if it were, it would dictate under what conditions this command is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were "M," it would mean that the "CONSTRAINT_ERROR" command is mandatory and must always be implemented in devices supporting the Door Lock Cluster. If the conformance were "O," it would be optional, meaning it could be implemented at the discretion of the manufacturer without any dependencies. Understanding the conformance rule is crucial for developers to ensure compliance with the Matter specification and to implement the feature appropriately in their IoT devices.

* The table row entry pertains to the Door Lock Cluster within the Commands section and describes a command named "DUPLICATE." This command is used to indicate that an attempt to set an RFID code has failed because it would result in a duplicate RFID code. The conformance rule for this command is not explicitly provided in the data, but based on the context, it likely follows a specific conformance condition that would be detailed elsewhere in the documentation. Typically, such a command would be implemented to ensure the integrity and uniqueness of RFID codes within the system, preventing conflicts or security issues that could arise from duplicate entries. The absence of a direct conformance tag suggests that the rule might be complex or conditional, requiring further reference to the documentation for precise implementation details.

5.2.10.27.1. UserID Field
This field SHALL indicate the user ID.
The value of the UserID field SHALL be between 0 and the value of the NumberOfRFIDUsersSup
ported attribute.
5.2.10.27.2. UserStatus Field
This field SHALL indicate what the status is for a specific user ID. The values are according to “Set
PIN” while not all are supported.
Only the values 1 (Occupied/Enabled) and 3 (Occupied/Disabled) are allowed for UserStatus.
5.2.10.27.3. UserType Field
The values are the same as used for SetPINCode command.
5.2.10.28. GetRFIDCode Command
Retrieve an RFID code.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the specific constraints for this command are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', meaning that this command is mandatory. This implies that any implementation of the Door Lock Cluster must include the 'UserID' command as a required element, ensuring its presence and functionality in all compliant devices.

5.2.10.28.1. UserID Field
This field SHALL indicate the user ID.
The value of the UserID field SHALL be between 0 and the value of the NumberOfRFIDUsersSup
ported attribute.
5.2.10.29. GetRFIDCodeResponse Command
Returns the RFID code for the specified user ID.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command with the ID '0' named 'UserID', which is of type 'uint16'. The 'Constraint' is marked as 'desc', indicating that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' field is marked as 'M', which means that this command is mandatory. Therefore, the 'UserID' command must always be implemented in any device that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Commands section, the entry for 'UserStatus' with ID '1' is defined as a command of type 'UserStatusEnum'. The 'Constraint' is described elsewhere in the documentation, and the 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in certain contexts. The default value for 'UserStatus' is 'Available'. The 'Conformance' is marked as 'M', which means this command is mandatory and must always be implemented in any device or application that supports the Door Lock Cluster. This ensures that the 'UserStatus' command is a required feature for compliance with the Matter specification in this context.

* The table row describes a command within the Door Lock Cluster, specifically identified by the ID '2' and named 'UserType'. This command utilizes the 'UserTypeEnum' type, and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The quality of this command is marked as 'X', meaning it is explicitly disallowed. The conformance rule for this command is 'M', which signifies that it is mandatory and always required within the Door Lock Cluster. Despite being mandatory, the quality 'X' suggests that while the command is defined as necessary, its use is explicitly not allowed, indicating a potential contradiction or a special case that might be further explained in the broader context of the specification.

* In the context of the Door Lock Cluster, the table row describes a command with the ID '3' named 'RFIDCode', which is of type 'octstr' (octet string). The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed within the specification. The 'Default' value is 'empty', suggesting that if it were allowed, it would start with an empty value. The 'Conformance' field is marked as 'M', meaning that under normal circumstances, this command would be mandatory. However, due to the 'Quality' being 'X', the command is not permitted in the current specification, overriding the mandatory conformance.

If the requested User ID is valid and the Code doesn’t exist, Get RFID Code Response SHALL have
the following format:
User ID = requested User ID
UserStatus = 0 (available)
UserType = 0xFF (not supported)
RFID Code = 0 (zero length)
If requested User ID is invalid, send Default Response with an error status. The error status SHALL
be equal to CONSTRAINT_ERROR when User_ID is less than the max number of users supported,
and NOT_FOUND if greater than or equal to the max number of users supported.
5.2.10.30. ClearRFIDCode Command
Clear an RFID code or all RFID codes.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'RFIDSlotIndex' command. This command is identified by the ID '0' and is of type 'uint16'. It has a constraint that limits its values to the range from 1 to the number of RFID users supported, with an additional specific value of 0xFFFE. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the 'RFIDSlotIndex' command must always be implemented and supported in any device or application that utilizes the Door Lock Cluster, without any conditions or exceptions.

For each RFID Code cleared whose user doesn’t have a PIN Code or other credential type, then the
corresponding  user  record’s  UserStatus  value  SHALL  be  set  to  Available,  and  UserType  value
SHALL be set to UnrestrictedUser and all schedules SHALL be cleared.
5.2.10.30.1. RFIDSlotIndex Field
This field SHALL indicate a valid RFID code slot index or 0xFFFE to indicate all RFID code slots
SHALL be cleared.
5.2.10.31. ClearAllRFIDCodes Command
Clear out all RFIDs on the lock. If you clear all RFID codes and this user didn’t have a PIN code, the
user status has to be set to "0 Available", the user type has to be set to the default value, and all
schedules which are supported have to be set to the default values.
5.2.10.32. SetUser Command
Set user into the lock.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, the table row describes a command named "OperationType" with an ID of '0'. This command is of the type 'DataOperationTypeEnum' and is constrained to the operations 'Add' and 'Modify'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "OperationType" command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, the table row describes a command with the ID '1' named 'UserIndex', which is of type 'uint16'. The 'UserIndex' command is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported', indicating that it is used to specify or reference a user within the supported range of users for the door lock. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the 'UserIndex' command is always required to be implemented in any device that supports the Door Lock Cluster, ensuring consistent functionality across all compliant devices.

* In the Door Lock Cluster, under the Commands section, the entry for 'UserName' is identified by ID '2' and is of type 'string' with a maximum constraint of 10 characters. The quality of this entry is marked as 'X', indicating that it is explicitly disallowed in this context. The default value for 'UserName' is 'empty'. The conformance rule for this entry is 'M', which means that the 'UserName' command is mandatory and always required in implementations of the Door Lock Cluster, regardless of other conditions or features.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '3' named 'UserUnique ID'. This element is of type 'uint32', meaning it is a 32-bit unsigned integer, and it applies to all constraints. The quality of this element is marked as 'X', indicating that it is explicitly disallowed. The default value for this element is set to '0xFFFFFFFF'. The conformance rule for 'UserUnique ID' is 'M', which means that this element is mandatory and always required in the implementation of the Door Lock Cluster. However, despite being mandatory, the quality 'X' suggests that its use is explicitly not allowed, which may indicate a contradiction or a need for further clarification in the specification.

* The table row describes a command within the Door Lock Cluster, specifically the "UserStatus" command, which is of the type "UserStatusEnum." This command can have values constrained to either "OccupiedEnabled" or "OccupiedDisabled," with a default value of "OccupiedEnabled." The "Quality" field indicates that this command is disallowed, as denoted by the "X." However, the "Conformance" field is marked with an "M," meaning that the "UserStatus" command is mandatory and always required to be implemented in the context of the Door Lock Cluster, regardless of any other conditions or features. This suggests that despite being disallowed in terms of quality, the command must still be present in the implementation.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically focusing on the "UserType" command. This command utilizes the "UserTypeEnum" type and can take on several values, including "UnrestrictedUser," "NonAccessUser," "ForcedUser," "DisposableUser," "ExpiringUser," "ScheduleRestrictedUser," and "RemoteOnlyUser." The "Quality" field is marked as "X," indicating that this element is explicitly disallowed in some contexts, although this does not affect its conformance status. The default value for this command is "UnrestrictedUser." The conformance rule for this command is "M," meaning it is mandatory and always required within the specification. This implies that any implementation of the Door Lock Cluster must support the "UserType" command as a fundamental requirement.

* The table row describes a command within the Door Lock Cluster, specifically the "CredentialRule" command, which is identified by ID '6' and is of the type 'CredentialRuleEnum'. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed. The 'Default' value for this command is 'Single'. The 'Conformance' field is marked as 'M', meaning that this command is mandatory and must always be implemented according to the Matter specification. Despite being mandatory, the 'Quality' field's 'X' designation means that, in practice, this command is not allowed to be used, reflecting a contradiction that may require further clarification in the broader context of the specification.

Fields used for different use cases:

_Table parsed from section 'Commands':_

* This entry pertains to the "Create a new user record" command within the Door Lock Cluster's command section. The command involves setting various parameters for a new user record, such as `OperationType`, `UserIndex`, `UserName`, `UserUniqueID`, `UserStatus`, `UserType`, and `CredentialRule`, with specific default values if certain fields are null. Additionally, `CreatorFabricIndex` and `LastModifiedFabricIndex` must be set to the accessing fabric index, and a `LockUserChange` event must be generated upon successful creation. The conformance rule for this command is not explicitly provided in the table row data, but based on the context and typical usage of such commands, it is likely mandatory (M) for devices implementing the Door Lock Cluster, ensuring that all devices supporting this cluster can create new user records as described.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically for modifying an existing user record. The command requires that the `OperationType` is set to Modify, and the `UserIndex` must correspond to a user record with a `UserType` not set to Available. The `UserName` and `UserUniqueID` fields must be null if the user record was not created by the accessing fabric, and an `INVALID_COMMAND` error is returned if these fields are not null and the accessing fabric index does not match the `CreatorFabricIndex`. If the `UserName` and `UserUniqueID` are valid, they should be set to the provided values. The `UserStatus`, `UserType`, and `CredentialRule` fields may be null, indicating no change, or set to new values if provided. The `CreatorFabricIndex` cannot be changed, and the `LastModifiedFabricIndex` should be updated to the accessing fabric index. A `LockUserChange

user
UserName SHALL be null if modifying a user
record that was not created by the accessing
INVALID_COMMAND SHALL be returned if
UserName is not null and the accessing fab
ric index doesn’t match the CreatorFabricIn
dex in the user record otherwise UserName
SHALL be set to the value provided in the
modifying
the user record that was not created by the
INVALID_COMMAND SHALL be returned if
UserUniqueID is not null and the accessing
Creator
otherwise
UserUniqueID SHALL be set to the value pro
UserStatus MAY be null causing no change to
UserStatus in user record otherwise UserSta
tus SHALL be set to the value provided in the
UserType MAY be null causing no change to
UserType in user record otherwise UserType
SHALL be set to the value provided in the
no
change to CredentialRule in user record oth
erwise CredentialRule SHALL be set to the
CreatorFabricIndex SHALL NOT be changed in
the user record. LastModifiedFabricIndex in the
new user record SHALL be set to the accessing
A LockUserChange event SHALL be generated
Return status is a global status code or a cluster-specific status code from the Status Codes table and
SHALL be one of the following values:
• SUCCESS, if setting User was successful.
• FAILURE, if some unexpected internal error occurred setting User.
• OCCUPIED, if OperationType is Add and UserIndex points to an occupied slot.
• INVALID_COMMAND, if one or more fields violate constraints or are invalid or if OperationType
is Modify and UserIndex points to an available slot.
5.2.10.32.1. OperationType Field
This field SHALL indicate the type of operation.
5.2.10.32.2. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.32.3. UserName Field
This field SHALL contain a string to use as a human readable identifier for the user.
If UserName is null then:
• If the OperationType is Add, the UserName in the resulting user record SHALL be set to an
empty string.
• If the OperationType is Modify, the UserName in the user record SHALL NOT be changed from
the current value.
If UserName is not null, the UserName in the user record SHALL be set to the provided value.
5.2.10.32.4. UserUniqueID Field
This field SHALL indicate the fabric assigned number to use for connecting this user to other users
on other devices from the fabric’s perspective.
If UserUniqueID is null then:
• If the OperationType is Add, the UserUniqueID in the resulting user record SHALL be set to
default value specified above.
• If the OperationType is Modify, the UserUniqueID in the user record SHALL NOT be changed
from the current value.
If UserUniqueID is not null, the UserUniqueID in the user record SHALL be set to the provided
value.
5.2.10.32.5. UserStatus Field
This field SHALL indicate the UserStatus to assign to this user when created or modified.
If UserStatus is null then:
• If the OperationType is Add, the UserStatus in the resulting user record SHALL be set to default
value specified above.
• If the OperationType is Modify, the UserStatus in the user record SHALL NOT be changed from
the current value.
If UserStatus is not null, the UserStatus in the user record SHALL be set to the provided value.
5.2.10.32.6. UserType Field
This field SHALL indicate the UserType to assign to this user when created or modified.
If UserType is null then:
• If the OperationType is Add, the UserType in the resulting user record SHALL be set to default
value specified above.
• If the OperationType is Modify, the UserType in the user record SHALL NOT be changed from
the current value.
If UserType is not null, the UserType in the user record SHALL be set to the provided value.
5.2.10.32.7. CredentialRule Field
This field SHALL indicate the CredentialRule to use for this user.
The valid CredentialRule enumeration values depends on the bits in the CredentialRulesBitmap
map. Each bit in the map identifies a valid CredentialRule that can be used.
If CredentialRule is null then:
• If the OperationType is Add, the CredentialRule in the resulting user record SHALL be set to
default value specified above.
• If the OperationType is Modify, the CredentialRule in the user record SHALL NOT be changed
from the current value.
If CredentialRule is not null, the CredentialRule in the user record SHALL be set to the provided
value.
5.2.10.33. GetUser Command
Retrieve user.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'UserIndex'. This element is of type 'uint16' and is constrained to values ranging from 1 to the total number of users supported by the device, as indicated by 'NumberOfTotalUsersSupported'. The conformance rule for 'UserIndex' is marked as 'M', which means it is a mandatory element. This implies that the 'UserIndex' must always be implemented and supported in any device or application utilizing the Door Lock Cluster, without any conditions or exceptions.

An InvokeResponse command SHALL be sent with an appropriate error (e.g. FAILURE, INVALID_
COMMAND, etc.) as needed otherwise the GetUserResponse Command SHALL be sent implying a
status of SUCCESS.
5.2.10.34. GetUserResponse Command
Returns the user for the specified UserIndex.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'UserIndex'. This element is of type 'uint16', which means it is a 16-bit unsigned integer. The 'Constraint' specifies that its value must be between 1 and the value of 'NumberOfTotalUsersSupported', indicating that it represents a user index within the supported range of total users. The 'Conformance' for 'UserIndex' is marked as 'M', which means this element is mandatory. It is always required to be implemented in any device or application that supports the Door Lock Cluster, ensuring consistent functionality across all implementations.

* In the Door Lock Cluster, within the Commands section, there is an entry for a command identified by ID '1' named 'UserName'. This command is of type 'string' and is constrained to a maximum length of 10 characters. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in some contexts, although the specifics of this disallowance are not detailed here. The default value for this command is 'empty'. The conformance rule for this entry is 'M', meaning that the 'UserName' command is mandatory and must always be implemented as specified in the Matter IoT specification.

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '2', named 'UserUnique ID', which is of type 'uint32' and has a constraint labeled 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The default value for this element is '0'. The 'Conformance' field is marked as 'M', which means that the 'UserUnique ID' command is mandatory and always required in the implementation of the Door Lock Cluster according to the Matter specification. This implies that any device implementing this cluster must include this command as part of its functionality.

* The table row describes a command within the Door Lock Cluster, specifically the "UserStatus" command, which is of the type "UserStatusEnum" and applies to all constraints. The "Quality" is marked as "X," indicating that this element is explicitly disallowed in certain contexts. The default value for this command is "Available." The conformance rule for "UserStatus" is "M," meaning that this command is mandatory and must always be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the "UserType" command. This command is of the type "UserTypeEnum" and applies to all constraints, with a default value of "UnrestrictedUser." The quality of this command is marked as "X," indicating it is explicitly disallowed. The conformance rule for this command is "M," meaning it is mandatory. However, since the quality is "X," it suggests that while the command is defined as mandatory in the specification, it is not allowed to be implemented or used in practice. This could indicate a conflict or a special case where the command is recognized but not permitted for use.

* The table row describes a command within the Door Lock Cluster, specifically the "CredentialRule" command, which is of the type "CredentialRuleEnum." The constraint for this command is described elsewhere in the documentation, as indicated by "desc." The quality of this command is marked as "X," meaning it is explicitly disallowed. The default value for this command is "Single." The conformance rule for this command is "M," which means that the "CredentialRule" command is mandatory and always required within the Door Lock Cluster context. Despite being mandatory, its quality being "X" suggests that while it is defined as a necessary element, it is not allowed to be implemented in this context, possibly due to a specification or security reason.

* The table row describes a command within the Door Lock Cluster, specifically related to the 'Credentials' element. This element is of the type 'list[CredentialStruct]' and is constrained by the range '0 to NumberOfCredentialsSupportedPerUser', indicating that the list can contain zero up to the maximum number of credentials supported per user. The 'Quality' is marked as 'X', meaning that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', which means that the 'Credentials' command is mandatory and must always be implemented within the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'CreatorFabricIndex' command. This command is identified by the ID '7' and is of the type 'fabric-idx', with a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', which typically denotes that this element is explicitly disallowed; however, this seems to be a discrepancy since the 'Conformance' is marked as 'M'. According to the Matter Conformance Interpretation Guide, 'M' signifies that the 'CreatorFabricIndex' command is mandatory, meaning it is always required to be implemented in any device or application that supports the Door Lock Cluster. This mandatory status ensures that the command is consistently available across all implementations of the Door Lock Cluster.

* The table row entry describes a command within the Door Lock Cluster, specifically the 'LastModifiedFabricIndex' command. This command has an ID of '8' and is of the type 'fabric-idx', with a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', which typically signifies that the element is disallowed; however, the 'Conformance' is marked as 'M', meaning that the 'LastModifiedFabricIndex' command is mandatory. This implies that despite any other quality indicators, this command must always be implemented in any device or application supporting the Door Lock Cluster according to the Matter specification.

* The table row describes a command within the Door Lock Cluster, specifically the "NextUserIndex" command. This command is identified by the ID '9' and is of type 'uint16', with a constraint that its value must be between 1 and the total number of users supported by the door lock. The 'Quality' field is marked as 'X', indicating that this command is explicitly disallowed in terms of quality considerations. The 'Conformance' field is marked as 'M', meaning that the "NextUserIndex" command is mandatory and must always be implemented in any device supporting the Door Lock Cluster, without any conditional dependencies or exceptions.

If the requested UserIndex is valid and the UserStatus is Available for the requested UserIndex then
UserName, UserUniqueID, UserStatus, UserType, CredentialRule, Credentials, CreatorFabricIndex,
and LastModifiedFabricIndex SHALL all be null in the response.
5.2.10.34.1. UserIndex Field
This field SHALL indicate the user ID.
5.2.10.34.2. UserName Field
This field SHALL contain a string to use as a human readable identifier for the user.
5.2.10.34.3. UserUniqueID Field
See UserUniqueID field.
5.2.10.34.4. UserStatus Field
This field SHALL indicate the UserStatus assigned to the user when created or modified.
5.2.10.34.5. UserType Field
This field SHALL indicate the UserType assigned to this user when created or modified.
5.2.10.34.6. CredentialRule Field
This field SHALL indicate the CredentialRule set for this user.
5.2.10.34.7. Credentials Field
This field SHALL contain a list of credentials for this user.
5.2.10.34.8. CreatorFabricIndex Field
This field SHALL indicate the user’s creator fabric index. CreatorFabricIndex SHALL be null if User
Status is set to Available or when the creator fabric cannot be determined (for example, when user
was created outside the Interaction Model) and SHALL NOT be null otherwise. This value SHALL be
set to 0 if the original creator fabric was deleted.
5.2.10.34.9. LastModifiedFabricIndex Field
This field SHALL indicate the user’s last modifier fabric index. LastModifiedFabricIndex SHALL be
null if UserStatus is set to Available or when the modifier fabric cannot be determined (for exam
ple, when user was modified outside the Interaction Model) and SHALL NOT be null otherwise. This
value SHALL be set to 0 if the last modifier fabric was deleted.
5.2.10.34.10. NextUserIndex Field
This field SHALL indicate the next occupied UserIndex in the database which is useful for quickly
identifying occupied user slots in the database. This SHALL NOT be null if there is at least one occu
pied entry after the requested UserIndex in the User database and SHALL be null if there are no
more occupied entries.
5.2.10.35. ClearUser Command
Clears a user or all Users.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '0' named 'UserIndex'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' specifies that its value must be between 1 and the 'NumberOfTotalUsersSupported', or it can be the special value 0xFFFE. The 'Conformance' for 'UserIndex' is marked as 'M', which stands for Mandatory. This means that the 'UserIndex' element is always required to be implemented in any device or application that supports the Door Lock Cluster, with no conditions or exceptions.

For each user to clear, all associated credentials (e.g. PIN, RFID, fingerprint, etc.) SHALL be cleared
and the user entry values SHALL be reset to their default values (e.g. UserStatus SHALL be Avail
able, UserType SHALL be UnrestrictedUser) and all associated schedules SHALL be cleared.
A LockUserChange event with the provided UserIndex SHALL be generated after successfully clear
ing users.
5.2.10.35.1. UserIndex Field
This field SHALL specify a valid User index or 0xFFFE to indicate all user slots SHALL be cleared.
5.2.10.36. SetCredential Command
Set a credential (e.g. PIN, RFID, Fingerprint, etc.) into the lock for a new user, existing user, or Pro
grammingUser.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "OperationType" command. This command is of the type "DataOperationTypeEnum" and is constrained to the operations "Add" and "Modify." The conformance rule for this command is marked as "M," which stands for Mandatory. This means that the "OperationType" command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the context of the Door Lock Cluster, the table row describes a command named "Credential" with an ID of '1' and a type of 'CredentialStruct'. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "Credential" command is always required to be implemented in any device or system that supports the Door Lock Cluster according to the Matter IoT specification. There are no conditions or exceptions; the command must be present and functional in all compliant implementations.

* The table row describes a command within the Door Lock Cluster, specifically the "CredentialData" command. This command is identified by the ID '2' and is of the type 'octstr', which indicates it is an octet string. The 'Constraint' field is marked as 'desc', suggesting that the constraints for this command are detailed elsewhere in the documentation. The 'Conformance' field is marked with 'M', which means that the "CredentialData" command is mandatory. This implies that any implementation of the Door Lock Cluster must include this command as a required element, without any conditions or exceptions.

* In the context of the Door Lock Cluster's Commands section, the table row describes an element with the ID '3', named 'UserIndex', which is of type 'uint16'. The 'UserIndex' is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', meaning that the 'UserIndex' is a mandatory element within this context. This implies that whenever the Door Lock Cluster is implemented, the 'UserIndex' command must be included and supported as per the Matter specification.

* In the Door Lock Cluster, within the Commands section, the table row describes a command identified as 'UserStatus' with an ID of '4'. This command utilizes the 'UserStatusEnum' type and can have values constrained to 'OccupiedEnabled' or 'OccupiedDisabled', with 'OccupiedEnabled' being the default value. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', meaning that the 'UserStatus' command is mandatory and must always be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '5' named 'UserType', which is of the type 'UserTypeEnum'. This element can take on several values: 'UnrestrictedUser', 'ProgrammingUser', 'NonAccessUser', 'ForcedUser', 'DisposableUser', 'ExpiringUser', and 'RemoteOnlyUser', with 'UnrestrictedUser' being the default. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in some contexts. The 'Conformance' is marked as 'M', meaning that the 'UserType' element is mandatory and always required in the implementation of the Door Lock Cluster. This implies that any device or application implementing this cluster must support the 'UserType' command as a fundamental part of its functionality.

Fields used for different use cases:

_Table parsed from section 'Commands':_

* This entry describes a command within the Door Lock Cluster for creating a new credential and user record. The operation requires setting the `OperationType` to Add and using a `UserIndex` that is null, allowing the lock to find an available user record and associate it with the provided `CredentialIndex` in `CredentialStruct`, which must be unoccupied. The `UserStatus` and `UserType` can be null, defaulting to `OccupiedEnabled` and `UnrestrictedUser`, respectively, unless specified otherwise, but `UserType` cannot be `ProgrammingUser`. The `CreatorFabricIndex` and `LastModifiedFabricIndex` must match the accessing fabric index. A `LockUserChange` event is triggered upon successful creation, detailing the `UserIndex` and `CredentialIndex` used. The conformance rule for this command is not explicitly stated in the provided data, but based on the detailed requirements and SHALL statements, it is likely mandatory (M) for implementations supporting this use case

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster for adding a new credential to an existing user record. The command has specific requirements: the `OperationType` must be set to Add, and the `UserIndex` must not be null or already associated with the `CredentialIndex` in the provided `CredentialStruct`. If these conditions are not met, an `INVALID_COMMAND` status will be returned. Additionally, the accessing fabric index must match the `CreatorFabricIndex` in the user record pointed to by `UserIndex`, and the `CredentialIndex` must refer to an available credential slot. The `UserStatus` and `UserType` should be null, and the `CreatorFabricIndex` in the user record must remain unchanged. The `LastModifiedFabricIndex` in the user record and both `CreatorFabricIndex` and `LastModifiedFabricIndex` in the new credential record should be set to the accessing fabric index. A `LockUserChange` event is triggered upon successfully

UserIndex SHALL NOT be null and SHALL
NOT already be associated with the Creden
tialIndex in CredentialStruct provided other
response
INVALID_COMMAND SHALL be returned if
the accessing fabric index doesn’t match the
record
pro
vided SHALL be for an available credential
CreatorFabricIndex SHALL NOT be changed in
the user record. LastModifiedFabricIndex in the
user record SHALL be set to the accessing fabric
LastModifiedFabricIn
dex in the new credential record SHALL be set
A LockUserChange event SHALL be generated

_Table parsed from section 'Commands':_

* This entry pertains to the "Modify credential for an existing user record" command within the Door Lock Cluster's commands section. The command requires that the `OperationType` is set to Modify, and the `UserIndex` must already be linked to the `CredentialIndex` in the provided `CredentialStruct`; otherwise, an `INVALID_COMMAND` status will be returned. Additionally, the command will return `INVALID_COMMAND` if the accessing fabric index does not match the `CreatorFabricIndex` in either the user or credential records. The `CredentialIndex` must refer to an occupied slot, and both `UserStatus` and `UserType` must be null. The `CreatorFabricIndex` cannot be altered, while the `LastModifiedFabricIndex` must be updated to the accessing fabric index. A `LockUserChange` event is triggered upon successful modification. The conformance rule for this command is not explicitly provided in the row, suggesting that it might be described in more detail elsewhere in the documentation

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically for the use case of modifying a credential for a Programming User. The command requires several specific conditions to be met: the `OperationType` must be set to Modify, `UserIndex` must be null, and the `CredentialStruct` must have `CredentialType` set to ProgrammingPIN and `CredentialIndex` set to 0. Additionally, if the accessing fabric index does not match the `CreatorFabricIndex` in the credential record, an `INVALID_COMMAND` should be returned. The `UserStatus` must be null, and `UserType` must be set to ProgrammingUser. The `CreatorFabricIndex` should remain unchanged, while the `LastModifiedFabricIndex` should be updated to the accessing fabric index. A `LockUserChange` event should be generated after successfully modifying the Programming User PIN code. The conformance rule for this command is not explicitly provided in the row, but based on the context and the

INVALID_COMMAND SHALL be returned if
the accessing fabric index doesn’t match the
CreatorFabricIndex in the credential record
pointed to by the CredentialIndex field value
SHALL
SHALL
Programmin
CreatorFabricIndex SHALL NOT be changed in
the credential record. LastModifiedFabricIndex
the
A LockUserChange event SHALL be generated
Programmin
5.2.10.36.1. OperationType Field
This field SHALL indicate the set credential operation type requested.
5.2.10.36.2. Credential Field
This field SHALL contain a credential structure that contains the CredentialTypeEnum and the cre
dential index (if applicable or 0 if not) to set.
5.2.10.36.3. CredentialData Field
This field SHALL indicate the credential data to set for the credential being added or modified. The
length of the credential data SHALL conform to the limits of the CredentialType specified in the Cre
dential structure otherwise an INVALID_COMMAND status SHALL be returned in the SetCredential
Response command.
5.2.10.36.4. UserIndex Field
This field SHALL indicate the user index to the user record that corresponds to the credential being
added or modified. This SHALL be null if OperationType is add and a new credential and user is
being added at the same time.
5.2.10.36.5. UserStatus Field
This field SHALL indicate the user status to use in the new user record if a new user is being cre
ated. This SHALL be null if OperationType is Modify. This MAY be null when adding a new creden
tial and user.
5.2.10.36.6. UserType Field
This field SHALL indicate the user type to use in the new user record if a new user is being created.
This SHALL be null if OperationType is Modify. This MAY be null when adding a new credential and
user.
5.2.10.37. SetCredentialResponse Command
Returns the status for setting the specified credential.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the 'Status' command, which has an ID of '0' and is of the 'status' type. The 'Constraint' for this command is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' field is marked as 'M', which means that this 'Status' command is mandatory. In the context of the Matter IoT specification, this implies that any implementation of the Door Lock Cluster must include this 'Status' command without exception.

* The table row describes a command within the Door Lock Cluster, specifically the 'UserIndex' command. This command is identified by the ID '1' and is of type 'uint16', which means it is a 16-bit unsigned integer. The value of 'UserIndex' must fall within the constraint range of '1 to NumberOfTotalUsersSupported', ensuring it aligns with the total number of users the system can support. The 'Quality' field is marked as 'X', indicating that this element is explicitly disallowed in terms of quality considerations. The default value for 'UserIndex' is '0'. The 'Conformance' field is marked as 'M', meaning that the 'UserIndex' command is mandatory and must always be implemented in any device or application using this specification. This mandatory status ensures that the command is a required part of the Door Lock Cluster's functionality.

* The table row describes a command named "NextCredentialIndex" within the Door Lock Cluster, identified by ID '2' and of type 'uint16'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The quality of this command is marked as 'X', meaning it is explicitly disallowed. The conformance rule for "NextCredentialIndex" is 'O', indicating that this command is optional and not required to be implemented, with no dependencies or conditions affecting its optional status.

5.2.10.37.1. Status Field
Status comes from the Status Codes table and SHALL be one of the following values:
• SUCCESS, if setting user credential was successful.
• FAILURE, if some unexpected internal error occurred setting user credential.
• OCCUPIED, if OperationType is Add and CredentialIndex in Credential structure points to an
occupied slot.
• OCCUPIED, if OperationType is Modify and CredentialIndex in Credential structure does not
match the CredentialIndex that is already associated with the provided UserIndex.
• DUPLICATE, if CredentialData provided is a duplicate of another credential with the same Cre
dentialType (e.g. duplicate PIN code).
• RESOURCE_EXHAUSTED, if OperationType is Add and the new credential cannot be added due
to resource constraints such as:
◦ The user referred to by UserIndex already has NumberOfCredentialsSupportedPerUser cre
dentials associated.
◦ The credential is of type AliroEvictableEndpointKey or AliroNonEvictableEndpointKey, and
adding it would cause the total number of credentials of those two types to exceed Num
berOfAliroEndpointKeysSupported.
• INVALID_COMMAND, if one or more fields violate constraints or are invalid.
• INVALID_COMMAND, if the CredentialIndex in the Credential provided exceeds the number of
credentials of the provided CredentialType supported by the lock.
• INVALID_COMMAND, if OperationType is Modify and UserIndex points to an available slot.
5.2.10.37.2. UserIndex Field
This field SHALL indicate the user index that was created with the new credential. If the status
being returned is not success then this SHALL be null. This SHALL be null if OperationType was
Modify; if the OperationType was Add and a new User was created this SHALL NOT be null and
SHALL provide the UserIndex created. If the OperationType was Add and an existing User was asso
ciated with the new credential then this SHALL be null.
5.2.10.37.3. NextCredentialIndex Field
This field SHALL indicate the next available index in the database for the credential type set, which
is useful for quickly identifying available credential slots in the database. This SHALL NOT be null if
there is at least one available entry after the requested credential index in the corresponding data
base and SHALL be null if there are no more available entries. The NextCredentialIndex reported
SHALL NOT exceed the maximum number of credentials for a particular credential type.
5.2.10.38. GetCredentialStatus Command
Retrieve the status of a particular credential (e.g. PIN, RFID, Fingerprint, etc.) by index.

_Table parsed from section 'Commands':_

* In the context of the Door Lock Cluster, specifically within the Commands section, the table row describes an element with the ID '0' named 'Credential', which is of the type 'CredentialStruct'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'Credential' element is always required to be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

An InvokeResponse command SHALL be sent with an appropriate error (e.g. FAILURE, INVALID_
COMMAND, etc.) as needed otherwise the GetCredentialStatusResponse command SHALL be sent
implying a status of SUCCESS.
5.2.10.38.1. Credential Field
This field SHALL contain a credential structure that contains the CredentialTypeEnum and the cre
dential index (if applicable or 0 if not) to retrieve the status for.
5.2.10.39. GetCredentialStatusResponse Command
Returns the status for the specified credential.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "CredentialExists" command, which is of type boolean. The "Constraint" is listed as "all," indicating that this command applies universally within its context. The "Conformance" is marked as "M," meaning that the "CredentialExists" command is mandatory. This implies that any implementation of the Door Lock Cluster must include this command, as it is a required element with no conditions or exceptions.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, within the Commands section, the table row describes an element with the ID '1' named 'UserIndex'. This element is of type 'uint16' and is constrained to values ranging from 1 to the 'NumberOfTotalUsersSupported'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', which means that the 'UserIndex' element is mandatory and always required in the context of the Door Lock Cluster commands. This implies that any implementation of this cluster must include the 'UserIndex' element as specified.

* The table row describes a command within the Door Lock Cluster, specifically the 'CreatorFabricIndex' command. This command is identified by the ID '2' and is of the type 'fabric-idx', with a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' field is marked as 'X', meaning this element is explicitly disallowed. The 'Conformance' field is marked as 'M', which signifies that the 'CreatorFabricIndex' command is mandatory. This means that, according to the Matter specification, this command must always be implemented in any device or application that supports the Door Lock Cluster, without any conditional exceptions or dependencies.

* The table row entry pertains to the "LastModifiedFabricIndex" command within the Door Lock Cluster's Commands section. This command is identified by the ID '3' and is of the type 'fabric-idx', with a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' field is marked as 'X', meaning this element is explicitly disallowed. Despite this, the 'Conformance' field is marked as 'M', which signifies that the "LastModifiedFabricIndex" command is mandatory according to the Matter specification. This means that, under normal circumstances, this command must be implemented in any device supporting the Door Lock Cluster, although the 'Quality' field suggests it is not allowed, indicating a potential contradiction or special case that might require further clarification in the broader documentation.

* In the Door Lock Cluster, under the Commands section, the entry for 'NextCredentialIndex' is identified by the ID '4' and is of type 'uint16'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The quality of this command is marked as 'X', meaning it is explicitly disallowed and should not be implemented or used. The conformance rule for 'NextCredentialIndex' is 'O', which signifies that this command is optional and not required for implementation. There are no dependencies or conditions that affect its optional status, allowing implementers the choice to include it or not without any further implications.

* In the Door Lock Cluster, under the Commands section, the entry for 'CredentialData' with ID '5' is of type 'octstr' and has a constraint described elsewhere in the documentation. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed. The 'Conformance' field is specified as '[ALIRO]', meaning that the 'CredentialData' command is optional if the feature 'ALIRO' is supported. However, given the 'Quality' is 'X', this command is not allowed regardless of the 'ALIRO' feature support.

5.2.10.39.1. CredentialExists Field
This field SHALL indicate if the requested credential type and index exists and is populated for the
requested user index.
5.2.10.39.2. UserIndex Field
This field SHALL indicate the credential’s corresponding user index value if the credential exists. If
CredentialType  requested  was  ProgrammingPIN  then  UserIndex  SHALL  be  null;  otherwise,
UserIndex SHALL be null if CredentialExists is set to False and SHALL NOT be null if CredentialEx
ists is set to True.
5.2.10.39.3. CreatorFabricIndex Field
This field SHALL indicate the credential’s creator fabric index. CreatorFabricIndex SHALL be null if
CredentialExists is set to False or when the creator fabric cannot be determined (for example, when
credential was created outside the Interaction Model) and SHALL NOT be null otherwise. This value
SHALL be set to 0 if the original creator fabric was deleted.
5.2.10.39.4. LastModifiedFabricIndex Field
This  field  SHALL  indicate  the  credential’s  last  modifier  fabric  index.  LastModifiedFabricIndex
SHALL be null if CredentialExists is set to False or when the modifier fabric cannot be determined
(for example, when credential was modified outside the Interaction Model) and SHALL NOT be null
otherwise. This value SHALL be set to 0 if the last modifier fabric was deleted.
5.2.10.39.5. NextCredentialIndex Field
This field SHALL indicate the next occupied index in the database for the credential type requested,
which is useful for quickly identifying occupied credential slots in the database. This SHALL NOT be
null if there is at least one occupied entry after the requested credential index in the corresponding
database and SHALL be null if there are no more occupied entries. The NextCredentialIndex
reported SHALL NOT exceed the maximum number of credentials for a particular credential type.
5.2.10.39.6. CredentialData
This field SHALL indicate the credential data for the requested user index.
If  the  CredentialType  in  the  GetCredentialStatus  command  was  not  AliroCredentialIssuerKey,
AliroEvictableEndpointKey, or AliroNonEvictableEndpointKey, this field SHALL NOT be included.
Otherwise, if CredentialExists is false this field SHALL be null.
Otherwise, the value of this field SHALL be the value of the relevant credential, as a 65-byte uncom
pressed elliptic curve public key as defined in section 2.3.3 of SEC 1.
Since the Aliro credentials are public keys, there is no security risk in allowing them
NOTE to be read. Possession of the credential octet string does not allow operating the
lock.
5.2.10.40. ClearCredential Command
Clear one, one type, or all credentials except ProgrammingPIN credential.

_Table parsed from section 'Commands':_

* In the Door Lock Cluster, under the Commands section, the table row describes an element with the ID '0', named 'Credential', which is of the type 'CredentialStruct'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed. Despite this, the 'Conformance' is marked as 'M', which means that the 'Credential' element is mandatory and always required according to the Matter specification. This presents a contradiction between the 'Quality' and 'Conformance' fields, suggesting that while the element is mandatory, it is simultaneously disallowed, which may require further clarification or context from the broader documentation.

Fields used for different use cases:

_Table parsed from section 'Commands':_

* The table row pertains to the "Clear a single credential" command within the Door Lock Cluster's Commands section. This command allows for the removal of a specific credential from the lock system. The description specifies that the `CredentialType` within the Credential structure must be set to the type of credential intended for removal, and it must not be set to `ProgrammingPIN`. Additionally, the `CredentialIndex` must be set to identify the specific credential to be cleared. Upon successful execution of this command, a `LockUserChange` event is triggered. The conformance rule for this command is not explicitly provided in the data, but based on the context, it is likely a mandatory feature for devices implementing this cluster, ensuring that they can manage credentials effectively.

structure
SHALL be set to the credential type to be
structure
structure
SHALL be set to the credential index to be
A LockUserChange event SHALL be generated

_Table parsed from section 'Commands':_

* This entry describes a command within the Door Lock Cluster, specifically the "Clear all credentials of one type" use case. The command requires that the `CredentialType` in the Credential structure be set to the type of credential that needs to be cleared, but it must not be set to `ProgrammingPIN`. Additionally, the `CredentialIndex` should be set to `0xFFFE` to indicate that all credentials of the specified type should be cleared. Upon successful execution, a single `LockUserChange` event must be generated, with the `DataIndex` set to the `CredentialIndex` in the Credential structure. The conformance rule for this command is not explicitly stated in the provided data, but based on the context, it likely follows a mandatory or optional condition depending on the specific features or requirements of the implementation.

* In the Door Lock Cluster, under the Commands section, the entry titled "Clear all credentials of all types" describes a command that clears all credentials except the ProgrammingPIN. When executed, the Credential field must be null, and for each type of credential cleared, a LockUserChange event is triggered with the LockDataType corresponding to the cleared credential. The DataIndex for this event is set to 0xFFFE. The conformance rule for this command is not explicitly provided in the row data, but based on the description, it implies that the command is likely mandatory for devices implementing this cluster, as it specifies clear operational requirements and event generation, which are typical of mandatory features.

For each credential cleared whose user doesn’t have another valid credential, the corresponding
user record SHALL be reset back to default values and its UserStatus value SHALL be set to Avail
able and UserType value SHALL be set to UnrestrictedUser and all schedules SHALL be cleared. In
this case a LockUserChange event SHALL be generated for the user being cleared.
Return status SHALL be one of the following values:

_Table parsed from section 'Commands':_

* The table row entry for the Door Lock Cluster under the Commands section describes a command named "SUCCESS," which indicates that clearing the requested credential was successful. The conformance rule for this command is not explicitly provided in the data you shared, but typically, such a command would be associated with a conformance rule indicating when it is required or optional. If we assume a conformance rule like `M`, it would mean that the "SUCCESS" command is mandatory and must always be implemented in devices supporting the Door Lock Cluster. If the conformance rule were more complex, such as `AB, O`, it would mean the command is mandatory if a specific feature `AB` is supported; otherwise, it is optional. Without the specific conformance string, we can only infer that this command is crucial for indicating successful credential clearance, and its implementation depends on the conformance rules outlined in the Matter specification.

* The table row entry pertains to the "FAILURE" command within the Door Lock Cluster's Commands section. This command is used to indicate that an unexpected internal error occurred while attempting to clear a requested credential. The conformance rule for this command is not explicitly provided in the data, suggesting that further details might be described elsewhere in the documentation. Typically, this would mean that the conformance is complex and cannot be captured by a simple tag or expression, aligning with the "desc" tag in the conformance interpretation guide. Therefore, to fully understand when and how this command should be implemented, one would need to refer to the detailed description provided in the broader Matter specification documentation.

* The table row entry for the Door Lock Cluster under the Commands section describes a command named 'INVALID_COMMAND', which is used when one or more fields violate constraints or are invalid. The conformance rule for this command is not explicitly provided in the data, but based on the context and typical usage in IoT specifications, it likely serves as a mechanism for error handling or signaling when an operation cannot be completed due to invalid input. Without a specific conformance tag or expression, it suggests that the command's inclusion and implementation details might be described elsewhere in the documentation, possibly under a 'desc' conformance tag. This means that the command's necessity and usage are likely conditional or context-dependent, requiring further reference to the detailed specification for precise implementation guidance.

5.2.10.40.1. Credential Field
This field SHALL contain a credential structure that contains the CredentialTypeEnum and the cre
dential index (0xFFFE for all credentials or 0 if not applicable) to clear. This SHALL be null if clear
ing all credential types otherwise it SHALL NOT be null.
5.2.10.41. UnboltDoor Command
This command causes the lock device to unlock the door without pulling the latch. This command
includes an optional code for the lock. The door lock MAY require a code depending on the value of
the RequirePINForRemoteOperation attribute.
If the attribute AutoRelockTime is supported, the lock will transition to the locked
NOTE
state when the auto relock time has expired.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "PINCode" command, which is of type "octstr" (octet string). The conformance rule `[COTA & PIN` indicates that this command is optional if both the COTA (presumably a feature related to over-the-air updates) and PIN (a feature related to personal identification numbers) features are supported. The use of brackets around the expression `[COTA & PIN` signifies that the command is not mandatory but becomes optional under the specified condition. If the condition is not met, the command is not required.

[COTA & PIN]
5.2.10.41.1. PINCode Field
See PINCode field.
5.2.10.42. SetAliroReaderConfig Command
This command allows communicating an Aliro Reader configuration, as defined in [Aliro], to the
lock.

_Table parsed from section 'Commands':_

* The table row describes a command within the Door Lock Cluster, specifically the "SigningKey" command. This command is identified by the ID '0' and is of type 'octstr', with a constraint indicating a length of 32. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "SigningKey" command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically identified as 'VerificationKey'. This command is of type 'octstr' with a constraint of '65', indicating it likely involves an octet string with a maximum length of 65 bytes. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'VerificationKey' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'GroupIdentifier' command. This command has an ID of '2' and is of type 'octstr' with a constraint of '16', indicating it likely involves an octet string with a maximum length of 16. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the 'GroupIdentifier' command is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes a command within the Door Lock Cluster, specifically the 'GroupResolvingKey' command, which is identified by the ID '3'. This command is of type 'octstr' and has a constraint of '16', indicating the expected data format or size. The conformance rule 'ALBU' suggests a conditional requirement based on the presence of certain features or conditions. However, without specific definitions for 'ALBU' within the provided conformance guide, it is not possible to directly interpret this string using the given rules. Typically, such a string would be broken down into individual feature codes or conditions that determine when the command is mandatory, optional, or otherwise. In this context, additional documentation or definitions for 'ALBU' would be necessary to fully understand the conformance requirements for the 'GroupResolvingKey' command.

5.2.10.42.1. SigningKey Field
This field SHALL indicate the signing key component of the Reader’s key pair.
5.2.10.42.2. VerificationKey Field
This field SHALL indicate the verification key component of the Reader’s key pair. This SHALL be
an uncompressed elliptic curve public key as defined in section 2.3.3 of SEC 1.
5.2.10.42.3. GroupIdentifier Field
This field SHALL indicate the reader group identifier for the lock.
5.2.10.42.4. GroupResolvingKey Field
This field SHALL indicate the group resolving key for the lock.
5.2.10.42.5. Effect on Receipt
1. If the lock already has an Aliro Reader configuration defined, (i.e. the AliroReaderVerification
Key attribute is not null), the response SHALL be INVALID_IN_STATE.
This avoids accidentally overwriting values that were just set by a different
NOTE administrator. If overwriting those is desired, they should be explicitly cleared
with the ClearAliroReaderConfig command.
2. Otherwise:
a. The door lock server SHALL save the SigningKey internally.
b. The AliroReaderVerificationKey attribute SHALL be set to the value of VerificationKey.
c. The AliroReaderGroupIdentifier attribute SHALL be set to the value of GroupIdentifier.
d. If the AliroBLEUWB feature is supported, the AliroGroupResolvingKey attribute SHALL be
set to the value of GroupResolvingKey.
e. The response SHALL be SUCCESS.
5.2.10.43. ClearAliroReaderConfig Command
This command allows clearing an existing Aliro Reader configuration for the lock.
Administrators SHALL NOT clear an Aliro Reader configuration without explicit user permission.
Using this command will revoke the ability of all existing Aliro user devices that
NOTE have the old verification key to interact with the lock. This effect is not restricted to
a single fabric or otherwise scoped in any way.
5.2.10.43.1. Effect on Receipt
On receipt of this command:
1. The door lock server SHALL clear out the stored SigningKey.
2. The  AliroReaderVerificationKey  and  AliroReaderGroupIdentifier  attributes  SHALL  be  set  to
null.
3. If the AliroBLEUWB feature is supported, the AliroGroupResolvingKey attribute SHALL be set to
null.

## Events
This cluster SHALL support these events:

_Table parsed from section 'Events':_

* The table row describes an event within the Door Lock Cluster, specifically the "DoorLockAlarm" event, which has an ID of '0x00'. This event is categorized with a 'CRITICAL' priority, indicating its high importance in the system. The 'Access' field is marked as 'V', which typically denotes that the event is visible or accessible in some way, though the specific meaning of 'V' would depend on the broader context of the specification. The 'Conformance' field is marked as 'M', meaning that the "DoorLockAlarm" event is mandatory. This implies that any implementation of the Door Lock Cluster must include this event, as it is a required element of the specification without any conditions or exceptions.

* The table row describes an event within the Door Lock Cluster, specifically the "DoorStateChange" event, identified by the ID '0x01'. The priority of this event is described elsewhere in the documentation, as indicated by 'desc'. The access level is marked as 'V', which typically denotes a specific access requirement or visibility level. The conformance rule 'DPS' indicates that this event is currently in a provisional state ('P'), meaning its status is temporary and subject to change. It is expected to become mandatory ('M') in the future. The 'D' suggests that there might be elements related to this event that are deprecated, but the primary focus here is on its provisional status. Overall, this entry highlights an event that is temporarily provisional but anticipated to be required in future iterations of the specification.

_Table parsed from section 'Events':_

* The table row describes an event within the Door Lock Cluster, specifically the "LockOperation" event, identified by the ID '0x02'. This event has a priority level that is described elsewhere in the documentation, as indicated by the 'desc' tag. The access level for this event is marked as 'V', which typically denotes a specific access requirement or visibility level. The conformance rule for this event is 'M', meaning it is mandatory. This indicates that the "LockOperation" event is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an event within the Door Lock Cluster, specifically the "LockOperationError" event, identified by the ID '0x03'. This event is characterized by a priority that is described elsewhere in the documentation, and it requires 'V' access, which typically refers to a specific access level or permission needed to interact with the event. The conformance rule for this event is 'M', meaning it is mandatory. This indicates that the "LockOperationError" event must always be implemented and supported in any device or application that utilizes the Door Lock Cluster, with no conditions or exceptions.

* The table row describes an event within the Door Lock Cluster, specifically the "LockUserChange" event, identified by the ID '0x04'. This event has a priority level of 'INFO', indicating it provides informational updates. The access level is 'V', which typically means it is visible or accessible for certain operations or roles. The conformance rule for this event is 'USR', meaning it is mandatory if the feature 'USR' (likely representing a User Management feature) is supported. In other words, if the Door Lock Cluster supports user management capabilities, the "LockUserChange" event must be implemented.

The Events specified in this cluster are not intended to define the user experience. The events are
only intended to define the metadata format used to notify any nodes that have subscribed for
updates.
If the DoorState reported in the DoorStateChange event is not DoorClosed then the priority SHALL
be CRITICAL; otherwise it MAY be INFO.
If the LockOperationType reported in the LockOperation event is Unlock or ForcedUserEvent then
the priority SHALL be CRITICAL; otherwise it MAY be INFO.
If the OperationError reported in the LockOperationError event is DisabledUserDenied or the Lock
OperationType is Lock the priority SHALL be CRITICAL; otherwise it MAY be INFO.
5.2.11.1. DoorLockAlarm Event
The door lock server provides several alarms which can be sent when there is a critical state on the
door lock. The alarms available for the door lock server are listed in AlarmCodeEnum.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the Door Lock Cluster, under the Events section, the table row describes an event with the ID '0' named 'AlarmCode', which is of the type 'AlarmCodeEnum' and applies to all constraints. The conformance rule for this event is marked as 'M', meaning it is mandatory. This indicates that the 'AlarmCode' event must always be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

5.2.11.1.1. AlarmCode Field
This field SHALL indicate the alarm code of the event that has happened.
5.2.11.2. DoorStateChange Event
The door lock server sends out a DoorStateChange event when the door lock door state changes.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event within the Door Lock Cluster, specifically the "DoorState" event. This event is identified by the ID '0' and uses the data type 'DoorStateEnum'. The constraint 'all' indicates that this event applies universally within the context of the Door Lock Cluster. The conformance rule 'M' signifies that the "DoorState" event is mandatory. This means that any implementation of the Door Lock Cluster must include this event without exception. The mandatory status ensures that the "DoorState" event is always present, providing essential functionality for the cluster.

5.2.11.2.1. DoorState Field
This field SHALL indicate the new door state for this door event.
5.2.11.3. LockOperation Event
The door lock server sends out a LockOperation event when the event is triggered by the various
lock operation sources.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an element within the Door Lock Cluster, specifically an event named "LockOperationType." This event is characterized by the type "LockOperationTypeEnum" and applies universally, as indicated by the constraint "all." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "LockOperationType" event is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an element within the Door Lock Cluster, specifically an event named "OperationSource" with an ID of '1'. The type of this event is "OperationSourceEnum", and it applies to all constraints. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "OperationSource" event is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row entry describes an element within the Door Lock Cluster, specifically an event named "UserIndex" with an ID of '2'. This event is of type 'uint16', indicating it uses a 16-bit unsigned integer. The constraint 'all' suggests that this event applies universally within its context. The quality 'X' indicates that this element is explicitly disallowed, meaning it should not be implemented or used. The conformance rule 'M' signifies that, despite being disallowed in terms of quality, the element is mandatory according to the specification. This means that, under normal circumstances, the "UserIndex" event must be included in any implementation of the Door Lock Cluster, although its usage is restricted by its disallowed quality status.

* In the context of the Door Lock Cluster's Events section, the table row describes an element with the ID '3', named 'FabricIndex', which is of type 'fabric-idx' and has a constraint labeled as 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', meaning that the 'FabricIndex' element is mandatory and always required within this context. This implies that regardless of any conditions or features, the 'FabricIndex' must be implemented as part of the Door Lock Cluster's Events.

* In the context of the Door Lock Cluster, the table row describes an event with the ID '4' named 'SourceNode', which is of the type 'node-id' and applies to all constraints. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', meaning that the 'SourceNode' event is a mandatory element within the Door Lock Cluster. This means that the 'SourceNode' event must always be implemented and supported in any device or application that conforms to the Matter specification for this cluster.

* The table row describes an event within the Door Lock Cluster, specifically focusing on the "Credentials" event. This event is identified by the ID '5' and is of the type 'list[CredentialStruct]', which means it involves a list of credential structures. The constraint for this event is defined as "1 to NumberOfCredentialsSupportedPerUser," indicating that the number of credentials must be between one and the maximum number supported per user. The quality of this event is marked as 'X', meaning it is explicitly disallowed. The conformance rule '[USR]' indicates that the "Credentials" event is optional if the condition 'USR' is true, where 'USR' likely refers to a specific feature or condition related to user support within the Door Lock Cluster. If 'USR' is not supported, the event is not required.

• If the door lock server supports the Unbolt Door command, it SHALL generate a LockOperation
event with LockOperationType set to Unlock after an Unbolt Door command succeeds.
• If the door lock server supports the Unbolting feature and an Unlock Door command is per
formed, it SHALL generate a LockOperation event with LockOperationType set to Unlatch when
the  unlatched  state  is  reached  and  a  LockOperation  event  with  LockOperationType  set  to
Unlock when the lock successfully completes the unlock → hold latch → release latch and
return to unlock state operation.
• If the command fails during holding or releasing the latch but after passing the unlocked state,
the door lock server SHALL generate a LockOperationError event with LockOperationType set
to Unlatch and a LockOperation event with LockOperationType set to Unlock.
◦ If it fails before reaching the unlocked state, the door lock server SHALL generate only a
LockOperationError event with LockOperationType set to Unlock.
• Upon manual actuation, a door lock server that supports the Unbolting feature:
◦ SHALL generate a LockOperation event of LockOperationType Unlatch when it is actuated
from the outside.
◦ MAY generate a LockOperation event of LockOperationType Unlatch when it is actuated
from the inside.
5.2.11.3.1. LockOperationType Field
This field SHALL indicate the type of the lock operation that was performed.
5.2.11.3.2. OperationSource Field
This field SHALL indicate the source of the lock operation that was performed.
5.2.11.3.3. UserIndex Field
This field SHALL indicate the UserIndex who performed the lock operation. This SHALL be null if
there is no user index that can be determined for the given operation source. This SHALL NOT be
null if a user index can be determined. In particular, this SHALL NOT be null if the operation was
associated with a valid credential.
5.2.11.3.4. FabricIndex Field
This field SHALL indicate the fabric index of the fabric that performed the lock operation. This
SHALL be null if there is no fabric that can be determined for the given operation source. This
SHALL NOT be null if the operation source is "Remote".
5.2.11.3.5. SourceNode Field
This field SHALL indicate the Node ID of the node that performed the lock operation. This SHALL be
null if there is no Node associated with the given operation source. This SHALL NOT be null if the
operation source is "Remote".
5.2.11.3.6. Credentials Field
This field SHALL indicate the list of credentials used in performing the lock operation. This SHALL
be null if no credentials were involved.
5.2.11.4. LockOperationError Event
The door lock server sends out a LockOperationError event when a lock operation fails for various
reasons.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an event within the Door Lock Cluster, specifically the 'LockOperationType' event. This event is identified by the ID '0' and is of the type 'LockOperationTypeEnum', which likely enumerates different types of lock operations. The 'Constraint' field is marked as 'all', indicating that this event applies universally within the context of the Door Lock Cluster. The 'Conformance' field is marked with 'M', meaning that the 'LockOperationType' event is mandatory. This implies that any implementation of the Door Lock Cluster must include this event, as it is a required element without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Events section, the table row describes an element with the ID '1' named 'OperationSource', which is of the type 'OperationSourceEnum' and has a constraint labeled as 'all'. The conformance rule for this element is marked as 'M', which stands for Mandatory. This means that the 'OperationSource' element is always required to be implemented in any device or system that supports the Door Lock Cluster, without any conditions or exceptions. This ensures that the source of operation is consistently tracked and reported across all implementations of this cluster.

_Table parsed from section 'Events':_

* The table row describes an event within the Door Lock Cluster, specifically the "OperationError" event. This event is identified by the ID '2' and is of the type 'OperationErrorEnum', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "OperationError" event is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, within the Events section, the table row describes an element with the ID '3' named 'UserIndex'. This element is of type 'uint16', indicating it is a 16-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is marked as 'M', which means that the 'UserIndex' element is mandatory and must always be included in implementations of the Door Lock Cluster according to the Matter specification.

* The table row describes an element within the Door Lock Cluster, specifically an event named "FabricIndex" with an ID of '4'. This event is of the type 'fabric-idx' and applies universally, as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'X', which typically means this element is not allowed; however, this may be context-specific or overridden by the conformance rule. The 'Conformance' is marked as 'M', meaning that the "FabricIndex" event is mandatory and must always be implemented within the Door Lock Cluster according to the Matter specification. This requirement is unconditional, with no dependencies or conditions altering its mandatory status.

* In the context of the Door Lock Cluster, specifically within the Events section, the table row describes an element with the ID '5' named 'SourceNode', which is of the type 'node-id' and has a constraint labeled as 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' is marked as 'M', meaning that the 'SourceNode' element is mandatory and must always be included in implementations of the Door Lock Cluster. This requirement is unconditional, with no dependencies or conditions affecting its mandatory status.

* In the Door Lock Cluster, under the Events section, there is an entry for an event named "Credentials" with an ID of '6'. This event is of the type 'list[CredentialStruct]', which means it is a list containing structures related to credentials. The constraint for this list is defined as ranging from 1 to the value specified by 'NumberOfCredentialsSupportedPerUser', indicating the minimum and maximum number of credentials that can be supported per user. The quality of this event is marked as 'X', meaning it is explicitly disallowed. The conformance rule '[USR]' indicates that the inclusion of this event is optional if the condition 'USR' is true, where 'USR' likely refers to a specific feature or condition related to user support within the Matter specification.

5.2.11.4.1. LockOperationType Field
This field SHALL indicate the type of the lock operation that was performed.
5.2.11.4.2. OperationSource Field
This field SHALL indicate the source of the lock operation that was performed.
5.2.11.4.3. OperationError Field
This field SHALL indicate the lock operation error triggered when the operation was performed.
5.2.11.4.4. UserIndex Field
This field SHALL indicate the lock UserIndex who performed the lock operation. This SHALL be null
if there is no user id that can be determined for the given operation source.
5.2.11.4.5. FabricIndex Field
This field SHALL indicate the fabric index of the fabric that performed the lock operation. This
SHALL be null if there is no fabric that can be determined for the given operation source. This
SHALL NOT be null if the operation source is "Remote".
5.2.11.4.6. SourceNode Field
This field SHALL indicate the Node ID of the node that performed the lock operation. This SHALL be
null if there is no Node associated with the given operation source. This SHALL NOT be null if the
operation source is "Remote".
5.2.11.4.7. Credentials Field
This field SHALL indicate the list of credentials used in performing the lock operation. This SHALL
be null if no credentials were involved.
5.2.11.5. LockUserChange Event
The door lock server sends out a LockUserChange event when a lock user, schedule, or credential
change has occurred.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* The table row describes an element within the Door Lock Cluster, specifically an event named 'LockDataType' with an ID of '0'. This event is of the type 'LockDataTypeEnum' and applies to all constraints. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'LockDataType' event is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* The table row describes an event within the Door Lock Cluster, specifically the "DataOperationType" event. This event is identified by the ID '1' and uses the data type 'DataOperationTypeEnum'. The constraint 'all' indicates that this event applies universally within its context. The conformance rule 'M' signifies that the "DataOperationType" event is mandatory, meaning it is always required to be implemented in any device or system that supports the Door Lock Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* The table row describes an event within the Door Lock Cluster, specifically the "OperationSource" event. This event is identified by the ID '2' and is of the type 'OperationSourceEnum'. The constraint specifies the possible sources of operation, which include 'Aliro', 'Unspecified', 'Keypad', and 'Remote'. The conformance rule for this event is marked as 'M', which stands for Mandatory. This means that the "OperationSource" event is always required to be implemented in any device or application that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, within the Events section, the table row describes an element with the ID '3' named 'UserIndex'. This element is of type 'uint16', which indicates it is a 16-bit unsigned integer, and it has a constraint labeled as 'all', suggesting it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is marked as 'M', which signifies that the 'UserIndex' element is mandatory. This means that it is always required to be implemented in any system or device that supports the Door Lock Cluster, without any conditions or exceptions.

* In the Door Lock Cluster, under the Events section, the table row describes an element with the ID '4' named 'FabricIndex', which is of type 'fabric-idx' and has a constraint labeled as 'all'. The quality of this element is marked as 'X', indicating it is explicitly disallowed. However, the conformance rule for 'FabricIndex' is 'M', meaning that despite its disallowed quality, this element is mandatory and always required according to the Matter specification. This suggests a potential contradiction or a need for further clarification in the specification, as an element cannot be both mandatory and disallowed simultaneously.

* In the context of the Door Lock Cluster's Events section, the table row describes an element with the ID '5', named 'SourceNode', which is of the type 'node-id' and has a constraint labeled as 'all'. The 'Quality' is marked as 'X', indicating that this element is explicitly disallowed in terms of quality. The 'Conformance' field is marked as 'M', which means that the 'SourceNode' element is mandatory. This implies that the 'SourceNode' must always be included and supported within the Door Lock Cluster's Events, without any conditions or exceptions.

* In the context of the Door Lock Cluster, specifically within the Events section, the table row describes an element with the ID '6' named 'DataIndex'. This element is of type 'uint16' and has a constraint labeled as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', meaning this element is explicitly disallowed in terms of quality considerations. The 'Conformance' is marked as 'M', which signifies that the 'DataIndex' element is mandatory. This means that regardless of any conditions or features, the 'DataIndex' must always be included and supported in implementations of the Door Lock Cluster.

5.2.11.5.1. LockDataType Field
This field SHALL indicate the lock data type that was changed.
5.2.11.5.2. DataOperationType Field
This field SHALL indicate the data operation performed on the lock data type changed.
5.2.11.5.3. OperationSource Field
This field SHALL indicate the source of the user data change.
5.2.11.5.4. UserIndex Field
This field SHALL indicate the lock UserIndex associated with the change (if any). This SHALL be
null if there is no specific user associated with the data operation. This SHALL be 0xFFFE if all users
are affected (e.g. Clear Users).
5.2.11.5.5. FabricIndex Field
This field SHALL indicate the fabric index of the fabric that performed the change (if any). This
SHALL be null if there is no fabric that can be determined to have caused the change. This SHALL
NOT be null if the operation source is "Remote".
5.2.11.5.6. SourceNode Field
This field SHALL indicate the Node ID that performed the change (if any). The Node ID of the node
that performed the change. This SHALL be null if there was no Node involved in the change. This
SHALL NOT be null if the operation source is "Remote".
5.2.11.5.7. DataIndex Field
This field SHALL indicate the index of the specific item that was changed (e.g. schedule, PIN, RFID,
etc.) in the list of items identified by LockDataType. This SHALL be null if the LockDataType does
not correspond to a list that can be indexed into (e.g. ProgrammingUser). This SHALL be 0xFFFE if
all  indices  are  affected  (e.g.  ClearPINCode,  ClearRFIDCode,  ClearWeekDaySchedule,  ClearYear
DaySchedule, etc.).