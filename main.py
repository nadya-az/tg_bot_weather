import requests
import datetime
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from geopy import geocoders

bot = Bot(token=config.tgbot)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "clear": "Ясно \U00002600",
        "clouds": "Облачно \U00002601",
        "rain": "Дождь\U00002614",
        "drizzle": "Дождь\U00002614",
        "thunderstorm": "Гроза \U000026A1",
        "snow": "Снег \U00002744",
        "mist": "Туман \U0001F32B"

    }
    try:
        geolocator = geocoders.Nominatim(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/98.0.4758.141 YaBrowser/22.3.3.866 Yowser/2.5 Safari/537.36')
        location = geolocator.geocode(message.text)
        url = f'https://api.weather.yandex.ru/v2/informers?lat={location.latitude}&lon={location.longitude}'
        headers = {'X-Yandex-API-Key': config.ya_weather}
        ya_r = requests.get(url, headers=headers)
        data = ya_r.json()
        city = message.text
        cur_weather = data["fact"]["temp"]
        humidity = data["fact"]["humidity"]
        sunrise_timestamp = data["forecast"]["sunrise"]
        weather_description = data["fact"]["condition"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно"

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}°C\n {wd}\nВлажность: {humidity}%\n"
                            f"Восход солнца: {sunrise_timestamp}\n"
                            f"Хорошего дня!")
    except Exception as ex:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)
