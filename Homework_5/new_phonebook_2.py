import csv
import re


# читаем адресную книгу в формате CSV в список contacts_list
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def get_new_phonebook(contact_list):
    new_phonebook = {}
    for contact in contacts_list:
        regex = re.compile(r"(^\w+)[\s,](\w+)[\s,](\w+|)\W+([А-яа-я]+)")
        subst_names = "\\1,\\2,\\3,\\4"
        contact[0:4] = re.sub(regex, subst_names, ' '.join(contact[0:4])).split(' ')

        regex_phone = re.compile(r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(.*?([а-я]{3}.).*?(\W\d{4}).?)?")
        subst_phone = "+7(\\2)\\3-\\4-\\5 \\7\\8 "
        contact[-2] = re.sub(regex_phone, subst_phone, contact[-2])

        regex_email = re.compile(r"([\w0-9-._]+@[\w0-9-._]+)")
        subst_email = "\\1"
        contact[-1] = re.sub(regex_email, subst_email, contact[-1])
        names = contact[0] + contact[1]
        if names not in new_phonebook:
            new_phonebook[names] = contact
        else:
            for elem, data in enumerate(contact):
                if data != '':
                    new_phonebook[names][elem] = data
    return list(new_phonebook.values())


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    with open("phonebook.csv", "w", encoding="UTF-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(get_new_phonebook(contacts_list))

# ([\w0-9-._]+@[\w0-9-._]+) email

# (\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(.*?([а-я]{3}.).*?(\W\d{4}).?)? phones

# (\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(.*?([а-я]{3}.).*?(\d{4})|)[,\)]([\w0-9-._]+@[\w0-9-._]+|) +email

# (^\w+)[\s,](\w+)[\s,](\w+|)\W+([А-яа-я]+) фио + работа

# (^\w+)[\s,](\w+)[\s,](\w+|) фио

# (^\w+)[\s,](\w+)[\s,](\w+|)\W+([А-яа-я]+).*?(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(.*?([а-я]{3}.).*?(\d{4})|)[,\)]([\w0-9-._]+@[\w0-9-._]+|)
