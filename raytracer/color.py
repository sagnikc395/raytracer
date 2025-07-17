from raytracer import vec3
import sys

Color = vec3.Vec3


def write_color(pixel_color: Color):
	r = pixel_color.X()
	g = pixel_color.Y()
	b = pixel_color.Z()

	# translate the [0,1] component values to the byte range [0,255]

	rbyte = int(255.999 * r)
	gbyte = int(255.999 * g)
	bbyte = int(255.999 * b)

	# write out the pixel color component
	sys.stdout.write(f'{rbyte} {gbyte} {bbyte}\n')
	sys.stdout.flush()
