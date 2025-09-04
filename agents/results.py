import json

class Results:
    """Handles the results of a simulation run."""
    def __init__(self, simulation_name):
        self.simulation_name = simulation_name
        self.events = []

    def log_event(self, timestamp, agent_name, action):
        """Logs an event that occurred during the simulation."""
        self.events.append({
            'timestamp': timestamp,
            'agent': agent_name,
            'action': action
        })

    def save_to_file(self, path=None):
        """Saves the simulation results to a JSON file."""
        if not path:
            path = f"{self.simulation_name}_results.json"
        with open(path, 'w') as f:
            json.dump(self.events, f, indent=4)
        print(f"Results saved to {path}")

