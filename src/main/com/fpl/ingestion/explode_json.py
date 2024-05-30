import csv, json
from src.main.com.fpl.utilities.local_utilities import flatten_data


def explode_json(json_data, parent='', delimiter='_'):
    element = {}
    try:
        for key, value in json_data.items():
            new_key = parent + delimiter + key if parent else key
            if isinstance(value, dict):
                element.update(explode_json(value, parent, delimiter))
            else:
                element[new_key] = value
    except BaseException:
        print(f"explode_json BaseException")
    return element


def json_to_csv(in_file_name, output_path, tables):
    try:
        with open(in_file_name, 'r') as file:
            json_data = json.load(file)

        for entry in tables:
            flatten_data(json_data, entry, output_path)
    except BaseException:
        print(f"json_to_csv BaseException")


def main():
    input_file = "../../../../output/fpl_bootstrap_static.json"
    output_path = "../../../../output/"
    tables = ["events", "game_settings", "phases", "teams",  "element_stats",
              "element_types"
              ]

    # tables = ["element"]
    json_to_csv(input_file, output_path, tables)


if __name__ == '__main__':
    main()
