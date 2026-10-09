from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

sessionKey = bytes.fromhex(input().strip())

# 1. Sinh cặp khóa RSA 1024 bit, xuất PEM
key = RSA.generate(1024)
privKeyPEM = key.export_key()
pubKeyPEM = key.publickey().export_key()
print(privKeyPEM.decode())
print(pubKeyPEM.decode())

# 2. Mã hóa khóa phiên bằng khóa công khai (OAEP)
pubKey = RSA.import_key(pubKeyPEM)
encrypted = PKCS1_OAEP.new(pubKey).encrypt(sessionKey)
print(encrypted.hex())

# 3. Giải mã bằng khóa riêng
privKey = RSA.import_key(privKeyPEM)
decrypted = PKCS1_OAEP.new(privKey).decrypt(encrypted)
print(decrypted.hex())