
# 6.2 Account Login Cluster

This cluster provides commands that facilitate user account login on a Content App or a node. For
example, a Content App running on a Video Player device, which is represented as an endpoint (see
Device Type Library document), can use this cluster to help make the user account on the Content
App match the user account on the Client.
Often a fabric administrator will facilitate commissioning of a Client (such as a Casting Video
Client), and invoke commands on the AccountLogin cluster on the Content App associated with that
client. Specifically:
1. GetSetupPIN in order to attempt to obtain the Passcode for commissioning.
2. Login in order to let the Content App know that commissioning has completed. The Content App
can use information provided in this command in order to determine the user account associ
ated with the client, and potentially assume that user account.
3. Logout in order to let the Content App know that client access has been removed, and poten
tially clear the current user account.
The cluster server for this cluster may be supported on each endpoint that represents a Content
App on a Video Player device.
See Device Type Library document for details of how a Content App, represented as an endpoint on
the Video Player device, may implement the cluster server for this cluster to simplify account login
for its users.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Account Login Cluster, specifically the "GetSetupPIN" command. This command is initiated by the client and directed towards the server, with an expected response of "GetSetupPINResponse." The access control for this command is denoted by the codes 'A F T,' which likely refer to specific access requirements or roles defined elsewhere in the specification. The conformance rule for this command is marked as 'M,' indicating that it is mandatory. This means that the "GetSetupPIN" command must always be implemented and supported in any device or application that includes the Account Login Cluster, without any conditions or exceptions.

* The table row describes a command within the Account Login Cluster, specifically the "GetSetupPINResponse" command. This command is identified by the ID '0x01' and is directed from the server to the client, as indicated by the direction 'client ⇐ server'. It does not require a response ('Response': 'N') and has an access level of 'F', which typically denotes a specific access control requirement. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "GetSetupPINResponse" command must always be implemented and supported in any device or application utilizing the Account Login Cluster, without any conditions or exceptions.

* The table row describes a command within the Account Login Cluster, specifically the "Login" command, which is identified by the ID '0x02'. This command is directed from the client to the server, and it requires a response, as indicated by 'Response: Y'. The access control for this command is defined by the flags 'A F T'. The conformance rule for this command is 'M', which means it is mandatory. This indicates that the "Login" command must always be implemented and supported in any device or application that utilizes the Account Login Cluster, without any conditions or exceptions.

* The table row describes a command within the Account Login Cluster, specifically the "Logout" command, which is identified by the ID '0x03'. This command is directed from the client to the server and requires a response ('Y'). The access level for this command is marked as 'O F T', indicating specific access control requirements that are not detailed here. The conformance rule for this command is 'M', meaning it is mandatory. This indicates that the "Logout" command must always be implemented in any device or application that supports the Account Login Cluster, without any conditions or exceptions.

6.2.4.1. GetSetupPIN Command
The purpose of this command is to determine if the active user account of the given Content App
matches the active user account of a given Commissionee, and when it does, return a Setup PIN
code which can be used for password-authenticated session establishment (PASE) with the Commis
sionee.
For example, a Video Player with a Content App Platform may invoke this command on one of its
Content App endpoints to facilitate commissioning of a Phone App made by the same vendor as the
Content App. If the accounts match, then the Content App may return a setup code that can be used
by the Video Player to commission the Phone App without requiring the user to physically input a
setup code.
The account match is determined by the Content App using a method which is outside the scope of
this specification and will typically involve a central service which is in communication with both
the Content App and the Commissionee. The GetSetupPIN command is needed in order to provide
the Commissioner/Admin with a Setup PIN when this Commissioner/Admin is operated by a differ
ent vendor from the Content App.
This method is used to facilitate Setup PIN exchange (for PASE) between Commissioner and Com
missionee when the same user account is active on both nodes. With this method, the Content App
satisfies proof of possession related to commissioning by requiring the same user account to be
active on both Commissionee and Content App, while the Commissioner/Admin ensures user con
sent by prompting the user prior to invocation of the command.
Upon receipt of this command, the Content App checks if the account associated with the Tempo
rary Account Identifier sent by the client is the same account that is active on itself. If the accounts
are the same, then the Content App returns the GetSetupPIN Response which includes a Setup PIN
that may be used for PASE with the Commissionee.
The Temporary Account Identifier for a Commissionee may be populated with the Rotating ID field
of the client’s commissionable node advertisement (see Rotating Device Identifier section in [Mat
terCore]) encoded as an octet string where the octets of the Rotating Device Identifier are encoded
as 2-character sequences by representing each octet’s value as a 2-digit hexadecimal number, using
uppercase letters.
The Setup PIN is a character string so that it can accommodate different future formats, including
alpha-numeric encodings. For a Commissionee it SHALL be populated with the Manual Pairing
Code (see Manual Pairing Code section in [MatterCore]) encoded as a string (11 characters) or the
Passcode portion of the Manual Pairing Code (when less than 11 characters) .
The server SHALL implement rate limiting to prevent brute force attacks. No more than 10 unique
requests in a 10 minute period SHALL be allowed; a command response status of FAILURE should
sent for additional commands received within the 10 minute period. Because access to this com
mand is limited to nodes with Admin-level access, and the user is prompted for consent prior to
Commissioning, there are in place multiple obstacles to successfully mounting a brute force attack.
A Content App that supports this command SHALL ensure that the Temporary Account Identifier
used by its clients is not valid for more than 10 minutes.

