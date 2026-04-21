import arrow

class Assignment:
    def __init__(self,
            due_at_timestamp: int | None = None,
            grace_time_secs: int | None = None,
            ...,
            ) -> None:
        self.due_at_timestamp: int | None = due_at_timestamp
        """ When an assignment is due, or None if there is no due date. """

        self.grace_time_secs: int | None = grace_time_secs
        """ Do not count a submission late if is only late by at most this number of seconds. """

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

    # Get the timestamp for the submission, or now if there is no timestamp.
    submission_timestamp = student_submission.submission_timestamp
    if (submission_timestamp is None):
        submission_timestamp = int(arrow.now().timestamp())

    grace_time_secs = assignment.grace_time_secs
    if (grace_time_secs is None):
        grace_time_secs = 0

    return (submission_timestamp > (due_timestamp + grace_time_secs))
