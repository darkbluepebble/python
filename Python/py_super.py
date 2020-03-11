from py_ex import MessageUser, some_func

obj=MessageUser()
obj.add_user("Justin",123.32,'hello@teamcpe.com')
obj.add_user("jOhn",94.23)
obj.add_user("EmiLee",93.23)
obj.add_user("JiM",193.23)
obj.add_user("Ron",13.32)

obj.get_details()

print(obj.make_messages())

some_func()
