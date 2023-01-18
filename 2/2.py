#!/usr/bin/python3

fib_num_a = 1
fib_num_b = 2
fib_num_c = 3
fib_sum = 2

while fib_num_c <= 4000000:
    if (fib_num_c % 2 == 0):
        fib_sum += fib_num_c

    tmp_c = fib_num_c
    tmp_b = fib_num_b
    fib_num_c += fib_num_b
    fib_num_b = tmp_c
    fib_num_a = tmp_b

print(fib_sum)
