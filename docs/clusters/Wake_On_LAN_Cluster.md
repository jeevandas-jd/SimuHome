
# 1.12 Wake On LAN Cluster

This cluster provides an interface for managing low power mode on a device that supports the
Wake On LAN or Wake On Wireless LAN (WLAN) protocol (see [Wake On LAN]).
This cluster would be supported on IP devices that have a low power mode AND support the ability
to be woken up using the Wake on LAN or Wake on WLAN protocol. This cluster provides the
device MAC address which is a required input to the Wake on LAN protocol. Besides the MAC
address, this cluster provides an optional link-local IPv6 address which is useful to support "Wake
on Direct Packet" used by some Ethernet and Wi-Fi devices.
Acting on the MAC address or link-local IPv6 address information does require the caller to be in
the same broadcast domain as the destination. To wake the destination up, the caller sends a multi
cast-based magic UDP packet that contains destination’s MAC address in the UDP payload to FF02::1,
the IPv6 all-nodes link-local multicast group address. If the optional link-local address is provided
by the destination through this cluster, the caller also sends the magic UDP packet in unicast to that
link-local address. This unicast-based method is particularly useful for Wi-Fi devices, since due to
lack of MAC layer retransmission mechanism, multicast over Wi-Fi is not as reliable as unicast. If a
device provides the link-local address in this cluster, its Ethernet controller or Wi-Fi radio SHALL
respond to the IPv6 neighbor solicitation message for the link-local address without the need to
wake host CPU up. In order to receive the magic or neighbor solicitation packets in multicast, the
Wi-Fi devices must support Group Temporal Key (GTK) rekey operation in low power mode.
Most devices automatically enter low power mode based upon inactivity.
The cluster server for Wake on LAN or Wake on WLAN is implemented by a device that supports
the Wake on LAN/WLAN protocol, such as a TV, Set-top Box, or Smart Speaker.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Wake On LAN Cluster, specifically the 'MACAddress' attribute. This attribute has an ID of '0x0000' and is of type 'string', with a constraint that limits its maximum length to 12 characters. The 'Quality' is marked as 'F', and it has 'R V' access, indicating it can be read and is volatile. The 'Conformance' field is marked as 'O', which means that the 'MACAddress' attribute is optional. It is not required for implementation and does not have any dependencies or conditions that would change its optional status.

* The table row describes an attribute within the Wake On LAN Cluster, specifically the 'LinkLocalAddress' attribute. This attribute has an ID of '0x0001' and is of the type 'ipv6adr', indicating it is an IPv6 address. The 'Constraint' is marked as 'desc', suggesting that the constraints for this attribute are detailed elsewhere in the documentation. The 'Quality' is 'F', which typically refers to the feature's reliability or performance characteristics, though the exact meaning would depend on the broader context of the specification. The 'Access' is 'R V', meaning the attribute is readable and possibly volatile, indicating it may change without notice. The 'Conformance' is 'O', which means that the 'LinkLocalAddress' attribute is optional; it is not required and has no dependencies, allowing implementers the flexibility to include or exclude it based on their specific needs or use cases.

1.12.4.1. MACAddress Attribute
This attribute SHALL indicate the current MAC address of the device. Only 48-bit MAC Addresses
SHALL be used for this attribute as required by the Wake on LAN protocol.
Format of this attribute SHALL be an upper-case hex-encoded string representing the hex address,
12345678ABCD
like  .
1.12.4.2. LinkLocalAddress Attribute
This attribute SHALL indicate the current link-local address of the device. Only 128-bit IPv6 link-
local addresses SHALL be used for this attribute.
Some companies may consider MAC Address to be protected data subject to PII han
NOTE dling considerations and will therefore choose not to include it or read it. The MAC
Address can often be determined using ARP in IPv4 or NDP in IPv6.