from datetime import datetime

import boto3

sqs = boto3.resource('sqs')
s3  = boto3.resource('s3')
ec2 = boto3.client('ec2')

response = ec2.describe_spot_instance_requests()
print('Instances EC2')
print(response)

queue = sqs.get_queue_by_name(QueueName='queue-test-2')

#print(queue)
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

for message in queue.receive_messages():
    # Print out the body
    print('Message: {0}'.format(message.body))
    # delete message
    message.delete()

