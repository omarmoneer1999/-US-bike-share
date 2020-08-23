import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': r'C:\Users\omarm\OneDrive\Desktop\bikeshare-2\chicago.csv',
              'n': r'C:\Users\omarm\OneDrive\Desktop\bikeshare-2\new_york_city.csv',
              'w': r'C:\Users\omarm\OneDrive\Desktop\bikeshare-2\washington.csv' }


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
        city = input('enter the desired city to filter it (c) for chicago, (n) for new york city, (w) for wachington\n').strip().lower()
        if city in ('c', 'n', 'w'):
            break
        else:
                print('the entered choice is wrong')# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('enter the desired month to filter it by months = [january , february, march, april, may, june or all]\n').strip().lower()
        if month in ('january' , 'february', 'march', 'april', 'may', 'june' , 'all'):
            break
        else:
            print('the entered choice is wrong')
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the wanted day [monday , tuesday, wednesday, thursday, friday, saturday, sunday or all]\n').strip().lower()
        if day in ('monday' , 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ,'all'):
            break
        else:
                print('the entered choice is wrong')


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

    
    if day != 'all':
        
        days = ['monday' , 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df

   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("the most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_dayofweek=df['day_of_week'].mode()[0]
    print("the most common day of week is: ", common_dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_starthour = df['hour'].mode()[0]
    print('the most common start hour', common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used End station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Comb_startandend = df.groupby(['Start Station','End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel = sum(df['Trip Duration'])
    print('\nTotal travel time',Total_travel/86400, " Days")

    # TO DO: display mean travel time
    mean_total_travel = df['Trip Duration'].mean()
    print('Mean travel time:', mean_total_travel/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\ncounts of user types',df['User Type'].value_counts())
    # TO DO: Display counts of gender
    try:
        print('\ncounts of gender',df['gender'].value_counts())
    except KeyError:
        print('Sorry,this state doesn\'t have gender data yet')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth',df['Birth Year'].max())
        print('the most recent year of birth',df['Birth Year'].min())
        print('the most common year of birth', df['Birth Year'].mode()[0])
    except KeyError:
        print('Sorry,this state doesn\'t have birth data yet')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
