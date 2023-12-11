import sys
import pandas as pd
import os

input_file = sys.argv[1]
output_dir = sys.argv[2]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# data = pd.read_parquet('./sample_data/input/test_data.parquet')
data = pd.read_parquet(input_file)
# print(data.shape)

data['timestamp_datetime'] = pd.to_datetime(data['timestamp'])

for unit in data['unit'].unique():
    trip_count = 0
    i = 1
    unit_data = data[data['unit'] == unit]
    while i < unit_data.shape[0]:
        # print(data.shape,i)
        time_diff = unit_data.iloc[i]['timestamp_datetime'] - unit_data.iloc[i - 1]['timestamp_datetime']
        seconds = time_diff.total_seconds()
        i = i + 1
        if seconds > 7 * 3600:
            # print(i - 1, i)
            # print(unit_data.iloc[i]['unit'], unit_data.iloc[i - 1]['unit'])
            # print(str(unit_data.iloc[0]['unit']))
            # unit_data[:i-1].to_csv
            # ('./sample_data/output/' + str(unit_data.iloc[0]['unit']) + '_' + str(trip_count) + '.csv',
            # index=False)
            unit_data[:i - 1][['latitude','longitude','timestamp']].to_csv(
                output_dir + str(unit_data.iloc[0]['unit']) + '_' + str(trip_count) + '.csv',
                index=False)
            trip_count = trip_count + 1
            unit_data = unit_data[i:]
            i = 1

    # unit_data.to_csv('./sample_data/output/' + str(unit_data.iloc[0]['unit']) + '_' + str(trip_count) + '.csv', index=False)
    unit_data[['latitude','longitude','timestamp']].to_csv(output_dir + str(unit_data.iloc[0]['unit']) + '_' + str(trip_count) + '.csv', index=False)
