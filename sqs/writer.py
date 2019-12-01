import boto3
import uuid

# Get the service resource
sqs = boto3.resource('sqs')
# Get the queue
queue = sqs.get_queue_by_name(QueueName='queue-test-2')

# Create a new message
for x in range(2):
    body = 'Bienvenidos a Open Cloud Colombia - {}'.format(uuid.uuid1())
    response = queue.send_message(MessageBody=body)
    print(body)
    print(response)