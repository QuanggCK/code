import sys
def majority(b1, b2, b3):
    return 1 if (b1 + b2 + b3) >= 2 else 0

def tiny_a5_1_encrypt():
    x_str = input().strip()
    y_str = input().strip()
    z_str = input().strip()
    plaintext = input().strip()

    X = [int(b) for b in x_str]
    Y = [int(b) for b in y_str]
    Z = [int(b) for b in z_str]
    cx, cy, cz = 1, 5, 4
    taps_x = [2, 4, 5]
    taps_y = [6, 7]
    taps_z = [2, 7, 8]

    ciphertext = []
    for bit in plaintext:
        p = int(bit)
        s = X[-1] ^ Y[-1] ^ Z[-1]
        c = p ^ s
        ciphertext.append(str(c))
        maj = majority(X[cx], Y[cy], Z[cz])
        if X[cx] == maj:
            fx = 0
            for t in taps_x:
                fx ^= X[t]
            X = [fx] + X[:-1]

        if Y[cy] == maj:
            fy = 0
            for t in taps_y:
                fy ^= Y[t]
            Y = [fy] + Y[:-1]

        if Z[cz] == maj:
            fz = 0
            for t in taps_z:
                fz ^= Z[t]
            Z = [fz] + Z[:-1]

    print("".join(ciphertext))

if __name__ == "__main__":
    tiny_a5_1_encrypt()