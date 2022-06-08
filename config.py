tgbot = '5507990619:AAFaqXpxi91mHhRhPxBCZcrL_2BzRSOI4W0'
ya_weather = '060dfe41-aaf5-48da-a4c9-ccfdb97ab4ca'

#
# import config
# import requests
# import datetime
# from pprint import pprint
# from geopy.geocoders import Nominatim
# from geopy import geocoders
#
#
# def get_weather(city, ya_weather):
#     try:
#         geolocator = geocoders.Nominatim(
#             user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                        'Chrome/98.0.4758.141 YaBrowser/22.3.3.866 Yowser/2.5 Safari/537.36')
#         location = geolocator.geocode(city)
#         url = f'https://api.weather.yandex.ru/v2/informers?lat={location.latitude}&lon={location.longitude}'
#         headers = {'X-Yandex-API-Key': ya_weather}
#         ya_r = requests.get(url, headers=headers)
#         data = ya_r.json()
#         print(data)
#     except Exception as ex:
#         print(ex)
#         print("Проверьте название города")
#
#
# def main():
#     city = input("Введите город: ")
#     get_weather(city, config.ya_weather)
#
#
# if __name__ == '__main__':
#     main()

