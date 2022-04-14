from dataclasses import dataclass
from random import choice


@dataclass
class Command:
    name: str
    help: str
    headings: list=None


def get_random_heading(command: Command):
    return choice(command.headings)

FACT = Command("fact", "Returns interesting facts about science, literature, philosophy and other cool topics.")
FACT.headings = [
    "Did you know?", "Fun fact!", "I bet you didn't know this", "Some people don't know this, but",
    "You might find this interesting", "How about this?", "Is this what you were looking for?",
    "I've got one for you", "I almost forgot about this one", "I feel like everyone should know this"
]
