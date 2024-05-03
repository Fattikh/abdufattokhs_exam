import  requests
import bs4
import lxml


class Scrapper:
    def __init__(self, *args, **kwargs):
        ...

    def get_title(self):
        url = f"https://tribuna.uz/"

        response = requests.get(url)

        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        # body > main > section > div > div > div.col-lg-9.col-md-12 > div.row.custom-gutter.mb-40

        news = soup.find_all("li", class_="dropdown")
        f = open("test.txt", 'w')


        for product in p:
            # image_linkroducts = product.find("div", attrs={"class": "product__item-img"}).find("img")['data-src']
            title = product.find("span", attrs={"class": "product__item__info-title"}).text
            f.write(title)
            price = product.find("span", attrs={"class": "product__item-price"}).text
            f.write(price)
            image_link = product.find("img", attrs={"class": "img-fluid"})['data-src']
            is_sale = product.find("span", attrs={"class": "pr_flash pr_discount"})

            if is_sale:
                is_sale = True
            else:
                is_sale = False


            print(f"Title: {title}", f"Price: {price}", f"Image: {image_link}", f"Is Sale: {is_sale}", sep="\n")


scrapper = AsaxiyScrapper()
scrapper.get_products("iphone")