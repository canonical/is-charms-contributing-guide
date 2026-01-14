# Static Code Analysis

There are many potential problems with code that can be spotted based on
analysing source code without executing it, such as mismatches in type
expectations. Additionally, code formatting discussions during PRs can be
cumbersome and take up a lot of time.

The automated static code analysis tools that should be used locally and
enforced through the CI system are listed in the [`lint`](https://github.com/canonical/platform-engineering-charm-template/blob/main/tox.toml#L44)
section and the [`static`](https://github.com/canonical/platform-engineering-charm-template/blob/main/tox.toml#L107) section of our charm template.

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

  ```python
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

  ```python
  <code>  # disable rule
  ```

  If a rule needs to be disabled for a section, re-enable it as soon as
  possible:

  ```python
  # disable rule
  <code>
  # enable rule
  ```

This ensures consistency across our projects, catches many potential bugs
before code is deployed and simplifies PRs.
