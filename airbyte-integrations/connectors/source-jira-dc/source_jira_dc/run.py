#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#

import sys
import json
from airbyte_cdk.entrypoint import launch
from .source import SourceJiraDc


def run():

    #'''
    config_path = "secrets/config.json"
    catalog_path = "secrets/configured_catalog.json"
    sys.argv = [sys.argv[0], "read", "--config", config_path, "--catalog", catalog_path]
    #'''

    source = SourceJiraDc()
    launch(source, sys.argv[1:])
