import telebot
from deeppavlov import build_model
from deeppavlov.core.common.file import read_json
from datetime import datetime

bot = telebot.TeleBot('token')

qa_model_config = read_json('squad_ru_bert_infer.json')
ic_model_config = read_json('intent_cacher.json')

qa_model = build_model(qa_model_config, download=True)


# Todo: Make property file

hello_message_RU = 'Привет, это бот студии разработки игр DandyGames ! ' \
                   'Ты можешь задать любой вопрос о компании'
hello_message_EN = r'Hello, I\'m a bot of the DandyGames team! ' \
                   r'You can ask any question about the company'
textRU = 'DandyGames это студия празработки игр основанная в 2021 году, идея основания появилась в 2019 году.' \
         'Студия аннонсировала 2 проекта LabOfFate и GameOfGods, ' \
         'ведущий геймдизайнер студии какое-то время работал над проектом Virsen.' \
         'Студия находится по адресу ул. Пушкина дом Колотушкина. ' \
         'Телефон для связи 8-800-352-11-12 '

textEN = r'DandyGames is a game development studio founded in 2021,the idea of foundation appeared in 2019.' \
         r'The studio announced 2 projects LabOfFate and GameOfGods, ' \
         r'Lead game designer of the studio worked for some time on the Virsen project' \
         r'The studio is located at st. Pushkin\'s house of Kolotushkin.' \
         r'Contact phone 8-800-352-11-12'

company_url = 'https://github.com/gDandyDev'


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, hello_message_EN)  # hello text


# ToDo: Перевести сообщения в нижний регистр
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    ic_model = build_model(ic_model_config, download=False)
    intent = ic_model([text])[0]
    print(intent)
    if intent == 'what_time':
        bot.send_message(message.from_user.id, "Time to make games !!")
    if intent == 'tell_me_more':
        bot.send_message(message.from_user.id, company_url)
    else:
        bot.send_message(message.from_user.id, qa_model_training(text))


# def get_url_messages(text):
#     company_url = 'https://github.com/gDandyDev'
#     answer = None
#     intent = ic_model(text)
#     if intent == "tell_me_more":
#         answer = company_url
#     return answer

def qa_model_training(request):
    model_answers = qa_model(
        [textEN],  # text for model
        [request])

    accuracy = model_answers[2][0]
    answer = model_answers[0][0]

    if (int(accuracy) < 1500):
        answer = "I don't know"
    return (answer)


if __name__ == '__main__':
    bot.polling()
