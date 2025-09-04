# AgentSim Tutorial

This tutorial will guide you through creating a simple simulation.

First, define your agent:

```python
from agents.core import Agent

class MyAgent(Agent):
    def decide(self, observation):
        return "do_nothing"
```

Then, create a simulation and run it:

```python
from agents.environments import Simulation

agent = MyAgent("my_agent")
sim = Simulation(agents=[agent])
sim.run()
```

