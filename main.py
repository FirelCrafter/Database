from datetime import date


    #########    Classes   ##############


class Base:
    def __init__(self):
        self.humans_counter = 0
        self.crimes_counter = 0
        self.humans_id = []
        self.crimes_id = []
        # тут думаю вместо спиков лучше словари, чтобы можно было легко реализовать алгоритм бинарного поиска по ID

    def watch_humans(self):
        return ['ID# {} {} {} Date of birth: {}'.format(id[0], id[1], id[2], id[3]) for id in self.humans_id] if \
            self.humans_id is not [] else 'Base of humans is empty'

    def watch_crimes(self):
        return ['ID# 5{} Type: {}, adress: {}, date: {}'.format(i[0], i[1], i[2], i[3]) for i in self.crimes_id] if \
            self.crimes_id is not [] else 'Base of crimes is empty'


class HumanExists(Base):
    def __init__(self, f_name, l_name, d_birth):
        super().__init__()
        self.f_name = f_name
        self.l_name = l_name
        self.d_birth = d_birth


class CrimeExists(Base):
    def __init__(self, date, adress, type):
        super().__init__()
        self.date = date
        self.adress = adress
        self.type = type


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
            print('ID# {} {} {} Date of birth: {} is added to Database'
                  .format(self.id, self.f_name, self.l_name, self.d_birth))


class Crime:
    def __init__(self, date, adress, type):
        self.date = date
        self.type = type
        self.adress = adress
        self.id = None
        self.criminal = None
        self.victim = None
        self.base = None

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

class Criminal(Base):
    def __init__(self, h_id, c_id):
        super().__init__()
        self.h_id = h_id
        self.c_id = c_id
        self.criminal_list = []

    def criminal_add(self, criminal):
        self.criminal_list.append(criminal)


class Victim(Human, Crime):
    pass


  #########  Functions   ########

def add_human(f_name, l_name, b_date):
    exists = HumanExists(f_name, l_name, b_date)
    if base.humans_id:
        for i in base.humans_id:
            if i[1] == exists.f_name and i[2] == exists.l_name and i[3] == exists.d_birth:
                print('This human is already exists on ID# {}'.format(i[0]))
    else:
        new_human = Human(f_name, l_name, b_date)
        new_human.add_to_base(base)


def add_crime(date, adress, type):
    exists = CrimeExists(date, adress, type)
    if base.crimes_id:
        for i in base.crimes_id:
            if i[1] == exists.type and i[2] == exists.adress and i[3] == exists.date:
                print('This crime is already exists on ID# {}'.format(i[0]))
    else:
        new_crime = Crime(date, adress, type)
        new_crime.add_to_base(base)


########################################################################################################################

print('Welcome to database!' + '\n'
      + 'Which data you like to add:' + '\n'
      + '1. Add human' + '\n'
      + '2. Add crime' + '\n'
      + '3. Watch humans' + '\n'
      + '4. Watch crimes' + '\n'
      + '5. Add criminal connection' + '\n'
      + '6. Exit')
base = Base()

while True:
    choice = input('Write number: ')
############################################

    if choice == '1':
        f_name = input('Enter first name: ')
        l_name = input('Enter last name: ')
        b_date = input('Enter birth date: ')
        add_human(f_name, l_name, b_date)

############################################

    elif choice == '2':
        date = input('Enter date: ')
        type = input('Enter type: ')
        adress = input('Enter adress: ')
        add_crime(date, adress, type)


############################################

    elif choice == '3':
        print(base.watch_humans())

############################################

    elif choice == '4':
        print(base.watch_crimes())

############################################

    elif choice == '5':
        h_id = input('Insert human ID # ')
        c_id = input('Insert crime ID # ')
        criminal = Criminal(h_id, c_id)
        human = []
        if base.humans_id:
            for i in base.humans_id:
                if i[0] == int(h_id):
                    human.append([i[1], i[2], i[3]])
                else:
                    print('Human ID # {} not found'.format(h_id))
        crime = []
        if base.crimes_id:
            for i in base.crimes_id:
                if i[0] == int(c_id):
                    crime.append([i[0], i[1], i[2]])
                else:
                    print('Crime ID # {} not found'.format(c_id))
        criminal.criminal_add(human+crime)
        print('Connection between human ID# {} and crime ID# {} was added'.format(h_id, c_id))


    elif choice == '6':
        break
    else:
        print('Wrong number')
