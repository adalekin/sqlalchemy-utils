from enum import Enum


def values_callable_default(enum_: Enum):
    return [enum_item.value for enum_item in enum_]
