from api import app
import sys

if __name__ == '__main__':
	host = app.config.get('HOST')
	port = app.config.get('PORT_STAGING')
	debug = app.config.get('DEBUG_STAGING')
	app.run(host,port,debug=False)
