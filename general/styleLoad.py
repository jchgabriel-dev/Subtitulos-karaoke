from PyQt5.QtCore import QFile, QTextStream

class StyleLoad:
    def cargar_css(self, archivo_css):
        css_file = QFile(archivo_css)
        if css_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(css_file)
            style_sheet = stream.readAll()
            self.setStyleSheet(style_sheet)