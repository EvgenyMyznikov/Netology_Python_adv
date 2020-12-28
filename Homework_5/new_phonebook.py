import re
import csv

# читаем адресную книгу в формате CSV в список contacts_list
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    fieldnames = contacts_list[0]
    for contact in contacts_list[1:]:
        if len(contact) > len(fieldnames):
            contact.pop()


def get_phone_numbers(phone):
    phones = ''.join(contact[-2])
    regex = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(.*?([а-я]{3}.).*?(\W\d{4})\)?)?"
    subst = "+7(\\2)\\3-\\4-\\5 \\7\\8 "
    phone_numbers = re.sub(regex, subst, phones, 0, re.MULTILINE)
    return phone_numbers


def get_full_names(lastname, firstname, surname):
    name = " ".join((lastname, firstname, surname)).strip()
    full_name = name.split()
    if len(full_name) < 3:
        full_name.append('')
    return tuple(full_name)


def get_sorted_contacts(contacts_list):
    new_contacts_list = []
    for lastname, firstname, surname, organization, position, phone, email in contacts_list[1:]:
        new_contacts_list.append(
            {'lastname': lastname, 'firstname': firstname, 'surname': surname, 'organization': organization,
             'position': position, 'phone': phone, 'email': email})

    for i in new_contacts_list:
        for j in new_contacts_list:
            if i['firstname'] == j['firstname'] and i['lastname'] == j['lastname']:
                for key in i.keys():
                    if i[key] == '' and j[key] != '':
                        i[key] = j[key]

    for i in new_contacts_list:
        while new_contacts_list.count(i) > 1:
            new_contacts_list.remove(i)

    return new_contacts_list


if __name__ == '__main__':
    for contact in contacts_list[1:]:
        contact[0], contact[1], contact[2] = get_full_names(contact[0], contact[1], contact[2])
        contact[-2] = get_phone_numbers(contact[-2])

sorted_contacts_list = get_sorted_contacts(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
    datawriter.writeheader()
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(sorted_contacts_list)
