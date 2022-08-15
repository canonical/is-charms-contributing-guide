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

# Non Compliant Code

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
