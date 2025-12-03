# lineage #

[![GitHub Build Status](https://github.com/cisagov/lineage/workflows/build/badge.svg)](https://github.com/cisagov/lineage/actions)
[![License](https://img.shields.io/github/license/cisagov/lineage)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/lineage/workflows/CodeQL/badge.svg)](https://github.com/cisagov/lineage/actions/workflows/codeql-analysis.yml)
[![Coverage Status](https://coveralls.io/repos/github/cisagov/lineage/badge.svg?branch=develop)](https://coveralls.io/github/cisagov/lineage?branch=develop)
[![Code Style](https://img.shields.io/badge/Code%20Style-black-black)](https://github.com/psf/black)

A GitHub Action to automatically generate PR requests from upstream repositories
regardless of the fork network.

## Repository Lineage configuration ##

Lineage is configured using `.github/lineage.yml` in a repository.  Each
upstream repository is listed in the `lineage` section.

| Key | Description | Required |
|-----|-------------|:--------:|
| local-branch | The branch that will receive new changes. | No |
| remote-url   | The `https` URL of the upstream repository. | Yes |
| remote-branch | The branch in the upstream repository. | No |

Below is an example configuration that defines two upstream repositories. The
`skeleton` repository specifies both the source and destination branches, while
the `extra-sauce` repository uses the default branches for both repositories.

```yml
---
version: "1"

lineage:
  skeleton:
    local-branch: develop
    remote-url: https://github.com/cisagov/skeleton-generic.git
    remote-branch: develop
  extra-sauce:
    remote-url: https://github.com/felddy/extra-skel-sauce.git
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
