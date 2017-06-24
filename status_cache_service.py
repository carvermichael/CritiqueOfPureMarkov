import json
from status_creator import create_status


def get_status():
    statuses = get_cache()
    return_status = statuses.pop(0)

    put_cache(statuses)

    if len(statuses) < 10:
        refresh_status_cache()

    return return_status


def get_cache():
    with open('statuses.json', 'r') as file:
        statuses = json.load(file)['statuses']

    return statuses


def put_cache(statuses):
    json_load = {'statuses': statuses}

    with open('statuses.json', 'w') as file:
        json.dump(json_load, file)


def refresh_status_cache():
    statuses = get_cache()

    while len(statuses) < 100:
        statuses.append(create_status(3))

    put_cache(statuses)
