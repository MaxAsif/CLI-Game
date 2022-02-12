from enum import Enum, auto
from typing import Set

class EntityEnum(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSOR = auto()
    SPOCK = auto()
    LIZARD = auto()

    def __repr__(self) -> str:
        return f"{self.name} : {self.value}"

class Rules:
    """
        Class to register all the rules
    """
    rules = {
            (EntityEnum.PAPER, EntityEnum.ROCK): {
                'winner': EntityEnum.PAPER,
                'message': 'Paper covers Rock'
            },
            (EntityEnum.PAPER, EntityEnum.SPOCK): {
                'winner': EntityEnum.PAPER,
                'message': 'Paper disapproves Spock'
            },
            (EntityEnum.ROCK, EntityEnum.LIZARD): {
                'winner': EntityEnum.ROCK,
                'message': 'Rock crushes Lizard'
            },
            (EntityEnum.ROCK, EntityEnum.SCISSOR): {
                'winner': EntityEnum.ROCK,
                'message': 'Rock crushes Scissor'
            },
            (EntityEnum.SCISSOR, EntityEnum.PAPER): {
                'winner':  EntityEnum.SCISSOR,
                'message': 'Scissor cuts Paper'
            },
            (EntityEnum.SCISSOR, EntityEnum.LIZARD): {
                'winner': EntityEnum.SCISSOR,
                'message': 'Scissor decapitates Lizard'
            },
            (EntityEnum.SPOCK, EntityEnum.SCISSOR): {
                'winner': EntityEnum.SPOCK,
                'message': 'Spock smashes Scissor'
            },
            (EntityEnum.SPOCK, EntityEnum.ROCK): {
                'winner': EntityEnum.SPOCK,
                'message': 'Spock vaporizes Rock'
            },
            (EntityEnum.LIZARD, EntityEnum.SPOCK): {
                'winner': EntityEnum.LIZARD,
                'message': 'Lizard poisons Spock'
            },
            (EntityEnum.LIZARD, EntityEnum.PAPER): {
                'winner': EntityEnum.PAPER,
                'message': 'Lizard eats Paper'
            },
            
        }
    
    def get_winner(self, entity1: EntityEnum, entity2: EntityEnum):
        """A function to find the winner between two entities

        Args:
            entity1 (EntityEnum): First entity
            entity2 (EntityEnum): Second entity

        Raises:
            KeyError: Invalid combination of entity

        Returns:
            EntityEnum: Winner of entity1 and entity2
        """
        if (entity1, entity2) in self.rules:
            return self.rules[(entity1, entity2)]['winner'], self.rules[(entity1, entity2)]['message']
        elif (entity2, entity1) in self.rules:
            return self.rules[(entity2, entity1)]['winner'], self.rules[(entity2, entity1)]['message']
        raise KeyError('Invalid entities')
    
    
  
