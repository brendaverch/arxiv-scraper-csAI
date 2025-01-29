"""
Scraper Melhorado para Capturar Títulos, Autores e Resumos do ArXiv
"""
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://arxiv.org"

def get_html(url: str) -> str:
    """ Obtém o HTML de uma URL com tratamento de erros. """
    try:
        response = requests.get(url, timeout=10, verify=False)  # Desativa verificação SSL para redes corporativas
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return ""

def parse_abstract_page(article_url: str) -> str:
    """ Captura o resumo de um artigo a partir da sua página no ArXiv. """
    html = get_html(article_url)
    if not html:
        return "Resumo não coletado"

    soup = BeautifulSoup(html, "html.parser")
    abstract_div = soup.find("blockquote", class_="abstract")
    if abstract_div:
        abstract_text = abstract_div.get_text(strip=True).replace("Abstract: ", "")
        return abstract_text
    return "Resumo não coletado"

def parse_list_page(html: str) -> list[dict]:
    """ Faz o parsing da página de listagem do ArXiv e retorna uma lista de artigos. """
    soup = BeautifulSoup(html, "html.parser")
    papers = []

    paper_list = soup.find_all("dt")
    for paper_dt in paper_list:
        title_tag = paper_dt.find_next("div", class_="list-title")
        authors_tag = paper_dt.find_next("div", class_="list-authors")
        link_tag = paper_dt.find_next("a")

        if not title_tag or not authors_tag or not link_tag:
            continue  # Pula se faltar alguma informação

        title = title_tag.get_text(strip=True).replace("Title:", "").strip()
        authors = [a.strip() for a in authors_tag.get_text(strip=True).replace("Authors:", "").split(",")]
        
        # Captura o link do artigo
        article_id = link_tag["href"].split("/")[-1]
        article_url = f"{BASE_URL}/abs/{article_id}"

        # Obtém o resumo do artigo
        abstract = parse_abstract_page(article_url)

        papers.append({
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "link": article_url
        })

    return papers

def main():
    """ Função principal do scraper. """
    url = f"{BASE_URL}/list/cs.AI/recent"
    html_content = get_html(url)
    papers_data = parse_list_page(html_content)

    # Salvar no CSV
    import csv
    csv_filename = "papers_ai.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "authors", "abstract", "link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers_data:
            writer.writerow(paper)

    print(f"Arquivo salvo: {csv_filename}")

if __name__ == "__main__":
    main()
