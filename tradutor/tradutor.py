from deep_translator import GoogleTranslator
import json


def translate_quotes(input_file, output_file, source_language='pt', target_language='zh'):
    with open(input_file, 'r', encoding='utf-8') as file:
        quotes = json.load(file)

    translated_quotes = {}
    total_quotes = len(quotes)
    translated_count = 0

    for key, value in quotes.items():
        # Obtendo a citação e o autor da lista
        quote = value[0]['quote']
        author = value[0]['author']

        # Traduzindo somente a citação (quote)
        translated_quote = GoogleTranslator(
            source=source_language, target=target_language).translate(quote)

        translated_quotes[key] = {
            'quote': translated_quote,
            'author': author
        }

        print(f"Citação traduzida ({key}): {translated_quote}\n")

        translated_count += 1
        if translated_count == total_quotes:
            print("Tradução completa!")

    # Escrevendo as citações traduzidas em um novo arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as new_file:
        json.dump(translated_quotes, new_file, indent=2, ensure_ascii=False)


input_file = './frases_bonitas.json'
output_file = 'frases_bonitas-en.json'
translate_quotes(input_file, output_file)
