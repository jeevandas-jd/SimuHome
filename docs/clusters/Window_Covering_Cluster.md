
# 5.3 Window Covering Cluster

The window covering cluster provides an interface for controlling and adjusting automatic window
coverings such as drapery motors, automatic shades, curtains and blinds.

## Data Types
5.3.5.1. ConfigStatusBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Window Covering Cluster, under the Data Types section, the table row describes a feature with the bit identifier '0' and the name 'Operational'. The summary indicates that this feature signifies whether the device is operational. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the 'Operational' feature is always required to be implemented in any device that supports the Window Covering Cluster, without any conditions or exceptions.

* In the context of the Window Covering Cluster's Data Types, the table row entry for 'Bit' 1, named 'OnlineReserved', has a conformance designation of 'D'. This means that the 'OnlineReserved' element is considered deprecated according to the current Matter specification. As a deprecated element, it is obsolete and should not be used in new implementations. Existing implementations that include this element are encouraged to transition away from it, as it may be removed in future versions of the specification.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a data element named "LiftMovementReversed," which is represented by bit 2. This element indicates that the lift movement of a window covering is reversed. The conformance rule for this element is "LF," meaning it is mandatory if the feature code "LF" is supported. If the feature "LF" is not supported, the conformance rule does not apply, and the element is not required. This implies that the presence of the "LiftMovementReversed" element is contingent upon the support of the "LF" feature within the implementation.

* In the context of the Window Covering Cluster's Data Types, the table entry describes a feature named 'LiftPositionAware', which is associated with bit 3. This feature indicates support for the PositionAwareLift feature, denoted by the code 'PA_LF'. According to the conformance rule 'PA_LF', the 'LiftPositionAware' feature is mandatory if the PositionAwareLift feature is supported. This means that if a device or implementation includes the PositionAwareLift capability, it must also include the 'LiftPositionAware' feature as part of its functionality.

* In the context of the Window Covering Cluster, the data type entry for 'TiltPositionAware' is associated with bit 4 and indicates support for the PositionAwareTilt feature, abbreviated as PA_TL. According to the conformance rule 'PA_TL', this element is mandatory if the PA_TL feature is supported. This means that if a device or implementation includes the PositionAwareTilt feature, it must also include the TiltPositionAware element as part of its configuration. The absence of any brackets or additional conditions in the conformance expression signifies that there are no optional or alternative conformance scenarios for this element—it is strictly required when PA_TL is present.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '5', named 'LiftEncoderControlled'. This feature indicates that the window covering uses an encoder for lift operations. The conformance rule 'PA_LF' specifies that this feature is conditionally mandatory. It is mandatory if the feature 'PA_LF' is supported. Otherwise, the conformance status is not explicitly defined in this entry, suggesting that further context or documentation may be needed to fully understand its optionality or other status when 'PA_LF' is not supported.

* The table row describes a data type within the Window Covering Cluster, specifically concerning the 'TiltEncoderControlled' feature, which indicates the use of an encoder for tilt operations. The 'Bit' value of '6' suggests its position or identifier within a set of data. The 'Conformance' field is marked as 'PA_TL', which, according to the Matter Conformance Interpretation Guide, means that the feature is conditionally mandatory based on the presence of the 'PA_TL' condition. If the 'PA_TL' feature is supported, then 'TiltEncoderControlled' is mandatory. If 'PA_TL' is not supported, the conformance of 'TiltEncoderControlled' is not explicitly defined in this entry, implying that it might be optional or subject to further documentation.

5.3.5.1.1. Operational Bit
This bit SHALL indicate whether the window covering is operational for regular use:
• 0 = Not Operational
• 1 = Operational
5.3.5.1.2. LiftMovementReversed Bit
This bit SHALL indicate whether the lift movement is reversed:
• 0 = Lift movement is normal
• 1 = Lift movement is reversed
5.3.5.1.3. LiftPositionAware Bit
This bit SHALL indicate whether the window covering supports the PositionAwareLift feature:
• 0 = Lift control is not position aware
• 1 = Lift control is position aware (PA_LF)
5.3.5.1.4. TiltPositionAware Bit
This bit SHALL indicate whether the window covering supports the PositionAwareTilt feature:
• 0 = Tilt control is not position aware
• 1 = Tilt control is position aware (PA_TL)
5.3.5.1.5. LiftEncoderControlled Bit
This bit SHALL indicate whether a position aware controlled window covering is employing an
encoder for positioning the height of the window covering:
• 0 = Timer Controlled
• 1 = Encoder Controlled
5.3.5.1.6. TiltEncoderControlled Bit
This bit SHALL indicate whether a position aware controlled window covering is employing an
encoder for tilting the window covering:
• 0 = Timer Controlled
• 1 = Encoder Controlled
5.3.5.2. ModeBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* The table row describes a data type within the Window Covering Cluster, specifically a bit named "MotorDirectionReversed" with a value of '0'. This bit is used to reverse the lift direction of a window covering. According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Window Covering Cluster. There are no conditions or dependencies affecting its requirement status; it must be included in all relevant implementations.

* The table row pertains to the "Window Covering Cluster" within the "Data Types" section, specifically focusing on the "CalibrationMode" feature. This feature is identified by the bit value '1' and is summarized as performing a calibration. The conformance rule for "CalibrationMode" is marked as 'M', which stands for Mandatory. This means that the "CalibrationMode" feature is always required to be implemented in any device or system that supports the Window Covering Cluster, without any conditions or exceptions.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature called "MaintenanceMode," which is represented by bit 2. The purpose of this feature is to freeze all motions for maintenance purposes. According to the conformance rule 'M', this feature is mandatory, meaning it is always required to be implemented in any device or system that supports the Window Covering Cluster. There are no conditions or exceptions to this requirement, ensuring that the MaintenanceMode feature is consistently available for maintenance operations across all relevant implementations.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature named "LedFeedback," which is associated with bit 3. This feature is responsible for controlling the feedback provided by LEDs. According to the conformance rule marked as "M," this feature is mandatory, meaning it is always required to be implemented in any device or system that supports the Window Covering Cluster. There are no conditions or dependencies affecting its requirement status; it must be included as part of the implementation.

5.3.5.2.1. MotorDirectionReversed Bit
This bit SHALL control the motor direction:
• 0 = Lift movement is normal
• 1 = Lift movement is reversed
5.3.5.2.2. CalibrationMode Bit
This bit SHALL set the window covering into calibration mode:
• 0 = Normal mode
• 1 = Calibration mode
5.3.5.2.3. MaintenanceMode Bit
This bit SHALL set the window covering into maintenance mode:
• 0 = Normal mode
• 1 = Maintenance mode
5.3.5.2.4. LedFeedback Bit
This bit SHALL control feedback LEDs:
• 0 = LEDs are off
• 1 = LEDs will display feedback
5.3.5.3. OperationalStatusBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the context of the Window Covering Cluster, the table row describes a data type related to the 'Global' operational state, which is represented by bits '1..0'. The 'Conformance' field for this entry is marked as 'M', indicating that this element is mandatory. This means that the 'Global' operational state must always be implemented and supported in any device or application that conforms to the Matter specification for the Window Covering Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature related to the 'Lift' operational state, which is represented by bits 3 to 2. The 'Conformance' field for this entry is marked as 'LF', indicating that the inclusion of this feature is mandatory if the 'LF' feature is supported. In other words, if the device or implementation supports the 'LF' feature, then the 'Lift' operational state must be included as part of the Window Covering Cluster's functionality. If 'LF' is not supported, the conformance rule does not apply, and the feature is not required.

* The table row pertains to the "Window Covering Cluster" within the "Data Types" section, specifically describing a data type related to the "Tilt" operational state, which is represented by bits 5 and 4. The "Conformance" field is marked as "TL," which does not directly match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. This suggests that "TL" might be a feature code or a specific condition described elsewhere in the documentation. Without additional context or a defined meaning for "TL" in the provided guide, it is unclear whether the "Tilt" operational state is mandatory, optional, or subject to another condition. Therefore, further reference to the specific documentation where "TL" is defined would be necessary to accurately interpret its conformance status.

The OperationalStatusBitmap is using several internal operational state fields (composed of 2 bits)
following this definition:
• 00b = Currently not moving
• 01b = Currently opening (e.g. moving from closed to open).
• 10b = Currently closing (e.g. moving from open to closed).
• 11b = Reserved
5.3.5.3.1. Global Bits
These bits SHALL indicate in which direction the covering is currently moving or if it has stopped.
Global operational state SHALL always reflect the overall motion of the device.
5.3.5.3.2. Lift Bits
These bits SHALL indicate in which direction the covering’s lift is currently moving or if it has
stopped.
5.3.5.3.3. Tilt Bits
These bits SHALL indicate in which direction the covering’s tilt is currently moving or if it has
stopped.
5.3.5.4. SafetyStatusBitmap Type
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* In the context of the Window Covering Cluster, the data type entry for 'RemoteLockout' is associated with the bit value '0'. This feature ensures that movement commands are ignored, effectively locking out the device, which might occur due to reasons such as lack of authorization or being outside a specified time/date range. The conformance rule for 'RemoteLockout' is marked as 'M', indicating that this feature is mandatory. This means that any implementation of the Window Covering Cluster must include the 'RemoteLockout' feature, ensuring that the system can handle scenarios where movement commands need to be ignored under specific conditions.

* In the Window Covering Cluster, under the Data Types section, the table row describes a feature named "TamperDetection," which is represented by the bit value '1'. This feature is summarized as the detection of tampering on sensors or other safety equipment, such as when a device is forcibly moved without its actuators. The conformance rule for "TamperDetection" is marked as 'M', which means it is a Mandatory element. This indicates that the feature must always be implemented and supported in any device or system that adheres to this specification. There are no conditions or exceptions; its inclusion is required without any dependencies or optionality.

* The table row entry pertains to the "Window Covering Cluster" within the "Data Types" section and describes a specific data type identified by the bit '2', named "FailedCommunication". This data type represents a scenario where there is a communication failure with sensors or other safety equipment. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "FailedCommunication" data type is a required element in the current specification and must be implemented in any device or system that supports the Window Covering Cluster.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '3', named 'PositionFailure'. This feature indicates that the device has failed to reach the desired position, such as when a position-aware device does not reach its TargetPosition before a timeout occurs. The conformance rule for 'PositionFailure' is marked as 'M', which means this feature is mandatory. Therefore, any implementation of the Window Covering Cluster must include this feature, as it is always required according to the Matter IoT specification.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a data element named 'ThermalProtection' associated with bit 4. This element indicates whether the motor(s) and/or electric circuit thermal protection has been activated. The conformance rule for 'ThermalProtection' is marked as 'M', which stands for Mandatory. This means that the 'ThermalProtection' feature is always required to be implemented in any device or system that supports the Window Covering Cluster, without any conditions or exceptions.

