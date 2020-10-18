import os
import json
import pytest

from moto import mock_s3
from uuid import uuid4


class MockContext(object):
    def __init__(self, function_name):
        self.function_name = function_name
        self.function_version = "v$LATEST"
        self.memory_limit_in_mb = '{{ cookiecutter.memory_limit_lambda }}'
        self.invoked_function_arn = f"arn:aws:lambda:{os.getenv('AWS_REGION_NAME')}:ACCOUNT:function:{self.function_name}"
        self.aws_request_id = str(uuid4)

@pytest.fixture(scope='function')
def aws_credentials():
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_REGION_NAME'] = 'us-east-1'

@pytest.fixture(scope='function')
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name=os.getenv('AWS_REGION_NAME'))

@pytest.fixture
def lambda_context():
    return MockContext("dummy_function")

@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    with open("./events/default_event.json", "r") as fp:
        return json.load(fp)
