import json
import os


def get_unique_ids(data):
    id_all_user = []
    for user, ids in data.items():
        id_all_user.extend(ids)
    ids_unique = list(set(id_all_user))
    return ids_unique


if __name__ == '__main__':
    filepath = os.path.join(os.getcwd(), 'database', 'ids.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    get_unique_ids(data)
    print(get_unique_ids(data))
