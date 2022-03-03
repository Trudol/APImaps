import pygame
import requests
import sys
import os


class MapsParams:
    def __init__(self):
        self.lat = 0  # Центр карты
        self.lon = 0  # Широта x
        self.zoom = 17.6  # Увеличение
        self.type = "map"  # Тип карты

    def ll(self):
        return self.lon, self.lat, self.zoom


# https://static-maps.yandex.ru/1.x/?azimuth=0.15&ll=50.607,55.3647&z=17&l=map

def load_map(lat, lon, zoom, type):
     map_request = f"https://static-maps.yandex.ru/1.x/?ll={lat},{lon}&z={zoom}&l={type}"
     response = requests.get(map_request)
     if not response:
         print("Ошибка выполнения запроса")
         print(map_request)
         print("Http статус:", response.status_code)
         sys.exit(1)

    map_file = "map.png"
    try:
        pass
    except IOError as error:
        print(error)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapsParams()

    running = True
    while running:

        screen.blit()
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    main()
