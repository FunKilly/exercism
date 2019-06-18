class Clock(object):
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + (minute - self.minute) // 60) % 24

    def __repr__(self):
        return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}'

    def __eq__(self, other):
        return self.minute == other.minute and self.hour == other.hour

    def __add__(self, minutes):
        self.__init__(self.hour, self.minute + minutes)
        return self

    def __sub__(self, minutes):
        self.__init__(self.hour, self.minute - minutes)
        return self