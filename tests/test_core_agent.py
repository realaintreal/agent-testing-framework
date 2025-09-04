import unittest
from agents.core import Agent

class TestCoreAgent(unittest.TestCase):

    def test_agent_creation(self):
        agent = Agent(name="test_agent")
        self.assertEqual(agent.name, "test_agent")

    def test_decide_method_not_implemented(self):
        agent = Agent(name="test_agent")
        with self.assertRaises(NotImplementedError):
            agent.decide(None)

if __name__ == '__main__':
    unittest.main()

