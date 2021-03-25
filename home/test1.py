CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
 
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city_selection = input('\n\nFirst, please choose a city to start with:\n for Chicago type letter(a)\n for New York City type letter(b)\n for Washington type letter(c)').lower()
            if city_selection ==['a'] or ['b'] or ['c']:
                break 
        except KeyboardInterrupt:
            print('Oops, \n no order taken')
            print('Please, type the chosen letter again')
        else:
            print('Wrong choice')
            print('Please, type the chosen letter again')

    city_selections = {'a':'chicago', 'b':'new york city', 'c':'washington'}
    if city_selection in city_selections.keys():
        city = city_selections[city_selection]
       
 # get user input for month (all, january, february, ... , june)
   
        month_selection= {'january':'1', 'february':'2', 'march':'3', 'april':'4', 'may':'5', 'june':'6','no filter':'all'}
        months = input('\n\n Now,you have to choose to filter the {} data  by month or not:\n if yes please type\n (1) for January \n (2) for February \n (3) for March \n (4) for April \n (5) for May\n (6) for June \n if you don\'t want to filter the data by month: \nplease, type (all)'.format(city.title())).lower()

        while True:
            try:
                months = input('\n\n Now,you have to choose to filter the {} data  by month or not:\n if yes please type\n (1) for January \n (2) for February \n (3) for March \n(4) for April \n (5) for May\n(6) for June \n if you don\'t want to filter the data by month: \nplease, type (all)'.format(city.title())).lower()
                if months in month_selection.keys():
                    break
            except months not in month_selection:
                 print('Oops, Wrong choice')
                 print('Please, choose again')
            else:
                 print('please, Try Again')
                
        if month in month_selection.keys():
            month = month_selection[months]

 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            days_selection = {'monday':'m', 'tuesday':'tu', 'wednesday':'w','thursday':'th', 'friday':'f', 'saturday':'sa', 'sunday':'su', 'no day filter':'all'}
            while True:
                 try:
                     days = input('\n\n Now,you have to choose to filter the {} data  by a particular day or not:\n if yes please type\n (m) for Monday \n (tu) for Tuesday \n (w) for Wednesday \n(th) for Thursday \n (f) for Friday\n(sa) for Saturday \n(su) for Sunday \n if you don\'t want to filter the data by a particular day: \nplease, type (all)'.format(city.title())).lower
                     if days in days_selection.keys():
                         break
                 except days not in day_selection:
                     print('Oops, Wrong choice')
                     print('Please, choose again')
                 else:
                     print('please, Try Again')
            if day in day_selection.keys():
                day = day_selection[days]
                return day
        print('-'*40)
        return city, month, day
