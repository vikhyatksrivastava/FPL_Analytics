import csv


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


def flatten_data(json_data, entry, output_path):
    flattened_data = [flatten_json(entry) for entry in json_data[entry]]
    print(flattened_data)
    out_file_name = output_path + entry + ".csv"

    header = sorted(set(key for row in flattened_data for key in row.keys()))

    if flattened_data:
        with open(out_file_name, 'w', newline='') as file:
            csvwriter = csv.DictWriter(file, fieldnames=header)
            csvwriter.writeheader()
            for row in flattened_data:
                complete_row = {key: row.get(key, None) for key in header}
                csvwriter.writerow(complete_row)
        print(f"JSON exploded for {entry}")
    else:
        print(f"JSON explode failed for {entry}")
