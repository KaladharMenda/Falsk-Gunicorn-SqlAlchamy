from flask import Blueprint,request,redirect,url_for
from modal import Users
from db import aldb
from sqlalchemy import update
from copy import deepcopy
import re
from api import utils
import os
from datetime import datetime,timedelta
from sqlalchemy import text,or_
import time
import pandas as pd

insurance = Blueprint('insurance', __name__)

@insurance.route('/first', methods = ['GET'])
def getAllItems():
	try:
		UsersRef = Users.query.filter(Users.phone_no == '9490943445')
		if UsersRef > 0:
			data = UsersRef.first().__dict__
			sent = {
				'Name': data['firstname'],
				'phoneNumber': data['phone_no'],
				'email':data['email']
			}
			response = utils.getJsonStr(sent)
		return response
	except Exception as e:
		return 'welcome to Insurance'

		


