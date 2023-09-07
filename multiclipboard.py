import sys
import clipboard
import json
import pprint


SAVED_DATA = "clipboard.json"


def save_data(file_path):
    with open(file_path, "w") as f:
        try:
            data = json.load(f)
        except:
            data = load_data(file_path)
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        json.dump(data, f)
        print("Data saved")


def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    

def search_for_key(file_path):
    key = input("What key are you looking for? ")
    with open(file_path, "r") as f:
        data = json.load(f)
        for entry in data:
            if entry == key.lower():
                clipboard.copy(data[entry])
                print("The key {} contains the following value: '{}' and it has been copied to your clipboard".format(key, data[entry]))
                return
        print("There are no keys matching your input.")


def list_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            print("These is the current state of the database: ")
            pprint.pprint(data)
    except FileNotFoundError:
        print("File was not found")



def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "save":
            save_data(SAVED_DATA)
        elif command == "load":
            search_for_key(SAVED_DATA)
        elif command == "list":
            list_data(SAVED_DATA)
        else:
            print("Unknown command")
    else:
        print("Please print exactly 1 command")


if __name__ == '__main__':
    main()