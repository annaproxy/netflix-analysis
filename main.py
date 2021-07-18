import csv
from datetime import timedelta, datetime


class Entry:
    def __init__(self, line):
        self.user = line[0]
        # 2020-07-22 19:34:38
        self.date_start = datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
        duration = line[2].split(":")
        self.duration = timedelta(
            hours=int(duration[0]), minutes=int(duration[1]), seconds=int(duration[2])
        )
        self.duration_in_seconds = self.duration.total_seconds()
        self.date_end = self.date_start + self.duration
        self.autoplayed = len(line[3]) > 0
        self.title = line[4] if len(line[4]) > 0 else line[5]
        self.device_type = line[6]


class Entries:
    def __init__(self, filename):
        self.entry_list = []
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i > 0:
                    entry = Entry(row)
                    self.entry_list.append(entry)
        self.df = pd.DataFrame(
            {
                "user": [e.user for e in self.entry_list],
                "start": [e.date_start for e in self.entry_list],
                "duration": [e.duration for e in self.entry_list],
                "duration_in_seconds": [e.duration_in_seconds for e in self.entry_list],
                "end": [e.date_end for e in self.entry_list],
                "title": [e.title for e in self.entry_list],
                "device_type": [e.device_type for e in self.entry_list],
            }
        )
