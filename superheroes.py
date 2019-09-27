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
        ''' <expand for comments>
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
        self.deaths = 0
        self.kills = 0 

    def add_kills(self, num_kills):
        ''' <expand for commments>
            Update kills with num_kills
            '''
            #TODO: This method should add the number of kills to self.kills 
        self.kills += num_kills
        
    
    def add_deaths(self, num_deaths):
        ''' <expand for comments> 
            Update deaths with num_death
            '''
            #TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        
    
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
            self.add_kills(1)
            opponent.add_deaths(1)
            
            
            

        else:
            print(f'{opponent.name} won!')
            self.add_deaths(1)
            opponent.add_kills(1)

class Weapon(Ability):
    def attack(self):
        ''' <expand for comments>
            This method returns a random value
            between one half to the full attack power of the weapon.
            '''
            # TODO: Use what you learned to complete this method.            
        half_damage = self.max_damage // 2  
        return random.randint(half_damage, self.max_damage)
        
class Team():
    def __int__(self, name):
        ''' <expand for comments>
            Initialize your team with its team name 
            '''
            #TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []
    
    def remove_hero(self, name):
        ''' <expand for comments> 
            Remove hero from heroes list.
            If Hero isn't found return 0.
            '''
            # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                break

    def view_all_heroes(self):
        ''' <expand for comments>
            Prints out all heroes to the console.
            '''
            # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)
    
    def add_hero(self, hero):
        ''' <expand for comments>
            Add Hero object to self.heroes.'''
            # TODO: Add the Hero object that is passed in to the list of heroes in
            # self.heroes
        self.heroes.append(hero)
    
    def attack(self, other_team):
        ''' <expand for comments>
            Battle each team against each other.'''
            # TODO: Randomly select a living hero from each team and have
            # them fight until one or both teams have no surviving heroes.
            # Hint: Use the fight method in the Hero class.
        pass

    def revive_heroes(self, health=100):
        ''' <expand for comments> 
            Reset all heroes health to starting_health'''
            # TODO: This method should reset all heroes health to their
            # original starting value.
        pass

    def stats(self):
        ''' <expand for comments>
            Print team statistics'''
            # TODO: This method should print the ratio of kills/deaths for each
            # member of the team to the screen.
            # This data must be output to the console.
            # Hint: Use the information stored in each hero.
        pass    

        


        

        
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
    