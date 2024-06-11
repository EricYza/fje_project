from abc import ABC, abstractmethod

# Abstract Component class
class Component(ABC):
    @abstractmethod
    def draw(self, level=0, icon=''):
        pass

# Leaf class representing a JSON leaf node
class Leaf(Component):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level=0, icon=''):
        return f"{'  ' * level}{icon}{self.name}: {self.value}\n"

# Container class representing a JSON container (composite node)
class Container(Component):
    def __init__(self, name, icon=''):
        self.name = name
        self.icon = icon
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def draw(self, level=0, icon=''):
        result = f"{'  ' * level}{icon}{self.name}\n"
        for child in self.children:
            result += child.draw(level + 1, icon)
        return result
