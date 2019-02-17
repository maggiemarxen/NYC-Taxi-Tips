import pandas as pd

#open file
##todo: change to absolute link
zonedf = pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\taxi+_zone_lookup.csv")
greendf = pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\green_tripdata_2018-01.csv")

def calculate_cost(fare_amount, extra, mta_tax, tolls_amount, ehail_fee, improvement_surcharge):
    return (fare_amount + extra + mta_tax + tolls_amount + ehail_fee + improvement_surcharge)

dict = {}

zonedf.rename(index={5: 'PULocationID'})

zonedf.index.names = ['index']

zone_id_dict = {}
for (index, row) in zonedf.iterrows():
    if (row['Borough']) in zone_id_dict:
        zone_id_dict[row['Borough']].append(row['LocationID'])
    else:
        zone_id_dict[row['Borough']] = [row['LocationID']]
        print(zone_id_dict[row['Borough']])
        
for (index, row) in greendf.iterrows():
    if (int(row.loc['PULocationID']), int(row.loc['DOLocationID'])) in dict:
        dict[(row['PULocationID'], row['DOLocationID'])].append(calculate_cost(row['fare_amount'], row['extra'], row['mta_tax'], row['tolls_amount'], row['ehail_fee'], row['improvement_surcharge']))
    else:
        dict[(row['PULocationID'], row['DOLocationID'])] = [calculate_cost(row['fare_amount'], row['extra'], row['mta_tax'], row['tolls_amount'], row['ehail_fee'], row['improvement_surcharge'])]
        print([(row['PULocationID'], row['DOLocationID'])])
        
for k,v in dict.iteritems():
    # v is the list of grades for student k
    avgDict[k] = sum(v)/ float(len(v))
    print(avgDict[k])
    
print(dict)