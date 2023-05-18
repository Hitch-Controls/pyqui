# from . import uic, QtCore, QtWidgets, QtGui, QtOpenGL, QtWebEngineWidgets
# from PySide6 import QtSvgWidgets, QtSvg  # noqa
import qtpy
from qtpy import QtCore, QtWidgets, QtGui, QtOpenGL, QtWebEngineWidgets
from qtpy import uic, QtSvg, QtSvgWidgets, QtCharts  # noqa

try:
    from qtpy import QtWinExtras
except qtpy.QtModuleNotInOSError:
    pass

# The wrapper modules included above are only needed so we can create these shortcuts
qtc = QtCore
qtw = QtWidgets
qtwe = QtWebEngineWidgets
qtg = QtGui
qtgl = QtOpenGL
