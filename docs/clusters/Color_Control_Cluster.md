
# 3.2 Color Control Cluster

This cluster provides an interface for changing the color of a light. Color is specified according to
the CIE 1931 Color space. Color control is carried out in terms of x,y values, as defined by this speci
fication.
Additionally, color MAY optionally be controlled in terms of color temperature, or as hue and satu
ration values based on optionally variable RGB and W color points. It is recommended that the hue
and saturation are interpreted according to the HSV (a.k.a. HSB) color model.
Control over luminance is not included, as this is provided by means of the Level Control for Light
ing cluster. It is recommended that the level provided by this cluster be interpreted as representing
a proportion of the maximum intensity achievable at the current color.

## Dependencies
3.2.5.1. Coupling color temperature to Level Control
If the Level Control for Lighting cluster identifier 0x0008 is supported on the same endpoint as the
Color Control cluster and color temperature is supported, it is possible to couple changes in the cur
rent level to the color temperature.
The CoupleColorTempToLevel bit of the Options attribute of the Level Control cluster indicates
whether the color temperature is to be linked with the CurrentLevel attribute in the Level Control
cluster.
If the CoupleColorTempToLevel bit of the Options attribute of the Level Control cluster is equal to 1
and the ColorMode or EnhancedColorMode attribute is set to 2 (ColorTemperatureMireds) then a
change in the CurrentLevel attribute SHALL affect the ColorTemperatureMireds attribute. This rela
tionship  is  manufacturer  specific,  with  the  qualification  that  the  maximum  value  of  the  Cur
rentLevel attribute SHALL correspond to a ColorTemperatureMired attribute value equal to the
CoupleColorTempToLevelMinMireds attribute. This relationship is one-way so a change to the Col
orTemperatureMireds attribute SHALL NOT have any effect on the CurrentLevel attribute.
In order to simulate the behavior of an incandescent bulb, a low value of the CurrentLevel attribute
SHALL be associated with a high value of the ColorTemperatureMireds attribute (i.e., a low value of
color temperature in kelvins).
If the CoupleColorTempToLevel bit of the Options attribute of the Level Control cluster is equal to 0,
there SHALL be no link between color temperature and current level.
3.2.5.2. Independent transition in hue and saturation
Various commands in this cluster can be used to start transitions in hue and/or saturation.
• When a transition in hue is in progress, and a command to change saturation (MoveSaturation
(with MoveMode!=Stop), StepSaturation, MoveToSaturation) is received by the server, this latter
command SHALL NOT interrupt the ongoing transition in hue.
• When a transition in saturation is in progress, and a command to change hue (MoveHue (with
MoveMode!=Stop),  EnhancedMoveHue  (with  MoveMode!=Stop)  StepHue,  EnhancedStepHue,
MoveToHue, EnhancedMoveToHue) is received by the server, this latter command SHALL NOT
interrupt the ongoing transition in saturation.

## Data Types
3.2.6.1. ColorCapabilitiesBitmap
This data type is derived from map16.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the Color Control Cluster, specifically within the Data Types section, and describes a feature named "HueSaturation" with a bit value of '0'. This feature allows for color specification using hue and saturation. The conformance rule 'HS' indicates that the "HueSaturation" feature is mandatory if the device supports the HS (HueSaturation) feature. In other words, if the device includes the capability to handle hue and saturation for color control, then the "HueSaturation" feature must be implemented. If the device does not support this capability, the conformance rule does not apply, and the feature is not required.

* In the context of the Color Control Cluster, specifically within the Data Types section, the table row describes an element named "EnhancedHue," which is associated with the bit value '1'. The summary indicates that this element pertains to the support of enhanced hue functionality. The conformance rule 'EHUE' implies that the EnhancedHue element is mandatory if the feature code 'EHUE' is supported. In other words, if a device or implementation includes the 'EHUE' feature, it must also include the EnhancedHue element as part of its functionality.

* In the context of the Color Control Cluster, specifically within the Data Types section, the table entry describes a feature named "ColorLoop," which is identified by the bit value '2'. The summary indicates that this feature supports a color loop functionality. The conformance rule for this feature is specified as 'CL'. According to the Matter Conformance Interpretation Guide, this means that the "ColorLoop" feature is mandatory if the 'CL' feature is supported. If the 'CL' feature is not supported, the conformance rule does not specify any alternative requirement, implying that the "ColorLoop" feature would not be required in such cases.

* In the context of the Color Control Cluster, the table row describes a data type with the bit identifier '3' and the name 'XY', which supports color specification via XY coordinates. The conformance rule 'XY' indicates that this element is mandatory if the feature 'XY' is supported. This means that if a device or implementation includes support for the XY feature, then the 'XY' data type must be included as part of its configuration. If the feature 'XY' is not supported, the conformance rule does not apply, and the inclusion of this data type is not required.

* The table row describes an element within the Color Control Cluster, specifically a data type called 'ColorTemperature', which is represented by bit '4'. This element allows for the specification of color through color temperature. The 'Conformance' field for 'ColorTemperature' is marked as 'CT'. According to the Matter Conformance Interpretation Guide, 'CT' is a feature code that likely corresponds to a specific condition or feature within the Matter specification. In this context, the 'ColorTemperature' element is mandatory if the 'CT' feature is supported. If 'CT' is not supported, the conformance of this element is not explicitly defined in the provided data, suggesting that further documentation would be needed to determine its status in such cases.

3.2.6.2. OptionsBitmap Type
This data type is derived from map8.

_Table parsed from section 'Data Types':_

* In the Color Control Cluster, under the Data Types section, the table row describes a feature named "ExecuteIfOff," which is associated with bit '0' and has a summary indicating a dependency on the On/Off cluster. The conformance rule for "ExecuteIfOff" is marked as 'M', meaning it is mandatory. This indicates that the "ExecuteIfOff" feature is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions. This mandatory status ensures that the feature is consistently available across all implementations that include this cluster, maintaining interoperability and functionality standards.

3.2.6.2.1. ExecuteIfOff Bit
This bit SHALL indicate if this cluster server instance has a dependency with the On/Off cluster.
3.2.6.3. UpdateFlagsBitmap Type
This data type is derived from map8 and is used in the ColorLoopSet command.

_Table parsed from section 'Data Types':_

* In the Color Control Cluster, under the Data Types section, the table entry for 'UpdateAction' with a bit value of '0' indicates that this data type is associated with the device's adherence to the specified action field. The conformance rule for 'UpdateAction' is marked as 'M', which stands for Mandatory. This means that the 'UpdateAction' element is always required and must be implemented in any device that supports the Color Control Cluster, without any conditions or exceptions.

_Table parsed from section 'Data Types':_

* In the Color Control Cluster, under the Data Types section, the table row describes a feature called "UpdateDirection," which is identified by the bit value '1'. The summary indicates that this feature involves the device updating the associated direction attribute. The conformance rule for "UpdateDirection" is marked as 'M', which stands for Mandatory. This means that the feature is always required to be implemented in any device that supports the Color Control Cluster, with no conditions or exceptions.

* In the context of the Color Control Cluster's data types, the table row describes an element named "UpdateTime," which is associated with the bit position '2'. The summary indicates that this element is responsible for updating the associated time attribute on the device. The conformance rule for "UpdateTime" is marked as 'M', which stands for Mandatory. This means that the "UpdateTime" element is always required to be implemented in any device that supports the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit number '3', named 'UpdateStartHue'. This feature involves the device updating the associated start hue attribute. According to the conformance rule 'M', this feature is mandatory, meaning that any device implementing the Color Control Cluster must include and support the 'UpdateStartHue' feature without exception. This requirement ensures consistent functionality across devices that utilize this cluster.

3.2.6.3.1. UpdateAction Bit
This bit SHALL indicate whether the server adheres to the Action field in order to process the com
mand.
• 0 = Device SHALL ignore the Action field.
• 1 = Device SHALL adhere to the Action field.
3.2.6.3.2. UpdateDirection Bit
This bit SHALL indicate whether the device updates the ColorLoopDirection attribute with the
Direction field.
• 0 = Device SHALL ignore the Direction field.
• 1 = Device SHALL update the ColorLoopDirection attribute with the value of the Direction field.
3.2.6.3.3. UpdateTime Bit
This bit SHALL indicate whether the device updates the ColorLoopTime attribute with the Time
field.
• 0 = Device SHALL ignore the Time field.
• 1 = Device SHALL update the value of the ColorLoopTime attribute with the value of the Time
field.
3.2.6.3.4. UpdateStartHue Bit
This bit SHALL indicate whether the device updates the ColorLoopStartEnhancedHue attribute with
the value of the StartHue field.
• 0 = Device SHALL ignore the StartHue field.
• 1 = Device SHALL update the value of the ColorLoopStartEnhancedHue attribute with the value
of the StartHue field.
3.2.6.4. DriftCompensationEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster's Data Types, the table row describes an entry with the value '0' and the name 'None', which summarizes that there is no compensation. The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that within the Color Control Cluster, the 'None' data type must always be included and supported, as it is a required element according to the Matter specification.

* The table row entry pertains to the "Color Control Cluster" within the "Data Types" section and describes a data type with the value '1' named "OtherOrUnknown." This data type indicates that the compensation mechanism is based on an unspecified or unknown method. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the "OtherOrUnknown" data type is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically under the Data Types section, with the name "TemperatureMonitoring." This element has a value of '2' and is summarized as a feature where compensation is based on temperature monitoring. The conformance rule for this element is marked as 'M,' which stands for Mandatory. This means that the TemperatureMonitoring feature is always required to be implemented within the Color Control Cluster, with no conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically under the Data Types section. The element is named "OpticalLuminanceMonitoringAndFeedback" and is identified by the value '3'. Its purpose is to provide compensation based on optical luminance monitoring and feedback. The conformance rule for this element is marked as 'M', which means it is mandatory. This indicates that the "OpticalLuminanceMonitoringAndFeedback" feature is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Data Types section, the entry for 'OpticalColorMonitoringAndFeedback' with a value of '4' indicates a feature where the compensation is based on optical color monitoring and feedback. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'OpticalColorMonitoringAndFeedback' feature is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.6.5. ColorModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the Color Control Cluster within the Data Types section, specifically focusing on the 'CurrentHueAndCurrentSaturation' attribute. This attribute is identified by the value '0' and is summarized as determining the color through the current hue and saturation attributes. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'CurrentHueAndCurrentSaturation' attribute is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Data Types section, the entry for 'CurrentXAndCurrentY' with a value of '1' represents attributes that determine the color by specifying the current X and Y coordinates. The conformance rule 'M' indicates that these attributes are mandatory, meaning they are always required to be implemented in any device or application that supports the Color Control Cluster. This ensures that the functionality to determine color through these coordinates is consistently available across all compliant implementations.

* In the Color Control Cluster, under the Data Types section, the table entry for 'ColorTemperatureMireds' indicates that this attribute is used to determine the color temperature. The 'Value' assigned to this attribute is '2'. According to the conformance rule 'M', this attribute is mandatory, meaning it is always required to be implemented in any device or application that supports the Color Control Cluster. There are no conditions or exceptions to this requirement, ensuring that the 'ColorTemperatureMireds' attribute is consistently available for use in controlling color temperature across all relevant implementations.

3.2.6.6. EnhancedColorModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "Color Control Cluster" within the "Data Types" section and describes a data type named "CurrentHueAndCurrentSaturation." This data type is identified by the value '0' and is summarized as determining the color through the current hue and saturation attributes. The conformance rule for this entry is marked as 'M,' which stands for Mandatory. This means that the "CurrentHueAndCurrentSaturation" data type is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the Color Control Cluster within the Data Types section, specifically focusing on an element named "CurrentXAndCurrentY." This element is summarized as determining the color through its current X and Y attributes. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "CurrentXAndCurrentY" element is always required to be implemented in any device or application that supports the Color Control Cluster according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, making it a fundamental component for color determination in this context.

_Table parsed from section 'Data Types':_

* The table row entry pertains to the "ColorTemperatureMireds" attribute within the Color Control Cluster, specifically under the Data Types section. This attribute is responsible for determining the color temperature, which is a crucial aspect of color management in lighting systems. The conformance rule for "ColorTemperatureMireds" is marked as "M," indicating that this attribute is mandatory. This means it is always required to be implemented in any device or system that supports the Color Control Cluster, ensuring consistent functionality related to color temperature across all compliant devices.

* The table row describes an element within the Color Control Cluster, specifically under the Data Types section. The element is named "EnhancedCurrentHueAndCurrentSaturation" and is identified by the value '3'. This element pertains to attributes that determine the color through enhanced current hue and saturation. The conformance rule for this element is 'M', which stands for Mandatory. This means that the "EnhancedCurrentHueAndCurrentSaturation" element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.6.7. DirectionEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster's Data Types, the table row describes an entry with the value '0', named 'Shortest', which summarizes as 'Shortest distance'. The conformance rule for this entry is 'M', indicating that it is a Mandatory element. This means that the 'Shortest' data type must always be included and supported within the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster under the Data Types section, the table row describes an entry with the value '1', named 'Longest', which summarizes as 'Longest distance'. The conformance rule for this entry is 'M', indicating that it is a mandatory element. This means that the 'Longest' data type must always be implemented and supported in any device or application that adheres to the Matter specification for the Color Control Cluster. There are no conditions or exceptions to this requirement; it is an essential component of the specification.

* This table row pertains to the Color Control Cluster within the Data Types section and describes an element named "Up" with a value of "2." The summary also labels it as "Up." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Up" element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the Color Control Cluster within the Data Types section, specifically detailing an element named "Down" with a value of "3." The summary also describes it as "Down." The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Down" element is always required in any implementation of the Color Control Cluster, with no conditions or exceptions. It must be included and supported as part of the cluster's functionality according to the Matter specification.

3.2.6.8. MoveModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster, specifically within the Data Types section, the table row describes an entry with the value '0', named 'Stop', which is summarized as 'Stop the movement'. The conformance rule for this entry is 'M', indicating that it is a Mandatory element. This means that the 'Stop' command or feature is always required to be implemented within the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, specifically within the Data Types section, the table entry describes a data type with the value '1' named 'Up', which is summarized as representing a movement in an upwards direction. The conformance rule for this entry is marked as 'M', indicating that this element is mandatory. This means that the 'Up' data type is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Data Types section, the table row describes an element with the name "Down," which has a value of "3" and a summary indicating that it represents a movement in a downwards direction. The conformance rule for this element is marked as "M," which stands for Mandatory. This means that the "Down" element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.6.9. StepModeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster, specifically within the Data Types section, the table row describes an element with the name "Up," which has a value of '1' and is summarized as "Step in an upwards direction." The conformance rule for this element is marked as 'M,' indicating that it is mandatory. This means that the "Up" element is always required to be implemented in any system or device that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Data Types section, the table row describes an entry with the value '3', named 'Down', which summarizes the action of stepping in a downwards direction. The conformance rule for this entry is 'M', indicating that it is mandatory. This means that the 'Down' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.6.10. ColorLoopActionEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster, specifically within the Data Types section, the table row describes an entry with the value '0' named 'Deactivate', which serves the purpose of deactivating the color loop. The conformance rule for this entry is marked as 'M', indicating that it is a Mandatory element. This means that the 'Deactivate' function must always be implemented and supported in any device or application that utilizes the Color Control Cluster according to the Matter specification. There are no conditions or exceptions; it is a required feature.

