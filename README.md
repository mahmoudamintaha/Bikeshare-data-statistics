# Bikeshare-data-statistics
used python and pandas to show statistics according to user input
I am happy to share my first data analysis project using python and pandas. (first project in Udacity's professional track for data analysis)

I programmed this script to show descriptive statistics according to the input of the user who chooses the filter to be applied, Such as city, month and day.

1- Python :
- helped user choose the right filter with clear prompts.
- prevented crash as a result of invalid input.
- gave the user an opportunity to see raw data.
- if the user asked for data about (Washington), since (Gender or Birth year) columns do not exist in Washington's data it will not show up and wont raise any error.
- converted the output of journey duration (secs) to
(days : hours : mins : secs)

2- Pandas :
- created (month & day) columns by extracting them from the (Start Time) column which is a time stamp.
- created a new column containing a combination of (Start station) and (End station) to study most common routes.
- showed random samples of data when user decides to see raw data.
- data analysis according to user input.


3- Questions answered:
- what is the most common (month, day of week, hour of day)?
- what is the most common (start, end station, route)?
- what is the (total, mean) travel time during the chosen filter?
- what is the number of (females, males) among users?
- what is the number of (subscribers, customers) among users?
- what is the (earliest, latest, most common) year of birth among users?
