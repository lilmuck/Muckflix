# -*- coding: utf-8 -*-

import traceback

if __name__ == "__main__":
    output = None
    try:
        from plugin import __run, __output

        output = __output
        __run()

    except Exception as e:
        import xbmcgui

        xbmcgui.Dialog().ok("Entschuldigung :(",
                            "Leider wurde ein unerwarteter Fehler festgestellt.\nBitte erneut Probieren ansonsten das Plugin erneut [B]Installieren[/B]!")
        raise