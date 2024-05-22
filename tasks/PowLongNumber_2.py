from MultiplyLongNumber_2 import multiply_strings as mul
from DivideLongNumber_2 import div_ as div

def pow_(x, n, m):
    if m == '1': return "0"
    N, Y, Z = n, "1", x
    while True:
        div_ = div(N, "2")
        N, remainder = div_[0], div_[1]
        if remainder == "1":
            Y = div(mul(Z, Y), m)[1]
        if N == "0":
            return Y
        Z = div(mul(Z, Z), m)[1]

def has_leading_zeros(num_str):
    return len(num_str) > 1 and num_str[0] == '0'

if __name__ == "__main__":
    print("Введите числа b (основание\база), p (показатель\степень), m (модуль) для возведения числа b в степень p по модулю m:")
    b = input("b = ").strip()
    p = input("p = ").strip()
    m = input("m = ").strip()
    if b.isdigit() and p.isdigit() and m.isdigit() and not has_leading_zeros(b) \
                                                   and not has_leading_zeros(p) \
                                                   and not has_leading_zeros(m) \
                                                   and m != "0":
        result = pow_(b, p, m)
        print("Результат:", result)
    else:
        print("Введены некоректные данные")