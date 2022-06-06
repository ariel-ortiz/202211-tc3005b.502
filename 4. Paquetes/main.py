from alfa.uno import fun_uno, Uno
from alfa.beta.dos import fun_dos, Dos
from gamma.tres import fun_tres, Tres

class Main:

    def just_do_it(self):
        fun_uno()
        u = Uno()
        print(u)
        fun_dos()
        d = Dos()
        print(d)
        fun_tres()
        t = Tres()
        print(t)

Main().just_do_it()