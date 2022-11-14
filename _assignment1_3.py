numbers = (1,2,3,4,5,6,7,8,9)
no_of_odd = 0
no_of_even = 0
for i in numbers:
    if i%2:
        no_of_odd += 1
    else:
        no_of_even += 1
print("Number of odd numbers:",no_of_odd)
print("Number of even numbers:",no_of_even)