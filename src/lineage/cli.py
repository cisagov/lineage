"""lineage is a tool to update GitHub repositories from upstream sources.

Search GitHub for repositories to update based on their configured upstream
lineage.

Usage:
    lineage [--exclude-non-public] [--show-non-public] --access-token=TOKEN --actor=ACTOR --repo-query=QUERY --working-directory=DIRECTORY

Options:
    -h --help                      Show this message.
    -v --version                   Show the version.
    --access-token=TOKEN           The GitHub access token to use.
    --actor=ACTOR                  The name to use for the commits created when
                                   updating repositories.
    --exclude-non-public           Exclude non-public (`private` and `internal`)
                                   repositories from updating.
    --repo-query=QUERY             The query used to find repositories to check for
                                   updates.
    --show-non-public              Do not mask the names of non-public (`private` and
                                   `internal`) repositories in the logs.
    --working-directory=DIRECTORY  The directory to change to before checking
                                   repositories.
"""

# Standard Python Libraries
import os.path
import sys
from typing import Any

# Third-Party Libraries
import docopt
from schema import And, Schema, SchemaError

from . import entrypoint
from ._version import __version__


def main() -> None:
    """Parse and verify command line arguments before calling the main entrypoint."""
    args: dict[str, bool | str] = docopt.docopt(__doc__, version=__version__)

    schema: Schema = Schema(
        {
            "--access-token": And(
                str,
                lambda s: len(s) == 40,
                error="Provided token does not match the expected format.",
            ),
            "--actor": And(
                str,
                lambda s: len(s) > 0,
                error="The actor value must be a non-empty string.",
            ),
            "--repo-query": And(
                str,
            ),
            "--working-directory": And(
                str,
                lambda d: os.path.exists(d),
                error="The target working directory must exist.",
            ),
            str: object,  # Don't care about other keys, if any
        }
    )

    try:
        validated_args: dict[str, Any] = schema.validate(args)
    except SchemaError as err:
        # Exit because one or more arguments were invalid
        print(err, file=sys.stderr)
        sys.exit(1)

    entrypoint.update_repos(
        validated_args["--access-token"],
        validated_args["--actor"],
        validated_args["--working-directory"],
        validated_args["--repo-query"],
        not validated_args["--exclude-non-public"],
        not validated_args["--show-non-public"],
    )
