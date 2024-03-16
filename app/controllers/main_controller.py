from decouple import config
import requests

def getTransactionByHash(tx):   
    transaction_data = {}
    try:

        urlData= config("URL_BUNDLER_LOADER_NOVER")
        response = requests.get(urlData+tx)
        data = response.json()
        transaction_data = {
            'blockHash': data['txReceipt']['blockHash'],
            'blockNumber':data['txReceipt']['blockNumber'],
            'from': data['txReceipt']['from'],
            'gas': int(data['rawTx']['gas'], 16),
            'gasPrice': int(data['rawTx']['gasPrice'], 16),
            'hash': data['rawTx']['hash'],
            'input': data['rawTx']['input'],
            'nonce': int(data['rawTx']['nonce'], 16),
            'r': data['rawTx']['r'],
            's': data['rawTx']['s'],
            'to': data['rawTx']['to'],
            'transactionIndex': int(data['rawTx']['transactionIndex'], 16),
            'type': int(data['rawTx']['type'], 16),
            'v': int(data['rawTx']['v'], 16),
            'value': int(data['rawTx']['value'], 16)
        }
    except Exception as e:
        transaction_data = {
            "error": str(e)  
        }

    return transaction_data

def getTransactionReceipt(tx):
    transaction_data = {}
    try:
        urlData = config("URL_BUNDLER_LOADER_NOVER")
        response = requests.get(urlData + tx)
        data = response.json()

        # Intenta obtener contractAddress y maneja la excepción KeyError si no está presente
        try:
            transaction_data['contractAddress'] = data['txReceipt']['contractAddress']
        except KeyError:
            pass


        transaction_data = {
            'blockHash': data['txReceipt']['blockHash'],
            'blockNumber': data['txReceipt']['blockNumber'],
            'contractAddress': None,  # Establece contractAddress como None por defecto
            'cumulativeGasUsed': int(data['txReceipt']['cumulativeGasUsed'], 16),
            'from': data['txReceipt']['from'],
            'gasUsed': int(data['txReceipt']['gasUsed'], 16),
            'logs': data['txReceipt']['logs'],
            'logsBloom': data['txReceipt']['logsBloom'],
            'status': int(data['txReceipt']['status'], 16),
            'to': data['rawTx']['to'],
            'transactionHash': data['txReceipt']['transactionHash'],
            'transactionIndex': int(data['rawTx']['transactionIndex'], 16),
        }
    except Exception as e:
        transaction_data = {
            "error": str(e)  # Retorna la descripción del error como un diccionario en caso de excepción
        }

    return transaction_data


def debug_traceTransaction(tx):
    debug_transaction = {}

    try:
        urlData = config("URL_BUNDLER_LOADER_NOVER")
        txUrl = urlData + tx['tx']
        response = requests.get(txUrl)
        data = response.json()

        debug_transaction = {
            "jsonrpc": tx['jsonrpc'],
            "id": tx['id'],
            "result": {
                "from": data['txReceipt']['from'],
                "gas": data['rawTx']['gas'],
                "gasUsed": data['txReceipt'].get('gasUsed', None),  
                "to": data['rawTx']['to'],
                "input": data['rawTx']['input'],
                "calls": data['rawTraces'].get('calls', None),  
                "value": data['rawTx']['value'],
                "type": data['rawTraces'].get('type', None)  
            }
        }
    except Exception as e:
        debug_transaction = {
            "error": str(e)  # Retorna la descripción del error como un diccionario en caso de excepción
        }

    return debug_transaction


def eth_getBlockByNumber(tx):
    transaction_data = {}
    try:
        urlData = config("URL_BUNDLER_LOADER_NOVER")
        response = requests.get(urlData + tx)
        data = response.json()


        transaction_data = {
            'difficulty': "missing in the bundle",
            'extraData': "missing in the bundle",
            'gasLimit': "missing in the bundle",
            'miner': "missing in the bundle",
            'number': "missing in the bundle",
            'parentHash': "missing in the bundle",
            'receiptsRoot': "missing in the bundle",
            'sha3Uncles': "missing in the bundle",
            'size': "missing in the bundle",
            'stateRoot': "missing in the bundle",
            'totalDifficulty': "missing in the bundle",
            'transactions': "missing in the bundle",
            'transactionsRoot': "missing in the bundle",

            'gasUsed': int(data['txReceipt']['gasUsed'], 16),
            'hash': data['rawTx']['hash'],
            'logsBloom': data['txReceipt']['logsBloom'],
            'nonce': int(data['rawTx']['nonce'], 16),
            'timestamp': data['rawTx']['timestamp'],
        }
    except Exception as e:
        debug_transaction = {
            "error": str(e)  # Retorna la descripción del error como un diccionario en caso de excepción
        }

    return transaction_data
