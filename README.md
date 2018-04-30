# BoomCloud

AWS automation using BOTO3 and troposphere API. Its is currently in progress. But when it's done, one will be able to create multiple stacks in AWS using BoomCloud.

# Prerequisites
1. An AWS account with access_key and secret_access_key.
2. Python 3
3. boto3 for python
4. troposphere for python
5. Follow the following commands to setup your aws credentials.
   1. Create .aws dir in you home directory
      * `$ cd`
      * `$ mkdir .aws`
      * `$ cd .aws`
   2. Copy paste the following and set you credentials in the credentials file.
      * `$ vi credentials`
      ```   
         [default]
         aws_access_key_id="your_aws_access_key_id"
         aws_secret_access_key="aws_secret_access_key" '''
 
 # Getting Started
 1. Clone this repository
 2. Go to the root of the repo.
 3. Export the python path for this repo
    * `$ export PYTHONPATH=./`
 4. Run the following command to create you first stack on **AWS**
    * `$ python ./bin/boomcloud.py --stack=vpc --opearation=create`
 5. Go and checkout you cloud formation console on your AWS dashboard.
 
 # Running Tests
 run `$ py.test ./tests/*` from root of your repo. 
