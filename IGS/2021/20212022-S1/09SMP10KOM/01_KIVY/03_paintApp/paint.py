#:import from_hex kivy.utils.get_color_from_hex 

#:set d 10



<TipButton@Button>
	background_color: from_hex('#0080FFFF')
	canvas:
        Color:
            rgba: from_hex('#FFFFFFFF')

<ColorButton@Button>
	#background_color: from_hex('#0080FFFF')
	on_release: app.paint_app.set_color_line(self.background_color)


<PainterWidget>:
	Button:
		text: 'DEL'
		right: root.right-20
		top: root.top-20
		width: 100
		height: 90
		on_release: app.paint_app.clear_canvas()
		#background_normal:  'delete-icon.jpeg'

	BoxLayout:
		orientation: 'horizontal'
		x: root.x+20
		top: root.top-20
		padding: 2
		spacing: 12
		width: 270
		height: 90

		TipButton:
			on_release: app.paint_app.set_line_width(d)
			canvas:
		        Ellipse:
		            pos: self.center_x - d/2, self.center_y - d/2
		            size: d, d
					
		TipButton:
			on_release: app.paint_app.set_line_width(3*d/2)
			canvas:
		        Ellipse:
		            pos: self.center_x - (3*d/2)/2, self.center_y - (3*d/2)/2
		            size: (3*d/2), (3*d/2)
		TipButton:
			on_release: app.paint_app.set_line_width(2*d)
			canvas:
		        Ellipse:
		            pos: self.center_x - (2*d)/2, self.center_y - (2*d)/2
		            size: (2*d), (2*d)

	BoxLayout:
		#6 Button menyimbolkan warna
		orientation: 'horizontal'
		x: 0
		y: 0
		width: root.width
		height: 90
		size_hint: (None, None)

		ColorButton:
			background_color: from_hex('#FF0000FF')
			canvas:
				Color:
					rgba: from_hex("#FF0000FF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)
		ColorButton:
			background_color: from_hex("#00FF00FF")
			canvas:
				Color:
					rgba: from_hex("#00FF00FF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)
		ColorButton:
			background_color: from_hex("#0000FFFF")
			canvas:
				Color:
					rgba: from_hex("#0000FFFF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)
		ColorButton:
			background_color: from_hex("#0F00F0FF")
			canvas:
				Color:
					rgba: from_hex("#0F00F0FF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)
		ColorButton:
			background_color: from_hex("#0000FFFF")
			canvas:
				Color:
					rgba: from_hex("#0000FFFF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)
		ColorButton:
			background_color: from_hex("#0F00F0FF")
			canvas:
				Color:
					rgba: from_hex("#0F00F0FF")
				Rectangle:
					pos: (self.center_x-50/2, self.center_y-50/2)
					size: (50, 50)










			
