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
        city = input('Input city name you would like to explore: Chicago, New York City, or Washington: ').lower()
        if city not in CITY_DATA:
            print("The city name you entered is not valid. Please input either Chicago, New York City, or Washington: ")
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Input the name of the month you would like to explore between january and june. You can also type "all" to display all months: ').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Input the day of the week you would like to explore. You can also type "all" to display all days: ').lower()
        days = ['sunday', 'monday', 'tuesday', 'thursday', 'friday', 'saturday']
        if day != 'all' and day not in days:
            print('the day you entered is not valid')

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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most Common Month: {}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day: {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:  {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:  {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip

    frequent_start_end_station = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip: {}".format(frequest_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Counts of User Types: {}".format(count_user_types))


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("Counts of Gender: {}".format(gender_count))
    except KeyError:
        print('The city you selected does not have gender data')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print("Earliest Birth Year: {}".format(round(earliest_year)))
        recent_birth_year = int(df['Birth Year'].max())
        print("Most Recent Birth Year: {}".format(round(recent_birth_year)))
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("Most Common Year of Birth: {}".format(round(Common_birth_year)))


    except KeyError:
        print('The city you selected does not have birth year data')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

# To display raw data

def display_raw_data(df):

    display_data_input = input("Would you like to display data for your chosen location? Enter YES or NO: ").lower()
    index = 0
    while display_data_input =='yes':
        print(df.iloc[index:index+5])
        index = index + 5
        display_data_input = input("Do you want to see 5 more rows of this data? Enter YES or NO: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
