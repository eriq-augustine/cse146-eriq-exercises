import math

def optimize(weights: list[float], variables: list[float], labels: list[float],
        step_size: float,
        iterations: int = 100000,
        ) -> float:
    """
    Optimize the weights to minimize the loss.
    Return the final loss.
    """

    loss = math.inf
    for i in range(iterations):
        # Take an optimization step by updating the weights.
        _take_step(weights, variables, loss, step_size)

        # Recompute the loss.
        loss = _compute_loss(weights, variables, labels)

    return loss

def _take_step(weights: list[float], variables: list[float], loss: float, step_size: float) -> None:
    """ Take a step by updating the weights. """

    ...

def _compute_loss(weights: list[float], variables: list[float], labels: list[float]) -> float:
    """ Take a step by updating the weights. """

    ...
