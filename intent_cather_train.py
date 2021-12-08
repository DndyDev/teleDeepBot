import json
from deeppavlov import configs, train_model

if __name__ == '__main__':
    train_data = json.load(open("intent_catcher_data/train.json"))
    test_data = json.load(open("intent_catcher_data/test.json"))
    valid_data = json.load(open("intent_catcher_data/valid.json"))

    del train_data['opinion_request']
    del test_data['opinion_request']
    del valid_data['opinion_request']

    # train_data['exit']

    train_data['complement'] = [
        "((you're)|(you are)|(you)) (such ){,1}((a wonderful)|(an amazing)|(a marvellous)|"
        "(a magnificent)|(a great)|(a glorious)|(a lovely)|(a terrific)|(a delightful)"
        "|(a fantastic)|(an incredible)|(a tremendous)|(a gorgeous)|(an awesome))( person){,1}\!{,1}"
    ]
    json.dump(train_data, open("intent_catcher_data/train.json", 'w'))
    json.dump(test_data, open("intent_catcher_data/test.json", 'w'))
    json.dump(valid_data, open("intent_catcher_data/valid.json", "w"))

config = json.load(open(configs['intent_catcher']['intent_catcher']))
