# File Encoding

If file encoding is not specified when interacting with a file, the default
value for the operating sytem is used. The default varies across operating
systems reducing the portability of code that does not specify a encoding
explicitly. See: <https://peps.python.org/pep-0597/>

For any file operations, specify the `utf-8` encoding where possible. For
example:

```python
with open(..., encoding="utf-8") as file:
    ...

from pathlib import Path

Path(...).read_text(encoding="utf-8")
Path(...).write_text(..., encoding="utf-8")
```

This ensures that the code we write is portable across operating systems.
