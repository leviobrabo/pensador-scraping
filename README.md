# Scraping de Citações do Pensador.com

Este script Python foi criado para extrair citações de uma determinada categoria do site [Pensador](pensador.com) e salvar as citações em um arquivo JSON.

# Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema. Este script depende das seguintes bibliotecas Python:

-   requests
-   beautifulsoup4

Você pode instalar as dependências executando o seguinte comando:

```bash
pip install requirements.txt
```

# Uso

Clone ou baixe este repositório para o seu ambiente local.

```bash
git clone https://github.com/leviobrabo/pensador-scraping
```

Execute o script pensador.py no terminal ou prompt de comando.

```bash
python pensador.py
```

# Personalização

Antes de executar o script, você pode personalizá-lo de acordo com suas necessidades:

Modifique a variável name para a categoria desejada no site Pensador.com.

![Alt text](assets/pensador.png)

Por exemplo:

`https://www.pensador.com/frases_bonitas/`

Name -> `frases_bonitas`

# Tradução

Se desejar traduzir o arquivo json para algum idioma, vá para pastar tradutor e leia o readme...

# Estruturação do projeto

```
pensador-scraping/
│
├── assets/
│ ├── image.png
│ └── pensador.png
│
├── pensador/
│ ├── Include/ (possíveis arquivos de inclusão de bibliotecas)
│ ├── Lib/ (possíveis bibliotecas específicas)
│ ├── Scripts/ (scripts do projeto)
│ ├── pyvenv.cfg (configurações do ambiente virtual Python)
│ └── pensador.py (possível arquivo principal do projeto)
│
├── tradutor/
│ ├── __init__.py
│ ├── README.md
│ └── tradutor.py (arquivo relacionado à funcionalidade de tradução)
│
├── .gitignore (arquivo com padrões para ignorar ao usar Git)
├── pensador.py (arquivo que pode ser relacionado ao projeto principal)
├── README.md (arquivo com informações sobre o projeto)
└── requirements.txt (arquivo com as dependências Python necessárias para o projeto)
```

# Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adicionar novos recursos a este script. Abra uma issue ou envie um pull request para colaborar.

[PR](https://github.com/leviobrabo/pensador-scraping/pulls)
