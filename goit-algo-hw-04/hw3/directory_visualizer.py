import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init()

def visualize_directory(path: Path, indent: str = ""):
    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не існує або це не директорія.{Style.RESET_ALL}")
        return
    
    # Проходимося по всіх елементах у директорії
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")  # Директорії в синьому
            visualize_directory(item, indent + "    ")  # Рекурсивно для піддиректорій
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")  # Файли в зеленому

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python directory_visualizer.py <шлях_до_директорії>{Style.RESET_ALL}")
        return

    dir_path = Path(sys.argv[1])
    visualize_directory(dir_path)

if __name__ == "__main__":
    main()
