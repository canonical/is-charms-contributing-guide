# End To End Tests

These are simulated user scenarios running on an environment as close as
possible to production. They ususally run on a staging environment with
preexisting data, and interact with the charm as a user would (ideally using the
juju cli). These are functional tests and ensure that the charm is working as
intended in the condition close to production in order to detect issues related
to this environment (ressources, pre-existing condition, migrations, ...).
