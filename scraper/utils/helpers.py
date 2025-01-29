"""
Módulo de funções auxiliares para o scraper.
- get_html: faz requisições HTTP e retorna o HTML
- parse_ai_papers: extrai informações sobre cada paper
"""

import requests
from bs4 import BeautifulSoup

def get_html(url: str) -> str:
    """
    Retorna o HTML de uma dada URL.

    :param url: URL que será requisitada
    :return: Conteúdo HTML da página
    :raises: Exception se não conseguir baixar o conteúdo
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def parse_ai_papers(html: str) -> list[dict]:
    """
    Faz o parsing do HTML e retorna uma lista de dicionários
    contendo dados de cada artigo (title, authors, abstract, etc.).

    :param html: Conteúdo HTML da página do ArXiv
    :return: Lista de dicionários com chaves ("title", "authors", "abstract")
    """
    soup = BeautifulSoup(html, "html.parser")
    
    papers_data = []


    title_divs = soup.find_all("div", class_="list-title")
    for t_div in title_divs:
        # Exemplo: remover "Title:" e eventuais espaços
        title_text = t_div.get_text(strip=True).replace("Title:", "")

        # Buscar a "próxima" div de autores
        authors_div = t_div.find_next("div", class_="list-authors")
        authors_list = []
        if authors_div:
            # "Authors: Fulano, Ciclano" -> tirar "Authors:" e depois split
            authors_text = authors_div.get_text(strip=True).replace("Authors:", "")
            authors_list = [auth.strip() for auth in authors_text.split(',') if auth.strip()]


        abstract_fake = "Resumo não coletado"  # Ajuste se necessário

        papers_data.append({
            "title": title_text,
            "authors": authors_list,
            "abstract": abstract_fake
        })

    return papers_data
