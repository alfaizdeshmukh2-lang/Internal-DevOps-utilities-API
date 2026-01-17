# import boto3
# from datetime import datetime

# def get_bucket_info():
#           s3_client  = boto3.client("s3")
          
#           buckets = s3_client.list_buckets()["Buckets"]

#           current_datetime = datetime.now()
#           old_buckets =[]
#           new_buckets = []
#           for bucket in buckets:
#                   bucket_name = buckets ["Name"]
#                   new_buckets.append (bucket_name )

#           return {
#                   "new_buckets":new_buckets
#           }


########################

import boto3
from datetime import datetime, timezone , timedelta 

def get_bucket_info():
    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()
    buckets = response["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    print (current_date )
    new_buckets = []
    old_buckets = []

    for bucket in buckets:
        bucket_name = bucket["Name"]    
        creation_date= bucket ["CreationDate"] 
        days_ago_90 = current_date - timedelta(days = 90)
        if creation_date < days_ago_90:
            old_buckets.apppend(bucket_name)
        else :
            new_buckets.append(bucket_name)

    return {
        "total_bucket ": len(buckets),
        "new_bucket" : len(new_buckets),
        "old_buckets ": len (old_buckets),
        "new_buckets_names": new_buckets,
        "old_buckets_names": old_buckets
    }





