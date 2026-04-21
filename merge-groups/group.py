class ProjectGroup:
    def __init__(self, name: str, members: list[Student] | None = None) -> None:
        self.name: str = name

        if (members is None):
            members = []

        self.member: list[Student] = members

    def add(self, student: Student) -> ProjectGroup:
        """ Add the student to this group (if they are not already in it). """

        ...

    def remove(self, student: Student) -> ProjectGroup:
        """ Remove the student from this group (if they are already in it). """

        ...

    def merge(self, other: ProjectGroup) -> ProjectGroup:
        """ Add all the members from the other group to this group. """

        # If the other group is not valid, use this group.
        if ((other is None) or (len(other.members) == 0)):
            return self

        # If this group is not valid, use the other group.
        if ((self is None) or (len(self.members) == 0)):
            return other

        self.members = list(set(self.members + other.members))

        return self
