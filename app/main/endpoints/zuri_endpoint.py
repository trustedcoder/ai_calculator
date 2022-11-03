import logging
from flask_restx import Resource
from flask import request
from app.main.business.zuri_business import AppBusiness
from app.main.util.dto import ZuriDto
from app.main.util.req_parser import payload_data

zuri_namespace = ZuriDto.api

audit_logger = logging.getLogger(__name__)


@zuri_namespace.route("/cal")
class Zuri(Resource):
    @zuri_namespace.doc("Calculate simple arithmetic")
    @zuri_namespace.expect(payload_data)
    def post(self):
        data = payload_data.parse_args(request)
        return AppBusiness.cal_arithmetic(data)
