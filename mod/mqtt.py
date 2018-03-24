from mod.modular import Modular


class Mqtt(Modular):
    def publish(self):
        print("publish")