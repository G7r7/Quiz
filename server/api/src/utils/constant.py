from .token_collector import TokenCollector
from .memory_quiz import MemoryQuiz
import socketio

mem_quiz = MemoryQuiz()
token_collector = TokenCollector(mem=mem_quiz, interval=1)
sio = socketio.AsyncServer(logger=True, engineio_logger=True, async_mode='asgi', cors_allowed_origins="*")

# Add events to the SIO
from ..events.quiz import *

app_socket = socketio.ASGIApp(sio)

