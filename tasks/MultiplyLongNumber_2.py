def multiply_strings(u, v):
    w = [0] * (len(u) + len(v))
    for j in range(len(v) - 1, -1, -1):
        k = 0
        for i in range(len(u) - 1, -1, -1):
            temp_val = int(u[i]) * int(v[j]) + w[i + j + 1] + k
            k = temp_val // 10
            w[i + j + 1] = temp_val % 10
        w[j] += k
    result_str = ''.join(map(str, w))
    return result_str.lstrip('0') or '0'
        
def has_leading_zeros(num_str):
    return len(num_str) > 1 and num_str[0] == '0'

if __name__ == "__main__":
    print("Введите два числа a и b для получения произведения:")
    a = input("a = ").strip()
    b = input("b = ").strip()
    if a.isdigit() and b.isdigit() and not has_leading_zeros(a) and not has_leading_zeros(b):
            print(f"{a} * {b} =", multiply_strings(a, b))
    else:
        print("Введены некоректные данные")