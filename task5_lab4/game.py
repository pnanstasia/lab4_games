"""
Module for game
"""
COUNTER =0

class Room:
    """
    class for information about rooms
    """
    def __init__(self, room_name, description = None, character = None, item = None) -> None:
        """
        Function for variables
        """
        self.room_name = room_name
        self.description = description
        self.rooms = []
        self.character = character
        self.item = item

    def set_description(self, message):
        """
        Function for messages
        """
        self.description = message

    def link_room(self, room, direction):
        """
        Function for direction
        """
        self.rooms.append((room, direction))

    def set_character(self, character):
        """
        Function for characters
        """
        self.character = character

    def set_item(self, item):
        """
        Function for items
        """
        self.item = item

    def get_details(self):
        """
        Function returns all information about room
        """
        print(self.room_name)
        print('--------------------')
        print(self.description)
        for i in self.rooms:
            print(f'The {i[0].room_name} is {i[1]}')

    def get_character(self):
        """
        Function returns character
        """
        return self.character

    def get_item(self):
        """
        Function returns character
        """
        return self.item

    def move(self, step):
        """
        Function for all moves
        """
        for i in self.rooms:
            if i[1] == step:
                return i[0]

class Character:
    """
    class for characters in game
    """
    def __init__(self, name, description, message=None) -> None:
        """
        Function for variables
        """
        self.name = name
        self.description = description
        self.message = message

    def describe(self):
        """
        Function for describing
        """
        print(f'{self.name} is here!')
        print(self.description)

    def set_conversation(self, conversation):
        """
        Function for conversation
        """
        self.message = conversation

    def talk(self):
        """
        Function for talking this character
        """
        print(f'[{self.name} says]: {self.message}')

class Enemy(Character):
    """
    class for information about enemy
    """
    def __init__(self, name, description, weakness=None) -> None:
        """
        Function for variables
        """
        super().__init__(name, description)
        self.weakness = weakness

    def set_weakness(self, subject):
        """
        Function for enemy's weakness
        """
        self.weakness = subject

    def fight(self, subject):
        """
        Function for fighting
        """
        if subject == self.weakness:
            global COUNTER
            COUNTER += 1
            print(f'You fend {self.name} off with the {subject}')
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def get_defeated(self):
        """
        Function for checking defead
        """
        return COUNTER

class Friend(Character):
    """
    class for friend for main character 
    """
    def __init__(self, name, description, message=None, action=None) -> None:
        """
        Function for variables
        """
        super().__init__(name, description, message)
        self.action = action

    def set_action(self, action):
        """
        Function for message, which inform about action of friend
        """
        self.action = action

    def get_action(self):
        """
        Function returns 
        """
        return self.action

class Item:
    """
    class for items
    """
    def __init__(self, name, description=None) -> None:
        """
        Function for variables
        """
        self.description = description
        self.name = name

    def set_description(self, message):
        """
        Function for description
        """
        self.description = message

    def describe(self):
        """
        Function for describing
        """
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        """
        Function returns name of item
        """
        return self.name
