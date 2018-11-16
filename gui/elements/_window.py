from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter

from ._viewer import Viewer


class Window:
    """Application window.
    """
    def __init__(self):
        self._qt_window = QMainWindow()
        self._qt_central_widget = QWidget()
        self._qt_window.setCentralWidget(self._qt_central_widget)
        self._qt_central_widget.setLayout(QHBoxLayout())
        self._qt_window.statusBar().showMessage('Ready')

        self._viewers = []

    @property
    def viewers(self):
        """list of Viewer: Contained viewers.
        """
        return self._viewers

    def add_viewer(self):
        """Adds a viewer to the containing layout.

        Returns
        -------
        viewer : Viewer
            Viewer object.
        """
        viewer = Viewer(self)
        self.viewers.append(viewer)

        # To split vertical sliders, viewer and layerlist, minimumsizes given for demo purposes/NOT FINAL
        horizontalSplitter = QSplitter(Qt.Horizontal)
        viewer.controls._qt.setMinimumSize(QSize(60, 60))
        horizontalSplitter.addWidget(viewer.controls._qt)
        viewer._qt.setMinimumSize(QSize(500, 500))
        horizontalSplitter.addWidget(viewer._qt)
        viewer.layers._qt.setMinimumSize(QSize(150, 150))
        horizontalSplitter.addWidget(viewer.layers._qt)

        self._qt_central_widget.layout().addWidget(horizontalSplitter)
        return viewer

    def resize(self, *args):
        self._qt_window.resize(*args)

    def show(self):
        self.resize(self._qt_window.layout().sizeHint())
        self._qt_window.show()
        self._qt_window.raise_()
