""""Utilities to API"""
from string import ascii_uppercase, digits
from random import choice


def random_string() -> str:
    """"Generate random ascii_uppercase+digit with 16 characters in format UPPER"""
    return ''.join(choice(ascii_uppercase + digits) for _ in range(16)).upper()


def httpstatus_to_api_response(http_status: tuple = None) -> dict | None:
    """Convert tuple from HTTPStatus to ApiResponse(dict)"""
    if http_status is None:
        return None
    try:
        return {
            'code': http_status[0],
            'type': http_status[1],
            'message': http_status[2],
        }
    except AttributeError as _error:
        return None
