def divide_strings(dividend_str, divisor_str):

    divisor = int(divisor_str)

    quotient = ''
    remainder = 0

    for digit in dividend_str:
        
        current_value = remainder * 10 + int(digit)

        current_quotient = current_value // divisor
        current_remainder = current_value % divisor
    
        quotient += str(current_quotient)
        remainder = current_remainder

    quotient = quotient.lstrip('0')

    if not quotient:
        quotient = '0'

    return quotient, str(remainder)

def del_leading_zero(arr):
    for i, el in enumerate(arr):
        if el != 0:
            return arr[i:]
    return [0]

def str_to_arr(str):
    return [int(el) for el in str]

# ----------------------------------------------------------

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
    for i in range(max_len - 1, -1, -1):
        diff = (int(str1[i]) - int(str2[i]) + k) % 10
        k = (int(str1[i]) - int(str2[i]) + k) // 10
        res.append(diff)
    res.reverse()

    return res, negative


# ---------------------------------------------------------

def multiply_strings(u, v):
    w = [0] * (len(u) + len(v))
    for j in range(len(v) - 1, -1, -1):
        k = 0
        for i in range(len(u) - 1, -1, -1):
            temp_val = int(u[i]) * int(v[j]) + w[i + j + 1] + k
            k = temp_val // 10
            w[i + j + 1] = temp_val % 10
        w[j] += k
    return w


# -----------------------------------------------------------

def add_strings(str1, str2):
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)
    carry, result = 0, []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(str1[i]) + int(str2[i]) + carry
        carry = digit_sum // 10
        result.append(digit_sum % 10)
    if carry:
        result.append(carry)
    return result[::-1]


# ------------------------------------------------------------------------

def to_str(arr):
    return "".join([str(i) for i in arr])

# -------------------------------------------------------------------------

def div_(u, v, b=10):

    if v == "0":
        return None
    
    if u == "0" :
        return ("0", "0")

    n = len(v)
    m = len(u) - n
    q = [0] * (m + 1)

    if n > len(u):
        return "0", u

    d = b // (int(v[0]) + 1)

    u = multiply_strings(u, str(d))
    v = multiply_strings(v, str(d))

    u.reverse()
    v.reverse()

    j = m

    while j >= 0:

        q_hat = (u[j + n] * b + u[j + n - 1]) // v[n - 1]
        r_hat = (u[j + n] * b + u[j + n - 1]) % v[n - 1]

        if q_hat == b or q_hat * v[n - 2] > b * r_hat + u[j + n - 2]:
            q_hat -= 1
            r_hat += v[n - 1]

            if r_hat < b and (q_hat == b or q_hat * v[n - 2] > b * r_hat + u[j + n - 2]):
                q_hat -= 1
                r_hat += v[n - 1]

        u_j = u[j: j + n + 1]

        # not rev
        u_j.reverse()
        v.reverse()

        # not rev
        sub = multiply_strings(str(q_hat), to_str(v))[1:]

        if sub[0] == 0:
            sub = sub[1:]

        sub_res, negative = subtract_strings(to_str(u_j), to_str(sub))
        sub_res = sub_res[1:]

        if negative:
            b_ = [1] + [0] * (n + 1)
            sub_res = subtract_strings(to_str(b_), to_str(sub_res))[0][1:]

        q[j] = q_hat

        # rev
        sub_res.reverse()

        u = u[:j] + sub_res + u[j + n + 1:]

        sub_res.reverse()
        if negative:
            q[j] -= 1
            sub_res = add_strings(to_str(sub_res), to_str(v))
            sub_res = sub_res[1:]

        sub_res.reverse()
        u = u[:j] + sub_res + u[j + n + 1:]

        j -= 1

        v.reverse()

    q.reverse()
    u.reverse()

    q = to_str(del_leading_zero(q))
    u = to_str(del_leading_zero(u))

    return q, divide_strings(u, str(d))[0]


def has_leading_zeros(num_str):
    if len(num_str) > 1 and num_str[0] == '0':
        return True
    return False

if __name__ == "__main__":
    print("Введите два числа a и b для получения разности:")
    a = input("a = ").strip()
    b = input("b = ").strip()
    if a.isdigit() and b.isdigit() and not has_leading_zeros(a) and not has_leading_zeros(b):
            result = div_(a, b)
            if result == None:
                print("Введены некоректные данные")
            else:
                print("Целая часть:", result[0])
                print("Остаток:", result[1])
    else:
        print("Введены некоректные данные")