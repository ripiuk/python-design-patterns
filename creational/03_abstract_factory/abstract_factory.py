"""
Абстрактна фабрика — це породжуючий патерн проектування,
який вирішує проблему створення цілих сімейств пов’язаних продуктів,
без прив’язки коду до конкретних класів продуктів.

Абстрактна фабрика задає інтерфейс створення всіх доступних типів продуктів,
а кожна конкретна реалізація фабрики породжує продукти однієї з варіацій.
Клієнтський код викликає методи фабрики для отримання продуктів,
замість самостійного створювання їх за допомогою оператора new.
При цьому, фабрика сама стежить за тим, щоб створюваний продукт був потрібної варіації.

Переваги:
    Гарантує поєднання створюваних продуктів.
    Звільняє клієнтський код від прив’язки до конкретних класів продукту.
    Виділяє код виробництва продуктів в одне місце, спрощуючи підтримку коду.
    Спрощує додавання нових продуктів до програми.
    Реалізує принцип відкритості/закритості.
Недоліки:
    Ускладнює код програми внаслідок введення великої кількості додаткових класів.
    Вимагає наявності всіх типів продукту в кожній варіації.

Абстрактная фабрика  — это устройство классов, облегчающее создание семейств продуктов.
Что такое семейство продуктов? Например, классы Транспорт + Двигатель + Управление.
Вариациями этого семейства могут стать:
    Автомобиль + ДвигательВнутренннегоСгорания + Руль
    Самолет + РеактивныйДвигатель + Штурвал
Если у вас нет семейств продуктов, значит не может быть и абстрактной фабрики.
"""
import platform
from abc import ABC, abstractmethod


# ====== Buttons ======

class Button(ABC):

    @abstractmethod
    def design(self) -> None:
        pass


class WinButton(Button):

    def design(self):
        print("Here are some instructions of how to draw windows button")


class LinuxButton(Button):

    def design(self):
        print("Here are some instructions of how to draw linux button")


class MacButton(Button):

    def design(self):
        print("Here are some instructions of how to draw mac button")


# ====== Text Areas ======

class TextArea(ABC):

    @abstractmethod
    def design(self):
        pass


class WinTextArea(TextArea):

    def design(self):
        print("Here are some instructions of how to draw windows text area")


class LinuxTextArea(TextArea):

    def design(self):
        print("Here are some instructions of how to draw linux text area")


class MacTextArea(TextArea):

    def design(self):
        print("Here are some instructions of how to draw mac text area")


# ====== Factories ======

class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_area(self) -> TextArea:
        pass


class WinFactory(GUIFactory):

    def create_button(self) -> WinButton:
        print("Creating windows button")
        return WinButton()

    def create_text_area(self) -> WinTextArea:
        print("Creating windows text area element")
        return WinTextArea()


class LinuxFactory(GUIFactory):

    def create_button(self) -> LinuxButton:
        print("Creating linux button")
        return LinuxButton()

    def create_text_area(self) -> LinuxTextArea:
        print("Creating linux text area element")
        return LinuxTextArea()


class MacFactory(GUIFactory):

    def create_button(self) -> MacButton:
        print("Creating linux button")
        return MacButton()

    def create_text_area(self) -> MacTextArea:
        print("Creating linux text area element")
        return MacTextArea()


# ====== Application ======

class Application:

    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.text_area = factory.create_text_area()

    def draw(self):
        self.button.design()
        self.text_area.design()


if __name__ == "__main__":
    platform_factories = {
        "Linux": LinuxFactory,
        "Windows": WinFactory,
        "MacOS": MacFactory,
    }
    my_os = platform.system()

    os_factory = platform_factories.get(my_os)
    if not os_factory:
        Exception("Unknown operation system")

    os_factory = os_factory()

    app = Application(os_factory)
    app.draw()


# ================ Output ================
# Creating linux button
# Creating linux text area element
# Here are some instructions of how to draw linux button
# Here are some instructions of how to draw linux text area
