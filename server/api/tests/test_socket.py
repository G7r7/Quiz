from fastapi.testclient import TestClient
from src.main import app

    
# def test_websocket():
#     client = TestClient(app)
#     with client.websocket_connect("/socket.io/") as websocket:
#         data = websocket.receive_json()
#         assert data == {"msg": "Hello WebSocket"}