import json
import sys
import os

import pandas as pd

input_dir = sys.argv[1]
output_dir = sys.argv[2]
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

file_list = os.listdir(input_dir)

unit_list=[]
trip_list=[]
toll_loc_id_start_list=[]
toll_loc_id_end_list=[]
toll_loc_name_start_list=[]
toll_loc_name_end_list=[]
toll_system_type_list=[]
entry_time_list=[]
exit_time_list=[]
tag_cost_list=[]
cash_cost_list=[]
license_plate_cost_list=[]

df = pd.DataFrame()

for file in file_list:
    json_filename = os.path.join(input_dir, file)
    # print(json_filename)
    f = open(json_filename, "r")
    data =json.load(f)
    #print(data['status'])
    if data['status'] == 'OK':
        if data['route']['hasTolls']:

            for toll in data['route']['tolls']:
                if toll['type'] != 'barrier':
                    unit = file[:4]
                    unit_list.append(unit)

                    trip_id = file[:6]
                    trip_list.append(trip_id)
                    # print(toll)
                    toll_loc_id_start = toll.get('start').get('id')
                    # print(toll_loc_id_start)
                    toll_loc_id_start_list.append(toll_loc_id_start)

                    toll_loc_id_end = toll.get('end').get('id')
                    # print(toll_loc_id_end)
                    toll_loc_id_end_list.append(toll_loc_id_end)

                    toll_loc_name_start = toll.get('start').get('name')
                    # print(toll_loc_name_start)
                    toll_loc_name_start_list.append(toll_loc_name_start)

                    toll_loc_name_end = toll.get('end').get('name')
                    # print(toll_loc_name_end)
                    toll_loc_name_end_list.append(toll_loc_name_end)

                    toll_system_type = toll.get('type')
                    # print(toll_system_type)
                    toll_system_type_list.append(toll_system_type)

                    entry_time = toll.get('start').get('arrival').get('time')
                    # print(entry_time)
                    entry_time_list.append(entry_time)

                    exit_time = toll.get('end').get('arrival').get('time')
                    # print(exit_time)
                    exit_time_list.append(exit_time)

                    tag_cost = toll.get('tagCost')
                    # print(tag_cost)
                    tag_cost_list.append(tag_cost)

                    cash_cost = toll.get('cashCost')
                    # print(cash_cost)
                    cash_cost_list.append(cash_cost)

                    license_plate_cost = toll.get('licensePlateCost')
                    # print(license_plate_cost)
                    license_plate_cost_list.append(license_plate_cost)

df['unit'] = unit_list
df['trip_id'] = trip_list
df['toll_loc_id_start'] = toll_loc_id_start_list
df['toll_loc_id_end'] = toll_loc_id_end_list
df['toll_loc_name_start '] = toll_loc_name_start_list
df['toll_loc_name_end'] = toll_loc_name_end_list
df['toll_system_type'] = toll_system_type_list
df['entry_time'] = entry_time_list
df['exit_time'] = exit_time_list
df['tag_cost'] = tag_cost_list
df['cash_cost'] = cash_cost_list
df['license_plate_cost'] = license_plate_cost_list
df.sort_values(by=['unit', 'trip_id'], inplace=True)
df.to_csv(os.path.join(output_dir, 'transformed_data.csv'), index=False)

