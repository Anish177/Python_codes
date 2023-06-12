import hashlib
import itertools

def crack_hash(hash_to_crack, pwd_len, salt_len):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
    pwd = "Tk" + "".join(["*"] * (pwd_len-2))
    salt_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    salt = "".join(["X"] * salt_len)
    
    for pwd_chars in itertools.product(chars, repeat=pwd_len-2):
        pwd = "Tk" + "".join(pwd_chars)
        for s in itertools.product(salt_chars, repeat=salt_len):
            salt = "".join(s)
            candidate = pwd + salt
            hash = hashlib.sha256(candidate.encode()).hexdigest()
            print(candidate)
            if hash == hash_to_crack:
                return pwd, salt
    return None, None

hash_to_crack = "eda840a3afb5533ec63900558435272a05b954152cba8fadcd190352d789ecd6"
pwd_len = 9
salt_len = 4
pwd, salt = crack_hash(hash_to_crack, pwd_len, salt_len)

if pwd is not None:
    print(f"Password: {pwd}")
    print(f"Salt: {salt}")
else:
    print("Password not found")
