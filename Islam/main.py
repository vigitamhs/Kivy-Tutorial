from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.metrics import dp

from functools import partial
import webbrowser, bidi.algorithm, db
import arabic_reshaper
from Style import *

Builder.load_file('Style/style.kv')

class MainApp(MDApp):
	def __init__(self,**kwargs):
		self.theme_cls.theme_style='Dark'
		super(MainApp,self).__init__(**kwargs)

	def on_start(self):
		for image, url in db.imageicon.items():
			self.root.ids.channel.add_widget(
			Factory.IconImage(icon=image,
			pos_hint={'center_y':0.5,'center_x':url[0]},
			on_release=partial(self.OpenUrl,url[1]),
			))

		for image,url in db.Islam.items():
			self.root.ids.Islam.add_widget(
			MCard(image=image,url=url))

	def ar_text(self,text):
		text = arabic_reshaper.reshape(text)
		text = bidi.algorithm.get_display(text)
		return text

	def OpenUrl(self,*url):
		webbrowser.open(url[0])

MainApp().run()
