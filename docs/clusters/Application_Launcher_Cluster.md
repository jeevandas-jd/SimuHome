
# 6.4 Application Launcher Cluster

This cluster provides an interface for launching applications on a Video Player device such as a TV.
This cluster is supported on endpoints that can launch Applications, such as a Casting Video Player
device with a Content App Platform. It supports identifying an Application by global identifier from
a given catalog, and launching it. It also supports tracking the currently in-focus Application.
Depending on the support for the Application Platform feature, the cluster can either support
launching the application corresponding to the endpoint on which the cluster is supported (AP fea
ture not supported) or it can support launching any application (AP feature supported).

## Data Types
6.4.5.1. StatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Application Launcher Cluster's Data Types, the table row describes an entry with the 'Value' of '0', named 'Success', which indicates that a command has succeeded. The 'Conformance' field for this entry is marked as 'M', meaning that this element is mandatory. This implies that the 'Success' status, represented by the value '0', is a required element in the specification and must always be implemented in any device or application that supports the Application Launcher Cluster. There are no conditions or dependencies affecting its mandatory status, making it an essential part of the cluster's functionality.

* In the context of the Application Launcher Cluster, specifically within the Data Types section, the table row describes an entry with the value '1' and the name 'AppNotAvailable'. This entry signifies that the requested application is not available. The conformance rule for this entry is marked as 'M', which stands for Mandatory. This means that the 'AppNotAvailable' data type is a required element in the specification and must be implemented in all devices or systems that support the Application Launcher Cluster, without any conditions or exceptions.

* In the context of the Application Launcher Cluster, specifically within the Data Types section, the table entry describes a data type with the value '2' named 'SystemBusy'. This data type indicates that a video platform is unable to honor a command, as summarized by its description. The conformance rule for 'SystemBusy' is marked as 'M', which stands for Mandatory. This means that the 'SystemBusy' data type is always required to be implemented in any system or device that supports the Application Launcher Cluster, without any conditions or exceptions.

* In the context of the Application Launcher Cluster, specifically within the Data Types section, the table row describes an entry with the 'Value' of '3' and the 'Name' of 'PendingUserApproval'. This entry signifies that user approval for an application download is pending, as indicated by its 'Summary'. The 'Conformance' field for this entry is marked as 'M', which stands for Mandatory. According to the Matter Conformance Interpretation Guide, this means that the 'PendingUserApproval' element is always required in any implementation of the Application Launcher Cluster, without any conditions or exceptions.

* In the context of the Application Launcher Cluster, specifically within the Data Types section, the table row describes a data type with the value '4', named 'Downloading'. This data type represents the state of "Downloading the requested app." According to the conformance rule 'M', this element is mandatory, meaning it is always required to be implemented in any device or application that supports the Application Launcher Cluster. There are no conditions or exceptions to this requirement, indicating its fundamental importance in the cluster's functionality.

* In the context of the Application Launcher Cluster's Data Types, the table entry describes a data type with the value '5', named 'Installing', which represents the state of "Installing the requested app". The conformance rule for this entry is 'M', indicating that this element is mandatory. This means that within the Application Launcher Cluster, the 'Installing' state must always be implemented and supported as part of the specification. There are no conditions or exceptions; it is a required element for compliance with the Matter specification.

6.4.5.2. ApplicationStruct Type
This indicates a global identifier for an Application given a catalog.

_Table parsed from section 'Data Types':_

* The table row describes an entry within the Application Launcher Cluster, specifically in the Data Types section. The entry is for an element named 'CatalogVendorID', which is of type 'uint16' and has a constraint labeled as 'all', indicating it applies universally without specific restrictions. The conformance rule for 'CatalogVendorID' is marked as 'M', meaning that this element is mandatory. This implies that 'CatalogVendorID' must always be implemented and supported in any device or application that utilizes the Application Launcher Cluster, without any conditions or exceptions.

* In the Application Launcher Cluster, within the Data Types section, the table row describes an element with the ID '1' named 'ApplicationID', which is of the type 'string' and has a constraint labeled 'all'. The conformance rule for this element is 'M', indicating that the 'ApplicationID' is a mandatory element. This means it is always required to be implemented in any device or application that supports the Application Launcher Cluster, without any conditions or exceptions.

6.4.5.2.1. CatalogVendorID Field
This field SHALL indicate the CSA-issued vendor ID for the catalog. The DIAL registry SHALL use
value 0x0000.
Content App Platform providers will have their own catalog vendor ID (set to their own Vendor ID)
and will assign an ApplicationID to each Content App.
6.4.5.2.2. ApplicationID Field
This field SHALL indicate the application identifier, expressed as a string, such as "PruneVideo" or
"Company X". This field SHALL be unique within a catalog.
For the DIAL registry catalog, this value SHALL be the DIAL prefix (see [DIAL Registry]).
6.4.5.3. ApplicationEPStruct Type
This specifies an app along with its corresponding endpoint.

_Table parsed from section 'Data Types':_

