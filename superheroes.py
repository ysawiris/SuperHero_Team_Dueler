import random 


class Ability:
    def __init__(self, name, max_damage):
        ''' <expand for comments>
            Create Instance Variables:
                name: String 
                max_damage: Integer 
            '''
            #TODO: Instatiate the variables listed in the docstring with then 
            #values passed in 
        self.name = name 
        self.max_damage = max_damage
    
    def attack(self):
        ''' <expand for comments>
            Return a value between 0 and the value set by the self.max_damaage.'''
            # TODO: Use random.randint(a, b) to select a random attack value.
            # Return an attack value between 0 and the full attack.
            # Hint: The constructor initializes the maximum attack value.
        attack_strength = random.randint(0, self.max_damage)
        return attack_strength

class Armor:
    def __init__(self, name, max_block):
        ''' <expand for comments> 
            Instantiate instance properties:
                name: String
                max_block: Integer
            '''
            #TODO: Create intance variables for the values passed in
        self.name = name 
        self.max_block = max_block
    
    def block(self):
        ''' 
            Return a random value between 0 and the initialized max_block strength. '''
        block_strength = random.randint(0, self.max_block)
        return block_strength

class Hero:
    def __init__(self, name, starting_health = 100):
        '''<expand for comments>
            Instance properties:
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
        self.current_health = starting_health
    
    def add_ability(self, ability):
        ''' <expand for comments>
            Add ability to abilities list '''
            #TODO: Add ability object to abilities:List
        self.abilities.append(ability)
    
    def attack(self):
        ''' <expand for comments>
            Calculate the total damage from all ability attacks.
            return: total:Int
            '''
            # TODO: This method should run Ability.attack() on every ability
            # in self.abilities and returns the total as an integer.
        total_damage = 0 

        for ability in self.abilities:
               total_attack =  ability.attack()
               total_damage += total_attack

        #print("Total damage: {}".format(total_damage))
        return total_damage

    def add_armor(self, armors):
        ''' <expand for comments>
            Add armor to self.armors
            Armor: Armor Object
            '''
            # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armors)

    def defend(self, damage_amt):
        ''' <expand for comments>
            Runs `block` method on each armor.
            Returns sum of all blocks
            '''
            # TODO: This method should run the block method on each armor in self.armors
        total_block = 0

        for armor in self.armors:
            block = int(armor.block())
            total_block += block
        damage_amt = abs(damage_amt - total_block)

        #print("Damage taken: {}".format(damage_amt))

        return damage_amt 

    def take_damage(self, damage):
        ''' <expand for comments>
            Updates self.current_health to reflect the damage minus the defense.'''
            # TODO: Create a method that updates self.current_health to the current
            # minus the the amount returned from calling self.defend(damage).
        self.current_health = self.current_health - self.defend(damage)

    def is_alive(self):
        ''' <expand for comments>
            Return True or False depending on whether the hero is alive or not.'''
            # TODO: Check whether the hero is alive and return true or false
        return self.current_health > 0 

    def fight(self, opponent):  
        ''' <expand for comments>
            Current Hero will take turns fighting the opponent hero passed in.'''
            # TODO: Fight each hero until a victor emerges.
            # Print the victor's name to the screen.
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opp_damage  = opponent.attack()

            opponent.take_damage(self_damage)
            self.take_damage(opp_damage)
            
        if self.is_alive():
            print(f'{self.name} won!')
            
        else:
            print(f'{opponent.name} won!')
            
if __name__ == "__main__":
    #If you run this file from the terminal 
    #this block is excuted 
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 50)
    ability2 = Ability("Super Eyes", 10)
    ability3 = Ability("Wizard Wand", 40)
    ability4 = Ability("Wizard Beard", 4)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)