* The table row describes a data type within the Color Control Cluster, specifically the 'ActivateFromColorLoopStartEnhancedHue' feature. This feature is responsible for activating the color loop using the value specified in the ColorLoopStartEnhancedHue field. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the 'ActivateFromColorLoopStartEnhancedHue' feature is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the Color Control Cluster within the Matter IoT specification, specifically under the Data Types section. It describes a feature named "ActivateFromEnhancedCurrentHue," which is identified by the value '2'. This feature allows the activation of a color loop based on the value of the EnhancedCurrentHue attribute. The conformance rule for this feature is marked as 'M', indicating that it is mandatory. This means that any implementation of the Color Control Cluster must include this feature, as it is always required according to the specification.

3.2.6.11. ColorLoopDirectionEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Color Control Cluster's Data Types, the table entry describes a feature named "Decrement," which is used to decrement the hue in the color loop. The conformance rule for this feature is marked as "M," indicating that it is mandatory. This means that the "Decrement" feature must always be implemented and supported in any device or application that adheres to the Matter specification for the Color Control Cluster. There are no conditions or exceptions; it is a required element for compliance.

* In the context of the Color Control Cluster, specifically within the Data Types section, the table entry describes a feature named "Increment" with a value of '1'. This feature is summarized as the ability to increment the hue in the color loop. The conformance rule for this feature is marked as 'M', which stands for Mandatory. This means that the "Increment" feature is always required to be implemented in any device or application that supports the Color Control Cluster according to the Matter specification. There are no conditions or exceptions; it is a fundamental requirement.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Color Control Cluster, specifically the "CurrentHue" attribute. This attribute is identified by the ID `0x0000` and is of type `uint8`, with a constraint that its maximum value is 254. The quality flags `P N Q` suggest specific characteristics or conditions related to the attribute, though these are not detailed in the provided guide. The default value for "CurrentHue" is `0`, and it has read and volatile access permissions, as indicated by `R V`. The conformance rule `HS` means that the "CurrentHue" attribute is mandatory if the feature `HS` (Hue/Saturation) is supported. If the device or implementation supports the `HS` feature, this attribute must be included; otherwise, its inclusion is not required.

* The table row describes an attribute within the Color Control Cluster, specifically the "CurrentSaturation" attribute. This attribute has an ID of '0x0001' and is of type 'uint8', with a constraint that its maximum value is 254. It has a default value of 0 and can be accessed with read (R) and view (V) permissions. The quality indicators 'P S N Q' suggest additional properties or statuses, though these are not defined in the provided context. The conformance rule 'HS' indicates that the "CurrentSaturation" attribute is mandatory if the feature 'HS' (likely referring to Hue and Saturation) is supported. If 'HS' is not supported, the attribute is not required. This means that devices implementing the Color Control Cluster must include this attribute if they support the Hue and Saturation feature.

* The table row describes an attribute within the Color Control Cluster, specifically the "RemainingTime" attribute. This attribute has an ID of '0x0002' and is of type 'uint16', with a constraint that its maximum value is 65534. It is marked with a quality of 'Q', has a default value of '0', and can be accessed with read ('R') and view ('V') permissions. The conformance rule for this attribute is 'O', which means it is optional. This indicates that the "RemainingTime" attribute is not required to be implemented and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Color Control Cluster, specifically the 'CurrentX' attribute. This attribute has an ID of '0x0003' and is of type 'uint16', with a constraint that its maximum value should not exceed 65279. It has a default value of 24939, which corresponds to a normalized value of 0.381. The 'CurrentX' attribute is accessible for reading and verification, as indicated by the 'R V' access specification. The conformance rule 'XY' implies that the 'CurrentX' attribute is mandatory if the feature 'XY' is supported. In other words, if a device or implementation supports the 'XY' feature, it must include the 'CurrentX' attribute.

* The table row describes an attribute named "CurrentY" within the Color Control Cluster, identified by the ID '0x0004'. This attribute is of type 'uint16' and has a constraint that its maximum value is 65279. It has a default value of 24701, which corresponds to 0.377, and its access is read-only and volatile ('R V'). The quality indicators 'P S N Q' suggest specific properties or states relevant to the attribute, such as being persistent, secure, non-volatile, or qualified. The conformance rule 'XY' indicates that the "CurrentY" attribute is mandatory if both features 'X' and 'Y' are supported by the device. If either or both of these features are not supported, the attribute is not required.

* The table row describes an attribute named "DriftCompensation" within the Color Control Cluster, identified by the ID '0x0005'. This attribute is of the type 'DriftCompensationEnum' and applies to all instances of the cluster. It does not have a specified default value and has read and view access permissions ('R V'). The conformance rule for this attribute is 'O', meaning it is optional. This indicates that the implementation of the "DriftCompensation" attribute is not required and does not depend on any other features or conditions. Implementers have the discretion to include or exclude this attribute based on their specific needs or use cases.

* The table row describes an attribute within the Color Control Cluster, specifically the 'CompensationText' attribute. This attribute has an ID of '0x0006' and is of type 'string', with a maximum length constraint of 254 characters. It does not have a default value specified and has read and view access permissions ('R V'). The conformance rule for this attribute is 'O', which means it is optional. This indicates that the 'CompensationText' attribute is not required to be implemented in devices that support the Color Control Cluster, and there are no dependencies or conditions that affect its optional status.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Color Control Cluster, specifically the "ColorTemperatureMireds" attribute, identified by ID '0x0007'. This attribute is of type 'uint16' and is constrained to a maximum value of 65279. It has a default value of 250, which corresponds to a color temperature of 4000K. The attribute's quality is marked as 'P S N Q', and its access is 'R V', indicating it is readable and has volatile characteristics. The conformance rule 'CT' implies that the attribute is mandatory if the Color Temperature feature is supported. If the device supports this feature, it must implement the ColorTemperatureMireds attribute; otherwise, the requirement does not apply.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorMode' attribute. This attribute has an ID of '0x0008' and is of the type 'ColorModeEnum'. It is constrained to apply to all instances, with a default value of '1'. The 'Access' field indicates that this attribute is readable ('R') and has a volatile characteristic ('V'), meaning its value can change without a specific event triggering it. The 'Quality' is marked as 'N', which typically indicates a standard quality level. The 'Conformance' field is marked as 'M', meaning that the 'ColorMode' attribute is mandatory. This implies that any implementation of the Color Control Cluster must include this attribute, as it is always required according to the Matter specification.

* In the Color Control Cluster, within the Attributes section, the table row describes an attribute with the ID '0x000F' named 'Options'. This attribute is of the type 'OptionsBitmap', with constraints described elsewhere in the documentation ('desc'), and it has a default value of '0'. The access level for this attribute is 'RW VO', indicating it is readable and writable with optional verification. The conformance rule for this attribute is 'M', meaning it is mandatory. This implies that the 'Options' attribute must always be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Color Control Cluster, specifically the 'NumberOfPrimaries' attribute, identified by the ID '0x0010'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint limiting its maximum value to 6. The 'Quality' field indicates 'F X', which typically refers to specific quality characteristics, though their exact meaning isn't provided here. The 'Access' field shows 'R V', indicating that the attribute is readable and possibly volatile. The 'Conformance' field is marked as 'M', meaning that the 'NumberOfPrimaries' attribute is mandatory. This implies that any implementation of the Color Control Cluster must include this attribute, as it is always required according to the Matter specification.

* In the Color Control Cluster, under the Attributes section, the attribute 'Primary1X' is identified by the ID '0x0011' and is of type 'uint16', with a constraint that its maximum value can be 65279. It has a quality of 'F', and its access is marked as 'R V', indicating it is readable and has a volatile nature. The conformance rule 'NumberOfPrimaries > 0, O' specifies that this attribute is mandatory if the feature 'NumberOfPrimaries' is greater than zero, meaning that if there is at least one primary color defined, 'Primary1X' must be implemented. Otherwise, if 'NumberOfPrimaries' is not greater than zero, the attribute is optional and does not need to be implemented.

* The table row describes an attribute named "Primary1Y" within the Color Control Cluster, identified by the ID '0x0012'. This attribute is of type 'uint16' and is constrained to a maximum value of 65279. It has a quality designation of 'F' and access rights of 'R V', indicating it is readable and volatile. The conformance rule 'NumberOfPrimaries > 0, O' specifies that the "Primary1Y" attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 0, meaning that if any primary colors are defined, this attribute must be present. Otherwise, if 'NumberOfPrimaries' is not greater than 0, the attribute is optional and not required.

* The table row describes an attribute within the Color Control Cluster, specifically the 'Primary1Intensity' attribute. This attribute has an ID of '0x0013' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that this attribute applies universally within its context. The 'Quality' is marked as 'F X', which typically relates to specific feature or implementation qualities, though the exact meaning isn't provided here. The 'Access' is 'R V', suggesting that the attribute is readable and possibly volatile. The 'Conformance' rule, 'NumberOfPrimaries > 0, O', indicates that the 'Primary1Intensity' attribute is mandatory if the 'NumberOfPrimaries' is greater than zero, meaning that the device supports one or more primary colors. If this condition is not met, the attribute is optional. This rule ensures that the attribute is only required when it is relevant to the device

* The table row describes an attribute named "Primary2X" within the Color Control Cluster, identified by the ID '0x0015'. This attribute is of type 'uint16' and has a constraint that its maximum value should not exceed 65279. The quality 'F' indicates it is a feature attribute, and the access 'R V' signifies it is readable and has a volatile nature. The conformance rule 'NumberOfPrimaries > 1, O' means that the "Primary2X" attribute is mandatory if the device supports more than one primary color (i.e., if the condition 'NumberOfPrimaries > 1' is true). Otherwise, if the device does not support more than one primary color, this attribute is optional.

* The table row describes an attribute named "Primary2Y" within the Color Control Cluster, identified by the ID '0x0016'. This attribute is of type 'uint16' and has a constraint that its maximum value should not exceed 65279. The quality of this attribute is marked as 'F', and it has read and view access ('R V'). The conformance rule 'NumberOfPrimaries > 1, O' indicates that the "Primary2Y" attribute is mandatory if the number of primaries is greater than one. If this condition is not met, the attribute is optional. This means that in devices where more than one primary color is supported, "Primary2Y" must be included, whereas in devices with only one primary color, its inclusion is not required.

* In the Color Control Cluster, under the Attributes section, the entry for 'Primary2Intensity' with ID '0x0017' is of type 'uint8' and applies to all constraints. It has a quality designation of 'F X' and access permissions of 'R V', indicating it is readable and volatile. The conformance rule 'NumberOfPrimaries > 1, O' specifies that this attribute is mandatory if the device supports more than one primary color (i.e., `NumberOfPrimaries > 1` is true). If this condition is not met, the attribute is optional. This means that devices with multiple primary colors must implement this attribute, while those with only one primary color may choose to implement it or not.

* The table row describes an attribute named "Primary3X" within the Color Control Cluster, identified by the ID '0x0019'. It is of type 'uint16' and has a constraint that its maximum value cannot exceed 65279. The attribute is of quality 'F' and has access permissions 'R V', indicating it can be read and is volatile. The conformance rule 'NumberOfPrimaries > 2, O' specifies that the "Primary3X" attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 2, meaning that the device supports more than two primary colors. If this condition is not met, the attribute is optional, indicating it is not required and has no dependencies.

* The table row describes an attribute named "Primary3Y" within the Color Control Cluster, identified by the ID '0x001A'. This attribute is of type 'uint16' and is constrained to a maximum value of 65279. It has a quality of 'F' and access permissions of 'R V', indicating it is readable and has a volatile nature. The conformance rule 'NumberOfPrimaries > 2, O' specifies that the "Primary3Y" attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 2, meaning that the device supports more than two primary colors. If this condition is not met, the attribute is optional, implying it is not required and can be omitted without affecting compliance.

* The table row describes an attribute named "Primary3Intensity" within the Color Control Cluster, identified by the ID '0x001B'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally ('Constraint': 'all'). The 'Quality' field indicates that it is a fixed value ('F') and not allowed to be extended ('X'). The 'Access' field specifies that it is readable ('R') and has a volatile nature ('V'). The conformance rule 'NumberOfPrimaries > 2, O' means that the "Primary3Intensity" attribute is mandatory if the device supports more than two primary colors (i.e., 'NumberOfPrimaries > 2'). If this condition is not met, the attribute is optional.

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "Primary4X" within the Color Control Cluster, identified by the ID '0x0020'. It is of type 'uint16' and has a constraint that its maximum value should not exceed 65279. The attribute is of quality 'F', which typically indicates a specific feature or characteristic, and it has read and view access permissions ('R V'). The conformance rule 'NumberOfPrimaries > 3, O' specifies that this attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 3, meaning that if a device supports more than three primary colors, this attribute must be implemented. Otherwise, if this condition is not met, the attribute is optional, meaning it is not required and can be implemented at the developer's discretion.

* In the Color Control Cluster, under the Attributes section, the attribute 'Primary4Y' is identified by the ID '0x0021' and is of type 'uint16', with a maximum constraint of 65279. It is a feature attribute (Quality: 'F') and has read and view access ('R V'). The conformance rule for 'Primary4Y' is expressed as 'NumberOfPrimaries > 3, O'. This means that the 'Primary4Y' attribute is mandatory if the device supports more than three primary colors (i.e., if the condition 'NumberOfPrimaries > 3' is true). If this condition is not met, the attribute is optional.

* In the Color Control Cluster, within the Attributes section, the attribute 'Primary4Intensity' is identified by the ID '0x0022' and is of type 'uint8'. It has a constraint applicable to all instances and a quality designation of 'F X', indicating specific feature or implementation restrictions. The access level is 'R V', meaning it is readable and possibly volatile. The conformance rule 'NumberOfPrimaries > 3, O' specifies that this attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 3, indicating that the device supports more than three primary colors. If this condition is not met, the attribute is optional, meaning it is not required but can be included without any dependencies.

* The table row describes an attribute named "Primary5X" within the Color Control Cluster, identified by the ID '0x0024'. It is of type 'uint16' and has a constraint limiting its maximum value to 65279. The attribute is of quality 'F' and has access permissions 'R V', indicating it can be read and is volatile. The conformance rule 'NumberOfPrimaries > 4, O' specifies that this attribute is mandatory if the feature 'NumberOfPrimaries' is greater than 4, meaning the device supports more than four primary colors. If this condition is not met, the attribute is optional.

* The table row describes an attribute named "Primary5Y" within the Color Control Cluster's Attributes section. This attribute has an ID of '0x0025' and is of type 'uint16', with a constraint that its maximum value should not exceed 65279. It is marked with a quality of 'F' and has access permissions 'R V', indicating it is readable and can be viewed. The conformance rule 'NumberOfPrimaries > 4, O' specifies that the "Primary5Y" attribute is mandatory if the number of primaries is greater than 4. If this condition is not met, the attribute is optional. This means that the attribute is required only when a device supports more than four primary colors; otherwise, its inclusion is not necessary.

* The table row describes an attribute named "Primary5Intensity" within the Color Control Cluster, identified by the ID '0x0026'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally ('Constraint': 'all'). The 'Quality' field indicates that it is a feature that is disallowed ('F X'), and the 'Access' field specifies that it is readable and volatile ('R V'). The conformance rule 'NumberOfPrimaries > 4, O' means that the "Primary5Intensity" attribute is mandatory if the device supports more than four primary colors. If the device does not support more than four primary colors, the attribute is optional. This rule ensures that the attribute is only required when the device's capabilities necessitate its presence.

