import maya.cmds as cmds
from os.path import realpath
from os.path import isdir
from pymel.core.general import ls
from subprocess import call
import platform

PROJECT_PATH = fixPath(cmds.workspace(q=True, rootDirectory=True))
SCENE_PATH = fixPath(cmds.file(q=True, sceneName=True))
RENDER_COMMAND = 'Render'
MENTAL_RAY = 'mr'
SOFTWARE_RENDER = 'sw'
PADDING = '3'
SPACE = ' '
IMAGE_EXTENSION = 'exr'
FNC_OPTION = '6'
RENDERER = 'hw'

def fixPath(path):
    return str(realpath(path).replace(" ", "\ "))


def getRenderCommandFileName():
    rootDir = str(cmds.workspace(q=True, rootDirectory=True))
    if(platform.system() == 'windows'):
        return rootDir + '\\scripts\\' + 'renderSequence.bat'
    else:
        isdir(rootDir + 'scripts/renderSequence')
        return rootDir + 'scripts/' + 'renderSequence.sh'

def createRenderStringFromShot(shot):
    render_cmd_string = RENDER_COMMAND + SPACE + \
    '-r' + SPACE + RENDERER + SPACE + \
    '-im' + SPACE + 'shot_name' + SPACE + \
    '-of' + SPACE + IMAGE_EXTENSION + SPACE + \
    '-fnc' + SPACE + FNC_OPTION + SPACE + \
    '-pad' + SPACE + PADDING + SPACE + \
    '-cam' + SPACE + str(shot.getCurrentCamera()) + SPACE + \
    '-s' + SPACE + str(shot.getStartTime()) + SPACE + \
    '-e' + SPACE + str(shot.getEndTime()) + SPACE + \
    '-proj' + SPACE + PROJECT_PATH + SPACE + \
    SCENE_PATH
    return render_cmd_string

def createSequenceRenderFile():
    renderFile = open(getRenderCommandFileName(), 'w+')
    for shot in ls(type='shot'):
        renderCommand = createRenderStringFromShot(shot)
        # renderCommands.append(createRenderStringFromShot(shot))
        renderFile.write(renderCommand + '\n')

    renderFile.close()

createSequenceRenderFile()
