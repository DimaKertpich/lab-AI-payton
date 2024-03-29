import re
import random

def bot_response(user_input):
    patterns = [
        
        (r"Доброго дня, я шукаю книгу на тему історії середньовіччя",
         "Звісно, я маю кілька цікавих пропозицій для вас.(повний збіг)"),
        (r"Чи є у вас книги на англійській мові?",
         "Так, ми маємо розділ з англійською літературою, включаючи книги різних жанрів.(повний збіг)"),

        
        (r"Я шукаю книгу про програмування",
         "У нас є кілька відмінних книг з програмування на {мови}, вибирайте за власним смаком.(використання замінювачів)"),
        (r"Я шукаю книгу для розвитку",
         "У нас є великий вибір книг для того, щоб розвинути {розвитку}, ви точно знайдете щось корисне.(використання замінювачів)"),

        
        (r"А що Ви можете сказати щодо умов праці?", "{Привітання}. Умови праці {умови праці}.(надання значень змінним у процесі зіставлення)"),
        (r"Які теми ви можете порекомендувати?", "Зараз вийшов новий бестселлер {назва бестселлеру}.(надання значень змінним у процесі зіставлення)"),

        
        (r"Ви вірите, що (.+)", "Важко сказати. Час покаже.(універсальний зразок)"),
        (r"Що ви можете сказати про (.+)", "Маємо багато цікавих творів на цю тему.(універсальний зразок)"),

        
        (r"Як ви ставитеся до (.+)?", ["Ми вітаємо різноманітні точки зору.", "Ми намагаємося бути об'єктивними в цьому питанні.(зіставлення більше ніж з одним зразком)"]),
        (r"Чи часто оновлюється ваш асортимент книг?", ["Ми стараємося оновлювати асортимент регулярно.", "Актуалізація асортименту відбувається залежно від новинок та популярних вимог.(зіставлення більше ніж з одним зразком)"])
    ]

    for pattern, response in patterns:
        
        match = re.match(pattern, user_input)
        if match:
            
            if isinstance(response, list):
                
                return random.choice(response)
            else:
                
                placeholders = re.findall(r"{(.*?)}", response)
                for placeholder in placeholders:
                    response = response.replace("{" + placeholder + "}", input(f"Введіть значення для {placeholder}: "))
                return response

    # Стандартна відповідь
    return "Вибачте, я не зрозумів ваш запит."


# Запуск програми
for _ in range(10):
    user_input = input("Користувач: ")
    response = bot_response(user_input)
    print("Бот:", response)

