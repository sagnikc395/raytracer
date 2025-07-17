## common utility files

### vector utility functions
from raytracer import vec3
import numpy as np


def add_vector(u: vec3.Vec3, v: vec3.Vec3):
	return u + v


def diff_vector(u: vec3.Vec3, v: vec3.Vec3):
	return u - v


def mult_vector(u: vec3.Vec3, v: vec3.Vec3):
	return vec3.Vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])


def mult_scalar(u: vec3.Vec3, t: float):
	# this is just broadcasting
	return u * t


def div_scalar(u: vec3.Vec3, t: float):
	return u * (1.0 / t)


def dot_product(u: vec3.Vec3, v: vec3.Vec3) -> float:
	return float(np.dot(u.e, v.e))


def cross_product(u: vec3.Vec3, v: vec3.Vec3):
	result = np.cross(u, v)
	return vec3.Vec3(*result)


def unit_vector(v: vec3.Vec3):
	return v / v.length()
