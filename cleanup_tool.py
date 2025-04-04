import boto3

# Find stopped EC2 servers
def find_stopped_ec2():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[
        {'Name': 'instance-state-name', 'Values': ['stopped']}
    ])
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['InstanceId'])
    return instances

# Delete EC2 servers
def delete_ec2(instances):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=instances)
    print("Deleted:", instances)

# Show menu
def menu():
    print("Welcome to AWS Cleanup Tool")
    print("1. Show stopped EC2 servers")
    print("2. Delete stopped EC2 servers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        servers = find_stopped_ec2()
        print("Stopped EC2 instances:", servers)
    elif choice == '2':
        servers = find_stopped_ec2()
        print("Deleting:", servers)
        delete_ec2(servers)
    elif choice == '3':
        print("Goodbye")
        exit()
    else:
        print("Invalid choice")

while True:
    menu()

