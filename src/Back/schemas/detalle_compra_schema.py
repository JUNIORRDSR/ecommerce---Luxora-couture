from marshmallow import Schema, fields, validate

class DetalleCompraSchema(Schema):
    DetalleCompraID = fields.Int(dump_only=True)
    CompraID = fields.Int(required=True)
    ProductoID = fields.Int(required=True)
    Cantidad = fields.Int(required=True, validate=validate.Range(min=1))
    PrecioUnitario = fields.Decimal(required=True, places=2, validate=validate.Range(min=0)) 