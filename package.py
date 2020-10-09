# -*- coding: utf-8 -*-

name = 'blosc'

version = '1.5.0-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

build_requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x64'],
]

build_system = 'cmake'

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.BLOSC_VERSION.set(split_versions[0])
    env.BLOSC_PACKAGE_VERSION.set(split_versions[1])

    env.BLOSC_ROOT.set("{root}")
    env.BLOSC_INCLUDE_DIR.set("{root}/include")
    env.BLOSC_LIBRARY_DIR.set("{root}/lib")
    env.BLOSC_BINARY_DIR.set("{root}/bin")

    env.PATH.append( str(env.BLOSC_BINARY_DIR) )
    env.PATH.append( str(env.BLOSC_LIBRARY_DIR) )
