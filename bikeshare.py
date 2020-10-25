import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }

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
        city = str(input('\nPlease choose the city to see the data: Chicago (C), New York City (N) or Washington (W)?: ').strip().lower())

        if city not in ('c', 'n', 'w'):
            print('\nInvalid response. Please try again.')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = str(input('\nPlease choose the month to filter the data: all, January, February, ... or June: ').strip().lower())

        if month not in ( 'all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('\nInvalid response. Please try again.')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = str(input('\nPlease choose the day of the week: all, Monday, Tuesday, ... or Sunday: ').strip().lower())

        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('\nInvalid response. Please try again.')
            continue
        else:
            break

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_index = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    popular_month = month_index[str(df['month'].mode()[0])]
    print('Most common month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most used start station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most used end station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' - ' + df['End Station']
    popular_combination = df['Station Combination'].mode()[0]
    print('Most frequent combination of start station and end station trip: {}'.format(popular_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    d = str(int(total_travel_time // (24 * 60 * 60)))
    h = str(int((total_travel_time % (24 * 60 * 60)) // (60 * 60)))
    m = str(int(((total_travel_time % (24 * 60 * 60)) % (60 * 60)) // 60))
    s = str(int(((total_travel_time % (24 * 60 * 60)) % (60 * 60)) % 60))

    print('Total travel time: {}d {}h {}min {}s'.format(d, h, m, s))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    m = str(int(mean_travel_time // 60))
    s = str(int(mean_travel_time % 60))

    print('Mean travel time: {}min {}s'.format(m, s))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts().to_string()
    print('Counts of user types:\n{}\n'.format(user_types_counts))

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts().to_string()
        print('Counts of gender:\n{}\n'.format(gender_counts))

    except KeyError:
        print('There is no data about gender for this city.\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print('Birth year of the oldest user: {}'.format(earliest_birth_year))

        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print('Birth year of the youngest user: {}'.format(most_recent_birth_year))

        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print('Most common birth year: {}'.format(most_common_birth_year))

    except:
        print('There is no data about year of birth for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Display 5 line raw data each time."""

    raw_input = input('\nWould you like to see the raw data? Enter yes (y) or no (n).\n')
    if raw_input.lower() != 'y':
        return
    i = 0
    while len(df.index) >= i:
        print('\n')
        print(df.iloc[i:i+5].to_string())
        i += 5
        raw_next_rows = input("\nWould you like to see the next 5 rows? Enter yes (y) or no (n)\n")

        if raw_next_rows.lower() != 'y':
            break

    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes (y) or no (n).\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
