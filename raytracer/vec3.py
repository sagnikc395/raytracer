import numpy as np
import math


class Vec3:
	e = np.array([], dtype=float)

	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.e.append(x, y, z)

	def X(self):
		return self.e[0]

	def Y(self):
		return self.e[1]

	def Z(self):
		return self.e[2]

	def __neg__(self):
		return self.e * -1

	def item_at(self, index):
		if index >= len(self.e):
			raise Exception('Item access invalid')
		return self.e[index]

	def __iadd__(self, other: np.array):
		return self.e + other

	def __imul__(self, other: float):
		# broadcasting
		return self.e * other

	def __idiv__(self, other: float):
		return self.e / other

	def _length_squared(self) -> float:
		return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

	def length(self) -> int:
		return math.sqrt(self._length_squared())
