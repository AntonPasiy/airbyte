#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_jira_dc_low import SourceJiraDcLow

if __name__ == "__main__":
    source = SourceJiraDcLow()
    launch(source, sys.argv[1:])
