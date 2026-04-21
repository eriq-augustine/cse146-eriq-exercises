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
