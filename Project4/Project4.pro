TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp


INCLUDEPATH += /usr/local/Cellar/armadillo/7.400.2/include
LIBS += -armadillo -lblas -llapack
