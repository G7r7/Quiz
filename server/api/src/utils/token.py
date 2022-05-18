from secrets import token_urlsafe
import time

class Token:
    
    def __init__(self, n):
        self.__token = token_urlsafe(n)
        self.__creation_time = time.time()
        
    def get_token(self):
        return self.__token
    
    def get_token_age(self):
        return time.time() - self.__creation_time
    
    def __hash__(self) -> int:
        return hash(self.__token + str(self.__creation_time))
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, str):
            return self.get_token() == __o
        elif isinstance(__o, Token):
            return self.get_token() == __o.get_token() and self.get_token_age() == __o.get_token_age()
        else:
            return False
        
    def __ne__(self, __o: object) -> bool:
        return not (self == __o)