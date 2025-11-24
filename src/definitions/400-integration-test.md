# Integration Tests

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
