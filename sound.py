import random
import threading
from pygame import mixer


class Sound:
    """Class for sounds in game."""

    def __init__(self):
        """Sounds initialization."""
        self.testo_win = [mixer.Sound("sounds/polacy_robacy.wav"), mixer.Sound("sounds/polacy_zwierzeta.wav"),
                          mixer.Sound("sounds/w_polsce_jak.wav"), mixer.Sound("sounds/jestem_najlepszy.wav"),
                          mixer.Sound("sounds/na_garbach.wav"), mixer.Sound("sounds/patrzcie_skuhwysyny.wav"),
                          mixer.Sound("sounds/rozpylaczem.wav"), mixer.Sound("sounds/w_polsce_jak.wav")]
        self.testo_loose = [mixer.Sound("sounds/prosze_was.wav"), mixer.Sound("sounds/zlitujcie_sie.wav"),
                            mixer.Sound("sounds/wyjebauem_siem.wav")]
        self.testo_defeated = mixer.Sound("sounds/umieram.wav")

    def play_sound_win(self):
        x = random.randrange(len(self.testo_win))
        mixer.music.set_volume(0.2)
        mixer.Sound.play(self.testo_win[x])
        self.reset_music_volume(self.testo_win[x])

    def play_sound_loose(self):
        y = random.randrange(len(self.testo_loose))
        mixer.music.set_volume(0.2)
        mixer.Sound.play(self.testo_loose[y])
        self.reset_music_volume(self.testo_loose[y])

    def play_sound_defeated(self):
        mixer.Sound.play(self.testo_defeated)

    @staticmethod
    def play_music():
        mixer.music.load("music/My_Button_Fly-JP.mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play(-1)

    @staticmethod
    def reset_music_volume(sound):
        sound_len = mixer.Sound.get_length(sound)
        sound_len = round(sound_len, 1)
        t = threading.Timer(sound_len, mixer.music.set_volume, [0.4])
        t.start()

