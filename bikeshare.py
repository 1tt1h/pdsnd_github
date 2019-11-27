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
    cities = ['chicago', 'new_york_city', 'washington']
    print('Which city would you like to explore')
    city = input('Enter chicago, new york city or washington: ')
    while city.lower() not in cities:
        print('Wrong input')
        city = input('Please enter available city:')
    print('Great! we are checking data for', city.lower())


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('\nWhich month would you like to explore')
    month = input('Enter months from january to june or "all" if you dont want to filter by month: ')
    while month.lower() not in months:
        print('Wrong input')
        month = input('Please enter available month: ')
    print('Great! we are checking data for', month.lower())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('\nWhich day of the week would you like to explore')
    day = input('Enter any day of the week or "all" if you dont want to filter by day: ')
    while day.lower() not in days:
        print('Wrong input')
        day in input('Please enter correct day: ')
    print('Great! we are checking data for', day.lower())



    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    #Load city_data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month, day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] ==day.title()]
        #displaying answer if user want to view first five rows of data or not
    while True:

        answer = input('\nWould you like to view raw data? Enter yes or no\n').lower() #added raw

        if answer == 'yes':
            print('First five raw data\n', df.head())
            print('Last five raw data\n', df.tail())
            print('Data statistics of raw data\n', df.describe())

            break

        elif answer == 'no':
           break

        else:
           True
    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + ' to ' + df['End Station']
    common_combo = df['comb'].mode()[0]
    print('Most frequent combination of start and end station: ', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total trip duration: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean Travel time: {}minutes'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Type: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Total Gender Count: ', gender_count)
    else:
        print('Gender information is not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year: ', int(common_birth_year))
    else:
        print('Birth year information is not available for this city')

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
