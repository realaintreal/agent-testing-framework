class Agent:
    """Base class for all agents in the simulation."""
    def __init__(self, name):
        self.name = name

    def decide(self, observation):
        """The core decision-making logic for the agent."""
        raise NotImplementedError("All agents must implement the 'decide' method.")

    def execute(self, action):
        """Executes the chosen action."""
        print(f"[{self.name}] executes: {action}")
        return f"executed {action}"

