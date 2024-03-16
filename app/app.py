from flask import Flask, request, jsonify,Response
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={'*': {'origins': '*'}})



#routes

from routes import main_routes


@app.route('/',methods=['GET'])
def index():
    return 'RPC Node '


def page_not_found(error):
    return '<h1>La página a la que intentas acceder no existe </h1>', 404


app.register_blueprint(main_routes.mainRoutes, url_prefix='/api/v1')

    
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

