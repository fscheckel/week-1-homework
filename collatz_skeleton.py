import numpy as np

def number_of_steps_to_one(number):
    """Function which determines how many steps
    it takes for a number to reach 1 in the Collatz
    sequence
    input: number (a positive integer)
    output: steps 
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    if not number>1:
        raise ValueError("number must be larger than one")

    return
    Line = [] 
    #this is the list
def step(n):
    while n > 1:
        if n%2 == 0:
    
            return n/2
    #Find if n is even and keeps finding even numbers
        else:
        
            return 3*(n)+1
    #If n is odd then use this function
    step = len(Line) 
    #this is to see how long the list is now
    
if __name__ == "__main__":
    max_number_to_check = 10**5
    numbers_to_check = np.linspace(1,10000, dtype = int)
    for b in numbers_to_check:
        b = int(b)
        step = number_of_steps_to_one(b)

    data = zip(numbers_to_check)