* The table row describes an attribute within the Color Control Cluster, specifically the 'Primary6X' attribute, which is identified by the ID '0x0028'. This attribute is of type 'uint16' and has a constraint that its maximum value should not exceed 65279. It is marked with a quality of 'F' and has access permissions of 'R V', indicating it is readable and has a volatile nature. The conformance rule for 'Primary6X' is defined as 'NumberOfPrimaries > 5, O'. This means that the attribute is mandatory if the device supports more than five primary colors (i.e., if the 'NumberOfPrimaries' feature is greater than 5). If this condition is not met, the attribute is optional.

* In the Color Control Cluster, under the Attributes section, the entry for 'Primary6Y' with ID '0x0029' is a 16-bit unsigned integer (uint16) attribute constrained to a maximum value of 65279. It is a feature attribute (Quality: F) with read and view access (Access: R V). The conformance rule 'NumberOfPrimaries > 5, O' indicates that this attribute is mandatory if the device supports more than five primary colors (i.e., if the 'NumberOfPrimaries' attribute is greater than 5). If this condition is not met, the attribute is optional.

* The table row describes an attribute named "Primary6Intensity" within the Color Control Cluster, identified by the ID '0x002A'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies to all instances of the cluster. The 'Quality' field indicates that this attribute is a feature that is disallowed ('F X'), and the 'Access' field specifies that it is readable and volatile ('R V'). The conformance rule 'NumberOfPrimaries > 5, O' means that the "Primary6Intensity" attribute is mandatory if the number of primary colors supported by the device is greater than five. If the device does not support more than five primary colors, this attribute is optional.

* The table row describes an attribute within the Color Control Cluster, specifically the 'WhitePointX' attribute. This attribute has an ID of '0x0030' and is of type 'uint16', with a constraint that its maximum value can be 65279. The access level for this attribute is 'RW VM', indicating it can be read and written, and it is volatile memory. The conformance rule for 'WhitePointX' is 'O', which means this attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

* The table row describes an attribute within the Color Control Cluster, specifically the "WhitePointY" attribute. This attribute has an ID of '0x0031' and is of type 'uint16', with a constraint that its maximum value can be 65279. The access level for this attribute is 'RW VM', indicating that it is readable and writable, with the possibility of being a volatile memory attribute. The conformance rule for "WhitePointY" is 'O', which means that this attribute is optional. It is not required to be implemented and does not have any dependencies or conditions that affect its optional status.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointRX' attribute. This attribute has an ID of '0x0032' and is of type 'uint16', with a constraint that its maximum value cannot exceed 65279. The access level for this attribute is 'RW VM', indicating it is readable and writable, with additional access constraints or conditions specified by 'VM'. The conformance rule for 'ColorPointRX' is 'O', meaning this attribute is optional. It is not required for implementation and does not have any dependencies that would otherwise mandate its inclusion.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointRY' attribute. This attribute has an ID of '0x0033' and is of type 'uint16', with a maximum constraint value of 65279. It has read-write access and is marked as volatile memory ('RW VM'). The conformance rule for 'ColorPointRY' is 'O', which means that this attribute is optional. It is not required for implementation and does not have any dependencies on other features or conditions. Implementers can choose to include this attribute in their devices, but it is not mandatory according to the Matter specification.

* The table row describes an attribute named "ColorPointRIntensity" within the Color Control Cluster. This attribute has an ID of '0x0034' and is of type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', which means this attribute is explicitly disallowed in the current specification. The 'Access' is 'RW VM', suggesting it can be read and written, and it is volatile memory. The 'Conformance' is 'O', indicating that this attribute is optional and not required to be implemented, with no dependencies affecting its optional status.

NumberOf
NumberOf
NumberOf
NumberOf
NumberOf
NumberOf
NumberOf
NumberOf
NumberOf

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointGX' attribute. This attribute is identified by the ID '0x0036' and is of type 'uint16', with a constraint that its maximum value cannot exceed 65279. The access level is 'RW VM', indicating that it can be read and written, and it is volatile and managed. The conformance rule for 'ColorPointGX' is 'O', which means that this attribute is optional. It is not required to be implemented and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointGY' attribute, which has an ID of '0x0037'. This attribute is of type 'uint16' and is constrained to a maximum value of 65279. It has read and write access, indicated by 'RW', and is subject to view management, as denoted by 'VM'. The conformance rule for 'ColorPointGY' is 'O', meaning that this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointGIntensity' attribute, which has an ID of '0x0038' and is of type 'uint8'. The 'Constraint' is listed as 'all', indicating it applies universally within its context. The 'Quality' is marked as 'X', meaning this attribute is explicitly disallowed. The 'Access' is specified as 'RW VM', suggesting it can be read and written, with VM likely indicating a specific access condition or mode. The 'Conformance' is marked as 'O', which means that the 'ColorPointGIntensity' attribute is optional. This indicates that the attribute is not required and has no dependencies, allowing implementers the choice to include it or not without affecting compliance with the Matter specification.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorPointBX' attribute. This attribute is identified by the ID '0x003A' and is of type 'uint16', with a maximum constraint value of 65279. It has an access level of 'RW VM', indicating it is readable and writable, and it can be modified by the manufacturer. The conformance rule for 'ColorPointBX' is 'O', meaning this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions within the Matter specification.

* The table row describes an attribute named "ColorPointBY" within the Color Control Cluster, identified by the ID '0x003B'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value cannot exceed 65279. The access level for this attribute is 'RW VM', indicating it is readable and writable, and it can be modified by the manufacturer. The conformance rule for "ColorPointBY" is 'O', which means that this attribute is optional. It is not required for the implementation of the Color Control Cluster and does not have any dependencies on other features or conditions.

* The table row describes an attribute named "ColorPointBIntensity" within the Color Control Cluster, identified by the ID '0x003C'. This attribute is of type 'uint8', meaning it is an 8-bit unsigned integer, and it applies universally without specific constraints. The 'Quality' is marked as 'X', indicating that this attribute is explicitly disallowed, meaning it should not be implemented or used. The 'Access' is specified as 'RW VM', which means it is readable and writable, with the possibility of being volatile or manufacturer-specific. The 'Conformance' is marked as 'O', signifying that the inclusion of this attribute is optional and not required by default, with no dependencies on other features or conditions.

* The table row describes an attribute within the Color Control Cluster, specifically the 'EnhancedCurrentHue' attribute. This attribute has an ID of '0x4000' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The 'Constraint' is listed as 'all', indicating it applies universally within its context. The 'Quality' field includes 'S N Q', which typically denotes specific characteristics or requirements such as stability, non-volatile storage, or quality of service. The default value for this attribute is '0', and it has 'R V' access, meaning it is readable and possibly volatile. The 'Conformance' field is marked as 'EHUE', which, according to the Matter Conformance Interpretation Guide, implies that the attribute is mandatory if the 'EHUE' feature is supported. If the 'EHUE' feature is not supported, the attribute is not required. This means that the presence of the 'EnhancedCurrentHue' attribute is contingent

* The table row describes an attribute within the Color Control Cluster, specifically the 'EnhancedColorMode' attribute. This attribute is identified by the ID '0x4001' and is of the type 'EnhancedColorModeEnum'. It applies universally, as indicated by the 'Constraint' being 'all'. The 'Quality' field 'S N' suggests specific characteristics or requirements, while the 'Default' value is set to '1'. The 'Access' field 'R V' indicates that this attribute is readable and has some form of volatile behavior. The 'Conformance' field is marked as 'M', which means that the 'EnhancedColorMode' attribute is mandatory. It must always be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Color Control Cluster, specifically the "ColorLoopActive" attribute. This attribute has an ID of '0x4002' and is of type 'uint8', with a constraint that its maximum value is 1. It has a default value of 0 and access permissions denoted as 'R V', which typically means it is readable and possibly volatile. The quality 'S N' suggests it is a standard attribute with no special conditions. The conformance rule 'CL' indicates that this attribute is mandatory if the Color Loop feature (denoted by 'CL') is supported by the device. In other words, if a device supports the Color Loop feature, it must include this attribute; otherwise, the attribute is not required.

* The table row describes an attribute named "ColorLoopDirection" within the Color Control Cluster. This attribute has an ID of '0x4003' and is of type 'uint8', with a constraint that its maximum value is 1. It has a default value of 0 and access permissions denoted by 'R V', indicating it is readable and has a volatile quality. The 'Quality' field 'S N' suggests specific characteristics related to the attribute's stability and notification behavior. The conformance rule 'CL' indicates that this attribute is mandatory if the Color Loop feature (abbreviated as 'CL') is supported by the device. If the device does not support the Color Loop feature, the attribute is not required.

* The table row describes an attribute named "ColorLoopTime" within the Color Control Cluster. This attribute has an ID of '0x4004' and is of type 'uint16', with a constraint applicable to all instances. It has a default value of '25' and can be accessed with read ('R') and view ('V') permissions. The quality indicators 'S N' suggest specific characteristics or requirements, such as stability or non-volatile storage. The conformance rule 'CL' indicates that the "ColorLoopTime" attribute is mandatory if the Color Loop feature (denoted by 'CL') is supported by the device. If the device does not support the Color Loop feature, this attribute is not required.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorLoopStartEnhancedHue' attribute. This attribute has an ID of '0x4005' and is of type 'uint16', with a constraint of 'all', meaning it applies universally within its context. Its default value is '8960', and it has an access level of 'R V', indicating it is readable and can be viewed. The conformance rule 'CL' means that this attribute is mandatory if the Color Loop feature (denoted by 'CL') is supported by the device. If the device does not support the Color Loop feature, the attribute is not required.

* The table row describes an attribute within the Color Control Cluster, specifically the "ColorLoopStoredEnhancedHue" attribute. This attribute has an ID of '0x4006' and is of type 'uint16', with a constraint applicable to all instances. Its default value is '0', and it has read and view access ('R V'). The conformance rule 'CL' indicates that this attribute is mandatory if the feature 'CL' (likely representing Color Loop) is supported. In other words, if a device supports the Color Loop feature, it must also support the ColorLoopStoredEnhancedHue attribute.

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Color Control Cluster, specifically the "ColorCapabilities" attribute. This attribute has an ID of '0x400A' and is of the type 'ColorCapabilitiesBitmap', with a constraint limiting its maximum value to '0x001F'. The default value for this attribute is '0', and it has read and view access permissions, denoted by 'R V'. The conformance rule for this attribute is 'M', which means it is mandatory. This indicates that the "ColorCapabilities" attribute is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Color Control Cluster, specifically the 'ColorTempPhysicalMinMireds' attribute, identified by the ID '0x400B'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its value must be between 1 and 65279. The 'Access' field indicates that this attribute is readable ('R') and has a volatile ('V') nature, suggesting it may change without a specific event triggering it. The 'Conformance' field is 'CT', which implies that this attribute is mandatory if the Color Temperature (CT) feature is supported by the device. If the device does not support the CT feature, the attribute is not required.

* The table row describes an attribute within the Color Control Cluster, specifically the "ColorTempPhysicalMaxMireds" attribute, identified by the ID '0x400C'. This attribute is of type 'uint16' and has a constraint with a maximum value of 65279. It is accessible for reading and is considered volatile, as indicated by the 'R V' access specification. The conformance rule 'CT' implies that this attribute is mandatory if the feature 'CT' (likely representing Color Temperature) is supported. Therefore, if a device supports the Color Temperature feature, it must include this attribute.

* The table row describes an attribute within the Color Control Cluster, specifically the "CoupleColorTempToLevelMinMireds" attribute, which has an ID of '0x400D' and is of type 'uint16'. This attribute is constrained between the values of 'ColorTempPhysicalMinMireds' and 'ColorTemperatureMireds'. Its default value is 'MS', and it has read and view access ('R V'). The conformance rule 'CT | ColorTemperatureMired' indicates that this attribute is mandatory if either the 'CT' feature or the 'ColorTemperatureMired' feature is supported. In simpler terms, the attribute must be implemented if the device supports controlling color temperature or specifically supports the 'ColorTemperatureMired' feature.

* The table row describes an attribute within the Color Control Cluster, specifically the 'StartUpColorTemperatureMireds' attribute, identified by ID '0x4010'. This attribute is of type 'uint16', constrained to values between 1 and 65279. The 'Quality' field indicates it is not executable ('N') and disallowed ('X') under certain conditions. The default value is 'MS', and it has read-write access ('RW') with a viewable and modifiable ('VM') quality. The conformance rule 'CT | ColorTemperatureMired' means that the 'StartUpColorTemperatureMireds' attribute is mandatory if either the 'CT' feature or the 'ColorTemperatureMired' feature is supported. If neither feature is supported, the attribute is not required.

