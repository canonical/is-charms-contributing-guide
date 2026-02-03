# Downloading Binaries

Downloading binaries is only permitted from what are classed as trusted sources.
These are:

* The Ubuntu Archives (for debian packages)
* Snaps
  [owned by the "canonical" account](https://snapcraft.io/publisher/canonical)
* Snaps where the binary is built from a trusted and approved source.
* [PyPi](https://pypi.org/)

These sources are considered trusted because we are confident that we understand
the way in which they're built, and the security commitments for packages/snaps
produced by them. At any point we can rerun our builds and know that we will
pull in the latest versions of these artefacts, and that in the case of the
first two they will include security updates that Canonical stands behind.

Downloading binaries from any other sources and including them in our charms or
ROCKs exposes our end users to potential security issues either now or in the
future. We don't know the manner in which the binaries were built and don't have
confidence that they will be updated in the future in case of security
vulnerabilities that affect them.

As such, we should ensure that we’re only downloading from either the trusted
sources above, or we're downloading the source instead, verifying that download
where possible, and then building that code from source on infrastructure we
trust (e.g. Launchpad builders or GitHub self-hosted runners).

Any exception to this should be specifically noted/documented and approved by IS
Charms managers.
