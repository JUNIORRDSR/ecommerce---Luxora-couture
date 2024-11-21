from marshmallow import Schema, fields, validate

class UsuarioSchema(Schema):
    UsuarioID = fields.Int(dump_only=True)
    NombreCompleto = fields.Str(required=True, validate=validate.Length(min=1, max=150))
    Email = fields.Email(required=True)
    Contraseña = fields.Str(required=True, load_only=True)
    Cedula = fields.Str(required=True, validate=validate.Length(min=5, max=20))
    Telefono = fields.Str(validate=validate.Length(max=20)) 