import random
from typing import Generator

from product import Product

FOOD_FILE = "food.txt"              # продовольственные товары
HOME_DEVICE_FILE = "device.txt"     # бытовая техника
HOUSEWORK_FILE = "housework.txt"    # хозяйственный товары
BUILDING_FILE = "building.txt"      # стройматериалы

PRODUCT_TYPES = ['food', 'home_device', 'housework', 'building']

PRODUCT_FILE_MAP = {
    'food': FOOD_FILE,
    'home_device': HOME_DEVICE_FILE,
    'housework': HOUSEWORK_FILE,
    'building': BUILDING_FILE
}


def get_rating() -> float:
    """
    Генерирует случайным образом значение рейтинга продукта.
    :return: рейтинг, число с плавающей запятой
    """
    return round(random.uniform(0, 10), 2)


def get_price() -> float:
    """
    Генерирует случайным образом стоимость продукта.
    :return: стоимость, число с плавающей запятой
    """
    return round(random.uniform(10, 500), 2)


def get_product(p_type: PRODUCT_TYPES) -> str:
    """
    Возвращает случайным образом название товара выбранного типа.
    Список товаров хранится в файле *.txt.
    :param p_type: тип товара
    :return: название товара
    """
    p_file = PRODUCT_FILE_MAP.get(p_type)
    return get_product_name(p_file)


def get_product_name(p_file: str) -> str:
    """
    Cчитывает только одну случайную строку с названием продукта из файла.
    Список товаров хранится в файлах food.txt, device.txt,
    housework.txt, building.txt.
    :param p_file: название файла со списком товаров
    :return: название товара
    """
    title_positions = _get_name_offset(p_file)
    with open(p_file, 'r', encoding="utf8") as f:
        read_pos = random.choice(title_positions)
        f.seek(read_pos)
        product_name = f.readline().strip()
    return product_name


def _get_name_offset(p_file: str) -> list[int]:
    """
    Возращает в байтах смещение строк с книгами в файле.
    :param p_file: название файла со списком товаров
    :return: список смещений в байтах
    """
    title_offset = [0]
    with open(p_file, 'rb') as f:
        for _ in f:
            title_offset.append(f.tell())
    return title_offset[:-1]


def product_gen(product_count: int) -> Generator:
    """
    Возвращает генератор товаров.
    :param product_count: количество товаров
    :return: генератор товаров.
    """
    for _ in range(product_count):
        p_type = random.choice(PRODUCT_TYPES)
        yield Product(
            name=get_product(p_type),
            rating=get_rating(),
            price=get_price()
        )


if __name__ == "__main__":
    # test fake product
    test_1 = get_rating()
    test_2 = get_price()

    p_count = 10
    p_gen_ = product_gen(product_count=p_count)
    p_data = []

    for i in range(p_count):
        product = next(p_gen_)
        p_data.append(product)
        print(product)
