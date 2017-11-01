from csv import reader

data = {}
header_row = None
total = 0
with open('Toggl_time_entries_2017-10-01_to_2017-10-31.csv', 'r', encoding='utf8') as f:
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
        total += duration

for k, v in data.items():
    print('%s - %s minutes' % (k, v))

print ('-----')
print ('Total hours %s' % (total / 60.0))
