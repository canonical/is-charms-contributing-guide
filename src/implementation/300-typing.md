# Type Hints

Python is a dynamic programming language that does not require type
declarations. Without type information, arguments might be passed to functions
that are not of the expected type (e.g., passing `None` where it is not
expected), which leads to more bugs. It also makes it more difficult to know
what functions accept as input and return as output.

Except when impractical, declare type hints on function parameters, return
values and class and instance variables. Examples of when type hints might
be impractical (not an exhaustive list):

- dictionaries with many nested dictionaries,
- decorator functions,
- when making small changes or
- contributions to projects not owned by the team.

To leverage the power of type hints, the following configuration snippet should
be added to `pyproject.toml`. This helps the user during the linting process by
ensuring that all functions, including tests, have type definitions and checks
for any typing issues even if a function does not have explicit type hints on
it.

```toml
[tool.mypy]
check_untyped_defs = true
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

The type hints should be checked with `mypy`. More information on
type hints can be found here: [PEP 484](https://peps.python.org/pep-0484/).

This will help users know what functions expect as parameters and return and
catches more bugs earlier.

# Handling Typing Issues with python-libjuju

In tests and elsewhere when interacting with `python-libjuju`, it is a frequent
requirement to check whether certain attributes are `None`. Doing this in many
tests reduces the readability of the code.

Instead of putting `assert ops_test.model` in individual tests, write a fixture:

```Python
@pytest_asyncio.fixture(scope="module", name="model")
async def model_fixture(ops_test: pytest_operator.plugin.OpsTest) -> ops.model.Model:
    """The current test model."""
    assert ops_test.model
    return ops_test.model
```

Instead of putting `assert hasattr(app, "units")`, write a fixture:

```Python
@pytest_asyncio.fixture(scope="function", name="units")
async def units_fixture(app: ops.model.Application) -> list[ops.model.Unit]:
    """The current test unit."""
    assert hasattr(app, "units")
    return app.units
```

This reduces code duplication which increases the readability of the tests.
