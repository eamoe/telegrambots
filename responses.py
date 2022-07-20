from datetime import datetime
import weather as w


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi'):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I'm an Eugene's bot!"

    if user_message in ("лиза", "liza"):
        return "Я люблю Лизу! ❤️"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message.split(" ")[0] in ('weather', 'погода'):
        city = user_message.split(" ")[1]
        return w.get_weather(city)

    return "I don't understand you!"