* The table row describes a data type within the Window Covering Cluster, specifically focusing on the 'ObstacleDetected' bit, which is bit number 5. This bit indicates that an obstacle is preventing the actuator from moving. The conformance rule for 'ObstacleDetected' is marked as 'M', meaning it is a Mandatory element. This signifies that the 'ObstacleDetected' bit must always be implemented in any device or application that supports the Window Covering Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the context of the Window Covering Cluster, the data type entry for 'Bit' 6, named 'Power', indicates a condition where the device has a power-related issue or limitation, such as operating on a backup battery or experiencing limited power availability. The conformance rule for this entry is 'M', meaning that the 'Power' attribute is mandatory. This implies that it is always required to be implemented in any device using this cluster, without any conditions or exceptions.

* The table row describes a data type within the Window Covering Cluster, specifically focusing on a bit labeled '7', named 'StopInput'. This bit indicates that a local safety sensor, which is not directly detecting an obstacle, is preventing movement, as per safety standards like the EU Standard EN60335. The conformance rule for this bit is 'M', meaning it is mandatory. This indicates that the 'StopInput' bit must always be implemented and supported within the Window Covering Cluster, ensuring compliance with the specified safety requirements.

* The table row entry pertains to the "MotorJammed" data type within the Window Covering Cluster, specifically under the Data Types section. This entry indicates that the "MotorJammed" bit, which is 8 bits in size, is used to signal a mechanical problem related to the motor(s) being detected. The conformance rule for this entry is marked as "M," which stands for Mandatory. This means that the "MotorJammed" data type is always required to be implemented in any device or application that supports the Window Covering Cluster, without any conditions or exceptions.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '9' with the name 'HardwareFailure'. This feature pertains to issues related to the printed circuit board (PCB), fuse, and other electrical problems. The conformance rule for 'HardwareFailure' is marked as 'M', which stands for Mandatory. This means that the 'HardwareFailure' feature is always required to be implemented in any device or system that supports the Window Covering Cluster, without any conditions or exceptions.

* In the context of the Window Covering Cluster's Data Types, the table row describes a feature named "ManualOperation," which is represented by the bit value '10'. This feature indicates that the actuator is being manually operated, preventing any automatic movement by disengaging or decoupling the actuator. The conformance rule for "ManualOperation" is marked as 'M', which stands for Mandatory. This means that the feature is always required to be implemented in any device or system that supports the Window Covering Cluster, without any conditions or exceptions.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes a feature named "Protection" associated with bit 11. The summary indicates that this feature is related to the activation of protection mechanisms. The conformance rule for this feature is marked as "M," which stands for Mandatory. This means that the "Protection" feature is always required to be implemented in any device or system that supports the Window Covering Cluster, without any conditions or exceptions.

5.3.5.5. TypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the Window Covering Cluster, specifically within the Data Types section, and describes a data type with the name and summary "RollerShade," which has a value of '0'. The conformance rule for this entry is 'LF'. However, 'LF' does not match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide provided. This suggests that 'LF' might be a typographical error or an undefined conformance tag within the context of the guide. As such, without further context or clarification from the documentation, the conformance status of this entry cannot be accurately interpreted based on the given rules.

* The table row describes a data type within the Window Covering Cluster, specifically named "RollerShade2Motor," which represents a roller shade with two motors. The 'Value' assigned to this data type is '1', and it is summarized as "RollerShade - 2 Motor." The 'Conformance' field is marked as 'LF', which does not directly match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. This suggests that 'LF' might be a custom or context-specific conformance condition that requires additional documentation or context from the specification to fully understand its implications. Without further information, it is unclear whether this element is mandatory, optional, or subject to other conditions.

* The table row pertains to the "Window Covering Cluster" within the "Data Types" section and describes a specific data type with the value '2', named 'RollerShadeExterior', which is summarized as 'RollerShade - Exterior'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' does not directly match any of the basic conformance tags or logical conditions provided in the guide. This suggests that 'LF' might be a feature code or a condition specific to the context of the Window Covering Cluster, which would need to be defined elsewhere in the documentation. Without additional context or definition for 'LF', it is not possible to determine the exact conformance requirement for 'RollerShadeExterior' based solely on the information provided.

* The table row describes a data type within the Window Covering Cluster, specifically named "RollerShadeExterior2Motor," which has a value of '3' and is summarized as "RollerShade - Exterior - 2 Motor." The conformance rule for this entry is 'LF,' which, according to the Matter Conformance Interpretation Guide, is not explicitly defined in the provided rules. However, it suggests that the conformance condition might be described elsewhere in the documentation, possibly indicating a complex or context-specific requirement. Therefore, to fully understand the conformance of this data type, one would need to refer to additional documentation or sections that detail the specific conditions under which this data type is required or optional.

* In the context of the Window Covering Cluster, the table row describes a data type with the value '4', named 'Drapery', which refers to drapery or curtains. The conformance rule for this entry is 'LF', which, according to the Matter Conformance Interpretation Guide, indicates that the element is mandatory if the feature 'LF' is supported. This means that if the 'LF' feature is part of the device's capabilities, the 'Drapery' data type must be implemented. If 'LF' is not supported, the conformance rule does not specify any alternative, implying that the element is not required.

* In the context of the Window Covering Cluster's Data Types, the table row describes a data type with the value '5', named 'Awning', which is summarized as 'Awning'. The conformance rule 'LF' indicates that this element is mandatory if the feature 'LF' is supported. Therefore, if a device or implementation supports the 'LF' feature, the 'Awning' data type must be included as part of the Window Covering Cluster. If 'LF' is not supported, the conformance of this element is not specified by this rule.

* In the context of the Window Covering Cluster's Data Types, the table row describes an element named "Shutter" with a value of '6'. The summary also identifies it as "Shutter". The conformance rule for this element is 'LF | TL', which means that the "Shutter" element is mandatory if either the feature 'LF' or the feature 'TL' is supported. In simpler terms, if a device supports either the 'LF' feature or the 'TL' feature, it must also support the "Shutter" element. If neither feature is supported, the element is not required.

* The table row entry pertains to the Window Covering Cluster, specifically within the Data Types section. It describes a data type with the value '7', named 'TiltBlindTiltOnly', which summarizes as 'Tilt Blind - Tilt Only'. The conformance rule for this entry is 'TL'. According to the Matter Conformance Interpretation Guide, 'TL' is not a standard conformance tag or expression as outlined in the guide. Therefore, it might refer to a specific feature or condition not explicitly covered by the basic conformance tags or logical conditions provided. To fully understand the conformance of 'TiltBlindTiltOnly', one would need to refer to additional documentation or context specific to the Matter specification that defines 'TL'.

* The table row describes a data type within the Window Covering Cluster, specifically named "TiltBlindLiftAndTilt" with a value of '8'. This data type is summarized as "Tilt Blind - Lift & Tilt." The conformance rule for this entry is expressed as "LF & TL," which means that the "TiltBlindLiftAndTilt" data type is mandatory if both the features represented by the codes "LF" (likely referring to a Lift feature) and "TL" (likely referring to a Tilt feature) are supported. In other words, the data type must be implemented when both of these features are present in the device's functionality.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Window Covering Cluster" within the "Data Types" section and describes a specific data type with the value '9', named 'ProjectorScreen', which represents a projector screen. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is not a standard conformance tag or expression as outlined in the guide. Therefore, without additional context or documentation specifying what 'LF' stands for, it is unclear how this conformance should be interpreted. Typically, conformance tags like 'M', 'O', 'P', 'D', 'X', or 'desc' are used to define the requirement status of an element. In this case, further clarification from the relevant documentation would be necessary to understand the conformance implications for 'ProjectorScreen'.

* In the context of the Window Covering Cluster's Data Types, the table row describes an entry with the 'Value' of '255', named 'Unknown', with a summary also labeled as 'Unknown'. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'Unknown' data type is not required to be implemented in devices that support the Window Covering Cluster. There are no dependencies or conditions that affect its optional status, allowing manufacturers the flexibility to include or exclude this data type based on their design preferences or specific use cases.

5.3.5.6. EndProductTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Window Covering Cluster, the table row describes a data type with the value '0', named 'RollerShade', which represents a 'Simple Roller Shade'. The conformance rule 'LF' indicates that this element is subject to a specific condition or description that is not straightforwardly expressed with basic tags or logical conditions. In this case, 'LF' suggests that the conformance of the 'RollerShade' data type is described elsewhere in the documentation, likely under a section that provides detailed conditions or scenarios under which this data type is applicable or required.

* In the context of the Window Covering Cluster's Data Types, the table entry describes a data type with the value '1', named 'RomanShade', which represents a Roman Shade. The conformance rule 'LF' indicates that this element is mandatory if the feature 'LF' is supported. There are no additional conditions or alternatives provided, so the presence of the 'RomanShade' data type is required whenever the 'LF' feature is part of the implementation.

* In the context of the Window Covering Cluster's Data Types, the table row describes an entry with the value '2', named 'BalloonShade', which represents a type of window covering known as a Balloon Shade. The 'Conformance' field for this entry is marked as 'LF'. However, 'LF' does not match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide provided. This suggests that 'LF' might be a specific feature code or condition relevant to the Matter specification that requires further context or documentation to interpret accurately. Without additional information, the conformance status of 'BalloonShade' under the 'LF' condition remains unclear.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table entry describes a data type with the value '3' named 'WovenWood', which is summarized as 'Woven Wood'. The conformance rule for this entry is 'LF'. However, 'LF' does not match any of the basic conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide provided. This suggests that 'LF' might be a typographical error, an undefined conformance tag, or a placeholder that requires further clarification from additional documentation. As it stands, without a defined meaning for 'LF', the conformance status of 'WovenWood' cannot be accurately interpreted based on the provided guide.

* In the context of the Window Covering Cluster's Data Types, the table entry describes a data type with the value '4', named 'PleatedShade', which represents a pleated shade. The conformance rule for this entry is 'LF', which is not explicitly defined in the provided conformance interpretation guide. However, based on typical conventions, 'LF' could imply a specific condition or feature requirement not covered by the basic tags or logical expressions outlined. Without additional context or documentation, the exact meaning of 'LF' remains unclear, but it suggests that the inclusion of the 'PleatedShade' data type is contingent upon a specific, possibly less common condition or feature within the Matter specification.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes an element with the name 'CellularShade', which has a value of '5' and is summarized as 'Cellular Shade'. The conformance rule for this element is 'LF'. However, 'LF' does not appear to match any of the standard conformance tags or logical conditions outlined in the Matter Conformance Interpretation Guide. This suggests that 'LF' might be a specific feature code or condition relevant to the Window Covering Cluster that is not covered by the basic conformance tags provided. Without additional context or documentation explaining 'LF', it is unclear whether this element is mandatory, optional, or subject to another condition. Therefore, further clarification from the relevant Matter specification documentation would be needed to accurately interpret the conformance of 'CellularShade'.

