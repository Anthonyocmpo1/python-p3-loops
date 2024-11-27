# 1. happy_new_year() - Count down from 10 to 1 and print "Happy New Year!"
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# 2. square_integers() - Return a list of squared integers
def square_integers(int_list):
    return [x ** 2 for x in int_list]

# 3. fizzbuzz() - Print numbers from 1 to 100 with substitutions for multiples of 3, 5, and both
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Running the functions to test them

# Test happy_new_year()
print("Testing happy_new_year()")
happy_new_year()
print("\n")

# Test square_integers()
print("Testing square_integers()")
print(square_integers([1, 2, 3, 4, 5]))  # Should print [1, 4, 9, 16, 25]
print("\n")

# Test fizzbuzz()
print("Testing fizzbuzz()")
fizzbuzz()
