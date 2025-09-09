seasons = ('spring', 'summer', 'autumn', 'winter')
number_of_a_month = int(input('What is the number of the month?: '))
if number_of_a_month in range (3,6):
    print('It is',seasons[0])
elif number_of_a_month in range (6,9):
    print('It is', seasons[1])
elif number_of_a_month in range (9,12):
    print('It is', seasons[2])
elif number_of_a_month in (12,1,2):
    print('It is', seasons[3])
else:
    print('Invalid month number!')


names = set()
while True:
    name = input('Enter a name:')
    if name == "":
        break
    if name in names:
        print('Existing name')
    else:
        names.add(name)
        print('New Name')
print('The names are:')
for name in names:
    print(name)


airport = {'AGAF' : 'Afutara Airport',
           'AGGA' : 'Auki Gwaunaruu Airport'}
while True:
    option = input('What do you want to do?:')
    if option == 'quit':
        print('You quit')
        break
    if option == 'I want to enter a new airport':
        ICAO = input('Enter the ICAO code of the airport:')
        name = input('Enter the name of the airport:')
        airport.update(({ICAO:name}))
    elif option == 'I want to fetch airport information':
        ICAO = input('What is the ICAO code of the airport?')
        if ICAO in airport:
            print('The name of the airport is', airport[ICAO])
        else:
            print('The ICAO code doesnt correspond to any airport')
    else:
        print('That is not an option!')







