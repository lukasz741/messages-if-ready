x = open("1..txt", "r")
x.con = x.read().splitlines()
print(x.con)
print(x.con[0])

y = open("2..txt", "r")
y.con = y.read().splitlines()

z = open("3..txt", "r")
z.con = z.read().splitlines()

class user:

    def __init__(self, name, surname, ready):
        self.name = name
        self.surname = surname
        self.ready = ready

    @classmethod
    def from_string(cls, user_list):
        name_string = user_list[0]
        name = name_string[5:]
        surname_string = user_list[1]
        surname = surname_string[9:]
        ready_string = user_list[2]
        ready = ready_string[7:]
        return cls(name, surname, ready)


all_users = []
user1 = user.from_string(x.con)
all_users.append(user1)
user2 = user.from_string(y.con)
all_users.append(user2)
user3 = user.from_string(z.con)
all_users.append(user3)




def message(name, surname, ISready):
    if name[-1] == "a":
        return "hello miss {} {}, your order is {}".format(name, surname, ISready)
    else:
        return "hello mister {} {}, your order is {}".format(name, surname, ISready)



for i in all_users:
    for x in range(1,4):
        name_rep = "{} message".format(x)
        with open(name_rep, 'w') as f:
            f.write(message(i.name, i.surname, i.ready))