_Table parsed from section 'Commands':_

* In the Account Login Cluster, under the Commands section, the entry for 'TempAccountIdentifier' is identified by the ID '0' and is of the type 'string'. This command has a constraint that requires its length to be between 16 and 100 characters. The conformance rule for 'TempAccountIdentifier' is marked as 'M', which means it is mandatory. This indicates that the 'TempAccountIdentifier' command must always be implemented and supported in any device or system that includes the Account Login Cluster, without any conditions or exceptions.

6.2.4.1.1. TempAccountIdentifier Field
This field SHALL specify the client’s Temporary Account Identifier. The length of this field SHALL
be at least 16 characters to protect the account holder against password guessing attacks.
6.2.4.2. GetSetupPINResponse Command
This message is sent in response to the GetSetupPIN command, and contains the Setup PIN code, or
null when the account identified in the request does not match the active account of the running
Content App.

_Table parsed from section 'Commands':_

* The table row describes a command within the Account Login Cluster, specifically the "SetupPIN" command, which is identified by the ID '0' and is of the type 'string'. The constraint for this command is described elsewhere in the documentation, as indicated by 'desc'. The conformance rule 'M' signifies that the "SetupPIN" command is mandatory, meaning it is always required to be implemented in any device or application that supports the Account Login Cluster. This ensures that the command is consistently available across all implementations of this cluster, providing a standardized method for setting up a PIN.

6.2.4.2.1. SetupPIN Field
This field SHALL provide the setup PIN code as a text string at least 8 characters in length or empty
string to indicate that the accounts do not match.
Newer cluster clients should be aware that AccountLogin cluster version 1 specified
NOTE
an 11 digit minimum length.
6.2.4.3. Login Command
The purpose of this command is to allow the Content App to assume the user account of a given
Commissionee by leveraging the Setup PIN code input by the user during the commissioning
process.
For example, a Video Player with a Content App Platform may invoke this command on one of its
Content App endpoints after the commissioning has completed of a Phone App made by the same
vendor as the Content App. The Content App may determine whether the Temporary Account Iden
tifier maps to an account with a corresponding Setup PIN and, if so, it may automatically login to
the account for the corresponding user. The end result is that a user performs commissioning of a
Phone App to a Video Player by inputting the Setup PIN for the Phone App into the Video Player UX.
Once commissioning has completed, the Video Player invokes this command to allow the corre
sponding Content App to assume the same user account as the Phone App.
The verification of Setup PIN for the given Temporary Account Identifier is determined by the Con
tent App using a method which is outside the scope of this specification and will typically involve a
central service which is in communication with both the Content App and the Commissionee.
Implementations of such a service should impose aggressive time outs for any mapping of Tempo
rary Account Identifier to Setup PIN in order to prevent accidental login due to delayed invocation.
Upon receipt, the Content App checks if the account associated with the client’s Temp Account Iden
tifier has a current active Setup PIN with the given value. If the Setup PIN is valid for the user
account associated with the Temp Account Identifier, then the Content App MAY make that user
account active.
The Temporary Account Identifier for a Commissionee may be populated with the Rotating ID field
of the client’s commissionable node advertisement encoded as an octet string where the octets of
the Rotating Device Identifier are encoded as 2-character sequences by representing each octet’s
value as a 2-digit hexadecimal number, using uppercase letters.
The Setup PIN for a Commissionee may be populated with the Manual Pairing Code encoded as a
string of decimal numbers (11 characters) or the Passcode portion of the Manual Pairing Code
encoded as a string of decimal numbers (8 characters) .
The server SHALL implement rate limiting to prevent brute force attacks. No more than 10 unique
requests in a 10 minute period SHALL be allowed; a command response status of FAILURE should
sent for additional commands received within the 10 minute period. Because access to this com
mand is limited to nodes with Admin-level access, and the user is involved when obtaining the
SetupPIN, there are in place multiple obstacles to successfully mounting a brute force attack. A Con
tent App that supports this command SHALL ensure that the Temporary Account Identifier used by
its clients is not valid for more than 10 minutes.

