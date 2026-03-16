import sys

password = sys.argv[1]

have_num = any(i.isdigit() for i in password)

sp_char = "!@#$%^&*"
have_sp_char = any(i in sp_char for i in password)

if len(password) >= 8 and (have_sp_char or have_num):
    print("strong")
else:
    print("weak")