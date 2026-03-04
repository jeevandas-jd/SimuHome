"""Utilities for wrapping simulator responses into HTTP-friendly payloads."""

from enum import IntEnum
from typing import Any, Dict, Optional

from src.simulator.domain.result import ErrorCode, Result


class HTTPStatus(IntEnum):
    """HTTP status code enumeration."""

    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    SERVICE_UNAVAILABLE = 503
    INTERNAL_SERVER_ERROR = 500


class ResponseBuilder:
    """Translate :class:`Result` values into HTTP response payloads."""

    @staticmethod
    def from_result(result: Result) -> Dict[str, Any]:
        """Build a standard HTTP response from a :class:`Result`."""

        if result.success:
            return ResponseBuilder._build_success(result.get_data())

        code, _, detail = result.get_error_info()
        http_status = ResponseBuilder._map_error_to_http(code)
        return ResponseBuilder._build_error(
            http_status, code.value if code else "INTERNAL_ERROR", detail
        )

    @staticmethod
    def _build_success(data: Any = None, message: str = "OK") -> Dict[str, Any]:
        return {
            "status": {"code": HTTPStatus.OK, "message": message},
            "data": data,
            "error": None,
        }

    @staticmethod
    def _build_error(
        http_code: int, error_type: str, detail: Optional[str]
    ) -> Dict[str, Any]:
        return {
            "status": {"code": http_code, "message": error_type},
            "data": None,
            "error": {"type": error_type, "detail": detail},
        }

    @staticmethod
    def _map_error_to_http(error_code: Optional[ErrorCode]) -> HTTPStatus:
        if error_code is None:
            return HTTPStatus.INTERNAL_SERVER_ERROR

        mapping = {
            
            ErrorCode.DEVICE_NOT_FOUND: HTTPStatus.NOT_FOUND,
            ErrorCode.ROOM_NOT_FOUND: HTTPStatus.NOT_FOUND,
            ErrorCode.CLUSTER_NOT_FOUND: HTTPStatus.NOT_FOUND,
            ErrorCode.ENDPOINT_NOT_FOUND: HTTPStatus.NOT_FOUND,
            ErrorCode.ATTRIBUTE_NOT_FOUND: HTTPStatus.NOT_FOUND,
            ErrorCode.COMMAND_NOT_FOUND: HTTPStatus.NOT_FOUND,
            
            ErrorCode.COMMAND_EXECUTION_ERROR: HTTPStatus.BAD_REQUEST,
            ErrorCode.COMMAND_INVALID_ARGS: HTTPStatus.BAD_REQUEST,
            ErrorCode.ATTRIBUTE_WRITE_ERROR: HTTPStatus.BAD_REQUEST,
            ErrorCode.ATTRIBUTE_INVALID_VALUE: HTTPStatus.BAD_REQUEST,
            ErrorCode.INVALID_ARGUMENT: HTTPStatus.BAD_REQUEST,
            ErrorCode.CONSTRAINT_ERROR: HTTPStatus.BAD_REQUEST,
            ErrorCode.UNSUPPORTED_MODE: HTTPStatus.BAD_REQUEST,
            ErrorCode.INVALID_IN_MODE: HTTPStatus.BAD_REQUEST,
            ErrorCode.UNSUPPORTED_COMMAND: HTTPStatus.BAD_REQUEST,
            ErrorCode.READ_ONLY: HTTPStatus.BAD_REQUEST,
            ErrorCode.VALIDATION_ERROR: HTTPStatus.BAD_REQUEST,
            ErrorCode.DEPENDENCY_VIOLATION: HTTPStatus.BAD_REQUEST,
            
            ErrorCode.INVALID_STATE: HTTPStatus.CONFLICT,
            
            ErrorCode.DEVICE_ALREADY_EXISTS: HTTPStatus.CONFLICT,
            
            ErrorCode.TIMEOUT_ERROR: HTTPStatus.REQUEST_TIMEOUT,
            
            ErrorCode.CONNECTION_ERROR: HTTPStatus.SERVICE_UNAVAILABLE,
            
            ErrorCode.HTTP_ERROR: HTTPStatus.BAD_REQUEST,
        }

        return mapping.get(error_code, HTTPStatus.INTERNAL_SERVER_ERROR)
