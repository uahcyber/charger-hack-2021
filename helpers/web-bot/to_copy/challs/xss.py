from bases.challengeList import *

class XSSChall(Challenge):

    flag = "UAH{sCr1PTiNG_N0T_sk1PpinG_ACr05s_the_s1tE}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, data):
        self.open_path_with_cookie(data,{"flag":flag})