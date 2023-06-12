import sys
from functools import lru_cache
from PyQt5.QtCore import QUrl, Qt, QStringListModel, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QCompleter, QWidget, QToolBar, QAction, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QIcon
import csv

@lru_cache
def get_completions():
    # read the CSV file and extract the Root domain column
    with open('url_list.csv', 'r') as f:
        reader = csv.DictReader(f)
        urls = [row['Domain'] for row in reader]
    return urls

class BrowserTab(QWebEngineView):
    def __init__(self, url):
        super().__init__()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setText(url.toString())
        self.setUrl(url)
        self.titleChanged.connect(self.update_tab_title)
        self.loadStarted.connect(self.page_load_started)
        self.loadFinished.connect(self.page_load_finished)

        self.history = QWebEngineHistory()
        self.history.setDefaultItemLimit(100)
        self.history.changed.connect(self.update_navigation_buttons)
        self.history.currentItemChanged.connect(self.update_url_bar)


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open("style_v2.css", "r").read())

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.toolbar = QToolBar("Navigation")
        self.addToolBar(self.toolbar)

        self.browser = BrowserTab(QUrl.fromLocalFile('D:/Study/Python/browser/home.html'))
        self.tabs.addTab(self.browser, "Google")
        self.current_tab = self.browser
        self.browser.page().urlChanged.connect(self.update_url_bar)

        self.back_button = QAction(QIcon('back-arrow.png'), "Back", self)
        self.back_button.triggered.connect(self.current_tab.back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction(QIcon('forward-arrow.png'), "Forward", self)
        self.forward_button.triggered.connect(self.current_tab.forward)
        self.toolbar.addAction(self.forward_button)

        self.reload_button = QAction(QIcon('reload.png'), "Reload", self)
        self.reload_button.triggered.connect(self.current_tab.reload)
        self.toolbar.addAction(self.reload_button)

        self.stop_button = QAction(QIcon('cross.png'), "Stop", self)
        self.toolbar.addAction(self.stop_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.url_bar)
        # Create a completer object with a string list of URLs
        # create a completer object with the list of URLs
        url_completer = QCompleter(get_completions())

        # use a QStringListModel as the model for the completer
        model = QStringListModel(get_completions())
        url_completer.setModel(model)

        # update the model when the text in the QLineEdit changes
        self.url_bar.textChanged.connect(lambda text: model.setStringList([url for url in get_completions() if len(text) > 2 and text in url]))

        # set the completer object to the URL bar
        self.url_bar.setCompleter(url_completer)

        url_completer.activated.connect(self.navigate_to_url)

        self.new_tab_button = QPushButton(QIcon('add.png'), '')
        self.new_tab_button.clicked.connect(self.add_new_tab)
        self.toolbar.addWidget(self.new_tab_button)

        self.tabs.currentChanged.connect(self.update_tab)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.update_tab)
        self.browser.page().urlChanged.connect(self.update_url_bar)
        self.browser.loadProgress.connect(self.handle_load_progress)

        self.setWindowTitle("Py Browser")

    def navigate_to_url(self, q):
        url = q
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        if not url.startswith("http://www.") and not url.startswith("https://www."):
            url = url.replace("http://", "http://www.")
            url = url.replace("https://", "https://www.")
        qurl = QUrl(url)
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ShiftModifier:
            browser = BrowserTab(qurl)
            self.tabs.addTab(browser, browser.page().title())
            self.tabs.setCurrentWidget(browser)
        else:
            self.current_tab.setUrl(qurl)
            self.url_bar.setText(qurl.toString())


    def update_url_bar(self, q):
        if q == QUrl.fromLocalFile('D:/Study/Python/browser/home.html'):
            self.url_bar.setText('')
        else:
            self.url_bar.setText(q.toString())

    def handle_load_progress(self, progress):
        if progress == 100:
            print("Page loaded successfully")

    def update_tab(self):
        self.current_tab = self.tabs.currentWidget()

    def close_current_tab(self, index):
        if self.tabs.count() == 1:
            sys.exit()
        self.tabs.removeTab(index)

    def add_new_tab(self):
        browser = BrowserTab(QUrl.fromLocalFile('D:/Study/Python/browser/home.html'))
        self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentWidget(browser)
        self.update_tab()

    def update_tab(self):
        self.current_tab = self.tabs.currentWidget()
        self.url_bar = self.current_tab.url_bar
        self.history = self.current_tab.history

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
