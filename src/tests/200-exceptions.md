# Test Exception Raised

Testing an exception being raised might not be enough as a type of exception
can be raised due to multiple reasons. E.g., a function could raise `ValueError`
for different arguments.

The property of the exception being raised should be asserted against as well.
A common test would be the string representation of the exception. Using the
following `pytest` example:

```Python
def something(a: int, b: bool):
  """Do something."""
  if a >= 5:
    raise ValueError("Argument a must be less than 5")
  if b:
    raise ValueError("Some other error message")
  # Rest of the function...


def test_something():
  """Test the something function."""
  with pytest.raises(ValueError) as err:
      something(a=10, b=False)
  assert "Argument a" in str(err.value)
  assert "less than 5" in str(err.value)
```

In the above example, the `something` function could have thrown a different
`ValueError` related to the argument `b`. Testing the string representation of
the `ValueError` ensures the proper type of error is being tested against.
