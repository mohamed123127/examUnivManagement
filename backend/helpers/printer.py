import json
from datetime import datetime, date, time, timedelta


def jsonPrint(data, itemsNumber=None, indent=4):
    if isinstance(data, list) and itemsNumber is not None:
        data_to_print = data[:itemsNumber]
    else:
        data_to_print = data

    print(json.dumps(data_to_print, indent=indent, ensure_ascii=False))

def Print(data, limit=None):
    def convert(obj):
        if isinstance(obj, date):
            return obj.strftime("%A,%Y-%m-%d")
        elif isinstance(obj, time):
            return obj.strftime("%H:%M")
        return obj

    if isinstance(data, list):
        to_print = data[:limit] if limit else data
        formatted = [ {k: convert(v) for k, v in item.items()} for item in to_print ]
    elif isinstance(data, dict):
        formatted = {k: convert(v) for k, v in data.items()}
    else:
        formatted = data

    print(json.dumps(formatted, indent=4, ensure_ascii=False))
