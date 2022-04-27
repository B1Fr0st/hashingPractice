#hasher.py
import hashlib,secrets,string

def h256(hashStr:str) -> str:
    """Easier way to hash a string using SHA-256"""
    return hashlib.sha256(hashStr.encode("utf-8")).hexdigest()
def saltPassword(password:str,saltLength:int=64) -> str:
    saltStr = ""
    for i in range(0,saltLength):
        saltStr = saltStr+secrets.choice(string.ascii_letters)
    return [password+saltStr,saltStr]
def hashPassword(password:str) -> str:
    """
    CRITICAL: PASSWORD SHOULD NOT BE SALTED, UNLESS IT IS BEING CALLED RECURSIVELY ON PURPOSE
    Returns a salted and hashed password, along with the salt.
    """
    saltedPass = saltPassword(password)
    return [h256(saltedPass[0]),saltedPass[1]]