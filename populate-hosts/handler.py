from boto3 import client
from aws_lambda_powertools import Logger

logger = Logger('populate-hosts')

def main(event, context):
    
    logger.info(event)

    ssm_client = client('ssm')
    ec2_client = client('ec2')

    response = ec2_client.describe_instances(Filters=[
        {
            'Name': 'tag:application',
            'Values': [
                'fairground',
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ])

    instance_ids = [ instance['InstanceId'] for instance in response['Reservations'][0]['Instances'] ]
    
    ssm_client.send_command(InstanceIds=instance_ids,
                            DocumentName='AWS-RunShellScript',
                            Parameters={'commands': ['python3 /root/populate_hosts.py']})
                            