from datetime import datetime
import bisect, random, re

# Завдання 1
# Перетворення рядка дати у об'єкт datetime
def string_to_date(date_string):    
    return datetime.strptime(date_string, "%Y-%m-%d")
    
# Повернення різниці у днях як ціле число
def get_days_from_today(data):
    try:
        return (datetime.today() - string_to_date(data)).days
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

# Завдання 2
def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    if min >= 1 and max <= 1000 and max > min and max - min +1 >= quantity :
        cnt = 0        
        while cnt < quantity:
            num = random.randint(min, max)
            if num not in lottery_numbers:
                bisect.insort(lottery_numbers, num)
                cnt = cnt + 1
        return lottery_numbers            
    else:
        return lottery_numbers

# Завдання 3
def normalize_phone(phone_number):
    # Залишаємо тільки цифри та символ '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)    
    # Перевіряємо, чи містить номер міжнародний код
    # Додаємо код країни '+38', якщо номер не містить міжнародного коду
    if not cleaned_number.startswith('+'):
        if not cleaned_number.startswith('38'):            
            cleaned_number = '+38' + cleaned_number
        else:
            cleaned_number = '+' + cleaned_number
    return cleaned_number


print(datetime.today())
print(string_to_date('2024-09-20'))
print(get_days_from_today('2024-09-20'))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
