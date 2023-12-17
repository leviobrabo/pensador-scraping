import json
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    quotes_count = 0
    current_page = 1
    day = 1
    month = 1
    quotes = {}
    dias = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    name = 'frases_bonitas'
    while quotes_count < 200:
        print(quotes_count)
        url = f'https://www.pensador.com/{name}/{current_page}/'

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            for element in soup.find_all(class_='frase fr'):
                if quotes_count > 366:
                    return  # Verifica se já coletou o suficiente

                quote = element.get_text().strip()
                author = (
                    element.find_next(class_='autor')
                    .find(class_='author-name')
                    .get_text()
                    .strip()
                )

                if quotes_count % 31 == 0 and quotes_count > 0:
                    month += 1
                    day = 1

                key = str(quotes_count + 1)
                if key not in quotes:
                    quotes[key] = []

                quotes[key].append({'quote': quote, 'author': author})
                quotes_count += 1
                day += 1
                # print(f"Frase {quotes_count}: {quote} - Autor: {author}")

            current_page += 1
        except Exception as e:
            print(f'Ocorreu um erro ao fazer o scraping da página {current_page}')
            print(e)
            break

    with open(f'{name}.json', 'w', encoding='utf-8') as file:
        json.dump(quotes, file, indent=2, ensure_ascii=False)
        print(f'Arquivo {name}.json criado com sucesso!')

scrape_quotes()
