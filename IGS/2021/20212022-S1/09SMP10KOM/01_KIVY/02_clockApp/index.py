
<RobotoLabel@Label>:
	markup: True
	font_name: 'Roboto'
	font_size: 90

<RobotoButton@Button>:
	font_name: 'Roboto'
	font_size: 25
	bold: True


BoxLayout:
	orientation: "vertical"

	RobotoLabel:
		text: "[b]00[/b]:00:00"
		id: time
		
	BoxLayout:
		height: 90
		orientation: 'horizontal'
		padding: 20
		spacing: 20
		size_hint: (1, None)

		RobotoButton:
			text: 'Start'
			id: start_stop
			on_press: app.start_stop()

		RobotoButton:
			text: 'Reset'
			on_press: app.reset()

	RobotoLabel:
		text: "00:00.[size=40]00[/size]"
		id: stopwatch
