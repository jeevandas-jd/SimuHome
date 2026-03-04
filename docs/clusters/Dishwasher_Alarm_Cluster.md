
# 8.4 Dishwasher Alarm Cluster

This cluster is a derived cluster of the Alarm Base cluster and provides the alarm definition related
to dishwasher devices.

## Data Types
8.4.4.1. AlarmBitmap Type
This data type is derived from map32.

_Table parsed from section 'Data Types':_

* In the context of the Dishwasher Alarm Cluster's Data Types, the table row describes a feature named "InflowError," which is associated with bit '0' and indicates that there is an abnormal water inflow. The conformance rule for "InflowError" is specified as "P, O.a+." This means that currently, the feature is in a provisional state, suggesting that its status is temporary and may change in the future. Following the provisional status, the feature is considered optional, with the notation "O.a+" indicating that it is optional without any additional conditions or dependencies. Therefore, while the feature is not mandatory, it is available for implementation at the discretion of the device manufacturer or developer.

* In the context of the Dishwasher Alarm Cluster's Data Types, the table row describes a feature named "DrainError," which is associated with bit '1' and indicates an abnormal water draining condition. The conformance rule for "DrainError" is specified as "P, O.a+." This means that currently, the "DrainError" feature is in a provisional status, indicating that its conformance is temporary and subject to change. The provisional status suggests that it may become mandatory or change in the future. Following the provisional status, the feature is considered optional, as indicated by "O.a+," meaning it is not required and has no dependencies at this time.

* In the context of the Dishwasher Alarm Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '2', named 'DoorError'. This feature indicates an abnormal condition related to the door or door lock of the dishwasher. The conformance rule for 'DoorError' is specified as 'O.a+', which suggests that this feature is optional. The 'O' indicates that the feature is not required and has no dependencies, while the '.a+' suffix is not explicitly defined in the provided conformance interpretation guide. However, it typically implies a versioning or additional context-specific condition that might be detailed elsewhere in the documentation. In essence, 'DoorError' is an optional feature that manufacturers can choose to implement in their dishwasher alarm systems.

* In the context of the Dishwasher Alarm Cluster's Data Types, the table row describes a feature named "TempTooLow," which is associated with bit 3. This feature indicates an alarm condition where the dishwasher is unable to reach its normal operating temperature. The conformance rule for "TempTooLow" is expressed as "P, O.a+." This means that the feature is currently provisional, indicating that its status is temporary and may change in the future. Following the provisional status, the feature is considered optional, denoted by "O.a+," which suggests that it is not required and has no dependencies. The "a+" suffix in the conformance rule is not explicitly defined in the provided guide, but it typically implies additional conditions or notes that are described elsewhere in the documentation.

* In the context of the Dishwasher Alarm Cluster's Data Types, the table row describes a feature named "TempTooHigh," which is associated with bit 4 and indicates that the temperature is too high. The conformance rule for this feature is "P, O.a+." This means that the "TempTooHigh" feature is currently provisional, indicating that its status is temporary and subject to change. In the future, it might become mandatory or have another defined conformance status. If the provisional status is not applicable, the feature is optional, as indicated by the "O" in the conformance rule. The ".a+" suffix suggests that there might be additional context or conditions described elsewhere in the documentation that further clarify when this feature is optional.

* In the context of the Dishwasher Alarm Cluster, specifically within the Data Types section, the table row describes a feature identified by the bit '5', named 'WaterLevelError', which indicates an abnormal water level condition. The 'Conformance' field for this feature is specified as 'P, O.a+'. This means that the 'WaterLevelError' feature is currently provisional, indicating that its status is temporary and may change in the future. The 'O.a+' part suggests that, after its provisional phase, it will become optional with additional conditions or annotations specified elsewhere in the documentation. Therefore, while it is not mandatory at this time, its future conformance may be subject to further specification or conditions.

