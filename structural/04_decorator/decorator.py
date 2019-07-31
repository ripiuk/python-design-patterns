"""
Декоратор — це структурний патерн, який дозволяє додавати
в режимі реального часу нові поведінки об’єктам,
розміщаючи їх в об’єктах-обгортках.

Декоратор дозволяє загортати об’єкти безліч разів завдяки тому,
що і обгортки, і реальні об’єкти, що загортаються, мають спільний інтерфейс.

Переваги:
  Більша гнучкість, ніж у спадкування.
  Дозволяє додавати обов’язки «на льоту».
  Можна додавати кілька нових обов’язків одразу.
  Дозволяє мати кілька дрібних об’єктів, замість одного об’єкта «на всі випадки життя».
Недоліки:
  Важко конфігурувати об’єкти, які загорнуто в декілька обгорток одночасно.
  Велика кількість крихітних класів.

The “Decorator Pattern” ≠ Python “decorators”!
"""


class Notification:

    def __init__(self, text: str):
        self.text = text

    def send(self) -> str:
        print("Sent through Email: {}".format(self.text))
        return self.text


class TelegramNotification(Notification):

    def __init__(self, wrapped: Notification):
        self.wrapped = wrapped

    def send(self) -> str:
        text = self.wrapped.send()
        print("Sent through Telegram: {}".format(text))
        return text


class SlackNotification(Notification):

    def __init__(self, wrapped: Notification):
        self.wrapped = wrapped

    def send(self) -> str:
        text = self.wrapped.send()
        print("Sent through Slack: {}".format(text))
        return text


if __name__ == "__main__":
    notification = Notification("Please fix this bug ASAP")
    urgent_notification = SlackNotification(TelegramNotification(notification))

    notification.send()
    print("-" * 50)
    urgent_notification.send()


# ================ Output ================
# Sent through Email: Please fix this bug ASAP
# --------------------------------------------------
# Sent through Email: Please fix this bug ASAP
# Sent through Telegram: Please fix this bug ASAP
# Sent through Slack: Please fix this bug ASAP
