from deeppavlov.core.common.file import read_json
from deeppavlov import build_model

if __name__ == '__main__':
    ic_model_config = read_json('intent_cacher.json')
    model = build_model(ic_model_config)
    intent = model(["I want to know more about GameOfGods"])[0]

    print(intent)
    if intent == 'tell_me_more':
        print("I don't want to tell")