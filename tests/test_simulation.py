import unittest
from agents.core import Agent
from agents.environments import Simulation

class TestSimulation(unittest.TestCase):

    def test_simulation_run(self):
        class TestAgent(Agent):
            def decide(self, observation):
                return "wait"

        agent = TestAgent("test_agent")
        sim = Simulation(agents=[agent])
        sim.run(steps=5)
        self.assertEqual(sim.time_step, 5)

if __name__ == '__main__':
    unittest.main()

