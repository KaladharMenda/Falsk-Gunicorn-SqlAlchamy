from api import app
from flask_sqlalchemy import SQLAlchemy

host='0.0.0.0'
#host='95.216.112.188'
podhost = '95.216.245.161'
# host='rtv.stockone.in'
username='root'
password='root'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+username+':'+password+'@'+host+':3306/rtv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_BINDS'] = {
#     'pod': 'mysql+pymysql://'+username+':'+password+'@'+podhost+':3306/POD_TEST'
# }
app.config['SQLALCHEMY_POOL_SIZE'] = 100000
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10000
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10000


aldb = SQLAlchemy(app)
