
# 6.9 Media Input Cluster

This cluster provides an interface for controlling the Input Selector on a media device such as a
Video Player.
This cluster would be implemented on TV and other media streaming devices, as well as devices
that provide input to or output from such devices.
This cluster provides the list of available inputs and provides commands for selecting and renam
ing them.
The cluster server for Media Input is implemented by a device that has selectable input, such as a
Video Player device.

## Data Types
6.9.5.1. InputTypeEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the Media Input Cluster, under the Data Types section, the table row describes a data type with the value '0' and the name 'Internal'. This data type is used to indicate content that is not sourced from a physical input. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Internal' data type is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

* In the Media Input Cluster's Data Types section, the table row describes an entry with the 'Value' of '1' and the 'Name' of 'Aux'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Aux' data type is a required element within the Media Input Cluster and must be implemented in all instances where this cluster is used. There are no conditions or dependencies affecting its mandatory status, indicating that it is a fundamental part of the cluster's specification.

* In the Media Input Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '2' and the 'Name' of 'Coax'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Coax' data type is a required element within the Media Input Cluster. It must be supported and implemented in all devices or systems that conform to this specification, without any conditions or exceptions.

* In the Media Input Cluster, under the Data Types section, there is an entry with the name "Composite" and a value of "3". The conformance rule for this entry is marked as "M", which stands for Mandatory. This means that the "Composite" data type is a required element within the Media Input Cluster and must be implemented in any device or application that supports this cluster, without any conditions or exceptions.

* In the context of the Media Input Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '4' and the 'Name' of 'HDMI'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the HDMI input type is a required element within the Media Input Cluster, and it must be supported by any implementation of this cluster according to the Matter specification. There are no conditions or dependencies affecting this requirement; it is an absolute necessity for compliance.

* In the Media Input Cluster, under the Data Types section, the table row describes an element with the name 'Input' and a value of '5'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Input' element is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

* In the context of the Media Input Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '6' and the 'Name' of 'Line'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'Line' data type is a required element within the Media Input Cluster and must be implemented in all devices or systems that support this cluster, without any conditions or exceptions.

* In the Media Input Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '7' and the 'Name' of 'Optical'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Optical' data type is a required element within the Media Input Cluster and must be implemented in all instances of this cluster according to the Matter specification. There are no conditions or dependencies that alter this requirement; it is a straightforward mandate.

* In the Media Input Cluster, under the Data Types section, there is an entry for a data type named 'Video' with a value of '8'. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'Video' data type is a required element within the Media Input Cluster and must be implemented in all devices or systems that support this cluster, without any conditions or exceptions.

* In the context of the Media Input Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '9' and the 'Name' of 'SCART'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the SCART data type is a required element within the Media Input Cluster and must be implemented in all instances of this cluster according to the Matter IoT specification. There are no conditions or exceptions; SCART must always be supported.

* In the context of the Media Input Cluster, specifically within the Data Types section, the table row entry describes a data type with the 'Value' of '10' and the 'Name' of 'USB'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'USB' data type is a required element within the Media Input Cluster and must be implemented in all instances where this cluster is used. There are no conditions or exceptions; the inclusion of this data type is obligatory according to the Matter specification.

* In the Media Input Cluster, under the Data Types section, the table row describes an entry with the 'Value' of '11' and the 'Name' of 'Other'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Other' data type with the value '11' is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

6.9.5.2. InputInfoStruct Type
This contains information about an input.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Media Input Cluster, specifically in the Data Types section. The entry is for an element named "Index," which is of type `uint8` and has a constraint labeled as "all," indicating it applies universally within its context. The conformance rule for this element is marked as "M," meaning that the "Index" element is mandatory. This implies that it is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

* The table row describes an element within the Media Input Cluster, specifically a data type named "InputType" with the type "InputTypeEnum." The constraint is marked as "desc," indicating that the constraints are detailed elsewhere in the documentation. The conformance rule for "InputType" is marked as "M," which means that this element is mandatory. Therefore, "InputType" must always be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

* In the Media Input Cluster, under the Data Types section, there is an entry with the ID '2' named 'Name', which is of the type 'string'. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Name' attribute is always required to be implemented in any device or application that supports the Media Input Cluster. There are no conditions or exceptions to this requirement, indicating that the 'Name' attribute is a fundamental and essential part of the Media Input Cluster specification.

* In the context of the Media Input Cluster, specifically within the Data Types section, the table row describes an element with the ID '3' named 'Description', which is of the type 'string'. The conformance rule for this element is 'M', indicating that it is mandatory. This means that the 'Description' element must always be included and supported in any implementation of the Media Input Cluster, without any conditions or exceptions.

