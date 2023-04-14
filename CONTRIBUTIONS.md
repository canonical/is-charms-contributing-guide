# Standards

- [CI-CD](#ci-cd)
- [Dependencies](#dependencies)
- [Failing Status Checks](#failing-status-checks)
- [Non Compliant Code](#non-compliant-code)
- [PR comments and requests for changes](#pr-comments-and-requests-for-changes)
- [Programming Languages and Frameworks](#programming-languages-and-frameworks)
- [Repository Setup](#repository-setup)
- [Static Code Analysis](#static-code-analysis)
- [When to use Python or Shell](#when-to-use-python-or-shell)

# CI-CD

The team maintains a number of repositories which are generally quite similar.
If each of the repositories maintains its own workflows, it is difficult to
introduce new tools across the repositories owned by the team. Additionally, if
shared workflows are unreliable, the team is unable to consistently merge
changes and have confidence in the CI-CD.

Use [`operator-workflows`](https://github.com/canonical/operator-workflows) for
the CI-CD of any repositories owned by the team. Even if the repository is not a
charm, such as a GitHub action, use it to the extent possible. If a repository
has unique requirements for certain workflows, use the `operator-workflows` as
much as possible. Consider proposing changes to `operator-workflows` instead of
doing something custom in a repository. Also consider whether to make partial
use of workflows in `operator-workflows` and add anything that can't be done
with `operator-workflows` to the individual repository, if the CI-CD
requirements are unique to a repository.

For any changes to `operator-workflows`, add tests just like we expect for any
other repository.

Using shared workflows will make it easy to evolve the workflows used by all our
repositories and roll out new tooling and checks across them. It will also avoid
duplication in many repositories.

Adding tests to `operator-workflows` will ensure stability of the workflows and
provide examples for how to use them.

## Dependencies

Including an external dependency in one of our projects is a significant
choice. It can help with reducing the complexity and development cost. However,
a poor dependency pick can lead to critical issues, such as security incidents
around our software supply chain. Other impacts include:

* We may need to take over maintenance of a project if the current maintainer
  becomes inactive.
* We need to keep monitoring the dependencies for any potential issues, such as
  deprecations of features we use or retirement of the dependency in favour of
  others.
* Updating our code in case of breaking changes.

Dependencies include anything we use that is not directly developed by our
team, such as:

* a python dependency in a `requirements.txt` file,
* a Docker image and
* a GitHub action.

Different levels of scrutiny apply depending on how the dependency is used:

* Development dependency (such as a linter): lowest level of scrutiny as it is
  potentially easier to stop using a linter if any problems arise. Linters also
  generally cannot make changes to our code without the team seeing the change
  in a PR. Increased scrutiny should be applied if a tool becomes important in
  our workflow, such as the testing library we use (e.g., `pytest`).
* Build dependency (such as a GitHub action): medium to high level of scrutiny
  as the output of our build processes are used in highly sensitive
  environments. For example, the Jenkins charm our team develops is used to
  build the Ubuntu images Canonical distributes which run many sensitive and
  critical workloads. Compromising the Jenkins charm build process gives an
  attacker potential access to the build process of the Ubuntu images.
* Production dependency: high level of scrutiny, especially for charms
  operating sensitive workloads. An example is the mattermost charm which runs
  the Canonical internal chat server which holds sensitive data.

The following are helpful indicators in assessing the quality of a dependency:

* How widely adopted the dependency is. For example, `pytest` is widely used
  across the industry and well maintained reducing the chance of, for example,
  the project being abandoned or malicious code making it into a release.
  Indications of adoption can include download counts (https://pypistats.org)
  and interactions on GitHub such as forks and stars.
* How well maintained the dependency is. This indicates whether the dependency
  is under active development or potentially has been abandoned. Indicators of
  maintenance can include recent commits, recent releases and the number of
  recent open and closed pull requests and issues.
* Whether the dependency is maintained by an individual or organisation. If the
  dependency is maintained by an organisation, it is less likely that it will
  stop being maintained as there are likely multiple people looking after the
  dependency.

By carefully selecting dependencies, we can limit security and maintenance
problems arising from our use of dependencies.

## Failing Status Checks

The team uses GitHub actions to run CI which includes automated status checks
to verify the code works as expected. If PRs are merged with failing status
checks, there are potential bugs in the code which may lead to downtime or
other operational issues or a shared tool not working as expected.

PRs can only be merged if all status checks pass. Some exceptions could
include:

* If the team has recently taken over a new charm and changes are urgently
  needed and the test suit of the existing charm is failing for spurious
  reasons.
* A tool we depend on is not working, no previous working version is available
  and a change is urgently needed to fix a critical issue in production.

Even in the above cases it is not clear whether it is reasonable to merge a PR
with failing checks due to the high risks of ignoring failing checks that have
been adopted by the team. Judgement is required in these cases weighing the
risks of introducing bugs with the urgency and impact of the underlying need to
land the change.

Alternatives to merging the PR with failing status checks include:

* Change the code to fix the problem.
* Disable the status check (e.g., mark the test as
  [`xfail`](https://docs.pytest.org/en/7.1.x/how-to/skipping.html)). This
  should not be done lightly as the value the status check provides to the team
  is lost.
* Wait for an upstream fix for the issue.

If it is deemed that a change should land despite a failing status check, the
following artifacts should be added to the PR:

* If the status check can be run in another way, e.g. locally, a copy of the run
  (e.g., a copy of the terminal output) including the git commit SHA which is
  being approved and the status check passing
* The reason why the PR needs to be merged without the status check passing
  (e.g., because the fix is needed in production and the status check is failing
  due to problems with GitHub).

One of the repository admins should then be asked to review the artifacts and
merge the PR after completing the review. The PR should be otherwise ready to be
merged (e.g., has been approved).

Resolving the underlying reason the status check is failing should be high
priority so that the team can rely on the automation again.

This will ensure that we minimise the number of bugs in our code and tooling.

## Non Compliant Code

Standards and best practices evolve over time which means that code already
written may not comply with a new standard. If this is wide spread, it can lead
to a culture of ignoring the standard and can degreade the value of team
standards.

At a minimum, any code changed in a pull request complies with team standards.
The team values initiative updating code to comply with new standards and
recognises that this needs to be balanced with other priorities, such as
delivering new features of fixing bugs. If possible, standards should be
enforced automatically by the CI system.

This ensures that:

1. code under active development is likely to be compliant with team standards,
2. less time is spent updating code that doesn't need to be updated frequently
   to new standards,
3. it encourages the team to go out of their way to implement any new standards
   as individuals see value in doing so and
4. compliance is enforced using CI where possible.

## PR comments and requests for changes

The team uses Github for reviewing changes in the codebase and integrating them
within our projects. A reviewer can comment and give feedback that potentially
leads to new changes in the submitted code. Github allows you to `request
changes` on a PR, meaning it cannot be merged until the changes are accepted. As
the team is distributed, requesting changes as a default slows down merges and
requires the reviewer to approve again. Even with sufficient approvals, a PR
cannot be merged unless the requestor accepts the changes, which might be
trivial.

Our team favors commenting in the usual case and resorting to requesting changes
only if there is something problematic. It is adviseable to comment and let the
engineer take action rather than request changes and block the PR. The preferred
way is to comment instead.  Note that committing new changes will reset
approvals either way and approvals need to be collected again, which is the
expected behavior and part of our workflow. Please note we expect the engineer
that raised the PR to deal with the comments in good faith, i.e., not just mark
them as resolved when they are not really resolved for the purpose of being able
to merge the PR. The engineer that raised the PR is responsible for closing the
comments once they are tackled.

With commenting rather than requesting changes, an engineer gives feedback and
still allows the team (based on approvals) to decide the way forward - a change
might make it in a different PR or the change might not be desireable in the
end. The best approach is having as much feedback from as many engineers as
possible to be able to reach a sound decision.

## Programming Languages and Frameworks

If we develop in many different programming languages and frameworks, the
maintenance cost increases, only those with knowledge of a given programming
language or framework can work on code bases in that programming language and
best practices and standards are difficult to set across the team.

We are a team primarily focused on developing charms, and we should follow the
recommended tools and best practices of the ecosystem we work within (and help
to improve them where appropriate). As a result, the primary programming
language we work in is Python, and the primary framework we use to develop
charms with is the [Operator
Framework](https://github.com/canonical/operator).

We will also be working on older charms which may be written in older
frameworks such as the [Reactive
Framework](https://charmsreactive.readthedocs.io/en/latest/). In some cases
we'll work on converting those to the Operator Framework but for small bug
fixes or changes this may not be the case.

As a team we'll also be exposed to a much lesser extent to other programming
languages as a result of working with specific applications that we deploy on
Juju, or via small changes to Juju itself, which is written in Go. We also
encourage exploration and experimentation in a range of programming languages
depending on the interest of the individual as part of using Canonical's
annual training budget.

## Repository Setup

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
- Approvals reset on any new commits.
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

## Static Code Analysis

There are many potential problems with code that can be spotted based on
analysing source code without executing it, such as mismatches in type
expectations. Additionally, code formatting discussions during PRs can be
cumbersome and take up a lot of time.

The following automated static code analysis tools should be used locally and
enforced through the CI system:

- [`black`](https://pypi.org/project/black/) for code formatting
   - line length of 99
   - Python target version based on the same is in the
     [Charm Ubuntu and Python Version](#charm-ubuntu-and-python-version)
- [`isort`](https://pypi.org/project/isort/) for import sorting
  - line length of 99
  - `black` profile
- [`flake8`](https://pypi.org/project/flake8/) for pythonic code style
   - refer to
     [indico `pyproject.toml`](https://github.com/canonical/indico-operator/blob/main/pyproject.toml)
   - use the following additional plugins:
     - `flake8-docstrings`
     - `flake8-docstrings-complete`
     - `flake8-test-docs`
     - `flake8-copyright`
     - `flake8-builtins`
     - `pyproject-flake8`
     - `pep8-naming`
     for additional configurations
- [`bandit`](https://pypi.org/project/bandit/) for security checks
- [`codespell`](https://pypi.org/project/codespell/) for spelling problems
- [`woke`](https://snapcraft.io/woke) for inclusive language
- [`prettier`](https://prettier.io) for JSON and YAML formatting
- [`mypy`](https://pypi.org/project/mypy/) for type checks
- [`pylint`](https://pypi.org/project/pylint/) for further python code style
  checks

Note:
* Disabling checks should be the last resort, alternatives such as refactoring
  the code should be considered first. For example, instead of disabling the
  `too-many-arguments` `pylint` rule, consider grouping the arguments, e.g.,
  using a `typing.NamedTuple`.
* When disabling a rule, if the tool allows for it, use the name of the rule
  rather than the code. For example, for `pylint`, always use the name of the
  rule (like `too-many-arguments`) rather than the code. This makes it easier
  for readers to know which rule is being disabled and potentially why.
* If a rule is disabled, a comment should to be included above the line
  disabling the rule explaining why the rule is disabled. This will mean that
  future readers don't have to guess why it was disabled and can also consider
  whether the disable can be removed.
* Disabling should be done as specifically as possible. That means, disabling
  the narrowest rule possible on the narrowest section of code. For example,
  instead of disabling a rule entirely, disable it on a file. Instead of
  disabling a rule for a file, disable it for just a line of code. The preferred
  way is to disable on a line of code:

  ```
  <code>  # disable rule
  ```

  If a rule needs to be disabled for a section, re-enable it as soon as
  possible:

  ```
  # disable rule
  <code>
  # enable rule
  ```

This ensures consistency across our projects, catches many potential bugs
before code is deployed and simplifies PRs.

## When to use Python or Shell

Shell scripts are powerful and easy to write. However, they can be challenging
to maintain as they can be difficult to read, have limited tools for testing
and are not easy to re-use through simple import statements. Charms run
production workloads, some of which are business critical, and it is important
to ensure that the code is bug free which requires extensive testing.

Limit the use of shell scripts and commands as much as possible in favour of
writing Python for charm code. This means that there needs to be a good reason
to use a shell command rather than Python. Examples include:

* Extracting data from a machine or container which can't be obtained through
  Python
* Issuing commands to applications that do not have Python bindings (e.g.,
  starting a process on a machine)

Note that, outside of charm source and test code, it is reasonable to use shell
scripts to, for example:

* Configure CI/CD
* Build docker images
* Utilities to support development

This will improve the maintainability of our charms, enable re-use and enable
the team to take advantage of the powerful tooling available through Python.

Note it is possible to run shell commands within python.
[See this section.](PYTHON.md#subprocess-calls-within-python)