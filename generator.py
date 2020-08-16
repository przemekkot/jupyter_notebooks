def give_me_first_n_numbers(number):
    for i in range(number):
    	yield i

n_sum = 0
for n in give_me_first_n_numbers(number=1000):
    n_sum = n_sum + n
print("Total sum is: %d" % n_sum)
"""
for n in give_me_first_n_numbers(100):
	print(n)
"""