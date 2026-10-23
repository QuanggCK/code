import urllib.request
import hashlib
url = input()

# Tải nội dung file từ URL
du_lieu = urllib.request.urlopen(url).read()

# Tính giá trị băm MD5
md5 = hashlib.md5(du_lieu).hexdigest()
# Tính giá trị băm SHA256
sha256 = hashlib.sha256(du_lieu).hexdigest()

print(md5)
print(sha256)
