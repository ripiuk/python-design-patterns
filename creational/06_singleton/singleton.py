"""
Одинак — це породжуючий патерн,
який гарантує існування тільки одного об’єкта певного класу,
а також дозволяє дістатися цього об’єкта з будь-якого місця програми.

Ви не зможете просто взяти і використовувати клас, залежний від одинака,
в іншій програмі. Для цього доведеться емулювати там присутність одинака.
Найчастіше ця проблема проявляється при написанні юніт-тестів.

Багато програмістів вважають Одинака антипатерном,
тому його все рідше і рідше можна зустріти в Python-коді.

Переваги:
  Гарантує наявність єдиного екземпляра класу.
  Надає глобальну точку доступу до нього.
  Реалізує відкладену ініціалізацію об’єкта-одинака.
Недоліки:
  Порушує принцип єдиного обов’язку класу.
  Маскує поганий дизайн.
  Проблеми багатопоточності.
  Вимагає постійного створення Mock-об’єктів при юніт-тестуванні.
"""
from collections import namedtuple

Connection = namedtuple("Connection", ('host', 'port', 'password'))


class DatabaseMeta(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Database(metaclass=DatabaseMeta):

    def __init__(self, host: str, port: int, password: str):
        self.connection = Connection(host, port, password)

    def __str__(self):
        return "DB params: {}".format(self.connection)


if __name__ == "__main__":
    db1 = Database(host='localhost', port=3306, password='123')
    db2 = Database(host='localhost', port=22156, password='root')

    print(db1, db2, sep='\n')
    print(id(db1) == id(db2))


# ================ Output ================
# DB params: Connection(host='localhost', port=3306, password='123')
# DB params: Connection(host='localhost', port=3306, password='123')
# True
