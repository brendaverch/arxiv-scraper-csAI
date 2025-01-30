# 📌 ArXiv Scraper - Inteligência Artificial

Este projeto é um scraper para coletar artigos da seção **Artificial Intelligence (cs.AI)** do ArXiv, extraindo **título, autores, resumo (abstract) e link para o artigo**.

---

## 🚀 **1. Como Funciona?**
O scraper acessa a página **[ArXiv cs.AI](https://arxiv.org/list/cs.AI/recent)** e realiza os seguintes passos:

1️⃣ **Coleta a lista de artigos mais recentes**.  
2️⃣ **Extrai os títulos e autores**.  
3️⃣ **Acessa cada página individual de artigo** e **coleta o resumo (abstract)**.  
4️⃣ **Salva os dados em um arquivo CSV** (`papers_ai.csv`).

---

## 🛠 **2. Como Rodar o Scraper?**

### 📌 **Opção 1: Executar Localmente**
1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/arxiv-scraper-csAI.git
   cd arxiv-scraper-csAI
