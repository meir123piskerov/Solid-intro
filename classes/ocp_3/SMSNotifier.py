from classes.ocp_3.Notifier import Notifier


class SMSNotifier(Notifier):
    def __init__(self, massage):
        self.massage = massage

    def send(self):
        print(self.massage)