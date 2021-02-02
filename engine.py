from prettytable import PrettyTable


def get_humans(base):
    with open('Humans', 'r') as h:
        for human in h.readlines():
            base.humans.append(human[:-1].split(' '))
    return base.humans


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
        new_crime.add_to_base()


def print_humans(humans):
    if humans:
        table = PrettyTable()
        table.field_names = ['ID#', 'First Name', 'Last Name', 'Date of birth']
        for human in humans:
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


def search_human(base, name):
    get_humans(base)
    if base.humans:
        name = Filter(name=name)
        found = name.humans_by_name(base)
        if found:
            base.humans = found
            print_humans(base)
