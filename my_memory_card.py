#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)

app=QApplication([])

linux=QWidget()
linux.setWindowTitle('Memory Card')
linux.resize(400,400)

baton=QPushButton('?????')
baton2=QLabel('?????')

radio=QGroupBox('yo')
radio_baton=QRadioButton('?????')
radio_baton2=QRadioButton('?????')
radio_baton3=QRadioButton('?????')
radio_baton4=QRadioButton('?????')

layouto1=QHBoxLayout()
layouto2=QVBoxLayout()
layouto3=QVBoxLayout()
layouto2.addWidget(radio_baton)
layouto2.addWidget(radio_baton2)
layouto3.addWidget(radio_baton3)
layouto3.addWidget(radio_baton4)

layouto1.addLayout(layouto2)
layouto1.addLayout(layouto3)

radio.setLayout(layouto1)

spec_layouto1=QHBoxLayout()
spec_layouto2=QHBoxLayout()
spec_layouto3=QHBoxLayout()

spec_layouto1.addWidget(baton, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
spec_layouto2.addWidget(radio)

spec_layouto3.addStretch(1)
spec_layouto3.addWidget(baton, stretch=2)
spec_layouto3.addStretch(1)

union_layouto=QVBoxLayout()

union_layouto.addLayout(spec_layouto1, stretch=2)
union_layouto.addLayout(spec_layouto2, stretch=8)
union_layouto.addStretch(1)
union_layouto.addLayout(spec_layouto3, stretch=1)
union_layouto.addStretch(1)
union_layouto.setSpacing(5)

linux.setLayout(union_layouto)
linux.show()
app.exec()