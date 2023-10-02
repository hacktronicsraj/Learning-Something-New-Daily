import os
import subprocess
from datetime import datetime
 
def lambda_handler(event, context):
    # Replace this with your ntfy.sh URL
    ntfy_url = "http://20.241.xx.xxx/raja"
 
    # Construct the curl command
    curl_command = f"curl -X POST {ntfy_url}"
 
    # Execute the curl command
    try:
        subprocess.run(curl_command, shell=True, check=True)
        return {
            'statusCode': 200,
            'body': 'Curl request sent successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }