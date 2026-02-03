# Function and Method Ordering

Without a logical order, it can be difficult to follow modules and classes as
the number of functions or methods on them grow increasing the maintenance
burden of the code.

Functions should be ordered according to the
["step-down"](https://dzone.com/articles/the-stepdown-rule) rule.
This means that a module should be readable from top to bottom,
with functions ordered by level of abstraction, from general to specific.
A calling function should always be above the called function.
Functions should also be grouped together logically. If functions have a
similar purpose, they should be grouped together.

On classes, the `__init__` method should come first followed by any other
factory methods, such as `from_charm`. The rest of the methods on a class should
be ordered similar to the guidance for function ordering on modules.

This will make it easier for readers to understand the code reducing the
maintenance cost.
