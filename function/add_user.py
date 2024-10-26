import csv


async def add_user(user_id, filename='./users.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and int(row[0]) == user_id:
                print(f'Пользователь {user_id} уже добавлен!')
                return  # Если пользователь уже есть, выходим из функции

    # Если пользователь не найден, добавляем его
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_id])
        print(f'Пользователь {user_id} добавлен!')
