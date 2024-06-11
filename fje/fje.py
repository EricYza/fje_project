import argparse
from styles import TreeStyleFactory, RectangleStyleFactory
from icon_families import PokerFaceIconFamilyFactory, DefaultIconFamilyFactory
from explorer import FunnyJsonExplorer

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='Visualization style')
    parser.add_argument('-i', '--icon', required=True, choices=['poker', 'default'], help='Icon family')
    
    args = parser.parse_args()
    
    # 选择样式工厂
    if args.style == 'tree':
        style_factory = TreeStyleFactory()
    elif args.style == 'rectangle':
        style_factory = RectangleStyleFactory()

    # 选择图标族工厂
    if args.icon == 'poker':
        icon_family_factory = PokerFaceIconFamilyFactory()
    elif args.icon == 'default':
        icon_family_factory = DefaultIconFamilyFactory()

    # 读取JSON文件
    with open(args.file, 'r') as file:
        json_data = file.read()

    # 构建FunnyJsonExplorer
    explorer = FunnyJsonExplorer(style_factory, icon_family_factory)

    # 显示JSON数据
    result = explorer.show(json_data)
    print(result)

if __name__ == "__main__":
    main()
