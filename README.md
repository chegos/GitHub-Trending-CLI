# 🚀 GitHub Trending CLI

Uma aplicação de linha de comando (CLI) desenvolvida em Python que consome a API pública do GitHub para exibir os repositórios mais populares do momento com base em diferentes períodos de tempo.

## 📌 Sobre o Projeto

Este projeto permite consultar os repositórios mais "trending" do GitHub utilizando a API oficial.

O usuário pode definir:

- 📅 Período de análise (`day`, `week`, `month`, `year`)
- 🔢 Quantidade de repositórios exibidos

Os resultados são apresentados de forma organizada, mostrando:

- Nome do repositório
- Descrição
- Número de estrelas
- Linguagem principal
- Link do repositório

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Requests
- Argparse
- GitHub REST API

---

## 📂 Estrutura do Projeto

```bash
github-trending-cli/
│── trending_repos.py
│── requirements.txt
│── README.md
