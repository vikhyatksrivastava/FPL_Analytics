import csv, json


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


def json_to_csv(in_file_name, out_file_name):
    try:
        with open(in_file_name, 'r') as file:
            json_data = json.load(file)

        def flatten_json(y):
            out = {}

            def flatten(x, name=''):
                if type(x) is dict:
                    for a in x:
                        flatten(x[a], name + a + '_')
                elif type(x) is list:
                    i = 0
                    for a in x:
                        flatten(a, name + str(i) + '_')
                        i += 1
                else:
                    out[name[:-1]] = x

            flatten(y)
            return out

        events_flattened_data = [flatten_json(event) for event in json_data['events']]
        phases_flattened_data = [flatten_json(setting) for setting in json_data['phases']]
        print(phases_flattened_data)

        events_header = sorted(set(key for row in events_flattened_data for key in row.keys()))
        phases_header = sorted(set(key for row in phases_flattened_data for key in row.keys()))

        if events_flattened_data:
            with open(out_file_name, 'w', newline='') as file:
                csvwriter = csv.DictWriter(file, fieldnames=events_header)
                csvwriter.writeheader()
                for row in events_flattened_data:
                    complete_row = {key: row.get(key, None) for key in events_header}
                    csvwriter.writerow(complete_row)
            print("JSON exploded for events")
        else:
            print("JSON explode failed for events")

        if phases_flattened_data:
            with open("../../../../output/fpl_bootstrap_static_phases.csv", 'w', newline='') as file:
                csvwriter = csv.DictWriter(file, fieldnames=phases_header)
                csvwriter.writeheader()
                for row in phases_flattened_data:
                    complete_row = {key: row.get(key, None) for key in phases_header}
                    csvwriter.writerow(complete_row)
            print("JSON exploded for phases")
        else:
            print("JSON explode for phases failed")
    except BaseException:
        print(f"json_to_csv BaseException")


def main():
    input_file = "../../../../output/fpl_bootstrap_static.json"
    output_file = "../../../../output/fpl_bootstrap_static.csv"
    json_to_csv(input_file, output_file)


if __name__ == '__main__':
    main()
