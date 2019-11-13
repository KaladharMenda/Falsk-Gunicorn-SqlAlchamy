from flask import Blueprint
from api import utils


default = Blueprint('default', __name__)

@default.route('/', methods = ['GET'])
def home():
	data = {
			'data':{'msg':'Welcome to SMART-TECH Solutions'},
			'http_code':200
		}
	response = utils.getJsonStr(data)
	return response
