import json
import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('ses', region_name='ap-south-1')
    ec2_client = boto3.client('ec2', region_name='ap-south-1')

    # Specify the tag key and value to filter instances
    tag_key = 'Environment'
    tag_value = 'Production'

    email_body = f"Sample Summary Email:\n\n"
    email_body += f"Good Evening,\n\n"
    email_body += f"Here is a list of Resources running on your account as on {datetime.datetime.now()}:\n\n"

    # Extract EC2 instance tags based on the specified tag key and value
    response = ec2_client.describe_instances(Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ami_id = instance['ImageId']
            instance_type = instance['InstanceType']
            region = instance['Placement']['AvailabilityZone'][:-1]
            subnet_id = instance['SubnetId']
            security_groups = [sg['GroupName'] for sg in instance['SecurityGroups']]
            key_name = instance.get('KeyName', 'N/A')

            tags = instance.get('Tags', [])
            tag_string = ", ".join([f"{tag['Key']}: {tag['Value']}" for tag in tags])

            email_body += f"Instance ID: {instance_id}\n"
            email_body += f"AMI ID: {ami_id}\n"
            email_body += f"Instance Type: {instance_type}\n"
            email_body += f"Region: {region}\n"
            email_body += f"Subnet ID: {subnet_id}\n"
            email_body += f"Security Groups: {', '.join(security_groups)}\n"
            email_body += f"Keypair: {key_name}\n"
            email_body += f"Tags: {tag_string}\n\n"

    # Adding line breaks and additional content
    email_body += "\n\nThank You,\nKind Regards!\nTeam AWS"

    response = client.send_email(
        Destination={
            'ToAddresses': ['akshaykhanna7798@gmail.com']
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': email_body,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Sample Summary Email',
                },
            },
        Source='ick.june8@gmail.com'
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
