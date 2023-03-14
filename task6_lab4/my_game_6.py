"""
Module with classes for game
"""
NUMBER_OF_WINS = 0

class Street:
    """
    class, which responsible for streets in game
    """
    def __init__(self, name_of_street: str, description=None, character=None, item=None) -> None:
        """
        Function for variables
        """
        self.name_of_street = name_of_street
        self.description = description
        self.character = character
        self.item = item
        self.ways = []

    def set_description(self, describe: str) -> None:
        """
        Function for describing street
        """
        self.description = describe

    def set_character(self, name_of_character: str) -> None:
        """
        Function for assigment character's name
        """
        self.character = name_of_character

    def get_character(self) -> str:
        """
        Function returns decription
        """
        return self.character

    def set_item(self, name_of_item: str) -> None:
        """
        Function for assigment item's name
        """
        self.item = name_of_item

    def get_item(self) -> str:
        """
        Function returns item
        """
        return self.item

    def available_streets(self, street_name: str, direction: str) -> None:
        """
        Function adds street and its direction in list
        """
        self.ways.append((street_name, direction))

    def step(self, action: str) -> str:
        """
        Function for checking step of character
        """
        for i in self.ways:
            if i[1] == action:
                return i[0]

    def information(self):
        """
        Function for getting all information about street
        """
        print(self.name_of_street)
        print('-*-*-*-*-*-*-*-*-*-*')
        print(f'Опис вулиці: {self.description}')
        for street in self.ways:
            print(f'Ви можете пройти на {street[0].name_of_street}, за напрямком {street[1]}')

class Character:
    """
    class, which describe characters
    """
    def __init__(self, name_of_character, description=None, talk=None) -> None:
        """
        Function for variables
        """
        self.character = name_of_character
        self.description = description
        self.talk = talk

    def set_description(self, describe: str) -> None:
        """
        Function for describing street
        """
        self.description = describe

    def get_description(self):
        """
        Function returns description
        """
        print(f'На цій вулиці є {self.character}')
        print(f'{self.description}')

    def talking(self, message: str) -> None:
        """
        Function for message from character
        """
        self.talk = message

    def get_talking(self):
        """
        Function returns message from character
        """
        print(f'{self.character}: "{self.talk}"')

class Enemy(Character):
    """
    class for enemys in game
    """
    def __init__(self, name_of_character, description=None, talk=None, weakness=None) -> None:
        super().__init__(name_of_character, description, talk)
        self.weakness = weakness

    def set_weakneas(self, subject: str) -> None:
        """
        Function for enemy's weaknes
        """
        self.weakness = subject

    def fight(self, thing: str) -> bool:
        """
        Function for fighting, which returns True if you won and False, if you were fighted
        """
        if thing == self.weakness:
            global NUMBER_OF_WINS
            NUMBER_OF_WINS += 1
            print(f'Ти переміг ворога! Тепер {self.character} не стане тобі на заваді')
            return True
        else:
            print('На жаль, ти програв і не зміг перемогти ворогів')
            return False

    def number_of_wins(self):
        """
        Function returns number of character wins
        """
        return NUMBER_OF_WINS

class BestFriend(Character):
    """
    class for friend
    """
    def __init__(self, name_of_character, description=None, talk=None, power=None) -> None:
        super().__init__(name_of_character, description, talk)
        self.power = power

    def set_power(self, action: str) -> None:
        """
        Function for assigment action for friend
        """
        self.power = action

    def get_power(self) -> str:
        """
        Function returns action, which will have character
        """
        return self.power

class Item:
    """
    class for items
    """
    def __init__(self, name_of_item: str, description=None) -> None:
        """
        Function for variables
        """
        self.item = name_of_item
        self.description = description

    def set_description(self, description: str) -> None:
        """
        Function for assigment description
        """
        self.description = description

    def get_description(self):
        """
        Function returns description
        """
        print(f'На цій вулиці є {self.item} - {self.description}')

    def get_name(self) -> str:
        """
        Function returns name of item
        """
        return self.item
