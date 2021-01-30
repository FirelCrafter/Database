from prettytable import PrettyTable


    #########    Classes   ##############


class Base:
    def __init__(self):
        self.humans = []
        self.crimes = []


class Filter(Base):
    def __init__(self, date=None, name=None):
        super().__init__()
        self.date = date
        self.name = name

    def crimes_by_date(self):
        if self.crimes:
            crimes = []
            for crime in self.crimes:
                if self.date == crime[1]:
                    crimes.append(crime)


class Human:
    def __init__(self, f_name, l_name, d_birth):
        self.f_name = f_name
        self.l_name = l_name
        self.d_birth = d_birth
        self.id = None
        self.base = None

    def exists(self, base):
        if base.humans:
            for h in base.humans:
                if h[1] == self.f_name and h[2] == self.l_name and h[3] == self.d_birth:
                    return h[0]
                else:
                    return None

    def add_to_base(self):
        with open('Humans') as f:
            size = sum(1 for string in f)
        self.id = size+1
        f = open('Humans', 'a')
        f.write(' '.join([str(self.id), self.f_name, self.l_name, str(self.d_birth)]) + '\n')
        f.close()
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

    def exists(self, base):
        if base.crimes:
            for c in base.humans:
                if c[1] == self.date and c[2] == self.type and c[3] == self.adress:
                    return c[0]
                else:
                    return None

    def add_to_base(self, base):
        with open('Crimes') as f:
            size = sum(1 for string in f)
        self.id = size + 1
        f = open('Crimes', 'a')
        f.write(' '.join([str(self.id), self.date, self.type, str(self.adress)]) + '\n')
        f.close()
        print('ID#{} Type: {}, address: {}, date: {} is added to database'
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

def get_humans(base):
    with open('Humans', 'r') as h:
        for human in h.readlines():
            base.humans.append(human[:-1].split(' '))


def get_crimes(base):
    with open('Crimes', 'r') as c:
        for crime in c.readlines():
            base.crimes.append(crime[:-1].split(' '))


def add_human(f_name, l_name, b_date):
    new_human = Human(f_name, l_name, b_date)
    get_humans(base)
    exists = new_human.exists(base)
    if exists:
        print('This human is already exists on ID# {}'.format(exists))
    else:
        new_human.add_to_base()


def add_crime(date, adress, type):
    new_crime = Crime(date, adress, type)
    exists = new_crime.exists(base)
    if exists:
        print('This crime is already exists on ID# {}'.format(exists))
    else:
        new_crime.add_to_base(base)


def print_humans(base):
    get_humans(base)
    if base.humans:
        table = PrettyTable()
        table.field_names = ['ID#', 'First Name', 'Last Name', 'Date of birth']
        for human in base.humans:
            table.add_row([human[0], human[1], human[2], human[3]])
        return table
    else:
        return 'Base of humans is empty'

def print_crimes(base):
    get_crimes(base)
    if base.crimes:
        table = PrettyTable()
        table.field_names = ['ID#', 'Date', 'Type', 'Address']
        for crime in base.crimes:
            table.add_row([crime[0], crime[1], crime[2], crime[3]])
        return table
    else:
        return 'Base of crimes is empty'

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
        print(print_humans(base))

############################################

    elif choice == '4':
        print(print_crimes(base))

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
