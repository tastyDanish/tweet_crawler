import json
import boto3

access_key = 'sdfsdf'
secret_key = 'asdfasdfasdf'

def tweets_processor(event, context):
    tweet = event['data']
    print(tweet)

    # Found a tweet of interest, push the record to SNS for mobile notification
    client = boto3.client('sns',
                          region_name='us-west-2',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key)

    response = client.publish(TargetArn='', Message=json.dumps({'default': json.dumps(tweet)}),MessageStructure='json')
