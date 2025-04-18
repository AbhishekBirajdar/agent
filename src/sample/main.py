#!/usr/bin/env python
import sys
import warnings

from agent_trial.crew import TrailAgentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the crew with basic inputs."""
    inputs = {
        'topic': 'Manchester United Europa League Match'
    }
    TrailAgentCrew().crew().kickoff(inputs=inputs)

def train():
    """Train the crew over several iterations."""
    inputs = {
        "topic": "Manchester United Europa League Match"
    }
    try:
        TrailAgentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred during training: {e}")

def replay():
    """Replay a crew execution starting from a task ID."""
    try:
        TrailAgentCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred during replay: {e}")

def test():
    """Test the crew and return results."""
    inputs = {
        "topic": "Manchester United Europa League Match"
    }
    try:
        TrailAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred during testing: {e}")


# If you want to call from CLI
if __name__ == "__main__":
    run()
