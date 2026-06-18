from pyfiglet import Figlet


def banner():
    f = Figlet(font="ansi_shadow")
    print(f.renderText("Tooldevs"))
