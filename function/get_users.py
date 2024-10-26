import csv


async def get_users(filename='./users.csv'):
    user_ids = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # проверка на пустую строку
                    user_ids.append(int(row[0]))
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError:
        print("Ошибка: В файле присутствуют некорректные данные.")
    return user_ids