* In the context of the Window Covering Cluster's Data Types, the table entry describes a data type with the value '6', named 'LayeredShade', which represents a 'Layered Shade'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is not directly defined in the provided rules, suggesting it might be a specific feature code or condition relevant to the Window Covering Cluster. In this case, the conformance rule implies that the 'LayeredShade' data type is mandatory if the feature or condition 'LF' is supported. If 'LF' is not supported, the conformance of 'LayeredShade' is not explicitly defined by this entry and would need to be interpreted based on additional context or documentation related to 'LF'.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes an entry with the value '7', named 'LayeredShade2D', which is summarized as 'Layered Shade 2D'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is not explicitly defined in the basic conformance tags or expressions provided. This suggests that 'LF' might be a specific feature code or condition relevant to the Window Covering Cluster that determines when the 'LayeredShade2D' data type is required. Without additional context or documentation on what 'LF' represents, it is unclear whether this element is mandatory, optional, or subject to other conditions. Therefore, further reference to the specific documentation for the Window Covering Cluster would be necessary to fully understand the conformance requirement for 'LayeredShade2D'.

* In the context of the Window Covering Cluster's Data Types, the table row describes an entry with the value '8', named 'SheerShade', which represents a 'Sheer Shade'. The conformance rule 'LF & TL' indicates that the 'SheerShade' element is mandatory if both the features 'LF' and 'TL' are supported. This means that for any implementation of the Window Covering Cluster, the 'SheerShade' data type must be included if the conditions of supporting both 'LF' and 'TL' features are met. If either or both of these features are not supported, the requirement for 'SheerShade' does not apply.

* In the context of the Window Covering Cluster's Data Types, the table row describes a data type with the value '9', named 'TiltOnlyInteriorBlind', which represents a 'Tilt Only Interior Blind'. The conformance rule 'TL' indicates that this element is mandatory if the feature 'TL' (presumably a feature related to tilt functionality) is supported. If the feature 'TL' is not supported, the conformance rule does not specify any alternative, implying that the element is not required. Therefore, the 'TiltOnlyInteriorBlind' data type must be implemented in devices that support the 'TL' feature within the Window Covering Cluster.

* In the context of the Window Covering Cluster, specifically under Data Types, the entry for 'InteriorBlind' with a value of '10' represents a type of window covering identified as an "Interior Blind." The conformance rule 'LF & TL' indicates that the inclusion of this element is mandatory if both the features represented by 'LF' and 'TL' are supported. This means that for any implementation of the Window Covering Cluster, the 'InteriorBlind' data type must be included if the conditions specified by 'LF' and 'TL' are met, ensuring that the system supports both features simultaneously.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the entry for 'VerticalBlindStripCurtain' with a value of '11' represents a specific type of window covering characterized as a vertical blind or strip curtain. The conformance rule 'LF & TL' indicates that this element is mandatory if both the features represented by the codes 'LF' and 'TL' are supported. This means that for devices or implementations that include both of these features, the 'VerticalBlindStripCurtain' data type must be included as part of the specification.

* In the context of the Window Covering Cluster's Data Types, the table row describes an element named "InteriorVenetianBlind" with a value of '12' and a summary of "Interior Venetian Blind." The conformance rule for this element is expressed as "LF & TL," which means that the "InteriorVenetianBlind" element is mandatory if both the features or conditions represented by the codes "LF" and "TL" are supported. If either or both of these conditions are not met, the element is not required. This conformance rule ensures that the element is only included when both specific features are present, aligning with the logical AND condition specified.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes an element with the value '13' named 'ExteriorVenetianBlind', which refers to an exterior Venetian blind. The conformance rule 'LF & TL' indicates that this element is mandatory if both the features 'LF' and 'TL' are supported. This means that for devices or implementations where both these features are present, the 'ExteriorVenetianBlind' element must be included. If either 'LF' or 'TL' is not supported, the element is not required.

* The table row describes an entry within the Window Covering Cluster, specifically under the Data Types section. The entry is for a data type named "LateralLeftCurtain," which is summarized as "Lateral Left Curtain" and has a value of '14'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is a feature code that would need to be defined elsewhere in the documentation. In this context, the conformance rule indicates that the "LateralLeftCurtain" data type is mandatory if the feature 'LF' is supported by the device. If 'LF' is not supported, the conformance of this data type is not specified in this entry, implying it may not be required.

* In the context of the Window Covering Cluster, the table row describes a data type with the value '15', named 'LateralRightCurtain', which is summarized as 'Lateral Right Curtain'. The conformance rule for this entry is 'LF', which is a feature code indicating a specific condition or feature within the Matter specification. According to the Matter Conformance Interpretation Guide, the absence of brackets around 'LF' implies that the 'LateralRightCurtain' data type is mandatory if the feature 'LF' is supported. If 'LF' is not supported, the conformance rule does not specify an alternative, suggesting that the data type would not be required.

* In the context of the Window Covering Cluster, the table row describes a data type with the value '16', named 'CentralCurtain', which is summarized as 'Central Curtain'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' does not directly correspond to any of the basic conformance tags or logical conditions provided. Therefore, it suggests that the conformance for 'CentralCurtain' is likely described elsewhere in the documentation, possibly under a specific feature or condition related to 'LF'. This means that the requirement status of 'CentralCurtain' is not immediately clear from the table and should be looked up in the detailed documentation for further clarification.

* The table row entry pertains to the "Window Covering Cluster" within the "Data Types" section and describes a data type with the value '17', named 'RollerShutter', which is summarized as 'Roller Shutter'. The conformance rule for this entry is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is not a standard conformance tag or expression as outlined in the guide. It might refer to a specific feature or condition not explicitly covered in the basic conformance tags or logical conditions provided. Therefore, the conformance of 'RollerShutter' would require further context or documentation to fully understand its requirements or optionality within the Matter specification.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the table row describes an element with the name "ExteriorVerticalScreen" and a value of '18', which represents an "Exterior Vertical Screen." The conformance rule for this element is 'LF'. According to the Matter Conformance Interpretation Guide, 'LF' is not a standard conformance tag or expression as outlined in the provided rules. Therefore, it suggests that the conformance for this element might be described elsewhere in the documentation, possibly under a more detailed or specific context not covered by the basic tags or logical conditions. This means that the requirements or conditions under which the "Exterior Vertical Screen" is applicable or necessary are likely detailed in another section of the Matter specification.

* The table row entry pertains to the "Window Covering Cluster" within the "Data Types" section, specifically describing a data type named "AwningTerracePatio" with a value of '19' and summarized as "Awning Terrace (Patio)." The conformance rule for this entry is 'LF,' which, according to the Matter Conformance Interpretation Guide, indicates that the conformance is described elsewhere in the documentation. This means that the conditions under which the "AwningTerracePatio" data type is required, optional, or otherwise specified are not straightforwardly expressed with basic tags or logical conditions and require further detailed explanation found in another part of the specification.

* In the context of the Window Covering Cluster, the table row describes a data type with the value '20', named 'AwningVerticalScreen', which represents an "Awning Vertical Screen." The conformance rule for this entry is 'LF', which does not match any of the specified conformance tags or expressions in the provided guide. This suggests that 'LF' might be a typographical error or an undefined conformance tag in this context. Without a clear definition from the guide, the conformance status of 'AwningVerticalScreen' remains ambiguous, and further clarification from the specification documentation would be necessary to determine its exact requirements or status.

* In the context of the Window Covering Cluster, specifically within the Data Types section, the entry for 'TiltOnlyPergola' with a value of '21' represents a type of window covering that is specifically designed to tilt, such as a pergola that can adjust its slats. The conformance rule 'LF | TL' indicates that this element is mandatory if either the feature 'LF' or 'TL' is supported. In simpler terms, if a device supports either of these features, it must also support the 'TiltOnlyPergola' data type. If neither feature is supported, the requirement does not apply.

* The table row describes a data type within the Window Covering Cluster, specifically for a feature named "SwingingShutter," which has a value of '22' and is summarized as "Swinging Shutter." The conformance rule 'LF | TL' indicates that this feature is conditionally mandatory based on the support of certain features. Specifically, the "SwingingShutter" feature is required if either the feature code 'LF' or 'TL' is supported. If at least one of these features is present, the "SwingingShutter" must be implemented; otherwise, it is not required. This rule allows for flexibility in implementation depending on the specific features supported by a device.

* The table row describes a data type within the Window Covering Cluster, specifically for a feature named "SlidingShutter," which is identified by the value '23'. The summary indicates that this data type pertains to a "Sliding Shutter." The conformance rule 'LF | TL' specifies that the "SlidingShutter" feature is mandatory if either the feature code 'LF' or 'TL' is supported. In simpler terms, if a device supports either the 'LF' or 'TL' feature, it must also support the "SlidingShutter" data type. If neither 'LF' nor 'TL' is supported, the requirement does not apply.

* In the context of the Window Covering Cluster's Data Types, the table entry describes a data type with the value '255', named 'Unknown', and summarized as 'Unknown'. The conformance rule for this entry is 'O', which stands for Optional. This means that the 'Unknown' data type is not required to be implemented in devices that support the Window Covering Cluster. There are no dependencies or conditions attached to this optional status, allowing implementers the flexibility to include or exclude this data type based on their specific needs or preferences.

## Attributes

_Table parsed from section 'Attributes':_

* In the context of the Window Covering Cluster, the table row describes an attribute with the ID `0x0000` named "Type". This attribute is of the type `TypeEnum` and has a constraint described elsewhere in the documentation. It is marked with a quality of `F`, has a default value of `0`, and is accessible with read (`R`) and view (`V`) permissions. The conformance rule for this attribute is `M`, which means it is mandatory. This implies that the "Type" attribute is always required to be implemented in any device or application that supports the Window Covering Cluster, without any conditions or exceptions.

* The table row describes an attribute named "PhysicalClosedLimitLift" within the Window Covering Cluster's Attributes section. This attribute has an ID of '0x0001' and is of type 'uint16', with a default value of '0'. It is constrained to be applicable in all contexts and has a quality rating of 'F'. The access level is 'R V', indicating it is readable and possibly volatile. The conformance rule '[LF & PA_LF & ABS]' specifies that this attribute is optional if the conditions involving the features 'LF', 'PA_LF', and 'ABS' are all supported. In other words, the attribute is not required unless all these specific features are present, in which case it becomes optional.

* The table row describes an attribute named "PhysicalClosedLimitTilt" within the Window Covering Cluster, identified by the ID '0x0002'. This attribute is of type 'uint16', applies to all constraints, and has a default value of '0'. It is accessible for reading and viewing ('R V') and is of fixed quality ('F'). The conformance rule '[TL & PA_TL & ABS]' indicates that this attribute is optional if the conditions 'TL', 'PA_TL', and 'ABS' are all supported. In other words, the attribute is not required unless all three specified features or conditions are present, in which case its inclusion becomes optional.

