import requests
from yaml import parse
import database
import formatter
import parser
import time
import random


# url = 'https://cabinet.amursu.ru/public_api/groups'

# r = requests.get(url)

# id_name = {
#     x.get('id') : x.get('name') for x in r.json()['groups']
# }

# # print(id_name)

db = database.Database()
formatter = formatter.Formatter()

for i in list(['1588','1478']):

    schedule = parser.get_schedule(str(i))
    formatted = formatter.format_week(list(schedule[1].values()))
    db.update(str(i),formatted)
    print(f"{i} - successfully updated")
    sleep_time = random.randint(0,10)
    time.sleep(sleep_time)