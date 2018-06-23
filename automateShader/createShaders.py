# VRAY_SHADER_NODE = "VRayMtl"
# ARNOLD_SHADER_NODE = "aiStandardSurface"
#
# SHADER_TYPE_VRAY = 1
# SHADER_TYPE_ARNOLD = 2
# SHADER_TYPE_REDSHIFT = 3
#
# def createShader(shaderType):
#     if SHADER_TYPE_VRAY:
#         shader = cmds.shadingNode(VRAY_SHADER_NODE, asShader=True)
#         print(shader)
#         surfaceShader = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader + 'SG')
#
#
# shader1 = cmds.shadingNode('anisotrophic', asShader=True)

import pprint
from os import listdir

directory = "C:\\Users\\tahmi\\Google Drive\\MayaProjects\\InteriorPortfolio"

ignoreTexList = ["3dPaintTextures"]

materials = listdir(directory + "\\sourceImages")


def listDirWithFullPath(path):
    listDirectory = listdir(path)
    return map(lambda p: path + "\\" + p, listDirectory)


def containsInList(givenString, list):
    for s in list:
        if s == givenString:
            return True
    return False


def filterMaterials(materials, filterList=ignoreTexList):
    return filter(lambda x: not containsInList(x, ignoreTexList), materials)


def createMaterialPaths(materialList):
    return map(lambda mat: directory + "\\sourceImages\\" + mat, materialList)


def listMaterials(materialPathList):
    arnoldMaterials = []
    vrayMaterials = []
    redshiftMaterials = []
    shaderlessMaterials = []
    for path in materialPathList:
        mapGroup = listdir(path)
        if containsInList('Arnold', mapGroup) or containsInList('Vray', mapGroup) or containsInList('Redshift',
                                                                                                    mapGroup):
            if containsInList('Arnold', mapGroup):
                arnoldMaterials.append(path + '\\Arnold')
            if containsInList('Vray', mapGroup):
                vrayMaterials.append(path + '\\Vray')
            if containsInList('Redshift', mapGroup):
                redshiftMaterials.append(path + '\\Redshift')
        else:
            shaderlessMaterials.append(path)
    return \
        {
            "arnoldMaterials": arnoldMaterials,
            "vrayMaterials": vrayMaterials,
            "redshiftMaterials": redshiftMaterials,
            "shaderlessMaterials": shaderlessMaterials
        }


def findAllTextureSets(textureSetPath):
    return list(set(map(lambda splittedStrList: "".join(splittedStrList[:-1]),
                        map(lambda str: str.split("_"), listdir(textureSetPath)))))


materialList = listMaterials(createMaterialPaths(filterMaterials(materials)))

pprint.PrettyPrinter().pprint(map(lambda texSet: findAllTextureSets(texSet), materialList["arnoldMaterials"]))
