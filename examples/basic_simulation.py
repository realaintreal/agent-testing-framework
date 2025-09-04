from agents.core import Agent
from agents.environments import Simulation

class SimpleAgent(Agent):
    def decide(self, observation):
        print(f"Agent {self.name} is observing time {observation['time']}")
        return "idle"

agent1 = SimpleAgent("Agent 1")
agent2 = SimpleAgent("Agent 2")

sim = Simulation(agents=[agent1, agent2])

print("Running basic simulation...")
sim.run(steps=3)
print("Simulation complete.")