orTemper
tureMireds
orTemper
tureMireds
3.2.7.1. Scene Table Extensions
If the Scenes Management server cluster is implemented on the same endpoint, the following
attributes SHALL be part of the ExtensionFieldSetStruct of the Scene Table. If an attribute is not
implemented, the value that will be used for it in the AttributeValuePairStruct is given in parenthe
ses. If the implicit form of the ExtensionFieldSetStruct is used, the order of the attributes in the
AttributeValueList is in the given order, i.e., the attribute listed as 1 is added first:
1. CurrentX (0)
2. CurrentY (0)
3. EnhancedCurrentHue (null)
4. CurrentSaturation (null)
5. ColorLoopActive (0)
6. ColorLoopDirection (0)
7. ColorLoopTime (0)
8. ColorTemperatureMireds (null)
9. EnhancedColorMode
Since there is a direct relation between ColorTemperatureMireds and XY, color temperature, if sup
ported, is stored as XY in the scenes table.
Attributes in the scene table that are not supported by the device (according to the FeatureMap
attribute) SHALL be present in the scene table but ignored.
If the Scenes Management cluster server is implemented on the same endpoint, and the cluster
revision is 6 or above, then all extension fields in the list above, including up to EnhancedColor
Mode (item 9), SHALL be present in the extension fields set for a Scene to be considered valid. This
disambiguates the color mode used within the Scene.
3.2.7.2. CurrentHue Attribute
The CurrentHue attribute contains the current hue value of the light. It is updated as fast as practi
cal during commands that change the hue.
The hue in degrees SHALL be related to the CurrentHue attribute by the relationship:
Hue = "CurrentHue" * 360 / 254
where CurrentHue is in the range from 0 to 254 inclusive.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
3.2.7.3. CurrentSaturation Attribute
This attribute SHALL indicate the current saturation value of the light. It is updated as fast as prac
tical during commands that change the saturation.
The saturation (on a scale from 0.0 to 1.0) SHALL be related to the CurrentSaturation attribute by
the relationship:
Saturation = "CurrentSaturation" / 254
where CurrentSaturation is in the range from 0 to 254 inclusive.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
3.2.7.4. RemainingTime Attribute
This attribute SHALL indicate the time remaining, in 1/10ths of a second, until transitions due to the
currently active command will be complete.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• When it changes from 0 to any value higher than 10, or
• When it changes, with a delta larger than 10, caused by the invoke of a command, or
• When it changes to 0.
For commands with a transition time or changes to the transition time less than 1 second, changes
to this attribute SHALL NOT be reported.
As this attribute is not being reported during a regular countdown, clients SHOULD NOT rely on the
reporting of this attribute in order to keep track of the remaining duration.
3.2.7.5. CurrentX Attribute
This attribute SHALL indicate the current value of the normalized chromaticity value x, as defined
in the CIE xyY Color Space. It is updated as fast as practical during commands that change the color.
The value of x SHALL be related to the CurrentX attribute by the relationship
x = "CurrentX" / 65536
where CurrentX is in the range from 0 to 65279 inclusive.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
3.2.7.6. CurrentY Attribute
This attribute SHALL indicate the current value of the normalized chromaticity value y, as defined
in the CIE xyY Color Space. It is updated as fast as practical during commands that change the color.
The value of y SHALL be related to the CurrentY attribute by the relationship
y = "CurrentY" / 65536
where CurrentY is in the range from 0 to 65279 inclusive.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
3.2.7.7. DriftCompensation Attribute
This attribute SHALL indicate what mechanism, if any, is in use for compensation for color/inten
sity drift over time.
3.2.7.8. CompensationText Attribute
This attribute SHALL contain a textual indication of what mechanism, if any, is in use to compen
sate for color/intensity drift over time.
3.2.7.9. ColorTemperatureMireds Attribute
This attribute SHALL indicate a scaled inverse of the current value of the color temperature. The
unit of ColorTemperatureMireds is the mired (micro reciprocal degree), a.k.a. mirek (micro recipro
cal kelvin). It is updated as fast as practical during commands that change the color.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
The color temperature value in kelvins SHALL be related to the ColorTemperatureMireds attribute
in mired by the relationship
"Color temperature [K]" = "1,000,000" / "ColorTemperatureMireds"
where ColorTemperatureMireds is in the range from 1 to 65279 inclusive, giving a color tempera
ture range from 1,000,000 K to 15.32 K.
If this attribute is implemented then the ColorMode attribute SHALL also be implemented.
3.2.7.10. ColorMode Attribute
This attribute SHALL indicate which attributes are currently determining the color of the device.
The value of the ColorMode attribute cannot be written directly - it is set upon reception of any
command in section Commands to the appropriate mode for that command.
3.2.7.11. Options Attribute
This attribute SHALL indicate a bitmap that determines the default behavior of some cluster com
mands. Each command that is dependent on the Options attribute SHALL first construct a tempo
rary Options bitmap that is in effect during the command processing. The temporary Options
bitmap has the same format and meaning as the Options attribute, but includes any bits that may
be overridden by command fields.
This attribute is meant to be changed only during commissioning.
Below is the format and description of the Options attribute and temporary Options bitmap and the
effect on dependent commands.
Command execution SHALL NOT continue beyond the Options processing if all of these criteria are
true:
• The On/Off cluster exists on the same endpoint as this cluster.
• The OnOff attribute of the On/Off cluster, on this endpoint, is FALSE.
• The value of the ExecuteIfOff bit is 0.
3.2.7.11.1. ExecuteIfOff Bit
• 0 = Do not execute command if the OnOff attribute in the On/Off cluster is FALSE.
• 1 = Execute command if the OnOff attribute in the On/Off cluster is FALSE.
3.2.7.12. EnhancedCurrentHue Attribute
This attribute SHALL indicate the non-equidistant steps along the CIE 1931 color triangle, and it
provides 16-bits precision.
The upper 8 bits of this attribute SHALL be used as an index in the implementation specific XY
lookup table to provide the non-equidistant steps. The lower 8 bits SHALL be used to interpolate
between these steps in a linear way in order to provide color zoom for the user.
To provide compatibility with clients not supporting EHUE, the CurrentHue attribute SHALL con
tain a hue value in the range 0 to 254, calculated from the EnhancedCurrentHue attribute.
Changes to this attribute SHALL only be marked as reportable in the following cases:
• At most once per second or
• At the end of the movement/transition.
3.2.7.13. EnhancedColorMode Attribute
This attribute SHALL indicate which attributes are currently determining the color of the device.
To provide compatibility with clients not supporting EHUE, the original ColorMode attribute SHALL
indicate CurrentHue and CurrentSaturation when the light uses the EnhancedCurrentHue attribute.
If the ColorMode attribute is changed, its new value SHALL be copied to the EnhancedColorMode
attribute.
3.2.7.14. ColorLoopActive Attribute
This attribute SHALL indicate the current active status of the color loop. If this attribute has the
value 0, the color loop SHALL NOT be active. If this attribute has the value 1, the color loop SHALL
be active.
3.2.7.15. ColorLoopDirection Attribute
This attribute SHALL indicate the current direction of the color loop. If this attribute has the value
0, the EnhancedCurrentHue attribute SHALL be decremented. If this attribute has the value 1, the
EnhancedCurrentHue attribute SHALL be incremented.
3.2.7.16. ColorLoopTime Attribute
This attribute SHALL indicate the number of seconds it SHALL take to perform a full color loop, i.e.,
to cycle all values of the EnhancedCurrentHue attribute (between 0 and 65534).
3.2.7.17. ColorLoopStartEnhancedHue Attribute
This attribute SHALL indicate the value of the EnhancedCurrentHue attribute from which the color
loop SHALL be started.
3.2.7.18. ColorLoopStoredEnhancedHue Attribute
This attribute SHALL indicate the value of the EnhancedCurrentHue attribute before the color loop
was started. Once the color loop is complete, the EnhancedCurrentHue attribute SHALL be restored
to this value.
3.2.7.19. ColorCapabilities Attribute
This attribute SHALL indicate the color control capabilities of the device.
Bits 0-4 of the ColorCapabilities attribute SHALL have the same values as the corresponding bits of
the FeatureMap attribute. All other bits in ColorCapabilities SHALL be 0.
3.2.7.20. ColorTempPhysicalMinMireds Attribute
This attribute SHALL indicate the minimum mired value supported by the hardware. ColorTemp
PhysicalMinMireds corresponds to the maximum color temperature in kelvins supported by the
hardware.
<=
ColorTempPhysicalMinMireds   ColorTemperatureMireds.
3.2.7.21. ColorTempPhysicalMaxMireds Attribute
This attribute SHALL indicate the maximum mired value supported by the hardware. ColorTemp
PhysicalMaxMireds corresponds to the minimum color temperature in kelvins supported by the
hardware.
<=
ColorTemperatureMireds   ColorTempPhysicalMaxMireds.
3.2.7.22. CoupleColorTempToLevelMinMireds Attribute
This attribute SHALL indicate a lower bound on the value of the ColorTemperatureMireds attribute
for the purposes of coupling the ColorTemperatureMireds attribute to the CurrentLevel attribute
when the CoupleColorTempToLevel bit of the Options attribute of the Level Control cluster is equal
to 1. When coupling the ColorTemperatureMireds attribute to the CurrentLevel attribute, this value
SHALL correspond to a CurrentLevel value of 254 (100%).
This attribute SHALL be set such that the following relationship exists:
<= <=
ColorTempPhysicalMinMireds   CoupleColorTempToLevelMinMireds   ColorTemperatureMireds
Note that since this attribute is stored as a micro reciprocal degree (mired) value (i.e. color temper
ature  in  kelvins  =  1,000,000  /  CoupleColorTempToLevelMinMireds),  the  CoupleColorTemp
ToLevelMinMireds attribute corresponds to an upper bound on the value of the color temperature
in kelvins supported by the device.
3.2.7.23. StartUpColorTemperatureMireds Attribute
This attribute SHALL indicate the desired startup color temperature value the light SHALL use
when it is supplied with power and this value SHALL be reflected in the ColorTemperatureMireds
attribute. In addition, the ColorMode and EnhancedColorMode attributes SHALL be set to 2 (Col
orTemperatureMireds). The values of the StartUpColorTemperatureMireds attribute are listed in
the table below,

_Table parsed from section 'Attributes':_

* This entry pertains to the Color Control Cluster, specifically within the Attributes section, and it describes the behavior of the "ColorTemperatureMireds" attribute. The attribute can have a value ranging from 1 to 65279. Upon powering up, the device should set the "ColorTemperatureMireds" attribute to the specified value. The conformance rule for this attribute is not explicitly provided in the given data, but based on the context, it likely involves conditions under which this attribute must be set or adjusted. If the conformance rule were provided, it would dictate whether setting this attribute is mandatory, optional, or subject to specific conditions based on the presence or absence of certain features or other attributes.

* In the context of the Color Control Cluster, specifically within the Attributes section, the table row describes an action related to the 'Value' attribute, which is set to 'null'. The action specified is that upon power-up, the 'ColorTemperatureMireds' attribute should be restored to its previous value. The conformance rule for this entry is not explicitly provided in the data, but given the context, it implies that this behavior is expected to be implemented in devices supporting the Color Control Cluster. If the conformance were specified, it would dictate whether this action is mandatory, optional, or subject to certain conditions based on the presence of specific features or other criteria. Without a specific conformance string, it is assumed to be a standard behavior for devices implementing this cluster.

Set the ColorTemperatureMireds attribute to this
3.2.7.24. NumberOfPrimaries Attribute
This attribute SHALL indicate the number of color primaries implemented on this device. A value
of null SHALL indicate that the number of primaries is unknown.
Where this attribute is implemented, the attributes below for indicating the “x” and “y” color values
of the primaries SHALL also be implemented for each of the primaries from 1 to NumberOfPri
maries, without leaving gaps. Implementation of the Primary1Intensity attribute and subsequent
intensity attributes is optional.
3.2.7.25. Primary1X Attribute
This attribute SHALL indicate the normalized chromaticity value x for this primary, as defined in
the CIE xyY Color Space.
The value of x SHALL be related to the Primary1X attribute by the relationship
x = Primary1X / 65536 (Primary1X in the range 0 to 65279 inclusive)
3.2.7.26. Primary1Y Attribute
This attribute SHALL indicate the normalized chromaticity value y for this primary, as defined in
the CIE xyY Color Space.
The value of y SHALL be related to the Primary1Y attribute by the relationship
y = Primary1Y / 65536 (Primary1Y in the range 0 to 65279 inclusive)
3.2.7.27. Primary1Intensity Attribute
This attribute SHALL indicate a representation of the maximum intensity of this primary as defined
in the Dimming Light Curve in the Ballast Configuration cluster (see Ballast Configuration Cluster),
normalized such that the primary with the highest maximum intensity contains the value 254.
A value of null SHALL indicate that this primary is not available.
3.2.7.28. Primary2X, Primary2Y, Primary2Intensity, Primary3X, Primary3Y, Primary3Intensity,
Primary4X, Primary4Y, Primary4Intensity, Primary5X, Primary5Y, Primary5Intensity,
Primary6X, Primary6Y and Primary6Intensity Attributes
nd rd th th th
These attributes SHALL represent the capabilities of the 2 , 3 , 4 , 5  and 6  primaries, where
present, in the same way as for the Primary1X, Primary1Y and Primary1Intensity attributes.
3.2.7.29. WhitePointX Attribute
This attribute SHALL indicate the normalized chromaticity value x, as defined in the CIE xyY Color
Space, of the current white point of the device.
The value of x SHALL be related to the WhitePointX attribute by the relationship
x = WhitePointX / 65536 (WhitePointX in the range 0 to 65279 inclusive)
3.2.7.30. WhitePointY Attribute
This attribute SHALL indicate the normalized chromaticity value y, as defined in the CIE xyY Color
Space, of the current white point of the device.
The value of y SHALL be related to the WhitePointY attribute by the relationship
y = WhitePointY / 65536 (WhitePointY in the range 0 to 65279 inclusive)
3.2.7.31. ColorPointRX Attribute
This attribute SHALL indicate the normalized chromaticity value x, as defined in the CIE xyY Color
Space, of the red color point of the device.
The value of x SHALL be related to the ColorPointRX attribute by the relationship
x = ColorPointRX / 65536 (ColorPointRX in the range 0 to 65279 inclusive)
3.2.7.32. ColorPointRY Attribute
This attribute SHALL indicate the normalized chromaticity value y, as defined in the CIE xyY Color
Space, of the red color point of the device.
The value of y SHALL be related to the ColorPointRY attribute by the relationship
y = ColorPointRY / 65536 (ColorPointRY in the range 0 to 65279 inclusive)
3.2.7.33. ColorPointRIntensity Attribute
This attribute SHALL indicate a representation of the relative intensity of the red color point as
defined in the Dimming Light Curve in the Ballast Configuration cluster (see Ballast Configuration
Cluster), normalized such that the color point with the highest relative intensity contains the value
254.
A value of null SHALL indicate an invalid value.
3.2.7.34. ColorPointGX, ColorPointGY, ColorPointGIntensity, ColorPointBX, ColorPointBY and
ColorPointBIntensity Attributes
These attributes SHALL represent the chromaticity values and intensities of the green and blue
color points, in the same way as for the ColorPointRX, ColorPointRY and ColorPointRIntensity
attributes.
If any one of these red, green or blue color point attributes is implemented then they SHALL all be
implemented.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "MoveToHue" command. This command is initiated by a client and directed to a server, with a response expected from the server, as indicated by the 'Response' field marked 'Y'. The 'Access' field is marked 'O', meaning the command is optional in terms of access control. The 'Conformance' field is 'HS', which, according to the Matter Conformance Interpretation Guide, means that the "MoveToHue" command is mandatory if the feature 'HS' (likely referring to Hue and Saturation) is supported by the device. If the device does not support the 'HS' feature, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "MoveHue" command. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The 'Access: O' suggests that access to this command is optional. The 'Conformance: HS' indicates that the "MoveHue" command is mandatory if the feature 'HS' (likely representing Hue and Saturation) is supported. In essence, if a device supports the Hue and Saturation feature, it must implement the "MoveHue" command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "StepHue" command, which is identified by the ID '0x02'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'HS' indicates that the "StepHue" command is mandatory if the feature 'HS' is supported. In other words, if the device supports the 'HS' feature, it must implement the "StepHue" command; otherwise, there is no obligation to include it.

* The table row describes a command within the Color Control Cluster, specifically the "MoveToSaturation" command, which is identified by the ID '0x03'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'HS' indicates that the command is mandatory if the feature 'HS' (Hue and Saturation) is supported. In summary, the "MoveToSaturation" command must be implemented if the device supports the Hue and Saturation feature, otherwise, it is not required.

* The table row describes a command within the Color Control Cluster, specifically the "MoveSaturation" command, which is identified by the ID '0x04'. This command is directed from the client to the server, and it requires a response ('Y'). The access level is marked as 'Optional' ('O'), indicating that the implementation of this command is not mandatory and has no dependencies. The conformance rule 'HS' specifies that the command is mandatory if the feature 'HS' (Hue and Saturation) is supported. Therefore, if a device supports the 'HS' feature, it must implement the "MoveSaturation" command; otherwise, the command is not required.

* The table row describes a command named "StepSaturation" within the Color Control Cluster, which is directed from the client to the server. This command requires a response, as indicated by 'Response: Y', and has an optional access level ('Access: O'). The conformance rule 'HS' specifies that the "StepSaturation" command is mandatory if the feature 'HS' (Hue/Saturation) is supported. In other words, if a device supports the Hue/Saturation feature, it must implement the "StepSaturation" command. If the device does not support this feature, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "MoveToHueAndSaturation" command, which is identified by the ID '0x06'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'HS' indicates that the command is mandatory if the feature 'HS' (Hue and Saturation) is supported. Therefore, if a device supports the Hue and Saturation feature, it must implement the "MoveToHueAndSaturation" command.

* The table row describes a command within the Color Control Cluster, specifically the "MoveToColor" command, which is identified by the ID '0x07'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'XY' indicates that the "MoveToColor" command is mandatory if both features 'X' and 'Y' are supported. If either or both of these features are not supported, the command is not required. This entry outlines the conditions under which the "MoveToColor" command must be implemented in a device supporting the Color Control Cluster.

* The table row describes a command within the Color Control Cluster, specifically the "MoveColor" command, which is identified by the ID '0x08'. This command is directed from the client to the server and requires a response ('Y'). The access level is marked as 'Optional' ('O'), indicating that the command is not required and has no dependencies. The conformance rule 'XY' means that the "MoveColor" command is mandatory if both features 'X' and 'Y' are supported. If either or both of these features are not supported, the command is not required. This entry outlines the conditions under which the "MoveColor" command must be implemented in a device supporting the Color Control Cluster.

