# VRAY_SHADER_NODE = 'VRayMtl'
# ARNOLD_SHADER_NODE = 'aiStandardSurface'
#
# SHADER_TYPE_VRAY = 1
# SHADER_TYPE_ARNOLD = 2
# SHADER_TYPE_REDSHIFT = 3
#
# def createShader(shaderType):
#     if SHADER_TYPE_VRAY:
#         shader = cmds.shadingNode(VRAY_SHADER_NODE, asShader=True)
#         print(shader)
#         surfaceShader = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader + 'SG') #
#
# shader1 = cmds.shadingNode('anisotrophic', asShader=True)

from os import listdir, sep, path
import platform
import pprint

pp = pprint.PrettyPrinter()
directory = ''

if platform.system == 'Windows':
    directory = path.join('c:', 'Users', 'tahmi', 'Google Drive', 'MayaProjects', 'InteriorPortfolio')
elif platform.system == 'Darwin':
    directory = path.join(sep, 'Users', 'tahmid', 'Documents', 'InteriorPortfolio')
else:
    directory = path.join(sep, 'Users', 'tahmid', 'Documents', 'InteriorPortfolio')

ignoreTexList = ['3dPaintTextures']
print(directory)

textureSetPathList = listdir(path.join(directory, 'sourceimages'))

def listDirWithFullPath(path):
    listDirectory = listdir(path)
    return map(lambda p: path.join(path, p, listDirectory))


def containsInList(givenString, list):
    for s in list:
        if s == givenString:
            return True
    return False


def filterMaterials(materials, filterList=ignoreTexList):
    return filter(lambda x: not containsInList(x, ignoreTexList), materials)


def createMaterialPaths(materialList):
    return map(lambda mat: path.join(directory, 'sourceImages', mat), materialList)


def listMaterials(materialPathList):
    arnoldMaterials = []
    vrayMaterials = []
    redshiftMaterials = []
    shaderlessMaterials = []
    for matPath in materialPathList:
        mapGroup = listdir(matPath)
        if containsInList('Arnold', mapGroup) or containsInList('Vray', mapGroup) or containsInList('Redshift', mapGroup):
            if containsInList('Arnold', mapGroup):
                arnoldMaterials.append(path.join(matPath, 'Arnold'))
            if containsInList('Vray', mapGroup):
                vrayMaterials.append(path.join(matPath, 'Vray'))
            if containsInList('Redshift', mapGroup):
                redshiftMaterials.append(path.join(matPath, 'Redshift'))
        else:
            shaderlessMaterials.append(matPath)
    return \
        {
            'arnoldMaterials': arnoldMaterials,
            'vrayMaterials': vrayMaterials,
            'redshiftMaterials': redshiftMaterials,
            'shaderlessMaterials': shaderlessMaterials
        }


def findAllTextureSets(textureSetPath):
    return list(set(map(lambda splittedStrList: "".join(splittedStrList[:-1]),
                        map(lambda str: str.split("_"), listdir(textureSetPath)))))


filteredTextureSetPaths = listMaterials(createMaterialPaths(filterMaterials(textureSetPathList)))
pp.pprint(filteredTextureSetPaths)

pprint.PrettyPrinter().pprint(list(map(lambda texSet: findAllTextureSets(texSet), filteredTextureSetPaths['arnoldMaterials'])))
