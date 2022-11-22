import os
import sys
from mutagen.mp3 import MP3
import json
from pydub import AudioSegment
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QScrollArea, \
    QInputDialog, QMessageBox, QFileDialog, QLabel
from ui.mpManager import Ui_Dialog
from ui.edit_w import Ui_Form
from ui.sspw import Ui_Form2
from ui.queue_ui import QueueWindow

# скрипт для поиска логических дисков на компьютере
drives = [f'{d}:' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{d}:')]
# создание файла кэша если он был удален
if not os.path.isfile('cache//player_cache.json'):
    with open('cache//player_cache.json', 'w') as file:
        file.write('{}')

sls = r' \ '.strip()


# главное окно
class MyApp(QMainWindow, Ui_Dialog):
    def __init__(self):
        self.drives = []
        self.last_drives = []
        self.queue_w = None
        self.music_files = [[os.path.join(root, f) for f in files] for root, dirs, files in os.walk('sample_audio')][0]
        self.files_group = []
        self.last_drives_search = {}
        self.trakDir = ''
        for d in drives:
            self.last_drives_search[d] = None
        self.fileExt = '.mp3'
        self.fileSize = 1
        super().__init__()
        self.setupUi(self)
        self.on_pause = False
        self.ed = None
        self.setWindowTitle('mp3 manager')
        self.OutView = QScrollArea(self)
        self.OutView.setGeometry(QRect(10, 100, 351, 251))
        self.start.clicked.connect(self.search)
        self.progressBar.hide()
        self.play.clicked.connect(self.playing)
        self.load.clicked.connect(self.loading)
        self.open.clicked.connect(self.open_on_explorer)
        self.edit.clicked.connect(self.edit_window)
        self.que.clicked.connect(self.call_qw)
        self.change_bck.clicked.connect(self.change_background)
        self.reset_bck.clicked.connect(self.reset_background)
        self.group = []
        self.spinBox.setValue(self.fileSize)
        for i in range(len(drives)):
            self.group.append((QCheckBox(drives[i], self)))
            self.group[i].move(490, 170 + i * 30)
        self.group[0].setChecked(True)
        self.play.hide()
        self.open.hide()
        self.edit.hide()
        self.media_player = QMediaPlayer()
        self.recompil_outw()
        self.search_first_start = True
        self.label_im = None

    # поиск файлов .mp3
    def search(self):
        if self.search_first_start:
            self.music_files.clear()
            self.search_first_start = False
        with open('cache//player_cache.json') as f:
            cache = json.load(f)
        self.drives.clear()
        for btn in self.group:
            if btn.isChecked():
                self.drives.append(btn.text())
        if not self.drives:
            self.group[0].setChecked(True)
            self.drives.append(drives[0])
        self.start.hide()
        self.fileSize = self.spinBox.value()
        self.progressBar.show()
        self.progressBar.setValue(0)
        count = 0
        i = 0
        for drive in self.drives:
            if drive in self.last_drives and self.last_drives_search[drive] == self.fileSize * 1024 ** 2:
                continue
            for drv, lnght in cache.items():
                if drive == drv:
                    print(drive, 'from cache', lnght)
                    count += lnght
                    break
            else:
                c = len([x[0] for x in os.walk(drive + sls)])
                count += c
                cache[drive] = c
        for drive in self.drives:
            if drive in self.last_drives and self.last_drives_search[drive] == self.fileSize * 1024 ** 2:
                continue
            else:
                self.last_drives.append(drive)
                self.last_drives_search[drive] = self.fileSize * 1024 ** 2
                self.music_files = list(filter(lambda x: x[0] != drive[0], self.music_files))
            self.music_files.append(f'{drive[:-1]}----------------------------------------------------------:')
            dir_i = 0
            for root, dirs, files in os.walk(drive + sls):
                i += 1
                dir_i += 1
                for f in files:
                    if f.split('.')[-1] == 'mp3':
                        filename = os.path.join(root, f)
                        if os.path.getsize(filename) >= self.fileSize * 1024 ** 2:
                            self.music_files.append(filename)
                self.progressBar.setValue(round(i / count * 100))
            if dir_i != int(cache[drive]):
                cache[drive] = dir_i
        self.progressBar.hide()
        self.recompil_outw()
        self.load.show()
        self.trakname.setText('No file choiced')
        self.trakname.show()
        self.start.show()
        with open("cache//player_cache.json", "w") as write_file:
            json.dump(cache, write_file)

    def loading(self):
        self.on_pause = False
        for btn in self.files_group:
            if btn.isChecked():
                self.trakDir = btn.text()
                break
        if self.trakDir:
            name_mp = self.trakDir[self.trakDir.rfind(sls) + 1: self.trakDir.find('.mp3')]
            self.trakname.setText(name_mp)
            self.play.setText('Play')
            self.play.show()
            self.open.show()
            self.edit.show()

    def playing(self):
        if self.play.text() == 'Play':
            if self.on_pause:
                self.on_pause = False
            else:
                url = QUrl.fromLocalFile(self.trakDir)
                content = QMediaContent(url)
                self.media_player.setMedia(content)
            self.media_player.play()
            self.play.setText('Pause')
        else:
            self.on_pause = True
            self.play.setText('Play')
            self.media_player.pause()

    def open_on_explorer(self):
        os.system(f'explorer.exe /select, {self.trakDir}')

    # открывает окно Edit
    def edit_window(self):
        self.ed = Editor(td=self.trakDir, par=self)
        self.ed.show()
        self.media_player.stop()

    def recompil_outw(self):
        self.files_group = []
        layout = QVBoxLayout()
        self.OutView = QScrollArea(self)
        self.OutView.setGeometry(QRect(10, 100, 351, 251))
        for i, el in enumerate(self.music_files):
            button = QRadioButton(el, self)
            button.resize(300, 30)
            layout.addWidget(button, i)
            if '----------------------------------------------------------:' not in el:
                self.files_group.append(button)
        w = QWidget()
        w.setLayout(layout)
        self.OutView.setWidget(w)
        self.OutView.show()
        self.trakDir = ''
        self.trakname.setText('')
        self.play.hide()
        self.open.hide()
        self.edit.hide()

    def change_background(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        if not fname:
            return
        image = QImage(fname).scaled(QSize(568, 515))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image))
        self.setPalette(palette)
        self.label_im = QLabel(self)
        self.label_im.setGeometry(0, 0, 568, 515)

    def reset_background(self):
        palette = QPalette()
        self.setPalette(palette)
        self.label_im = QLabel('', self)

    # открывает окно проигрывателя
    def call_qw(self):
        self.queue_w = Queue_Window(self.music_files)
        self.queue_w.show()


