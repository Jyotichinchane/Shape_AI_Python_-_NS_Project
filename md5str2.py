import hashlib

# encode it to bytes using UTF-8 encoding
message = "Pooja Bhoskar".encode()

# hash with MD5 (not recommended)
print("MD5:", hashlib.md5(message).hexdigest())

# hash with SHA-2 (SHA-256 & SHA-512)

print("SHA-256:", hashlib.sha256(message).hexdigest())

print("SHA-512:", hashlib.sha512(message).hexdigest())

# hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())

print("SHA-3-512:", hashlib.sha3_512(message).hexdigest())