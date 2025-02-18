# The Collatz Sequence

number = int(input("Hi please give me a number: "))
print(number)
def collatz(number):
    try :
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
    except Exception as e:
        print(f"an exception {e} has occured")
                
collatz(number)
    

