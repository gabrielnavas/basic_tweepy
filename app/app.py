from api import get_api


def main():
    api = get_api()
    gabriel = api.get_user('gabrnavas')
    print(gabriel._json)

main()