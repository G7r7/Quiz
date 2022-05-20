from typing import List, Tuple
from src.utils.player import Player
from src.utils.quiz import Quiz

class MemoryQuiz:
    
    def __init__(self) -> None:
        self.quizs = dict()
        self.__player_token_to_quiz = dict()
        self.current_playing = dict()
        
    def play_quiz(self, quiz: Quiz):
    
        quiz.open_to_register = False
        for player in quiz.players:
            self.current_playing[player.player_sid] = player
        
    def end_quiz(self, quiz: Quiz):
        for player in quiz.players:
            try:
                self.current_playing.pop(player.player_sid)
            except KeyError:
                pass
            
    def pause_quiz(self, quiz: Quiz):
        self.open_to_response = False
        for player in quiz.players:
            player.stop = True
            
    def unpause_quiz(self, quiz: Quiz):
        self.open_to_response = True
        for player in quiz.players:
            player.stop = False
        
    def __getitem__(self,key: Tuple[int, int]) -> Quiz:
        return self.quizs[key]
    
    def __getitem__(self,token: str) -> Quiz:
        return self.quizs[self.__player_token_to_quiz[token]]
    
    def __setitem__(self,key: Tuple[int, int],value: Quiz) -> None:
        self.quizs[key] = value
        self.__player_token_to_quiz[value.player_token.get_token()] = key
        
    def __contains__(self, key: Tuple[int, int]) -> bool:
        return key in self.quizs.keys()
    
    def __contains__(self, token: str) -> bool:
        return token in self.__player_token_to_quiz.keys()
    
    def delete(self, key: Tuple[int, int]) -> None:
        quiz = self.quizs[key]
        del self.__player_token_to_quiz[quiz.player_token.get_token()]
        del self.quizs[key]

    
    def values(self) -> List[Quiz]:
        return self.quizs.values()
    
    def admin_tokens(self) -> List[str]:
        return [quiz.admin_token.get_token() for quiz in self.values()]
    
    def player_tokens(self) -> List[str]:
        return [quiz.player_token.get_token() for quiz in self.values()]
    
    def get_player_from_sid(self, sid):
        return self.current_playing[sid]
    
    def remove_player(self, sid):
        try:
            player = self.get_player_from_sid(sid)
            name = player.name
            quiz = self[sid]
            quiz.remove_player(player)
            del self.current_playing[sid]
        except KeyError:
            return ""
        return name