* The table row describes an attribute named "CurrentPositionLift1" within the Window Covering Cluster's Attributes section. This attribute has an ID of '0x0003' and is of type 'uint16'. It is constrained between 'InstalledOpenLimitLift' and 'InstalledClosedLimitLift'. The 'Quality' field indicates that this attribute is disallowed ('X') and non-reportable ('N'). The default value is 'null', and it has read ('R') and view ('V') access permissions. The conformance rule '[LF & PA_LF & ABS]' specifies that the attribute is optional if the conditions 'LF', 'PA_LF', and 'ABS' are all supported. If these conditions are not met, the attribute is not required.

* The table row describes an attribute named "CurrentPositionTilt1" within the Window Covering Cluster, identified by the ID '0x0004'. This attribute is of type 'uint16' and is constrained to values between 'InstalledOpenLimitTilt' and 'InstalledClosedLimitTilt'. It has a quality designation of 'X N', indicating it is explicitly disallowed in some contexts. The default value for this attribute is 'null', and it has read-only access with a volatile quality ('R V'). The conformance rule '[TL & PA_TL & ABS]' indicates that the attribute is optional if the conditions 'TL', 'PA_TL', and 'ABS' are all supported. If these conditions are not met, the attribute is not required.

* The table row describes an attribute named "NumberOfActuationsLift" within the Window Covering Cluster, identified by the ID '0x0005'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally ('Constraint': 'all'). The attribute is marked with a quality of 'N', has a default value of '0', and is accessible for reading and viewing ('Access': 'R V'). The conformance rule '[LF]' indicates that the attribute is optional if the feature 'LF' (likely representing a specific functionality or capability related to lift operations) is supported. If 'LF' is not supported, the attribute is not required.

* The table row describes an attribute within the Window Covering Cluster, specifically the "NumberOfActuationsTilt" attribute. This attribute has an ID of '0x0006' and is of type 'uint16', which means it is a 16-bit unsigned integer. It applies universally ('Constraint': 'all') and has a default value of '0'. The 'Access' field indicates that this attribute is readable ('R') and can be viewed ('V'). The 'Conformance' field is '[TL]', which means that the attribute is optional if the condition 'TL' is true. In other words, the attribute is not required unless the specific feature or condition represented by 'TL' is supported. If 'TL' is not supported, the attribute does not need to be included.

* The table row describes an attribute within the Window Covering Cluster, specifically the "ConfigStatus" attribute. This attribute is identified by the ID '0x0007' and is of the type 'ConfigStatusBitmap'. The 'Constraint' and 'Default' fields are described elsewhere in the documentation, indicated by 'desc'. The 'Quality' is marked as 'N', and the 'Access' is 'R V', meaning it is readable and has volatile access. The 'Conformance' is marked as 'M', which means that the "ConfigStatus" attribute is mandatory. It is always required to be implemented in any device that supports the Window Covering Cluster, without any conditions or exceptions.

* The table row describes an attribute named "CurrentPositionLiftPercentage1" within the Window Covering Cluster, identified by the ID '0x0008'. This attribute is of the 'percent' type and has a quality designation of 'X N P', indicating it is disallowed, not supported, and provisional. Its default value is 'null', and it has read and volatile access permissions ('R V'). The conformance rule '[LF & PA_LF]' specifies that this attribute is optional if both the 'LF' (Lift feature) and 'PA_LF' (Position Awareness for Lift feature) conditions are true. This means that the attribute is not required by default, but if a device supports both the Lift feature and Position Awareness for Lift, then the attribute may be included as an optional element.

* The table row describes an attribute named "CurrentPositionTiltPercentage1" within the Window Covering Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0009' and is of the type 'percent'. It is constrained to apply to all instances, with a quality designation of 'X N P', indicating it is disallowed, not applicable, and provisional. The default value for this attribute is 'null', and it has read and view access ('R V'). The conformance rule '[TL & PA_TL]' means that this attribute is optional if both the 'TL' (Tilt) and 'PA_TL' (Position Awareness for Tilt) features are supported. If these conditions are not met, the attribute is not required.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Window Covering Cluster, specifically the "OperationalStatus" attribute. This attribute is identified by the ID '0x000A' and is of the type 'OperationalStatusBitmap', with a constraint pattern of '0b00xx xxxx', indicating specific bits are used to represent its status. The quality of this attribute is marked as 'P', suggesting it is provisional, and its default value is '0'. It has read and view access, denoted by 'R V'. The conformance rule for this attribute is 'M', meaning it is mandatory and must always be implemented in any device or application that supports the Window Covering Cluster. This requirement is unconditional, with no dependencies or conditions affecting its mandatory status.

* The table row describes an attribute named "TargetPositionLiftPercent100ths 2" within the Window Covering Cluster, identified by the ID '0x000B'. This attribute is of the type 'percent100ths', and its quality is marked as 'X P', indicating it is currently disallowed but provisionally included for future consideration. The default value for this attribute is 'null', and it has read and view access ('R V'). The conformance rule 'LF & PA_LF' specifies that this attribute is mandatory if both the 'LF' (Lift Feature) and 'PA_LF' (Position Awareness for Lift) features are supported. If either of these features is not supported, the attribute is not required.

* The table row describes an attribute named "TargetPositionTiltPercent100ths 2" within the Window Covering Cluster, identified by the ID '0x000C'. This attribute is of the type 'percent100ths', with a default value of 'null', and it has read and view access ('R V'). The quality of this attribute is marked as 'X P', indicating it is currently disallowed but provisionally might change in the future. The conformance rule 'TL & PA_TL' means that this attribute is mandatory if both the 'TL' and 'PA_TL' features are supported. In essence, this attribute must be implemented if the device supports both of these specific features, otherwise, it is not required.

* In the context of the Window Covering Cluster, the table row describes an attribute named "EndProductType" with an ID of '0x000D'. This attribute is of the type 'EndProductTypeEnum' and has a default value of '0'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Quality' is labeled as 'F', and the 'Access' is specified as 'R V', meaning it is readable and possibly volatile. The 'Conformance' is marked as 'M', which means that the "EndProductType" attribute is mandatory and must always be implemented in any device that supports the Window Covering Cluster.

* The table row describes an attribute within the Window Covering Cluster, specifically the "CurrentPositionLiftPercent100ths 1" attribute. This attribute is identified by the ID '0x000E' and is of the type 'percent100ths', constrained to a maximum value of 10000. It has a quality designation of 'X N P', indicating it is disallowed, not supported, and provisional. The default value is 'null', and it has read and view access ('R V'). The conformance rule 'LF & PA_LF' means that this attribute is mandatory if both the 'LF' (Lift feature) and 'PA_LF' (Position Awareness for Lift feature) are supported. In essence, this attribute is required only when both these specific features are present in the device's implementation.

* The table row describes an attribute within the Window Covering Cluster, specifically the "CurrentPositionTiltPercent100ths 1" attribute. This attribute is identified by the ID '0x000F' and is of the type 'percent100ths', with a constraint that its maximum value is 10000. The quality indicators 'X N P' suggest that this attribute is disallowed, not applicable, or provisional under certain conditions, though these are not detailed here. The default value for this attribute is 'null', and it has read and volatile access ('R V'), meaning it can be read and its value may change without notice. The conformance rule 'TL & PA_TL' indicates that this attribute is mandatory if both the 'TL' and 'PA_TL' features are supported. In essence, this attribute must be implemented when both these specific features are present in the device.

* The table row describes an attribute named "InstalledOpenLimitLift" within the Window Covering Cluster's Attributes section. This attribute has an ID of '0x0010', is of type 'uint16', and has a maximum constraint of 65534. It is marked with a quality of 'N', has a default value of '0', and its access is restricted to 'Read' and 'View' (R V). The conformance rule 'LF & PA_LF & ABS' indicates that this attribute is mandatory if both the 'LF' (Lift feature) and 'PA_LF' (Position Awareness for Lift feature) are supported, as well as if the 'ABS' (Absolute Positioning feature) is supported. If these conditions are met, the attribute must be implemented; otherwise, it is not required.

* The table row describes an attribute named "InstalledClosedLimitLift" within the Window Covering Cluster, identified by the ID '0x0011'. This attribute is of type 'uint16', with a constraint that its maximum value can be 65534. It has a default value of 65534 and is accessible for reading and viewing ('R V'). The quality is marked as 'N', indicating a specific quality characteristic defined elsewhere. The conformance rule 'LF & PA_LF & ABS' indicates that this attribute is mandatory if the features 'LF', 'PA_LF', and 'ABS' are all supported. In other words, the attribute must be implemented if the device supports these specific features, ensuring that the attribute is present in devices with these capabilities.

* The table row describes an attribute within the Window Covering Cluster, specifically the "InstalledOpenLimitTilt" attribute. This attribute has an ID of '0x0012' and is of type 'uint16', with a maximum constraint of 65534. It is marked with a quality of 'N', has a default value of '0', and access permissions of 'R V', indicating it can be read and is volatile. The conformance rule 'TL & PA_TL & ABS' means that this attribute is mandatory if the device supports all three features: TL (Tilt), PA_TL (Partial Automation for Tilt), and ABS (Absolute Positioning). If any of these features are not supported, the attribute is not required.

* The table row describes an attribute named "InstalledClosedLimitTilt" within the Window Covering Cluster, specifically under the Attributes section. This attribute has an ID of '0x0013' and is of type 'uint16', with a maximum constraint of 65534. It has a default value of 65534 and is accessible with read and view permissions ('R V'). The conformance rule 'TL & PA_TL & ABS' indicates that this attribute is mandatory if both the 'TL' (Tilt Limit) feature and the 'PA_TL' (Position Awareness for Tilt) feature are supported, as well as the 'ABS' (Absolute Positioning) feature. This means that the attribute must be implemented when these specific conditions are met, ensuring compatibility and functionality within the specified context of the Window Covering Cluster.

* The table row pertains to the "VelocityLift" attribute within the Window Covering Cluster's attributes section. The 'Conformance' field for this attribute is marked as 'D', which stands for Deprecated. This means that the "VelocityLift" attribute is considered obsolete in the current Matter specification. It is no longer recommended for use and may be removed in future versions of the specification. Developers and implementers should avoid using this attribute in new designs and consider transitioning away from it in existing implementations.

LF & PA_LF
TL & PA_TL
LF & PA_LF
TL & PA_TL
LF & PA_LF
LF & PA_LF
TL & PA_TL
TL & PA_TL

_Table parsed from section 'Attributes':_

