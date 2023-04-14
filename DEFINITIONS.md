## Definitions

### Tool

A tool is a project the team works on which isn't a charm, such as a GitHub
action.

### Unit Tests

These are tests that cover charm/ service functions to ensure that given a
specific context and mocked interfaces, the function returns the expected
output. Tests could cover more than one function if some of them don't include
business logic. These tests shouldn't be functional, they just ensure that the
code is doing what it's supposed to do. A test that requires too many mocks
indicates the design needs to be improved to reduce coupling.

### Integration Tests

Integration tests ensure that the charm integrated with its dependencies will
behave properly. It doesn't test the code in a production like environment,
meaning that we don't connect to environments with equivalent resources and
production like datasets. The integration tests will spawn specific dependencies
that could differ from the production one (e.g using localstack instead of
openstack, sqlite instead of a production grade database, ...). These tests can
be functional (they ensure that the features provided by the charm are working
as intended) or focus on checking an abstracted interface. They don't
necessarily need to ensure that the API/Service/CLI they're interacting with are
working as intended.

### End To End Tests

These are simulated user scenarios running on an environment as close as
possible to production. They ususally run on a staging environment with
preexisting data, and interact with the charm as a user would (ideally using the
juju cli). These are functional tests and ensure that the charm is working as
intended in the condition close to production in order to detect issues related
to this environment (ressources, pre-existing condition, migrations, ...).

### Smoke Tests

These are functional tests for business critical use cases used to ensure that
the most critical features are still working after a production deployment. The
aim is to ensure that a deployment didn't impact business continuity and detect
potential defects immediately after a production release.

### Business Critical Charm

This charm is critical to the operations of Canonical or our customers. Any
bugs, security issues or other problems will have a wide impact to important
business processes.