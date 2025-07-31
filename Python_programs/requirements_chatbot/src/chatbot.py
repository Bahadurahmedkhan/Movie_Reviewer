import questionary
from typing import Dict, List
import yaml
from jinja2 import Template
import os

class RequirementsChatbot:
    def __init__(self):
        self.template_path = os.path.join(os.path.dirname(__file__), 'templates', 'story_template.yaml')
        with open(self.template_path, 'r') as f:
            self.template = Template(f.read())

    def start_conversation(self) -> Dict:
        """Start the conversation flow to gather requirements."""
        print("\n🤖 Welcome! Let's create a user story together.\n")
        
        # Gather basic story information
        title = questionary.text(
            "What's a good title for this user story?",
            validate=lambda text: len(text) > 0
        ).ask()

        as_a = questionary.text(
            "Who is the user? (As a...)",
            validate=lambda text: len(text) > 0
        ).ask()

        i_want = questionary.text(
            "What do they want to do? (I want to...)",
            validate=lambda text: len(text) > 0
        ).ask()

        so_that = questionary.text(
            "What's the benefit? (So that...)",
            validate=lambda text: len(text) > 0
        ).ask()

        # Gather acceptance criteria
        acceptance_criteria = []
        while True:
            criterion = questionary.text(
                "\nAdd an acceptance criterion (or press Enter to finish):"
            ).ask()
            
            if not criterion:
                if len(acceptance_criteria) >= 2:
                    break
                print("Please add at least 2 acceptance criteria.")
                continue
            
            acceptance_criteria.append(criterion)

        # Generate the story using the template
        story_data = {
            'title': title,
            'as_a': as_a,
            'i_want': i_want,
            'so_that': so_that,
            'acceptance_criteria': acceptance_criteria
        }

        return self.generate_story(story_data)

    def generate_story(self, story_data: Dict) -> Dict:
        """Generate a formatted user story using the template."""
        yaml_content = self.template.render(**story_data)
        return yaml.safe_load(yaml_content)

    def save_story(self, story: Dict, filename: str):
        """Save the story to a YAML file."""
        with open(filename, 'w') as f:
            yaml.dump(story, f, default_flow_style=False, sort_keys=False) 