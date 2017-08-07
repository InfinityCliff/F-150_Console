from kivy.factory import Factory

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty, StringProperty, ListProperty

from kivy.uix.button import Button

from side_menu import SideMenu
from console_screen import ConsoleScreen

import canbus



from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

music_screen_kv = """
#:include music_screen.kv
"""

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    pass


class SelectionViewClass(RecycleDataViewBehavior, BoxLayout):

    text = StringProperty("")
    artist = StringProperty('')
    album = StringProperty('')
    index = None

    #def set_state(self, state, app):
    #    app.root.ids.rv.data[self.index]['selected'] = state

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectionViewClass, self).refresh_view_attrs(rv, index, data)


class SelectionView(RecycleView):
    data = []

    def update_data(self, new_data):
        self.data = new_data
        self.refresh_from_data()


class SearchBar(BoxLayout):
    selection_view = ObjectProperty()

    def add_AlphaButtons(self, widget):
        for x in '#ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            widget.add_widget(Button(text=x))


albums_lst = [
    {'All Sons & Daughters': {'Brokenness Aside (EP)':
                                  ['Alive', 'Let It Shine', 'All The Poor And Powerless', 'Brokenness Aside',
                                   'I Am Set Free', 'Your Glory']}},
    {'Deer Tick': {'Divine Providence':
                       ['The Bump', 'Funny Word', "Let's All Go To The Bar", 'Clownin Around', 'Main Street',
                        'Chevy Express', 'Something To Brag About', 'Walkin Out The Door', 'Make Believe',
                        "Now It's Your Turn", 'Electric', 'Miss K.', 'Hidden Song']}},
    {'Kassidy': {'One Man Army (Deluxe Version)':
                     ['Kallisti', 'Get By', "Maybe I'll Find", 'One Man Army', 'The Hunted', 'Home',
                      'Flowers At the Edge of the Rain', "I Can't Fly", 'Driven by Fools', 'There Is a War Coming',
                      'This Life Is an Ocean', 'Afterburn (Hidden Track)', 'Anybody Else (Bonus Track)',
                      'The Four Walls (Bonus Track)']}}]


class IpodSelectionScreen(Screen):
    #selection_view = ObjectProperty()
    albums_lst = []

    def __init__(self, **kwargs):
        super(IpodSelectionScreen, self).__init__(**kwargs)
        self.albums_lst = self.get_albums_lst()

    def get_albums_lst(self):
        #TODO ultimatley needs to get this from disc or preloaded file
        return albums_lst

    def extract_songs(self):
        song_list = [{'text': song, 'artist': artist, 'album': album, 'selected': 'normal', 'input_data': song}
                          for artists in self.albums_lst
                          for (artist, albums) in artists.items()
                          for (album, songs) in albums.items() for song in songs]
        self.ids.search_bar.ids.rv.update_data(song_list)

    def extract_albums(self):
        album_list = [{'text': album, 'selected': 'normal', 'input_data': album}
                      for artists in self.albums_lst
                      for (artist, albums) in artists.items()
                      for (album, _) in albums.items()]

        self.ids.search_bar.ids.rv.update_data(album_list)

    def extract_artists(self):
        artist_list = [{'text': artist + '  [' + str(len(albums)) + ']', 'selected': 'normal', 'input_data': artist}
                      for artists in self.albums_lst
                      for (artist, albums) in artists.items()]

        self.ids.search_bar.ids.rv.update_data(artist_list)

    def extract_playlists(self):
        self.ids.search_bar.ids.rv.update_data([])


class IpodScreen(Screen):
    album_cover = StringProperty("")
    play_mode = StringProperty("Shuffle Song")

    def PlayAlbum(self):
        print('switch to first song and play ablum')

    def ShuffleSongs(self):
        print('Shuffle all songs on Ipod')

    def DoubleShuffle(self):
        print('Shuffle all songs, with two from each artist')

    def AlbumShuffle(self):
        print('shuffle all albums')


class MusicManager(ScreenManager):
    ipod_screen = ObjectProperty()
    radio_screen = ObjectProperty()
    aux_screen = ObjectProperty()
    ipod_selection_screen = ObjectProperty()


class MusicScreen(ConsoleScreen):
    mm = ObjectProperty()
    screen_side_menu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mm = MusicManager()
        self.add_widget(self.mm)
        self.screen_side_menu = SideMenu(self.get_screen)
        self.screen_side_menu.add_content(Factory.MusicScreenSideMenu())
        self.screen_side_menu.set_manager(self.mm)
        self.add_widget(self.screen_side_menu)

    def get_screen(Self):
        print(Self)

    def Shuffle(self):
        pass

    def Double_Shuffle(self):
        pass

    def Album_Shuffle(self):
        pass

    def Play_Album(self):
        pass

    def send_CANBUS(self, code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)




