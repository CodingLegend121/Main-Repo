import random
# My Database
first_names = ['James',    'John',    'Robert',  'Michael', 'William',
               'David',    'Richard',  'Joseph',  'Thomas',  'Charles', 'Christopher',
               'Daniel',   'Matthew',  'Anthony', 'Donald',  'Mark',    'Paul',
               'Steven',   'Andrew',   'Kenneth', 'George',  'Joshua',  'Kevin',
               'Brian',    'Edward',   'Mary',    'Patricia', 'Jennifer', 'Elizabeth',
               'Linda',    'Barbara',  'Susan',   'Jessica', 'Margaret', 'Sarah',
               'Karen',    'Nancy',    'Betty',   'Lisa',    'Dorothy', 'Sandra',
               'Ashley',   'Kimberly', 'Donna',   'Carol',   'Michelle', 'Emily',
               'Amanda',   'Helen',    'Mellisa', 'Carlos',  'Connor', 'Benjamin',
               'Logan',	'Noah',     'Cooper',  'Megan',   'Austin',  'Evan',
               'Tyler',    'Zach',		'Zoe',     'Jamie',   'Alicia',  'Kristin',
               'Liam',		'Wilbur',	'Orvile',  'Jake',	  'Ryan',	 'Jana',
               'Bruce', 'Harry', 'Peter'
               ]
last_names = [	  'Smith',    'Johnson',   'Williams', 'Jones',     'Brown',
                 'Odinson',  'Davis',    'Miller',    'Wilson',   'Moore',     'Taylor',
                 'Anderson', 'Thomas',   'Jackson',   'White',    'Harris',    'Martin',
                 'Thompson', 'Garcia',   'Martinez',  'Robinson', 'Clark',		'Black',
                 'Rodriguez', 'Lewis',    'Lee',       'Walker',   'Hall',  	'Allen',
                 'Young',    'Hernandez', 'King',      'Wright',   'Lopez',     'Hill',
                 'Scott',    'Green',    'Adams',     'Baker',    'Gonzalez',  'Nelson',
                 'Roberts',  'Turner',   'Philips',   'Campbell', 'Parker',    'Evans',
                 'Edwards',  'Collins',  'Kenway',    'Connor',   'Scarbrough', 'Keller',
                 'Anwar',    'McGee',    'Yarberry',  'Kristol',  'Jardine',   'Rice',
                 'Angst',	  'Heinman',  'Washington', 'Jefferson', 'Durant',	'Trump',
                 'Banner',	  'Stark'
                 ]
# main code


def name_stuff():
    x = 1
    p = input(
        'What do you need\n[ l for List  ](<- use this for now)\n[ d for Decode]\n[ e to Encode ]\n\n')
    # List
    if p == 'l':
        num = input('A list of how many names ?\n')
        while(x <= int(num)):
            a = random.choice(first_names)
            b = random.choice(last_names)
            full_name = (str(x) + '.|   ' + a + ' ' + b + ' (' +
                         str(first_names.index(a)) + '/' + str(last_names.index(b)) + ')')
            print(full_name)
            x = x + 1
    # Decode
    elif p == 'd':
        fn = input('Code\n')
        ft, lt = fn.split('/')
        print('___________________\n            \n' +
              first_names[int(ft)] + ' ' + last_names[int(lt)] + '\n___________________')
    # Encode
    elif p == 'e':
        name = input('Enter a valid name (Check for Caps)\n')
        fa, la = name.split(' ')
        decode = str(first_names.index(fa)) + '/' + str(last_names.index(la))
        print('_______\n          \n' + decode + '\n_______')
    # ERROR
    else:
        print('Rerun	ERROR')


def date_stuff():
    SLDate = input('One [o] or More [m]\n')
    if SLDate == 'o':
        year_change = input(
            'The default year range is 1945 - 2005.\n Wanna change it? [y/n]\n')
        if year_change == 'y':
            MinMaxYear = input('Enter the Min-Max Year\n')
            minYear, maxYear = MinMaxYear.split('-')
            year = random.randrange(int(minYear), int(maxYear))
            month = random.randrange(1, 12)
            date = random.randrange(1, 30)
        elif year_change == 'n':
            year = random.randrange(1945, 2005)
            month = random.randrange(1, 12)
            date = random.randrange(1, 30)
        print(str(month) + '/' + str(date) + '/' + str(year))
    elif SLDate == 'm':
        LDate = input('How many\n')
        x = 1
        while x <= int(LDate):
            year = random.randrange(1945, 2005)
            month = random.randrange(1, 12)
            date = random.randrange(1, 30)
            full_date = (str(month) + '/' + str(date) + '/' + str(year))
            print(full_date)
            x = x + 1


main_thing = input('Do you want a\n[n - Name]\n[d - Date]\n[b - Both]\n')
if main_thing == 'n':
    name_stuff()
elif main_thing == 'd':
    date_stuff()
elif main_thing == 'b':
    a = random.choice(first_names)
    b = random.choice(last_names)
    year = random.randrange(1945, 2005)
    month = random.randrange(1, 13)
    date = random.randrange(1, 31)
    print('______________\n')
    print(a + ' ' + b + '\n' + str(month) + '/' + str(date) + '/' + str(year))
    print('______________')
