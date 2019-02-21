# NYC-Taxi-Tips

Abstract
-
NYC TaxiTips filters past NYC taxi data based on date, location, and transit type.


Design process
-
I began my design thinking about the features that would ease my own transit, putting myself into the mindset of a NYC traveler, while keeping in mind the given API data. My list is as follows:
-based on a preference of saving either time or money or both, if yellow, green, or for hire is best
-tips to save money, ex avoiding extra charges
-tips to save time, ex traveling later or earlier
-tradeoffs of saving time/money, with lower tolls
-success rates of negotiated fares & their average savings
After weighing these features, I decided to pursue consumer research to think of additional features as well as rank their priorities. 

Market research
-
One of my friends recently started a full time job in NYC, so I asked her to participate in a quick user research study. Over FaceTime video call, I asked her to think of one recent instance where she used a taxi or rideshare in NYC. On my screen, I showed my MVP paper webpage and filled in her corresponding starting and ending boroughs. I then asked what tips would have been useful for her, telling her they can include details about ride start time, end time, tolls, rush hour charges, overnight charges, etc.

She described an overnight ride share trip between Brooklyn and Manhattan. Her advice changed my perspective greatly. I had been thinking of mostly money saving-related tools, but she stressed the annoyance of traffic in NYC and said that saving a few dollars is never worth the hassle of additional traffic, to her. She would generally use the subway in cases where time is less of a concern, as she uses taxis/ride shares when she needs to arrive somewhere by a deadline, such as to the airport or an appointment.

After listening to her ideas, I then shared my ideas. We discussed and ranked our ideas, combined, to create a priority-rated feature list. My top design goal became to create predictors for surge pricing and traffic/ trip time.


Solution
-
My first idea was to create a GitHub webpage to display money-saving tips based on starting and ending boroughs, and surge pricing. This idea was quickly quickly put to a halt as I realized GitHub Pages have to be static sites. I then looked into the many data science opportunities available with Python, and decided to make a Python-coded web app. I have never made a web app, but have some Python experience (using Anaconda and Jupyter, which I used for testing here as well), so I began with the familiar: writing a Python file with the logic of converting from Borough to LocationID, and vice versa, while writing unit tests in a separate file and testing in Jupyter as I went. My beginning data set contained four files: the zone/borough breakdown, and the Jan 2019 yellow, green, and for-hire files. The for-hire file gave me some trouble, as it was too big to download as a single csv file, so I kept it as the maximum csv file size, which goes up until Jan 20; 8490755 pieces of data, while not covering as great of a range of dates, provides an adequate representation of data points :). 

As I tested methods and waited for them to finish running, I concurrently began the web app. As this was new ground for me, I completed research of Django and Flask (two popular choices online). I decided on a Flask framework because it was simpler, and I did not need advanced functionality.  After some time spent beginning a non-functional web app, I went back to the drawing board and decided to create a simpler command line argument program.

I eventually had a program working that took in [-y] to filter yellow data, [-g] to filter green data, and [-f] to filter for-hire data. I moved on to add code to filter by time, then lastly code to filter by borough. This functionality became easier as I coded more, because I learned how to process the arguments. By the time I got to the borough filter, I created a method that could be used with all data sets. I could have written more concise code if I would have created methods for every one of these filters.

Testing
-
Test_Equations.py contains self tests for methods used within Calculations.py

I created mock data files of ~5 rows each so that I was able to mark myself whether the correct data was filtered within my tests. These are titled mock_fhv_data.csv, mock_green_data.csv, and mock_yellow_data.csv. They are hard-coded into the NYCTaxi.py file.

Due to a limitation of time, I was not able to address every program limitation that I encountered.

Known errors/limitations:
-Must enter known, correctly-spelled names as starting and ending boroughs
-Date and time must be in correct format and within the Python library's limitation of valid times and dates
-Time zone is in given time zone with no opportunity to switch to other time zones

Directions to use
-
Run on the command line using python NYCTaxi.py (then arguments)
Due to struggling taking too long testing the big data files, my project currently uses smaller mock data files (mock_zones.csv, mock_fhv_data.csv, mock_green_data.csv, and mock_yellow_data.csv) which are hard-coded into the beginning of NYCTaxi.py, and for testing you may need to check that the paths line up on your computer.

[-y] [-g] [-f]
These tags show to represent data from the yellow taxis [-y], green taxis [-g], and for-hire vehicles [-f]. Results from [-y] will be stored in filtered_yellow_data.csv, results from [-g] will be stored in filtered_green_data.csv, and results from [-f] will be stored in filtered_fhv_data.csv. The program must be run with at least one of these tags.

[--start DATE TIME]
[--end DATE TIME]
These tags filter the pickup time data, with [--start] representing the beginning range window and [--end] representing the ending range window. Each requires being followed by a date in the format YEAR-MM-DD HH:MM:SS. These tags are optional and can be used separately, eg. [--start] without [--end].

[--sborough BOROUGH]
[--eborough BOROUGH]
These tags filter the ride's starting and ending boroughs. The starting borough [--sborough] must be followed by a Borough Name and the ending borough [-eborough] must be followed by a Borough Name, as well. These tags are optional and can be used separately, eg. [--sborough] without [--eborough].

Example of all tags used combined on command line, with sample data:
python NYCTaxi.py -y -g -f --start 2018-01-01 00:21:04 --end 2018-01-01 00:21:06 --sborough Dog --eborough Dog


Project limitations
-
One limitation (as well as advantage for analyzation purposes) was the huge amount of data and the time it took my laptop to run all this data. As my inital tests were taking very long to run each, I created mock data files to save time testing. I decided to not import data past Jan 2019, which is only representative of one month (and only 20 days in the case of for-hire). I had been committing all my changes locally, but when I wanted to push the data, I ran into more errors because the .csv files, which had been in my project folders, are too large to be stored in GitHub.

Another limitation is in my market research. My research that helped to dictate my priorities only covered one rider’s experience on one ride in particular, which is clearly not representative of all taxi and for-hire rides in NYC. If I had more time, I would interview a variety of people about rides at different types of each day, using different methods. 

Time was ultimately the most major limitation. As this was the first Python command line project that I have created, I spent time researching every library and function used. I realized by the end that I spent too long researching possible features (and, in some cases, writing beginning code) which are ultimately less important than documenting and testing basic functionality.

