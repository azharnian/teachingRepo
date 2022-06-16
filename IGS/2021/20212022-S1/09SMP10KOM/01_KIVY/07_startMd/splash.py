MDScreen:
	name: "splash"
	MDFloatLayout:
		md_bg_color: 226/255, 0, 48/255, 1
		Image:
			source: "igs.png"
			size_hint: .26, .26
			pos_hint: {"center_x": .5, "center_y": .55}
			canvas.before:
				Color:
					rgb: 1,1,1,1
				Ellipse:
					size: 300, 300
					pos: self.center_x-150, self.center_y-150
		MDLabel:
			text: "Ignatius Global School"
			pos_hint: {"center_x": .5, "center_y": .40}
			halign: "center"
			font_name: "Roboto"
			color: 1,1,1,1
			font_size: "25sp"
			#bold: True
