"""Tests standard tap features using the built-in SDK tests library."""

import json
from singer_sdk.testing import get_tap_test_class

from tap_gong.tap import TapGong

with open('.secrets/config.json') as f:
    SAMPLE_CONFIG = json.load(f)
    print(SAMPLE_CONFIG)

# Run standard built-in tap tests from the SDK:
TestTap = get_tap_test_class(
    tap_class=TapGong,
    config=SAMPLE_CONFIG
)