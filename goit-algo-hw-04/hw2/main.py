def get_cats_info(path):
    list_cats = []
    try:
        with open(path, 'r', encoding='utf-8')as file:
            for line in file:
                id, name, age = line.strip().split(',')
                list_cats.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за вказаним шляхом '{path}' не знайдено.")
    except (IOError, OSError) as e:
        print(f"Помилка читання файлу, ймовірно вын пошкоджений: {e}")
    except ValueError as ve:
        print(f"Помилка при обробці даних: {ve} in line {line}.")
    finally:
        return list_cats

cats_info = get_cats_info("cats.txt")
print(cats_info)