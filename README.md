# AgentSim Framework

A lightweight, extensible framework for testing autonomous agent interactions and decision-making processes.

## Overview

AgentSim provides a simple environment to simulate agent behavior and verify outcomes. It is designed for rapid prototyping and testing of agent logic.

## Features

*   **Core Agent Class:** A simple base class for creating new agents.
*   **Test Harness:** Basic test structures for asserting agent behavior.
*   **Extensible:** Easily add new agents and test scenarios.

## Getting Started

To get started, simply define your agent by inheriting from the `Agent` class and create a test case to simulate its environment.

```python
from agents.core import Agent

class MyAgent(Agent):
    def decide(self, observation):
        if "danger" in observation:
            return "flee"
        return "continue"

```

