# Import the libraries from Mycroft.
from mycroft.skills.core import MycroftSkill
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger

#################################################

# Add the author and enable logging.
__author__ = 'kadams1463'

LOGGER = getLogger(__name__)

#################################################

# Create the FlipCoinSkill class.
class FlipCoinSkill(MycroftSkill):

    def __init__(self):
        super(FlipCoinSkill, self).__init__(name="FlipCoinSkill")

    # Create flip_intent using the flip.voc file.
    def initialize(self):
        flip_intent = IntentBuilder("FlipIntent").require("flip").build()
        # Intent callback.
        self.register_intent(flip_intent, self.handle_flip_intent)

    # Create the dialog from the results.dialog file for Mycroft to speak.
    def handle_flip_intent(self, message):
        self.speak_dialog("results")

    def stop(self):
        pass

def create_skill():
    return FlipCoinSkill()