* The table row describes a command within the Color Control Cluster, specifically the "StepColor" command, identified by the ID '0x09'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'XY' indicates that the "StepColor" command is mandatory if both features 'X' and 'Y' are supported. If either or both of these features are not supported, the command is not required. This entry outlines the conditions under which the "StepColor" command must be implemented in a device that supports the Color Control Cluster.

* The table row describes a command within the Color Control Cluster, specifically the "MoveToColorTemperature" command, which is identified by the ID '0x0A'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'CT', indicating that it is mandatory if the feature 'CT' (Color Temperature) is supported. Therefore, if a device supports the Color Temperature feature, it must implement the "MoveToColorTemperature" command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "EnhancedMoveToHue" command, which is identified by the ID '0x40'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required to be implemented and has no dependencies. The conformance rule 'EHUE' indicates that the command is mandatory if the feature 'EHUE' is supported. Therefore, if a device supports the 'EHUE' feature, it must implement the "EnhancedMoveToHue" command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the 'EnhancedMoveHue' command, which is identified by the ID '0x41'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented unless specified by other conditions. The conformance rule 'EHUE' indicates that the command is mandatory if the 'EHUE' feature is supported. In this context, 'EHUE' likely refers to a specific feature or capability related to enhanced hue control. Therefore, the 'EnhancedMoveHue' command must be implemented if the device supports the 'EHUE' feature; otherwise, it is not required.

* The table row describes a command within the Color Control Cluster, specifically the "EnhancedStepHue" command, which is identified by the ID '0x42'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'EHUE' indicates that the command is mandatory if the feature 'EHUE' (Enhanced Hue) is supported. In other words, if a device supports the Enhanced Hue feature, it must implement the EnhancedStepHue command; otherwise, the command is not required.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "EnhancedMoveToHueAndSaturation" command, which is identified by the ID '0x43'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'EHUE' indicates that the command is mandatory if the feature 'EHUE' is supported. Therefore, if a device supports the 'EHUE' feature, it must implement this command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "ColorLoopSet" command, which is identified by the ID '0x44'. This command is directed from the client to the server and requires a response, as indicated by 'Response: Y'. The access level for this command is optional ('Access: O'), meaning it is not required and has no dependencies. The conformance rule 'CL' indicates that the command is mandatory if the feature 'CL' (likely representing a specific capability or feature within the Color Control Cluster) is supported. Therefore, if a device supports the 'CL' feature, it must implement the "ColorLoopSet" command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "StopMoveStep" command, which is identified by the ID '0x47'. This command is sent from a client to a server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented unless certain conditions are met. The conformance rule 'HS | XY | CT' indicates that the "StopMoveStep" command is mandatory if any of the features 'HS', 'XY', or 'CT' are supported by the device. In simpler terms, if a device supports any of these features related to color control, it must also support the "StopMoveStep" command; otherwise, the command is not required.

* The table row describes a command within the Color Control Cluster, specifically the "MoveColorTemperature" command, which is identified by the ID '0x4B'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule for this command is 'CT', indicating that it is mandatory if the feature 'CT' (likely representing Color Temperature) is supported. If the feature 'CT' is not supported, the command is not required. This conformance rule ensures that the "MoveColorTemperature" command is implemented only in devices that support the relevant feature, maintaining compatibility and functionality within the Matter IoT specification.

* The table row describes a command within the Color Control Cluster, specifically the "StepColorTemperature" command, which is identified by the ID '0x4C'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required and has no dependencies. The conformance rule 'CT' indicates that the command is mandatory if the feature 'CT' (likely representing Color Temperature) is supported. If 'CT' is not supported, the command is not required. Thus, the implementation of this command depends on the presence of the 'CT' feature within the device's capabilities.

3.2.8.1. Generic Usage Notes
When asked to change color via one of these commands, the implementation SHALL select a color,
within the limits of the hardware of the device, which is as close as possible to that requested. The
determination as to the true representations of color is out of the scope of this specification. How
ever, as long as the color data fields of the received command are within the permitted range of this
specification and no error condition applies, the resulting status code SHALL be SUCCESS.
For example the MoveToColorTemperature command: if the target color temperature is not achiev
able by the hardware then the color temperature SHALL be clipped at the physical minimum or
maximum achievable (depending on the direction of the color temperature transition) when the
device reaches that color temperature (which MAY be before the requested transition time).
If a color loop is active (i.e., the ColorLoopActive attribute is equal to 1), it SHALL only be stopped
by sending a specific ColorLoopSet command frame with a request to deactivate the color loop (i.e.,
the color loop SHALL NOT be stopped on receipt of another command which has a 'stop' semantic
such as the EnhancedMoveToHue command with MoveMode==Stop, or the StopMoveStep com
mand). In addition, while a color loop is active, a manufacturer MAY choose to ignore incoming
color commands which affect a change in hue.
3.2.8.2. Note on Change of ColorMode
The first action taken when any one of these commands is received is to change the ColorMode
attribute to the appropriate value for the command (see individual commands). Note that, when
moving from one color mode to another (e.g., CurrentX/CurrentY to CurrentHue/CurrentSatura
tion), the starting color for the command is formed by calculating the values of the new attributes
(in this case CurrentHue, CurrentSaturation) from those of the old attributes (in this case CurrentX
and CurrentY).
When moving from a mode to another mode that has a more restricted color range (e.g., Cur
rentX/CurrentY to CurrentHue/CurrentSaturation, or CurrentHue/CurrentSaturation to ColorTem
peratureMireds) it is possible for the current color value to have no equivalent in the new mode.
The behavior in such cases is manufacturer dependent, and therefore it is recommended to avoid
color mode changes of this kind during use.
3.2.8.3. Use of the OptionsMask and OptionsOverride Fields
The OptionsMask and OptionsOverride Fields SHALL both be present. Default values are provided
to interpret missing fields from legacy devices. A temporary Options bitmap SHALL be created from
the Options attribute, using the OptionsMask and OptionsOverride Fields. Each bit of the temporary
Options bitmap SHALL be determined as follows:
Each bit in the Options attribute SHALL determine the corresponding bit in the temporary Options
bitmap, unless the OptionsMask field is present and has the corresponding bit set to 1, in which
case the corresponding bit in the OptionsOverride field SHALL determine the corresponding bit in
the temporary Options bitmap.
The resulting temporary Options bitmap SHALL then be processed as defined in section Options.
3.2.8.4. MoveToHue Command

_Table parsed from section 'Commands':_

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes a command identified by the ID '0' and named 'Hue'. This command is of the type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint with a maximum value of 254. The conformance rule for this command is 'M', indicating that it is mandatory. This means that the 'Hue' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Color Control Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '1' named 'Direction', which is of the type 'DirectionEnum' and has a constraint labeled 'all'. The conformance rule for this element is marked as 'M', indicating that it is Mandatory. This means that the 'Direction' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, the table row describes a command named "TransitionTime" with an ID of '2'. This command is of type 'uint16', which means it is a 16-bit unsigned integer, and it has a constraint that its maximum value is 65534. The conformance rule for "TransitionTime" is 'M', indicating that this command is mandatory. This means that the "TransitionTime" command must always be implemented and supported in any device or application that uses the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named "OptionsMask" with an ID of '3'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is mandatory. This indicates that the "OptionsMask" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the entry for 'OptionsOverride' is identified by ID '4' and is of the type 'OptionsBitmap'. The constraint for this entry is described elsewhere in the documentation, and it has a default value of '0'. The conformance rule for 'OptionsOverride' is marked as 'M', which means it is a Mandatory element. This indicates that the 'OptionsOverride' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

3.2.8.4.1. Hue Field
This field SHALL indicate the hue to be moved to.
3.2.8.4.2. Direction Field
This field SHALL indicate the movement direction.
3.2.8.4.3. TransitionTime Field
This field SHALL indicate, in 1/10ths of a second, the time that SHALL be taken to move to the new
hue.
3.2.8.4.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.4.5. Effect on Receipt
On receipt of this command, a device SHALL also set the ColorMode attribute to the value 0 and
then SHALL move from its current hue to the value given in the Hue field.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new hue SHALL be equal to the TransitionTime field.
As hue is effectively measured on a circle, the new hue MAY be moved to in either direction. The
direction of hue change is given by the Direction field. If Direction is 'Shortest distance', the direc
tion is taken that involves the shortest path round the circle. This case corresponds to expected nor
mal usage. If Direction is 'Longest distance', the direction is taken that involves the longest path
round the circle. This case can be used for 'rainbow effects'. In both cases, if both distances are the
same, the Up direction SHALL be taken.
3.2.8.5. MoveHue Command

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '0' named 'MoveMode', which is of the type 'MoveModeEnum' and applies to all constraints. The conformance rule for 'MoveMode' is marked as 'M', indicating that this element is mandatory. This means that the 'MoveMode' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '1' named 'Rate', which is of type 'uint8' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Rate' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table entry for 'OptionsMask' with ID '2' is defined as an 'OptionsBitmap' type. The 'Constraint' is described elsewhere in the documentation, and its default value is '0'. The 'Conformance' for this entry is marked as 'M', which means that the 'OptionsMask' command is mandatory. This indicates that it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command named "OptionsOverride" within the Color Control Cluster, specifically under the Commands section. This command is identified by the ID '3' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc', and it has a default value of '0'. The conformance rule for "OptionsOverride" is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

3.2.8.5.1. MoveMode Field
This field SHALL indicate the mode of movement.
3.2.8.5.2. Rate Field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the
device’s hue of one unit.
3.2.8.5.3. OptionsMask and OptionsOverride field
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.5.4. Effect on Receipt
On receipt of this command,
• If the MoveMode field is set to 1 (Up) or 3 (Down):
◦ If the Rate field has a value of zero, the command has no effect and a response SHALL be
returned with the status code set to INVALID_COMMAND.
◦ Otherwise, a device SHALL set the ColorMode attribute to the value 0 (CurrentHueAndCur
rentSaturation) and SHALL then move from its current hue in an up or down direction in a
continuous fashion, as detailed in the table.
• If the MoveMode field is set to 0 (Stop), the Rate field SHALL be completely ignored.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes the 'MoveMode' command with the value 'Stop'. The action specified upon receipt of this command is that if the device is currently moving, it must stop; otherwise, the command is accepted but has no effect. This command is specifically intended to halt any ongoing transitions of hue and/or saturation. The conformance rule for this command is not explicitly provided in the table row data, but based on the context and typical usage in the Matter specification, it is likely considered mandatory (M) for devices that support the Color Control Cluster, ensuring that they can appropriately respond to a 'Stop' command by ceasing any active color transitions.

* The table row entry pertains to the "MoveMode" command within the Color Control Cluster, specifically focusing on the "Up" mode. This command's action upon receipt is to increase the device's hue at a specified rate. If the hue reaches the device's maximum allowable value, it will wrap around and continue from the minimum allowable value. The conformance rule for this command is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, if it were to be described, it would specify whether the command is mandatory, optional, provisional, deprecated, or disallowed, potentially with conditions based on supported features. Since the conformance rule is missing, it is assumed that further documentation would clarify its requirement status within the specification.

* The table row entry pertains to the "MoveMode" command within the Color Control Cluster, specifically focusing on the "Down" mode. This command instructs a device to decrease its hue at a specified rate. If the hue reaches the device's minimum allowed value, it should wrap around and continue decreasing from the maximum allowed value. The conformance rule for this command is not explicitly provided in the data, but based on the context, it would typically involve determining whether the command is mandatory, optional, or subject to specific conditions based on the device's features or capabilities. If the conformance was specified, it would dictate when and how this command must be implemented by devices supporting the Color Control Cluster, ensuring consistent behavior across different implementations.

the command is accepted but has no effect). This
Decrease the device’s hue at the rate given in the
3.2.8.6. StepHue Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "StepMode" command. This command is identified by the ID '0' and utilizes the type 'StepModeEnum'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the "StepMode" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically under the Commands section. The element is identified by the ID '1' and is named 'StepSize'. It is of type 'uint8', indicating it is an unsigned 8-bit integer, and it applies to all constraints. The conformance rule for 'StepSize' is marked as 'M', which means that this element is mandatory. Therefore, 'StepSize' must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '2' named 'TransitionTime', which is of type 'uint8' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that 'TransitionTime' is a mandatory element. This means that it is always required to be implemented in any device or system that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the entry for 'OptionsMask' with ID '3' is defined as an 'OptionsBitmap' type with a constraint described elsewhere in the documentation. The default value for this element is '0'. The conformance rule for 'OptionsMask' is marked as 'M', which means it is a Mandatory element. This indicates that the 'OptionsMask' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the "OptionsOverride" command within the Color Control Cluster, specifically under the Commands section. This command is identified by the ID '4' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc', and it has a default value of '0'. The conformance rule for "OptionsOverride" is marked as 'M', meaning that this command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditional dependencies or exceptions.

3.2.8.6.1. StepMode Field
This field SHALL indicate the mode of the step to be performed.
3.2.8.6.2. StepSize Field
This field SHALL indicate the change to be added to (or subtracted from) the current value of the
device’s hue.
3.2.8.6.3. TransitionTime Field
This field SHALL indicate, in 1/10ths of a second, the time that SHALL be taken to perform the step.
A step is a change in the device’s hue of Step size units.
Here the TransitionTime data field is of data type uint8, where uint16 is more com
NOTE
mon for TransitionTime data fields in other clusters / commands.
3.2.8.6.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.6.5. Effect on Receipt
On receipt of this command, if the StepSize field has a value of zero, the command has no effect and
a response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL set the ColorMode attribute to the value 0 (CurrentHueAndCurrentSatu
ration) and SHALL then move from its current hue in an up or down direction by one step, as
detailed in the table.

_Table parsed from section 'Commands':_

* The table row entry pertains to the "StepMode" command within the Color Control Cluster, specifically under the Commands section. The command is labeled as 'Up', and its action upon receipt is to increase the device's hue by one step continuously. If the hue value reaches its maximum, it wraps around to the minimum allowed value and continues from there. The conformance rule for this command is not explicitly provided in the data, but based on the context and typical usage in the Matter specification, it would likely be a mandatory feature for devices supporting the Color Control Cluster, ensuring consistent behavior across compliant devices. This means that any device implementing this cluster must support this command to maintain interoperability and expected functionality within the Matter ecosystem.

* The table row entry pertains to the "StepMode" command within the Color Control Cluster, specifically focusing on the "Down" action. This command is designed to decrease the device's hue by one step continuously. If the hue value reaches its minimum, it wraps around to the maximum allowed value and continues decreasing. The conformance rule for this command is not explicitly provided in the data you shared, but if we were to interpret a typical conformance expression, it might specify conditions under which this command is mandatory, optional, or otherwise. For instance, if the conformance were "M," it would mean the command is always required. If it were "O," it would be optional with no dependencies. Without a specific conformance string, we can only describe the command's intended function and its behavior upon receipt.

