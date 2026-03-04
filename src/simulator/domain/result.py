from typing import Any, Optional
from dataclasses import dataclass
from enum import Enum


class ErrorCode(Enum):
    

    COMMAND_NOT_FOUND = "COMMAND_NOT_FOUND"
    COMMAND_EXECUTION_ERROR = "COMMAND_EXECUTION_ERROR"
    COMMAND_INVALID_ARGS = "COMMAND_INVALID_ARGS"

    ATTRIBUTE_NOT_FOUND = "ATTRIBUTE_NOT_FOUND"
    ATTRIBUTE_WRITE_ERROR = "ATTRIBUTE_WRITE_ERROR"
    ATTRIBUTE_INVALID_VALUE = "ATTRIBUTE_INVALID_VALUE"
    READ_ONLY = "READ_ONLY"

    DEVICE_NOT_FOUND = "DEVICE_NOT_FOUND"
    ROOM_NOT_FOUND = "ROOM_NOT_FOUND"
    CLUSTER_NOT_FOUND = "CLUSTER_NOT_FOUND"
    ENDPOINT_NOT_FOUND = "ENDPOINT_NOT_FOUND"

    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DEPENDENCY_VIOLATION = "DEPENDENCY_VIOLATION"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    HTTP_ERROR = "HTTP_ERROR"
    DEVICE_ALREADY_EXISTS = "DEVICE_ALREADY_EXISTS"

    
    UNSUPPORTED_COMMAND = "UNSUPPORTED_COMMAND"
    INVALID_ARGUMENT = "INVALID_ARGUMENT"
    INVALID_STATE = "INVALID_STATE"
    CONSTRAINT_ERROR = "CONSTRAINT_ERROR"

    
    SUCCESS = "SUCCESS"
    UNSUPPORTED_MODE = "UNSUPPORTED_MODE"
    INVALID_IN_MODE = "INVALID_IN_MODE"


@dataclass(frozen=True)
class Result:
    

    success: bool
    data: Optional[Any] = None
    error_code: Optional[ErrorCode] = None
    error_message: Optional[str] = None
    error_detail: Optional[str] = None

    @classmethod
    def ok(cls, data: Any = None) -> "Result":
        
        return cls(success=True, data=data)

    @classmethod
    def fail(
        cls,
        error_code: ErrorCode,
        error_message: str,
        error_detail: Optional[str] = None,
    ) -> "Result":
        
        return cls(
            success=False,
            error_code=error_code,
            error_message=error_message,
            error_detail=error_detail or error_message,
        )

    def __bool__(self) -> bool:
        
        return self.success

    def get_data(self) -> Any:
        
        return self.data if self.success else None

    def get_error_info(
        self,
    ) -> tuple[Optional[ErrorCode], Optional[str], Optional[str]]:
        
        return (self.error_code, self.error_message, self.error_detail)


class ResultBuilder:
    

    @staticmethod
    def device_not_found(device_id: str) -> Result:
        return Result.fail(
            ErrorCode.DEVICE_NOT_FOUND,
            "Device not found",
            f"Device with ID '{device_id}' does not exist.",
        )

    @staticmethod
    def command_not_found(command_id: str, cluster_id: str) -> Result:
        return Result.fail(
            ErrorCode.COMMAND_NOT_FOUND,
            "Command not found",
            f"Command '{command_id}' does not exist in cluster '{cluster_id}'.",
        )

    @staticmethod
    def command_invalid_args(command_id: str, reason: str) -> Result:
        return Result.fail(
            ErrorCode.COMMAND_INVALID_ARGS,
            f"Invalid arguments for command '{command_id}'",
            reason,
        )

    @staticmethod
    def attribute_not_found(attribute_id: str, cluster_id: str) -> Result:
        return Result.fail(
            ErrorCode.ATTRIBUTE_NOT_FOUND,
            "Attribute not found",
            f"Attribute '{attribute_id}' does not exist in cluster '{cluster_id}'.",
        )

    @staticmethod
    def cluster_not_found(cluster_id: str) -> Result:
        return Result.fail(
            ErrorCode.CLUSTER_NOT_FOUND,
            "Cluster not found",
            f"Cluster '{cluster_id}' does not exist on the target endpoint.",
        )

    @staticmethod
    def endpoint_not_found(endpoint_id: int) -> Result:
        return Result.fail(
            ErrorCode.ENDPOINT_NOT_FOUND,
            "Endpoint not found",
            f"Endpoint '{endpoint_id}' does not exist on the target device.",
        )

    @staticmethod
    def internal_error(error: Exception) -> Result:
        error_type = type(error).__name__
        return Result.fail(
            ErrorCode.INTERNAL_ERROR,
            "An internal error occurred",
            f"Internal server error ({error_type})",
        )
