Screen:
	name: "dashboard"
	MDFloatLayout:
		md_bg_color: 246/255, 250/255, 1, 1
		MDToolbar:
			top : root.top
			title: "Dashboard Profile"
			md_bg_color: 202/255, 0, 13/255, 1
			left_action_items: [["dots-vertical", lambda x: root.ids.nav_drawer.toggle_nav_drawer()]]

		MDNavigationDrawer:
			id: nav_drawer

	
		MDFloatLayout:
			size_hint: 1, .3
			pos_hint: {"center_y": .75}
			md_bg_color: 1, 1, 1, 1
			radius: [0,0,20,20]
			#MDIconButton:
			#	icon: "arrow-left"
			#	pos_hint: {"center_x": .08,"center_y": .9}
			#	font_size: "20sp"
			#	text_color: rgba(71, 92, 119, 255)

			#MDIconButton:
			#	icon: "dots-vertical"
			#	pos_hint: {"center_x": .92,"center_y": .9}
			#	font_size: "20sp"
			#	text_color: rgba(71, 92, 119, 255)

			MDLabel:
				text: "anasaz.har"
				font_name: "Roboto"
				font_size: "16sp"
				pos_hint: {"center_x":.18, "center_y": .9}
				halign: "center"
				color: rgba(71, 92, 119, 255)
				bold: True

			Image:
				source: "assets/img/user.png"
				size_hint_y: .2
				pos_hint: {"center_x": .5, "center_y": .7}

				canvas.before:
					Color:
						rgba: rgba(202, 0, 13, 255)

					Ellipse:
						size: 150, 150
						pos: self.center_x-75, self.center_y-75

			MDLabel:
				text: "Anas Azhar"
				font_name: "Roboto"
				font_size: "12sp"
				pos_hint: {"center_x":.5, "center_y": .4}
				halign: "center"
				color: rgba(71, 92, 119, 255)
				bold: True

			MDLabel:
				text: "Learning Code Everyday"
				font_name: "Roboto"
				font_size: "12sp"
				pos_hint: {"center_x":.5, "center_y": .3}
				halign: "center"
				color: rgba(71, 92, 119, 255)