3.2.8.7. MoveToSaturation Command

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes a command with the ID '0' named 'Saturation'. This command is of the type 'uint8', which means it is an 8-bit unsigned integer, and it has a constraint that limits its maximum value to 254. The conformance rule for this command is 'M', indicating that the 'Saturation' command is mandatory. This means it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes an element with the ID '1' named 'TransitionTime'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value is 65534. The conformance rule for 'TransitionTime' is marked as 'M', which stands for Mandatory. This means that the 'TransitionTime' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsMask" command. This command is identified by the ID '2' and is of the type 'OptionsBitmap'. The 'Constraint' for this command is marked as 'desc', indicating that the constraints are described elsewhere in the documentation. The default value for this command is '0'. The 'Conformance' field is marked as 'M', which means that the "OptionsMask" command is mandatory. This implies that the command must always be implemented and supported in any device or application that uses the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap" and has a constraint described elsewhere in the documentation, with a default value of '0'. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.7.1. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.7.2. Effect on Receipt
On receipt of this command, a device SHALL set the ColorMode attribute to the value 0 (Curren
tHueAndCurrentSaturation) and SHALL then move from its current saturation to the value given in
the Saturation field.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new saturation SHALL be equal to the TransitionTime field, in 1/10ths of a second.
3.2.8.8. MoveSaturation Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "MoveMode" command. This command is identified by the ID '0' and is of the type 'MoveModeEnum', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "MoveMode" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically identified by the ID '1' and named 'Rate'. This command is of type 'uint8', which indicates it uses an 8-bit unsigned integer for its data representation. The 'Constraint' field marked as 'all' suggests that there are no specific limitations or conditions on the usage of this command across different implementations. The 'Conformance' field is marked with 'M', which means that the 'Rate' command is mandatory. This implies that any implementation of the Color Control Cluster must include this command as a required element, with no exceptions or conditions altering its necessity.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsMask" command. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a mandatory element. This implies that the "OptionsMask" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap" and has a constraint described elsewhere in the documentation, with a default value of 0. The conformance rule for this command is marked as "M," which means it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditional dependencies or exceptions.

3.2.8.8.1. MoveMode Field
This field SHALL indicate the mode of movement, as described in the MoveHue command.
3.2.8.8.2. Rate Field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the
device’s saturation of one unit.
3.2.8.8.3. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.8.4. Effect on Receipt
On receipt of this command,
• If the MoveMode field is set to 1 (Up) or 3 (Down)
◦ If the Rate field has a value of zero, the command has no effect and a response SHALL be
returned with the status code set to INVALID_COMMAND.
◦ Otherwise, a device SHALL set the ColorMode attribute to the value 0 (CurrentHueAndCur
rentSaturation) and SHALL then move from its current saturation in an up or down direc
tion in a continuous fashion, as detailed in the table.
• If the MoveMode field is set to 0 (Stop), the Rate field SHALL be completely ignored.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes the 'MoveMode' command with the value 'Stop'. The action specified upon receipt of this command is that if a device is currently moving (i.e., undergoing a hue and/or saturation transition), it must stop; if not moving, the command is accepted but has no effect. The conformance rule for this command is not explicitly provided in the table row data, but based on the context, it likely follows a mandatory implementation for devices supporting the Color Control Cluster. This means that any device implementing this cluster must support the 'MoveMode: Stop' command to ensure proper functionality in stopping ongoing transitions.

* The table row entry for the Color Control Cluster under the Commands section describes the 'MoveMode' command with the value 'Up'. This command's action on receipt is to increase the device's saturation at the specified rate in the Rate field, stopping when the maximum saturation allowed by the device is reached. The conformance rule for this command is not explicitly provided in the data snippet, but if we were to interpret a typical conformance expression for such a command, it might indicate whether the command is mandatory, optional, or conditional based on certain features or conditions. For example, if the conformance were `M`, it would mean the command is always required. If it were `O`, it would be optional with no dependencies. If a conditional expression like `[AB]` were present, it would mean the command is optional if feature `AB` is supported. Without the specific conformance string, we can only describe the command's intended action and potential conformance scenarios based on typical usage in the

* The table row entry pertains to the "MoveMode" command within the Color Control Cluster, specifically focusing on the "Down" mode. This command instructs a device to decrease its saturation at a specified rate, as indicated in the Rate field. The action will continue until the saturation reaches the device's minimum allowable level, at which point it will stop. The conformance rule for this command is not explicitly provided in the data snippet, but based on the context, it would typically be interpreted using the Matter Conformance Interpretation Guide. If a conformance rule were provided, it would specify whether the command is mandatory, optional, provisional, deprecated, or disallowed, and under what conditions these statuses apply, using logical expressions and conditionality as outlined in the guide.

3.2.8.9. StepSaturation Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "StepMode" command. This command is identified by the ID '0' and is of the type 'StepModeEnum', with a constraint applicable to 'all', indicating it applies universally within the context of its use. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "StepMode" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '1', named 'StepSize', which is of type 'uint8' and has a constraint labeled as 'all'. The conformance rule for this element is 'M', indicating that the 'StepSize' command is mandatory. This means that the 'StepSize' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '2', named 'TransitionTime', which is of type 'uint8' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that 'TransitionTime' is a Mandatory element. This means it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '3' named 'OptionsMask'. This element is of the type 'OptionsBitmap' and has a default value of '0'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' field is marked as 'M', which means that the 'OptionsMask' element is mandatory. This implies that it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically named "OptionsOverride," which is identified by the ID '4' and is of the type 'OptionsBitmap.' The constraint for this command is described elsewhere in the documentation, as indicated by 'desc,' and it has a default value of '0.' The conformance rule for this command is marked as 'M,' which means it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

3.2.8.9.1. StepMode Field
This field SHALL indicate the mode of the step to be performed, as described in the StepHue com
mand.
3.2.8.9.2. StepSize Field
This field SHALL indicate the change to be added to (or subtracted from) the current value of the
device’s saturation.
3.2.8.9.3. TransitionTime Field
This field SHALL indicate, in 1/10ths of a second, the time that SHALL be taken to perform the step.
A step is a change in the device’s saturation of Step size units.
Here the TransitionTime data field is of data type uint8, where uint16 is more com
NOTE
mon for TransitionTime data fields in other clusters / commands.
3.2.8.9.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.9.5. Effect on Receipt
On receipt of this command, if the StepSize field has a value of zero, the command has no effect and
a response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL set the ColorMode attribute to the value 0 (CurrentHueAndCurrentSatu
ration) and SHALL then move from its current saturation in an up or down direction by one step.

_Table parsed from section 'Commands':_

* The table row entry for the Color Control Cluster under the Commands section describes the 'StepMode' command with the action 'Up'. This command is designed to increase the device's saturation by one step in a continuous manner. However, if the saturation is already at its maximum value, the command will have no effect. The conformance rule for this entry is not explicitly provided in the data, but if we were to interpret it using the Matter Conformance Interpretation Guide, we would need to know the specific conformance string to determine whether this command is mandatory, optional, or subject to any conditions. Without the conformance string, we can only describe the command's intended function and its behavior when executed.

* The table row entry pertains to the "StepMode" command within the Color Control Cluster, specifically focusing on the action "Down." When this command is received, the device is instructed to decrease its saturation by one step continuously. However, if the saturation is already at its minimum value, the command will have no effect. The conformance rule for this entry is not explicitly provided in the data you shared, but if we were to interpret a typical conformance scenario, it might involve conditions under which this command is mandatory, optional, or otherwise. For instance, if the conformance were "M," it would mean that the "StepMode" command with the "Down" action is always required to be implemented. If it were "O," the implementation would be optional, with no dependencies. Without a specific conformance string, we can only describe the typical behavior expected from this command.

Increase the device’s saturation by one step, in a
Decrease the device’s saturation by one step, in a
3.2.8.10. MoveToHueAndSaturation Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "Hue" command. This command is identified by the ID '0' and uses a data type of 'uint8', with a constraint that its value can be a maximum of 254. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Hue" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, there is an entry for a command named "Saturation" with an ID of '1'. This command is of type 'uint8', meaning it is an 8-bit unsigned integer, and it has a constraint that its maximum value is 254. The conformance rule for this command is 'M', which stands for Mandatory. This means that the Saturation command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "TransitionTime" command. This command is identified by the ID '2' and is of the type 'uint16', with a constraint that its maximum value can be 65534. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "TransitionTime" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically identified by the ID '3' and named 'OptionsMask'. This command is of the type 'OptionsBitmap', which suggests it involves a bitmap of options that can be set or cleared. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The default value for this command is '0', meaning that, unless specified otherwise, the options are initially unset. The conformance rule for 'OptionsMask' is marked as 'M', which stands for Mandatory. This means that the 'OptionsMask' command is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

* The table row entry pertains to the "OptionsOverride" command within the Color Control Cluster, specifically under the Commands section. The command is identified by the ID '4' and is of the type 'OptionsBitmap', with its constraints described elsewhere in the documentation. The default value for this command is '0'. The conformance rule for "OptionsOverride" is marked as 'M', meaning it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.10.1. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.10.2. Effect on Receipt
On receipt of this command, a device SHALL set the ColorMode attribute to the value 0 (Curren
tHueAndCurrentSaturation) and SHALL then move from its current hue and saturation to the val
ues given in the Hue and Saturation fields.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new color SHALL be equal to the TransitionTime field, in 1/10ths of a second.
The path through color space taken during the transition is not specified, but it is recommended
that the shortest path is taken through color space, i.e., movement is 'in a straight line' across the
CIE xyY Color Space.
3.2.8.11. MoveToColor Command

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '0' named 'ColorX'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value cannot exceed 65279. The conformance rule for 'ColorX' is denoted by 'M', which stands for Mandatory. This means that the 'ColorX' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '1', named 'ColorY'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value is 65279. The conformance rule for 'ColorY' is 'M', which stands for Mandatory. This means that the 'ColorY' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint16', which means it is a 16-bit unsigned integer, and it has a constraint that its maximum value can be 65534. The conformance rule for 'TransitionTime' is marked as 'M', indicating that this element is mandatory. This means that the 'TransitionTime' command must always be implemented and supported in any device or application that uses the Color Control Cluster, without any conditions or exceptions.

* The table row describes an entry within the Color Control Cluster, specifically under the Commands section. The entry is for an element named "OptionsMask," which is of the type "OptionsBitmap." The constraint for this element is described elsewhere in the documentation, as indicated by "desc," and its default value is set to "0." The conformance rule for "OptionsMask" is marked as "M," meaning that this element is mandatory. It is always required to be implemented in any device or system that supports the Color Control Cluster, with no conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the entry for 'OptionsOverride' with ID '4' is defined as a command of type 'OptionsBitmap'. The 'Constraint' is described elsewhere in the documentation, and its default value is '0'. The 'Conformance' for this command is marked as 'M', which means it is mandatory. This indicates that the 'OptionsOverride' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.11.1. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.11.2. Effect on Receipt
On receipt of this command, a device SHALL set the value of the ColorMode attribute, where imple
mented, to 1 (CurrentXAndCurrentY), and SHALL then move from its current color to the color
given in the ColorX and ColorY fields.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new color SHALL be equal to the TransitionTime field, in 1/10ths of a second.
The path through color space taken during the transition is not specified, but it is recommended
that the shortest path is taken through color space, i.e., movement is 'in a straight line' across the
CIE xyY Color Space.
3.2.8.12. MoveColor Command

_Table parsed from section 'Commands':_

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '0' named 'RateX', which is of type 'int16' and has a constraint labeled as 'all'. The conformance rule for 'RateX' is marked as 'M', indicating that this element is mandatory. This means that 'RateX' is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command named "RateY" within the Color Control Cluster, identified by ID '1'. This command is of type 'int16' and applies universally, as indicated by the 'Constraint' being 'all'. The 'Conformance' field is marked as 'M', which means that the "RateY" command is mandatory. This implies that any implementation of the Color Control Cluster must include the "RateY" command without exception. The mandatory status ensures that this command is always available and supported in all compliant devices or systems utilizing this cluster.

* In the context of the Color Control Cluster, specifically within the Commands section, the table entry for 'OptionsMask' is identified by ID '2' and is of the type 'OptionsBitmap'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc', and it has a default value of '0'. The conformance rule for 'OptionsMask' is marked as 'M', which means that this element is mandatory. Therefore, it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is identified by the ID '3' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc', and its default value is '0'. The conformance rule for this command is 'M', which means that the "OptionsOverride" command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.12.1. RateX Field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the
device’s CurrentX attribute of one unit.
3.2.8.12.2. RateY Field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the
device’s CurrentY attribute of one unit.
3.2.8.12.3. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.12.4. Effect on Receipt
On receipt of this command, if both the RateX and RateY fields contain a value of zero, no move
ment SHALL be carried out, and the command execution SHALL have no effect other than stopping
the operation of any previously received command of this cluster. While this command (when used
with both the RateX and RateY fields set to zero) can be used to stop any operation of this cluster, it
is recommended to instead use the StopMoveStep command to achieve this goal.
Otherwise, a device SHALL set the value of the ColorMode attribute, where implemented, to 1 (Cur
rentXAndCurrentY), and SHALL then move from its current color in a continuous fashion according
to the rates specified. This movement SHALL continue until the target color for the next step cannot
be implemented on this device.
3.2.8.13. StepColor Command

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "StepX" command. This command has an identifier of '0' and is of type 'int16', with a constraint applicable to 'all', meaning it is universally applicable within its context. The conformance rule for "StepX" is denoted by 'M', which stands for Mandatory. This indicates that the "StepX" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes a command named "StepY" with an ID of '1'. This command is of type 'int16' and applies to all constraints. The conformance rule for "StepY" is marked as 'M', which means it is mandatory. This indicates that the "StepY" command is a required element in the Color Control Cluster and must be implemented in all devices that support this cluster, without any exceptions or conditions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint16', which means it is a 16-bit unsigned integer, and it has a constraint that its maximum value can be 65534. The conformance rule for 'TransitionTime' is 'M', indicating that this element is mandatory. This means that the 'TransitionTime' command must always be implemented and supported in any device or application that uses the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named "OptionsMask" with an ID of '3'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a mandatory element. This implies that the "OptionsMask" command must always be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '4' named 'OptionsOverride'. This element is of the type 'OptionsBitmap', with constraints described elsewhere in the documentation, and it has a default value of '0'. The conformance rule for 'OptionsOverride' is marked as 'M', which means this element is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.13.1. StepX and StepY Fields
These fields SHALL indicate the change to be added to the device’s CurrentX attribute and CurrentY
attribute respectively.
3.2.8.13.2. TransitionTime Field
The field SHALL indicate, in 1/10ths of a second, the time that SHALL be taken to perform the color
change.
3.2.8.13.3. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.13.4. Effect on Receipt
On receipt of this command, if both the StepX and StepY fields contain a value of zero, the com
mand has no effect and a response SHALL be returned with the status code set to INVALID_COM
MAND.
Otherwise, a device SHALL set the value of the ColorMode attribute, where implemented, to 1 (Cur
rentXAndCurrentY), and SHALL then move from its current color by the color step indicated.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new color SHALL be equal to the TransitionTime field, in 1/10ths of a second.
The path through color space taken during the transition is not specified, but it is recommended
that the shortest path is taken through color space, i.e., movement is 'in a straight line' across the
CIE xyY Color Space.
Note also that if the required step is larger than can be represented by signed 16-bit integers then
more than one step command SHOULD be issued.
3.2.8.14. MoveToColorTemperature Command

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the entry for 'ColorTemperatureMireds' is identified by the ID '0' and is of type 'uint16', with a constraint that its maximum value is 65279. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'ColorTemperatureMireds' command is always required to be implemented in any device or system that supports the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes an element with the ID '1' named 'TransitionTime'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value can be 65534. The conformance rule for 'TransitionTime' is marked as 'M', which stands for Mandatory. This indicates that the 'TransitionTime' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the 'OptionsMask' command. This command is of the type 'OptionsBitmap' and has a default value of '0'. The 'Constraint' field is marked as 'desc', indicating that the constraints for this command are described in detail elsewhere in the documentation. The 'Conformance' field is marked with 'M', which means that the 'OptionsMask' command is mandatory. This implies that any implementation of the Color Control Cluster must include this command, as it is always required according to the Matter specification.

