#  when function call itself it is called recursion
#  three major part of recursion
# 1. where recursion start
# 2. what is the logic of recursion
# 3. where will recursion end

# example : factorial of n number 
# if n = 5 then factorial of 5 is [ 5 * 4 * 3 * 2 * 1] = 120
# starting point is 5, logic (n * n-1), end 1

def factorial_of_number(my_num):
    if my_num <= 1 :
        return 1
    
    return my_num * factorial_of_number(my_num - 1)

factorial_result = factorial_of_number(5)
# print("Factorial Of Number : ", factorial_result )


# 0, 1, 1, 2, 3, 5, 8
def fibonacci_series(my_number):
    if my_number <= 0:
        return 0
    
    if my_number == 1:
        return 1

    return fibonacci_series(my_number - 1 ) + fibonacci_series(my_number - 2)


for i in range(10):
    print(fibonacci_series(i))

