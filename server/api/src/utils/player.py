class Player:
    
    def __init__(self, player_sid: str, name: str, quiz: str) -> None:
        self.player_sid = player_sid
        self.name = name
        self.current_question_responses = []
        self.score = 0
        self.stop = False
        self.quiz = quiz
        
    def add_response(self, response):
        self.current_question_responses.append(response)
        
    def clear_responses(self):
        self.current_question_responses.clear()
        
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.player_sid == __o.player_sid
        else:
            return False
        
    def __hash__(self) -> int:
        return hash(self.player_sid + self.name)
        
    
    def add_score(self, points) -> None:
        self.score += points
