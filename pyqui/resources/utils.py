# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
from pathlib import Path

from . import RES_PATH

SVG_ICON_DIR = RES_PATH / "images" / "svg_icons"
SVG_IMAGE_DIR = RES_PATH / "images" / "svg_images"
IMAGES_DIR = RES_PATH / "images" / "images"


def svg_icon(icon_name):
    if not icon_name.startswith(':'):
        return (SVG_ICON_DIR / icon_name).as_posix()
    return icon_name


def svg_image(image_name):
    if not image_name.startswith(':'):
        return (SVG_IMAGE_DIR / image_name).as_posix()
    return image_name
