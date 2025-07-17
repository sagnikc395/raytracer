## common utility files

### vector utility functions
import vec3
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
	return u * (1 // t)


def dot_product(u: vec3.Vec3, v: vec3.Vec3):
	return np.dot(u, v)


def cross_product(u: vec3.Vec3, v: vec3.Vec3):
	return np.cross(u, v)


def unit_vector(v: vec3.Vec3):
	return v / v.length()
