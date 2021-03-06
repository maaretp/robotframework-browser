from enum import Enum, auto
from typing import TypedDict


class RequestMethod(Enum):
    HEAD = auto()
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()


class MouseButton(Enum):
    left = auto()
    middle = auto()
    right = auto()


class KeyboardModifier(Enum):
    Alt = auto()
    Control = auto()
    Meta = auto()
    Shift = auto()


class SelectAttribute(Enum):
    value = auto()
    label = auto()
    text = label
    index = auto()


class SupportedBrowsers(Enum):
    chromium = "chromium"
    firefox = "firefox"
    webkit = "webkit"


ColorScheme = Enum("ColorScheme", ["dark", "light", "no-preference"])

ViewportDimensions = TypedDict("ViewportDimensions", {"width": int, "height": int})


class ElementState(Enum):
    attached = auto()
    detached = auto()
    visible = auto()
    hidden = auto()


AssertionOperator = Enum(
    "AssertionOperator",
    {
        "equal": "==",
        "==": "==",
        "shouldbe": "==",
        "inequal": "!=",
        "!=": "!=",
        "shouldnotbe": "!=",
        "lessthan": "<",
        "<": "<",
        "greaterthan": ">",
        ">": ">",
        "<=": "<=",
        ">=": ">=",
        "contains": "*=",
        "*=": "*=",
        "starts": "^=",
        "^=": "^=",
        "shouldstartwith": "^=",
        "ends": "$=",
        "$=": "$=",
        "matches": "$",
        "validate": "validate",
        "then": "then",
        "evaluate": "then",
    },
)
