def total_salary(path):
    total = 0
    count = 0
    average = 0

    try:
        with open(path, 'r', encoding='utf-8')as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        if count == 0:
            average = 0
        else:
            average = total / count

    except FileNotFoundError:
        print(f"Файл за вказаним шляхом '{path}' не знайдено.")
    except (IOError, OSError) as e:
        print(f"Помилка читання файлу, ймовірно вын пошкоджений: {e}")
    except ValueError as ve:
        print(f"Помилка при обробці даних: {ve}.")
    finally:
        return total, average
    
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")