from abc import ABC, abstractmethod
from components import Container, Leaf  # 确保导入了 Leaf 和 Container 类

# JSONStyle class
class JSONStyle(ABC):
    @abstractmethod
    def render(self, data, icon_family):
        pass
    
    def _draw_node(self, node, level, icon_family, is_last, is_first_level):
        pass

class TreeStyle(JSONStyle):
    def render(self, data, icon_family):
        return self._draw_tree(data, 0, icon_family, is_last=True, is_first_level=True)

    def _draw_tree(self, node, level, icon_family, is_last, is_first_level):
        result = ""
        for i, child in enumerate(node.children):
            result += self._draw_node(child, level, icon_family, i == len(node.children) - 1, is_first_level)
        return result

    def _draw_node(self, node, level, icon_family, is_last, is_first_level):
        # Only add a vertical line at the first level
        if level == 0 and not is_last:
            indent = '│  '
        else:
            indent = '   '

        branch = '└─ ' if is_last else '├─ '
        icon = icon_family.get_middle_node_icon() if isinstance(node, Container) else icon_family.get_leaf_node_icon()

        result = f"{indent * level}{branch}{icon}{node.name}\n"
        if isinstance(node, Container):
            for i, child in enumerate(node.children):
                result += self._draw_node(child, level + 1, icon_family, i == len(node.children) - 1, False)
        elif isinstance(node, Leaf):
            result = f"{indent * level}{branch}{icon}{node.name}: {node.value}\n"
        return result

class RectangleStyle(JSONStyle):
    def render(self, data, icon_family):
        lines = self._draw_rectangle(data, 0, icon_family, is_last=True)
        width = max(len(line) for line in lines)
        result = self._add_borders(lines, width)
        return result

    def _draw_rectangle(self, node, level, icon_family, is_last):
        lines = []
        self._draw_node(node, level, icon_family, is_last, lines)
        return lines

    def _draw_node(self, node, level, icon_family, is_last, lines):
       
        indent = '│  ' * (level - 1) + ('└─ ' if is_last else '├─ ')
        icon = icon_family.get_middle_node_icon() if isinstance(node, Container) else icon_family.get_leaf_node_icon()
        if isinstance(node, Leaf):
           
            line = f"{indent}{icon}{node.name}: {node.value}"
            lines.append(line)
        else:
            #针对level=1的第一个节点的indent=┌─
            if level == 1:
                indent="┌─ "
                if is_last:
                    indent="├─ "
            line = f"{indent}{icon}{node.name}"
            if node.name == "root":
                indent="┌─ "
                line = f"{indent}{icon}{node.name}"
            else: lines.append(line)
            for i, child in enumerate(node.children):
                self._draw_node(child, level + 1, icon_family, i == len(node.children) - 1, lines)

    def _add_borders(self, lines, width):
        bordered_lines = []
        border_top = '─' * width
        #result = f"┌─{border_top}─┐\n"
        result=""
        for i, line in enumerate(lines):
            filled_line = line + '─' * (width - len(line))
            if i == 0:
                result += f"{filled_line}┐\n"
            elif i < len(lines) - 1:
                result += f"{filled_line}┤\n"
            else:
                #将filled_line的第一个字符改为└─ 
                filled_line="└─"+filled_line[2:]
                result += f"{filled_line}┘\n"
        #result += f"└─{'─' * (width)}─┘\n"
        return result

# JSONStyleFactory class
class JSONStyleFactory(ABC):
    @abstractmethod
    def create_style(self) -> JSONStyle:
        pass

class TreeStyleFactory(JSONStyleFactory):
    def create_style(self) -> JSONStyle:
        return TreeStyle()

class RectangleStyleFactory(JSONStyleFactory):
    def create_style(self) -> JSONStyle:
        return RectangleStyle()
