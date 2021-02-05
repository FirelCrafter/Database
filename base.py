import numpy as np
import datetime as d


class Base:
    def __init__(self):
        self.humans = []
        self.crimes = []


class Filter:
    def __init__(self, base, date=None, name=None):
        self.date = date
        self.name = name
        self.base = base

    def crimes_by_date(self, crimes):
        if crimes:
            found = []
            for crime in crimes:
                if self.date == crime[1]:
                    found.append(crime)
                else:
                    return 'Crimes for date: {} not found'.format(self.date)
            return crimes
        else:
            return 'Base of crimes is empty'

    def levenshtein_distance(self, name):
        size_x = len(self.name) + 1
        size_y = len(name) + 1
        matrix = np.zeros((size_x, size_y))
        for x in range(size_x):
            matrix[x, 0] = x
        for y in range(size_y):
            matrix[0, y] = y

        for x in range(1, size_x):
            for y in range(1, size_y):
                if self.name[x - 1] == name[y - 1]:
                    matrix[x, y] = min(
                        matrix[x - 1, y] + 1,
                        matrix[x - 1, y - 1],
                        matrix[x, y - 1] + 1)
                else:
                    matrix[x, y] = min(
                        matrix[x - 1, y] + 1,
                        matrix[x - 1, y - 1] + 1,
                        matrix[x, y - 1] + 1)
        return matrix[size_x - 1, size_y - 1]

    def humans_by_name(self, humans):
        if humans:
            found = []
            for human in humans:
                if self.name == human[1] or self.name == human[2]:
                    found.append(human)
            return found
        else:
            return 'Not found'


class Human:
    def __init__(self, f_name, l_name, d_birth):
        self.f_name = f_name
        self.l_name = l_name
        self.d_birth = d_birth
        self.id = None
        self.base = None

    def exists(self, humans):
        if humans:
            for h in humans:
                if h[1] == self.f_name and h[2] == self.l_name and h[3] == self.d_birth:
                    return h[0]
            else:
                return None

    def add_to_base(self):
        with open('Humans') as f:
            size = sum(1 for string in f)
        self.id = size + 1
        f = open('Humans', 'a')
        f.write(' '.join([str(self.id), self.f_name, self.l_name, str(self.d_birth)]) + ' ' + str(d.date.today()) + '\n')
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

    def exists(self, crimes):
        if crimes:
            for c in crimes:
                if c[1] == self.date and c[2] == self.type and c[3] == self.adress:
                    return c[0]
            else:
                return None

    def add_to_base(self):
        with open('Crimes') as f:
            size = sum(1 for string in f)
        self.id = size + 1
        f = open('Crimes', 'a')
        f.write(' '.join([str(self.id), self.date, self.type, str(self.adress)]) + '\n')
        f.close()
        print('ID#{} Type: {}, address: {}, date: {} is added to database'
              .format(self.id, self.type, self.adress, self.date))


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


