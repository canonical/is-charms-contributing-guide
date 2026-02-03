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
