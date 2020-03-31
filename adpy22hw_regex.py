from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

def regex_iter():

    for row in contacts_list:
        text = str(row)
        phone_pattern = re.compile(phone_search_str)
        sub_pattern = phone_replace_str
        new_text = phone_pattern.sub(sub_pattern, text)
        print(new_text)
        yield new_text

if __name__ == '__main__':

    new_contacts_list = []
    phone_search_str = r'(\+7|8)(\s*)?\(?(\d{3})\)?(\s*|\-)?(\d{3})\-?(\d{2})\-?(\d{2})(\s*\(?(доб\.)\s*(\d+)\)?)?'
    phone_replace_str = r'+7(\3)\5-\6-\7 \9\10'
    for new_text in regex_iter():
        new_contacts_list.append(new_text)
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)


