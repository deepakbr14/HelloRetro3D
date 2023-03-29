from Retro3D import *



###############################################################################
#
###############################################################################
class HelloRetro3D(Game):

    REZ_MODEL_CUBE          = "cube" + os.sep + "cube.obj"


    ###############################################################################
    #
    # need to override so you can initialize your game with your stuff
    #
    ###############################################################################
    def __init__(self, config: ConfigGame, fpath_base:str):
    
        super().__init__(config, fpath_base)

        
        # camera info
        self.engine.camera.pos = pg.math.Vector3(0.0, 0.0, -10.0)
        self.engine.camera.rot = pg.math.Vector3(0.0, 0.0, 0.0)

        # load models
        self.rez.add_model(HelloRetro3D.REZ_MODEL_CUBE)

        # game needs to tell engine to start menu mode        
        self.game_state = Game.STATE_MENU

        # create cube
        self.cube = Object()
        self.cube.set_model(self.rez.get_model(HelloRetro3D.REZ_MODEL_CUBE), pg.Color(255, 255, 0))
        self.cube.set_pos(0.0, 0.0, 0.0)
        self.cube.set_rot(0.0, 0.0, 0.0)  
        self.engine.add_display_object(self.cube, Engine.DISPLAY_LIST_SHADED_OUTLINE)



    ###############################################################################
    #
    # need to override so you can update 3d objects
    #
    ###############################################################################
    def update(self):
        
        if super().update() == False:
            return

        self.cube.rot.x += 0.01
        self.cube.rot.y += 0.05
        self.cube.update()

    ###############################################################################
    #
    # override this if you want something other than the default background
    # 
    ###############################################################################
    def draw_background(self):  
    
        super().draw_background()

        rect = pg.Rect(0, 0, self.engine.config.screen_resolution.x, self.engine.config.screen_resolution.y)
        self.engine.draw_rect_gradient(pg.Color(30, 30, 30), pg.Color(0, 0, 0), rect, SiDirection.VERTICAL)
       

