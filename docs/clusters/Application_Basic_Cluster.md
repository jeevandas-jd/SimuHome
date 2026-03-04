
# 6.3 Application Basic Cluster

This cluster provides information about a Content App running on a Video Player device which is
represented as an endpoint (see Device Type Library document).
The cluster server for this cluster should be supported on each endpoint that represents a Content
App on a Video Player device. This cluster provides identification information about the Content
App such as vendor and product.

## Data Types
6.3.4.1. ApplicationStatusEnum Type
This data type is derived from enum8.

_Table parsed from section 'Data Types':_

* In the context of the Application Basic Cluster, specifically within the Data Types section, the table row describes a data type with the value '0' named 'Stopped', which indicates that the application is not running. The conformance rule for this entry is 'M', meaning that the 'Stopped' state is a mandatory element. This implies that any implementation of the Application Basic Cluster must include this data type to be compliant with the Matter specification. The mandatory status ensures that the 'Stopped' state is always recognized and supported, providing a consistent understanding across different implementations that the application is not currently active.

* In the context of the Application Basic Cluster, specifically within the Data Types section, the table row describes an element named "ActiveVisibleFocus" with a value of '1'. This element signifies that the application is currently running, visible to the user, and is the active target for input. The conformance rule for "ActiveVisibleFocus" is marked as 'M', which means it is mandatory. This indicates that the element is always required to be implemented in any device or application that adheres to this specification, without any conditions or exceptions.

* In the context of the Application Basic Cluster, specifically within the Data Types section, the table row describes an element named 'ActiveHidden' with a value of '2'. The summary indicates that this element represents a state where the application is running but not visible to the user. The conformance rule for 'ActiveHidden' is marked as 'M', which means it is mandatory. This implies that the 'ActiveHidden' element is always required to be implemented in any device or application that supports the Application Basic Cluster, without any conditions or exceptions.

* In the context of the Application Basic Cluster, under the Data Types section, the table row describes a data type with the value '3' named 'ActiveVisibleNotFocus'. This data type indicates that an application is running and visible but is not the active target for input. The conformance rule 'M' signifies that this element is mandatory, meaning it is always required to be implemented according to the Matter specification. There are no conditions or dependencies affecting its mandatory status, ensuring that any implementation of the Application Basic Cluster must include this data type.

6.3.4.2. ApplicationStruct Type
This indicates a global identifier for an Application given a catalog.

_Table parsed from section 'Data Types':_

* In the context of the Application Basic Cluster, within the Data Types section, the table row describes an element with the ID '0' named 'CatalogVendorID'. This element is of the type 'uint16', which indicates it is a 16-bit unsigned integer. The 'Constraint' field is marked as 'all', suggesting that this data type applies universally within its context. The 'Conformance' field is marked with 'M', which stands for Mandatory. This means that the 'CatalogVendorID' element is always required to be implemented in any device or application that supports the Application Basic Cluster, without any conditions or exceptions.

* The table row describes an element within the Application Basic Cluster, specifically in the Data Types section. The element is identified by the ID '1' and is named 'ApplicationID'. It is of the 'string' type and has a constraint labeled 'all', indicating that it applies universally without specific limitations. The conformance rule for 'ApplicationID' is marked as 'M', which stands for Mandatory. This means that the 'ApplicationID' element is always required to be implemented in any device or application that supports the Application Basic Cluster, with no conditions or exceptions.

6.3.4.2.1. CatalogVendorID Field
This field SHALL indicate the Connectivity Standards Alliance issued vendor ID for the catalog. The
DIAL registry SHALL use value 0x0000.
It is assumed that Content App Platform providers (see Video Player Architecture section in [Matter
DevLib]) will have their own catalog vendor ID (set to their own Vendor ID) and will assign an
ApplicationID to each Content App.
6.3.4.2.2. ApplicationID Field
This field SHALL indicate the application identifier, expressed as a string, such as "123456-5433",
"PruneVideo" or "Company X". This field SHALL be unique within a catalog.
For the DIAL registry catalog, this value SHALL be the DIAL prefix.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Application Basic Cluster, specifically the 'VendorName' attribute. This attribute has an ID of '0x0000' and is of type 'string', with a constraint limiting its maximum length to 32 characters. The quality of this attribute is marked as 'F', indicating it is a fundamental attribute, and its default value is 'empty'. The access level is 'R V', meaning it is readable and can be viewed. The conformance rule for 'VendorName' is 'O', which means this attribute is optional. It is not required for implementation and has no dependencies on other features or conditions.

* The table row describes an attribute within the Application Basic Cluster, specifically the 'VendorID' attribute. This attribute is identified by the ID '0x0001' and is of the type 'vendor-id'. It applies to all instances of the cluster, as indicated by the 'Constraint' being 'all'. The 'Quality' is marked as 'F', which typically denotes a specific characteristic or requirement related to the attribute's quality. The 'Access' field 'R V' suggests that the attribute is readable ('R') and may be volatile ('V'), meaning its value can change without notice. The 'Conformance' field is marked as 'O', indicating that the 'VendorID' attribute is optional. This means that while it is not required to be implemented, it can be included without any dependencies or conditions.

