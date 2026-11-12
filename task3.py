
# ==========================================
# Task 3: Second-Highest Distinct Score
# Placement Readiness Tracker
# Roll Number: 2481078
# ==========================================


def find_runner_up(scores):
    """
    Find the second-highest distinct score.
    """

    # Remove duplicate scores
    unique_scores = set(scores)

    # Sort scores in descending order
    sorted_scores = sorted(unique_scores, reverse=True)

    # Return the second-highest score
    return sorted_scores[1]


# Main program
if __name__ == "__main__":

    # Read the number of scores
    n = int(input())

    scores = []

    # Read exactly n scores
    while len(scores) < n:
        values = input().split()

        for value in values:
            if len(scores) < n:
                scores.append(int(value))

    # Find and display the runner-up score
    result = find_runner_up(scores)

    print(result)
