
# 1.11 Low Power Cluster

This cluster provides an interface for managing low power mode on a device.
This cluster would be supported on an endpoint that represents a physical device with a low power
mode. This cluster provides a sleep() command to allow clients to manually put the device into low
power mode. There is no command here to wake up a sleeping device because that operation often
involves other protocols such as Wake On LAN. Most devices automatically enter low power mode
based upon inactivity.
The cluster server for Low Power is implemented by a device that supports a low power mode, such
as a TV, Set-top box, or Smart Speaker.
We have considered a “DisableLowPowerMode” command but have not added it
NOTE due to suspected issues with energy consumption regulations. This can be added in
the future.

## Commands

_Table parsed from section 'Commands':_

* The table row describes a command within the Low Power Cluster, specifically the "Sleep" command, which is directed from the client to the server. The command has an ID of '0x00' and requires a response, as indicated by 'Response: Y'. The access level is optional ('Access: O'), meaning that while the command can be accessed, it is not required to be implemented by default. The conformance rule for this command is 'M', which signifies that the "Sleep" command is mandatory. This means that any implementation of the Low Power Cluster must include this command, ensuring that it is always available for use in the specified client-server direction.

1.11.4.1. Sleep Command
This command SHALL put the device into low power mode.