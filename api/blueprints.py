""""Blueprints to API"""
from flask import Blueprint
from flask_restx import Api

from api.src.namespaces import ns_provider
from core.settings import Settings


api_bp_provider = Blueprint(name='api', import_name=__name__, url_prefix='/api/v1')
settings = Settings()
api_provider = Api(
    api_bp_provider,
    version='1.0',
    title='Fornecedores - API',
    description='Bem vindo a UI documentacão da Fornecedores API com Swagger',
    doc='/ui' if Settings().debug_is_enabled() else False,
    validate=True
)
api_provider.add_namespace(ns_provider)

if not settings.debug_is_enabled():
    api_provider.init_app(api_bp_provider, add_specs=False)
