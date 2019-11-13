import json
import bson,pytz
from datetime import datetime
import re
from bson import json_util


from api import app

def getJsonStr(json_object):
	return json.dumps(json_object, default=json_util.default)


def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except ValueError, e:
		return False
	return True

def getTZCodecOptions():
	return bson.CodecOptions(tz_aware=True, tzinfo=pytz.timezone(app.config.get('TZ')))

def getDateFormat(fmt_str=None):
	if fmt_str == 'YmdHMS':
		return "%Y-%m-%d %H:%M:%S"
	elif fmt_str == 'Ymd':
		return "%Y-%m-%d"
	elif fmt_str == 'Y':
		return "%Y"
	elif fmt_str == None:
		return "%Y-%m-%d %H:%M:%S"
	else:
		return "%d-%m-%Y"

def getDateTimeObject(dt_str,dt_frmt=None):
	return datetime.strptime(dt_str, getDateFormat(dt_frmt))

def getLikeStr(keyword,like_format=None):
	if like_format=='*+':
		return re.compile('.*'+keyword, re.IGNORECASE)
	elif like_format=='+*':
		return re.compile(keyword+'.*', re.IGNORECASE)
	elif like_format=='*+*':
		return re.compile('.*'+keyword+'.*', re.IGNORECASE)
	elif like_format==None:
		return re.compile(keyword, re.IGNORECASE)
	else:
		return re.compile('.*'+keyword+'.*', re.IGNORECASE)

def getLikeInt(keyint,like_format=None):
	# "/^"+str(zipCode)+".*/
	if like_format=='*+':
		return "/.*"+str(keyint)+"$/"
	elif like_format=='+*':
		return "/^"+str(keyint)+".*/"
	elif like_format=='*+*':
		return "/.*"+str(keyint)+".*/"
	elif like_format==None:
		return "/^"+str(keyint)+"$/"
	else:
		return "/.*"+str(keyint)+".*/"

def sanitizeStr(_str,datatype='str'):
	if datatype=='str':
		_str = _str or None
	elif datatype=='bool':
		_str = bool(_str or None)
	elif datatype=='int':
		try:
			_str = int(_str)
		except:
			_str = None
	elif datatype=='df':
		if type(_str) == 'bool':
			_str = bool(_str | None)
		else:
			_str = _str or None
	return _str

def getURLVars(req,remCount):
	return req.url_rule.rule.split('/')[remCount:]