* In the context of the Application Basic Cluster, the table row describes an attribute named "ApplicationName" with an ID of '0x0002'. This attribute is of type 'string' and has constraints that are described elsewhere in the documentation, indicated by 'desc'. The quality is marked as 'F', and it has access permissions of 'R V', meaning it can be read and viewed. The conformance rule for "ApplicationName" is 'M', which signifies that this attribute is mandatory. It is always required to be implemented in any device or application that supports the Application Basic Cluster, with no conditions or exceptions.

* The table row describes an attribute within the Application Basic Cluster, specifically the 'ProductID', which is identified by the ID '0x0003'. This attribute is of type 'uint16', meaning it is a 16-bit unsigned integer, and it applies to all instances of the cluster as indicated by the 'Constraint' field. The 'Quality' field is marked as 'F', which typically denotes a specific quality or characteristic defined elsewhere in the specification. The 'Access' field 'R V' indicates that this attribute is readable and has a specific visibility or access level. The 'Conformance' field is marked as 'O', meaning that the 'ProductID' attribute is optional. This indicates that while the attribute can be implemented, it is not required and does not depend on any other features or conditions within the Matter specification.

* In the Application Basic Cluster, under the Attributes section, the entry with ID '0x0004' refers to an attribute named 'Application', which is of the type 'ApplicationStruct'. The 'Constraint' is described elsewhere in the documentation, and the 'Quality' is marked as 'F', indicating a specific quality level. The 'Access' is defined as 'R V', meaning it is readable and possibly volatile. The 'Conformance' for this attribute is marked as 'M', which signifies that it is mandatory. This means that the 'Application' attribute is always required to be implemented in any device or application that supports the Application Basic Cluster, without any conditions or exceptions.

* The table row describes an attribute within the Application Basic Cluster, specifically the 'Status' attribute, identified by the ID '0x0005'. This attribute is of the type 'ApplicationStatusEnum' and has constraints described elsewhere in the documentation. Its default value is 'MS', and it has read and view access permissions ('R V'). The conformance rule for this attribute is 'M', which means that the 'Status' attribute is mandatory and must always be implemented in any device or application that supports the Application Basic Cluster. This requirement is unconditional and does not depend on any other features or conditions.

* In the Application Basic Cluster, under the Attributes section, the table row describes an attribute with the ID `0x0006` named `ApplicationVersion`. This attribute is of type `string` with a maximum constraint of 32 characters. It is marked with a quality of `F`, indicating a specific characteristic or requirement defined elsewhere in the specification. The access level is `R V`, meaning it is readable and possibly volatile. The conformance rule for `ApplicationVersion` is `M`, which signifies that this attribute is mandatory. This means it is always required to be implemented in any device or application that supports the Application Basic Cluster, with no conditions or exceptions.

* The table row describes an attribute named "AllowedVendorList" within the Application Basic Cluster's Attributes section. This attribute has an ID of '0x0007' and is of the type 'list[vendor-id]', indicating it holds a list of vendor IDs. The 'Quality' is marked as 'F', which typically denotes a specific characteristic or requirement related to the attribute, though the exact meaning of 'F' is not provided in the context. The 'Access' is 'R A', meaning the attribute can be read ('R') and accessed ('A'), which usually implies it can be modified or interacted with in some way. The conformance rule for this attribute is 'M', which stands for Mandatory. This means that the "AllowedVendorList" attribute is always required to be implemented in any device or application that supports the Application Basic Cluster, with no conditions or exceptions.

6.3.5.1. VendorName Attribute
This attribute SHALL specify a human readable (displayable) name of the vendor for the Content
App.
6.3.5.2. VendorID Attribute
This attribute, if present, SHALL specify the Connectivity Standards Alliance assigned Vendor ID for
the Content App.
6.3.5.3. ApplicationName Attribute
This attribute SHALL specify a human readable (displayable) name of the Content App assigned by
the  vendor.  For  example,  "NPR  On  Demand".  The  maximum  length  of  the  ApplicationName
attribute is 256 bytes of UTF-8 characters.
6.3.5.4. ProductID Attribute
This attribute, if present, SHALL specify a numeric ID assigned by the vendor to identify a specific
Content App made by them. If the Content App is certified by the Connectivity Standards Alliance,
then this would be the Product ID as specified by the vendor for the certification.
6.3.5.5. Application Attribute
This attribute SHALL specify a Content App which consists of an Application ID using a specified
catalog.
6.3.5.6. Status Attribute
This attribute SHALL specify the current running status of the application.
6.3.5.7. ApplicationVersion Attribute
This attribute SHALL specify a human readable (displayable) version of the Content App assigned
by the vendor. The maximum length of the ApplicationVersion attribute is 32 bytes of UTF-8 charac
ters.
6.3.5.8. AllowedVendorList Attribute
This attribute is a list of vendor IDs. Each entry is a vendor-id.