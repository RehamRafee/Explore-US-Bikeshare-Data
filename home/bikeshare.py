import time
import pandas as pd
import numpy as np


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
   
        # get user input for month (all, january, february, ... , june)
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = input('\n\n Now,you have to choose to filter the {} data  by month or not:\n if yes please type the month name \n January\n February\n March \n April\n May\n June\n\nif you don\'t want to filter the data please type all'.format(city.title())).lower()
        while month not in months:
            print("that is wrong choice, please type the month name or all")
            month = input('\n\n Now,you have to choose to filter the {} data  by month or not:\n if yes please type the month name \n January\n February\n March \n April\n May\n June\n\nif you don\'t want to filter the data please type all'.format(city.title())).lower()
  
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday','all']
        day = input('\n\n Now,you have to choose to filter the {} data  by a particular day or not:\n if yes please type the day name\n  Monday \n  Tuesday \n  Wednesday \n  Thursday \n  Friday\n  Saturday \n  Sunday \n if you don\'t want to filter the data by a particular day: \nplease, type (all)'.format(city.title())).lower()
        while day not in days:
            print("that is wrong choice, please type the day name or all")
            day = input('\n\n Now,you have to choose to filter the {} data  by a particular day or not:\n if yes please type the day name\n  Monday \n  Tuesday \n  Wednesday \n Thursday \n  Friday\n  Saturday \n  Sunday \n if you don\'t want to filter the data by a particular day: \nplease, type (all)'.format(city.title())).lower()
     
            
        print('-'*40)
        return city, month, day
 
    filtered_values = get_filters()
    city, month, day = filtered_values

    
        
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df
 


def time_stats(df,city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # load data file into a dataframe

    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month

   # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
   # find the most common month
    common_month = df['month'].mode()[0]

    print('Most common month:', common_month)

    # TO DO: display the most common day of week

 # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day
   # find the most common month
    common_day = df['day'].mode()[0]

    print('Most common day:', common_day)
    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station:', start_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+'-'+df['End Station']
    most_frequent_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is:', most_frequent_combination)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in minutes is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in seconds is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user type is', user_types)

    # TO DO: Display counts of gender

    try:
        gender = df['Gender'].value_counts()
        print('\n the users count of gender is:',gender)
    except KeyError:
        print('This information is not available for Washington!')
         
 
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington': 
        earliest_year_of_birth = df['Birth Year'].min()
        print('\n The earliest year of birth is:',earliest_year_of_birth)
        most_recent_year_of_birth = df['Birth Year'].max()
        print('\n The most recent year of birth is:',most_recent_year_of_birth)
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('\n The most common year of birth is:',most_common_year_of_birth)
  
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(city):
    ''' here we ask the user if he want to see the raw data 5 rows by time, if he answered «yes»'''
    #First,  we ask the user if he want us to display raw data
    display_raw = input( "\n Would you like to see raw data, please type (yes) or (no)").lower() 
   #loop over the chunks in the pd.read_csv
    while display_raw == 'yes':
        try:
            for chunks in pd.read_csv(CITY_DATA[city],chunksize= 5):
                print(chunks) 
                
                display_raw = input("\n DO you want to see more raw data, please type (yes) or (no)").lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break       
        except KeyboardInterrupt:
            print('Thank you.')
            
        
                                    
                                       
                                    
             
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n') 
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
