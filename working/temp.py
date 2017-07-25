class TabbedPageHeader(Label):
    #orientation = 'vertical'

    def __init__(self, **kwargs):
        super(TabbedPageHeader, self).__init__(**kwargs)
        self.base = BoxLayout()
        self.base.orientation = 'vertical'
        self.add_widget(self.base)
        #bt = Button(text='default')
        #self.add_widget(bt)

    def add_tab_header(self, tab_):
        print(tab_)
        bt = Button(text=tab_)
        self.base.add_widget(bt)

    def add_tab_headers(self, tablist):
        for tab in tablist:
            self.add_tab_header(tab)

class PageTab(BoxLayout):
    def __init__(self, text='default', **kwargs):
        super(PageTab, self).__init__(**kwargs)

        self.base = Label(text=text)
        self.add_widget(self.base)


class TabbedPage(Label):

    def __init__(self, **kwargs):
        super(TabbedPage, self).__init__(**kwargs)

        #self.pages = [PageTab()]
        #self._active_page = self.pages[0]
        #self.header = TabbedPageHeader()
        #self.add_widget(self.header)
        #self.add_widget(self.pages[0])

    def set_active_page(self, new_active_page):
        self._active_page.size = (0, 0)
        self._active_page = new_active_page
        self._active_page.size = self.size

    def add_page(self, tab):
        pt = PageTab(id=tab, text=tab)
        pt.size_hint = None, None
        pt.size = (0, 0)
        pt.x = self.x
        pt.y = self.y
        #bt = Button(text=tab)
        #bt.bind(on_release=self.set_active_page(self.parent.ids.tab))

        self.pages.append(pt)

        last_page = len(self.pages) - 1
        #self.add_widget(self.pages[last_page])
        self.header.add_tab_header(tab)

    def add_pages(self, tablist):
        for tab in tablist:
            self.add_page(tab)


class IpodPanel(BoxLayout):
    ipod_tab_page = ObjectProperty(None)
    ipod_tab_header = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(IpodPanel, self).__init__(**kwargs)

        self.tab_list = ['Artist', 'Albums', 'Songs', 'Playlist']

        self.ipod_tab_page = TabbedPage()
        self.add_widget(self.ipod_tab_page)

        #def on_ipod(self, panel, ipod):
        #ipod.add_pages(self.tab_list)

    def on_ipod_tab_header(self, panel, ipod_tab_header):
        ipod_tab_header.add_tab_headers(self.tab_list)