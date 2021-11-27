CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        # checks if list is empty, etc
        # ...

        self.channels = channels
        self._current_channel = channels[0]

    def first_channel(self):
        self._current_channel = self.channels[0]
        return self._current_channel

    def last_channel(self):
        self._current_channel = self.channels[-1]
        return self._current_channel

    def turn_channel(self, channel):
        """
        channel - can be from 1 to the number of channels

        to return the first channel from the list of channels, index should be 0 (1 - 1).
        to return the second channel from the list of channels, index should be 1 (2 - 1).
        """

        self._current_channel = self.channels[channel-1]
        return self._current_channel

    def next_channel(self):
        # index of the current channel from the list of channels
        idx = self.channels.index(self._current_channel)

        if idx == (len(self.channels) - 1):
            self._current_channel = self.channels[0]
        else:
            self._current_channel = self.channels[idx+1]

        return self._current_channel

    def previous_channel(self):
        # index of the current channel from the list of channels
        idx = self.channels.index(self._current_channel)

        if idx == 0:
            self._current_channel = self.channels[-1]
        else:
            self._current_channel = self.channels[idx-1]

        return self._current_channel

    def current_channel(self):
        return self._current_channel

    def is_exist(self, channel):
        if type(channel) is int:
            return "No" if channel < 1 or channel > len(self.channels) else "Yes"
            # or
            # if  channel < 1 or channel > len(self.channels):
            #     return "No"
            # else:
            #     return "Yes"

        return "Yes" if channel in self.channels else "No"
        # or
        # if channel in self.channels:
        #     return "Yes"
        # else:
        #     return "No"


controller = TVController(CHANNELS)

# controller.first_channel() == "BBC"
print("First channel:", controller.first_channel())

# controller.last_channel() == "TV1000"
print("Last channel:", controller.last_channel())

# controller.turn_channel(1) == "BBC"
print("Channel under number 1:", controller.turn_channel(1))

# controller.next_channel() == "Discovery"
print("Next channel:", controller.next_channel())

# controller.previous_channel() == "BBC"
print("Previous channel:", controller.previous_channel())

print("Current channel:", controller.current_channel())

# controller.is_exist(4) == "No"
print("Have channel with number 4:", controller.is_exist(4))

# controller.is_exist("BBC") == "Yes"
print("Have channel 'BBC':", controller.is_exist('BBC'))
