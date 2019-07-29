"""
фабрика — это объект для создания других объектов.
Формально фабрика — это функция или метод, который возвращает объекты
изменяющегося прототипа или класса из некоторого вызова метода, который считается «новым».

Простая фабрика  — это класс, в котором есть один метод с большим условным оператором,
выбирающим создаваемый продукт. Этот метод вызывают с неким параметром, по которому
определяется какой из продуктов нужно создать. У простой фабрики, обычно, нет подклассов.
Простая фабрика генерирует экземпляр для клиента, не раскрывая никакой логики.

Когда использовать: Когда создание объекта — это не просто несколько присвоений,
а какая-то логика, тогда имеет смысл создать отдельную фабрику вместо повторения
одного и того же кода повсюду.
"""


class User:

    def __init__(self):
        print("Created simple user")


class Customer:

    def __init__(self):
        print("Created customer user")


class Admin:

    def __init__(self):
        print("Created admin user")


class UserFactory:

    def __init__(self, user_type: str):
        self.user_type = user_type
        self.users = {
            "user": User,
            "customer": Customer,
            "admin": Admin,
        }

    def create(self):
        user = self.users.get(self.user_type)
        if not user:
            Exception("Wrong user type")
        return user()


if __name__ == "__main__":
    UserFactory("admin").create()
    UserFactory("user").create()
    UserFactory("customer").create()


# ================ Output ================
# Created admin user
# Created simple user
# Created customer user
