from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points = 5000):
        """Initializes attributes of random walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Generates a step for each point in the walk."""
        direction = choice([1, -1])
        distance = choice([num for num in range(5)])
        return direction * distance

    def fill_walk(self):
        """Calculate all points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Gets a new step for each iteration.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)