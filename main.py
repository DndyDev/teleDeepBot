import telebot
from deeppavlov import build_model
from deeppavlov.core.common.file import read_json

bot = telebot.TeleBot('token')
model_config = read_json('squad_ru_bert_infer.json')
model = build_model(model_config, download=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, я бот команды игровой студии DandyGames !"
                                      "Ты можешь задать любой вопрос о компании ")


# ToDo: Перевести сообщения в нижний регистр
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, model_training(message.text))


def model_training(request):
    model_answers = model(
        ['DandyGames это студия празработки игр основанная в 2021 году, идея основания появилась в 2019 году.'
         'Студия аннонсировала 2 проекта LabOfFate и GameOfGods, '
         'ведущий геймдизайнер студии какое-то время работал над проектом Virsen.'
         'Студия находится по адресу ул. Пушкина дом Колотушкина. '
         'Телефон для связи 8-800-352-11-12 '],
        [request])

    accuracy = model_answers[2][0]
    answer = model_answers[0][0]

    if (int(accuracy) < 1500):
        answer = "Я не знаю"
    return (answer)


bot.polling()