_Table parsed from section 'Commands':_

* The table row describes a command within the Account Login Cluster, specifically the "TempAccountIdentifier" command. This command is of the type "string" and must adhere to a constraint where its length is between 16 and 100 characters. The conformance rule for this command is denoted by "M," which means it is mandatory. Therefore, the "TempAccountIdentifier" command is always required to be implemented in any device or application that supports the Account Login Cluster, without any conditions or exceptions.

* The table row describes a command within the Account Login Cluster, specifically the "SetupPIN" command. This command is identified by the ID '1' and is of the type 'string', with a constraint that requires a minimum length of 8 characters. The conformance rule for this command is marked as 'M', which means it is mandatory. This indicates that the "SetupPIN" command must always be implemented in any device or application that supports the Account Login Cluster, without any conditions or exceptions.

* In the context of the Account Login Cluster, specifically within the Commands section, the table row describes an element with the ID '2' and the name 'Node', which is of the type 'node-id'. The conformance rule for this element is 'O', indicating that the 'Node' command is optional. This means that the implementation of this command is not required and there are no dependencies or conditions that affect its optional status. Developers have the discretion to include or exclude this command in their implementation of the Account Login Cluster without impacting compliance with the Matter specification.

6.2.4.3.1. TempAccountIdentifier Field
This field SHALL specify the client’s temporary account identifier.
6.2.4.3.2. SetupPIN Field
This field SHALL provide the setup PIN code as a text string at least 8 characters in length.
Newer cluster clients should be aware that AccountLogin cluster version 1 specified
NOTE
an 11 digit minimum length.
6.2.4.3.3. Node Field
This optional field SHALL provide the Node ID of the Client. This field can be used by the Content
App to keep track of Nodes which currently have access to it.
6.2.4.4. Logout Command
The purpose of this command is to instruct the Content App to clear the current user account. This
command SHOULD be used by clients of a Content App to indicate the end of a user session.

_Table parsed from section 'Commands':_

* In the Account Login Cluster, within the Commands section, the table row describes a command identified by 'ID' 0, named 'Node', which is of the type 'node-id'. The 'Conformance' for this command is marked as 'O', indicating that it is Optional. This means that the 'Node' command is not required to be implemented and has no dependencies or conditions that affect its inclusion. Implementers of the Account Login Cluster can choose to include this command at their discretion, but it is not necessary for compliance with the Matter specification.

6.2.4.4.1. Node Field
This optional field SHALL provide the Node ID of the Client. This field can be used by the Content
App to keep track of Nodes which currently have access to it.

## Events

_Table parsed from section 'Events':_

* The table row describes an event named "LoggedOut" within the Account Login Cluster, specifically under the Events section. This event has an ID of '0' and is classified with a priority level of 'CRITICAL', indicating its high importance. The access level is denoted as 'A S', which typically refers to specific access permissions required for this event. The conformance rule for the "LoggedOut" event is marked as 'O', meaning it is optional. This indicates that the implementation of this event is not required and does not depend on any other features or conditions within the Matter specification.

6.2.5.1. LoggedOut Event
This event can be used by the Content App to indicate that the current user has logged out. In
response to this event, the Fabric Admin SHALL remove access to this Content App by the specified
Node. If no Node is provided, then the Fabric Admin SHALL remove access to all non-Admin Nodes.
The data of this event SHALL contain the following information:

_Table parsed from section 'Events':_

* In the context of the Account Login Cluster, specifically within the Events section, the table row describes an event identified as 'Node' with an ID of '0' and a type of 'node-id'. The constraint for this event is labeled as 'all', indicating it applies universally within its context. The conformance rule for this event is marked as 'O', meaning that the inclusion of the 'Node' event is optional. This implies that while the event can be implemented, it is not required and does not depend on any other features or conditions within the Matter specification.

6.2.5.1.1. Node
This field SHALL provide the Node ID corresponding to the user account that has logged out, if that
Node ID is available. If it is NOT available, this field SHALL NOT be present in the event.