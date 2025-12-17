"""Functions used in preparing Guido's gorgeous lasagna.

This module provides helper functions to calculate preparation time,
bake time remaining, and total elapsed cooking time for a lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40        # in minutes
PREPARATION_TIME = 2           # in minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
