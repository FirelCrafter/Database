class Base:
    def __init__(self):
        self.humans_counter = 0
        self.crimes_counter = 0
        self.humans_id = []
        self.crimes_id = []
        # тут думаю вместо спиков лучше словари, чтобы можно было легко реализовать алгоритм бинарного поиска по ID

    def watch_humans(self):
        return ['ID#{} {} {} Date of birth: {}'.format(id[0], id[1], id[2], id[3]) for id in self.humans_id] if \
            self.humans_id is not [] else 'Base of humans is empty'
    def watch_crimes(self):
        return ['ID#{} Type: {}, adress: {}, date: {}'.format(i[0], i[1], i[2], i[3]) for i in self.crimes_id] if\
            self.crimes_id is not [] else 'Base of crimes is empty'

class Human:
    def __init__(self, f_name, l_name, d_birth):
        self.f_name = f_name
        self.l_name = l_name
        self.d_birth = d_birth
        self.id = None
        self.base = None

    def add_to_base(self, base):
        self.base = base
        self.base.humans_counter += 1
        self.id = self.base.humans_counter
        self.base.humans_id.append([self.id, self.f_name, self.l_name, self.d_birth])
        print('ID#{} {} {} Date of birth: {} is added to Database'
              .format(self.id, self.f_name, self.l_name, self.d_birth))


class Crime:
    def __init__(self, date, adress, type):
        self.date = date
        self.type = type
        self.adress = adress
        self.id = None
        self.criminal = None
        self.victim = None

    def add_to_base(self, base):
        self.base = base
        self.base.crimes_counter += 1
        self.id = self.base.crimes_counter
        self.base.crimes_id.append([self.id, self.type, self.adress, self.date])
        print('ID#{} Type: {}, adress: {}, date: {} is added to database'
              .format(self.id, self.type, self.adress, self.date))


# думаю вот тут сделать наследников в виде преступника и жертвы, в них можно реализовать методы поиска по баз данных,
# однако сам объект человека может быть как преступником в одном пресуплении, так и жертвой в другом преступлении,
# такое часто бывает в реальной жизни, и чтобы не "дублировать людей" как бы это реализовать, я думаю создать еще список
# в котором будут указываться преступления в которых человек был жертвой или преступником

class Criminal(Human, Crime):
    pass

class Victim(Human, Crime):
    pass



########################################################################################################################

print('Welcome to database!' + '\n'
      + 'Which data you like to add:' + '\n'
      + '1. Add human' + '\n'
      + '2. Add crime' + '\n'
      + '3. Watch humans' + '\n'
      + '4. Watch crimes' + '\n'
      + '5. Exit')
base = Base()

while True:
    choice = input('Write number: ')
    if choice == '1':
        f_name = input('Enter first name: ')
        l_name = input('Enter last name: ')
        b_date = input('Enter birth date: ')
        new_human = Human(f_name, l_name, b_date)
        new_human.add_to_base(base)
    elif choice == '2':
        date = input('Enter date: ')
        type = input('Enter type: ')
        adress = input('Enter adress: ')
        new_crine = Crime(date, adress, type)
        new_crine.add_to_base(base)
    elif choice == '3':
        print(base.watch_humans())
    elif choice == '4':
        print(base.watch_crimes())
    elif choice == '5':
        break
    else:
        print('Wrong number')
