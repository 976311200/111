from PyQt5.QtWidgets import QFileDialog, QDateTimeEdit, QPushButton, QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5.QtCore import QDate
from prf_split import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.layout = QVBoxLayout()    #布局方式，H代表横向，V代表纵向，后面的

        self.pdf = "" # 建立一个保存路径的字符串
        self.label1 = QLabel("选择pdf")
        self.myButton1 = QPushButton(self)
        self.myButton1.setObjectName('mybutton1')
        self.myButton1.setText('浏览')
        self.myButton1.clicked.connect(self.fil)

        self.save_path = ""
        self.label5 = QLabel("保存路径")
        self.myButton2 = QPushButton(self)
        self.myButton2.setObjectName('mybutton2')
        self.myButton2.setText("浏览")
        self.myButton2.clicked.connect(self.dir)

        self.label2 = QLabel("开始页码")
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setObjectName('lineEdit')

        self.label3 = QLabel("结束页码")
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setObjectName('lineEdit')

        self.label4 = QLabel("开始执行")
        self.myButton3 = QPushButton(self)
        self.myButton3.setObjectName("myButton3")
        self.myButton3.setText("确认")
        self.myButton3.clicked.connect(self.run) # 调用self.down函数进行下载

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.myButton1)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.myButton2)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.lineEdit1)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.lineEdit2)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.myButton3)
        self.layout.setSpacing(25) # 设置布局
        self.setLayout(self.layout)  # 定义布局




    def run(self):
        self.start = self.lineEdit1.text()
        self.end = self.lineEdit2.text()
        split_pdf(start_page=int(self.start), end_page=int(self.end), pdf_dir=self.pdf, save_dir=self.out_dir)
        reply = QMessageBox.question(self, '分割已完成', '是否退出？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)  #修改默认的值
        if reply == QMessageBox.Yes:
            exit()


    def fil(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, "选取文件", "./", "PDF Files (*.pdf)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.pdf = filename
        print(self.pdf)
        self.myButton1.setText(self.pdf)


    def dir(self):
        directory = QFileDialog.getExistingDirectory(
            self, "选取文件夹", "./")  # 起始路径
        self.out_dir = directory
        self.myButton2.setText(self.out_dir)
        print(self.out_dir)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())