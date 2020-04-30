class user:

    def __init__(self, name, surname, ready):
        self.name = name
        self.surname = surname
        self.isReady = ready

    @classmethod
    def from_string(cls, user_list):
        name_string = user_list[0]
        name = name_string[5:]
        surname_string = user_list[1]
        surname = surname_string[9:]
        isReady_string = user_list[2]
        isReady = isReady_string[7:]
        return cls(name, surname, isReady)

import os
os.chdir("D:\PYTHON_NAUKA\project_auto_messages_for_clients\clients_all")

all_users = []
for person in os.listdir():
    f = open(person, "r")
    client = f.read().splitlines()
    usufructuary = user.from_string(client)
    all_users.append(usufructuary)
    f.close()

def message(name, surname, isReady):
    if name[-1] == "a":
        return "hello miss {} {}, your order is {}".format(name, surname, isReady)
    else:
        return "hello mister {} {}, your order is {}".format(name, surname, isReady)


os.chdir("D:\PYTHON_NAUKA\project_auto_messages_for_clients")

for i in all_users:
    name_rep = "{} {} message.txt".format(i.name, i.surname)
    with open(name_rep, 'w') as f:
        f.write(message(i.name, i.surname, i.isReady))





