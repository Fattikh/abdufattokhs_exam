import requests
from bs4 import BeautifulSoup


def scrape_title():
    # Задаем URL, на который будем отправлять запрос
    url = f'https://tribuna.uz/'

    # Отправляем GET-запрос на указанный URL и сохраняем ответ
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с классом, содержащим информацию о товаре (название и цена)
        titles = soup.find_all("div", class_='header-menu')

        # Проходимся по каждому товару и извлекаем название и цену
        for title in titles:
            # Получаем название товара
            name = title.find('li').text.strip()

            # Получаем цену товара
            price = title.find("li", class_="dropdown").text.strip()
            print(f"Title: {name}", f"Price: {price}")

            scrapper = scrape_title()
            scrapper.get_products()


