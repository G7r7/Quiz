from src.utils.token import Token
from src.utils.player import Player

class Quiz:
    
    def __init__(self, user_id: int, quiz_id: int, admin_token: Token, player_token: Token) -> None:
        self.admin = user_id
        self.players = set()
        self.id = quiz_id
        self.admin_token = admin_token
        self.player_token = player_token
        self.open_to_register = True
        
    
    def get_age_quiz(self):
        return self.admin_token.get_token_age()
    
    def get_player_names(self):
        return list(player.name for player in self.players)
    
    def add_player(self, p: Player):
        self.players.add(p)
        
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Quiz):
            return self.id == __o.id
        else:
            return False