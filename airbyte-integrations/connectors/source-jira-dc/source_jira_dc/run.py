#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceJiraDc


def run():
    source = SourceJiraDc()
    launch(source, sys.argv[1:])
