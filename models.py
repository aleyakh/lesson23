from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit')


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *arg, **kwargs):
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('"cmd" contains invalid value')
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
