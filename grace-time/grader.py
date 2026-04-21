class Assignment:
    ...

    def get_due_at_timestamp(self) -> int | None:
        """
        Get a timestamp (Unix Time (seconds)) for when the assignment is due,
        or None if there is no listed due date.
        """

        ...

class Submission:
    ...

    def get_submission_timestamp(self) -> int | None:
        """
        Get a timestamp (Unix Time (seconds)) for when the assignment submission was made at,
        or None if there is no submission time.
        """

        ...

def is_late(assignment: , submission):
    # Check if the assignment has a due date.
    # Timestamps are in Unix Time: https://en.wikipedia.org/wiki/Unix_time
    due_timestamp = assignment.get_due_at_timestamp()
    if (due_timestamp is None):
        return False

    # Get the timestamp for the submission, or now if there is no timestamp.
    submission_timestamp = student_submission.get_submission_timestamp()
    if (submission_timestamp is None):
        return False

    return (submission_timestamp > due_timestamp)