* In the context of the Application Launcher Cluster, within the Data Types section, the table row describes an element with the ID '0' named 'Application', which is of the type 'ApplicationStruct' and has a constraint labeled 'all'. The conformance rule for this element is 'M', which stands for Mandatory. This means that the 'Application' element is always required to be implemented in any device or system that supports the Application Launcher Cluster, without any conditions or exceptions.

* In the context of the Application Launcher Cluster, specifically within the Data Types section, the table row describes an element with the ID '1' named 'Endpoint'. This element is of the type 'endpoint-no' and has a constraint labeled 'all', with a default value of 'MS'. The conformance rule for this element is 'O', which indicates that the 'Endpoint' element is optional. This means that while it is not required to be implemented, it can be included without any dependencies or conditions. The optional status allows for flexibility in implementation, as the element can be omitted without affecting compliance with the Matter specification.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "CatalogList" within the Application Launcher Cluster, specifically under the Attributes section. This attribute has an ID of '0x0000' and is of the type 'list[uint16]', indicating it is a list composed of 16-bit unsigned integers. The 'Quality' is marked as 'N', which typically denotes a non-reportable attribute, and the 'Access' is 'R V', meaning it is readable and has a volatile nature. The 'Conformance' field is marked as 'AP', which, according to the Matter Conformance Interpretation Guide, indicates that the attribute is currently provisional. This means its status is temporary, and it is intended to become mandatory in the future. Therefore, while it is not yet a required element, it is expected to be so in subsequent updates of the specification.

* The table row describes an attribute named "CurrentApp" within the Application Launcher Cluster, identified by the ID '0x0001'. This attribute is of the type 'ApplicationEPStruct' and has a constraint described elsewhere in the documentation. It is marked with a quality of 'X', indicating that it is explicitly disallowed in some contexts. The default value for this attribute is 'null', and it has read and view access permissions ('R V'). The conformance rule 'O' signifies that the "CurrentApp" attribute is optional, meaning it is not required and has no dependencies on other features or conditions within the Matter specification.

6.4.6.1. CatalogList Attribute
This attribute SHALL specify the list of supported application catalogs, where each entry in the list
is the CSA-issued vendor ID for the catalog. The DIAL registry (see [DIAL Registry]) SHALL use value
0x0000.
It is expected that Content App Platform providers will have their own catalog vendor ID (set to
their own Vendor ID) and will assign an ApplicationID to each Content App.
6.4.6.2. CurrentApp Attribute
This attribute SHALL specify the current in-focus application, identified using an Application ID,
catalog vendor ID and the corresponding endpoint number when the application is represented by
a Content App endpoint. A null SHALL be used to indicate there is no current in-focus application.

## Commands

_Table parsed from section 'Commands':_

* In the context of the Application Launcher Cluster, the command 'LaunchApp' with ID '0x00' is a client-to-server command that expects a response of type 'LauncherResponse'. The access level for this command is optional ('O'), indicating that it is not required for all implementations. However, the conformance rule for 'LaunchApp' is marked as 'M', meaning that this command is mandatory. This implies that any implementation of the Application Launcher Cluster must support the 'LaunchApp' command, regardless of other conditions or features.

* The table row describes a command within the Application Launcher Cluster, specifically the "StopApp" command. This command is directed from the client to the server and expects a "LauncherResponse" in return. The access level for this command is marked as optional ("O"), indicating that it is not required to be implemented by all devices. However, the conformance rule for this command is marked as "M," meaning that it is mandatory. This implies that, regardless of the optional access level, the "StopApp" command must be implemented in all devices that support the Application Launcher Cluster, ensuring consistent functionality across compliant devices.

* The table row describes a command named "HideApp" within the Application Launcher Cluster, which is directed from the client to the server. The command has an associated response called "LauncherResponse" and requires optional access permissions. The conformance rule for this command is marked as "M," which means it is mandatory. This indicates that the "HideApp" command must always be implemented in any device or application that supports this cluster, without any conditional dependencies or exceptions.

* The table row describes a command within the Application Launcher Cluster, specifically the "LauncherResponse" command. This command is identified by the ID '0x03' and is directed from the server to the client, as indicated by the "client ⇐ server" direction. The 'Response' field marked as 'N' suggests that this command does not expect a response. The 'Conformance' field is marked as 'M', which means that the "LauncherResponse" command is mandatory. This implies that any implementation of the Application Launcher Cluster must include this command, as it is always required according to the Matter specification.

6.4.7.1. LaunchApp Command
Upon receipt of this command, the server SHALL launch the application with optional data. The
application SHALL be either
• the specified application, if the Application Platform feature is supported;
• otherwise the application corresponding to the endpoint.
The endpoint SHALL launch and bring to foreground the requisite application if the application is
not already launched and in foreground. The Status attribute SHALL be updated to ActiveVisibleFo
cus on the Application Basic cluster of the Endpoint corresponding to the launched application. The
Status attribute SHALL be updated on any other application whose Status MAY have changed as a
result of this command. The CurrentApp attribute, if supported, SHALL be updated to reflect the
new application in the foreground.
This command returns a Launcher Response.

