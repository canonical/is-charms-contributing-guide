## Programming Language

If we develop in many different programming languages, the maintenance cost
increases, only those with knowledge of a given programming language can work
on code bases in that programming language and best practices and standards are
difficult to set across the team.

The team encourages exploration and experimentation in a range of programming
languages. For code intended for production, follow the programming language
commonly used in the ecosystem. For example, any charm code should be written
in Python and any contributions to juju should be in Go.

This means we only have a dependency on contributors knowing two programming
languages which reduces to one for those focussed on charm development.

# Non Compliant Code

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
