import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def name_list():
    set_list =[]
    for column in contacts_list:
        name = ' '.join(column[:3]).split(' ')
        if 'доб' not in column[5]:
            pattern = r"(\+7|8)\s*\(*(495)\)*\s*[-]*(\d+)[\s|-]*(\d{2})[\s|-]*(\d{2})"
            result = re.sub(pattern, r"+7(\2)\3-\4-\5", column[5])
            set_list.append([name[0], name[1], name[2], column[3], column[4], result, column[6]])
        else:
            pattern = r"(\+7|8)\s*\(*(495)\)*\s*[-]*(\d+)[\s|-]*(\d{2})[\s|-]*(\d{2})\s*\(*(\w*[.])\s(\d{4})\)*"
            result = re.sub(pattern, r"\1(\2)\3-\4-\5 \6\7", column[5])
            set_list.append([name[0], name[1], name[2], column[3], column[4], result, column[6]])
    return duplication_function(set_list)


def duplication_function(contacts):
    for contact in contacts:
        name = contact[1]
        last_name = contact[0]
        for el_contact in contacts:
            el_name = el_contact[1]
            el_last_name = el_contact[0]
            if name == el_name and last_name == el_last_name:
                if contact[2] == "":
                    contact[2] = el_contact[2]
                if contact[3] == "":
                    contact[3] = el_contact[3]
                if contact[4] == "":
                    contact[4] = el_contact[4]
                if contact[5] == "":
                    contact[5] = el_contact[5]
                if contact[6] == "":
                    contact[6] = el_contact[6]

    result_list = []
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list

if __name__ == '__main__':

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(name_list())
