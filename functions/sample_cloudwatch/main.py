import time

def handle(event, context):
    unix_epoch_timestamp = int(time.time())
    value = 42
    metric_type = 'count'
    metric_name = 'my.metric.name'
    tags = ['tag1:value', 'tag2']

    print(
        'MONITORING|{0}|{1}|{2}|{3}|#{4}'.format(unix_epoch_timestamp, value, metric_type, metric_name, ','.join(tags)
    ))

