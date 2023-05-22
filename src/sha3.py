import hashlib

def sha3_256(data):
    hash_object = hashlib.sha3_256()
    hash_object.update(data)
    return hash_object.hexdigest()

def sha3_512(data):
    hash_object = hashlib.sha3_512()
    hash_object.update(data)
    return hash_object.hexdigest()