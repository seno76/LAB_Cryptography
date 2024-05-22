from SumLongNumbers_2 import add_strings as sum_
from SubstractLongNumber_3 import subtract_strings as sub_
from DivideLongNumber_2 import divide_strings as div_
from MultiplyLongNumber_2 import multiply_strings as mul_
from PowLongNumber_2 import pow_
from random import randint
import os
import time

t = 1e9

alphabet =  {
        "а": "499", "б": "411", "в": "412", "г": "413", "д": "414",
        "е": "415", "ж": "416", "з": "417", "и": "418", "й": "419",
        "к": "211", "л": "111", "м": "112", "н": "113", "о": "114",
        "п": "115", "р": "116", "с": "117", "т": "118", "у": "119",
        "ф": "221", "х": "121", "ц": "122", "ч": "123", "ш": "124",
        "щ": "125", "ъ": "126", "ы": "127", "ь": "128", "э": "129",
        "ю": "231", "я": "131", "А": "132", "Б": "133", "В": "134",
        "Г": "135", "Д": "136", "Е": "137", "Ж": "138", "З": "139",
        "И": "341", "Й": "141", "К": "142", "Л": "143", "М": "144",
        "Н": "145", "О": "146", "П": "147", "Р": "148", "С": "149",
        "Т": "351", "У": "151", "Ф": "152", "Х": "153", "Ц": "154",
        "Ч": "155", "Ш": "156", "Щ": "157", "Ъ": "158", "Ы": "159",
        "Ь": "361", "Э": "161", "Ю": "162", "Я": "163", "1": "164",
        "2": "165", "3": "166", "4": "167", "5": "168", "6": "169",
        "7": "371", "8": "171", "9": "172", "0": "173", ".": "174",
        ",": "175", "!": "176", "?": "177", "-": "178", ":": "179",
        ";": "189", "{": "181", "}": "182", "[": "183", "]": "184",
        "'": "185", "\"": "186", " ": "187", "\n": "188" , "ё": "999",
        "Ё": "997"
}

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

def mod_(neg_val, n):
    sub = sub_(n, neg_val[1])
    while sub[0] == "-":
        n = sum_(n, n)
        sub = sub_(n, neg_val[1])
    return sub

def jacobi(a, n):
    a = div_(a, n)[1]
    t = "1"
    while (a != "0"):
        while div_(a, "2")[1] == "0":
            a = div_(a, "2")[0] 
            r = div_(n, "8")[1]
            if r == "3" or r == "5":
                if t[0] == "-":
                    t = t[1]
                else:
                    t = "-" + t
        r = n
        n = a
        a = r
        if div_(a, "4")[1] == "3" and div_(n, "4")[1] == "3":
            if t[0] == "-":
                t = t[1]
            else:
                t = "-" + t
        a = div_(a, n)[1]
    if n == "1":
        return t
    else:
        return "0"

def del_leading_zero(str_num):
    for i, el in enumerate(list(str_num)):
        if el != "0":
            return "".join(str_num[i:])
    return "0"

def strassen_test(n):
    n = del_leading_zero(n)
    for _ in range(10):
        a = str(randint(2, int(n) - 1))
        if is_bigger(gcd_(a, n), "1"):
            return False
        int_div = div_(sub_(n, "1"), "2")[0]
        val = jacobi(a, n)
        if val[0] == "-":
            mod_n = mod_(val, n)
        else:
            mod_n = div_(val, n)[1]
        pow_a = pow_(a, int_div, n)
        if mod_n != div_(pow_a, n)[1]:
            return False
    return True
        
def phi(n):
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            count = 0
            while n % p == 0:
                n //= p
                count += 1
            result *= pow((p - 1) * p, (count - 1))
        if p == 2:
            p = 3
        else:
            p += 2
    if n > 1:
        result *= n - 1
    return str(result)

