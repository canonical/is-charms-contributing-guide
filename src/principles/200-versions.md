# Charm Ubuntu and Python Version

Using inconsistent minor Python version for development, CI and production means
that, even if tests pass during development and CI, the charm may not work in
production.

When charms are running in production, the version of Python available to them
is dictated by the version of Ubuntu that it is running on. This is configured
in the `charmcraft.yaml` file under the `bases.build-on` and `bases.run-on`
keys. The CI should be configured to use the same version of Ubuntu as
configured under the `charmcraft.yaml` `bases.run-on` key. It is recommended
that local development be done on the version of Python that is shipped with
the Ubuntu version defined in `charmcraft.yaml` `bases.run-on`. The unit and
integration tests should be run on the same minor Python version as is shipped
with the the OS as configured under the `charmcraft.yaml` `bases.run-on` key.
With tox, for Ubuntu 22.04, this can be done using:

```
[testenv]
basepython = python3.10
```

This ensures that the tests are run on the same Python version as the charm
will be running in production, catching any issues related to mismatched Python
versions.
