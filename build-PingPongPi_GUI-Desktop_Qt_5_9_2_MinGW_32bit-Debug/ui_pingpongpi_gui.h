/********************************************************************************
** Form generated from reading UI file 'pingpongpi_gui.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PINGPONGPI_GUI_H
#define UI_PINGPONGPI_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PingPongPi_GUI
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_5;
    QLabel *PlayerScoreLabel0;
    QSpacerItem *horizontalSpacer_2;
    QLabel *PlayerScoreLabel1;
    QSpacerItem *horizontalSpacer_6;
    QHBoxLayout *horizontalLayout_3;
    QSpacerItem *horizontalSpacer_3;
    QLabel *PlayerNameLabel0;
    QSpacerItem *horizontalSpacer;
    QLabel *PlayerNameLabel1;
    QSpacerItem *horizontalSpacer_4;
    QMenuBar *menuBar;
    QMenu *menuPingPongPiScoreboard;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *PingPongPi_GUI)
    {
        if (PingPongPi_GUI->objectName().isEmpty())
            PingPongPi_GUI->setObjectName(QStringLiteral("PingPongPi_GUI"));
        PingPongPi_GUI->resize(1000, 1060);
        PingPongPi_GUI->setMaximumSize(QSize(16777215, 16777215));
        PingPongPi_GUI->setAutoFillBackground(false);
        centralWidget = new QWidget(PingPongPi_GUI);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy);
        centralWidget->setMinimumSize(QSize(0, 0));
        centralWidget->setMaximumSize(QSize(100000, 100000));
        QFont font;
        font.setFamily(QStringLiteral("Comic Sans MS"));
        centralWidget->setFont(font);
        centralWidget->setAutoFillBackground(false);
        gridLayout_2 = new QGridLayout(centralWidget);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_5);

        PlayerScoreLabel0 = new QLabel(centralWidget);
        PlayerScoreLabel0->setObjectName(QStringLiteral("PlayerScoreLabel0"));
        PlayerScoreLabel0->setMinimumSize(QSize(150, 150));
        QFont font1;
        font1.setPointSize(100);
        font1.setBold(true);
        font1.setWeight(75);
        PlayerScoreLabel0->setFont(font1);
        PlayerScoreLabel0->setAlignment(Qt::AlignHCenter|Qt::AlignTop);
        PlayerScoreLabel0->setWordWrap(false);

        horizontalLayout->addWidget(PlayerScoreLabel0);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        PlayerScoreLabel1 = new QLabel(centralWidget);
        PlayerScoreLabel1->setObjectName(QStringLiteral("PlayerScoreLabel1"));
        PlayerScoreLabel1->setMinimumSize(QSize(150, 150));
        PlayerScoreLabel1->setFont(font1);
        PlayerScoreLabel1->setAlignment(Qt::AlignHCenter|Qt::AlignTop);
        PlayerScoreLabel1->setWordWrap(false);

        horizontalLayout->addWidget(PlayerScoreLabel1);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_6);


        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_3);

        PlayerNameLabel0 = new QLabel(centralWidget);
        PlayerNameLabel0->setObjectName(QStringLiteral("PlayerNameLabel0"));
        PlayerNameLabel0->setMinimumSize(QSize(150, 150));
        QFont font2;
        font2.setPointSize(40);
        font2.setBold(true);
        font2.setUnderline(true);
        font2.setWeight(75);
        PlayerNameLabel0->setFont(font2);
        PlayerNameLabel0->setAlignment(Qt::AlignCenter);
        PlayerNameLabel0->setWordWrap(false);

        horizontalLayout_3->addWidget(PlayerNameLabel0);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        PlayerNameLabel1 = new QLabel(centralWidget);
        PlayerNameLabel1->setObjectName(QStringLiteral("PlayerNameLabel1"));
        PlayerNameLabel1->setMinimumSize(QSize(150, 150));
        PlayerNameLabel1->setFont(font2);
        PlayerNameLabel1->setAlignment(Qt::AlignCenter);
        PlayerNameLabel1->setWordWrap(false);

        horizontalLayout_3->addWidget(PlayerNameLabel1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_4);


        gridLayout->addLayout(horizontalLayout_3, 0, 0, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        PingPongPi_GUI->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(PingPongPi_GUI);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1000, 21));
        menuPingPongPiScoreboard = new QMenu(menuBar);
        menuPingPongPiScoreboard->setObjectName(QStringLiteral("menuPingPongPiScoreboard"));
        PingPongPi_GUI->setMenuBar(menuBar);
        mainToolBar = new QToolBar(PingPongPi_GUI);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(mainToolBar->sizePolicy().hasHeightForWidth());
        mainToolBar->setSizePolicy(sizePolicy1);
        PingPongPi_GUI->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(PingPongPi_GUI);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        PingPongPi_GUI->setStatusBar(statusBar);

        menuBar->addAction(menuPingPongPiScoreboard->menuAction());

        retranslateUi(PingPongPi_GUI);

        QMetaObject::connectSlotsByName(PingPongPi_GUI);
    } // setupUi

    void retranslateUi(QMainWindow *PingPongPi_GUI)
    {
        PingPongPi_GUI->setWindowTitle(QApplication::translate("PingPongPi_GUI", "PingPongPi_GUI", Q_NULLPTR));
        PlayerScoreLabel0->setText(QApplication::translate("PingPongPi_GUI", "0", Q_NULLPTR));
        PlayerScoreLabel1->setText(QApplication::translate("PingPongPi_GUI", "0", Q_NULLPTR));
        PlayerNameLabel0->setText(QApplication::translate("PingPongPi_GUI", "Player 1", Q_NULLPTR));
        PlayerNameLabel1->setText(QApplication::translate("PingPongPi_GUI", "Player 2", Q_NULLPTR));
        menuPingPongPiScoreboard->setTitle(QApplication::translate("PingPongPi_GUI", "PingPongPiScoreboard", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class PingPongPi_GUI: public Ui_PingPongPi_GUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PINGPONGPI_GUI_H
