def check_negate(str1, str2):
       # Проверка, если str1 меньше str2, меняем их местами
    if int(str1) < int(str2):
        str1, str2 = str2, str1
        negative_result = True
    else:
        negative_result = False
    return str1, str2, negative_result

def subtract_strings(str1, str2):
    max_len = max(len(str1), len(str2))
    str1, str2, negative = check_negate(str1, str2)
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)
    k = 0
    res = []
    for i in range(max_len-1, -1, -1):
        diff = (int(str1[i]) - int(str2[i]) + k) % 10
        k = (int(str1[i]) - int(str2[i]) + k) // 10
        res.append(diff)
    res.reverse()
    result_str = ''.join(map(str, del_leading_zero(res)))

    if negative:
        result_str = '-' + result_str

    return result_str

def del_leading_zero(str_num):
    if len(str_num) == 1:
        return str_num
    for i in range(len(str_num)):
        if str_num[i] > 0:
            break
    return str_num[i:]

def has_leading_zeros(num_str):
    if len(num_str) > 1 and num_str[0] == '0':
        return True
    return False

if __name__ == "__main__":
    print("Введите два числа a и b для получения разности:")
    a = input("a = ").strip()
    b = input("b = ").strip()
    if a.isdigit() and b.isdigit() and not has_leading_zeros(a) and not has_leading_zeros(b):
            print(subtract_strings(a, b))
    else:
        print("Введены некоректные данные")