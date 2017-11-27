#include "pingpongpi_gui.h"
#include "ui_pingpongpi_gui.h"

PingPongPi_GUI::PingPongPi_GUI(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::PingPongPi_GUI)
{
    ui->setupUi(this);
}

PingPongPi_GUI::~PingPongPi_GUI()
{
    delete ui;
}
