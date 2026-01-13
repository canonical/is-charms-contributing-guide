# Repository Setup

The repositories that store the source code for our charms are critical to the
ongoing development of our charms. They also enforce team policies around code
review and ensure business continuity. If the repository is setup poorly, it
exposes our team and Canonical to operational risks.

- GitHub should be used for charm source code and issue tracking.
- The repository should be publicly accessible.
- The `is-charms` team is added as maintainers.
- Management and director of the team that owns the charm are added as admins
  on the repository.
- Branches are auto-deleted after merging.
- The only option for merging PRs is using a squash commit.
- The default branch is called `main`.
- The default branch is protected and can only be changed using PRs.
- The number of approvers for PRs is 2.
- Approvals are not dismissed on new commits.
- PRs can only be merged if all checks pass.
- Bypassing of the rules is disabled.
- Commits must be signed.
- [Automated secret scanning](https://docs.github.com/en/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories#enabling-secret-scanning-alerts-for-users)
  must be enabled.

The above configuration ensures our team processes around changes are enforced
and provides access to the repository even if some team members are unavailable.

The repository will contain a `CODEOWNERS` file in its root to automatically add
the `is-charms` team as reviewer

```
*       @canonical/is-charms
```
