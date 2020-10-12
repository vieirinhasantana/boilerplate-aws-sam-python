import os
import json
import pytest
from uuid import uuid4

os.environ['POWERTOOLS_TRACE_DISABLED'] = '1'
os.environ['POWERTOOLS_METRICS_NAMESPACE'] = 'MyServerlessApplication'


class MockContext(object):

    def __init__(self, function_name):
        self.function_name = function_name
        self.function_version = "v$LATEST"
        self.memory_limit_in_mb = 512
        self.invoked_function_arn = f"arn:aws:lambda:us-east-1:ACCOUNT:function:{self.function_name}"
        self.aws_request_id = str(uuid4)


@pytest.fixture
def lambda_context():
    return MockContext("dummy_function")


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    with open("./events/default_event.json", "r") as fp:
        return json.load(fp)
