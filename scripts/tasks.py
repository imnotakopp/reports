import csv
from datetime import datetime
import calendar


def get_tasks():
    now = datetime.now()
    meta = ['sec', 'min', 'hour', 'day', 'month', 'year']

    with open("C:\\git_hub\\reports\\assets\\data.tsv", 'r') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        for line in reader:
            parts = line['frequency'].split(" ")
            if len(parts) != len(meta):
                raise SyntaxError('frequency: {} in correctly defined. '
                                  'Expected {} arguments but found {}'.format(line['frequency'], len(meta), len(parts)))
            parts = [x.split(',') for x in parts]
            config = dict(zip(meta, parts))

            if config['sec'][0] != '*' and now.second not in config['sec']:
                print(config['sec'])
                print('sec didn\'t match')
                continue
            elif config['min'][0] != '*' and now.minute not in config['min']:
                print('min didn\'t match')
                continue
            elif config['hour'][0] != '*' and now.minute not in config['hour']:
                print('hour didn\'t match')
                continue
            elif config['day'][0] != '*' and now.minute not in config['day'] and \
                    calendar.day_abbr[now.weekday()].upper() not in config['day']:
                print('day didn\'t match')
                continue
            elif config['month'][0] != '*' and now.minute not in config['month']:
                print('month didn\'t match')
                continue
            elif config['year'][0] != '*' and now.minute not in config['year']:
                print('year didn\'t match')
                continue

            print("task should be added to the queue")
            add_task_to_queue(line['report_id'])


def add_task_to_queue(report_id):
    with open("C:\\git_hub\\reports\\assets\\queue.tsv", 'a+') as tsvFile:
        writer = csv.writer(tsvFile, delimiter='\t')
        writer.writerow([report_id, datetime.now().isoformat()])


if __name__ == "__main__":
    get_tasks()
    add_task_to_queue(10)
