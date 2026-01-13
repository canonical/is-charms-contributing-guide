# Failing Status Checks

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