* The table row entry pertains to the "AccelerationTimeLift" attribute within the Window Covering Cluster's Attributes section. The 'ID' for this attribute is '0x0015'. According to the conformance rule, this attribute is marked as 'D', which stands for Deprecated. This means that "AccelerationTimeLift" is considered obsolete in the current Matter specification and should not be used in new implementations. Existing implementations that use this attribute should plan for its removal or replacement, as it is no longer supported or recommended for future use.

* The table row entry pertains to the "DecelerationTimeLift" attribute within the Window Covering Cluster's Attributes section. The 'ID' for this attribute is '0x0016'. According to the conformance rule 'D', this attribute is classified as Deprecated. This means that "DecelerationTimeLift" is considered obsolete in the current Matter specification and is not recommended for use in new implementations. Existing implementations may still recognize it, but it is expected to be phased out in future updates.

* The table row describes an attribute within the Window Covering Cluster, specifically the "Mode" attribute, identified by the ID '0x0017'. This attribute is of the type 'ModeBitmap' and has a constraint of '0b0000 xxxx', indicating that only the lower four bits are used. The quality is marked as 'N', meaning it does not have a specific quality requirement, and it defaults to '0'. The access level is 'RW VM', which means it is readable and writable, with the ability to be modified by the manufacturer. The conformance rule for this attribute is 'M', which signifies that the "Mode" attribute is mandatory and must always be implemented in any device supporting the Window Covering Cluster.

* The table row describes an attribute within the Window Covering Cluster, specifically the 'IntermediateSetpointsLift' attribute, identified by the ID '0x0018'. According to the conformance rule 'D', this attribute is marked as Deprecated. This means that the 'IntermediateSetpointsLift' attribute is considered obsolete in the current Matter specification and should not be used in new implementations. Existing implementations that use this attribute are encouraged to transition away from it, as it may be removed in future versions of the specification.

* In the context of the Window Covering Cluster, specifically within the Attributes section, the table row describes an attribute named "IntermediateSetpointsTilt" with an ID of '0x0019'. The conformance rule for this attribute is marked as 'D', which stands for Deprecated. This means that the "IntermediateSetpointsTilt" attribute is considered obsolete in the current Matter specification. It is no longer recommended for use, and developers should avoid implementing it in new devices or systems, as it may be removed in future versions of the specification.

* The table row describes an attribute within the Window Covering Cluster, specifically the "SafetyStatus" attribute. This attribute is identified by the ID `0x001A` and is of the type `SafetyStatusBitmap`. The attribute's constraint is described elsewhere in the documentation, as indicated by "desc." It has a provisional quality, suggesting that its status might change in future specifications. The default value for this attribute is `0`, and it has read and view access permissions, denoted by `R V`. The conformance rule for this attribute is `O`, meaning it is optional. This indicates that the implementation of the "SafetyStatus" attribute is not required and does not depend on any other features or conditions within the current specification.

Nullable positions
1 - The null value indicates that the current position is unknown, e.g. calibration is
needed.
NOTE
2 - The null value indicates that the value is unavailable, e.g. no target position has
been set.
5.3.6.1. Type Attribute
This attribute SHALL identify the type of window covering.
5.3.6.2. PhysicalClosedLimitLift Attribute
This attribute SHALL indicate the maximum possible encoder position possible (Unit cm, centime
ters) to position the height of the window covering lift.
5.3.6.3. PhysicalClosedLimitTilt Attribute
This attribute SHALL indicate the maximum possible encoder position possible (Unit 0.1°, tenths of
a degree) to position the angle of the window covering tilt.
5.3.6.4. CurrentPositionLift Attribute
This attribute SHALL indicate the actual lift position (Unit cm, centimeters) of the window covering
from the fully-open position.
5.3.6.5. CurrentPositionTilt Attribute
This attribute SHALL indicate the actual tilt position (Unit 0.1°, tenths of a degree) of the window
covering from the fully-open position.
5.3.6.6. NumberOfActuationsLift Attribute
This attribute SHALL indicate the total number of lift/slide actuations applied to the window cover
ing since the device was installed.
5.3.6.7. NumberOfActuationsTilt Attribute
This attribute SHALL indicate the total number of tilt actuations applied to the window covering
since the device was installed.
5.3.6.8. ConfigStatus Attribute
This attribute specifies the configuration and status information of the window covering.
To change settings, devices SHALL write to the Mode attribute. The behavior causing the setting or
clearing of each bit is vendor specific.
5.3.6.8.1. Operational Bit
The SafetyStatus & Mode attributes might affect this bit state.
5.3.6.8.2. LiftMovementReversed Bit
This bit identifies if the directions of the lift/slide movements have been reversed in order for com
mands (e.g: Open, Close, GoTos) to match the physical installation conditions
This bit can be adjusted by setting the MotorDirectionReversed bit in the Mode attribute.
5.3.6.8.3. LiftEncoderControlled Bit
This bit is ignored if the device does not support the PositionAwareLift feature (PA_LF).
5.3.6.8.4. TiltEncoderControlled Bit
This bit is ignored if the device does not support the PositionAwareTilt feature (PA_TL).
5.3.6.9. CurrentPositionLiftPercent100ths Attribute
This attribute SHALL indicate the actual position as a percentage with a minimal step of 0.01%. E.g
Max 10000 equals 100.00%.
5.3.6.10. CurrentPositionTiltPercent100ths Attribute
This attribute SHALL indicate the actual position as a percentage with a minimal step of 0.01%. E.g
Max 10000 equals 100.00%.
5.3.6.11. CurrentPositionLiftPercentage Attribute
This attribute SHALL indicate the actual position as a percentage from 0% to 100% with 1% default
step. This attribute is equal to CurrentPositionLiftPercent100ths attribute divided by 100.
5.3.6.12. CurrentPositionTiltPercentage Attribute
This attribute SHALL indicate the actual position as a percentage from 0% to 100% with 1% default
step. This attribute is equal to CurrentPositionTiltPercent100ths attribute divided by 100.
5.3.6.13. TargetPositionLiftPercent100ths Attribute
This attribute SHALL indicate the position where the window covering lift will go or is moving to as
a percentage (Unit 0.01%).
5.3.6.14. TargetPositionTiltPercent100ths Attribute
This attribute SHALL indicate the position where the window covering tilt will go or is moving to as
a percentage (Unit 0.01%).
5.3.6.15. OperationalStatus Attribute
This attribute SHALL indicate the currently ongoing operations and applies to all type of devices.
5.3.6.16. EndProductType Attribute
This attribute SHOULD provide more detail about the product type than can be determined from
the main category indicated by the Type attribute.
The table below helps to match the EndProductType attribute with the Type attribute.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Window Covering Cluster, specifically related to a 'RollerShade'. The 'Value' is set to '0', indicating a default or initial state. The 'Indoor Outdoor' field is marked as 'I', suggesting that this attribute is relevant for indoor applications. The 'Indicative Dimension' is '1D', which likely refers to the dimensionality or measurement aspect of the RollerShade. The 'Recommended Type Attribute' is also 'RollerShade', reinforcing the specific type of window covering being addressed. However, the conformance rule for this attribute is not explicitly provided in the table row data, so we cannot determine its mandatory, optional, or other status based on the provided information.

* The table row describes an attribute within the Window Covering Cluster, specifically for a type of window covering known as "RomanShade." The attribute has a value of '1' and is categorized under the 'Indoor Outdoor' context as 'I', indicating it is intended for indoor use. The 'Indicative Dimension' is '1D', suggesting a one-dimensional aspect relevant to this attribute. The 'Recommended Type Attribute' is 'RollerShade', which implies that the RomanShade shares similarities or recommended usage with the RollerShade type. The conformance rule is not explicitly provided in the data, but based on the context, if we assume a typical conformance expression, it might indicate whether the RomanShade attribute is mandatory, optional, or subject to other conditions within the specification. Without a specific conformance string, we cannot definitively interpret its requirement status, but it would typically be evaluated against the presence of certain features or conditions as outlined in the Matter Conformance Interpretation Guide.

* This table row describes an attribute within the Window Covering Cluster, specifically for a type of window covering called "BalloonShade." The attribute has a value of '2' and is categorized under the 'Indoor Outdoor' context as 'I', indicating it is intended for indoor use. It is associated with an indicative dimension of '1D', suggesting a one-dimensional aspect, and the recommended type attribute for this is 'RollerShade'. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it would typically be interpreted using the Matter Conformance Interpretation Guide. If the conformance was specified, it would dictate whether the BalloonShade attribute is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these apply. However, since the conformance detail is missing, further documentation would be needed to determine its specific requirements.

* This table row describes an attribute within the Window Covering Cluster, specifically for a type of window covering named "WovenWood." The attribute has a value of '3' and is categorized under 'Indoor' use, with an indicative dimension of '1D,' suggesting it is a one-dimensional attribute. The recommended type attribute for this entry is 'RollerShade.' The conformance rule for this attribute is not explicitly provided in the data, but based on the context, it would typically indicate whether the attribute is mandatory, optional, or subject to certain conditions. Since the conformance field is missing, we cannot determine the exact requirements for this attribute without additional information. However, if it were included, it would specify under what conditions this attribute must be implemented, using the rules outlined in the Matter Conformance Interpretation Guide.

* The table row describes an attribute within the Window Covering Cluster, specifically for a 'PleatedShade' with a value of '4'. This attribute is categorized under 'Indoor Outdoor' as 'I', indicating it is intended for indoor use. The 'Indicative Dimension' is '1D', suggesting it has a one-dimensional aspect, likely referring to its operation or installation. The 'Recommended Type Attribute' is 'RollerShade', which implies that the 'PleatedShade' shares similar characteristics or functionality with roller shades. The conformance rule for this attribute is not explicitly provided in the table row data, but if we were to interpret a typical conformance expression, it would dictate when this attribute is required, optional, or otherwise, based on the presence or absence of certain features or conditions. Since no specific conformance string is given, we assume it follows the general rules of the Matter specification, where the attribute's necessity would depend on the implementation context and any applicable conditions described in the

* The table row describes an attribute within the Window Covering Cluster, specifically for a feature named 'CellularShade', which has a value of '5'. This feature is categorized under 'Indoor Outdoor' as 'I', indicating it is intended for indoor use, and it has an 'Indicative Dimension' of '1D', suggesting it is a one-dimensional attribute. The 'Recommended Type Attribute' is 'RollerShade', implying that 'CellularShade' is recommended to be used in conjunction with or as a type of 'RollerShade'. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it would typically specify whether the 'CellularShade' attribute is mandatory, optional, provisional, deprecated, or disallowed, or it might involve conditional expressions based on the presence of other features. Without the specific conformance string, we can infer that the attribute's inclusion and behavior depend on the broader context of the Window Covering Cluster

