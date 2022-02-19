from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QListView, QGroupBox, QLineEdit, QTextEdit, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget, QMessageBox
)

from .contacts_service import ContactsService


class MainWindow(QMainWindow):
    def __init__(self, contacts_service: ContactsService) -> None:
        super().__init__()

        self.contacts_service = contacts_service
        self.contacts_model = QStandardItemModel(self)
        self.current_contact = None

        self.initUi()
        self.initActions()
        self.refreshContacts()
    

    def initUi(self):
        self.contacts_list = QListView(self)
        self.contacts_list.setModel(self.contacts_model)

        # Contact details form elements
        contact_details = QGroupBox("Contact details", self)
        name_label = QLabel("Name", contact_details)
        self.name_edit = QLineEdit(contact_details)
        email_label = QLabel("Email", contact_details)
        self.email_edit = QLineEdit(contact_details)
        address_label = QLabel("Address", contact_details)
        self.address_edit = QLineEdit(contact_details)
        notes_label = QLabel("Notes", contact_details)
        self.notes_edit = QTextEdit(contact_details)

        # Contact details form layout
        details_layout = QVBoxLayout()
        details_layout.addWidget(name_label)
        details_layout.addWidget(self.name_edit)
        details_layout.addWidget(email_label)
        details_layout.addWidget(self.email_edit)
        details_layout.addWidget(address_label)
        details_layout.addWidget(self.address_edit)
        details_layout.addWidget(notes_label)
        details_layout.addWidget(self.notes_edit)

        contact_details.setLayout(details_layout)

        # Buttons
        self.quit_btn = QPushButton("Quit", self)
        self.quit_btn.setHidden(True)
        
        self.delete_btn = QPushButton("Delete", self)
        self.delete_btn.setDisabled(True)

        self.save_btn = QPushButton("Save", self)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.delete_btn)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_btn)
        # buttons_layout.addWidget(self.quit_btn)

        # Right column layout
        right_column = QVBoxLayout()
        right_column.addWidget(contact_details)
        right_column.addLayout(buttons_layout)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.contacts_list)
        main_layout.addLayout(right_column)

        # Main widget
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Toolbars and actions
        main_toolbar = self.addToolBar("Main")
        main_toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.new_contact_action = QAction(QIcon("contacts_app/icons/add.png"), "Add contact", self)
        self.new_contact_action.setIconText("Add contact")
        self.new_contact_action.setToolTip("Add a new contact")

        self.quit_action = QAction(QIcon("contacts_app/icons/logout.png"), "Quit", self)
        self.quit_action.setIconText("Quit")

        main_toolbar.addAction(self.new_contact_action)
        main_toolbar.addSeparator()
        main_toolbar.addAction(self.quit_action)

        # Menubar
        main_menu = self.menuBar().addMenu("Contacts")
        main_menu.addAction(self.new_contact_action)
        main_menu.addSeparator()
        main_menu.addAction(self.quit_action)

        self.resize(800, 600)
        self.setWindowTitle("My Contacts")

    def initActions(self):
        self.quit_btn.clicked.connect(self.quit)
        self.quit_action.triggered.connect(self.quit)

        self.save_btn.clicked.connect(self.saveClicked)
        self.delete_btn.clicked.connect(self.deleteClicked)
        self.contacts_list.activated.connect(self.contactActivated)
        self.contacts_list.clicked.connect(self.contactActivated)
        self.new_contact_action.triggered.connect(self.newContactActivated)

    def refreshContacts(self):
        contacts = self.contacts_service.get_contacts()
        self.contacts_model.clear()
        for contact in contacts:
            name = QStandardItem(contact["name"])
            name.setData(contact["id"])

            email = QStandardItem(contact["email"])
            email.setData(contact["id"])

            self.contacts_model.appendRow([name, email])

    def newContactActivated(self):
        self.current_contact = None
        self.contacts_list.clearSelection()
        self.clearFields()
        self.delete_btn.setDisabled(True)
        self.name_edit.setFocus()

    def contactActivated(self, index):
        contact_id = self.contacts_model.itemFromIndex(index).data()
        self.current_contact = self.contacts_service.get_contact(contact_id)

        self.name_edit.setText(self.current_contact["name"])
        self.email_edit.setText(self.current_contact["email"])
        self.address_edit.setText(self.current_contact["address"])
        self.notes_edit.setMarkdown(self.current_contact["notes"])

        self.delete_btn.setDisabled(False)

    def saveClicked(self):
        is_edit = False if self.current_contact is None else True

        if not is_edit:
            self.current_contact = {}

        self.current_contact["name"] = self.name_edit.text()
        self.current_contact["email"] = self.email_edit.text()
        self.current_contact["address"] = self.address_edit.text()
        self.current_contact["notes"] = self.notes_edit.toMarkdown()

        if is_edit:
            self.contacts_service.update(self.current_contact)
            QMessageBox.information(self, "Updated", "Your contact has been successfully updated")
        else:
            self.contacts_service.create(self.current_contact)
            QMessageBox.information(self, "Created", "Your contact has been successfully created")

        self.refreshContacts()

    def deleteClicked(self):
        response = QMessageBox.question(
            self, 
            "Delete contact", 
            "Dou you really want to delete {} contact".format(self.current_contact["name"])
        )

        if response != QMessageBox.StandardButton.Yes:
            return

        self.contacts_service.delete(self.current_contact)
        self.current_contact = None

        self.clearFields()

        self.refreshContacts()

        QMessageBox.information(self, "Removed", "Contact has been successfully removed")

    def quit(self):
        QApplication.instance().quit()

    def clearFields(self):
        self.name_edit.clear()
        self.email_edit.clear()
        self.address_edit.clear()
        self.notes_edit.clear()
