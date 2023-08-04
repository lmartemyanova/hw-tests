import json
import os


def find_same_names(course):
    same_names_dict = {}
    all_names_list = []
    for mentor in course['mentors']:
        all_names_list.append(mentor.split()[0])
    unique_names = sorted(list(set(all_names_list)))

    same_name_list = []
    for name in unique_names:
        if all_names_list.count(name) > 1:
            for mentor in course['mentors']:
                if name in mentor:
                    same_name_list.append(mentor)

    if len(same_name_list) > 0:
        same_names_dict[course["title"]] = same_name_list

    return same_names_dict


if __name__ == '__main__':
    input_filepath = os.path.join(os.getcwd(), 'database', 'courses_info.json')
    with open(input_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for course in data:
        print(find_same_names(course))
