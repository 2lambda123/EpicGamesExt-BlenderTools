import boto3
import urllib
import sys
import time
import requests
import json


class LogFile:
    def __init__(self, contents):
        self.contents = contents

    def read(self, amount=None):
        if not amount:
            return ''.encode('utf-8')

        return self.contents.encode('utf-8')


class S3Logger:
    def __init__(self, bucket_name, sha):
        self.client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.sha = sha
        self.public_web_address = f'https://{bucket_name}.s3.amazonaws.com'

    def write_log(self, log_contents):
        log_file = LogFile(log_contents)
        self.client.upload_fileobj(
            Fileobj=log_file,
            Bucket=self.bucket_name,
            Key=self.sha,
            ExtraArgs={'ACL': 'public-read'}
        )

    def read_log(self):
        try:
            file = urllib.request.urlopen(f'{self.public_web_address}/{self.sha}')
            return file.read().decode("utf-8")
        except:
            return ''

    def delete_log(self):
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=self.sha,
        )


def get_commit_state(repo, token, sha):
    headers = {f'Authorization': f'token {token}'}
    response = requests.get(
        headers=headers,
        url=f'https://api.github.com/repos/{repo}/commits/{sha}/status'
    )
    return json.loads(response.text)['state'].lower()


def get_flags():
    args = sys.argv[1:]
    flags = {}
    for index, arg in enumerate(args):
        if '--' in arg:
            try:
                flags[arg] = args[index+1]
            except IndexError:
                raise ValueError(f'The flag {arg} needs a value!')
    return flags


if __name__ == '__main__':
    arguments = get_flags()

    repo_name = 'james-baber/BlenderTools'
    sha = arguments.get('--sha')
    token = arguments.get('--token')

    s3_logger = S3Logger(bucket_name='blender-tools-logs', sha=sha)

    if arguments.get('--listen') == 'True':
        print('Ping')
        print(s3_logger.read_log())

    if arguments.get('--report') == 'True':

        while get_commit_state(repo_name, token, sha) == 'pending':
            time.sleep(3)
            logs_file = open('/tmp/unittest_results.log')
            s3_logger.write_log(logs_file.read())
            logs_file.close()

    if arguments.get('--delete') == 'True':
        s3_logger.delete_log()