* In the Color Control Cluster, within the Commands section, the entry for 'OptionsOverride' is identified by the ID '3' and is of the type 'OptionsBitmap'. The constraint for this entry is described elsewhere in the documentation, as indicated by 'desc', and it has a default value of '0'. The conformance rule for 'OptionsOverride' is marked as 'M', which means that this element is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.14.1. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.14.2. Effect on Receipt
On receipt of this command, a device SHALL set the value of the ColorMode attribute, where imple
mented, to 2 (ColorTemperatureMireds), and SHALL then move from its current color to the color
given by the ColorTemperatureMired field.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new color SHALL be equal to the TransitionTime field, in 1/10ths of a second.
By definition of this color mode, the path through color space taken during the transition is along
the 'Black Body Line'.
If the ColorTemperatureMireds field is less than the value of the ColorTempPhysicalMinMireds
attribute, the value of the ColorTempPhysicalMinMireds attribute SHALL be used as the final target
for the ColorTemperatureMireds attribute.
If the ColorTemperatureMireds field is greater than the value of the ColorTempPhysicalMaxMireds
attribute, the value of the ColorTempPhysicalMaxMireds attribute SHALL be used as the final target
for the ColorTemperatureMireds attribute.
3.2.8.15. EnhancedMoveToHue Command
This command allows the light to be moved in a smooth continuous transition from their current
hue to a target hue.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the 'EnhancedHue' command. This command is identified by the ID '0' and is of type 'uint16', which indicates it uses a 16-bit unsigned integer for its data. The constraint 'all' suggests that this command applies universally within the context of the cluster. The conformance rule for 'EnhancedHue' is marked as 'M', meaning it is mandatory. This indicates that the 'EnhancedHue' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the entry with ID '1' is named 'Direction' and is of the type 'DirectionEnum'. The 'Constraint' for this entry is 'all', indicating that it applies universally within its context. The 'Conformance' for this entry is marked as 'M', which means that the 'Direction' command is mandatory. This implies that the 'Direction' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "TransitionTime" command. This command has an ID of '2' and is of type 'uint16', with a constraint that its maximum value is 65534. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "TransitionTime" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named "OptionsMask" with an ID of '3'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a Mandatory element. This implies that the "OptionsMask" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for this command is marked as 'M', which means it is mandatory. This implies that the "OptionsOverride" command must always be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.15.1. EnhancedHue Field
This field SHALL indicate the target extended hue for the light.
3.2.8.15.2. Direction Field
This field SHALL indicate the movement direction.
3.2.8.15.3. TransitionTime Field
This field SHALL indicate the transition time, as described in the MoveToHue command.
3.2.8.15.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.15.5. Effect on Receipt
On receipt of this command, a device SHALL set the ColorMode attribute to 0 (CurrentHueAndCur
rentSaturation) and set the EnhancedColorMode attribute to the value 3 (EnhancedCurrentHueAnd
CurrentSaturation). The device SHALL then move from its current enhanced hue to the value given
in the EnhancedHue field.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new enhanced hue SHALL be equal to the TransitionTime field.
3.2.8.16. EnhancedMoveHue Command
This command allows the light to start a continuous transition starting from their current hue.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes a command with the ID '0' named 'MoveMode'. This command is of the type 'MoveModeEnum', and its constraints are detailed elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'MoveMode' is marked as 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "Rate" command, which is identified by the ID '1' and is of type 'uint16'. The constraint 'all' indicates that this command applies universally across all relevant contexts within the cluster. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Rate" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsMask" command. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is mandatory. This implies that the "OptionsMask" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap," which indicates it involves a bitmap of options. The constraint for this command is described elsewhere in the documentation, as indicated by "desc." The default value for this command is set to '0'. The conformance rule for "OptionsOverride" is marked as 'M', meaning it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

3.2.8.16.1. MoveMode Field
This field SHALL indicate the mode of movement, as described in the MoveHue command.
3.2.8.16.2. Rate field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the
extended hue of a device by one unit.
3.2.8.16.3. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.16.4. Effect on receipt
On receipt of this command,
• If the MoveMode field is set to 1 (Up) or 3 (Down)
◦ If the Rate field has a value of zero, the command has no effect and a response SHALL be
returned with the status code set to INVALID_COMMAND.
◦ Otherwise, a device SHALL set the ColorMode attribute to 0 (CurrentHueAndCurrentSatura
tion) and set the EnhancedColorMode attribute to the value 3 (EnhancedCurrentHueAndCur
rentSaturation). The device SHALL then move from its current enhanced hue in an up or
down direction in a continuous fashion, as detailed in the table.
• If the MoveMode field is set to 0 (Stop), the Rate field SHALL be completely ignored.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the table row describes the 'MoveMode' command with the value 'Stop'. The action specified upon receipt of this command is to halt any ongoing hue and/or saturation transition if such a transition is currently in progress; otherwise, the command is accepted but has no effect. The conformance rule for this command is not explicitly stated in the provided data, but based on the context and typical usage in Matter specifications, it can be inferred that the command is likely mandatory (M) for devices implementing the Color Control Cluster. This means that any device supporting this cluster must implement the 'MoveMode: Stop' command to ensure it can properly handle stopping transitions as described.

* In the Color Control Cluster, under the Commands section, the table row describes the 'MoveMode' command with the value 'Up'. This command instructs a device to increase its enhanced hue at a specified rate. If the enhanced hue reaches the device's maximum allowed value, it will wrap around and continue from the minimum allowed value. The conformance rule for this command is not explicitly provided in the data, but based on the context, it is likely a standard command that is either mandatory or optional depending on the specific implementation requirements of the device. Without a specific conformance string, we assume that the command's inclusion depends on the device's support for the Color Control Cluster and its features.

* The table row describes a command within the Color Control Cluster, specifically the 'MoveMode' set to 'Down'. The action associated with this command is to decrease the device's enhanced hue at a specified rate. If the hue reaches the device's minimum allowed value, it should wrap around and continue from the maximum allowed value. The conformance rule for this command is not explicitly provided in the data, but based on the context, it likely involves conditions under which this command is mandatory, optional, or otherwise specified. Without a specific conformance string, we can infer that the command's implementation might depend on the device's capabilities or specific feature support, such as whether it supports enhanced hue control. If a conformance string were provided, it would clarify whether this command is always required, conditionally required, or optional based on certain features or conditions.

the command is accepted but has no effect). This
3.2.8.17. EnhancedStepHue Command
This command allows the light to be moved in a stepped transition from their current hue, resulting
in a linear transition through XY space.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, within the Commands section, the table row describes a command identified by 'ID' 0, named 'StepMode', which is of the type 'StepModeEnum'. The 'Constraint' for this command is marked as 'desc', indicating that the specific constraints or conditions for this command are detailed elsewhere in the documentation. The 'Conformance' for 'StepMode' is marked as 'M', meaning that this command is mandatory. It must always be implemented and supported within the Color Control Cluster, with no conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "StepSize" command. This command has an identifier of '1' and is of type 'uint16', meaning it is a 16-bit unsigned integer. The constraint 'all' indicates that this command applies universally within its context. The conformance rule for "StepSize" is 'M', which stands for Mandatory. This means that the "StepSize" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint specifying a maximum value of 65534. The conformance rule for 'TransitionTime' is marked as 'M', indicating that this element is mandatory. This means that the 'TransitionTime' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Color Control Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes an element named "OptionsMask" with an ID of '3'. This element is of the type "OptionsBitmap" and has a constraint that is described elsewhere in the documentation, with a default value of '0'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a Mandatory element. This indicates that the "OptionsMask" must always be implemented and supported in any device or system that adheres to the Matter specification for the Color Control Cluster. There are no conditions or dependencies affecting its requirement status; it is an essential component of the cluster's functionality.

* The table row describes a command within the Color Control Cluster, specifically named "OptionsOverride" with an ID of '4'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint is marked as 'desc', indicating that the specific constraints are detailed elsewhere in the documentation. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

3.2.8.17.1. StepMode Field
This field SHALL indicate the mode of the step to be performed, as described in the StepHue com
mand.
3.2.8.17.2. StepSize Field
This field SHALL indicate the change to be added to (or subtracted from) the current value of the
device’s enhanced hue.
3.2.8.17.3. TransitionTime Field
The field SHALL indicate, in units of 1/10ths of a second, the time that SHALL be taken to perform
the step. A step is a change to the device’s enhanced hue of a magnitude corresponding to the Step
Size field.
Here TransitionTime data field is of data type uint16, while the TransitionTime data
NOTE
field of the StepHue command is of data type uint8.
3.2.8.17.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.17.5. Effect on Receipt
On receipt of this command, if the StepSize field has a value of zero, the command has no effect and
a response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL set the ColorMode attribute to 0 (CurrentHueAndCurrentSaturation)
and the EnhancedColorMode attribute to the value 3 (EnhancedCurrentHueAndCurrentSaturation).
The device SHALL then move from its current enhanced hue in an up or down direction by one
step, as detailed in the table.

_Table parsed from section 'Commands':_

* The table row entry for the Color Control Cluster under the Commands section describes the 'StepMode' command with the action 'Up'. This command is designed to increase the device's enhanced hue by one step. If the enhanced hue reaches the device's maximum limit, it will wrap around and continue from the minimum allowed value. The conformance rule for this command is not explicitly provided in the data, but based on the context, it would typically be interpreted as a mandatory feature if the device supports enhanced hue control. This means that any device implementing the Color Control Cluster with enhanced hue capabilities must support this command to ensure proper functionality and user experience.

* The table row entry pertains to the "StepMode" command within the Color Control Cluster, specifically focusing on the action "Down." This command, when received, instructs the device to decrease its enhanced hue by one step. If the hue reaches the device's minimum allowed value, it will wrap around and continue from the maximum allowed value. The conformance rule for this command is not explicitly stated in the provided data, but based on the context, it likely follows a standard conformance pattern. If we assume a typical conformance scenario, it might be mandatory (M) for devices supporting the Color Control Cluster, ensuring consistent behavior across compliant devices. However, without a specific conformance string, this is an interpretation based on typical usage within the Matter specification.

3.2.8.18. EnhancedMoveToHueAndSaturation Command
This command allows the light to be moved in a smooth continuous transition from their current
hue to a target hue and from their current saturation to a target saturation.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "EnhancedHue" command. This command has an ID of '0' and is of type 'uint16', which indicates it uses a 16-bit unsigned integer. The 'Constraint' field is marked as 'all', suggesting that this command applies universally within its context. The 'Conformance' field is marked with an 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the "EnhancedHue" command is always required to be implemented in any device or application that supports the Color Control Cluster. There are no conditions or exceptions to this requirement, making it a fundamental part of the cluster's functionality.

* The table row describes a command within the Color Control Cluster, specifically the "Saturation" command. This command has an identifier (ID) of '1' and is of type 'uint8', which means it is an 8-bit unsigned integer. The value of this command is constrained to a maximum of 254. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Saturation" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint16', which means it is a 16-bit unsigned integer, and it has a constraint that its maximum value can be 65534. The conformance rule for 'TransitionTime' is marked as 'M', indicating that this element is mandatory. This means that the 'TransitionTime' command must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named "OptionsMask" with an ID of '3'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', which means it is a Mandatory element. This implies that the "OptionsMask" command must always be implemented and supported in any device or application that uses the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the "OptionsOverride" command within the Color Control Cluster, specifically under the Commands section. The command is identified by the ID '4' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc', and it has a default value of '0'. The conformance rule for this command is marked as 'M', which means that the "OptionsOverride" command is mandatory. This implies that it is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.18.1. EnhancedHue Field
This field SHALL indicate the target extended hue for the light.
3.2.8.18.2. Saturation Field
This field SHALL indicate the saturation, as described in the MoveToHueAndSaturation command.
3.2.8.18.3. TransitionTime Field
This field SHALL indicate the transition time, as described in the MoveToHue command.
3.2.8.18.4. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.18.5. Effect on Receipt
On receipt of this command, a device SHALL set the ColorMode attribute to the value 0 (Curren
tHueAndCurrentSaturation) and set the EnhancedColorMode attribute to the value 3 (Enhanced
CurrentHueAndCurrentSaturation). The device SHALL then move from its current enhanced hue
and saturation to the values given in the EnhancedHue and Saturation fields.
The movement SHALL be continuous, i.e., not a step function, and the time taken to move to the
new color SHALL be equal to the TransitionTime field, in 1/10ths of a second.
The path through color space taken during the transition is not specified, but it is recommended
that the shortest path is taken through color space, i.e., movement is 'in a straight line' across the
CIE xyY Color Space.
3.2.8.19. ColorLoopSet Command
This command allows a color loop to be activated such that the color light cycles through its range
of hues.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "UpdateFlags" command. This command is identified by the ID '0' and is of the type 'UpdateFlagsBitmap', with a constraint labeled as 'all', indicating it applies universally within its context. The conformance rule for this command is 'M', which stands for Mandatory. This means that the "UpdateFlags" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes a command with the ID '1' named 'Action', which is of the type 'ColorLoopActionEnum' and applies to all constraints. The conformance rule for this command is 'M', indicating that it is mandatory. This means that the 'Action' command must always be implemented and supported in any device or application that adheres to the Matter specification for the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "Direction" command, which is of the type "ColorLoopDirectionEnum" and applies to all instances of this cluster. The conformance rule for this command is marked as "M," indicating that it is mandatory. This means that the "Direction" command must be implemented in all devices or applications that support the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically identified by the ID '3' and named 'Time'. This command is of type 'uint16', indicating it uses a 16-bit unsigned integer for its data. The constraint 'all' suggests that this command applies universally within its context. The conformance rule 'M' signifies that this command is mandatory, meaning it is always required to be implemented in any device or application that supports the Color Control Cluster. There are no conditions or dependencies affecting its requirement status; it must be included in all relevant implementations.

