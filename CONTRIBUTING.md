## Programming Languages and Frameworks

If we develop in many different programming languages and frameworks, the
maintenance cost increases, only those with knowledge of a given programming
language or framework can work on code bases in that programming language and
best practices and standards are difficult to set across the team.

We are a team primarily focused on developing charms, and we should follow the
recommended tools and best practices of the ecosystem we work within (and help
to improve them where appropriate). As a result, the primary programming
language we work in is Python, and the primary framework we use to develop
charms with is the [Operator
Framework](https://github.com/canonical/operator).

We will also be working on older charms which may be written in older
frameworks such as the [Reactive
Framework](https://charmsreactive.readthedocs.io/en/latest/). In some cases
we'll work on converting those to the Operator Framework but for small bug
fixes or changes this may not be the case.

As a team we'll also be exposed to a much lesser extent to other programming
languages as a result of working with specific applications that we deploy on
Juju, or via small changes to Juju itself, which is written in Go. We also
encourage exploration and experimentation in a range of programming languages
depending on the interest of the individual as part of using Canonical's
annual training budget.

## Charm Ubuntu and Python Version

Using inconsitent minor Python version for development, CI and production means
that, even if tests pass during development and CI, the charm may not work in
production.

When charms are running in production, the version of Python available to them
is dictated by the version of Ubuntu that it is running on. This is configured
in the `charmcraft.yaml` file under the `bases.build-on` and `bases.run-on`
keys. The CI should be configured to use the same version of Ubuntu as
configured under the `charmcraft.yaml` `bases.run-on` key. It is recommended
that local development be done on the version of Python that is shipped with
the Ubuntu version defined in `charmcraft.yaml` `bases.run-on`. The unit and
integration tests should be run on the same minor Python version as is shipped
with the the OS as configured under the `charmcraft.yaml` `bases.run-on` key.
With tox, for Ubuntu 22.04, this can be done using:

```
[testenv]
basepython = python3.10
```

This ensures that the tests are run on the same Python version as the charm
will be running in production, catching any issues related to mismatched Python
versions.

## Repository Setup

The repositories that store the source code for our charms are critical to the
ongoing development of our charms. They also enforce team policies around code
review and ensure business continuity. If the repository is setup poorly, it
exposes our team and Canonical to operational risks.

- GitHub should be used for charm source code and issue tracking.
- The repository should be publicly accessible.
- The `is-charms` team is added as maintainers.
- Management and director of the team that owns the charm are added as admins
  on the repository.
- Branches are auto-deleted after merging.
- The only option for merging PRs is using a squash commit.
- The default branch is called `main`.
- The default branch is protected and can only be changed using PRs.
- The number of approvers for PRs is 2.
- Approvals reset on any new commits.
- PRs can only be merged if all checks pass.
- Bypassing of the rules is disabled.

The above configuration ensures our team processes around changes are enforced
and provdes access to the repository even if some team members are unavailable.

The repository will contain a `CODEOWNERS` file in its root to automatically add 
the `is-charms` team as reviewer
```
*       @canonical/is-charms
```

## Test Structure

Tests that are difficult to understand are of lower value because if they fail
it is difficult to understand why they fail.

The docstring of a test has 3 sections, *arrange*, *act* and *assert*. Arrange
explains the pre-conditions required for the test, act explains what steps the
test performs and assert explains what the state must be after all actions are
complete. The test code is separated into blocks for each section. For example:

```Python
def test_something():
    """
    arrange: given 2 numbers
    act: when they are added
    assert: the result must be the sum of the 2 numbers.
    """
    num_a = 1
    num_b = 2

    result = num_a + num_b

    assert result == 3
```

Whilst this standard is usually valuable, there are cases where it imposes
unreasonable constraints. An example is complex functional tests that check
multiple interactions that require individual arrange, act, assert blocks
because they, for example, build on each other. In those cases, apply judgement
keeping in mind the option of breaking up the test into multiple tests.

This structure makes it easy to understand what is required before test
execution, how the test works and what it checks for in the end.

## Test Coverage

Unit tests check whether the intended functionality has been implemented. This
is valuable to reduce bugs and checking whether any changes to the code break
any features. The benefits of testing are roughly proportional to the test
coverage percentage, the lower the coverage the higher the chances of bugs and
the higher the risk of code changes.

The team has a coverage percentage which is the maximum of 85% and the current
percentage on the default branch, usually `main`. Any code that is already
covered on the default branch should not cease to be covered by new commits to
main, such as through a pull request. Any coverage exclusion should have an
explanatory comment, such as:

```Python
# Exclude from coverage since unit tests should not run as __main__
if __name__ == "__main__":  # pragma: no cover
   ...
```

To enforce this, the `pyproject.toml` file should include the following
configuration:

```toml
[tool.coverage.report]
fail_under = <maximum of coverage % on main and 85%>
```

This value should be updated in each PR to reflect any increase in coverage
compared to the main branch as a result of the PR.

This ensures a high coverage minimum and no coverage regression.

## f-strings

The `str.format` based syntax is difficult to read because, to figure out what
the final string looks like, the format parameters have to be checked against
their position in the string which adds additional mental overhead to reading
the code. String concatenation with + is also difficult read read.

f-strings are the preferred way of including variables in a string. For
example:

```Python
foo = "substring"
# .format is not preferred
bar = "string {}".format(foo)
# string concatenation is not preferred
bar = "string " + foo
# f-strings are preferred
bar = f"string {foo}"
```

f-strings are much easier to read because the variable is placed at the
location it appears in the final string.

## Formatting Log Messages

Log messages often need to include the value of variables, such as exceptions
or configuration. Usually f-strings are the preferred way of formatting
strings. However, due to logging features, using f-strings or `str.format` is a
security risk (see [issue46200](https://bugs.python.org/issue46200)) and also
causes the string formatting to be done even if the log level for the message
is disabled.

Use the string formatting provided by logging:

```Python
foo = "substring"
# Security risk
logging.debug(f"string {foo}")
# Safe
logging.debug("string %s", foo)
```

Whilst this is less readable, it prevents security issues and avoids
unnecessary evaluation of the string formatting. Even if the formatting input
is trusted, the logging provided formatting should be used because the input
may become untrusted due to a code change in the future.

## Docstrings

Functions without a well formatted description can be difficult to understand
and maintain, especially if the function is longer than just a few lines.

Each module, function and class should have a docstring. The Google standard on
docstring applies:
[docstring guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

Exemptions:

1. Test functions
2. Test fixtures

This makes the code easier to understand and maintain.

## Non Compliant Code

Standards and best practices evolve over time which means that code already
written may not comply with a new standard. If this is wide spread, it can lead
to a culture of ignoring the standard and can degreade the value of team
standards.

At a minimum, any code changed in a pull request complies with team standards.
The team values initiative updating code to comply with new standards and
recognises that this needs to be balanced with other priorities, such as
delivering new features of fixing bugs. If possible, standards should be
enforced automatically by the CI system.

This ensures that:

1. code under active development is likely to be compliant with team standards,
2. less time is spent updating code that doesn't need to be updated frequently
   to new standards,
3. it encourages the team to go out of their way to implement any new standards
   as individuals see value in doing so and
4. compliance is enforced using CI where possible.
