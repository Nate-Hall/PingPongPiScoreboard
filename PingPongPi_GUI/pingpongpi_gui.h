#ifndef PINGPONGPI_GUI_H
#define PINGPONGPI_GUI_H

#include <QMainWindow>

namespace Ui {
class PingPongPi_GUI;
}

class PingPongPi_GUI : public QMainWindow
{
    Q_OBJECT

public:
    explicit PingPongPi_GUI(QWidget *parent = 0);
    ~PingPongPi_GUI();
    AddLabels();

private:
    Ui::PingPongPi_GUI *ui;
};

#endif // PINGPONGPI_GUI_H
