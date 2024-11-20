
class YouTube:
    def __init__(self):
        self.observers = [] 
        self.video = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_channel(self, name):
        self.name = name
        self._notify_observers()

    def _notify_observers(self):
        for observer in self.observers:
            observer.update(self.name)

    def delete_channel(self, name):
        self.name = name
        self.notify_observers_delete()

    def notify_observers_delete(self): #Tengo que tener un notify para cada una de las acciones?
        for observer in self.observers:
            observer.close_channel(self.name)
