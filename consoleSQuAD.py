from deeppavlov import build_model, configs
from deeppavlov.core.common.file import read_json

model_config = read_json('squad_ru_bert_infer.json')

model = build_model(model_config,download=True)
model_answers =  model(['DandyGames это студия празработки игр основанная в 2021 году, идея основания появилась в 2019 году.'
                        'Студия аннонсировала 2 проекта LabOfFate и GameOfGods, '
                        'ведущий геймдизайнер студии какое-то время работал над проектом Virsen'
                        'Студия находится по адресу ул. Пушкина дом Колотушкина. '
                        'Телефон для связи 8-800-352-11-12 '],
                       ['кто такой денди'])

accuracy = model_answers[2][0]

# if (accuracy > 1500):
#     print(model_answers)
# else:
#     print("I dont now")

print(model_answers)