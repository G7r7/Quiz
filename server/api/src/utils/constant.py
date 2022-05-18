from .token_collector import TokenCollector
from .memory_quiz import MemoryQuiz
import socketio

class GlobalVar:

    MEM_QUIZ = MemoryQuiz()
    TOKEN_COLLECTOR = TokenCollector(mem=MEM_QUIZ, interval=1)
    SIO = socketio.AsyncServer(logger=True, engineio_logger=True, async_mode='asgi', cors_allowed_origins="*")
    APP_SOCKET = socketio.ASGIApp(SIO)

