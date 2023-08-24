import boto3
from datetime import datetime

def lambda_handler(event, context):
    currentTime = datetime.now()
    print("Time at which Lambda invoked:" + str(currentTime))

    ec2_client = boto3.client('ec2', region_name='ap-south-1')
    filters = [
        {'Name': 'tag:test', 'Values': ['yes']}
    ]
    instances = ec2_client.describe_instances(Filters=filters)

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2_client.start_instances(InstanceIds=[instance_id])
            print(f"Started EC2 Instance: {instance_id}")
