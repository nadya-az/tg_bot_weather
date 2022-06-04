import requests
import datetime
from config import tg_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь\U00002614",
        "Drizzle": "Дождь\U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U00002744",
        "Mist": "Туман \U0001F32B"

    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно"

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}°C {wd}\nВлажность: {humidity}%\n"
              f"Восход солнца: {sunrise_timestamp}\n"
              f"Хорошего дня!")

    except :

        await message.reply("\U00002620 Проверьте название города \U00002620")

if __name__ == '__main__':
    executor.start_polling(dp)
