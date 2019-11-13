from api import app

app.config['ENV'] = 'PRODUCTION'
app.config['TZ'] = 'Asia/Calcutta'

#app.config['CORS_ORIGINS'] = ['*']
#app.config['CORS_HEADERS'] = ['Content-Type', 'Authorization','DCUBE-API-KEY']
#app.config['CORS_AUTOMATIC_OPTIONS'] = True

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8888
app.config['PORT_STAGING'] = 9898
app.config['DEBUG'] = True
app.config['DEBUG_STAGING'] = True
