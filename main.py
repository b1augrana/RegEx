import re
from pprint import pprint
import csv


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
replace = r"+7(\2)\3-\4-\5 \6\7"

def main(contacts_list: list):
    new_list = list()
    for item in contacts_list:
        full_name = " ".join(item[:3]).split(" ")
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4], re.sub(pattern, replace, item[5]),  item[6]]
        new_list.append(result)     
    return merger(new_list)             

def merger(contacts: list):
    for con in contacts:
        first_name = con[0]
        last_name = con[1]
        for new_con in contacts:
            new_first_name = new_con[0]
            new_last_name = new_con[1]
            if first_name == new_first_name and last_name == new_last_name:
                if con[2] == "": con[2] = new_con[2]
                if con[3] == "": con[3] = new_con[3]
                if con[4] == "": con[4] = new_con[4]
                if con[5] == "": con[5] = new_con[5]
                if con[6] == "": con[6] = new_con[6]
                
    result = list()                
    for i in contacts: 
        if i not in result:
            result.append(i)
    return result   

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))    
