import requests


def main():
    my_ip = "unknown"

    try:
        response = requests.get("https://api.ipify.org?format=json")
        my_ip = response.json()["ip"]
    except requests.exceptions.RequestException:
        pass

    print("Hello from chaos! My IP is:", my_ip)


if __name__ == "__main__":
    main()
