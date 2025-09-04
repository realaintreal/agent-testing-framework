from .config import Config
from .results import Results

class Simulation:
    """A simple environment to simulate agent interactions."""
    def __init__(self, agents, config_path=None):
        self.config = Config(config_path)
        self.results = Results(self.config.get('simulation_name'))
        self.agents = agents
        self.time_step = 0

    def run(self):
        """Runs the simulation for a given number of steps."""
        max_steps = self.config.get('max_steps')
        print(f"Starting simulation '{self.config.get('simulation_name')}' for {max_steps} steps.")
        for _ in range(max_steps):
            for agent in self.agents:
                try:
                    observation = {"time": self.time_step}
                    action = agent.decide(observation)
                    self.results.log_event(self.time_step, agent.name, action)
                    agent.execute(action)
                except Exception as e:
                    print(f"Error with agent {agent.name} at step {self.time_step}: {e}")
            self.time_step += 1
        self.results.save_to_file()

