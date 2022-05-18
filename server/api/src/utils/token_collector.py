import time
import threading
from threading import Thread

from src.utils.memory_quiz import MemoryQuiz

class TokenCollector(Thread):
        
    @staticmethod
    def __delete_outdated_tokens(mem: MemoryQuiz, interval: int):
        for t in [(quiz.admin, quiz.id) for quiz in mem.values() if quiz.admin_token.get_token_age() > interval]:
            mem.delete(t)
                
        
    def __init__(self, mem: MemoryQuiz, interval: int) -> None:
        
        super(TokenCollector, self).__init__()
        self.mem = mem
        self.interval = interval
        self._stop = threading.Event()
        
        
    def stop(self):
        self._stop.set()
 
    def stopped(self):
        return self._stop.isSet()
    
    def run(self):
        while True:
            if self.stopped():
                return
            TokenCollector.__delete_outdated_tokens(self.mem, self.interval)
            print(f"Thread is stopped: {self.stopped()}")
            time.sleep(1)
