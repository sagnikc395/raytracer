import numpy as np
import math


class Vec3:
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.e = np.array([x, y, z], dtype=float)

	def X(self):
		return self.e[0]

	def Y(self):
		return self.e[1]

	def Z(self):
		return self.e[2]

	def __neg__(self):
		return Vec3(*(-self.e))

	def item_at(self, index):
		if index >= len(self.e):
			raise Exception('Item access invalid')
		return self.e[index]

	def __iadd__(self, other: np.array):
		self.e += other.e
		return self

	def __imul__(self, other: float):
		# broadcasting
		self.e *= other
		return self

	def __itruediv__(self, other: float):
		self.e /= other
		return self

	def _length_squared(self) -> float:
		return np.dot(self.e, self.e)

	def length(self) -> int:
		return math.sqrt(self._length_squared())

	def __repr__(self) -> str:
		return ' '.join(self.e)

	def __add__(self, other):
		return Vec3(*(self.e + other.e))

	def __sub__(self, other):
		return Vec3(*(self.e - other.e))

	def __mul__(self, t: float):
		return Vec3(*(self.e * t))

	def __truediv__(self, t: float):
		return Vec3(*(self.e / t))
