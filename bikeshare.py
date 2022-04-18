import time
import datetime as dt
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

for city in CITY_DATA:
    print(city)

def get_filters():

    print('\nHello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Please select city a city from above:").lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Not an allowed city, please try again.")
        else:
            break

    while True:
        month = input('Please enter a month. User can enter any month between January and June or simply type all to show all available months: ').lower()
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Not an allowed month, please try again.")
        else:
            break

    while True:
        day = input('Please enter a day. User can enter any day or simply type all to show all available days: ').lower()
        if day.lower() not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print("Not an allowed day, please try again.")
        else:
            break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print ('The most commonly used start and end station is: ', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    total_trip = df['Trip Duration'].sum()
    print('The total trip duration for all rides in seconds is: \n', total_trip)


    # TO DO: display mean travel time
    avg_trip = df['Trip Duration'].mean()
    print('\nThe average trip duration for all rides in seconds is: \n', avg_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nTotal counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    while True:
        city = input("\nPlease re-confirm city for Gender information:").lower()
        if city in ('chicago', 'new york city'):
            gender = df['Gender'].value_counts()
            print('\nTotal counts of gender types:\n', gender)
            break
        else:
           print('No gender information available')
           break


    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        city = input("\nPlease re-confirm city for Birth information:").lower()
        if city.lower() in ('chicago', 'new york city'):
            min_birth_year = df['Birth Year'].min()
            print('\nThe earliest birth year is: ', min_birth_year)


            max_birth_year = df['Birth Year'].max()
            print('\nThe most recent birth year is: ', max_birth_year)


            common_birth_year = df['Birth Year'].mode()[0]
            print('\nThe most common birth year is: ', common_birth_year)
            break

        else:
           print('No birth information available')
           break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data."""
    raw = input('Would you like to see raw data? Please enter Yes or No: ').lower()
    i = 0

    while True:
        if raw == 'yes':
            print(df.iloc[i:5+i])
            raw = input('Would you like to see more raw data? Please enter Yes or No:  ').lower()
            i += 5
        else:
            print('no more data')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
