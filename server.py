import random

from flask import Flask, json

api = Flask(__name__)


class ToneGenerator():
    def __init__(self):
        self.tone_set = ['humorous', 'ironic', 'cynical']

    def generate_tone(self):
        index = random.randint(0, len(self.tone_set)-1)
        return self.tone_set[index]


@api.route('/tone', methods=['GET'])
def get_tone():
    generator = ToneGenerator()
    tone = generator.generate_tone()
    return json.dumps({"tone": tone})


if __name__ == '__main__':
    api.run()
