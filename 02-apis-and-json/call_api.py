# Call a public API, parse the JSON, filter the result.

import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_todo(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    todo = fetch_todo(API_URL)

    for key, value in todo.items():
        print(f"{key:10}: {value}")

    if todo.get("userId") == 1:
        print("\n>> This todo belongs to user 1")


if __name__ == "__main__":
    main()
