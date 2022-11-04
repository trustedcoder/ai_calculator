from flask_restx import reqparse


payload_data = reqparse.RequestParser()
payload_data.add_argument("operation_type",type=str,required=True,location="json",help="operation type should be subtraction, addition or multiplication, ")
payload_data.add_argument("x",type=int,required=True,location="json",help="x should be an integer")
payload_data.add_argument("y",type=int,required=True,location="json",help="y should be an integer")
