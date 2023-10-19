class DelaySynchronizer:
    def __init__(self, apis: list = []):
        self.apis = [i for i in apis]  # Костыль.
        # Оно почему-то линкается и если ниже ремувать из self.apis, то из переменной, которая передавалась в apis тоже ремувается. Я хуй знает почему
        for api in self.apis:
            api._add_delay_synchronizer(self)

    def _synchronize(self, auto_delay_new):
        for api in self.apis:
            api._auto_delay_time = auto_delay_new

    def add(self, api):
        if type(api) is list:
            for api_ in api:
                self.apis.append(api_)
                api_._add_delay_synchronizer(self)
        elif type(api) is dict:
            for key, value in api.items():
                self.apis.append(value)
                value._add_delay_synchronizer(self)
        else:
            self.apis.append(api)
            api._add_delay_synchronizer(self)

    def remove(self, api):
        if type(api) is list:
            for api_ in api:
                self.apis.remove(api_)
                api_._remove_delay_synchronizer(self)
        elif type(api) is dict:
            for key, value in api.items():
                self.apis.remove(value)
                value._remove_delay_synchronizer(self)
        else:
            self.apis.remove(api)
            api._remove_delay_synchronizer()

    def clear(self):
        apis_td = []
        for api in self.apis:
            apis_td.append(api)
        for api in apis_td:
            self.remove(api)

    def __del__(self):  # Удаляем линки на синхронайзеры из объектов LolzteamApi при удалении
        self.clear()
