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
    global city
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("""What is the name of the city you\'re interested in investigating its data?
    ("Chicago", "New york city" or "Washington") """)).lower()

    while city not in ["chicago", "new york city", "washington"]:
        print("""Make sure you\'ve chosen from: Chicago, New york city or Washington.\n """)
        city = str(input("""What is the name of the city you\'re interested in investigating its data? """))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("""Please, write the desired month:
                     (All, January, February, March, April, May, June) """)).lower()
    while month.title() not in ["All", "January", "February", "March", "April", "May", "June"]:
        print("""Make sure you\'ve chosen from: All, January, February, March, April, May or June """)
        month = str(input("""What is the name of the month you\'re interested in investigating its data? """))
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("""Would you like show data about a specifec day of the week :
                     (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, sunday) """)).lower()
    while day.title() not in ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        print("""Make sure you\'ve chosen from: All, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday """)
        day = str(input("""What is the name of the day you\'re interested in investigating its data? """))


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
    # loading the data file.
    df = pd.read_csv(CITY_DATA[city])
    
    # making the Start Time column processable.
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    # Extraction of month and day.
    df["month"] = df["Start Time"].dt.month
    df["day"] =  df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month is : {}".format(most_common_month))
    
    # TO DO: display the most common day of week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    
    most_common_dayofweek = df["day"].mode()
    print("The most common day of the week is : {}".format(most_common_dayofweek))
    
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    most_common_hour = df["hour"].mode()[0]
    print("The most common hour of the day is : {}".format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df["Start Station"].mode()
    print("The most common start station is : {}".format(most_common_start))
    
    # TO DO: display most commonly used end station
    most_common_end = df["End Station"].mode()
    print("The most common destination is : {}".format(most_common_end))
    
    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + " to " + df["End Station"]
    most_common_route = df["combination"].mode()
    print("The most common route is : {}".format(most_common_route))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    
    # creat a readable format of total travel time
    D = total_travel_time // 86400  # there are 86400 secs in a day
    d = total_travel_time % 86400 

    H = d // 3600   # there are 3600 secs in an hour
    h = d % 3600

    M = h // 60 
    m = h % 60

    S = m

    print("The total travel time is : {} days {} hours {} mins {} secs".format(D, H, M, S))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is : {} secs ".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("""The types of users are as follows:
    {}""".format(user_types))

    if city in ["chicago", "new york city"]:
        # TO DO: Display counts of gender
        gender_counts = df["Gender"].value_counts()
        print("""The gender counts of users are as follows:
        {}""".format(gender_counts))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df["Birth Year"].min())
        most_recent = int(df["Birth Year"].max())
        most_common = int(df["Birth Year"].mode()[0])
        
        print("""Our oldest user was born in {}
        Our youngest user was born in {}
        Most common year of birth among our users is {}        
        """.format(earliest, most_recent, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

              

def ans(df):
    n = 0
    N = 5
    i = "y"
    while True:
        answer = str(input("""If you want to see raw data say yes. 
        "y" for yes, "n" for no: """)).lower()
        if answer == i:
            print(df.iloc[n:N])
            n += 5
            N += 5
        else: break
        
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ans(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
