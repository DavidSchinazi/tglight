#!/usr/bin/python
#
# Installs useful dependencies for dfplayer development.

import os
import shutil
import subprocess
import sys

_PILLOW_DEPS = [
    'libfreetype6-dev',
    'libjpeg8-dev',
    'liblcms2-dev',
    'libtiff4-dev',
    'libwebp-dev',
    'tcl-dev',
    'tk-dev',
    'zlib1g-dev',
    ]

_PLAYER_DEPS = [
    'libaudiofile-dev',
    'libav-tools',
    'libopencv-dev',
    'mpd',
    #'nvidia-current',
    'nvidia-cg-dev',
    'nvidia-cg-toolkit',
    'opencv-doc',
    'python-dev',
    'python-mpd',
    'python-mutagen',
    'python-setuptools',
    'python-tk',
    'swig',
    ]

_KINECT_DEPS = [
    'freeglut3-dev',
    'libjpeg-turbo8-dev',
    'libturbojpeg',
    'libusb-1.0-0-dev',
    'libxmu-dev',
    ]

_EXTERNAL_DEPS = [
    'cmake',
    'libasound2-dev',
    'libglew-dev',
    'libftgl-dev',
    ]

_USEFUL_PACKAGES = [
    'apcupsd',
    'gdb',
    'gimp',
    'git',
    'libasound2-doc',
    'mesa-utils',
    'synaptic',
    'vim',
    ]

if os.geteuid() != 0:
  print 'ERROR: Please run as root'
  sys.exit(1)

subprocess.check_call(['apt-get', 'install', '-y'] + _PILLOW_DEPS)
subprocess.check_call(['apt-get', 'install', '-y'] + _PLAYER_DEPS)
subprocess.check_call(['apt-get', 'install', '-y'] + _KINECT_DEPS)
subprocess.check_call(['apt-get', 'install', '-y'] + _EXTERNAL_DEPS)
subprocess.check_call(['apt-get', 'install', '-y'] + _USEFUL_PACKAGES)

subprocess.check_call(['easy_install', 'pip'])

# PIL and Pillow cannot coexist.
# subprocess.check_call(['pip', 'uninstall', 'PIL'])

subprocess.check_call(['pip', 'install', 'dxfgrabber'])
subprocess.check_call(['pip', 'install', 'flask'])
subprocess.check_call(['pip', 'install', 'pillow'])
subprocess.check_call(['pip', 'install', 'virtualenv'])

TURBO_JPEG = '/usr/lib/x86_64-linux-gnu/libturbojpeg.so'
if not os.path.exists(TURBO_JPEG):
  os.symlink(TURBO_JPEG + '.0', TURBO_JPEG)

RULES_DIR = '/etc/udev/rules.d'
shutil.copyfile(
    'external/kkonnect/external/libfreenect/platform/linux/udev/51-kinect.rules',
    RULES_DIR + '/51-kinect.rules')
shutil.copyfile(
    'external/kkonnect/external/libfreenect2/rules/90-kinect2.rules',
    RULES_DIR + '/90-kinect2.rules')


print '=== SUCCESS ==='

