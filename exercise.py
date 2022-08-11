# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn



# Task1

def even_or_odd(number):
    #print(number)
    if number %2 !=  0:
        return 'odd number'
    else:
        return 'even Number'    


def user_input():
    counter = 0
    while counter < 3:
        number = int(input('Enter some Numbers: '))
        counter += 1
        print(even_or_odd(number))
        


    
#if __name__ == "__main__":
user_input()

def Test():
    return 'Pasco'

print(Test())


#Task 2
#n = int(input("How many Arguments wanna do?:"))
Start = int(input("Start_number please?:"))
Stop = int(input("Stop_number please?:"))
Step = int(input("Step please?:"))

for i in range(Start,Stop+1,Step):
    print(i)


# Task 3

usernumber = int(input("Give me a Number: "))

for k in range (1, usernumber):
    if usernumber % k == 0:
        print(k)



# Task 4

num= int(input("Give me a number:"))

prime = True

for k in range (2, num):
    if num % k == 0:
        prime = False

if prime == True:
    print(f"{num} is a prime number!")
else:
    print(f"{num}  is not a prime number")


# Task 5

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 ==0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

# Task 6

for i in range(1000,2001):
    if i%7 == 0 and i %5 != 0:
       print(i)




