# Unit Tests

These are tests that cover charm/ service functions to ensure that given a
specific context and mocked interfaces, the function returns the expected
output. Tests could cover more than one function if some of them don't include
business logic. These tests shouldn't be functional, they just ensure that the
code is doing what it's supposed to do. A test that requires too many mocks
indicates the design needs to be improved to reduce coupling.
