
# 1.7 Boolean State Cluster

This cluster provides an interface to a boolean state.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute named "StateValue" within the Boolean State Cluster, identified by the ID '0x0000'. This attribute is of type 'bool', indicating it represents a boolean value. The 'Quality' is marked as 'P', suggesting that the attribute's status is provisional, meaning it is temporary and may change in future specifications. The 'Access' field 'R V' indicates that this attribute can be read and is volatile, meaning its value can change without a write operation. The 'Conformance' is marked as 'M', which means that the "StateValue" attribute is mandatory and must always be implemented in any device or application that supports the Boolean State Cluster, according to the Matter specification.

1.7.4.1. StateValue Attribute
This represents a boolean state.
The semantics of this boolean state are defined by the device type using this cluster.
For example, in a Contact Sensor device type, FALSE=open or no contact, TRUE=closed or contact.

## Events

_Table parsed from section 'Events':_

* In the Boolean State Cluster, under the Events section, the table row describes an event with the ID '0x00' named 'StateChange'. This event has an informational priority level ('INFO') and requires 'V' access, which typically indicates a specific type of access permission such as view or read. The conformance for this event is marked as 'O', meaning it is optional. This indicates that the 'StateChange' event is not required to be implemented in all devices or scenarios; it can be included at the discretion of the implementer without any dependencies or conditions.

1.7.5.1. StateChange Event
If this event is supported, it SHALL be generated when the StateValue attribute changes.

_Table parsed from section 'Events':_

* The table row describes an event within the Boolean State Cluster, specifically the "StateValue" event, which is of type boolean. The conformance rule for this event is marked as "M," indicating that it is mandatory. This means that the "StateValue" event must always be implemented and supported in any device or application that utilizes the Boolean State Cluster, without any conditions or exceptions.

1.7.5.1.1. StateValue Field
This field SHALL indicate the new value of the StateValue attribute.