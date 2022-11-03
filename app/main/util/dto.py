from flask_restx import Namespace, fields


class ZuriDto:
    api = Namespace("zuri", description="Zuri related operations")
    payload_data = api.model(
        "payload_data",
        {
            "operation_type": fields.String(required=True, description="mathematical operation", enum=['addition', 'subtraction', 'multiplication']),
            "x": fields.Integer(required=True, description="x value"),
            "y": fields.Integer(required=True, description="y value"),
        },
    )