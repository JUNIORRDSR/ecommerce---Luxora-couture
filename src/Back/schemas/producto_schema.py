from marshmallow import Schema, fields, validate

class ProductoSchema(Schema):
    ProductoID = fields.Int(dump_only=True)
    Nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    Descripcion = fields.Str()
    Precio = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    Imagen = fields.Str(validate=validate.Length(max=255))
    Stock = fields.Int(required=True, validate=validate.Range(min=0))
    Categoria = fields.Str(validate=validate.Length(max=50))
    Talla = fields.Str(validate=validate.Length(max=10)) 