import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'all','january','february','march','april','may','june'}
days = { 'sunday ','monday','tuesday','wednesday','thursday','friday','saturday','all'}
def get_filters() :
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        city = input('What city would you like to analyze? Chicago, New York City or Washington?: ').lower()
        if city in (CITY_DATA.keys()):
            print('We will be analyze for ', city.capitalize(),'. ')
            break
        else:
            print("Please choose Chicago, New York City or Washington")
            
    while True:
        month = input('Which month would you like to analyze? January, February, March, April, May, June or All?: ').lower()
        if month in (months):
            print('We will be analyze for ',city.capitalize(),' in ' ,month)
            break
        else:
            print("Please choose from January, February, March, April, May, June or All")
 
    while True:
        day = input('What day of the week would you like to analyze? Sunday, Monday, etc: ').lower()
        if day in (days):
            print('We will be analyze for ', day)
            break
        else:
            print("Please choose Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday  ")

        
    print('-'*40)
    return city,month,day
  

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all' :
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        df = df[df['day_of_week'] == days.index(day.title())]
   
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combination is: {}".format(df['routes'].mode().values[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:" , start_time/86400, " days")
    
    # TO DO: display mean travel time
    avg_travel_time= df['Trip Duration'].mean()
    print('Mean travel time: ',avg_travel_time/60, " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user = df['User Type'].value_counts()
    print('Counts of user types: ',count_user)

    # TO DO: Display counts of gender
    try:

       gender_types = df['Gender'].value_counts()

       print('\nGender types:\n', gender_types)

    except KeyError:

          print("\nGender Types:\nThere is no data for this month.")



    # TO DO: Display earliest, most recent, and most common year of birth
    try:

        min_birth_year = df['Birth Year'].min()

        print('\nEarliest birth year:', min_birth_year)

    except KeyError:

           print("\nEarliest Year:\nThere is no data for this month.")
    try:

        max_birth_year = df['Birth Year'].max()

        print('\nMost recent birth year:', max_birth_year)

    except KeyError:

           print("\nMost recent birth year:\nThere is no data for this month.\n")  
    try:

        most_common_year = df['Birth Year'].value_counts().idxmax()

        print('\nMost common year:', most_common_year)

    except KeyError:

          print("\Most common year:\nThere is no data for this month.")        
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):

    i = 0

    raw = input("\nWould you like to see the first 5 rows of raw data? Type 'yes' or 'no'\n").lower()

    pd.set_option('display.max_columns',200)

    while True:

         if raw not in ['yes', 'no']:

             print("Incorrect response. Please try again!")

             raw_input = input("\nWould you like to see first 5 rows of raw data? Type 'yes' or 'no'\n").lower()

             continue

         elif raw == 'no':

              break

         else:

              print(df[i:i+5])

              raw = input('\nWould you like to see next rows of raw data?\n').lower()

              i += 5            
    print('-'*40)        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
