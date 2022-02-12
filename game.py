import random
from scoreboard import Scoreboard
from rules import EntityEnum, Rules


class Game:
    def __init__(self, user: str) -> None:
        print("Rock paper scissor spock and lizard...\n Welcome to the game.")
        print("Rules are simple...")
        print("Scissors decapitate Lizard, Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")
        print("To begin press [Enter]")
        _ = input()
        
        self.scoreboard = Scoreboard()
        self.max_round = 5
        self.entities = EntityEnum
        self.rules = Rules()
        self.user: str = user
        self.cpu: str = "cpu"
        
        # register players in scoreboard
        self.scoreboard.register_player(self.user)
        self.scoreboard.register_player(self.cpu)
        
    
    def display_entity_to_select(self):
        choices_text = ", ".join(f"({entity.value} for {entity.name})" for entity  in self.entities)
        print(f"Select {choices_text}:", end='\t')
    
    def get_user_input(self):
        available_choices = [entity.value for entity in self.entities]
        while True:
            try:
                self.display_entity_to_select()
                choice = int(input())
                
                if choice not in available_choices:
                    print("Please select from available choices")
                else:
                    return self.entities(choice)
            except ValueError:
                print("You entered something other than a number")
    
    def get_cpu_input(self):
        cpu_choice = random.randint(1, len(self.entities))
        return self.entities(cpu_choice)
    
    def display_current_round(self, user_entity: EntityEnum, cpu_entity: EntityEnum):
        print(f"{self.user} ({user_entity.name}) x {self.cpu} ({cpu_entity.name})")
        print("....")
    
    def display_tie(self):
        print(f"It's a tie..")
    
    def display_round_winner(self, winner_name: str, winner_entity: EntityEnum, message: str):
        print(f"{winner_name} ({winner_entity.name}) wins the round as {message}")
    
    def do_turn(self):
        user_entity = self.get_user_input()
        cpu_entity = self.get_cpu_input()
        
        self.display_current_round(user_entity, cpu_entity)
        if cpu_entity == user_entity:
            self.display_tie()
            return

        winner, message = self.rules.get_winner(user_entity, cpu_entity)
        if winner == user_entity:
            self.display_round_winner(self.user, user_entity, message)
            self.scoreboard.points[self.user] += 1
        else:
            self.display_round_winner(self.cpu, cpu_entity, message)
            self.scoreboard.points[self.cpu] += 1
    
    @staticmethod
    def get_user_name():
        print("Please enter your name:", end='\t')
        return str(input().strip())
        
    
    def play(self):
        for i in range(self.max_round):
            self.do_turn()
            self.scoreboard.display_scores()