# TODO's in source code

Engineers tend to add TODO comments in the source code for different purposes,
e.g.:

- To remind themselves to do something before merging a PR.
- To acknowledge that the current state of the code needs improvement, but it
depends on  something external (e.g., a feature not being ready yet).
- To indicate that refactoring is necessary, but the cost is too high
- (e.g., development efforts or the PR becoming too large).

In general, comments tend to be inaccurate because code changes faster than
comments are updated. The same applies to TODOs.
They tend to stick around forever and confuse future engineers,
who don't know what the TODO is about or if they should take action.
Therefore, TODOs should preferably be added to the product backlog
(e.g., Jira).
It is acceptable to add TODOs while developing a feature on a feature branch,
but they should be removed before merging the PR.
