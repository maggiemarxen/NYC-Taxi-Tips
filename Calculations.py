import numpy
import pandas as pd
from sys import argv
from argparse import ArgumentParser as Parse
from datetime import datetime

# function to calculate cost of the ride. Cost does not include tip
# Note: cost does not include tip to prevent inaccuracies, as some were via cash and some were via credit
def calculate_cost(fare_amount, extra, mta_tax, tolls_amount, improvement_surcharge):
    return (fare_amount + extra + mta_tax + tolls_amount + improvement_surcharge)

# filters information by start and/or end borough using zone dictionary
def calc_start_end(df, args, zone_id_dict, s_column, e_column):
    if ("sborough" in args and args["sborough"] is not None):
        zone_dict = convert_zone_ID(zone_id_dict, args["sborough"][0])
        df = df[df[s_column].isin(zone_dict)]
    if ("eborough" in args and args["eborough"] is not None):
        zone_dict = convert_zone_ID(zone_id_dict, args["eborough"][0])
        df = df[df[e_column].isin(zone_dict)] 
    return df 

# dictionary where Key is Borough name, and Values are LocationIDs
def init_zone_dict(zonedf):
    zone_id_dict = {}
    for (index, row) in zonedf.iterrows():
        if (row['Borough']) in zone_id_dict:
            zone_id_dict[row['Borough']].append(row['LocationID'])
        else:
            zone_id_dict[row['Borough']] = [row['LocationID']]
    return zone_id_dict

# using Borough name as Key, returns a list of associated LocationIDs
def convert_zone_ID(zone_id_dict, zone):
    return zone_id_dict.get(zone)

# will return value if (from_zone, to_zone) is in the given dictionary,
# else returns None
# note: untested
def compute_one_method_cost(from_zone, to_zone, zone_id_dict, given_dict):
    given_cost = 0
    given_count = 0
    for from_id in convert_zone_ID(zone_id_dict, from_zone):
        for to_id in convert_zone_ID(zone_id_dict, to_zone):
            if (from_id, to_id) in given_dict:
                cost_list = given_dict.get((from_id, to_id))
                for one_cost in cost_list:
                    given_cost = given_cost + one_cost
                    given_count = given_count + 1
    if given_count is not 0:
        return given_cost / given_count

# given two zones, computes an average cost using yellow and green taxi data
# note: untested
def compute_avg_cost(from_zone, to_zone, green_dict, yellow_dict, zone_id_dict):
    avg_cost = 0
    if compute_one_method_cost(from_zone, to_zone, zone_id_dict, green_dict) is not None:
        avg_green_cost = compute_one_method_cost(from_zone, to_zone, zone_id_dict, green_dict)
        avg_cost = avg_cost + avg_green_cost
    if compute_one_method_cost(from_zone, to_zone, zone_id_dict, yellow_dict) is not None:
        avg_yellow_cost = compute_one_method_cost(from_zone, to_zone, zone_id_dict, yellow_dict)
        avg_cost = avg_cost + avg_yellow_cost

    return (avg_green_cost + avg_yellow_cost) / 2

# dictionary where Key is a tuple of (pick up location ID, drop off location ID), and Values are costs of rides between    
# contains error!!
def calc_dict_costs(df, s_column, e_column): 
    df_dict = {}   
    df = df.reset_index()
    for (index, row) in df.iterrows():
        if (int(row.loc[s_column]), int(row.loc[e_column])) in df_dict:
            df_dict[(row[s_column], row[e_column])].append(calculate_cost(row['fare_amount'], row['extra'], row['mta_tax'], row['tolls_amount'],  row['improvement_surcharge']))
        else:
            df_dict[(row[s_column], row[e_column])] = [calculate_cost(row['fare_amount'], row['extra'], row['mta_tax'], row['tolls_amount'], row['improvement_surcharge'])]
    return df_dict
     