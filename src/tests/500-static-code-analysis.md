# Static Code Analysis

There are many potential problems with code that can be spotted based on
analysing source code without executing it, such as mismatches in type
expectations. Additionally, code formatting discussions during PRs can be
cumbersome and take up a lot of time.

The following automated static code analysis tools should be used locally and
enforced through the CI system:

- [`black`](https://pypi.org/project/black/) for code formatting
  - line length of 99
  - Python target version based on the same is in the
     [Charm Ubuntu and Python Version](#charm-ubuntu-and-python-version)
- [`isort`](https://pypi.org/project/isort/) for import sorting
  - line length of 99
  - `black` profile
- [`flake8`](https://pypi.org/project/flake8/) for pythonic code style
  - refer to
     [indico `pyproject.toml`](https://github.com/canonical/indico-operator/blob/main/pyproject.toml)
  - use the following additional plugins:
    - `flake8-docstrings`
    - `flake8-docstrings-complete`
    - `flake8-test-docs`
    - `flake8-copyright`
    - `flake8-builtins`
    - `pyproject-flake8`
    - `pep8-naming`
     for additional configurations
- [`bandit`](https://pypi.org/project/bandit/) for security checks
- [`codespell`](https://pypi.org/project/codespell/) for spelling problems
- [`woke`](https://snapcraft.io/woke) for inclusive language
- [`prettier`](https://prettier.io) for JSON and YAML formatting
- [`mypy`](https://pypi.org/project/mypy/) for type checks
- [`pylint`](https://pypi.org/project/pylint/) for further python code style
  checks

Note:

- Disabling checks should be the last resort, alternatives such as refactoring
  the code should be considered first. For example, instead of disabling the
  `too-many-arguments` `pylint` rule, consider grouping the arguments, e.g.,
  using a `typing.NamedTuple`.
- When disabling a rule, if the tool allows for it, use the name of the rule
  rather than the code. For example, for `pylint`, always use the name of the
  rule (like `too-many-arguments`) rather than the code. This makes it easier
  for readers to know which rule is being disabled and potentially why.
- If a rule is disabled, a comment should to be included above the line
  disabling the rule explaining why the rule is disabled. This will mean that
  future readers don't have to guess why it was disabled and can also consider
  whether the disable can be removed. For rules tied to import, it may be better
  to comment on each usage rather than on the import. Note that comments for
  import must be added at the start of an import section to prevent the
  formatter from messing up the import sections:

  ```
  # Comment explaining why subprocess is imported.
  import logging
  import os
  import subprocess  # nosec B404
  import time
  ```

- Disabling should be done as specifically as possible. That means, disabling
  the narrowest rule possible on the narrowest section of code. For example,
  instead of disabling a rule entirely, disable it on a file. Instead of
  disabling a rule for a file, disable it for just a line of code. The preferred
  way is to disable on a line of code:

  ```
  <code>  # disable rule
  ```

  If a rule needs to be disabled for a section, re-enable it as soon as
  possible:

  ```
  # disable rule
  <code>
  # enable rule
  ```

This ensures consistency across our projects, catches many potential bugs
before code is deployed and simplifies PRs.
