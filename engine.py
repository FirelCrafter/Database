from prettytable import PrettyTable
from base import Filter, Human, Crime


def get_humans():
    humans = []
    with open('Humans', 'r') as h:
        for human in h.readlines():
            humans.append(human[:-1].split(' '))
    return humans


def get_crimes():
    crimes = []
    with open('Crimes', 'r') as c:
        for crime in c.readlines():
            crimes.append(crime[:-1].split(' '))
    return crimes


def print_humans(humans):
    if humans:
        table = PrettyTable()
        table.field_names = ['ID#', 'First Name', 'Last Name', 'Date of birth']
        for human in humans:
            table.add_row([human[0], human[1], human[2], human[3]])
        return table
    else:
        return 'Base of humans is empty'


def print_crimes(crimes):
    if crimes:
        table = PrettyTable()
        table.field_names = ['ID#', 'Date', 'Type', 'Address']
        for crime in crimes:
            table.add_row([crime[0], crime[1], crime[2], crime[3]])
        return table
    else:
        return 'Base of crimes is empty'


def add_human(f_name, l_name, b_date, base):
    new_human = Human(f_name, l_name, b_date)
    humans = get_humans()
    exists = new_human.exists(humans)
    if exists:
        print('This human is already exists on ID# {}'.format(exists))
    else:
        f1 = Filter(name=f_name, base=base)
        f2 = Filter(name=l_name, base=base)
        names = [name[1] for name in humans] + [name[2] for name in humans]
        distances = [f1.levenshtein_distance(dist) for dist in names] + [f2.levenshtein_distance(dist) for dist in names]
        lev = dict(zip(names, distances))
        rec_names = []
        for key, value in lev.items():
            if int(value) <= 5:
                rec_names.append(key)
        if rec_names:
            rec_humans = []
            for h in humans:
                if h[1] in rec_names and h[2] in rec_names:
                    rec_humans.append(h)
            if rec_humans:
                print('Do you mean these humans?')
                print(print_humans(rec_humans))
                answer = input('Input y/n: ')
                if answer == 'y':
                    return
                elif answer == 'n':
                    new_human.add_to_base()
                else:
                    print('Wrong input')
            else:
                new_human.add_to_base()
        else:
            new_human.add_to_base()


def add_crime(date, adress, type):
    new_crime = Crime(date, adress, type)
    crimes = get_crimes()
    exists = new_crime.exists(crimes)
    if exists:
        print('This crime is already exists on ID# {}'.format(exists))
    else:
        new_crime.add_to_base()


def search_human(base, name):
    humans = get_humans()
    if humans:
        f = Filter(base=base, name=name)
        found = f.humans_by_name(humans)
        if found:
            return print_humans(found)
        else:
            names = [name[1] for name in humans] + [name[2] for name in humans]
            distances = [f.levenshtein_distance(dist) for dist in names]
            lev = dict(zip(names, distances))
            rec_names = []
            for key, value in lev.items():
                if int(value) <= 3:
                    rec_names.append(key)
            if rec_names:
                return 'Do you mean: ' + ', '.join(rec_names).strip(', ') + ' ?'
            else:
                return 'Person with name: {} not found.'.format(f.name)
