#hashingPractice

Usage:
python hasher.py arg1
You can use as many args as you want, and they will be converted to hashes and returned alongside the salt in this format:
[hash,salt]

If a .txt file is provided,
each of the lines will be ran, eg:

passwords.txt

redfox2022

thisistotallymypassword

loremipsum,


3 results will come out in the form of:


[hash,salt]
[hash,salt]
