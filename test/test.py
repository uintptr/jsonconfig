#!/usr/bin/env python3

import os
import sys
import tempfile

from jsonconfig import JSONConfig


def main() -> int:

    status = 1

    try:

        with tempfile.TemporaryDirectory(prefix="json_test_") as td:

            config_file = os.path.join(td, "config.json")

            conf = JSONConfig(config_file)

            v = conf.get_int("/path/to/bleh", 10)

            assert v == 10, "doesn't exist"

            conf.set("/path/to/bleh", 1234)

            v = conf.get_int("/path/to/bleh")

            assert v == 1234, "expected"

            try:
                v = conf.get_str("/path/to/bleh")
                assert False, "shouldn't get here"
            except ValueError:
                pass  # expected

            conf.set("/path/to/bleh", "Hello, World!")

            v = conf.get_str("/path/to/bleh")

            assert v == "Hello, World!", "expected"

        status = 0
    except KeyboardInterrupt:
        pass

    return status


if __name__ == '__main__':

    status = main()

    if 0 != status:
        sys.exit(status)