* The table row describes an attribute named "LayeredShade" within the Window Covering Cluster, specifically in the context of attributes. This attribute has a value of '6' and is associated with indoor use, indicated by 'I'. It is characterized by a one-dimensional ('1D') indicative dimension and is recommended for use with the 'RollerShade' type attribute. The conformance rule for this attribute is not explicitly provided in the data, but based on the context, it would typically be interpreted using the Matter Conformance Interpretation Guide. If a conformance expression were provided, it would dictate whether the "LayeredShade" attribute is mandatory, optional, provisional, deprecated, or disallowed under certain conditions. Without a specific conformance string, we assume the attribute's inclusion is subject to the general rules of the specification or further detailed documentation.

* The table row describes an attribute named "LayeredShade2D" within the Window Covering Cluster, specifically under the Attributes section. This attribute is identified by the value '7' and is associated with indoor applications ('I') and a two-dimensional indicative dimension ('2D'). The recommended type attribute for this is 'RollerShade2Motor'. However, the conformance rule for this attribute is not explicitly provided in the data given. Therefore, based on the provided information, we cannot determine whether this attribute is mandatory, optional, provisional, deprecated, or disallowed. Additional context from the conformance column or documentation would be needed to fully interpret its conformance status.

* The table row describes an attribute named "SheerShade" within the Window Covering Cluster, specifically in the context of attributes. The "Value" of this attribute is '8', and it is associated with indoor applications, indicated by 'I' under "Indoor Outdoor". The "Indicative Dimension" is '2D', suggesting that it pertains to a two-dimensional aspect of the window covering. The "Recommended Type Attribute" is 'TiltBlindLiftAndTilt', indicating that this attribute is particularly relevant for window coverings that can tilt, lift, and tilt again. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it would be interpreted using the Matter Conformance Interpretation Guide. If a conformance string were present, it would dictate whether the "SheerShade" attribute is mandatory, optional, provisional, deprecated, or disallowed, possibly with conditions based on the presence of certain features or logical expressions.

* The table row describes an attribute named 'TiltOnlyInteriorBlind' within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '9' and is associated with indoor use, as indicated by 'Indoor Outdoor': 'I'. It is characterized by a one-dimensional ('1D') indicative dimension and is recommended to be of the type 'TiltBlindTiltOnly'. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context, it would typically involve conditions under which the attribute is mandatory, optional, or otherwise. Without a specific conformance string, we can infer that the attribute is likely to be optional or mandatory depending on the presence of certain features or conditions related to the Window Covering Cluster, such as whether the device supports tilt-only functionality.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "InteriorBlind" within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '10' and is associated with indoor use, as indicated by the 'Indoor Outdoor' field marked as 'I'. It is characterized by a '2D' indicative dimension, suggesting it involves two-dimensional control or representation. The recommended type attribute for this is 'TiltBlindLiftAndTilt', which implies that the attribute is best suited for window coverings that can tilt, lift, and tilt again. The conformance rule for this attribute is not explicitly provided in the table row data, but based on the context, it would typically be interpreted using the Matter Conformance Interpretation Guide. However, since the conformance string is missing, we cannot determine the specific conditions under which this attribute is mandatory, optional, or otherwise.

* The table row describes an attribute within the Window Covering Cluster, specifically named "VerticalBlindStripCurtain," which has a value of '11'. This attribute is relevant to indoor applications, as indicated by the 'Indoor Outdoor' field marked 'I'. It is associated with a two-dimensional indicative dimension ('2D'), suggesting it pertains to a feature that involves both width and height, such as the movement or adjustment of blinds. The recommended type attribute for this is 'TiltBlindLiftAndTilt', which implies that this attribute is particularly suited for window coverings that can tilt and lift, like vertical blinds or strip curtains. The conformance rule for this attribute is not explicitly provided in the table row data, but based on the context, it would typically be interpreted using the Matter Conformance Interpretation Guide to determine whether it is mandatory, optional, or subject to other conditions.

* The table row describes an attribute within the Window Covering Cluster, specifically for the 'InteriorVenetianBlind'. This attribute has a 'Value' of '12' and is categorized under 'Indoor Outdoor' as 'I', indicating it is intended for indoor use. The 'Indicative Dimension' is '2D', suggesting that it involves two-dimensional control, likely related to the tilt and lift functionalities of the blind. The 'Recommended Type Attribute' is 'TiltBlindLiftAndTilt', which implies that this attribute is associated with blinds that can both tilt and lift. The conformance rule for this attribute is not explicitly provided in the row data, but based on the context and typical usage, it would likely be mandatory or optional depending on the specific features supported by the device or implementation. Without a specific conformance string, we assume it follows the general guidelines of the cluster or section it belongs to.

* The table row describes an attribute named "ExteriorVenetianBlind" within the Window Covering Cluster, specifically in the context of Attributes. This attribute has a value of '13' and is associated with the "TiltBlindLiftAndTilt" recommended type attribute. The 'Indoor Outdoor' field is marked as 'O', indicating that this attribute is optional and not required, with no dependencies on other features or conditions. The 'Indicative Dimension' is noted as '2D', suggesting that this attribute may relate to a two-dimensional aspect of the window covering, such as tilt and lift functionality. Overall, the conformance rule for "ExteriorVenetianBlind" means that its implementation is optional and can be included at the discretion of the device manufacturer, without any mandatory requirements or conditional dependencies.

* The table row describes an attribute named "LateralLeftCurtain" within the Window Covering Cluster, specifically in the context of attributes. This attribute has a value of '14' and is associated with indoor use ('I') and a one-dimensional indicative dimension ('1D'). The recommended type for this attribute is 'Drapery'. The conformance rule for this attribute is not explicitly provided in the data, so we cannot determine its mandatory or optional status based on the given information. However, if a conformance rule were provided, it would dictate under what conditions this attribute is required, optional, provisional, deprecated, or disallowed, following the guidelines outlined in the Matter Conformance Interpretation Guide.

* The table row describes an attribute named "LateralRightCurtain" within the Window Covering Cluster, specifically in the context of attributes. This attribute has a value of '15', is intended for indoor use ('I'), and is associated with a one-dimensional ('1D') indicative dimension. The recommended type for this attribute is 'Drapery'. The conformance rule for "LateralRightCurtain" is not explicitly provided in the data, but based on the context, it would typically specify when this attribute is required or optional. If we assume a conformance rule like `M`, it would mean that the "LateralRightCurtain" attribute is mandatory for devices implementing this cluster. If the conformance rule were more complex, such as `AB, O`, it would mean the attribute is mandatory if feature `AB` is supported, otherwise optional. Without the specific conformance string, we can only infer that its inclusion depends on the device's implementation and the specific features it

* The table row describes an attribute named "CentralCurtain" within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '16', is intended for indoor use ('I'), and is associated with a one-dimensional ('1D') indicative dimension. The recommended type attribute for "CentralCurtain" is 'Drapery'. The conformance rule for this attribute is not explicitly provided in the data snippet, but if we were to interpret a typical conformance expression, it would dictate when and under what conditions this attribute is required, optional, or otherwise. For instance, if the conformance were 'M', it would mean "CentralCurtain" is always mandatory. If it were 'O', it would be optional with no dependencies. Without a specific conformance expression provided, we assume the attribute's inclusion is determined by the broader context of the specification or additional documentation.

* The table row describes an attribute named "RollerShutter" within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '17' and is associated with the recommended type attribute "RollerShadeExterior." The "Indoor Outdoor" field is marked as 'O', indicating that this attribute is optional and does not have any dependencies. The "Indicative Dimension" is '1D', suggesting a one-dimensional characteristic. The conformance rule 'O' means that the "RollerShutter" attribute is not required for implementation; it can be included at the discretion of the developer without any mandatory conditions or dependencies.

* The table row describes an attribute named "ExteriorVerticalScreen" within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '18' and is associated with the indicative dimension '1D'. It is recommended to be used with the type attribute 'RollerShadeExterior'. The 'Indoor Outdoor' field is marked as 'O', indicating that this attribute is optional and does not have any dependencies or conditions that must be met for its inclusion. Therefore, the "ExteriorVerticalScreen" attribute can be implemented at the discretion of the developer, without any mandatory requirements or restrictions imposed by the Matter specification.

* The table row describes an attribute within the Window Covering Cluster, specifically named "AwningTerracePatio" with a value of '19'. This attribute is categorized under the "Attributes" section and is associated with the "Awning" as its recommended type attribute. The "Indoor Outdoor" field is marked as 'O', indicating that this attribute is optional and not required by default, with no dependencies on other features or conditions. The "Indicative Dimension" is specified as '1D', suggesting a one-dimensional characteristic. The conformance rule 'O' means that the "AwningTerracePatio" attribute is not mandatory for implementation and can be included at the discretion of the developer or manufacturer, without any additional conditions or requirements.

* The table row describes an attribute named "AwningVerticalScreen" within the Window Covering Cluster, specifically in the context of attributes. The attribute is identified by the value '20' and is associated with the indicative dimension '1D', suggesting it pertains to a one-dimensional aspect of the window covering. The recommended type attribute for this entry is 'Awning', indicating that this attribute is particularly relevant for awning-type window coverings. The 'Indoor Outdoor' field is marked as 'O', meaning that this attribute is optional and does not have any dependencies or conditions that must be met for its inclusion. In essence, the "AwningVerticalScreen" attribute is not required for all implementations of the Window Covering Cluster, but it can be included at the discretion of the implementer, especially when dealing with awning-type coverings.

* The table row describes an attribute named "TiltOnlyPergola" within the Window Covering Cluster, specifically under the Attributes section. This attribute has a value of '21' and is associated with the 'Shutter' as the recommended type attribute. It is indicative of a one-dimensional (1D) characteristic and is optionally applicable to both indoor and outdoor contexts, as denoted by 'O' in the 'Indoor Outdoor' column. The conformance rule for "TiltOnlyPergola" is not explicitly provided in the row data, but if we assume a typical conformance expression, it would dictate when this attribute is required or optional based on certain conditions or features. Without a specific conformance expression, we can infer that its inclusion is likely optional, given the 'O' in the 'Indoor Outdoor' column, unless further conditions are specified elsewhere in the documentation.

* The table row describes an attribute named "SwingingShutter" within the Window Covering Cluster, specifically under the Attributes section. The attribute has a value of '22' and is associated with an indicative dimension of '1D', suggesting it pertains to a one-dimensional aspect of the shutter. The recommended type attribute for this is 'Shutter'. The 'Indoor Outdoor' field is marked as 'O', indicating that this attribute is optional and does not have any dependencies or conditions that must be met for its inclusion. This means that the "SwingingShutter" attribute can be implemented at the discretion of the developer or manufacturer, without any mandatory requirement or specific conditions tied to its use.

