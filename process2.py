import json
import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()

input_dir = sys.argv[1]
output_dir = sys.argv[2]
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
# print(input_dir)
# print(output_dir)
file_list = os.listdir(input_dir)
# print(file_list)
url = os.environ.get('TOLLGURU_API_URL')
key = os.environ.get('TOLLGURU_API_KEY')
#print(url)
#print(key)

headers = {'x-api-key': key, 'Content-Type': 'text/csv'}
for input_file in file_list:
    file = input_dir + input_file
    with open(file, 'rb') as file:
        response = requests.post(url, data=file, headers=headers)
        output_file = output_dir + input_file[:-4] + ".json"
        json_data = json.loads(response.text)
        json.dump(json_data, open(output_file, 'w'))
        #print(response.text)
