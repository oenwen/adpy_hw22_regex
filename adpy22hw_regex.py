import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def regex_iter():
    phone_search_str = r'(\+7|8)(\s*)?\(?(\d{3})\)?(\s*|\-)?(\d{3})\-?(\d{2})\-?(\d{2})(\s*\(?(доб\.)\s*(\d+)\)?)?'
    phone_replace_str = r'+7(\3)\5-\6-\7 \9\10'

    for row in contacts_list:
        phone_text = row[5]
        phone_pattern = re.compile(phone_search_str)
        sub_pattern = phone_replace_str
        new_phone_text = phone_pattern.sub(sub_pattern, phone_text)
        row[5] = new_phone_text.strip(' ')

        name = row[0] + ' ' + row[1] + ' ' + row[2]
        name_split = re.split('[\s+]', name)
        row[0] = name_split[0]
        row[1] = name_split[1]
        row[2] = name_split[2]

        yield row


def search_doubles():
    new_contacts_list = []
    contact_dict = dict()

    for new_list in regex_iter():
        new_contacts_list.append(new_list)

    for row in new_contacts_list:
        last_and_first_name = row[0] + ' ' + row[1]
        if last_and_first_name not in contact_dict.keys():
            contact_info = []
            for i in range(2,7):
                field = str(row[i])
                contact_info.append(field)
            contact_dict.update({last_and_first_name:contact_info})
        else:
            list1 = contact_dict[last_and_first_name]
            list2 = [row[2], row[3], row[4], row[5], row[6]]
            zipped_list = list(zip(list1, list2))
            list3 = []
            for i, item in enumerate(zipped_list):
                if item[0] == item[1]:
                    list3.append(item[0])
                elif item[0] == '':
                    list3.append(item[1])
                elif item[1] == '':
                    list3.append(item[0])
            contact_dict[last_and_first_name] = list3

    new_contacts_list = []
    for key, value in contact_dict.items():
        new_item = []
        new_item.extend([key.split(' ')[0], key.split(' ')[1]])
        for i in range(5):
            new_item.append(value[i])
        new_contacts_list.append(new_item)

    return new_contacts_list

if __name__ == '__main__':

    new_contacts_list = search_doubles()

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)


