import os
import json


def extract_tbt_values(data):
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if isinstance(value, dict):
                sub_result = extract_tbt_values(value)
                if sub_result:
                    result[key] = sub_result
            elif isinstance(value, list):
                sub_result = extract_tbt_values(value)
                if sub_result:
                    result[key] = sub_result
            elif isinstance(value, str) and value.startswith("TBT:"):
                result[key] = value
                print(f"Found TBT value: {value}")
        return result
    elif isinstance(data, list):
        result = []
        for item in data:
            sub_result = extract_tbt_values(item)
            if sub_result:
                result.append(sub_result)
        return result
    else:
        return {}


def collect_tbt_values(folder_path):
    tbt_values = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".json"):
            with open(file_path, "r") as file:
                data = json.load(file)
                result = extract_tbt_values(data)
                if result:
                    tbt_values[file_name] = result
    return tbt_values


def write_result_file(tbt_values, result_file):
    with open(result_file, "w") as file:
        json.dump(tbt_values, file, indent=4)
    print("Result file written successfully.")


if __name__ == "__main__":
    translations_folder = "/Users/tarmokouhkna/PycharmProjects/PythonEE23/AlgorithmsandDatastructures/Class 3/Translations"
    result_file = "tbt_result.json"
    tbt_values = collect_tbt_values(translations_folder)
    write_result_file(tbt_values, result_file)
    print("TBT values extracted and saved to", result_file)
