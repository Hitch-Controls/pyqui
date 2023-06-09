# copied from qtpy
import os

__all__ = ['loadUi']

from PySide6.QtCore import QMetaObject
from PySide6.QtUiTools import QUiLoader


class UiLoader(QUiLoader):
    """
    Subclass of :class:`~PySide.QtUiTools.QUiLoader` to create the user
    interface in a base instance.

    Unlike :class:`~PySide.QtUiTools.QUiLoader` itself this class does not
    create a new instance of the top-level widget, but creates the user
    interface in an existing instance of the top-level class if needed.

    This mimics the behaviour of :func:`PyQt4.uic.loadUi`.
    """

    def __init__(self, baseinstance, customWidgets=None):
        """
        Create a loader for the given ``baseinstance``.

        The user interface is created in ``baseinstance``, which must be an
        instance of the top-level class in the user interface to load, or a
        subclass thereof.

        ``customWidgets`` is a dictionary mapping from class name to class
        object for custom widgets. Usually, this should be done by calling
        registerCustomWidget on the QUiLoader, but with PySide 1.1.2 on
        Ubuntu 12.04 x86_64 this causes a segfault.

        ``parent`` is the parent object of this loader.
        """

        QUiLoader.__init__(self, baseinstance)

        self.baseinstance = baseinstance

        if customWidgets is None:
            self.customWidgets = {}
        else:
            self.customWidgets = customWidgets

    def createWidget(self, class_name, parent=None, name=''):
        """
        Function that is called for each widget defined in ui file,
        overridden here to populate baseinstance instead.
        """

        if parent is None and self.baseinstance:
            # supposed to create the top-level widget, return the base
            # instance instead
            return self.baseinstance

        else:

            # For some reason, Line is not in the list of available
            # widgets, but works fine, so we have to special case it here.
            if class_name in self.availableWidgets() or class_name == 'Line':
                # create a new widget for child widgets
                widget = QUiLoader.createWidget(self, class_name, parent, name)

            else:
                # If not in the list of availableWidgets, must be a custom
                # widget. This will raise KeyError if the user has not
                # supplied the relevant class_name in the dictionary or if
                # customWidgets is empty.
                try:
                    widget = self.customWidgets[class_name](parent)
                except KeyError:
                    raise Exception('No custom widget ' + class_name + ' '
                                                                       'found in customWidgets')

            if self.baseinstance:
                # set an attribute for the new child widget on the base
                # instance, just like PyQt4.uic.loadUi does.
                setattr(self.baseinstance, name, widget)

            return widget


def _get_custom_widgets(ui_file):
    """
    This function is used to parse a ui file and look for the <customwidgets>
    section, then automatically load all the custom widget classes.
    """

    import sys
    import importlib
    from xml.etree.ElementTree import ElementTree

    # Parse the UI file
    etree = ElementTree()
    ui = etree.parse(ui_file)

    # Get the customwidgets section
    custom_widgets = ui.find('customwidgets')

    if custom_widgets is None:
        return {}

    custom_widget_classes = {}

    for custom_widget in custom_widgets.getchildren():
        cw_class = custom_widget.find('class').text
        cw_header = custom_widget.find('header').text

        module = importlib.import_module(cw_header)

        custom_widget_classes[cw_class] = getattr(module, cw_class)

    return custom_widget_classes


def loadUi(uifile, baseinstance=None, workingDirectory=None):
    """
    Dynamically load a user interface from the given ``uifile``.

    ``uifile`` is a string containing a file name of the UI file to load.

    If ``baseinstance`` is ``None``, the a new instance of the top-level
    widget will be created. Otherwise, the user interface is created within
    the given ``baseinstance``. In this case ``baseinstance`` must be an
    instance of the top-level widget class in the UI file to load, or a
    subclass thereof. In other words, if you've created a ``QMainWindow``
    interface in the designer, ``baseinstance`` must be a ``QMainWindow``
    or a subclass thereof, too. You cannot load a ``QMainWindow`` UI file
    with a plain :class:`~PySide.QtGui.QWidget` as ``baseinstance``.

    :method:`~PySide.QtCore.QMetaObject.connectSlotsByName()` is called on
    the created user interface, so you can implemented your slots according
    to its conventions in your widget class.

    Return ``baseinstance``, if ``baseinstance`` is not ``None``. Otherwise
    return the newly created instance of the user interface.
    """

    # We parse the UI file and import any required custom widgets
    customWidgets = _get_custom_widgets(uifile)

    loader = UiLoader(baseinstance, customWidgets)

    if workingDirectory is not None:
        loader.setWorkingDirectory(workingDirectory)

    widget = loader.load(uifile)
    QMetaObject.connectSlotsByName(widget)
    return widget
