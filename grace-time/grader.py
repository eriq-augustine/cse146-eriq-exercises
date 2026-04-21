class Assignment:
    def __init__(self,
            due_at_timestamp: int | None = None,
            ...,
            ) -> None:
        self.due_at_timestamp: int | None = due_at_timestamp
        """ When an assignment is due, or None if there is no due date. """

        ...

    ...

class Submission:
    def __init__(self,
            submission_timestamp: int | None = None,
            ...,
            ) -> None:
        self.submission_timestamp: int | None = submission_timestamp
        """
        When the submission attempt was made,
        or None if there was no time sent with the submission.
        """

        ...

    ...

def is_late(assignment: Assignment, submission: Submission) -> bool:
    # Check if the assignment has a due date.
    # Timestamps are in Unix Time: https://en.wikipedia.org/wiki/Unix_time
    due_timestamp = assignment.due_at_timestamp
    if (due_timestamp is None):
        return False

    # Get the timestamp for the submission.
    submission_timestamp = student_submission.submission_timestamp
    if (submission_timestamp is None):
        return False

    return (submission_timestamp > due_timestamp)
