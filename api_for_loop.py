import requests
import json
import time
from datetime import datetime, timedelta

# The search term we want to get from scrapping
searchTerm = ["diaper","hair clippers","razor","moisturizers","lip stick","digital camera",
              "laptop","TV","conditioners","laundry detergent","plastic wrap","toilet paper",
              "trash bags","vitamins","bath towel","air mattresses","pillow","chef's pans","mixers",
              "vacuum cleaner","running shoes","yoga mat"]

for iterator in range(0, 365):
    for x in searchTerm:
        todayTime = datetime.now().strftime("%Y-%b-%d-%H")
        params = {
            'api_key': '....',
            'type': 'search',
            'amazon_domain': 'amazon.com',
            'search_term': x,
            'output': 'json'
        }
        api_result = requests.get('https://api.rainforestapi.com/request', params)
        jsonStr = json.dumps(api_result.json(), indent=4)
        local_file = todayTime + "_" + x + ".json"
        with open(local_file, "w") as outfile:
            outfile.write(jsonStr)
    print("waiting 6 hours for next run")
    time.sleep(6*60*60) # sleep for 6 hours



