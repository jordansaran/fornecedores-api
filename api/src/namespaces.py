""""Namespaces with resources to API"""
from flask_restx import Namespace


ns_provider = Namespace(name="Fornecedor",
                        description="Informações sobre Fornecedores.",
                        validate=True,
                        path='/providers')
