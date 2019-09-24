import random 


class Ability:
    def __init__(self, name, max_damage):
        ''' Create Instance Variables:
             name: String 
             max_damage: Integer 
        '''
        #TODO: Instatiate the variables listed in the docstring with then 
        #values passed in 
        self.name = name 
        self.max_damage = max_damage
    
    def attack(self):
        ''' Return a value between 0 and the value set by the self.max_damaage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        attack_strength = random.randint(0, self.max_damage)
        return attack_strength

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        #TODO: Create intance variables for the values passed in
        self.name = name 
        self.max_block = max_block
    
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        block_strength = random.randint(0, self.max_block)
        return block_strength

class Hero:
    def __init__(self, name, starting_health):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        # TODO: Initialize instance variables values as instance variables
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = 100


if __name__ == "__main__":
    #If you run this file from the terminal 
    #this block is excuted 
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    armor = Armor("Debugging Armor", 20)
    print(armor.name)
    print(armor.block())

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.starting_health)
    print(my_hero.current_health)
    
