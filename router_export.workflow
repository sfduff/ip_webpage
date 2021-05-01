activate application "AirPort Utility"
delay 2
tell application "System Events"
	try
		click image 2 of group 1 of scroll area 1 of window 1 of application process "AirPort Utility"
		delay 1
		
		click UI element "Edit" of group 1 of UI element 1 of image "Time Capsule AirPort Time Capsule working normally" of group 1 of scroll area 1 of window "AirPort Utility" of application process "AirPort Utility"
		delay 1
		
		click menu bar item "File" of menu bar 1 of application process "AirPort Utility"
		delay 1
		
		click menu item "Export Configuration File..." of menu 1 of menu bar item "File" of menu bar 1 of application process "AirPort Utility"
		delay 1
		
		click UI element "Save" of sheet 1 of sheet 1 of window "AirPort Utility" of application process "AirPort Utility"
		delay 1
		
		click UI element "Replace" of sheet 1 of sheet 1 of sheet 1 of window "AirPort Utility" of application process "AirPort Utility"
		delay 1
		
		click UI element "Cancel" of sheet 1 of window "AirPort Utility" of application process "AirPort Utility"
		delay 1
		
		click UI element 3 of window "AirPort Utility" of application process "AirPort Utility"
	end try
end tell
