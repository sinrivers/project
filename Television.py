class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 1
    MAX_CHANNEL = 5

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status and self.__volume < self.MAX_VOLUME:
            self.__volume += 10

    def volume_down(self):
        if self.__status and self.__volume > self.MIN_VOLUME:
            self.__volume -= 10

    def get_state(self):
        return {
            "status": self.__status,
            "muted": self.__muted,
            "volume": self.__volume,
            "channel": self.__channel,
        }
