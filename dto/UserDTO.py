from classLibrary.User import User
def GetUserByPhone(phone:str):
    user = User.select().where(User.phone == phone).get()
    return user
def RegistrationUser():
    name = input("введите имя пользователя")
    phone = input("введите номер телефона")
    user = User(name=name,phone=phone,bouns=0)
    user.save()
