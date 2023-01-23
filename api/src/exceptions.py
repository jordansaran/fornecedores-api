import functools
from http import HTTPStatus

from flask_restx import marshal, Namespace
from sqlalchemy.exc import OperationalError, IntegrityError

from api.src.constants import StatusAPI
from api.src.marshalls import marshall_api_response


class ExceptionsDatabase:
    """Exceptions Database to API"""

    namespace: Namespace

    def __init__(self, namespace: Namespace):
        self.namespace = namespace

    def exceptions(self, function: callable):
        """Exception to OperationalError on database"""
        namespace = self.namespace

        @functools.wraps(function)
        def type_exceptions(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except (OperationalError, IntegrityError) as _error:
                namespace.logger.error(_error)
                response, code = marshal(StatusAPI.INTERNAL_SERVER_ERROR_API, marshall_api_response), \
                    int(HTTPStatus.INTERNAL_SERVER_ERROR)
            return response, code
        return type_exceptions
