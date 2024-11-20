from abc import ABC, abstractmethod

class GameCharacter:
    def performe_action(self):
        self.introduccion()
        self.primary()
        self.secondary()
        self.ulti()

    @abstractmethod
    def introduccion(self):
        pass

    @abstractmethod
    def primary(self):
        pass

    @abstractmethod
    def secondary(self):
        pass

    @abstractmethod
    def ulti(self):
        pass