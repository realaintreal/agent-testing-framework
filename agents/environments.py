class Simulation:
    """A simple environment to simulate agent interactions."""
    def __init__(self, agents):
        self.agents = agents
        self.time_step = 0

    def run(self, steps=10):
        """Runs the simulation for a given number of steps."""
        for _ in range(steps):
            for agent in self.agents:
                observation = {"time": self.time_step}
                action = agent.decide(observation)
                agent.execute(action)
            self.time_step += 1

