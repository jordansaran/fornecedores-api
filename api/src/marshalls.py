"""Marshall to Namespaces"""
from flask_restx import Model, fields

marshall_provider = Model("Provider", {
    'id': fields.String(max_length=16, readonly=True, description="ID"),
    'name': fields.String(max_length=50, required=True, description="Proprietário da empresa"),
    'company': fields.String(max_length=255, required=True, description="Nome da empresa"),
    'amount_products': fields.Integer(min=0, required=True, description="valor da empresa em reais(R$)"),
    'created_at': fields.DateTime(readonly=True, description="Data criação do fornecedor")
})
marshall_api_response = Model("ApiResponse", {
    'code': fields.Integer(readonly=True, description="código"),
    'type': fields.String(readonly=True, description="Tipo de reposta da API"),
    'message': fields.String(readonly=True, description="Mensagem descrevndo a resposta da API"),
})
