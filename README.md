## miniature-parakeet
### a clicker game made in pygame

a project i started to help me get better with python and game develepment.

the progression with the game halted when i lost motivation and interest(and couldnt code very well), but i will try to push out two more versions

- [x] `first update - code clean up and removing unnecessary code`

- [x] `second update - adding classes and further code cleanup, and maybe more features`
 
 #### the game shouldn't be to hard to expand upon, and to make look prettier
---
## so apparently im not done

ive added quite a bit to the code base
- [x] recursion
- [x] another button
- [x] and i might work on a passive income system

altho im not sure how i would work in the passive incomve system, maybe i can count the clock.tick and for every tick add 1, im not sure idk

---

## how i do the passive income

I've created a class which passes itself as a perameter and returns an int like this(with help from a friend)
```
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
```
then i create a custom event in pygame like this 
```
PASSIVEVENT = USEREVENT + 1

if event.type == PASSIVEVENT:
    main_counter += input_passive_income
    print(f"main counter is {main_counter}")
```
which allows me to use this function in ***pygame.time.set_timer(userevent, 1000)***, which takes a custom event and then counts a time down and then restarts the event
