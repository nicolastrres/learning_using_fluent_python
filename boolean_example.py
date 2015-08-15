
#  when a class doesn't have a __bool__ defined, or len, it returns True.
class MyClass():
    pass

a = MyClass()

print("It should return True:")
print(bool(a))

#  when a class have defined __bool__, the bool() method return that value
class MyClassWithBool():
    def  __bool__(self):
        return False

a = MyClassWithBool()
print("It should return False:")
print(bool(a))


#  when a class have not defined __bool__, the bool() return the value of __len__ (if it is 0 returns false) 

class MyClassWithoutBoolWithLen():
    def __len__(self):
        return 0

a = MyClassWithoutBoolWithLen()
print("It should return False:")
print(bool(a))