* The table row describes an attribute named "SlidingShutter" within the Window Covering Cluster, specifically in the context of attributes. The 'Value' assigned to this attribute is '23'. The 'Indoor Outdoor' field is marked as 'O', indicating that this attribute is optional and does not have any dependencies. The 'Indicative Dimension' is noted as '1D', suggesting that it pertains to a one-dimensional aspect of the window covering. The 'Recommended Type Attribute' is 'Shutter', implying that this attribute is best suited for shutter-type window coverings. The conformance rule 'O' means that the SlidingShutter attribute is not required for implementation and can be included at the discretion of the developer, without any conditional requirements or dependencies.

* The table row entry pertains to the "Unknown" attribute within the Window Covering Cluster's Attributes section. The 'Value' of '255' and 'Recommended Type Attribute' of 'Unknown' suggest that this attribute is used to represent an undefined or unspecified state within the cluster. The conformance rule for this attribute is not explicitly provided in the data given, but if we were to interpret a typical conformance scenario using the Matter Conformance Interpretation Guide, it might involve conditions under which this attribute is mandatory, optional, or otherwise. Without a specific conformance string, we can infer that the attribute's presence and usage are likely context-dependent, potentially serving as a placeholder or default state when the actual attribute value is not determined.

5.3.6.17. InstalledOpenLimitLift Attribute
This attribute SHALL indicate the open limit for lifting the window covering whether position (in
centimeters) is encoded or timed.
5.3.6.18. InstalledClosedLimitLift Attribute
This attribute SHALL indicate the closed limit for lifting the window covering whether position (in
centimeters) is encoded or timed.
5.3.6.19. InstalledOpenLimitTilt Attribute
This attribute SHALL indicate the open limit for tilting the window covering whether position (in
tenth of a degree) is encoded or timed.
5.3.6.20. InstalledClosedLimitTilt Attribute
This attribute SHALL indicate the closed limit for tilting the window covering whether position (in
tenth of a degree) is encoded or timed.
5.3.6.21. Mode Attribute
The Mode attribute allows configuration of the window covering, such as: reversing the motor
direction, placing the window covering into calibration mode, placing the motor into maintenance
mode, disabling the network, and disabling status LEDs.
In the case a device does not support or implement a specific mode, e.g. the device has a specific
installation method and reversal is not relevant or the device does not include a maintenance
mode, any write interaction to the Mode attribute, with an unsupported mode bit or any out of
bounds bits set, must be ignored and a response containing the status of CONSTRAINT_ERROR will
be returned.
5.3.6.21.1. MotorDirectionReversed Bit
This bit SHALL control the LiftMovementReversed bit in the ConfigStatus attribute.
5.3.6.21.2. CalibrationMode Bit
If in calibration mode, all commands (e.g: UpOrOpen, DownOrClose, GoTos) that can result in move
ment, could be accepted and result in a self-calibration being initiated before the command is exe
cuted.
In case the window covering does not have the ability or is not able to perform a self-calibration,
the command SHOULD be ignored and a FAILURE status SHOULD be returned.
In a write interaction, setting this bit to 0, while the device is in calibration mode, is not allowed
and SHALL generate a FAILURE error status. In order to leave calibration mode, the device must
perform its calibration routine, either as a self-calibration or assisted by external tool(s), depending
on the device/manufacturer implementation.
A manufacturer might choose to set the Operational bit of the ConfigStatus attribute to its not oper
ational value, if applicable during calibration mode.
5.3.6.21.3. MaintenanceMode Bit
While in maintenance mode, all commands (e.g: UpOrOpen, DownOrClose, GoTos) or local inputs
that can result in movement, must be ignored and respond with a BUSY status. Additionally, the
Operational bit of the ConfigStatus attribute should be set to its not operational value.
5.3.6.22. SafetyStatus Attribute
The SafetyStatus attribute reflects the state of the safety sensors and the common issues preventing
movements. By default for nominal operation all flags are cleared (0). A device might support none,
one or several bit flags from this attribute (all optional).

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Window Covering Cluster, specifically the "UpOrOpen" command, which is identified by the ID '0x00'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required to be implemented by all devices. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "UpOrOpen" command must always be supported and implemented by any device that includes the Window Covering Cluster, without any conditions or exceptions.

* The table row describes a command within the Window Covering Cluster, specifically the "DownOrClose" command. This command is directed from the client to the server, indicating that it is initiated by the client and received by the server. The command requires a response, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', suggesting that access to this command is optional, though this does not affect its conformance. The 'Conformance' field is marked 'M', which means that the "DownOrClose" command is mandatory. This implies that any implementation of the Window Covering Cluster must support this command without exception.

* The table row describes a command within the Window Covering Cluster, specifically the "StopMotion" command, which is identified by the ID '0x02'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented by all devices. However, the conformance rule for this command is marked as 'M', indicating that the "StopMotion" command is mandatory. This means that any implementation of the Window Covering Cluster must support this command, regardless of any other conditions or features.

* The table row describes a command within the Window Covering Cluster, specifically the "GoToLiftValue" command, which is identified by the ID '0x04'. This command is intended to be sent from a client to a server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented unless certain conditions are met. The conformance rule '[LF & ABS]' indicates that the command is optional if both the 'LF' (Lift feature) and 'ABS' (Absolute Positioning feature) are supported. If these conditions are not met, the command does not need to be implemented. This setup allows for flexibility in implementation based on the specific features supported by the device.

* The table row describes the "GoToLiftPercentage" command within the Window Covering Cluster, which is directed from the client to the server and requires a response. The access level for this command is optional. The conformance rule `(LF & PA_LF), [LF]` indicates that the command is mandatory if both the LF (Lift feature) and PA_LF (Presumably a related feature to Lift) are supported. If only the LF feature is supported, the command is optional. This means that the implementation of this command depends on the support of specific features within the device, ensuring flexibility based on the device's capabilities.

* The table row describes a command within the Window Covering Cluster, specifically the "GoToTiltValue" command, which is identified by the ID '0x07'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'). The conformance rule '[TL & ABS]' indicates that the "GoToTiltValue" command is optional if both the 'TL' (Tilt feature) and 'ABS' (Absolute Positioning feature) are supported. If these conditions are not met, the command is not required.

* The table row describes a command named "GoToTiltPercentage" within the Window Covering Cluster, specifically in the context of commands sent from a client to a server. This command has an ID of '0x08' and requires a response ('Y'). The access level is optional ('O'), meaning it is not required by default. The conformance rule '(TL & PA_TL), [TL]' indicates that the command is mandatory if both the TL (Tilt feature) and PA_TL (Position Awareness for Tilt feature) are supported. If only the TL feature is supported, the command is optional. This rule ensures that the command's necessity is contingent on the specific features supported by the device, reflecting its adaptability to different device capabilities.

5.3.7.1. UpOrOpen Command
Upon receipt of this command, the window covering will adjust its position so the physical lift/slide
and tilt is at the maximum open/up position. This will happen as fast as possible. The server attrib
utes SHALL be updated as follows:
if the PositionAware feature is supported:
• TargetPositionLiftPercent100ths attribute SHALL be set to 0.00%.
• TargetPositionTiltPercent100ths attribute SHALL be set to 0.00%.
The server positioning attributes will follow the movements, once the movement has successfully
finished, the server attributes SHALL be updated as follows:
if the PositionAware feature is supported:
• CurrentPositionLiftPercent100ths attribute SHALL be 0.00%.
• CurrentPositionLiftPercentage attribute SHALL be 0%.
• CurrentPositionTiltPercent100ths attribute SHALL be 0.00%.
• CurrentPositionTiltPercentage attribute SHALL be 0%.
if the AbsolutePosition feature is supported:
• CurrentPositionLift attribute SHALL be equal to the InstalledOpenLimitLift attribute.
• CurrentPositionTilt attribute SHALL be equal to the InstalledOpenLimitTilt attribute.
5.3.7.2. DownOrClose Command
Upon receipt of this command, the window covering will adjust its position so the physical lift/slide
and tilt is at the maximum closed/down position. This will happen as fast as possible. The server
attributes supported SHALL be updated as follows:
if the PositionAware feature is supported:
• TargetPositionLiftPercent100ths attribute SHALL be set to 100.00%.
• TargetPositionTiltPercent100ths attribute SHALL be set to 100.00%.
The server positioning attributes will follow the movements, once the movement has successfully
finished, the server attributes SHALL be updated as follows:
if the PositionAware feature is supported:
• CurrentPositionLiftPercent100ths attribute SHALL be 100.00%.
• CurrentPositionLiftPercentage attribute SHALL be 100%.
• CurrentPositionTiltPercent100ths attribute SHALL be 100.00%.
• CurrentPositionTiltPercentage attribute SHALL be 100%.
if the AbsolutePosition feature is supported:
• CurrentPositionLift attribute SHALL be equal to the InstalledClosedLimitLift attribute.
• CurrentPositionTilt attribute SHALL be equal to the InstalledClosedLimitTilt attribute.
5.3.7.3. StopMotion Command
Upon receipt of this command, the window covering will stop any adjusting to the physical tilt and
lift/slide that is currently occurring. The server attributes supported SHALL be updated as follows:
• TargetPositionLiftPercent100ths  attribute  will  be  set  to  CurrentPositionLiftPercent100ths
attribute value.
• TargetPositionTiltPercent100ths  attribute  will  be  set  to  CurrentPositionTiltPercent100ths
attribute value.
5.3.7.4. GoToLiftValue Command
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Window Covering Cluster, specifically the "LiftValue" command, which is identified by the ID '0' and is of the type 'uint16'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "LiftValue" is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Window Covering Cluster, without any conditions or exceptions.

5.3.7.4.1. LiftValue Field
This field SHALL specify the requested physical lift/slide position in unit cm (centimeters).
5.3.7.4.2. Effect on Receipt
Upon receipt of this command, the window covering will adjust the lift position to the value speci
fied in the LiftValue field, as long as that value is not larger thanInstalledOpenLimitLift attribute
and  not  smaller  than  InstalledClosedLimitLift  attribute.  The  TargetPositionLiftPercent100ths
attribute SHALL update its value accordingly.
If the value is out of bounds a response containing the status of CONSTRAINT_ERROR will be
returned.
5.3.7.5. GoToLiftPercentage Command
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row pertains to the "LiftPercent100thsValue" command within the Window Covering Cluster's Commands section. This command is identified by the ID '0' and utilizes the 'percent100ths' data type, with constraints described elsewhere in the documentation. The conformance rule for this command is marked as 'M', indicating that it is a Mandatory element. This means that the "LiftPercent100thsValue" command is always required to be implemented in any device or application that supports the Window Covering Cluster, without any conditions or exceptions.

