import eel
import os
import socket
from breeze_connect import BreezeConnect

def find_free_port(start_port):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', port))
                return port
            except OSError:
                port += 1

PORT = find_free_port(8082)

eel.init(os.path.join(os.path.dirname(__file__), 'web'))

@eel.expose
def connectBreeze(sessionToken):

    breeze = BreezeConnect(api_key=os.getenv('BREEZE_API_KEY') )
    breeze.generate_session(api_secret=os.getenv('BREEZE_API_SECRET'), session_token=sessionToken)
    return breeze

eel.start('index.html', mode=None, host='0.0.0.0', size=(900, 600), port=PORT)

