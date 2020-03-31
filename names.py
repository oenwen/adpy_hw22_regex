import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    for row in contacts_list:
        print(str(row))
        name_pattern = re.compile('^\w+(\s+|\,)\w+((\s+|\,)\w+)?')  # <class 're.Pattern'>
        result = name_pattern.findall(str(row))
        print(result)
# sub_name_pattern = re.split('[\,?|\s?]', name_pattern)

# for row in contacts_list:
#     name_corr = name_pattern.sub(sub_name_pattern, str(row))
#     print(name_corr)


    # name_search_str = '^((\w+)(\s+|\,)(\w+)(\s+|\,)?(\w+))'
    # name_replace_str = r'\2,\4,\6'
    # name_replace(name_search_str, name_replace_str)
