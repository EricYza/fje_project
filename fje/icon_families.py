from abc import ABC, abstractmethod

# IconFamily class
class IconFamily(ABC):
    @abstractmethod
    def get_middle_node_icon(self):
        pass

    @abstractmethod
    def get_leaf_node_icon(self):
        pass

class PokerFaceIconFamily(IconFamily):
    def get_middle_node_icon(self):
        return "♢"

    def get_leaf_node_icon(self):
        return "♤"
    
class DefaultIconFamily(IconFamily):
    def get_middle_node_icon(self):
        return ""

    def get_leaf_node_icon(self):
        return ""

# IconFamilyFactory class
class IconFamilyFactory(ABC):
    @abstractmethod
    def create_icon_family(self) -> IconFamily:
        pass

class PokerFaceIconFamilyFactory(IconFamilyFactory):
    def create_icon_family(self) -> IconFamily:
        return PokerFaceIconFamily()

class DefaultIconFamilyFactory(IconFamilyFactory):
    def create_icon_family(self) -> IconFamily:
        return DefaultIconFamily()
