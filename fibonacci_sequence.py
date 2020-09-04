# program to display fibonacci sequence
# up to n number of terms
# as desired by the user

n_terms = int(input("How many numbers do you need in the Fibonacci sequence? "))

num_1, num_2 = 0, 1
count_terms = 0
value = 1

while value:

    if n_terms <= 0:
        print('Please enter a positive number')
        n_terms = int(input("How many numbers do you need in the Fibonacci sequence? "))
    elif n_terms == num_2:
        print("Fibonacci sequence for ",n_terms,"is: ")
        print(num_1)
        value = 0
    else:
        print('Fibonacci sequence for ',n_terms, "is: ")
        while count_terms < n_terms:
            print(num_1)
            new_number = num_1 + num_2
            num_1 = num_2
            num_2 = new_number
            count_terms += 1
        value = 0

