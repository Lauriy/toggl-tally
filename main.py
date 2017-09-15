from csv import reader

data = {}
header_row = None
with open('Toggl_time_entries_2017-08-01_to_2017-08-31.csv', 'r') as f:
    for row in reader(f, delimiter=','):
        if not header_row:
            header_row = row
            continue
        row = dict(zip(header_row, row))
        duration = row.get('Duration')
        duration_parts = duration.split(':')
        duration = int(duration_parts[0]) * 60 + int(duration_parts[1]) + int(float(duration_parts[2]) / 60.0)
        description = row.get('Description')
        if description in data:
            data[description] += duration
        else:
            data[description] = duration

for k, v in data.items():
    print('%s - %s minutes' % (k, v))
