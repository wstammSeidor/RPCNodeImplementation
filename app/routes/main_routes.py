from flask import Blueprint,jsonify,request
from decouple import config
from controllers import main_controller

mainRoutes = Blueprint('mainRoutes', __name__)

@mainRoutes.route('/',methods=['POST'])
def index():

    actions = request.json['actions']
    transaction_data = []

    available_functions = {
        'getTransactionByHash': main_controller.getTransactionByHash,
        'getTransactionReceipt': main_controller.getTransactionReceipt,
        'debug_traceTransaction': main_controller.debug_traceTransaction,
        'eth_getBlockByNumber': main_controller.eth_getBlockByNumber,
    }
    for action in actions:
        function_name = action['function']
        params = action['params']

        if function_name in available_functions:
            func = available_functions[function_name]
            result = func(params)
            transaction_data.append(result)
        else:
            transaction_data.append({'error': f'Función "{function_name}" no encontrada'})


    return jsonify(transaction_data)

  