from api import app

# Import all required modules
from flask_cors import CORS, cross_origin
from api.default import default
#from api.error import error
from api.insurance import insurance

# Register Blueprints
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(insurance, url_prefix='/insurance')
app.register_blueprint(default, url_prefix='/')
# app.register_blueprint(error, url_prefix='/error')