* The table row describes a command within the Color Control Cluster, specifically the "StartHue" command, which is identified by the ID '4' and uses a data type of 'uint16'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Conformance' field is marked as 'M', which means that the "StartHue" command is mandatory. This implies that any implementation of the Color Control Cluster must include this command without exception, as it is a required element of the specification.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsMask" command. This command is identified by the ID '5' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The default value for this command is '0'. The conformance rule for "OptionsMask" is 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is identified by the ID '6' and is of the type 'OptionsBitmap', with constraints described elsewhere in the documentation. The default value for this command is '0'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.19.1. UpdateFlags Field
This field SHALL indicate which color loop attributes to update (from the values supplied in the
other fields, see field descriptions below) before the color loop is started.
3.2.8.19.2. Action Field
This field SHALL indicate the action to take for the color loop.
3.2.8.19.3. Direction Field
This field SHALL indicate the direction for the color loop.
3.2.8.19.4. Time Field
This field SHALL indicate the number of seconds over which to perform a full color loop.
3.2.8.19.5. Start Hue Field
This field SHALL indicate the starting hue to use for the color loop.
3.2.8.19.6. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.19.7. Effect on Receipt
On receipt of this command, the device SHALL first update its color loop attributes according to the
value of the UpdateFlags field, as follows.
• If  the  UpdateDirection  sub-field  is  set  to  1,  the  device  SHALL  set  the  ColorLoopDirection
attribute to the value of the Direction field.
• If the UpdateTime sub-field is set to 1, the device SHALL set the ColorLoopTime attribute to the
value of the Time field.
• If the UpdateStartHue sub-field is set to 1, the device SHALL set the ColorLoopStartEnhanced
Hue attribute to the value of the StartHue field.
• If the UpdateAction sub-field of the UpdateFlags field is set to 1, the device SHALL adhere to the
action specified in the Action field, as follows.
◦ If the value of the Action field is set to 0 and the color loop is active, i.e. the ColorLoopActive
attribute is set to 1, the device SHALL de-active the color loop, set the ColorLoopActive
attribute to 0 and set the EnhancedCurrentHue attribute to the value of the ColorLoopStore
dEnhancedHue attribute.
◦ If the value of the Action field is set to 0 and the color loop is inactive, i.e. the Color
LoopActive attribute is set to 0, the device SHALL ignore the action update component of the
command, i.e. the EnhancedCurrentHue attribute SHALL NOT be updated (contrasting with
the case described in the previous bullet).
◦ If the value of the Action field is set to 1, the device SHALL set the ColorLoopStoredEn
hancedHue  attribute  to  the  value  of  the  EnhancedCurrentHue  attribute,  set  the  Color
LoopActive attribute to 1 and activate the color loop, starting from the value of the Color
LoopStartEnhancedHue attribute.
◦ If the value of the Action field is set to 2, the device SHALL set the ColorLoopStoredEn
hancedHue  attribute  to  the  value  of  the  EnhancedCurrentHue  attribute,  set  the  Color
LoopActive  attribute  to  1  and  activate  the  color  loop,  starting  from  the  value  of  the
EnhancedCurrentHue attribute.
If  the  color  loop  is  active,  the  device  SHALL  cycle  over  the  complete  range  of  values  of  the
EnhancedCurrentHue attribute in the direction of the ColorLoopDirection attribute over the time
specified in the ColorLoopTime attribute. The level of increments/decrements is application spe
cific.
If the color loop is active (and stays active), the device SHALL immediately react on updates of the
ColorLoopDirection and ColorLoopTime attributes.
3.2.8.20. StopMoveStep Command
This command is provided to allow MoveTo and Step commands to be stopped.
NOTE This automatically provides symmetry to the Level Control cluster.
NOTE The StopMoveStep command has no effect on an active color loop.

_Table parsed from section 'Commands':_

* The table row describes an element within the Color Control Cluster, specifically a command named "OptionsMask" with an ID of '0'. This command is of the type "OptionsBitmap" and has a default value of '0'. The constraint for this element is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for "OptionsMask" is marked as 'M', meaning it is mandatory. This indicates that the "OptionsMask" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap" and has constraints that are described elsewhere in the documentation, as indicated by "desc" in the Constraint field. The default value for this command is "0". The Conformance field is marked as "M", which means that the "OptionsOverride" command is mandatory. This implies that any implementation of the Color Control Cluster must include this command, as it is always required according to the Matter specification.

3.2.8.20.1. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.20.2. Effect on Receipt
Upon receipt of this command, any MoveTo, Move or Step command currently in process SHALL be
terminated. The values of the CurrentHue, EnhancedCurrentHue and CurrentSaturation attributes
SHALL be left at their present value upon receipt of the StopMoveStep command, and the Remain
ingTime attribute SHALL be set to zero.
3.2.8.21. MoveColorTemperature Command
This command allows the color temperature of the light to be moved at a specified rate.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "MoveMode" command. This command is identified by the ID '0' and utilizes the 'MoveModeEnum' type, with a constraint of 'all', indicating it applies universally within its context. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "MoveMode" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically identified as 'Rate' with an ID of '1'. This command is of the type 'uint16', meaning it is a 16-bit unsigned integer, and it applies universally across all contexts as indicated by the 'Constraint' being 'all'. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'Rate' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named 'ColorTemperatureMinimumMireds'. This command has an ID of '2' and is of type 'uint16', with a constraint that its maximum value cannot exceed 65279. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'ColorTemperatureMinimumMireds' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes an element within the Color Control Cluster, specifically a command named "ColorTemperatureMaximumMireds" with an ID of '3'. This command is of type 'uint16' and is constrained to a maximum value of 65279. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the "ColorTemperatureMaximumMireds" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the table row describes an element with the ID '4' named 'OptionsMask'. This element is of the type 'OptionsBitmap' and has a default value of '0'. The 'Constraint' is marked as 'desc', indicating that the constraints are detailed elsewhere in the documentation. The 'Conformance' for 'OptionsMask' is marked as 'M', which means it is a Mandatory element. This implies that the 'OptionsMask' must always be implemented and supported in any device or application that utilizes the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the "OptionsOverride" command. This command is of the type "OptionsBitmap" and has a constraint that is described elsewhere in the documentation, with a default value of '0'. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "OptionsOverride" command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.21.1. MoveMode Field
This field SHALL indicate the mode of movement, as described in the MoveHue command.
3.2.8.21.2. Rate Field
This field SHALL indicate the rate of movement in steps per second. A step is a change in the color
temperature of a device by one unit.
3.2.8.21.3. ColorTemperatureMinimumMireds Field
This field SHALL indicate a lower bound on the ColorTemperatureMireds attribute (≡ an upper
bound on the color temperature in kelvins) for the current move operation such that:
<= <=
ColorTempPhysicalMinMireds    ColorTemperatureMinimumMireds  field    ColorTempera
tureMireds
As such if the move operation takes the ColorTemperatureMireds attribute towards the value of the
ColorTemperatureMinimumMireds field it SHALL be clipped so that the above invariant is satisfied.
If the ColorTemperatureMinimumMireds field is set to 0, ColorTempPhysicalMinMireds SHALL be
used as the lower bound for the ColorTemperatureMireds attribute.
3.2.8.21.4. ColorTemperatureMaximumMireds Field
This field SHALL indicate an upper bound on the ColorTemperatureMireds attribute (≡ a lower
bound on the color temperature in kelvins) for the current move operation such that:
<= <=
ColorTemperatureMireds    ColorTemperatureMaximumMireds  field    ColorTempPhysical
MaxMireds
As such if the move operation takes the ColorTemperatureMireds attribute towards the value of the
ColorTemperatureMaximumMireds field it SHALL be clipped so that the above invariant is satis
fied.  If  the  ColorTemperatureMaximumMireds  field  is  set  to  0,  ColorTempPhysicalMaxMireds
SHALL be used as the upper bound for the ColorTemperatureMireds attribute.
3.2.8.21.5. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.21.6. Effect on Receipt
On receipt of this command,
• If the MoveMode field is set to 1 (Up) or 3 (Down)
◦ If the Rate field has a value of zero, the command has no effect and a response SHALL be
returned with the status code set to INVALID_COMMAND.
◦ Otherwise, a device SHALL set both the ColorMode and EnhancedColorMode attributes to 2
(ColorTemperatureMireds) The device SHALL then move from its current color temperature
in an up or down direction in a continuous fashion, as detailed in the table.
• If the MoveMode field is set to 0 (Stop), the Rate field SHALL be completely ignored.

_Table parsed from section 'Commands':_

* In the context of the Color Control Cluster, specifically within the Commands section, the table row describes the 'MoveMode' command with the value 'Stop'. The action to be taken upon receipt of this command is to halt any ongoing operation if movement is currently occurring; otherwise, the command is accepted but has no effect. The conformance rule for this command is not explicitly provided in the data, but based on the typical structure of such tables, it would likely be mandatory (M) or optional (O) depending on the specific implementation requirements of the device. If it were mandatory, it would mean that all devices supporting the Color Control Cluster must implement this command. If optional, devices can choose whether to implement it without any dependencies. The absence of a specific conformance expression suggests that the command's implementation is straightforward and does not depend on complex conditions or feature support.

command (i.e., the command is accepted but has

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the 'MoveMode' command with the value 'Up' is designed to increase the ColorTemperatureMireds attribute, which effectively decreases the color temperature in kelvins, at a specified rate. This operation will continue until the ColorTemperatureMireds attribute reaches the device's maximum limit, as defined by either the ColorTemperatureMaximumMireds field or the ColorTempPhysicalMaxMireds attribute, at which point the operation must stop. The conformance rule for this command is not explicitly provided in the table row, but if it were, it would dictate when this command is required, optional, or otherwise, based on the conditions and logical expressions outlined in the Matter Conformance Interpretation Guide.

* In the Color Control Cluster, under the Commands section, the table row describes the 'MoveMode' command with a value of 'Down'. This command is designed to decrease the ColorTemperatureMireds attribute, which effectively increases the color temperature in kelvins, at a specified rate. The operation will automatically stop if the ColorTemperatureMireds attribute reaches the device's minimum allowable value, as defined by either the ColorTemperatureMinimumMireds field or the ColorTempPhysicalMinMireds attribute. The conformance rule for this command is not explicitly provided in the table row data, but based on the context and typical usage, it would likely be mandatory (M) for devices supporting color temperature adjustments, ensuring that all compliant devices can perform this essential function.

3.2.8.22. StepColorTemperature Command
This command allows the color temperature of the light to be stepped with a specified step size.

_Table parsed from section 'Commands':_

* The table row describes a command within the Color Control Cluster, specifically the "StepMode" command, which is identified by the ID '0' and is of the type 'StepModeEnum'. The 'Constraint' field indicates that this command applies universally ('all'). The 'Conformance' field is marked as 'M', which means that the "StepMode" command is mandatory. This implies that any implementation of the Color Control Cluster must include the "StepMode" command, as it is always required according to the Matter specification.

* The table row entry pertains to the "StepSize" command within the Color Control Cluster, specifically under the Commands section. The "StepSize" command is identified by the ID '1' and is of the type 'uint16', which indicates it is a 16-bit unsigned integer. The constraint 'all' suggests that this command applies universally within its context. The conformance rule 'M' signifies that the "StepSize" command is mandatory, meaning it is always required to be implemented in any device or application that supports the Color Control Cluster. There are no conditions or exceptions to this requirement, making it an essential component of the cluster's functionality.

* In the Color Control Cluster, within the Commands section, the table row describes an element with the ID '2' named 'TransitionTime'. This element is of type 'uint16', meaning it is a 16-bit unsigned integer, and it has a constraint that its maximum value can be 65534. The conformance rule for 'TransitionTime' is 'M', which stands for Mandatory. This means that the 'TransitionTime' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row entry pertains to the Color Control Cluster within the Commands section and describes an element named 'ColorTemperatureMinimumMireds'. This element is identified by the ID '3' and is of type 'uint16', with a constraint that its maximum value is 65279. The conformance rule for this element is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'ColorTemperatureMinimumMireds' element is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row entry for the Color Control Cluster under the Commands section describes the 'ColorTemperatureMaximumMireds' command, which has an ID of '4' and is of type 'uint16'. The command has a constraint indicating that its maximum value is 65279. The conformance rule for this command is marked as 'M', which stands for Mandatory. This means that the 'ColorTemperatureMaximumMireds' command is always required to be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

* The table row describes a command within the Color Control Cluster, specifically the 'OptionsMask' command. This command is identified by the ID '5' and is of the type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The default value for this command is '0'. The conformance rule for 'OptionsMask' is 'M', which means that this command is mandatory. It is always required to be implemented in any device or application that supports the Color Control Cluster, with no conditions or exceptions.

* In the Color Control Cluster, under the Commands section, the entry for 'OptionsOverride' with ID '6' is defined as a command of type 'OptionsBitmap'. The constraint for this command is described elsewhere in the documentation, and its default value is '0'. The conformance rule for 'OptionsOverride' is marked as 'M', which means it is a mandatory element. This indicates that the 'OptionsOverride' command must always be implemented in any device or application that supports the Color Control Cluster, without any conditions or exceptions.

3.2.8.22.1. StepMode Field
This field SHALL indicate the mode of the step to be performed, as described in the StepHue com
mand.
3.2.8.22.2. StepSize Field
This field SHALL indicate the change to be added to (or subtracted from) the current value of the
device’s color temperature.
3.2.8.22.3. TransitionTime Field
This field SHALL indicate, in units of 1/10ths of a second, the time that SHALL be taken to perform
the step. A step is a change to the device’s color temperature of a magnitude corresponding to the
StepSize field.
3.2.8.22.4. ColorTemperatureMinimumMireds Field
This field SHALL indicate a lower bound on the ColorTemperatureMireds attribute (≡ an upper
bound on the color temperature in kelvins) for the current step operation such that:
<= <=
ColorTempPhysicalMinMireds    ColorTemperatureMinimumMireds  field    ColorTempera
tureMireds
As such if the step operation takes the ColorTemperatureMireds attribute towards the value of the
ColorTemperatureMinimumMireds field it SHALL be clipped so that the above invariant is satisfied.
If the ColorTemperatureMinimumMireds field is set to 0, ColorTempPhysicalMinMireds SHALL be
used as the lower bound for the ColorTemperatureMireds attribute.
3.2.8.22.5. ColorTemperatureMaximumMireds Field
This field SHALL indicate an upper bound on the ColorTemperatureMireds attribute (≡ a lower
bound on the color temperature in kelvins) for the current step operation such that:
ColorTemperatureMireds  ≤  ColorTemperatureMaximumMireds  field  ≤  ColorTempPhysical
MaxMireds
As such if the step operation takes the ColorTemperatureMireds attribute towards the value of the
ColorTemperatureMaximumMireds field it SHALL be clipped so that the above invariant is satis
fied.  If  the  ColorTemperatureMaximumMireds  field  is  set  to  0,  ColorTempPhysicalMaxMireds
SHALL be used as the upper bound for the ColorTemperatureMireds attribute.
3.2.8.22.6. OptionsMask and OptionsOverride Fields
These fields SHALL be processed according to section Use of the OptionsMask and OptionsOverride
Fields.
3.2.8.22.7. Effect on Receipt
On receipt of this command, if the StepSize field has a value of zero, the command has no effect and
a response SHALL be returned with the status code set to INVALID_COMMAND.
Otherwise, a device SHALL set both the ColorMode and EnhancedColorMode attributes to 2 (Col
orTemperatureMireds). The device SHALL then move from its current color temperature in an up
or down direction by one step, as detailed in the table.

_Table parsed from section 'Commands':_

* In the Color Control Cluster, under the Commands section, the 'StepMode' command with the value 'Up' is designed to increase the ColorTemperatureMireds attribute, which effectively decreases the color temperature in kelvins by one step. This action continues until the ColorTemperatureMireds attribute reaches the device's maximum limit, as defined by either the ColorTemperatureMaximumMireds field or the ColorTempPhysicalMaxMireds attribute, at which point the stepping operation must cease. The conformance rule for this command is not explicitly provided in the table row data, but based on the Matter Conformance Interpretation Guide, if it were to be specified, it would indicate whether this command is mandatory, optional, provisional, deprecated, or disallowed, possibly with conditions based on the presence of certain features or attributes.

* In the Color Control Cluster, under the Commands section, the 'StepMode' command with the value 'Down' is designed to decrease the ColorTemperatureMireds attribute, which effectively increases the color temperature in kelvins by one step. The operation will cease if the ColorTemperatureMireds attribute reaches the device's minimum limit, as defined by either the ColorTemperatureMinimumMireds field or the ColorTempPhysicalMinMireds attribute. The conformance rule for this command is not explicitly provided in the table row data, but if it were, it would specify the conditions under which this command is mandatory, optional, provisional, deprecated, or disallowed, using the conformance interpretation guide. Without a specific conformance string, we assume it follows the default behavior expected for such commands in the Matter specification.

