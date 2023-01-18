from random import randint, uniform, choice
from typing import Union, Generator

import faker

BOOKS_LABELS = ['Властелин колец', 'Гордость и предубеждение', 'Тёмные начала', 'Автостопом по галактике',
                'Гарри Поттер и Кубок огня', 'Убить пересмешника', 'Винни Пух', '1984',
                'Лев, колдунья и платяной шкаф', 'Джейн Эйр', 'Уловка-22', 'Грозовой перевал', 'Пение птиц',
                'Ребекка', 'Над пропастью во ржи', 'Ветер в ивах', 'Большие надежды', 'Маленькие женщины',
                'Мандолина капитана Корелли[en]', 'Война и мир', 'Унесённые ветром',
                'Гарри Поттер и философский камень', 'Гарри Поттер и Тайная комната',
                'Гарри Поттер и узник Азкабана', 'Хоббит, или Туда и обратно', 'Тэсс из рода д’Эрбервиллей',
                'Миддлмарч[en]', 'Молитва об Оуэне Мини', 'Гроздья гнева', 'Алиса в Стране чудес',
                'Дневник Трейси Бикер[en]', 'Сто лет одиночества', 'Столпы Земли', 'Дэвид Копперфильд',
                'Чарли и шоколадная фабрика', 'Остров сокровищ', 'Город как Элис[en]', 'Доводы рассудка',
                'Дюна', 'Эмма', 'Аня из Зелёных Мезонинов', 'Обитатели холмов', 'Великий Гэтсби',
                'Граф Монте-Кристо', 'Возвращение в Брайдсхед', 'Скотный двор', 'Рождественская песнь',
                'Вдали от обезумевшей толпы', 'Спокойной ночи, мистер Том', 'Семейная реликвия[en]',
                'Таинственный сад', 'О мышах и людях', 'Противостояние', 'Анна Каренина',
                'Подходящий жених[en]', 'БДВ, или Большой и добрый великан', 'Ласточки и амазонки[en]',
                'Чёрный красавчик', 'Артемис Фаул', 'Преступление и наказание', 'Крестики-нолики[en]',
                'Мемуары гейши', 'Повесть о двух городах', 'Поющие в терновнике', 'Мор, ученик Смерти',
                'Далёкое волшебное дерево[en]', 'Волхв', 'Благие знамения', 'Стража! Стража!',
                'Повелитель мух', 'Парфюмер', 'Филантропы в рваных штанах[en]', 'Ночная стража', 'Матильда',
                'Дневник Бриджит Джонс', 'Тайная история', 'Женщина в белом', 'Улисс', 'Холодный дом',
                'Двойняшки[en]', 'Семейство Твит[en]', 'Я захватываю замок[en]', 'Ямы[en]', 'Горменгаст',
                'Бог мелочей', 'Вики-Ангел[en]', 'О дивный новый мир', 'Неуютная ферма[en]', 'Чародей[en]',
                'В дороге', 'Крёстный отец', 'Клан пещерного медведя[en]', 'Цвет волшебства', 'Алхимик',
                'Кэтрин[en]', 'Каин и Авель[en]', 'Любовь во время холеры', 'Девчонки в поисках любви[en]',
                'Дневники принцессы[en]', 'Дети полуночи']

fake = faker.Faker("ru")


def get_title() -> str:
    """
    Получение названия книги

    :return: название книги
    """

    return choice(BOOKS_LABELS)


def get_year() -> int:
    """
    Получение года в промежутке от 0 до 2022

    :return: целочисленное значение от 0 до 2022
    """

    return randint(0, 2020)


def get_max_pages() -> len:
    """
    Получение количества страниц

    :return: целочисленное значение от 10 до 1000
    """

    return randint(10, 1000)


def get_isbn13() -> str:
    """
    Получение кода isbn13

    :return: код isbn13
    """

    return fake.isbn13()


def get_rating() -> Union[int, float]:
    """
    Получение рейтинга для книги

    :return: значение рейтинга
    """

    return uniform(1, 10)


def get_author() -> list:
    """
    Получение автора/авторов для книги

    :return: список имён
    """

    output_names = []
    for i in range(randint(1, 3)):
        if i == randint(1, 3):
            output_names.append(fake.first_name_male() + " " + fake.last_name_male())
        else:
            output_names.append(fake.first_name_female() + " " + fake.last_name_female())
        return output_names


def get_price() -> Union[int, float]:
    """
    Получение стоимости книги

    :return: число от 1 до 100
    """
    return uniform(1, 100)


def get_random_book(book_count: int=5, start_id_: int = 1) -> Generator:
    """
    Создание книги со случайными параметрами

    :return: None
    """
    index = start_id_

    for _ in range(book_count):
        book = {
            "id": index,
            "name": get_title(),
            "pages": get_max_pages(),
            "year": get_year(),
            "isbn13": get_isbn13(),
            "rating": get_rating(),
            "price": get_price(),
            "authors": get_author()
        }
        yield book
        index += 1

    return book


if __name__ == '__main__':
    book_count = 2
    book_gen_ = get_random_book(book_count=2, start_id_=1)
    for i in range(book_count):
        book = next(book_gen_)
        print(book)
