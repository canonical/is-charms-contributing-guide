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
