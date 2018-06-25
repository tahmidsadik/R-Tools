# VRAY_SHADER_NODE = 'VRayMtl'
# ARNOLD_SHADER_NODE = 'aiStandardSurface'
#
# SHADER_TYPE_VRAY = 1
# SHADER_TYPE_ARNOLD = 2
# SHADER_TYPE_REDSHIFT = 3
#
# def createShader(shaderType):
#     if SHADER_TYPE_VRAY:
#         shader = cmds.shadingNode(VRAY_SHADER_NODE, asShader=True) #
#         print(shader)
#         surfaceShader = cmds.sets(
#           renderable=True, noSurfaceShader=True,
#                empty=True, name=shader + 'SG') #
#
# shader1 = cmds.shadingNode('anisotrophic', asShader=True)

import platform
import pprint
from os import listdir, sep, path

pp = pprint.PrettyPrinter()
directory = ''

if platform.system() == 'Windows':
    directory = path.join('C:', sep, 'Users', 'tahmi', 'Google Drive',
                          'MayaProjects', 'InteriorPortfolio')
elif platform.system() == 'Darwin':
    directory = path.join(sep, 'Users', 'tahmid', 'Documents',
                          'InteriorPortfolio')

ignoreTexList = ['3dPaintTextures']

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
    return map(lambda mat: path.join(directory, 'sourceimages', mat),
               materialList)


def listMaterials(materialPathList):
    arnoldMaterials = []
    vrayMaterials = []
    redshiftMaterials = []
    shaderlessMaterials = []
    for matPath in materialPathList:
        mapGroup = listdir(matPath)
        if containsInList('Arnold', mapGroup) or containsInList(
                'Vray', mapGroup) or containsInList('Redshift', mapGroup):
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
    return list(
        set(
            map(lambda splittedStrList: "_".join(splittedStrList[:-1]),
                map(lambda str: str.split("_"), listdir(textureSetPath)))))


def listAllTextureSets(materialPaths):
    textureSets = {}
    for key, value in materialPaths.items():
        tset = []
        for tsetPath in value:
            ts = {
                "textureSets": findAllTextureSets(tsetPath),
                "path": tsetPath
            }
            tset.append(ts)
        if key == 'arnoldMaterials':
            textureSets['arnoldTextureSets'] = tset
        elif key == 'vrayMaterials':
            textureSets['vrayTextureSets'] = tset
        elif key == 'redshiftMaterials':
            textureSets['redshiftTextureSets'] = tset
        else:
            textureSets['shaderlessTextureSets'] = tset
    return textureSets


def extractTextureMapsFromTextureSetPath(textureSetDict):
    """textureSetDict is a dictionary of shape
       {'path': 'xx', 'textureSets': ['texSet1', 'texSet2']
       This function finds all the maps of each textureSet contained in a
       textureSetPath.
       The function returns a list of shape
       [{
            'name': 'tset1',
            'path': 'path',
            'maps': [{'type': 'normal', 'path': 'path_to_normal_map'},
                    {'type': 'diffuse', 'path': 'path_to_diffuse'},
                    {'type': 'roughness', 'path': 'path_to_roughness'}]
       }, {
            'name': 'tset2',
            'path': 'path',
            'maps': ['normal', 'diffuse', 'glosiness', 'roughness']
       }]
       ]
    """
    textureMaps = []
    for tset in textureSetDict['textureSets']:
        textureSet = {'name': tset, 'path': textureSetDict['path'], 'maps': []}
        for tmap in listdir(textureSetDict['path']):
            if tset in tmap:
                map_type = tmap.split('_')[-1]
                map_path = path.join(textureSetDict['path'], tmap)
                # can't write this
                # textureSet['maps'] = textureSet['maps']
                #                      .append(
                #                      {'type': map_type, 'path': map_path})
                # cause python is a bitch
                # instead we need to do this
                textureSet.setdefault('maps', textureSet['maps']).append({
                    'type':
                    map_type,
                    'path':
                    map_path
                })
        textureMaps.append(textureSet)

    return textureMaps


def extractAllTextureSets(tsetDict):
    allTexSets = {}
    for textureSetName, textureSetPaths in tsetDict.items():
        tsets = []
        for tpath in textureSetPaths:
            tsets.append(extractTextureMapsFromTextureSetPath(tpath))
        allTexSets[textureSetName] = tsets
    return allTexSets


filteredTextureSetPaths = listMaterials(
    createMaterialPaths(filterMaterials(textureSetPathList)))
allTextureSets = listAllTextureSets(filteredTextureSetPaths)
pp.pprint(extractAllTextureSets(allTextureSets))
