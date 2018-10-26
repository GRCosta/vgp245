# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:32:24 2018

@author: grcos
"""

class Character:
    
    def __init__(self, name, hp = 150, ph_dmg = 50, mg_dmg = 50, df = 75):
        self.name = name
        self.hp = hp
        self.ph_dmg = ph_dmg
        self.mg_dmg = mg_dmg
        self.df = df
        
        
    def physical_attack(self):
        print(self.name,"attacked with damage", self.ph_dmg)
        return self.ph_dmg
    
    def magic_attack(self):
        print(self.name,"perfomed a magic attack with damage", self.mg_dmg)
        return self.mg_dmg
    
    def defense_movement(self):
        print(self.name, "defended the attack!")
        return self.df
    
    def flee(self):
        print("Success!", self.name, "escaped the battle")

class Warrior(Character):
    def __init__(self, name, hp = 200, ph_dmg = 100, mg_dmg = 10, df = 100):
        self.name = name
        self.hp = hp
        self.ph_dmg = ph_dmg
        self.mg_dmg = mg_dmg
        self.df = df
        
class Mage(Character):
    def __init__(self, name, hp = 180, ph_dmg = 10, mg_dmg = 75, df = 200):
        self.name = name
        self.hp = hp
        self.ph_dmg = ph_dmg
        self.mg_dmg = mg_dmg
        self.df = df        
        
        
#=======================#        
char1 = Mage("Gandalf")
char2 = Warrior("Conan")

char1.physical_attack()
char2.physical_attack()
print("\n")

char1.magic_attack()
char2.magic_attack()
print("\n")

char1.defense_movement()
char2.defense_movement()
print("\n")

char1.flee()
char2.flee()
print("\n")

