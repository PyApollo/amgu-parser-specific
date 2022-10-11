import requests
import constants

def get_schedule(group_id='1588'):
    response = requests.get(constants.URL.format(group_id)).json()
    group_name = response['group_name']
    schedule = response['timetable_tamplate_lines']
    schedule = [l for l in schedule if l.get('discipline_str')]
    schedule = sorted(schedule, key=lambda x : list(x.values())[1])
    schedule_dict = {
    x : [[j.get(k) if j.get(k) else 'Неизвестно' for k in constants.INFO[1:]] for j in schedule if j.get('weekday') == x] for x in range(1,8)
    }
    return group_name, schedule_dict