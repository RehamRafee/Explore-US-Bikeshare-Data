import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_count.idxmax
    print('\nThe most commonly used start station:', start_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_count.idxmax
    print('\nThe most commonly used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).agg(lambda x: stats.mode(x)[0][0])
    print('The most frequent combination of start station and end station trip is:', combination)