6.9.5.2.1. Index Field
This field SHALL indicate the unique index into the list of Inputs.
6.9.5.2.2. InputType Field
This field SHALL indicate the type of input
6.9.5.2.3. Name Field
This field SHALL indicate the input name, such as “HDMI 1”. This field may be blank, but SHOULD
be provided when known.
6.9.5.2.4. Description Field
This field SHALL indicate the user editable input description, such as “Living room Playstation”.
This field may be blank, but SHOULD be provided when known.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Media Input Cluster, specifically the 'InputList' attribute, which is identified by the ID '0x0000'. This attribute is of the type 'list[InputInfoStruct]', indicating it holds a list of structures related to input information. The 'Access' field specifies 'R V', meaning the attribute is readable and has volatile characteristics, which might imply it can change frequently or is not persistent. The 'Conformance' field is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'InputList' attribute is always required to be implemented in any device supporting the Media Input Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Media Input Cluster, specifically the 'CurrentInput' attribute. This attribute has an ID of '0x0001' and is of type 'uint8', which means it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', indicating that there are no specific constraints on the values it can hold beyond those inherent to its type. The 'Access' field is marked as 'R V', meaning that the attribute is readable and can be viewed. The 'Conformance' field is marked as 'M', which stands for Mandatory. This means that the 'CurrentInput' attribute is always required to be implemented in any device that supports the Media Input Cluster, without any conditions or exceptions.

6.9.6.1. InputList Attribute
This attribute SHALL provide a list of the media inputs supported by the device.
6.9.6.2. CurrentInput Attribute
This attribute SHALL contain the value of the index field of the currently selected InputInfoStruct.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Media Input Cluster, specifically the "SelectInput" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response ('Y'). The access level is optional ('O'), indicating that while the command can be accessed, it is not required to be implemented by all devices. The conformance rule for this command is 'M', meaning it is mandatory. This implies that any device implementing the Media Input Cluster must support the "SelectInput" command, ensuring consistent functionality across compliant devices.

* The table row describes a command within the Media Input Cluster, specifically the "ShowInputStatus" command. This command is initiated by the client and directed towards the server, with a response expected from the server. The access level for this command is optional, meaning it is not required to be implemented by default. However, the conformance rule for this command is marked as "M," indicating that it is mandatory. This means that, according to the Matter specification, any implementation of the Media Input Cluster must include the "ShowInputStatus" command, ensuring that it is always available and supported in compliant devices.

* The table row describes a command within the Media Input Cluster, specifically the "HideInputStatus" command, which is directed from the client to the server. The command has an ID of '0x02' and requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required for all implementations. The conformance rule for this command is 'M', indicating that it is mandatory. This means that any implementation of the Media Input Cluster must support the "HideInputStatus" command, regardless of any other conditions or features.

* The table row describes a command within the Media Input Cluster, specifically the "RenameInput" command, which is directed from the client to the server. This command requires a response, as indicated by the 'Response' field marked 'Y', and it has mandatory access, as shown by the 'Access' field marked 'M'. The 'Conformance' field is marked as 'NU', which, according to the Matter Conformance Interpretation Guide, suggests that the command is mandatory if the feature 'NU' is supported. If 'NU' is not supported, the conformance of this command is not explicitly defined in this entry, implying that further documentation might be needed to fully understand its status in such cases.

6.9.7.1. SelectInput Command
Upon receipt, this command SHALL change the media input on the device to the input at a specific
index in the Input List.

_Table parsed from section 'Commands':_

* In the Media Input Cluster, under the Commands section, the table row describes a command with the ID '0' named 'Index', which is of type 'uint8' and applies to all constraints. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Index' command is always required to be implemented in any device or application that supports the Media Input Cluster, with no exceptions or conditions.

6.9.7.1.1. Index Field
This field SHALL indicate the index field of the InputInfoStruct from the InputList attribute in
which to change to.
6.9.7.2. ShowInputStatus Command
Upon receipt, this command SHALL display the active status of the input list on screen.
6.9.7.3. HideInputStatus Command
Upon receipt, this command SHALL hide the input list from the screen.
6.9.7.4. RenameInput Command
Upon receipt, this command SHALL rename the input at a specific index in the Input List.
Updates to the input name SHALL appear in the device’s settings menus.

_Table parsed from section 'Commands':_

* In the Media Input Cluster, under the Commands section, the table row describes a command with the ID '0' named 'Index', which is of type 'uint8' and has a constraint labeled 'all'. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Index' command is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

* The table row describes an element within the Media Input Cluster, specifically under the Commands section. The element is identified by the ID '1' and is named 'Name'. It is of the type 'string' and has a constraint labeled 'all', indicating that it applies universally within its context. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Name' command is always required to be implemented in any device or application that supports the Media Input Cluster, without any conditions or exceptions.

