from bases.challengeList import *

class XSSChall(Challenge):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, data):
        self.open_path_with_cookie(data,{"flag":"UAH{AYYYyyYYyYYY}"})