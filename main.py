import engine
from base import Base, Filter

########################################################################################################################

print('Welcome to database!' + '\n'
      + 'Which data you like to add:' + '\n'
      + '1. Add human' + '\n'
      + '2. Add crime' + '\n'
      + '3. Watch humans' + '\n'
      + '4. Watch crimes' + '\n'
      + '5. Find human by name' + '\n'
      + '6. Get crimes by date')
base = Base()

while True:
    choice = input('Write number: ')
############################################

    if choice == '1':
        f_name = input('Enter first name: ')
        l_name = input('Enter last name: ')
        b_date = input('Enter birth date: ')
        engine.add_human(f_name, l_name, b_date, base)

############################################

    elif choice == '2':
        date = input('Enter date: ')
        type = input('Enter type: ')
        adress = input('Enter address: ')
        engine.add_crime(date, adress, type)


############################################

    elif choice == '3':
        humans = engine.get_humans()
        print(engine.print_humans(humans))

############################################

    elif choice == '4':
        crimes = engine.get_crimes()
        print(engine.print_crimes(crimes))

############################################

    elif choice == '5':
        name = input('Input name: ')
        print(engine.search_human(base, name))    

    elif choice == '6':
        crimes = engine.get_crimes()
        if crimes:
            date = input('Input date (DD.MM.YYYY): ')
            f_date = Filter(date=date, base=base)
            found = f_date.crimes_by_date(crimes)
            if found:
                print(engine.print_crimes(found))
            else:
                print('Crimes for date: {} not found'.format(date))
    else:
        print('Wrong number')


####################################################
        #
        #
        # h_id = input('Insert human ID # ')
        # c_id = input('Insert crime ID # ')
        # criminal = Criminal(h_id, c_id)
        # human = []
        # if base.humans_id:
        #     for i in base.humans_id:
        #         if i[0] == int(h_id):
        #             human.append([i[1], i[2], i[3]])
        #         else:
        #             print('Human ID # {} not found'.format(h_id))
        # crime = []
        # if base.crimes_id:
        #     for i in base.crimes_id:
        #         if i[0] == int(c_id):
        #             crime.append([i[0], i[1], i[2]])
        #         else:
        #             print('Crime ID # {} not found'.format(c_id))
        # criminal.criminal_add(human+crime)
        # print('Connection between human ID# {} and crime ID# {} was added'.format(h_id, c_id))
