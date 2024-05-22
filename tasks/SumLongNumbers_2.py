# Сложение двух строк
def add_strings(str1, str2):
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)
    carry, result = 0, []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(str1[i]) + int(str2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])

if __name__ == "__main__":
    print("Введите два числа a и b для получения суммы:")
    a = input("a = ")
    b = input("b = ")
    if a.isdigit() and b.isdigit():
        if (a[0] != '0' or len(a) == 1) and (b[0] != '0' or len(b) == 1):
            print(add_strings(a, b))
        else:
            print("Введены некоректные данные")
    else:
        print("Введены некоректные данные")

