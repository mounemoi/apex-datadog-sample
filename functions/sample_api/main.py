import os
import time
import datadog

def handle(event, context):
    now = time.time()
    value = 42
    metric_type = 'count'
    metric_name = 'sample.api.value'
    tags = ['tag1:value', 'tag2']

    options = {
        'api_key': os.environ['DD_API_KEY'],
        'app_key': os.environ['DD_APP_KEY'],
    }
    datadog.initialize(**options)
    datadog.api.Metric.send(metric=metric_name, points=(now, value), host="example.com", tags=tags)

