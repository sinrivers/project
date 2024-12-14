from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from controller import Controller
import os

class TVGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Television")
        self.setGeometry(100, 100, 533, 400)  # Window width matches 4:3 aspect ratio for 400 height

        # Image display
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(533, 400)  # Ensure 4:3 aspect ratio (width:height = 4:3)

        # Volume bar overlay
        self.volume_label = QLabel(self)
        self.volume_label.setAlignment(Qt.AlignCenter)
        self.volume_label.setStyleSheet("color: green; font-family: arial;")
        self.volume_label.setFixedWidth(533)

        # Status label
        self.status_label = QLabel("Power: OFF", self)

        # Channel label
        self.channel_label = QLabel("Channel: 1", self)

        # Layout for buttons
        layout = QVBoxLayout()

        # Power Button
        self.power_button = QPushButton("Power")
        self.power_button.clicked.connect(self.controller.toggle_power)

        # Channel controls
        self.channel_up = QPushButton("Channel +")
        self.channel_down = QPushButton("Channel -")

        # Volume controls
        self.volume_up = QPushButton("Volume +")
        self.volume_down = QPushButton("Volume -")

        self.channel_up.clicked.connect(self.controller.channel_up)
        self.channel_down.clicked.connect(self.controller.channel_down)
        self.volume_up.clicked.connect(self.controller.volume_up)
        self.volume_down.clicked.connect(self.controller.volume_down)

        # Adding widgets to the layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.volume_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.channel_label)
        layout.addWidget(self.power_button)
        layout.addWidget(self.channel_up)
        layout.addWidget(self.channel_down)
        layout.addWidget(self.volume_up)
        layout.addWidget(self.volume_down)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.update_ui(self.controller.tv.get_state())

    def update_ui(self, state):
        # Update power status
        self.status_label.setText(f"Power: {'ON' if state['status'] else 'OFF'}")

        # Enable/disable controls based on power status
        is_power_on = state['status']
        self.channel_up.setEnabled(is_power_on)
        self.channel_down.setEnabled(is_power_on)
        self.volume_up.setEnabled(is_power_on)
        self.volume_down.setEnabled(is_power_on)

        # Update channel info
        self.channel_label.setText(f"Channel: {state['channel']}")

        # Update image
        if is_power_on:
            image_path = os.path.join(os.getcwd(), f"image{state['channel']}.jpg")
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(533, 400, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
                self.image_label.setPixmap(pixmap)
            else:
                self.image_label.setText("No Image Found")
                self.image_label.setPixmap(QPixmap())
        else:
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText("TV is OFF")

        # Update volume bar
        if is_power_on and not state['muted']:
            volume_bars = int(state['volume'] / 10)  # One '=' for every 10 units of volume
            self.volume_label.setText(f"[{'=' * volume_bars}{' ' * (10 - volume_bars)}]")
        else:
            self.volume_label.setText("")  # Clear volume bar if TV is off or muted

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    controller = Controller(None)
    view = TVGUI(controller=controller)
    controller.view = view
    view.show()
    sys.exit(app.exec())
