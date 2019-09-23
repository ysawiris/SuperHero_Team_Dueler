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


if __name__ == "__main__":
    #If you run this file from the terminal 
    #this block is excuted 
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
