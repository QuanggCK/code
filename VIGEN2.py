def VIGEN2():
    cipher_text = input()
    plaint_text = input()

    n = len(cipher_text)

    full_key_stream = []
    for i in range(n):
        c_val = ord(cipher_text[i]) - ord('A')
        p_val = ord(plaint_text[i]) - ord('A')

        k_val = (c_val - p_val) % 26
        full_key_stream.append(chr(k_val + ord('A')))

    full_key_str = ''.join(full_key_stream)

    for L in range(2, n + 1):
        is_valid = True
        for i in range(n):
            if full_key_str[i] != full_key_str[i%L]:
                is_valid = False
                break
        if is_valid:
            print(full_key_str[:L])
            return

if __name__ == "__main__":
    VIGEN2()