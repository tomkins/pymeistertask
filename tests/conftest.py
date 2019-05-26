import os

import betamax
import pytest
from betamax_serializers import pretty_json

MEISTERTASK_TOKEN = os.environ.get("MEISTERTASK_TOKEN", "x" * 20)
MEISTERTASK_EMAIL = os.environ.get("MEISTERTASK_EMAIL", "meistertask@example.org")


def pytest_addoption(parser):
    parser.addoption(
        "--record", action="store_true", default=False, help="Record new betamax cassettes"
    )


betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "tests/cassettes"

    if not os.path.isdir(config.cassette_library_dir):
        os.makedirs(config.cassette_library_dir)

    config.default_cassette_options["record_mode"] = "none"

    # Readable JSON output
    config.default_cassette_options["serialize_with"] = "prettyjson"

    # Filter out some settings for secrecy
    config.define_cassette_placeholder("<MEISTERTASK_TOKEN>", MEISTERTASK_TOKEN)
    config.define_cassette_placeholder("<MEISTERTASK_EMAIL>", MEISTERTASK_EMAIL)


@pytest.fixture(scope="class")
def meistertask_settings(request):
    request.cls.meistertask_token = MEISTERTASK_TOKEN
    request.cls.meistertask_email = MEISTERTASK_EMAIL


@pytest.fixture(scope="class")
def betamax_record(request):
    request.cls.record = request.config.getoption("record")
