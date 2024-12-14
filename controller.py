from Television import Television

class Controller:
    def __init__(self, view):
        self.tv = Television()
        self.view = view
        self.update_view()

    def update_view(self):
        if self.view:
            self.view.update_ui(self.tv.get_state())

    def toggle_power(self):
        self.tv.power()
        self.update_view()

    def toggle_mute(self):
        self.tv.mute()
        self.update_view()

    def channel_up(self):
        self.tv.channel_up()
        self.update_view()

    def channel_down(self):
        self.tv.channel_down()
        self.update_view()

    def volume_up(self):
        self.tv.volume_up()
        self.update_view()

    def volume_down(self):
        self.tv.volume_down()
        self.update_view()
