import json
import datetime

def count_events_per_hour(file_name: str) -> None:
    with open(file_name, "r") as f:
        content = f.read()
        parsed_content = json.loads(content)

        result = {}
        for entry in parsed_content:
            dt = datetime.datetime.strptime(entry["createdAt"], '%Y-%m-%d %H:%M:%S.%f %Z')
            if (dt.hour in result):
                result[dt.hour] += 1
                continue
            
            result[dt.hour] = 0
        print(result)

count_events_per_hour("visits.json")