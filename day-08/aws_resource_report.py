import boto3
import json

class AWSCON:

    def __init__(self):
        print("Init Load\n")

    def show_s3_buckets(self):
        s3 = boto3.client('s3')
        buckets_res = s3.list_buckets()
        buckets_list = []
        for bucket in buckets_res['Buckets']:
            buckets_list.append(bucket['Name'])
        return buckets_list
        

    def show_ec2(self):
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        ec2_list = []
        for r in response["Reservations"]:
            for t in r["Instances"]:
                for v in t["Tags"]:
                    ec2_list.append(v['Value'])
        return ec2_list
        

    def save_to_file(self,data):
        with open('aws_report.json','w+') as f:
            json.dump(data,f, indent=4, default=str)


if __name__ == "__main__":
    service = AWSCON()

    ec2_list=service.show_ec2()
    s3_list=service.show_s3_buckets()
    final_data = {
        "ec2": ec2_list,
        "s3": s3_list
    }
    print(final_data)
    if final_data:
        input = input("\nDo you want to store data in file? [y/n]: ")

        if input == "y":
            service.save_to_file(final_data)
            print("\nData stored in file !!\n")
        else:
            exit