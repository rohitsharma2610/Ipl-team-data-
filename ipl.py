

import pandas as pd
import time
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "ipl_data.csv"


def made_by():
    msg = ''' 
            IPL Data Analysis made by       : Rohit Sharma
            
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv("ipl_data.csv")
    print(df)

# name of function      : clear
# purpose               : clear output screen


def data_analysis_menu():
        df = pd.read_csv("ipl_data.csv")
        while True:
            print('\n\nD A T A   A N A L Y S I S   M E N U  ')
            print('_'*100,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   Show Top Rows')
            print('4.   Show Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Data Summery')
            print('11.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:'))
            if ch == 1:
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 6:
                a = input('Enter Match ID :')
                b = input('Enter IPL season :')
                c = input('Enter City Name :')
                d = input('Enter Match date :')
                e = input('Enter Team 1 Name  :')
                f = input('Enter Team 2 Name :')
                g = input('Enter Toss Winner :')
                h = input('Enter Toss Decision :')
                i = input('Enter Result (Normal /tie/ DL ) :')
                j = input('Enter Duckwoth Lewis Method applied (0 for No, 1 for Yes ) :) :')
                k = input('Enter Winner Team :')
                l = input('Enter Win By runs :')
                m = input('Enter Win By Wickets :')
                n = input('Enter Man of the Match Player :')
                data = {'Jersey': a, 'season': b, 'Boundary': c,
                        'date': d, 'team1': e, 'team2': f, 'toss_winner': g,
                        'toss_decision':h,'result':i,'dl_applied':j,'winner':k,
                        'win_by_runs':l,'win_by_wickets':m,'player_of_match':n
                        
                        }
                df = df.append(data, ignore_index=True)
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = input('Enter default column value :')
                df[col_name] = col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(
                    input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                print(df.describe()) 
                wait = input('\n\n\n Press any key to continue....')
            if ch == 11:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv("ipl_data.csv")
    while True:
        print('\nGRAPH MENU ')
        print('_'*100)
        print('\n1. Season wise Matches - Line Graph')
        print('\n2. Season wise Matches - Bar Graph')
        print('\n3. Season wise Matches - Horizontal Bar Graph')
        print('\n4. Most Successful Team - Bar Graph')
        print('\n5. Most Successful Player - Bar Graph')
        print('\n6.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            
        if ch == 3:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()
           

        if ch == 4:
            g = df.groupby('winner')
            x = df['winner'].unique()
            y = g['winner'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('winner')
            plt.ylabel('Matches')
            plt.title('Most Successful Team')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()

        if ch == 5:
            g = df.groupby('player_of_match')
            x = df['player_of_match'].unique()
            y = g['player_of_match'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('Player Name')
            plt.ylabel('Total Man of the Match')
            plt.title('Most successful Player')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()
        if ch ==6:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv("teams.csv")
    while True:
        print('\n\nE X P O R T    M  E N U ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch == 1:
            df.to_csv('teams.csv')
            print('\n\nCheck your new file "ipl_data_backup.csv"  on C: Drive.....')
            wait = input('\n\n\n Press any key to continuee.....')

        if ch == 2:
            break


def main_menu():
           while True:
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Made By\n')
                      print('6.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice == 1:
                                read_csv_file()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 2:
                                data_analysis_menu()
                                wait = input('\n\n Press any key to continue....')

                      if choice == 3:
                                graph()
                                wait = input('\n\n Press any key to continue....')
                      if choice == 4:
                                export_menu()
                                wait = input(
                                    '\n\n Press any key to continue....')
                      if choice == 5:
                                made_by()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 6:
                          print('THANKS FOR VISITING MY FILE')
                          break

           


# call your main menu
main_menu()
