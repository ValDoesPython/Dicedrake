from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget,QMainWindow
import wallpaper_rc
import icons_rc
import random, string, math, sys
import sqlite3 as lite
class Ui_MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(list)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.oldPos = self.pos()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1317, 907)
        MainWindow.setStyleSheet("*{\n"
"   border:none;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(103,7,71);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.slide_menu_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.slide_menu_container.setMouseTracking(True)
        self.slide_menu_container.setStyleSheet("background-color:rgb(20,16,15);")
        self.slide_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu_container.setObjectName("slide_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slidemenu = QtWidgets.QFrame(self.slide_menu_container)
        self.slidemenu.setMinimumSize(QtCore.QSize(198, 0))
        self.slidemenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slidemenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slidemenu.setObjectName("slidemenu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.slidemenu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.MenuHeader = QtWidgets.QFrame(self.slidemenu)
        self.MenuHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuHeader.setObjectName("MenuHeader")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.MenuHeader)
        self.horizontalLayout_8.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.DicedrakeLabel = QtWidgets.QLabel(self.MenuHeader)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DicedrakeLabel.setFont(font)
        self.DicedrakeLabel.setObjectName("DicedrakeLabel")
        self.horizontalLayout_8.addWidget(self.DicedrakeLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.DicedrakeDice = QtWidgets.QLabel(self.MenuHeader)
        self.DicedrakeDice.setText("")
        self.DicedrakeDice.setPixmap(QtGui.QPixmap(":/icons/hexagon.svg"))
        self.DicedrakeDice.setObjectName("DicedrakeDice")
        self.horizontalLayout_8.addWidget(self.DicedrakeDice, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.MenuHeader, 0, QtCore.Qt.AlignTop)
        self.MenuFrame = QtWidgets.QFrame(self.slidemenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuFrame.sizePolicy().hasHeightForWidth())
        self.MenuFrame.setSizePolicy(sizePolicy)
        self.MenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuFrame.setObjectName("MenuFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.MenuFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.MenuToolbox = QtWidgets.QToolBox(self.MenuFrame)
        self.MenuToolbox.setStyleSheet("QtoolBox{\n"
"    background-color: rgb(103,7,71);\n"
"    text-align: left;\n"
"}\n"
"QToolBox::tab {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(64,12,42);\n"
"    text-align: left;\n"
"}")
        self.MenuToolbox.setObjectName("MenuToolbox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 164, 705))
        self.page.setObjectName("page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.page)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Profile = QtWidgets.QPushButton(self.frame_10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile.setIcon(icon)
        self.Profile.setObjectName("Profile")
        self.verticalLayout_11.addWidget(self.Profile)
        self.Friends = QtWidgets.QPushButton(self.frame_10)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Friends.setIcon(icon1)
        self.Friends.setObjectName("Friends")
        self.verticalLayout_11.addWidget(self.Friends)
        self.Forum = QtWidgets.QPushButton(self.frame_10)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/message-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Forum.setIcon(icon2)
        self.Forum.setObjectName("Forum")
        self.verticalLayout_11.addWidget(self.Forum)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.MenuToolbox.addItem(self.page, icon1, "")
        self.MainMenu = QtWidgets.QWidget()
        self.MainMenu.setGeometry(QtCore.QRect(0, 0, 164, 705))
        self.MainMenu.setObjectName("MainMenu")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.MainMenu)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.MainMenu)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.CharacterCreator = QtWidgets.QPushButton(self.frame_11)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/hexagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CharacterCreator.setIcon(icon3)
        self.CharacterCreator.setObjectName("CharacterCreator")
        self.verticalLayout_12.addWidget(self.CharacterCreator)
        self.CharacterEditor = QtWidgets.QPushButton(self.frame_11)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/edit-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CharacterEditor.setIcon(icon4)
        self.CharacterEditor.setObjectName("CharacterEditor")
        self.verticalLayout_12.addWidget(self.CharacterEditor)
        self.CharacterVierwe = QtWidgets.QPushButton(self.frame_11)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CharacterVierwe.setIcon(icon5)
        self.CharacterVierwe.setObjectName("CharacterVierwe")
        self.verticalLayout_12.addWidget(self.CharacterVierwe)
        self.verticalLayout_8.addWidget(self.frame_11)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuToolbox.addItem(self.MainMenu, icon6, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setGeometry(QtCore.QRect(0, 0, 164, 705))
        self.Settings.setObjectName("Settings")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Settings)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.Settings)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Placeholder = QtWidgets.QPushButton(self.frame_12)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/alert-octagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Placeholder.setIcon(icon7)
        self.Placeholder.setObjectName("Placeholder")
        self.verticalLayout_13.addWidget(self.Placeholder)
        self.verticalLayout_10.addWidget(self.frame_12)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuToolbox.addItem(self.Settings, icon8, "")
        self.verticalLayout_7.addWidget(self.MenuToolbox)
        self.verticalLayout_5.addWidget(self.MenuFrame)
        self.MenuFooter = QtWidgets.QFrame(self.slidemenu)
        self.MenuFooter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuFooter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuFooter.setObjectName("MenuFooter")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.MenuFooter)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ExitMenu = QtWidgets.QPushButton(self.MenuFooter)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitMenu.setIcon(icon9)
        self.ExitMenu.setIconSize(QtCore.QSize(32, 32))
        self.ExitMenu.setObjectName("ExitMenu")
        self.verticalLayout_6.addWidget(self.ExitMenu, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.MenuFooter, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.slidemenu)
        self.horizontalLayout.addWidget(self.slide_menu_container)
        self.mainbodcontainer = QtWidgets.QFrame(self.centralwidget)
        self.mainbodcontainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbodcontainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbodcontainer.setObjectName("mainbodcontainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainbodcontainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerframe = QtWidgets.QFrame(self.mainbodcontainer)
        self.headerframe.setStyleSheet("background-color:rgb(20,16,15);")
        self.headerframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerframe.setObjectName("headerframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerframe)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuButtonFrame = QtWidgets.QFrame(self.headerframe)
        self.MenuButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuButtonFrame.setObjectName("MenuButtonFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.MenuButtonFrame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.menuButton = QtWidgets.QPushButton(self.MenuButtonFrame)
        self.menuButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon10)
        self.menuButton.setIconSize(QtCore.QSize(32, 32))
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_7.addWidget(self.menuButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.MenuButtonFrame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SearchFrame = QtWidgets.QFrame(self.headerframe)
        self.SearchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame.setObjectName("SearchFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SearchBar = QtWidgets.QLineEdit(self.SearchFrame)
        self.SearchBar.setObjectName("SearchBar")
        self.horizontalLayout_6.addWidget(self.SearchBar)
        self.SearchButton = QtWidgets.QPushButton(self.SearchFrame)
        self.SearchButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon11)
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_6.addWidget(self.SearchButton)
        self.horizontalLayout_2.addWidget(self.SearchFrame)
        self.frame = QtWidgets.QFrame(self.headerframe)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Profile_2 = QtWidgets.QPushButton(self.frame)
        self.Profile_2.setText("")
        self.Profile_2.setIcon(icon)
        self.Profile_2.setObjectName("Profile_2")
        self.horizontalLayout_5.addWidget(self.Profile_2)
        self.Notification = QtWidgets.QPushButton(self.frame)
        self.Notification.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Notification.setIcon(icon12)
        self.Notification.setObjectName("Notification")
        self.horizontalLayout_5.addWidget(self.Notification)
        self.horizontalLayout_2.addWidget(self.frame)
        self.Navigation = QtWidgets.QFrame(self.headerframe)
        self.Navigation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navigation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navigation.setObjectName("Navigation")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Navigation)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Minimise = QtWidgets.QPushButton(self.Navigation)
        self.Minimise.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/arrow-down-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimise.setIcon(icon13)
        self.Minimise.setObjectName("Minimise")
        self.horizontalLayout_4.addWidget(self.Minimise)
        self.Maximise = QtWidgets.QPushButton(self.Navigation)
        self.Maximise.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Maximise.setIcon(icon14)
        self.Maximise.setObjectName("Maximise")
        self.horizontalLayout_4.addWidget(self.Maximise)
        self.Quit = QtWidgets.QPushButton(self.Navigation)
        self.Quit.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Quit.setIcon(icon15)
        self.Quit.setObjectName("Quit")
        self.horizontalLayout_4.addWidget(self.Quit)
        self.horizontalLayout_2.addWidget(self.Navigation)
        self.verticalLayout.addWidget(self.headerframe)
        self.mainbody = QtWidgets.QFrame(self.mainbodcontainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy)
        self.mainbody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbody.setObjectName("mainbody")
        self.gridLayout = QtWidgets.QGridLayout(self.mainbody)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Viewer = QtWidgets.QWidget(self.mainbody)
        self.Viewer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Viewer.sizePolicy().hasHeightForWidth())
        self.Viewer.setSizePolicy(sizePolicy)
        self.Viewer.setObjectName("Viewer")
        self.gridLayout.addWidget(self.Viewer, 0, 1, 1, 1)
        self.Creator = QtWidgets.QWidget(self.mainbody)
        self.Creator.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Creator.sizePolicy().hasHeightForWidth())
        self.Creator.setSizePolicy(sizePolicy)
        self.Creator.setObjectName("Creator")
        self.gridLayout.addWidget(self.Creator, 0, 2, 1, 1)
        self.Editor = QtWidgets.QWidget(self.mainbody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Editor.sizePolicy().hasHeightForWidth())
        self.Editor.setSizePolicy(sizePolicy)
        self.Editor.setObjectName("Editor")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Editor)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.editorheader = QtWidgets.QFrame(self.Editor)
        self.editorheader.setMaximumSize(QtCore.QSize(16777215, 75))
        self.editorheader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editorheader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editorheader.setObjectName("editorheader")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.editorheader)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Charctereditselectlaber = QtWidgets.QLabel(self.editorheader)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Charctereditselectlaber.setFont(font)
        self.Charctereditselectlaber.setAlignment(QtCore.Qt.AlignCenter)
        self.Charctereditselectlaber.setIndent(1)
        self.Charctereditselectlaber.setObjectName("Charctereditselectlaber")
        self.horizontalLayout_9.addWidget(self.Charctereditselectlaber)
        self.verticalLayout_14.addWidget(self.editorheader)
        self.editorgrid = QtWidgets.QFrame(self.Editor)
        self.editorgrid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editorgrid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editorgrid.setObjectName("editorgrid")
        self.verticalLayout_14.addWidget(self.editorgrid)
        self.gridLayout.addWidget(self.Editor, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.mainbody)
        self.footer = QtWidgets.QFrame(self.mainbodcontainer)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Versionframe = QtWidgets.QFrame(self.footer)
        self.Versionframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Versionframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Versionframe.setObjectName("Versionframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Versionframe)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.VersionNo = QtWidgets.QLabel(self.Versionframe)
        self.VersionNo.setObjectName("VersionNo")
        self.verticalLayout_4.addWidget(self.VersionNo)
        self.horizontalLayout_3.addWidget(self.Versionframe, 0, QtCore.Qt.AlignBottom)
        self.Icon = QtWidgets.QFrame(self.footer)
        self.Icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Icon.setObjectName("Icon")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Icon)
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Box = QtWidgets.QPushButton(self.Icon)
        self.Box.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Box.setIcon(icon16)
        self.Box.setObjectName("Box")
        self.verticalLayout_3.addWidget(self.Box)
        self.horizontalLayout_3.addWidget(self.Icon, 0, QtCore.Qt.AlignBottom)
        self.sizeGrip = QtWidgets.QFrame(self.footer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(10, 10))
        self.sizeGrip.setMaximumSize(QtCore.QSize(10, 10))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_3.addWidget(self.sizeGrip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.mainbodcontainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.MenuToolbox.setCurrentIndex(2)
        self.CharacterCreator.clicked['bool'].connect(self.Viewer.hide)
        self.CharacterVierwe.clicked['bool'].connect(self.Creator.hide)
        self.menuButton.clicked['bool'].connect(self.slide_menu_container.show)
        self.CharacterEditor.clicked['bool'].connect(self.Viewer.hide)
        self.CharacterEditor.clicked['bool'].connect(self.Editor.show)
        self.CharacterVierwe.clicked['bool'].connect(self.Viewer.show)
        self.CharacterCreator.clicked['bool'].connect(self.Creator.show)
        self.CharacterVierwe.clicked['bool'].connect(self.Editor.hide)
        self.CharacterEditor.clicked['bool'].connect(self.Creator.hide)
        self.CharacterCreator.clicked['bool'].connect(self.Editor.hide)
        self.ExitMenu.clicked['bool'].connect(self.slide_menu_container.hide)
        self.Maximise.clicked['bool'].connect(MainWindow.showFullScreen)
        self.Minimise.clicked['bool'].connect(MainWindow.showMinimized)
        self.Quit.clicked['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DicedrakeLabel.setText(_translate("MainWindow", "DiceDrake"))
        self.Profile.setText(_translate("MainWindow", "Profile"))
        self.Friends.setText(_translate("MainWindow", "Friends"))
        self.Forum.setText(_translate("MainWindow", "Forum"))
        self.MenuToolbox.setItemText(self.MenuToolbox.indexOf(self.page), _translate("MainWindow", "Social Menu"))
        self.CharacterCreator.setText(_translate("MainWindow", "Create character"))
        self.CharacterEditor.setText(_translate("MainWindow", "Edit character"))
        self.CharacterVierwe.setText(_translate("MainWindow", "View character"))
        self.MenuToolbox.setItemText(self.MenuToolbox.indexOf(self.MainMenu), _translate("MainWindow", "Game menu"))
        self.Placeholder.setText(_translate("MainWindow", "Placeholder"))
        self.MenuToolbox.setItemText(self.MenuToolbox.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.ExitMenu.setText(_translate("MainWindow", "Exit"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.Charctereditselectlaber.setText(_translate("MainWindow", "Character Editor Selector"))
        self.VersionNo.setText(_translate("MainWindow", "Dicedrake PreAlpha1.05"))




























class Registration_Ui(QMainWindow):
    switch_window = QtCore.pyqtSignal(list)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.oldPos = self.pos()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 643)
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(440, 110, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title.setObjectName("Title")
        self.LoginButton = QtWidgets.QPushButton(Form, clicked= lambda: self.RegisterPressed())
        self.LoginButton.setGeometry(QtCore.QRect(460, 392, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 0), stop:1 rgba(170, 0, 0, 255));")
        self.LoginButton.setObjectName("LoginButton")
        self.Pictureframe = QtWidgets.QTextEdit(Form)
        self.Pictureframe.setGeometry(QtCore.QRect(100, 90, 331, 481))
        self.Pictureframe.setStyleSheet("border-radius:20px;\n"
"background-image: url(:/photos/Dragon.jpg);\n"
"color: rgb(255, 255, 255);")
        self.Pictureframe.setObjectName("Pictureframe")
        self.UserName = QtWidgets.QLineEdit(Form)
        self.UserName.setGeometry(QtCore.QRect(450, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255,255);")
        self.UserName.setObjectName("UserName")
        self.mainbody = QtWidgets.QTextEdit(Form)
        self.mainbody.setGeometry(QtCore.QRect(400, 110, 321, 441))
        self.mainbody.setStyleSheet("background-color: rgba(88, 6, 6, 230);\n"
"color:rgba(255,255,255,230);\n"
"border-radius:20px;")
        self.mainbody.setObjectName("mainbody")
        self.UserPass = QtWidgets.QLineEdit(Form)
        self.UserPass.setGeometry(QtCore.QRect(450, 280, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.UserPass.setFont(font)
        self.UserPass.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255,255);")
        self.UserPass.setObjectName("UserPass")
        self.mainbody.raise_()
        self.UserPass.raise_()
        self.Pictureframe.raise_()
        self.UserName.raise_()
        self.LoginButton.raise_()
        self.Title.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def RegisterPressed(self):
        con1=lite.connect('Dicedrake.db')
        cur1=con1.cursor()
        username = self.UserName.text()
        password = self.UserPass.text()
        cur1.execute("INSERT INTO Accounts (Username, Password) VALUES (?, ?)",
        (username, password))
        con1.commit()
        cur1.close()
        con1.close()
        print('Account registered')
        self.switch_window.emit(['Registered'])
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "Register to dicedrake"))
        self.LoginButton.setText(_translate("Form", "Register"))
        self.UserName.setPlaceholderText(_translate("Form", "Username"))
        self.UserPass.setPlaceholderText(_translate("Form", "Password"))





class Ui_Form(QMainWindow):
    switch_window = QtCore.pyqtSignal(list)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.oldPos = self.pos()
        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 670)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        Form.setStyleSheet("color: rgb(255, 255, 255);")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.mainbody = QtWidgets.QTextEdit(Form)
        self.mainbody.setGeometry(QtCore.QRect(340, 170, 321, 441))
        self.mainbody.setStyleSheet("background-color: rgba(88, 6, 6, 230);\n"
"color:rgba(255,255,255,230);\n"
"border-radius:20px;")
        self.mainbody.setObjectName("mainbody")
        self.Pictureframe = QtWidgets.QTextEdit(Form)
        self.Pictureframe.setGeometry(QtCore.QRect(60, 150, 331, 481))
        self.Pictureframe.setStyleSheet("border-radius:20px;\n"
"background-image: url(:/photos/Dragon.jpg);\n"
"color: rgb(255, 255, 255);")
        self.Pictureframe.setObjectName("Pictureframe")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(400, 200, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.registrationButton = QtWidgets.QPushButton(Form,clicked= lambda: self.RegisterPressed())
        self.registrationButton.setGeometry(QtCore.QRect(400, 510, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.registrationButton.setFont(font)
        self.registrationButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 0), stop:1 rgba(170, 0, 0, 255));")
        self.registrationButton.setObjectName("registrationButton")
        self.LoginButton = QtWidgets.QPushButton(Form, clicked= lambda: self.LoginPressed())
        self.LoginButton.setGeometry(QtCore.QRect(530, 510, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 0), stop:1 rgba(170, 0, 0, 255));")
        self.LoginButton.setObjectName("LoginButton")
        self.UserName = QtWidgets.QLineEdit(Form)
        self.UserName.setGeometry(QtCore.QRect(410, 300, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255,255);")
        self.UserName.setObjectName("UserName")
        self.UserPass = QtWidgets.QLineEdit(Form)
        self.UserPass.setGeometry(QtCore.QRect(410, 370, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.UserPass.setFont(font)
        self.UserPass.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255,255);")
        self.UserPass.setObjectName("UserPass")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def LoginPressed(self):
        con1=lite.connect('Dicedrake.db')
        cur1=con1.cursor()
        username = self.UserName.text()
        password = self.UserPass.text()
        PFound = False
        tries=0
        while PFound == False and tries != 3:
            print('entered while')
            for x in cur1.execute("SELECT Password FROM Accounts WHERE Username='"+(username)+"'"):
                print('entered for')
                if x[0]== password:
                    PFound = True
                    print(' user and password found')
            if PFound == True:
                print("Logged in!")
                self.switch_window.emit(["Login"])
            if PFound == False:
                print("Wrong!")
                tries=tries+1
                print(tries)
        if PFound is False:
            print('loop ignored or incorrect password or username')
            cur1.close()
            con1.close()
            
        
        
        

    def RegisterPressed(self):
        print ("Pending")
        self.switch_window.emit(["Register"])
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "login to dicedrake"))
        self.registrationButton.setText(_translate("Form", "register new user"))
        self.LoginButton.setText(_translate("Form", "Log in"))
        self.UserName.setPlaceholderText(_translate("Form", "Username"))
        self.UserPass.setPlaceholderText(_translate("Form", "Password"))


















#Dont need this -  just to show how to pass the text through different screens
class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text[1])
        layout.addWidget(self.label)

        self.label2 = QtWidgets.QLabel(text[2])
        layout.addWidget(self.label2)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)
               
        self.oldPos = self.pos()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()






















class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.ui = Ui_Form()
        self.ui.switch_window.connect(self.show_window_two)
        self.ui.show()

    def show_registration(self):
        self.rui = Registration_Ui()
        self.rui.switch_window.connect(self.show_window_two)
        self.rui.show()

    def show_main(self):
        self.main = Ui_MainWindow()
        self.main.switch_window.connect(self.show_window_two)
        self.main.show()
        

    #Dont need 'self.window_two' objects -  just to show how to pass the text through different screens
    def show_window_two(self, text):
        if text[0] == 'Register':
            self.ui.close()
            self.show_registration()
        elif text[0] == 'Login':
            self.ui.close()
            self.show_main()
            #can remove next line
            #self.window_two = WindowTwo(text)
            #can remove next line
            #self.window_two.show()
        elif text[0] == 'Registered':
            #uncomment next line to run main window when registered
            self.rui.close()
            self.show_main()
            #can remove next line
            #self.window_two = WindowTwo(text)
            #can remove next line
            #self.window_two.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())

