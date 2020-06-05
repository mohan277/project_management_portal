

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "from_state": "string",
    "to_state": "string"
}
"""


RESPONSE_200_JSON = """
{
    "name": "string",
    "transition_id": 1,
    "description": "string",
    "from_state": {
        "name": "string",
        "from_state_id": 1
    },
    "to_state": {
        "name": "string",
        "to_state_id": 1
    }
}
"""

