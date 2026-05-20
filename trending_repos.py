import argparse
import requests
from datetime import datetime, timedelta


def get_date_from_duration(duration):
    """Retorna a data inicial com base na duração escolhida."""
    today = datetime.now()

    if duration == "day":
        return today - timedelta(days=1)
    elif duration == "week":
        return today - timedelta(weeks=1)
    elif duration == "month":
        return today - timedelta(days=30)
    elif duration == "year":
        return today - timedelta(days=365)
    else:
        raise ValueError(
            "Duração inválida. Use: day, week, month ou year."
        )


def fetch_trending_repositories(duration, limit):
    """Busca os repositórios em alta na API do GitHub."""
    start_date = get_date_from_duration(duration)
    formatted_date = start_date.strftime("%Y-%m-%d")

    url = "https://api.github.com/search/repositories"

    params = {
        "q": f"created:>{formatted_date}",
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("items", [])

    except requests.exceptions.RequestException as error:
        print(f"Erro ao acessar a API do GitHub: {error}")
        return []


def display_repositories(repositories):
    """Exibe os repositórios formatados."""
    if not repositories:
        print("Nenhum repositório encontrado.")
        return

    print("\n🔥 GitHub Trending Repositories\n")

    for index, repo in enumerate(repositories, start=1):
        name = repo["full_name"]
        description = repo["description"] or "Sem descrição."
        stars = repo["stargazers_count"]
        language = repo["language"] or "N/A"
        url = repo["html_url"]

        print(f"{index}. {name}")
        print(f"   ⭐ Stars: {stars}")
        print(f"   📝 Description: {description}")
        print(f"   💻 Language: {language}")
        print(f"   🔗 URL: {url}")
        print("-" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Exibe os repositórios em alta no GitHub."
    )

    parser.add_argument(
        "--duration",
        choices=["day", "week", "month", "year"],
        default="week",
        help="Período: day, week, month ou year."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Número de repositórios a exibir."
    )

    args = parser.parse_args()

    if args.limit <= 0:
        print("O valor de --limit deve ser maior que zero.")
        return

    repositories = fetch_trending_repositories(
        args.duration,
        args.limit
    )

    display_repositories(repositories)


if __name__ == "__main__":
    main()
