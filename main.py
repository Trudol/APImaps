import pygame
import requests
import sys
import os


def ll(x, y):
    return x, y


class Maps:
    def __init__(self):
        self.cntr = 0  # Центр карты
        self.lng = 0  # Широта
        self.zoom = 17  # Увеличение
        self.type = "map"  # Тип карты

    def ll(self):
        return ll(self.lng, self.cntr)


if __name__ == '__main__':
    Maps()
