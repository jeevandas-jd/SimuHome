
# 8.10 Oven Cavity Operational State Cluster

This cluster is derived from the Operational State cluster and provides an interface for monitoring
the operational state of an oven.

## Attributes
8.10.4.1. PhaseList Attribute
As defined in the base cluster, this attribute indicates a list of names of different phases that the
device can go through for the selected function or mode.
For this derived cluster, only these pre-defined strings may be used in the PhaseList attribute:
"pre-heating", "pre-heated", and "cooling down".
Other values SHALL NOT be used.
As defined in the base cluster, a null value indicates that the device does not present phases during
its operation. When this attribute’s value is null, the CurrentPhase attribute SHALL also be set to
null.

## Commands

_Table parsed from section 'Commands':_

* In the context of the Oven Cavity Operational State Cluster, specifically within the Commands section, the table row describes a command identified by the ID '0x00' and named 'Pause'. The conformance rule for this command is 'X', which means it is explicitly disallowed. This indicates that within the current Matter specification, the 'Pause' command cannot be implemented or used in any device or application that adheres to this cluster's standards.

* The table row describes a command within the Oven Cavity Operational State Cluster, specifically the "Stop" command, identified by the ID '0x01'. According to the Matter Conformance Interpretation Guide, the conformance rules for this command are not explicitly provided in the data snippet. However, if we assume a typical scenario where no specific conformance expression is given, the command's inclusion would generally depend on the default rules or additional context from the specification. If the conformance were to follow a basic tag like 'M', it would mean the "Stop" command is mandatory for any device implementing this cluster. If it were 'O', it would be optional. Without explicit conformance data, we would need to refer to the broader specification or additional documentation for precise requirements.

* The table row pertains to the "Start" command within the Oven Cavity Operational State Cluster, specifically under the Commands section. The conformance rule for this command is not explicitly provided in the data snippet, but based on the Matter Conformance Interpretation Guide, we would interpret the conformance string to determine when this command is required. For instance, if the conformance were "M," it would mean the "Start" command is mandatory and must always be implemented. If it were "O," the command would be optional with no dependencies. If the conformance were a logical condition or a chain of conditions, it would specify under what circumstances the command is mandatory, optional, deprecated, or disallowed. Without the specific conformance string, we can only outline potential interpretations based on the guide.

* In the context of the Oven Cavity Operational State Cluster, specifically within the Commands section, the table row describes a command identified by the ID '0x03' and named 'Resume'. The conformance rule for this command is marked as 'X', which means that the 'Resume' command is explicitly disallowed according to the Matter IoT specification. This indicates that the command should not be implemented or used in any devices or applications that adhere to this specification.

_Table parsed from section 'Commands':_

* The table row entry for the "OperationalCommandResponse" command within the "Oven Cavity Operational State Cluster" pertains to the commands section of the Matter specification. The conformance rule for this entry is not explicitly provided in the data you shared, so I will assume it is missing or needs clarification. Generally, the conformance rule would dictate whether this command is mandatory, optional, provisional, deprecated, or disallowed based on specific conditions or features. For example, if the conformance were `M`, it would mean that the "OperationalCommandResponse" command is always required for devices implementing this cluster. If it were `O`, the command would be optional, allowing flexibility in implementation. Without the specific conformance string, we cannot determine the exact requirement status of this command. If you have the conformance string, please provide it for a more precise interpretation.

