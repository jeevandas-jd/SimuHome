
# 6.5 Audio Output Cluster

This cluster provides an interface for controlling the Output on a Video Player device such as a TV.
This cluster would be supported on a device with audio outputs like a Video Player device (Smart
TV, TV Setup Top Box, Smart Speaker, etc).
This cluster provides the list of available outputs and provides commands for selecting and renam
ing them.
The cluster server for Audio Output is implemented by a device that has configurable audio output.

## Data Types
6.5.5.1. OutputTypeEnum Type
This data type is derived from enum8.
The type of output, expressed as an enum, with the following values:

_Table parsed from section 'Data Types':_

* In the context of the Audio Output Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '0', named 'HDMI', which is summarized as 'HDMI'. The 'Conformance' field for this entry is marked as 'M', indicating that the HDMI data type is a mandatory element within this cluster. This means that any implementation of the Audio Output Cluster must include support for the HDMI data type, as it is required by the Matter specification without any conditions or exceptions.

* In the context of the Audio Output Cluster, specifically within the Data Types section, the table row describes an element with the 'Value' of '1' and the 'Name' of 'BT'. The 'Conformance' field for this element is marked as 'M', which stands for Mandatory. This means that the 'BT' element is always required to be implemented in any device or system that supports the Audio Output Cluster according to the Matter specification. There are no conditions or dependencies that alter this requirement; it is an absolute necessity for compliance.

* In the context of the Audio Output Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '2' and the 'Name' of 'Optical'. The 'Conformance' for this entry is marked as 'M', which stands for Mandatory. This means that the 'Optical' data type is a required element within the Audio Output Cluster. It must be implemented and supported in all instances where this cluster is used, without any conditions or exceptions.

* In the context of the Audio Output Cluster, specifically within the Data Types section, the table row describes an element with the 'Value' of '3' and the 'Name' 'Headphone'. The 'Conformance' for this element is marked as 'M', which stands for Mandatory. This means that the 'Headphone' element is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions. This mandatory status ensures that the 'Headphone' functionality is consistently available across all implementations of this cluster.

* In the context of the Audio Output Cluster under the Data Types section, the table row describes an element with the 'Value' of '4' and the 'Name' of 'Internal'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. This means that the 'Internal' element is always required to be implemented in any device or system that supports the Audio Output Cluster, without any conditions or exceptions. This mandatory status ensures that the 'Internal' data type is consistently available across all implementations of this cluster.

* The table row describes an entry within the Audio Output Cluster, specifically under the Data Types section. The entry is identified by the 'Value' of '5' and is named 'Other'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'Other' data type is always required to be implemented in any device or application that supports the Audio Output Cluster. There are no conditions or dependencies affecting its requirement; it must be included in all cases.

6.5.5.2. OutputInfoStruct Type
This contains information about an output.

_Table parsed from section 'Data Types':_

* In the context of the Audio Output Cluster, under the Data Types section, the table row describes an element with the ID '0' named 'Index', which is of type 'uint8' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Index' element is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions.

* The table row describes an element within the Audio Output Cluster, specifically a data type named 'OutputType' with an ID of '1'. This data type is of the type 'OutputTypeEnum', and its constraints are described elsewhere in the documentation, as indicated by 'desc'. The conformance rule for 'OutputType' is marked as 'M', which means it is mandatory. This indicates that the 'OutputType' element is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions.

* In the context of the Audio Output Cluster, within the Data Types section, the table row describes an element with the ID '2' named 'Name', which is of the type 'string' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Name' element is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions.

6.5.5.2.1. Index Field
This field SHALL indicate the unique index into the list of outputs.
6.5.5.2.2. OutputType Field
This field SHALL indicate the type of output.
6.5.5.2.3. Name Field
The device defined and user editable output name, such as “Soundbar”, “Speakers”. This field may
be blank, but SHOULD be provided when known.

## Attributes

_Table parsed from section 'Attributes':_

* The table row entry pertains to the "OutputList" attribute within the Audio Output Cluster, specifically under the Attributes section. This attribute is identified by the ID '0x0000' and is of the type 'list[OutputInfoStruct]', indicating it is a list composed of structures defined as OutputInfoStruct. The access level for this attribute is 'R V', meaning it is readable ('R') and has a volatile nature ('V'), which typically implies that its value can change without a specific event or command. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "OutputList" attribute is always required to be implemented in any device or application that supports the Audio Output Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Audio Output Cluster, specifically the 'CurrentOutput' attribute. This attribute has an ID of '0x0001' and is of type 'uint8', indicating it is an 8-bit unsigned integer. The 'Constraint' is listed as 'all', suggesting that this attribute applies universally within its context. The 'Access' field is marked as 'R V', meaning it is readable and has a volatile nature, which typically implies that its value can change frequently or is not stored persistently. The 'Conformance' is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'CurrentOutput' attribute is always required to be implemented in any device that supports the Audio Output Cluster, without any conditions or exceptions.

6.5.6.1. OutputList Attribute
This attribute provides the list of outputs supported by the device.
6.5.6.2. CurrentOutput Attribute
This attribute contains the value of the index field of the currently selected OutputInfoStruct.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Audio Output Cluster, specifically the "SelectOutput" command, which is identified by the ID '0x00'. This command is directed from the client to the server, and it requires a response ('Y'). The access level for this command is optional ('O'), meaning it is not required to be implemented by default. The conformance rule for this command is 'M', indicating that it is mandatory. This means that regardless of any other conditions or features, the "SelectOutput" command must always be implemented in any device that supports the Audio Output Cluster.

_Table parsed from section 'Commands':_

* The table row describes a command within the Audio Output Cluster, specifically the "RenameOutput" command, which is directed from the client to the server. The command has an ID of '0x01' and requires a response ('Y'), with mandatory access ('M'). The conformance rule 'NU' indicates that the command is mandatory if the feature 'NU' is supported. If 'NU' is not supported, the conformance rule does not specify an alternative, implying that the command is not required. This means that the presence and implementation of the "RenameOutput" command depend on whether the 'NU' feature is part of the device's capabilities.

6.5.7.1. SelectOutput Command
Upon receipt, this SHALL change the output on the device to the output at a specific index in the
Output List.
Note that when the current output is set to an output of type HDMI, adjustments to volume via a
Speaker endpoint on the same node MAY cause HDMI volume up/down commands to be sent to the
given HDMI output.

_Table parsed from section 'Commands':_

* The table row describes a command within the Audio Output Cluster, specifically the 'Index' command. This command has an ID of '0', is of type 'uint8', and applies to all constraints. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Index' command is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions.

6.5.7.1.1. Index Field
This SHALL indicate the index field of the OutputInfoStruct from the OutputList attribute in which
to change to.
6.5.7.2. RenameOutput Command
Upon receipt, this SHALL rename the output at a specific index in the Output List.
Updates to the output name SHALL appear in the device’s settings menus. Name updates MAY auto
matically be sent to the actual device to which the output connects.

_Table parsed from section 'Commands':_

* The table row describes a command within the Audio Output Cluster, specifically the "Index" command. This command is identified by the ID '0' and is of the type 'uint8', meaning it is an 8-bit unsigned integer. The 'Constraint' field indicates that this command applies universally ('all'). The conformance rule for this command is 'M', which stands for Mandatory. This means that the "Index" command is always required to be implemented in any device or application that supports the Audio Output Cluster, without any conditions or exceptions.

* In the context of the Audio Output Cluster, under the Commands section, the table row describes an element with the ID '1' and the Name 'Name', which is of the type 'string' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the element is always required to be implemented in any device or system that supports the Audio Output Cluster, without any conditions or exceptions.

