from SubstractLongNumber_3 import subtract_strings
from SumLongNumbers_2 import add_strings
from SumLongNumbers_2 import add_strings as sum_
from MultiplyLongNumber_2 import multiply_strings
from DivideLongNumber_2 import divide_strings as div_
from PowLongNumber_2 import pow_
from random import randint
import time
from math import gcd 

def test_sub():

    for _ in range(10000):
        a = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        b = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        if a > b:
            start_1 = time.perf_counter_ns()
            num1 = subtract_strings(str(a), str(b))
            end_1 = time.perf_counter_ns()

            start_2 = time.perf_counter_ns()
            num2 = a - b
            end_2 = time.perf_counter_ns()
            
            print(f"Алгоритм: {num1}  time {end_1 - start_1} ns")
            print(f"Встроенная: {num2}  time {end_2 - start_2} ns")
            print()

def test_add():

    for _ in range(100000000):
        a = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        b = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        start_1 = time.perf_counter_ns()
        num1 = add_strings(str(a), str(b))
        end_1 = time.perf_counter_ns()

        start_2 = time.perf_counter_ns()
        num2 = a + b
        end_2 = time.perf_counter_ns()
        
        print(f"Алгоритм: {num1}  time {end_1 - start_1} ns")
        print(f"Встроенная: {num2}  time {end_2 - start_2} ns")
        print()

def test_mul():

    for _ in range(1000):
        a = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        b = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        start_1 = time.perf_counter_ns()
        num1 = multiply_strings(str(a), str(b))
        end_1 = time.perf_counter_ns()

        start_2 = time.perf_counter_ns()
        num2 = a * b
        end_2 = time.perf_counter_ns()
        
        print(f"Алгоритм: {num1}  time {end_1 - start_1} ns")
        print(f"Встроенная: {num2}  time {end_2 - start_2} ns")
        print()

def test_div():

    for _ in range(1000):
        a = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        b = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        start_1 = time.perf_counter_ns()
        div1, remainder1 = div_(str(a), str(b))
        end_1 = time.perf_counter_ns()

        start_2 = time.perf_counter_ns()
        div2, remainder2 = a // b, a % b
        end_2 = time.perf_counter_ns()
        
        print(f"Алгоритм:\n Целая часть: {div1}\n Остаток:{remainder1}\n Время: {end_1 - start_1} ns\n")
        
        print(f"Встроенная:\n Целая часть: {div2}\n Остаток:{remainder2}\n Время: {end_2 - start_2} ns\n")
        print()


def test_pow():

    for _ in range(1000):
            
            a = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
            b = randint(100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
            m = randint(1000000000000, 100000000000000000000000000000000000000000)

            start_1 = time.perf_counter_ns()
            res_1 = pow(a, b, m)
            end_1 = time.perf_counter_ns()

            start_2 = time.perf_counter_ns()
            res_2 = pow_(str(a), str(b), str(m))
            end_2 = time.perf_counter_ns()
            
            print(f"Встроенная:\n {res_1}\n Время: {end_1 - start_1} ns\n")
            
            print(f"Алгоритм:\n  {res_2}\n Время: {end_2 - start_2} ns\n")
            print()

def is_bigger(a, b):
    len_a, len_b = len(a), len(b)
    if len_a == len_b:
        return a > b
    return len_a > len_b

def gcd_(a, b):
    while a != "0" and b != "0":
        if is_bigger(a, b):
            a = div_(a, b)[1]
        else:
            b = div_(b, a)[1]
    return sum_(a, b)




def test_gcd():
    for _ in range(10000):
            
        a = randint(100000000000, 100000000000000000000)
        b = randint(100000, 1000000000000000000)
    
        start_1 = time.perf_counter_ns()
        res_1 = gcd(a, b)
        end_1 = time.perf_counter_ns()

        start_2 = time.perf_counter_ns()
        res_2 = gcd_(str(a), str(b))
        end_2 = time.perf_counter_ns()
        
        print(f"Встроенная:\n Целая часть: {res_1}\n Время: {end_1 - start_1} ns\n")
        
        print(f"Алгоритм:\n Целая часть: {res_2}\n Время: {end_2 - start_2} ns\n")
        print()
           

if __name__ == "__main__":
    #test_add()
    #test_sub()
    #test_mul()
    #test_div()
    #test_pow()
    test_gcd()  