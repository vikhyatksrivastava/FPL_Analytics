import requests
import json


def callAPI():
    fpl_bootstrap_static_api = "https://fantasy.premierleague.com/api/bootstrap-static/"
    fpl_bootstrap_static_response = requests.get(fpl_bootstrap_static_api)

    if fpl_bootstrap_static_response.status_code == 200:
        data = fpl_bootstrap_static_response.json()
        fpl_bootstrap_static_file = "../../../../output/fpl_bootstrap_static.json"

        with open(fpl_bootstrap_static_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f'Response saved to {fpl_bootstrap_static_file}')
    else:
        print(f'Failed to fetch data. Status code: {fpl_bootstrap_static_response.status_code}')


def main():
    callAPI()


if __name__ == '__main__':
    main()
