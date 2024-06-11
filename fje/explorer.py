import json
from components import Container, Leaf

class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_family_factory):
        self.style = style_factory.create_style()
        self.icon_family = icon_family_factory.create_icon_family()

    def show(self, json_data):
        data_structure = self._load(json_data)
        return self.style.render(data_structure, self.icon_family)

    def _load(self, json_data):
        def build_component(data, name="root"):
            if isinstance(data, dict):
                container = Container(name)
                for key, value in data.items():
                    container.add(build_component(value, key))
                return container
            else:
                return Leaf(name, data)

        parsed_data = json.loads(json_data)
        return build_component(parsed_data)
