import boto3

def lambda_handler(event, context):
    # TODO implement
    
    # eventname, usernamem, region, account number, 
    account = event['account']
    region = event ['region']
    username = event['detail']['userIdentity']['userName']
    eventname = event['detail']['requestParameters']['name']
    state = event['detail']['requestParameters']['state']
    
    
    eventslist = ['test-ctrail-state-change', 'event2', 'event3']
    
    if (state == "DISABLED") and (eventname in eventslist):
        import boto3

        client = boto3.client('sns')
        
        response = client.publish(
            TopicArn='arn:aws:sns:us-east-1:412601977023:rule',
            Message="Cloudwatch Event named %s was disabled by %s in %s region. Account number %s ." % (eventname, username, region, account),
            Subject='Cloudwatch Event:  '+eventname+ ' disabled',
            
        )
        
        
        
    return 'Hello from Lambda'
