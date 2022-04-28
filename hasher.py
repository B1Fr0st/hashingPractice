#hasher.py
import hashlib,secrets,string,sys
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
    return [hashlib.sha256(saltedPass[0].encode("utf-8")).hexdigest(),saltedPass[1]]
if sys.argv:
    for arg in range(1,len(sys.argv)):
        if ".txt" in sys.argv[arg] == False:
            print(hashPassword(sys.argv[arg]))
        elif ".txt" in sys.argv[arg]:
            with open(sys.argv[arg],"r") as passwords:
                passwords = passwords.readlines()
                for password in passwords:
                    print(hashPassword(password))
        