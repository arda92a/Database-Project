from PyQt6 import QtWidgets

class UIHelper:
    @staticmethod
    def update_combo_box(combo_box, items):
        combo_box.clear()
        combo_box.addItems(items)

    @staticmethod
    def update_table(table_widget, data):
        table_widget.setRowCount(0)
        for row_number, row_data in enumerate(data):
            table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table_widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    @staticmethod
    def show_message(parent, message_type, title, message):
        if message_type == 'info':
            QtWidgets.QMessageBox.information(parent, title, message)
        elif message_type == 'warning':
            QtWidgets.QMessageBox.warning(parent, title, message)
        elif message_type == 'error':
            QtWidgets.QMessageBox.critical(parent, title, message)
        elif message_type == 'question':
            return QtWidgets.QMessageBox.question(parent, title, message, QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        elif message_type == 'input':
            return QtWidgets.QInputDialog.getText(parent, title, message)