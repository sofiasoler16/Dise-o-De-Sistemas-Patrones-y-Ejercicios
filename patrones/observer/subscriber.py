

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, newVideo):
        print("Notificacion para ", self.name, ": salio un video nuevo de ", newVideo)

    def close_channel(self, channel):
        print("El canal ", channel, "ha cerrado para siempre :(")
        
        