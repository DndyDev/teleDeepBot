import json
from deeppavlov import configs, train_model,build_model

if __name__ == '__main__':
    config = json.load(open("intent_cacher.json"))
    model = train_model(config, download=False)
    print("Model done")
