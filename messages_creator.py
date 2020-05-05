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

#creating messages from txt files
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

#creating messages from csv file
import csv

clients_from_csv =[]
with open("clients.csv", 'r') as csv_f:
    csv_reader = csv.reader(csv_f)
    for line in csv_reader:
        if line == ["imie", "nazwisko", "gotowe"]:
            continue
        client_csv = user(line[0], line[1], line[2])
        clients_from_csv.append(client_csv)


os.chdir("D:\PYTHON_NAUKA\project_auto_messages_for_clients\messages_from_csv")

for i in clients_from_csv:
    name_rep = "{} {} message.txt".format(i.name, i.surname)
    with open(name_rep, 'w') as f:
        f.write(message(i.name, i.surname, i.isReady))

os.chdir("D:\PYTHON_NAUKA\project_auto_messages_for_clients")
with open("clients.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open("clientscopy.csv", 'w', newline='') as csv_write:
            csv_writer = csv.writer(csv_write)
            for line in csv_reader:
                if line == ["imie", "nazwisko", "gotowe"]:
                    line.append('sent')
                    csv_writer.writerow(line)
                elif line[2] == "ready":
                    line.append('yes')
                    csv_writer.writerow(line)
                else:
                    line.append('no')
                    csv_writer.writerow(line)







