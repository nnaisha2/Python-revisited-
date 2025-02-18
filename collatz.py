# The Collatz Sequence
while True: # input validation
    try:
        number = int(input("Hi, please give me a number: "))
        print(number)
        break  
    except ValueError:
        print("Integers only! Please try again.")
    
def collatz(number):
        while True:
            if number == 1:
                break
            elif number % 2 == 0:
                newNumber = number // 2
                print(newNumber)
                number= newNumber
            
            else:
                newNumber = 3 * number +1
                print(newNumber)
                number= newNumber
                
collatz(number)
    

