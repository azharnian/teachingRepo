#:import from_hex kivy.utils.get_color_from_hex
# icon from http://zavoloklom.github.io/material-design-iconic-font/icons.html

MDScreen:
	name: "login"
	MDFloatLayout:
		md_bg_color: from_hex("#ffffff")
		MDIconButton:
			icon: "chevron-left"
			user_font_size: "35sp"
			pos_hint: {"center_x": .06, "center_y" : .95}
		MDLabel:
			text: "Back"
			font_size: "18sp"
			font_name: "Roboto"
			pos_hint: {"center_x": .58, "center_y": .949}
		Image:
			source: "igs.png"
			size_hint: .26, .26
			pos_hint: {"center_x": .22, "center_y":.8}

		MDLabel:
			text: "Proceed with your"
			font_size: "22sp"
			font_name: "Roboto"
			color: from_hex("#101216")
			pos_hint: {"center_x":.6, "center_y":.65}

		MDLabel:
			text: "Login"
			font_size: "28sp"
			font_name: "Roboto"
			bold: True
			color: from_hex("#101216")
			pos_hint: {"center_x":.6, "center_y":.58}

		MDFloatLayout:
			size_hint: .79, .08
			pos_hint: {"center_x": .5, "center_y": .42}
			MDLabel:
				text: "Username"
				font_size: "14sp"
				font_name: "Roboto"
				pos_hint: {"center_x": .5, "center_y": .9}
			TextInput:
				size_hint_y: .75
				font_name: "Roboto"
				pos_hint: {"center_x": .49, "center_y":.4}
				background_color: 0,0,0,0
				cursor_color: 0,0,0,1
				cursor_width: "2sp"
				foreground_color: from_hex("#101216")
				font_size: "17sp"
				multiline: False
				write_tab: False
			MDIcon:
				icon: "account"
				user_font_size: "35sp"
				pos_hint: {"center_x": 1.4, "center_y":.5}

			MDFloatLayout:
				pos_hint: {"center_x": .5, "center_y":0}
				size_hint_y: .03
				md_bg_color: from_hex("#101216")

		MDFloatLayout:
			size_hint: .79, .08
			pos_hint: {"center_x": .5, "center_y": .28}
			MDLabel:
				text: "Password"
				font_size: "14sp"
				font_name: "Roboto"
				pos_hint: {"center_x": .5, "center_y": .9}
			TextInput:
				size_hint_y: .75
				font_name: "Roboto"
				pos_hint: {"center_x": .49, "center_y":.4}
				background_color: 0,0,0,0
				cursor_color: 0,0,0,1
				cursor_width: "2sp"
				foreground_color: from_hex("#101216")
				font_size: "17sp"
				multiline: False
				write_tab: False
				password: True
			MDIcon:
				icon: "key"
				user_font_size: "35sp"
				pos_hint: {"center_x": 1.4, "center_y":.4}

			MDFloatLayout:
				pos_hint: {"center_x": .5, "center_y":0}
				size_hint_y: .03
				md_bg_color: from_hex("#101216")

		Button:
			text: "Login"
			background_color: 0,0,0,0
			font_name: "Roboto"
			font_size: "18sp"
			bold: True
			size_hint: .79, .08
			pos_hint: {"center_x": .5, "center_y": .15}
			canvas.before:
				Color:
					rgb: 226/255, 0, 48/255, 1
				RoundedRectangle:
					size: self.size
					pos: self.pos
					radius: [10]

		MDTextButton:
			text: "Forget Password?"
			font_size: "15sp"
			pos_hint: {"center_x": .5, "center_y": .07}
			halign: "center"
			color: 120/255, 120/255, 120/255







