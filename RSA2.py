from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
 
# Đối tượng key chứa cả 2 khóa riêng và công khai
key = RSA.generate(1024)        
privKeyPEM = key.export_key()
privKeyText = privKeyPEM.decode()
print(privKeyText)
 
pubKeyPEM = key.publickey().export_key()
pubKeyText = pubKeyPEM.decode()
print(pubKeyText)
 
#Mã hóa dùng RSA với padding PKCS1 OAEP:
 
sessionKey = bytes.fromhex(input())
pubKey = RSA.import_key(pubKeyPEM)
e_rsa = PKCS1_OAEP.new(pubKey)
encrypted = e_rsa.encrypt(sessionKey)
print(encrypted.hex())