# окно для редактирования
class Editor(QMainWindow, Ui_Form):
    def __init__(self, par, td=''):
        super().__init__()
        self.setupUi(self)
        self.trackDir = td
        self.setWindowTitle('Editor')
        self.main_w = par
        self.w = None
        try:
            self.lenght = int(MP3(self.trackDir).info.length)
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()
            return
        self.rename_b.clicked.connect(self.rename)
        self.delete_b.clicked.connect(self.delete)
        self.copy_b.clicked.connect(self.copy)
        self.end_scroll.setValue(100)
        self.start_scroll.valueChanged.connect(self.change_count1)
        self.end_scroll.valueChanged.connect(self.change_count2)
        self.cut_b.clicked.connect(self.cut)
        self.speed_b.clicked.connect(self.call_for_w)
        minutes = str(self.lenght // 60)
        seconds = str(self.lenght % 60)
        if len(seconds) == 1:
            seconds = '0' + seconds
        self.label_end.setText(minutes + ':' + seconds)

    def rename(self):
        try:
            txt = self.trackDir[self.trackDir.rfind(sls) + 1: self.trackDir.find('.mp3')]
            new_name, ok = QInputDialog.getText(self, "подтверждение", "введите новое имя файла", text=txt)

            if ok:
                new_name = self.trackDir[:self.trackDir.rfind(sls) + 1] + new_name + '.mp3'
                os.rename(self.trackDir, new_name)
                self.main_w.music_files[self.main_w.music_files.index(self.trackDir)] = new_name
                self.main_w.recompil_outw()
                self.trackDir = new_name
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()

    def delete(self):
        try:
            msg = QMessageBox.question(self, 'точно?', 'Это удалит файл с компьютера', QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.Yes:
                os.remove(self.trackDir)
                del self.main_w.music_files[self.main_w.music_files.index(self.trackDir)]
                self.main_w.recompil_outw()
                self.close()
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()

    def copy(self):
        try:
            with open(self.trackDir, 'rb') as f:
                old_b = bytes(f.read())
            name_mp = self.trackDir[self.trackDir.rfind(sls) + 1: self.trackDir.find('.mp3')]
            fname = QFileDialog.getExistingDirectory(self, "выберите папку для сохранения",
                                                     self.trackDir[:self.trackDir.rfind(sls) + 1]) + '/'
            fname = ''.join([i if i != '/' else sls for i in fname])
            if not fname:
                return
            with open(fname + name_mp + '_copy' + '.mp3', 'wb') as f:
                f.write(old_b)
            if fname[0] + '----------------------------------------------------------:' in self.main_w.music_files:
                ind = self.main_w.music_files.index(fname[0] +
                                                    '----------------------------------------------------------:')
                self.main_w.music_files.insert(ind + 1, fname + name_mp + '_copy' + '.mp3')
            else:
                self.main_w.music_files.append(fname[0] + '----------------------------------------------------------:')
                self.main_w.music_files.append(fname + name_mp + '_copy' + '.mp3')
            self.main_w.recompil_outw()
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()

    def change_count1(self):
        if self.start_scroll.value() >= self.end_scroll.value():
            self.start_scroll.setValue(self.end_scroll.value() - 1)
        new_lenght = int(self.lenght / 100 * self.start_scroll.value())
        minutes = str(new_lenght // 60)
        seconds = str(new_lenght % 60)
        if len(seconds) == 1:
            seconds = '0' + seconds
        self.label_start.setText(minutes + ':' + seconds)

    def change_count2(self):
        if self.end_scroll.value() <= self.start_scroll.value():
            self.end_scroll.setValue(self.start_scroll.value() + 1)
        new_lenght = int(self.lenght / 100 * self.end_scroll.value())
        minutes = str(new_lenght // 60)
        seconds = str(new_lenght % 60)
        if len(seconds) == 1:
            seconds = '0' + seconds
        self.label_end.setText(minutes + ':' + seconds)

    def cut(self):
        try:
            msg = QMessageBox.question(self, 'подтверждение', 'Обрезать?', QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.No:
                return
            start = int(self.lenght / 100 * self.start_scroll.value()) * 1000
            end = int(self.lenght / 100 * self.end_scroll.value()) * 1000
            song = AudioSegment.from_mp3(self.trackDir)
            song = song[start:end]
            name = self.trackDir[:self.trackDir.rfind('.mp3')] + '_cutted.mp3'
            song.export(name, format='mp3')
            self.main_w.music_files.insert(self.main_w.music_files.index(self.trackDir) + 1, name)
            self.main_w.recompil_outw()
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()

    # открывает окно Set_speed
    def call_for_w(self):
        self.w = Set_speed_window(par=self)
        self.w.show()

    def set_speed(self, speed):
        try:
            if speed == 1.0:
                return
            song = AudioSegment.from_mp3(self.trackDir)
            new = song._spawn(song.raw_data, overrides={"frame_rate": int(song.frame_rate * speed)})
            name = self.trackDir[:self.trackDir.rfind('.mp3')] + ('_slowed.mp3' if speed < 1.0 else '_fastered.mp3')
            new.export(name, format='mp3')
            self.main_w.music_files.insert(self.main_w.music_files.index(self.trackDir) + 1, name)
            self.main_w.recompil_outw()
        except Exception as e:
            print('У разработчиков отклонения:\n', e, sep='')
            QMessageBox.critical(self, 'голову себе сломай', 'Выбранный файл был поврежден или переименнован извне',
                                 QMessageBox.Ok)
            self.close()


# Окно с ползунком дли изменения скорости, запускает Editor.set_speed с float числом скорости
class Set_speed_window(QMainWindow, Ui_Form2):
    def __init__(self, par):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('get speed')
        self.par = par
        self.ok_b.clicked.connect(self.ok)
        self.cancel_b.clicked.connect(self.cancel)
        self.verticalSlider.valueChanged.connect(self.set_txt)
        self.verticalSlider.setValue(10)
        self.value = '1.0'

    def ok(self):
        self.close()
        self.par.set_speed(float(self.value))

    def cancel(self):
        self.close()

    def set_txt(self):
        val = str(self.verticalSlider.value())
        if val == '0':
            self.verticalSlider.setValue(1)
            val = '1'
        if int(val) < 10:
            val = '0' + val
        self.value = val[0] + '.' + val[1]
        self.label.setText(self.value + 'x')


# окно проигрывателя
class Queue_Window(QMainWindow, QueueWindow):
    def __init__(self, files):
        super().__init__()
        self.setupUi(self)
        self.btn_group = []
        self.ac_files = []
        self.label = None
        self.change_files = False
        self.music_files = files.copy()
        self.music_files.insert(0, 'Add all')
        self.load_b.clicked.connect(self.load)
        self.prew_b.clicked.connect(self.prew)
        self.next_b.clicked.connect(self.next)
        self.play_b.clicked.connect(self.play)
        self.change_b.clicked.connect(self.change_bg)
        self.rem_b.clicked.connect(self.remove_bg)
        self.media_player = QMediaPlayer()
        layout = QVBoxLayout()
        for i, el in enumerate(self.music_files):
            button = QCheckBox(el, self)
            button.resize(300, 30)
            layout.addWidget(button, i)
            if '----------------------------------------------------------:' not in el and el != 'Add all':
                self.btn_group.append(button)
            else:
                button.stateChanged.connect(self.add_all)
        w = QWidget()
        w.setLayout(layout)
        self.outw.setWidget(w)
        self.outw.show()

    def add_all(self, state):
        if self.sender().text() != 'Add all':
            d = self.sender().text()[0]
            for elem in self.btn_group:
                if elem.text().startswith(d):
                    if state == Qt.Checked:
                        elem.setChecked(True)
                    else:
                        elem.setChecked(False)
        else:
            for elem in self.btn_group:
                if state == Qt.Checked:
                    elem.setChecked(True)
                else:
                    elem.setChecked(False)

    def load(self):
        self.change_files = True
        self.play_b.setText('play')
        self.ac_files.clear()
        for elem in self.btn_group:
            if elem.isChecked():
                self.ac_files.append(elem.text())
        if not self.ac_files:
            return
        name_mp1 = self.ac_files[0][self.ac_files[0].rfind(sls) + 1:
                                    self.ac_files[0].find('.mp3')]
        self.this_l.setText('this: ' + name_mp1)
        self.next_l.setText('')
        self.prew_l.setText('')
        if len(self.music_files) > 1:
            name_mp2 = self.ac_files[1][self.ac_files[1].rfind(sls) + 1:
                                        self.ac_files[1].find('.mp3')]
            self.next_l.setText('next: ' + name_mp2)

    def prew(self):
        if self.media_player.playlist().currentIndex() == 0:
            return
        self.media_player.playlist().previous()

    def next(self):
        if self.media_player.playlist().currentIndex() == len(self.ac_files) - 1:
            return
        self.media_player.playlist().next()

    def play(self):
        if not self.ac_files:
            return
        if self.change_files:
            playlist = QMediaPlaylist(self.media_player)
            for el in self.ac_files:
                url = QUrl.fromLocalFile(el)
                content = QMediaContent(url)
                playlist.addMedia(content)
            self.media_player.setPlaylist(playlist)
            self.media_player.playlist().currentIndexChanged.connect(self.review)
            self.media_player.play()
            self.play_b.setText('pause')
            self.change_files = False
        else:
            if self.play_b.text() == 'play':
                self.media_player.play()
                self.play_b.setText('pause')
            else:
                self.play_b.setText('play')
                self.media_player.pause()

    def review(self):
        pos = self.media_player.playlist().currentIndex()
        name_mp1 = self.ac_files[pos][self.ac_files[pos].rfind(sls) + 1:
                                      self.ac_files[pos].find('.mp3')]
        self.this_l.setText('this: ' + name_mp1)
        if pos > 0:
            name_mp2 = self.ac_files[pos - 1][self.ac_files[pos - 1].rfind(sls) + 1:
                                              self.ac_files[pos - 1].find('.mp3')]
            self.prew_l.setText('previous: ' + name_mp2)
        else:
            self.prew_l.setText('')
        if pos < len(self.ac_files) - 1:
            name_mp3 = self.ac_files[pos + 1][self.ac_files[pos + 1].rfind(sls) + 1:
                                              self.ac_files[pos + 1].find('.mp3')]
            self.next_l.setText('next: ' + name_mp3)
        else:
            self.next_l.setText('')

    def change_bg(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        if not fname:
            return
        image = QImage(fname).scaled(QSize(401, 394))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image))
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 568, 515)

    def remove_bg(self):
        palette = QPalette()
        self.setPalette(palette)
        self.label = QLabel('', self)

    def closeEvent(self, event):
        self.media_player.stop()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
