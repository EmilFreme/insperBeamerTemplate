#!/usr/bin/env python3
import os

def install():
    if "linux" in  os.sys.platform:
        texlivePath = "/usr/share/texlive/texmf-dist/tex/latex/beamer"
        print(os.path.exists(texlivePath))
        if(os.path.isdir(texlivePath)):
            print("Texlive beamer path found...")
            print("Copying theme file into beamer folder...")
            os.system("cp beamerthemeinsper.sty \
{}/beamerthemeinsper.sty".format(texlivePath))
            print("Copying themeinner file into beamer folder...")
            os.system("cp beamerinnerthemeinsper.sty \
{}/beamerinnerthemeinsper.sty".format(texlivePath))
            print("Copying themeouter file into beamer folder...")
            os.system("cp beamerouterthemeinsper.sty \
{}/beamerouterthemeinsper.sty".format(texlivePath))
            print("Copying themecolor file into beamer folder...")
            os.system("cp beamercolorthemeinsper.sty \
{}/beamercolorthemeinsper.sty".format(texlivePath))
            print("Copying themefont file into beamer folder...")
            os.system("cp beamerfontthemeinsper.sty \
{}/beamerfontthemeinsper.sty".format(texlivePath))
            print("Copying images folter into beamer folder...")
            os.system("cp -a img/. \
{}/img/".format(texlivePath))

if __name__ == "__main__":
    install()
