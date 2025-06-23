class PhotographyCamera:
	def __init__(self, storage_size_in_mb):
		self.photographies = []
		# each photo takes around 65mb
		self.max_photographies = storage_size_in_mb / 65
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)