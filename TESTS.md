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

## When to Write and What to Cover In Integration Tests

The team creates charms and tooling used and intended to be used directly or as
building blocks for mission critical purposes by both Canonical and external
users. The charms and tools we provide need to meet a high quality bar to ensure
that they work for our users as intended. If we ship charms and tools that don't
meet this high standard, the impact could be widespread.

This standard covers when to write integration tests and also provides guidance
on what should be covered by them.

The intent of integration tests is to check that what we provide to our users
works as advertised. There are two key concepts in that statement:
`what we provide` and `works as advertised`. `what we provide` addresses the
scope of our integration tests which are the features specifically provided by
the charm or tool. The following examples illustrate what this means by
providing guidance on what should and should not be covered by integration
tests.

The following should be covered by integration tests for business critical
charms:

* An action the charm provides
* An integration the charm provides
* A configuration the charm provides
* That the workload is up and running
* The features of a tool

The reason these examples should be covered is because we are accountable for
these features of a charm or tool by being its owner. Charms that are not
business critical may not include integration tests for these examples based on
the value these tests would provide compared to the cost of writing them.

The following does not usually need to be covered by integration tests because
we do not own them:

* A feature provided by the workload which is not enhanced by the charm
* That GitHub works
* That the network works
* That the operating system works
* That Kubernetes works
* That Juju works

To address the second concept of `works as advertised`, when writing an
integration test for business critical charms, it is not sufficient to just
check that, for example, that Juju reports that running the action was
successful. Additional checks need to be executed to ensure that whatever the
action was intended to achieve worked. For charms that are not business
critical, the checks can be more relaxed, such as just checking that juju
reports success for the action that was triggered.

By writing integration tests that cover the features provided by the charm, we
ensure that we are meeting the expectations our users have of us. This will make
the charms and tools we provide reliable and enable our users to use them for
their use cases, including those that are business critical.

