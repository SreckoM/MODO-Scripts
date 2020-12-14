import modo

scene = modo.Scene()

for itm in scene.selected:

	name = itm.name
	print ('Old name: %s') % name
	itm.name = itm.name.replace(" ", "_")
	itm.name = itm.name.replace(".", "_")
	itm.name = itm.name.replace(":", "")
	itm.name = itm.name.replace('"', "")
	itm.name = itm.name.replace('/', "")
	itm.name = itm.name.replace('[', "")
	itm.name = itm.name.replace(']', "")
	itm.name = itm.name.replace('-', "")
	itm.name = itm.name.replace("'", "")
	itm.name = itm.name.replace("@", "")

	print ('New name: %s') % itm.name
	

#Test push	
