from Retro3D import *
from HelloRetro3D import *


if __name__ == '__main__':

    # the Retro3D engine uses this config to setup basic stuff for your game
    config = ConfigGame()

    config.screen_resolution = pg.math.Vector2(1200, 768)

    config.menu_background_color_top = pg.Color(0, 0, 100)
    config.menu_background_color_bottom = pg.Color(0, 0, 0)
    config.light_direction = pg.math.Vector3(1.0, 0.0, 0.0)
    config.title = "Hello Retro3D";
    config.author = "Deepak Deo"
    config.year = "1977"

    config.instructions =  "Put your\n"
    config.instructions += " Insructions Here!\n"

    config.credits = ""
    config.credits += "Put your\n"
    config.credits += "Credits here!\n"
    

    # create your game and get it running
    # rez_fpath is the path to the rez folder which holds all of your assets (art/sound/fonts) in a standardized folder structure
    rez_fpath = os.path.dirname(__file__) + os.sep + "rez" + os.sep
    game = HelloRetro3D(config, rez_fpath)
    game.run()


