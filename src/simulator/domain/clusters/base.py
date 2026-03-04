import inspect
from typing import Any
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


class Cluster:
    def __init__(self, cluster_id: str):
        self.cluster_id = cluster_id
        self.attributes = {}
        self.commands = {}
        self.readonly_attributes = (
            set()
        )

    def execute_command(self, command_id: str, **args) -> Result:
        if command_id not in self.commands:
            available_commands = list(self.commands.keys())
            return Result.fail(
                error_code=ErrorCode.COMMAND_NOT_FOUND,
                error_message=f"Command '{command_id}' not found in cluster '{self.cluster_id}'",
                error_detail=f"Available commands: {available_commands}",
            )

        try:

            command_func = self.commands[command_id]
            result = command_func(**args)


            if isinstance(result, Result):
                return result

            if isinstance(result, bool):
                if result is True:
                    return Result.ok(
                        {
                            "cluster": self.cluster_id,
                            "command": command_id,
                            "success": True,
                        }
                    )
                else:
                    return Result.fail(
                        error_code=ErrorCode.COMMAND_EXECUTION_ERROR,
                        error_message=f"Command '{command_id}' failed in cluster '{self.cluster_id}'",
                        error_detail="Command returned False",
                    )

            return Result.ok(
                {"cluster": self.cluster_id, "command": command_id, "result": result}
            )
        except TypeError as error:

            command_func = self.commands[command_id]
            sig = inspect.signature(command_func)
            expected_params = []
            for param_name, param in sig.parameters.items():
                if param_name != "self":
                    param_info = param_name
                    if param.annotation != inspect.Parameter.empty:
                        param_info += f": {param.annotation.__name__ if hasattr(param.annotation, '__name__') else str(param.annotation)}"
                    if param.default != inspect.Parameter.empty:
                        param_info += f" = {param.default}"
                    expected_params.append(param_info)

            return Result.fail(
                error_code=ErrorCode.COMMAND_EXECUTION_ERROR,
                error_message=f"Invalid arguments for command '{command_id}' in cluster '{self.cluster_id}'",
                error_detail=f"Expected parameters: {expected_params}. Provided: {list(args.keys())}. Error: {str(error)}",
            )
        except Exception as error:
            return ResultBuilder.internal_error(error)

    def write_attribute(self, attribute_id: str, value: Any) -> Result:
        if attribute_id not in self.attributes:
            return ResultBuilder.attribute_not_found(
                attribute_id=attribute_id, cluster_id=self.cluster_id
            )


        if attribute_id in self.readonly_attributes:
            return Result.fail(
                ErrorCode.READ_ONLY,
                f"Attribute '{attribute_id}' is read-only",
                f"Attribute '{attribute_id}' in cluster '{self.cluster_id}' is managed by environment aggregator",
            )

        old_value = self.attributes.get(attribute_id)
        self.attributes[attribute_id] = value
        return Result.ok(
            {
                "cluster": self.cluster_id,
                "attribute": attribute_id,
                "old_value": old_value,
                "new_value": value,
            }
        )

    def get_structure(self) -> dict[str, Any]:
        
        from enum import Enum

        attributes_schema = {}
        for attr_id, value in self.attributes.items():
            attr_info = {"value": value}
            if isinstance(value, Enum):
                attr_info["type"] = "enum"
                attr_info["enum_name"] = value.__class__.__name__
                attr_info["enum_values"] = {
                    member.name: member.value for member in value.__class__
                }
            else:
                attr_info["type"] = type(value).__name__
            attr_info["readonly"] = attr_id in self.readonly_attributes
            attributes_schema[attr_id] = attr_info

        return {
            "cluster_id": self.cluster_id,
            "attributes": attributes_schema,
            "commands": list(self.commands.keys()),
        }


    def blocks_exact_batch_advance(self) -> bool:
        return True
