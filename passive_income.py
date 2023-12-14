import math
import time

class Passiveincome:
    
    def __init__(self, number):
        self.number = number
        
    def passive_counter(self):      
        self.number += 1
        time.sleep(1)
        
    def __str__(self):
        return str(self.number)
        
    def __add__(self, other):        
        return Passiveincome(self.number + other)
    
    def __iadd__(self, other):
        self.number += other
        return self
    
    def __radd__(self, other):
        return other + self.number
    
    def __eq__(self, other):
        return self.number == other