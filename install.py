#!/usr/bin/env python3
import os

def install():
    if not "win32" in  os.sys.platform:
        searchFile = "beamerthemedefault.sty"
        paths = os.popen("find /usr -name {}".format(searchFile)).readlines()
        beamerPath = [line for line in paths if searchFile in line][0]
        beamerPath = beamerPath.replace("/beamerthemedefault.sty\n", "");
        print(beamerPath)
        print(os.path.exists(beamerPath))
        if(os.path.isdir(beamerPath)):
            print("Texlive beamer path found...")
            print(beamerPath)
            print("Copying theme file into beamer folder...")
            os.system("cp beamerthemeinsper.sty \
{}/beamerthemeinsper.sty".format(beamerPath))
            print("Copying themeinner file into beamer folder...")
            os.system("cp beamerinnerthemeinsper.sty \
{}/beamerinnerthemeinsper.sty".format(beamerPath))
            print("Copying themeouter file into beamer folder...")
            os.system("cp beamerouterthemeinsper.sty \
{}/beamerouterthemeinsper.sty".format(beamerPath))
            print("Copying themecolor file into beamer folder...")
            os.system("cp beamercolorthemeinsper.sty \
{}/beamercolorthemeinsper.sty".format(beamerPath))
            print("Copying themefont file into beamer folder...")
            os.system("cp beamerfontthemeinsper.sty \
{}/beamerfontthemeinsper.sty".format(beamerPath))
            print("Copying images folter into beamer folder...")
            os.system("cp -a img/. \
{}/img/".format(beamerPath))
        else:
            print("Beamer Path não encontrado")
    else:
        print("Script para windows em construção")
        print("Não instalado")

if __name__ == "__main__":
    install()