_Table parsed from section 'Commands':_

* In the context of the Application Launcher Cluster, specifically within the Commands section, the table row describes an element with the ID '0' and the name 'Application', which is of the type 'ApplicationStruct'. The 'Constraint' is marked as 'desc', indicating that the constraints for this element are detailed elsewhere in the documentation. The 'Conformance' field is labeled as 'AP', which, according to the Matter Conformance Interpretation Guide, suggests that the element is provisionally required. This means that while it is currently in a provisional state, it is intended to become mandatory in the future. Therefore, implementers should be aware that this element may soon be required for compliance with the Matter specification.

* In the context of the Application Launcher Cluster, specifically within the Commands section, the table row describes an element with the ID '1' named 'Data'. This element is of the type 'octstr' and has a default value of 'MS'. According to the conformance rule 'O', this element is classified as Optional. This means that the 'Data' command is not required to be implemented in every instance of the Application Launcher Cluster, and there are no dependencies or conditions that affect its optional status. Implementers have the discretion to include or exclude this element based on their specific application needs or design preferences.

6.4.7.1.1. Application Field
This field SHALL specify the Application to launch.
6.4.7.1.2. Data Field
This field SHALL specify optional app-specific data to be sent to the app.
This format and meaning of this value is proprietary and outside the specification.
It provides a transition path for device makers that use other protocols (like DIAL)
NOTE which  allow  for  proprietary  data.  Apps  that  are  not  yet  Matter  aware  can  be
launched via Matter, while retaining the existing ability to launch with proprietary
data.
6.4.7.2. StopApp Command
Upon receipt of this command, the server SHALL stop the application if it is running. The applica
tion SHALL be either
• the specified application, if the Application Platform feature is supported;
• otherwise the application corresponding to the endpoint.
The Status attribute SHALL be updated to Stopped on the Application Basic cluster of the Endpoint
corresponding to the stopped application. The Status attribute SHALL be updated on any other
application whose Status MAY have changed as a result of this command.
This command returns a Launcher Response.

_Table parsed from section 'Commands':_

* In the Application Launcher Cluster, within the Commands section, the table row describes an element with the ID '0' and the Name 'Application', which is of the Type 'ApplicationStruct'. The 'Constraint' for this element is described elsewhere in the documentation, indicated by 'desc'. The 'Default' value for this element is 'MS'. The 'Conformance' field is marked as 'AP', meaning this element is Mandatory if the feature 'AP' is supported. This implies that whenever the 'AP' feature is present, the 'Application' command must be implemented as part of the Application Launcher Cluster.

6.4.7.2.1. Application Field
This field SHALL specify the Application to stop.
6.4.7.3. HideApp Command
Upon receipt of this command, the server SHALL hide the application. The application SHALL be
either
• the specified application, if the Application Platform feature is supported;
• otherwise the application corresponding to the endpoint.
The endpoint MAY decide to stop the application based on manufacturer specific behavior or
resource constraints if any. The Status attribute SHALL be updated to ActiveHidden or Stopped,
depending on the action taken, on the Application Basic cluster of the Endpoint corresponding to
the application on which the action was taken. The Status attribute SHALL be updated on any other
application whose Status MAY have changed as a result of this command.
This command returns a Launcher Response.

_Table parsed from section 'Commands':_

* In the context of the Application Launcher Cluster, specifically within the Commands section, the table row describes an element with the ID '0' named 'Application', which is of the type 'ApplicationStruct'. The 'Constraint' for this element is described elsewhere in the documentation, as indicated by 'desc'. The default value for this element is 'MS'. The conformance rule 'AP' signifies that this element is mandatory if the feature 'AP' is supported. In simpler terms, if the 'AP' feature is present, the 'Application' command must be implemented; otherwise, it is not required.

6.4.7.3.1. Application Field
This field SHALL specify the Application to hide.
6.4.7.4. LauncherResponse Command
This command SHALL be generated in response to LaunchApp/StopApp/HideApp commands.

_Table parsed from section 'Commands':_

* In the context of the Application Launcher Cluster, within the Commands section, the table row describes a command identified by 'ID' 0, named 'Status', which is of the type 'StatusEnum' and applies to all constraints. The conformance rule for this command is 'M', which stands for Mandatory. This means that the 'Status' command is always required to be implemented in any device or application that supports the Application Launcher Cluster, without any conditions or exceptions.

* In the context of the Application Launcher Cluster, specifically within the Commands section, the table row describes an element with the ID '1' named 'Data', which is of type 'octstr' and has a default value of 'MS'. The conformance rule for this element is marked as 'O', indicating that it is optional. This means that the 'Data' command is not required to be implemented and does not have any dependencies or conditions that would make it mandatory. Implementers have the flexibility to include or exclude this element based on their specific needs or preferences without affecting compliance with the Matter specification.

6.4.7.4.1. Status Field
This field SHALL indicate the status of the command which resulted in this response.
6.4.7.4.2. Data Field
This field SHALL specify Optional app-specific data.