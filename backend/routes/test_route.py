from flask import Blueprint, request, jsonify

test_bp = Blueprint('test',__name__)

@test_bp.route('/initial', methods =['GET'])
def test_intial():
    return jsonify({
        "message":"Hello World"
    })