Upon receipt of this command, the server will adjust the window covering to the lift/slide percent
age specified in the payload of this command.
If the command includes LiftPercent100thsValue, then TargetPositionLiftPercent100ths attribute
SHALL be set to LiftPercent100thsValue. Otherwise the TargetPositionLiftPercent100ths attribute
SHALL be set to LiftPercentageValue * 100.
If a client includes LiftPercent100thsValue in the command, the LiftPercentageValue SHALL be set
to LiftPercent100thsValue / 100, so a legacy server which only supports LiftPercentageValue (not
LiftPercent100thsValue) has a value to set the target position.
If the server does not support the PositionAware feature, then a zero percentage SHALL be treated
as a UpOrOpen command and a non-zero percentage SHALL be treated as an DownOrClose com
mand. If the device is only a tilt control device, then the command SHOULD be ignored and a
UNSUPPORTED_COMMAND status SHOULD be returned.
5.3.7.6. GoToTiltValue Command
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* In the context of the Window Covering Cluster, the table row describes a command named "TiltValue" with an ID of '0' and a data type of 'uint16'. The 'Constraint' is marked as 'desc', indicating that specific constraints are detailed elsewhere in the documentation. The 'Conformance' is marked as 'M', which means that the "TiltValue" command is mandatory. This implies that any implementation of the Window Covering Cluster must include this command, as it is always required according to the Matter specification.

5.3.7.6.1. TiltValue Field
This field SHALL specify the requested physical tilt position in unit 0.1° (tenth of a degrees).
5.3.7.6.2. Effect on Receipt
Upon receipt of this command, the window covering will adjust the tilt position to the value speci
fied in the TiltValue field, as long as that value is not larger than InstalledOpenLimitTilt attribute
and  not  smaller  than  InstalledClosedLimitTilt  attribute.  The  TargetPositionTiltPercent100ths
attribute SHALL update its value accordingly.
If the tilt value is out of bounds a response containing the status of CONSTRAINT_ERROR will be
returned.
5.3.7.7. GoToTiltPercentage Command
This command SHALL have the following data fields:

_Table parsed from section 'Commands':_

* The table row describes a command within the Window Covering Cluster, specifically the "TiltPercent100thsValue" command. This command is of the type "percent100ths," which likely refers to a percentage value expressed in hundredths, allowing for precise control over the tilt of window coverings. The constraint for this command is marked as "desc," indicating that the specific constraints are detailed elsewhere in the documentation. The conformance rule for this command is marked as "M," meaning it is mandatory. This indicates that the "TiltPercent100thsValue" command must be implemented and supported in any device or application that utilizes the Window Covering Cluster, as it is an essential component of the cluster's functionality.

Upon receipt of this command, the server will adjust the window covering to the tilt percentage
specified in the payload of this command.
If the command includes TiltPercent100thsValue, then TargetPositionTiltPercent100ths attribute
SHALL be set to TiltPercent100thsValue. Otherwise the TargetPositionTiltPercent100ths attribute
SHALL be set to TiltPercentageValue * 100.
If a client includes TiltPercent100thsValue in the command, the TiltPercentageValue SHALL be set
to TiltPercent100thsValue / 100, so a legacy server which only supports TiltPercentageValue (not
TiltPercent100thsValue) has a value to set the target position.
If the server does not support the PositionAware feature, then a zero percentage SHALL be treated
as a UpOrOpen command and a non-zero percentage SHALL be treated as an DownOrClose com
mand. If the device is only a tilt control device, then the command SHOULD be ignored and a
UNSUPPORTED_COMMAND status SHOULD be returned.
Chapter 6. Media
The Cluster Library is made of individual chapters such as this one. See Document Control in the
Cluster Library for a list of all chapters and documents. References between chapters are made
using a X.Y notation where X is the chapter and Y is the sub-section within that chapter. References
to external documents are contained in Chapter 1 and are made using [Rn] notation.
6.1. General Description

## Introduction
The clusters specified in this document are for use typically in applications involving media (e.g.,
Video Players, Content Apps, Speakers), but MAY be used in any application domain.

## Cluster List
This section lists the media specific clusters as specified in this chapter.
Table 11. Overview of the Media Clusters

_Table parsed from section 'Cluster List':_

* The table row describes the "Account Login" cluster within the context of the Window Covering Cluster's Cluster List. This cluster, identified by the Cluster ID '0x050E', is designed to provide an interface for facilitating user account login on an application or a node. The conformance rule for this cluster is not explicitly provided in the data you shared, but typically, it would specify whether the cluster is mandatory, optional, or subject to certain conditions based on the presence of other features or elements. Without a specific conformance string, we cannot determine its exact requirement status, but generally, such a cluster would be included based on the needs of the application or device it is intended for, possibly being optional unless certain conditions necessitate its inclusion.

* The table row describes the "Application Basic" cluster within the Window Covering Cluster's Cluster List. This cluster, identified by the Cluster ID '0x050D', provides information about a Content App running on a Video Player device, which is represented as an endpoint. The conformance rule for this cluster is not explicitly provided in the given data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which this cluster is required, optional, or otherwise specified. In the absence of a specific conformance string, we can infer that the cluster's inclusion and implementation would depend on the broader context of the device's capabilities and the specific requirements of the Matter specification for the Window Covering Cluster.

* The table row describes the "Application Launcher" cluster within the Window Covering Cluster's Cluster List, identified by the Cluster ID '0x050C'. This cluster is designed to offer an interface for launching content on a Video Player device. The conformance rule for this entry is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance rule using the Matter Conformance Interpretation Guide, it would specify under what conditions this cluster is required, optional, or otherwise. For example, if the conformance were 'M', it would mean the Application Launcher cluster is always mandatory. If it were 'O', it would be optional with no dependencies. Without a specific conformance string, we cannot definitively state the requirements for this cluster.

* The table row describes the "Audio Output" cluster within the Window Covering Cluster's Cluster List, identified by the Cluster ID '0x050B'. This cluster offers an interface for managing audio output on a Video Player device. The conformance rule for this cluster is not explicitly provided in the data you shared, so I cannot interpret its specific conformance requirements. However, if the conformance string were provided, it would dictate whether the "Audio Output" cluster is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply, based on the Matter Conformance Interpretation Guide.

* The table row describes a cluster within the Window Covering Cluster, specifically the "Channel" cluster, identified by the Cluster ID `0x0504`. This cluster offers an interface for controlling the current channel on an endpoint. The conformance rule for this cluster is not explicitly provided in the data you shared. However, if we were to interpret a typical conformance string using the guide, it would dictate when and under what conditions this cluster is required, optional, or otherwise. For instance, if the conformance were `M`, it would mean the Channel cluster is always mandatory. If it were `O`, it would be optional with no dependencies. Without the specific conformance string, we cannot determine the precise requirements for this cluster, but the guide provides a framework for understanding how such rules would be applied.

* The table row describes a cluster within the Window Covering Cluster context, specifically the "Content App Observer" with a Cluster ID of '0x0510'. This cluster facilitates communication by allowing targeted messages to be sent from a Content App to its client. The conformance rule for this cluster is not explicitly provided in the data you shared, but if it were, it would dictate whether the inclusion of this cluster is mandatory, optional, provisional, deprecated, or disallowed based on certain conditions or features. Without the conformance string, we cannot determine the exact requirements for implementing this cluster.

_Table parsed from section 'Cluster List':_

* The table row describes the "Content Launcher" cluster within the Window Covering Cluster's Cluster List, identified by the Cluster ID '0x050A'. This cluster is designed to provide an interface for launching content on a Video Player device or a Content App. The conformance rule for this cluster is not explicitly provided in the data you shared, but typically, it would specify under what conditions the cluster is required, optional, provisional, deprecated, or disallowed. Without the specific conformance string, we can't determine the exact requirements for implementing this cluster. However, if a conformance string were provided, it would dictate whether the Content Launcher cluster must be implemented, can be optionally implemented, or is subject to other conditions based on the presence or absence of certain features or other logical conditions as outlined in the Matter Conformance Interpretation Guide.

* The table row describes the "Keypad Input" cluster, identified by the Cluster ID '0x0509', within the context of the Window Covering Cluster's Cluster List. This cluster serves as an interface for controlling a Video Player or a Content App through action commands like UP, DOWN, and SELECT. The conformance rule for this cluster is not explicitly provided in the data you shared, but based on the Matter Conformance Interpretation Guide, it would typically specify whether the inclusion of this cluster is mandatory, optional, provisional, deprecated, or disallowed, possibly with conditions based on supported features. Without the specific conformance string, we cannot determine its exact requirement status, but it would dictate when and how this cluster should be implemented in a device supporting the Window Covering Cluster.

* The table row describes the "Media Input" cluster within the Window Covering Cluster's Cluster List, identified by the Cluster ID '0x0507'. This cluster offers an interface for managing the Input Selector on a Video Player device. The conformance rule for this cluster is not explicitly provided in the data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate when the Media Input cluster is required or optional, depending on specific conditions or features. For instance, if the conformance were 'M', it would mean the Media Input cluster is always mandatory. If it were 'O', it would be optional without dependencies. The absence of a conformance string in the provided data suggests that further context or documentation is needed to determine its specific conformance requirements.

* The table row describes the "Media Playback" cluster within the Window Covering Cluster's Cluster List, identified by the Cluster ID '0x0506'. This cluster offers an interface for controlling media playback functions such as PLAY and PAUSE on a video player device. The conformance rule for this entry is not explicitly provided in the row data, but based on the Matter Conformance Interpretation Guide, if a conformance string were present, it would dictate the conditions under which the Media Playback cluster is required, optional, provisional, deprecated, or disallowed. For example, if the conformance were 'M', it would mean the Media Playback cluster is always required in the implementation of the Window Covering Cluster. Without a specific conformance string, we cannot determine the exact requirement status for this cluster.

* The table row describes the "Target Navigator" cluster within the Window Covering Cluster's Cluster List. This cluster, identified by the Cluster ID '0x0505', offers an interface for user experience navigation across a set of targets on a Video Player device or Content App endpoint. The conformance rule for this cluster is not explicitly provided in the data you shared, but if it were included, it would specify the conditions under which the Target Navigator cluster is required, optional, or otherwise, based on the Matter Conformance Interpretation Guide. This would involve determining whether the cluster is mandatory, optional, provisional, deprecated, or disallowed, depending on the presence or absence of certain features or conditions.

* The table row describes a cluster within the Window Covering Cluster context, specifically the "Content Control" cluster with the ID '0x050F'. This cluster is designed to manage content control features, such as enabling or disabling the content control functionality on a video player device. The conformance rule for this cluster is not explicitly provided in the data you shared, but if we assume it follows the Matter Conformance Interpretation Guide, it would specify when and how this cluster should be implemented in devices. For example, if the conformance were 'M', it would mean that the Content Control cluster is mandatory for all devices supporting the Window Covering Cluster. If it were 'O', it would be optional, allowing manufacturers to include it at their discretion. The actual conformance rule would dictate the necessity and conditions under which this cluster must be implemented, ensuring consistent functionality across compliant devices.

device or Content App endpoint.
Example Usage of the Media Clusters