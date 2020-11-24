import random
from nltk import edit_distance
from bot_config import BOT_CONFIG


def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- ']
    text = ''.join(text)
    return text


def get_intent(question):
    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            filtered_example = filter_text(example)
            dist = edit_distance(filtered_example, filter_text(question))   # Levenshtein distance
            if dist / len(filtered_example) < 0.4:
                return intent


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases)


def generate_answer_by_text(question):
    # TODO
    return None


def get_failure_phrases():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)


def bot(question):
    # NLU
    intent = get_intent(question)

    # Getting answer

    # Looking for completed answer
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer

    # Generating a match by context response
    answer = generate_answer_by_text(question)
    if answer:
        return answer

    # Using plugs
    answer = get_failure_phrases()

    return answer


if __name__ == '__main__':
    text = None
    while text not in ['exit', 'Выход']:
        text = input()
        result = bot(text)
        print(result)
