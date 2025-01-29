"""
Módulo principal do scraping. Orquestra as chamadas de parsing, coleta e armazenamento em CSV.
"""

import csv
import os

from scraper.utils.helpers import get_html, parse_ai_papers

def main():
    """
    Função principal do script para coletar dados de artigos de IA no ArXiv
    e salvar em CSV.
    """
    # URL da seção "cs.AI/recent" no ArXiv
    url = "https://arxiv.org/list/cs.AI/recent"

    # 1) Baixar o HTML
    html_content = get_html(url)

    # 2) Parsear dados
    papers_data = parse_ai_papers(html_content)

    # 3) Salvar em CSV
    csv_filename = "papers_ai.csv"
    
    # 'w' = sobrescreve se já existir, 'a' = anexa
    write_mode = 'w' if not os.path.exists(csv_filename) else 'a'

    with open(csv_filename, mode=write_mode, newline='', encoding='utf-8') as csvfile:
        # Ajuste os campos conforme o que você parseia em parse_ai_papers
        fieldnames = ["title", "authors", "abstract"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if write_mode == 'w':
            writer.writeheader()

        for paper in papers_data:
            writer.writerow(paper)

if __name__ == "__main__":
    main()
