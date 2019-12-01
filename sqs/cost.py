from datetime import datetime

import boto3

sqs = boto3.resource('sqs')
s3  = boto3.resource('s3')
ec2 = boto3.client('ec2')

response = ec2.describe_spot_instance_requests()
print('Instances EC2')
print(response)

prices=ec2.describe_spot_price_history(InstanceTypes=['m3.medium'],MaxResults=1,
                                      ProductDescriptions=['Linux/UNIX (Amazon VPC)'])
print (prices['SpotPriceHistory'][0])