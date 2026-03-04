
# 10.2 Wi-Fi Network Management Cluster

This cluster provides an interface for getting information about the Wi-Fi network that a Network
Infrastructure Manager device type provides. Privileged nodes within the same fabric as a Network
Infrastructure Manager can use these interfaces to request information related to the Wi-Fi Net
work such as SSID and Passphrase.

## Attributes

_Table parsed from section 'Attributes':_

* The table row describes an attribute within the Wi-Fi Network Management Cluster, specifically the "SSID" attribute. This attribute has an ID of '0x0000' and is of type 'octstr', meaning it is an octet string. It has a constraint that limits its length to between 1 and 32 characters. The 'Quality' field is marked as 'XN', indicating specific quality characteristics, and its default value is 'null'. The 'Access' field is 'R V', which means it is readable and can be viewed. The 'Conformance' field is marked as 'M', which, according to the Matter Conformance Interpretation Guide, signifies that the SSID attribute is mandatory. This means that the SSID attribute is always required to be implemented in any device that supports the Wi-Fi Network Management Cluster, with no conditions or exceptions.

* The table row describes an attribute named "PassphraseSurrogate" within the Wi-Fi Network Management Cluster, identified by the ID '0x0001'. This attribute is of type 'uint64', with a constraint applicable to all instances, and it has a default value of 'null'. The access level for this attribute is 'R M', indicating it is readable and mandatory. The conformance rule 'M' signifies that the "PassphraseSurrogate" attribute is mandatory, meaning it is always required to be implemented in any device or application that supports this cluster. The quality 'XN' indicates that this attribute is explicitly disallowed in certain contexts, but the conformance rule ensures its presence where applicable.

10.2.4.1. SSID Attribute
This attribute SHALL indicate the SSID of the primary Wi-Fi network provided by this device.
A value of null SHALL indicate that no primary Wi-Fi network is available (e.g. because the Wi-Fi
network has not yet been configured by the user).
The SSID in Wi-Fi is a collection of 1-32 bytes, the text encoding of which is not spec
ified. Implementations must be careful to support transferring these byte strings
NOTE without requiring a particular encoding. The most common encoding is UTF-8, how
ever this is just a convention. Some configurations may use Latin-1 or other charac
ter sets.
10.2.4.2. PassphraseSurrogate Attribute
This attribute SHALL contain an arbitrary numeric value; this value SHALL increase whenever the
passphrase or PSK associated with the primary Wi-Fi network provided by this device changes.
A value of null SHALL indicate that no primary Wi-Fi network is available.
Clients can subscribe to this attribute or compare its value to a locally cached copy to detect if a
cached passphrase value has become stale.
It is RECOMMENDED that servers implement this attribute as either a timestamp or a counter.
When implemented as a counter it SHOULD be initialized with a random value.
The  passphrase  itself  is  not  exposed  as  an  attribute  to  avoid  its  unintentional
retrieval or caching by clients that use wildcard reads or otherwise routinely read
NOTE
all available attributes. It can be retrieved using the NetworkPassphraseRequest
command.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Wi-Fi Network Management Cluster, specifically the "NetworkPassphraseRequest" command. This command is initiated by the client and directed towards the server, expecting a "NetworkPassphraseResponse" in return. The access level for this command is marked as "M," indicating that it is mandatory for the client to have access to this command. The conformance rule for this command is also "M," which means that the "NetworkPassphraseRequest" command is a mandatory feature of the Wi-Fi Network Management Cluster. This implies that any implementation of this cluster must include this command as a required element, without any conditional dependencies or optional status.

* The table row describes a command within the Wi-Fi Network Management Cluster, specifically the "NetworkPassphraseResponse" command. This command is identified by the ID '0x01' and is directed from the server to the client, as indicated by the direction 'client ⇐ server'. The 'Response' field marked as 'N' suggests that this command does not expect a response. The conformance rule for this command is 'M', which means it is mandatory. This implies that the "NetworkPassphraseResponse" command must always be implemented and supported in any device or application utilizing the Wi-Fi Network Management Cluster, without any conditions or exceptions.

10.2.5.1. NetworkPassphraseRequest Command
This command is used to request the current WPA-Personal passphrase or PSK associated with the
Wi-Fi network provided by this device.
If the command is not executed via a CASE session, the command SHALL be rejected with a status
of UNSUPPORTED_ACCESS.
If no primary Wi-Fi network is available (the SSID attribute is null), the command SHALL be
rejected with a status of INVALID_IN_STATE.
Otherwise a NetworkPassphraseResponse SHALL be generated.
10.2.5.2. NetworkPassphraseResponse Command
This command SHALL be generated in response to a NetworkPassphraseRequest command. The
data for this command SHALL be as follows:

_Table parsed from section 'Commands':_

* In the Wi-Fi Network Management Cluster, under the Commands section, the entry for 'Passphrase' is defined with a type of 'octstr' and a constraint of a maximum length of 64 characters. The conformance rule for this entry is 'M', which stands for Mandatory. This means that the 'Passphrase' command is always required to be implemented in any device or application that supports the Wi-Fi Network Management Cluster, without any conditions or exceptions.

10.2.5.2.1. Passphrase Field
This field SHALL indicate the current WPA-Personal passphrase or PSK associated with the primary
Wi-Fi network provided by this device, in one of the following formats:
• 8..63 bytes: WPA/WPA2/WPA3 passphrase.
• 64 bytes: WPA/WPA2/WPA3 raw hex PSK. Each byte SHALL be a ASCII hexadecimal digit.
This matches the formats defined for WPA networks by the Credentials field in the Network Com
missioning cluster (see [MatterCore]).
WPA3-Personal permits passphrases shorter than 8 or longer than 63 characters,
NOTE however the Network Commissioning cluster does not currently support configur
ing Matter devices to connect to operational networks utilizing such a passphrase.