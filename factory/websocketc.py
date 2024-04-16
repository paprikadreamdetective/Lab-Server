from socketc import SocketC
import websocket 

class WebSocket(SocketC):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.websocket = self.init_connection()

    def init_connection(self):
        ws = websocket.WebSocket()
        ws.connect('ws://'+self.host+':'+self.port)
        return ws
    
    def send_msg(self, msg: str):
        self.websocket.send(msg)

    