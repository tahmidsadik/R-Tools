from pymel.core.general import ls

RENDER_COMMAND = 'Render'
MENTAL_RAY = 'mr'
SOFTWARE_RENDER = 'sw'
PROJECT_PATH = ''
SCENE_PATH = ''
PADDING = '3'
SPACE = ' '
IMAGE_EXTENSION = 'exr'
FNC_OPTION = '6'
RENDERER = MENTAL_RAY


def createRenderStringFromShot(shot):
    render_cmd_string = RENDER_COMMAND + SPACE + '-r' + SPACE + RENDERER + SPACE
    + '-im' + SPACE + 'shot_name' + SPACE + '-of' + IMAGE_EXTENSION + SPACE +
    '-fnc' + SPACE + FNC_OPTION + '-pad' + SPACE + PADDING + '-proj' + SPACE +
    PROJECT_PATH + SPACE + SCENE_PATH

    return render_cmd_string


for shot in ls(type='shot'):
    print(createRenderStringFromShot(shot))
