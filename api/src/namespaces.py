""""Namespaces with resources to API"""
from flask_restx import Namespace
import functools
from http import HTTPStatus
from flask_restx import Resource, marshal
from api.src.constants import StatusAPI
from api.src.controllers import ProviderController
from api.src.exceptions import ExceptionsDatabase
from api.src.marshalls import marshall_api_response, marshall_provider
from api.src.models import Provider


ns_provider = Namespace(name="Fornecedor",
                        description="Informações sobre Fornecedores.",
                        validate=True,
                        path='/providers')
ns_provider.models.update({marshall_provider.name: marshall_provider})
ns_provider.models.update({marshall_api_response.name: marshall_api_response})


@ns_provider.route("/<string:id>")
@ns_provider.response(int(HTTPStatus.BAD_REQUEST),
                      'Fornecedor inválido',
                      marshall_api_response)
@ns_provider.response(int(HTTPStatus.NOT_FOUND),
                      'Fornecedor não encontrado',
                      marshall_api_response)
class Providers(Resource):
    """ Handles HTTP requests to URL: /providers """

    exceptions_database: ExceptionsDatabase = ExceptionsDatabase(namespace=ns_provider)

    @staticmethod
    def check_path_id(function: callable):
        """To valid id on path in request"""
        @functools.wraps(function)
        def is_valid(*args, **kwargs):
            if ProviderController().is_valid(kwargs.get('id')):
                return function(*args, **kwargs)
            return marshal(StatusAPI.BAD_REQUEST_API, marshall_api_response), \
                int(HTTPStatus.BAD_REQUEST)
        return is_valid

    @check_path_id
    @exceptions_database.exceptions
    @ns_provider.response(int(HTTPStatus.OK),
                          "Fornecedor encontrado com sucesso.",
                          marshall_provider)
    def get(self, id: str = None):
        """Obter dados do Fornecedor a partir do ID"""
        provider = Provider.find_by_id(id)
        if provider is not None:
            return marshal(provider.__dict__, marshall_provider), int(HTTPStatus.OK)
        return marshal(StatusAPI.REQUEST_NOT_FOUND_API, marshall_api_response), int(HTTPStatus.NOT_FOUND)

    @check_path_id
    @exceptions_database.exceptions
    @ns_provider.response(int(HTTPStatus.OK), 'Fornecedor atualizado com sucesso.', marshall_provider)
    @ns_provider.expect(marshall_provider, validate=True)
    def put(self, id: str = None):
        """Atualizar dados do Fornecedor"""
        return self.__response(Provider().update(update=ns_provider.payload, id=id))

    @check_path_id
    @exceptions_database.exceptions
    @ns_provider.response(int(HTTPStatus.OK), 'Fornecedor apagado com sucesso.', marshall_api_response)
    def delete(self, id: str = None):
        """Apagar Fornecedor"""
        return self.__response(Provider().delete(id=id))

    @staticmethod
    def __response(result: bool):
        if result:
            return marshal(StatusAPI.REQUEST_SUCCESS_API, marshall_api_response), int(HTTPStatus.OK)
        return marshal(StatusAPI.REQUEST_NOT_FOUND_API, marshall_api_response), int(HTTPStatus.NOT_FOUND)


@ns_provider.route("")
@ns_provider.response(int(HTTPStatus.INTERNAL_SERVER_ERROR),
                      'Erro de conexão com o servidor.',
                      marshall_api_response)
class ProviderByBody(Resource):
    """Handles HTTP requests to url: /providers by Body"""

    exceptions_database: ExceptionsDatabase = ExceptionsDatabase(namespace=ns_provider)

    @exceptions_database.exceptions
    @ns_provider.expect(marshall_provider, validate=True)
    @ns_provider.response(int(HTTPStatus.CREATED),
                          'Fornecedor criado com sucesso.',
                          marshall_provider)
    def post(self):
        """Cadastrar Fornecedor"""
        provider = Provider(**ns_provider.payload).insert()
        return marshal(provider, marshall_provider), int(HTTPStatus.CREATED)

    @exceptions_database.exceptions
    @ns_provider.marshal_list_with(marshall_provider)
    def get(self):
        """Retornar lista de fornecedores"""
        return Provider.query.all()
