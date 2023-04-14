# Standards

- [Test Coverage](#test-coverage)
- [Test Fixture](#test-fixture)
- [Test Structure](#test-structure)
- [When to Write and What to Cover In Integration Tests](#when-to-write-and-what-to-cover-in-integration-tests)

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

# Test Fixture

When declaring fixture functions and requesting them in the same Python module, 
there is a risk of accidentally using the fixture function declared in the 
global scope instead of requesting it in the test case function parameters.

To prevent this problem, it is recommended to add a "fixture" prefix or suffix 
to the fixture function name and use the `name` argument in the `pytest.fixture`
decorator to name the fixture.

Here's an example of using the `name` argument in `pytest.fixture`:

```python
import pytest

@pytest.fixture(name="app")
def app_fixture():
    return "app"

def test_my_fixture(app):
    assert app == "app"
```

## Test Structure

Tests that are difficult to understand are of lower value because if they fail
it is difficult to understand why they fail.

The docstring of a test has 3 sections, *arrange*, *act* and *assert*. Arrange
explains the pre-conditions required for the test, act explains what steps the
test performs and assert explains what the state must be after all actions are
complete. If the description for a section is longer than one line, any
additional lines are indented by the default indentation of the file. The test
code is separated into blocks for each section. For example:

```Python
def test_something():
    """
    arrange: given 2 numbers
    act: when they are added
    assert: the result must be the sum of the 2 numbers. If a description spans
        multiple lines, lines after the first should be indented by the default
        spacing of the file to indicate that the description continues.
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

## When to use Python or Shell

Shell scripts are powerful and easy to write. However, they can be challenging
to maintain as they can be difficult to read, have limited tools for testing
and are not easy to re-use through simple import statements. Charms run
production workloads, some of which are business critical, and it is important
to ensure that the code is bug free which requires extensive testing.

Limit the use of shell scripts and commands as much as possible in favour of
writing Python for charm code. This means that there needs to be a good reason
to use a shell command rather than Python. Examples include:

* Extracting data from a machine or container which can't be obtained through
  Python
* Issuing commands to applications that do not have Python bindings (e.g.,
  starting a process on a machine)

Note that, outside of charm source and test code, it is reasonable to use shell
scripts to, for example:

* Configure CI/CD
* Build docker images
* Utilities to support development

This will improve the maintainability of our charms, enable re-use and enable
the team to take advantage of the powerful tooling available through Python.

Note it is possible to run shell commands within python.
[See this section.](PYTHON.md#subprocess-calls-within-python)
