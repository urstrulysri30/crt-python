db = [
    {'saiteja': '123'},
    {'david': '456'},
    {'sri': '789'}
]
print(db)
username = input("enter username :")
password = input("enter password :")
temp = {username: password}
if temp in db:
    print("login success")
else:
    print("invalid credentials")