def is_primitive_root(g, m):
    g, m = int(g), int(m)
    phi_ = int(phi(m))
    factors = set()
    t = phi_
    for p in range(2, int(phi_**0.5) + 1):
        if t % p == 0:
            factors.add(p)
            while t % p == 0:
                t //= p
    if t > 1:
        factors.add(t)
    for p in factors:
        if pow(g, phi_ // p, m) == 1:
            return False
    return pow(g, phi_, m) == 1

def find_primitive_root(p):
    start = randint(3, int(p))
    for g in range(start, int(p)):
        if is_primitive_root(str(g), p):
            return str(g)
    return find_primitive_root(p)

def gen_key(p):

    if len(p) < 17:
        g = str(find_primitive_root(p))
    else:
        time.sleep(randint(120, 200))
        g = str(randint(3, int(p)))

    x = str(randint(2, int(p) - 2))
    y = pow_(g, x, p)

    with open("primary_key.txt", "w", encoding="utf-8") as f:
        f.write(x)

    with open("public_key.txt", "w", encoding="utf-8") as f:
        f.write(f"{y}:{g}:{p}")

    return y, g

def transform_text(text):
    low_text = text.lower()
    transform_txt = ""
    str_ = ""
    lst_chars = alphabet.keys()
    for char in low_text:
        if char in lst_chars or char in lst_chars or char.isdigit():
            transform_txt += alphabet[char]
            str_ += char
    print(f"Строка после удаления:\n{str_}")
    return transform_txt

def get_chanks(enc_text, pattren):
    len_pattern = len(pattren)
    lst_chanks = []
    i = 0
    for _ in range(len(enc_text)):
        if is_bigger(pattren, enc_text[i: i + len_pattern]):
            lst_chanks.append(enc_text[i: i + len_pattern])
            i = i + len_pattern
        else:
            lst_chanks.append(enc_text[i: i + len_pattern - 1])
            i = i + len_pattern - 1
    return lst_chanks[:lst_chanks.index('')]

def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

def write_table_chars():
    alphabet_ = open("alphabet.txt", "w", encoding="utf-8")
    for key in alphabet.keys():
        alphabet_.write(f"{key} - {alphabet[key]}\n")
    alphabet_.close()

def encrypt_elgamal(p, file_path, y=None, g=None):

    if y == None or g == None:
        y, g = gen_key(p)
    

    output_file = open("encode.txt", "w", encoding="utf-8")
    encode_file = open("enc_chars.txt", "w", encoding="utf-8")

    with open(file_path, "r", encoding="utf-8") as in_file:
       text = in_file.read()
       text = transform_text(text)
       print(f"Полученная строка после кодировки: {text}")
       
    encode_file.write(text)
    encode_file.close()
    
    lst_chanks = get_chanks(text, p)
    print(f"Полученное разбиение по блоками для числа p = {p}:")
    for i, block in enumerate(lst_chanks):
        print(f"{i + 1}) {block}")
    
    pairs = ""

    print("Полученные закодированные блоки (a, b): ")
    for i, chr_ in enumerate(lst_chanks):

        k = str(randint(2, int(p) - 2))
        a = pow_(g, k, p)
        buff = pow_(y, k, p)
        b = mul_(chr_, buff)
        pairs += f"({a} {b}),"
        print(f"{i + 1}) ({a} {b})")

    output_file.write(pairs[:-1])
    
    output_file.close()

def decode_(code_text):
    dec_ = ""
    for i in range(0, len(code_text), 3):
        pat = code_text[i:i + 3]
        dec_ += find_key_by_value(alphabet, pat)
        
    return dec_

def decrypt_elgamal(file_path, primary_key, public_key):

    with open(primary_key, "r", encoding="utf-8") as f:
        x = f.read()
    
    with open(public_key, "r", encoding="utf-8") as f:
        _, _, p = f.read().split(":")

    dec_file_1 = open("decode_1.txt", "w", encoding="utf-8")
    dec_file_2 = open("decode_2.txt", "w", encoding="utf-8")

    with open(file_path, "r", encoding="utf-8") as enc_file:

        encode_txt = enc_file.read().split(",")
        decode_text = ""

        for val in encode_txt:
            if val != '':

                pair = val.split()
                a = pair[0][1:]
                b = pair[1][:-1]
                
                sub_p_x = sub_(p, x)
                exp = sub_(sub_p_x, "1")
                buff = pow_(a, exp, p)
                m = div_(mul_(b, buff), p)[1]

            decode_text += m 

        dec_file_1.write(decode_text)
        dec_file_2.write(decode_(decode_text))
    
    dec_file_1.close()
    dec_file_2.close()

def get_keys_from_file(f1, f2):
    prim_key = open(f1, "r")
    public_key = open(f2, "r")

    x = prim_key.read()
    y, g, p = public_key.read().split(":")

    public_key.close()
    prim_key.close()
    return x, y, g, p

if __name__ == "__main__":

    print("Укажите режим работы (enc - шифрование / dec - расшифрование / gen - генерация ключей):")
    flag = False

    while not flag:
        try:
            type_ = input("Режим = ")
            
            match type_:

                case "enc":

                    write_table_chars()
                    print("Использовать старые ключи или сгенерировать новые? (new / old):")
                    while True:
                        val = input("Тип используемых ключей: ") 
                        if val in ("new", "old"):
                            break

                    if val == "old":
                        if os.path.getsize("primary_key.txt") == 0 or os.path.getsize("public_key.txt") == 0:
                            print("Ключи не существуют, будут сгенерированы новые:")
                            while True:
                                p = input("Введите простое число p: ")
                                if strassen_test(p):
                                    break
                                else:
                                    print("Заданное число не является простым!")
                            gen_key(p)
                        flag = True
                        path_file = input("Укажиете путь к файлу для шифрования: ")

                        prim_key = open("primary_key.txt", "r")
                        public_key = open("public_key.txt", "r")

                        x = prim_key.read()
                        y, g, p = public_key.read().split(":")

                        prim_key.close()
                        public_key.close()

                        start = time.perf_counter_ns()
                        encrypt_elgamal(p, path_file, y, g)
                        end = time.perf_counter_ns()

                        x, y, g, p = get_keys_from_file("primary_key.txt", "public_key.txt")

                        print(f"Приватный ключ: {x}")
                        print(f"Публичный ключ: {y} {g} {p}")
                        print(f"Время шифрования сообщения: {(end - start) / t} sec.")
                        print("Зашифрованный файл - encode.txt")
                    else:
                        while True:
                            p = input("Введите простое число p: ")
                            if strassen_test(p):
                                break
                            else:
                                print("Заданное число не является простым!")

                        flag = True
                        path_file = input("Укажиете путь к файлу для шифрования: ")

                        start = time.perf_counter_ns()
                        encrypt_elgamal(p, path_file)
                        end = time.perf_counter_ns()

                        x, y, g, p = get_keys_from_file("primary_key.txt", "public_key.txt")

                        print(f"Приватный ключ: {x}")
                        print(f"Публичный ключ: {y} {g} {p}")
                        print(f"Время шифрования сообщения: {(end - start) / t} sec.")
                        print("Зашифрованный файл - encode.txt")

                case "dec":

                    write_table_chars()
                    flag = True
                    path_file = input("Укажиете путь к файлу для дешифрования: ")

                    start = time.perf_counter_ns()
                    decrypt_elgamal(path_file, "primary_key.txt", "public_key.txt")
                    end = time.perf_counter_ns()

                    x, y, g, p = get_keys_from_file("primary_key.txt", "public_key.txt")

                    print(f"Приватный ключ: {x}")
                    print(f"Публичный ключ: {y} {g} {p}")
                    print(f"Время расшифровки сообщения: {(end - start) / t} sec.")
                    print("Дешифрованный файл - decode_2.txt")

                case "gen":

                    write_table_chars()
                    while True:
                        p = input("Введите простое число p: ")
                        if strassen_test(p):
                            flag = True 
                            break
                        else:
                            print("Заданное число не является простым!")

                    start = time.perf_counter_ns()
                    gen_key(p)
                    end = time.perf_counter_ns()

                    x, y, g, p = get_keys_from_file("primary_key.txt", "public_key.txt")

                    print(f"Приватный ключ: {x}")
                    print(f"Публичный ключ: {y} {g} {p}")
                    print(f"Время генерации ключей: {(end - start) / t} sec.")
                    
                case _:
                    
                    print("Введен некорректный режим!")

        except Exception as err:

            print("Произошла ошибка!!")
            print(err)