import os
import json
import argparse
import tempfile


def storage_data_out():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            data = json.load(f)
            return data


def storage_data_in(map):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(map, f)


def add_val(key, val):
    foo = storage_data_out() or dict()
    if os.path.exists('storage.data'):
        if key in foo:
            foo[key].append(val)
        else:
            foo[key] = [val]
    storage_data_in(foo)


def get_val(key):
    foo = storage_data_out()
    if os.path.exists('storage.data') and key in foo:
        print(*foo[key], sep=', ')
    else:
        print(None)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--key')
    parser.add_argument('--val')

    args = parser.parse_args()

    key = args.key
    val = args.val

    if key and val:
        add_val(key, val)
    elif key:
        get_val(key)


if __name__ == '__main__':
    main()
