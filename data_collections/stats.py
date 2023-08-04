import json
import os


def get_max_stats(stats):
    max_value = max(stats.values())
    for key in stats.keys():
        if stats[key] == max_value:
            return key


if __name__ == '__main__':
    filepath = os.path.join(os.getcwd(), 'database', 'stats.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        stats = json.load(f)
        for i in stats:
            print(get_max_stats(i))
