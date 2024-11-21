from marshmallow import Schema, fields, validate

class CompraSchema(Schema):
    CompraID = fields.Int(dump_only=True)
    UsuarioID = fields.Int(required=True)
    FechaCompra = fields.DateTime(dump_only=True)
    MetodoPago = fields.Str(required=True, validate=validate.Length(max=50))
    Total = fields.Decimal(required=True, places=2, validate=validate.Range(min=0)) 