import numpy
import pandas as pd
from sys import argv
from argparse import ArgumentParser as Parse
import datetime
import Calculations

# #open file
# zonedf_path = r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\taxi+_zone_lookup.csv"

# greendf_path = r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\datafiles\green_tripdata_2018-01.csv"

# yellowdf_path = r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\datafiles\yellow_tripdata_2018-01.csv"

# fhvdf_path = r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\datafiles\fhv_tripdata_2018-01.csv"

# saves link to mock zone csv
zonedf = pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_zones.csv")

# creates dictionary of zone IDs associated with boroughs
zone_id_dict = Calculations.init_zone_dict(zonedf)


# -y -g -f include data from given service providers (y for yellow, etc.)
parser = Parse(description='Given start and end borough, displays average cost.')
parser.add_argument('-y', action="store_true", default=False)
parser.add_argument('-g', action="store_true", default=False)
parser.add_argument('-f', action="store_true", default=False)

# --start 00/00/0000 00:00:00 --end 00/00/0000 00:00:00
parser.add_argument("--start", nargs=2, action="store")
parser.add_argument("--end", nargs=2, action="store")

# --sborough BoroughName --eborough BoroughName
parser.add_argument("--sborough", nargs=1, action="store")
parser.add_argument("--eborough", nargs=1, action="store")

# parse arguments
args = vars(parser.parse_args()) 

# must select at least one data source. else, error
if args["y"] is False and args["g"] is False and args["f"] is False:
    print("error: must choose at least one list")
    exit()

# create datetime object for command line start information
if "start" in args and args["start"] is not None:
    year, month, day = map(int, args["start"][0].split('-'))
    start_date = datetime.date(year, month, day)
    start_time = datetime.datetime.strptime(args["start"][1],'%H:%M:%S').time()
    time_object_start = datetime.datetime.combine(start_date, start_time)
    # if end date is not given, make end date into the future
    if "end" in args and args["end"] is None:
        end_date = datetime.datetime(2050, 1, 1)
        end_time = datetime.datetime.strptime("00:00:00",'%H:%M:%S').time()
        time_object_end = datetime.datetime.combine(end_date, end_time)
# create datetime object for command line end information
if "end" in args and args["end"] is not None:
    year, month, day = map(int, args["end"][0].split('-'))
    end_date = datetime.date(year, month, day)
    end_time = datetime.datetime.strptime(args["end"][1],'%H:%M:%S').time()
    time_object_end = datetime.datetime.combine(end_date, end_time)
    # if start date is not given, include all information from beginning
    if "start" in args and args["start"] is None:
        start_date = datetime.datetime(1900, 1, 1)
        start_time = datetime.datetime.strptime("00:00:00",'%H:%M:%S').time()
        time_object_start = datetime.datetime.combine(start_date, start_time)
# read in yellow information
if args["y"] is True:
    tot_list = []
    tot_list.append(pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_yellow_data.csv",index_col=0, header=0))
    df = pd.concat(tot_list, axis = 0, ignore_index = False)
    # filter by pick up date/time
    if (("start" in args and args["start"] is not None) or ("end" in args and args["end"] is not None)):
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        mask = (df['tpep_pickup_datetime'] > time_object_start) & (df['tpep_pickup_datetime'] <= time_object_end)
        df.loc[mask]
        df = df.loc[mask]
    # filter if start/end info is given
    df = Calculations.calc_start_end(df, args, zone_id_dict, 'PULocationID', 'DOLocationID')  
    df.to_csv("filtered_yellow_data.csv")
# read in green information
if args["g"] is True:
    tot_list = []
    tot_list.append(pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_green_data.csv",index_col=0, header=0))
    df = pd.concat(tot_list, axis = 0, ignore_index = False)
    # filter by pick up date/time
    if (("start" in args and args["start"] is not None) or ("end" in args and args["end"] is not None)):
        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
        mask = (df['lpep_pickup_datetime'] > time_object_start) & (df['lpep_pickup_datetime'] <= time_object_end)
        df.loc[mask]
        df = df.loc[mask]
    # filter if start/end info is given
    df = Calculations.calc_start_end(df, args, zone_id_dict, 'PULocationID', 'DOLocationID') 
    df.to_csv("filtered_green_data.csv")
# read in for-hire information
if args["f"] is True:
    tot_list = []
    tot_list.append(pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_fhv_data.csv",index_col=0, header=0))
    df = pd.concat(tot_list, axis = 0, ignore_index = False)
    # filter by pick up date/time
    if (("start" in args and args["start"] is not None) or ("end" in args and args["end"] is not None)):
        df['Pickup_DateTime'] = pd.to_datetime(df['Pickup_DateTime'])
        mask = (df['Pickup_DateTime'] > time_object_start) & (df['Pickup_DateTime'] <= time_object_end)
        df.loc[mask]
        df = df.loc[mask]
    # filter if start/end info is given
    df = Calculations.calc_start_end(df, args, zone_id_dict, 'PUlocationID', 'DOlocationID') 
    df.to_csv("filtered_fhv_data.csv")





