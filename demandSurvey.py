from dbModule import *
from datetime import datetime
import pandas as pd


db = Database()

#menu = db.get_list('menu_management', '*')
#a = menu[-1]
#print(a, type(a))

def demand_survey(db):
    while True:
        demand_survey = 'Demand Survey\n' \
                        '=============\n' \
                        '1. Check Menu\n' \
                        '2. Survey\n' \
                        '3. Go Back\n' \
                        '=============\n' \

        print(demand_survey)
        choice = input('Select (1/2): ')

        if choice == '1':
            n = True
            while n:
                options = 'Check Menu\n' \
                          '=========================\n' \
                          '1. Today\'s Menu\n' \
                          '2. 1 Week Menu From Today\n' \
                          '3. Go Back\n' \
                          '=========================\n'
                print(options)
                choice = input('Select (1/2): ')
                menu = db.get_list('menu_management', '*')

                if choice == '1':
                    menu = pd.DataFrame(menu)
                    today_menu = menu.iloc[-1]
                    print(today_menu)
                    i = True

                    while i:
                        print('\nEnter y when you want to go back')
                        answer = input('Select (y): ')
                        if answer == 'y':
                            break
                        else:
                            pass
                    break
                elif choice == '2':
                    pass
                else:
                    print('\nYou put wrong input data. Please enter correct number.\n')

        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

#demand_survey(db)