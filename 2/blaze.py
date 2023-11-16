import requests


class Blaze:
    def __init__(self, url):
        self.url = url

    def buscar_resultados(self):
        r = requests.get(self.url)
        return r.text


if __name__ == "__main__":
    url = "https://blaze.com/api/crash_games/recent"
    obj_blaze = Blaze(url)
    obj_blaze.buscar_resultados()
