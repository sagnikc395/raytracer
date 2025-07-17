from raytracer.vec3 import Vec3


class Ray:
	def __init__(self, origin: Vec3, direction: Vec3):
		self._origin = origin
		self._direction = direction

	def origin(self):
		return self._origin

	def direction(self):
		return self._direction

	def at(self, t: float):
		return self.origin() + t * self.direction()
