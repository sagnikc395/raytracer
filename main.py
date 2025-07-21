import sys
import logging

from raytracer.vec3 import Vec3
from raytracer.color import write_color, Color
from raytracer.ray import Ray
from raytracer.utils import unit_vector


IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def ray_color(r: Ray) -> Color:
	# this will just return the black color
	# return Color(0.0,0.0,0.0)
	unit_direction = unit_vector(r.direction())
	a = (unit_direction.Y() + 1.0) * 0.5
	return Color(1.0, 1.0, 1.0) * (1.0 - a) + Color(0.5, 0.7, 1.0) * a


def main():
	sys.stdout.write(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n')
	sys.stdout.flush()

	logger = logging.getLogger(__name__)
	logging.basicConfig(filename='raytracer.log', encoding='utf-8', level=logging.DEBUG)

	# image gen
	aspect_ratio = 16.0 / 9.0
	image_width = 400

	# calculating the image height and ensure that it's at least 1
	image_height = image_width / aspect_ratio
	image_height = 1 if image_height < 1 else image_height

	# camera
	focal_length = 1.0
	viewport_height = 2.0
	viewport_width = viewport_height * (float(image_width) / image_height)
	camera_center = Vec3(0.0, 0.0, 0.0)

	# calc the vectors across the horizontal and down the vertical viewport edges
	viewport_u = Vec3(viewport_width, 0, 0)
	viewport_v = Vec3(0, -viewport_height, 0)

	# calc the horizontal and vertical data vectors from pixel to pixel
	pixel_delta_u = viewport_u / image_width
	pixel_delta_v = viewport_v / image_height

	# calc the location of the upper left pixel
	viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
	pixel00_location = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5

	for j in range(0, IMAGE_HEIGHT):
		logger.debug('\rScanlines remaining: %s', (IMAGE_HEIGHT - j))
		for i in range(0, IMAGE_WIDTH):
			# r = float(i) / (IMAGE_HEIGHT - 1)
			# g = float(j) / (IMAGE_HEIGHT - 1)
			# b = 0.0

			# ir = int(255.999 * r)
			# ig = int(255.999 * g)
			# ib = int(255.999 * b)

			# sys.stdout.write(f'{ir} {ig} {ib}\n')
			# sys.stdout.flush()
			# pixel_color = Vec3(float(i) / (IMAGE_WIDTH - 1), float(j) / (IMAGE_HEIGHT - 1), 0.0)
			# write_color(pixel_color)
			pixel_center = pixel00_location + (pixel_delta_u * i) + (pixel_delta_v * j)
			ray_direction = pixel_center - camera_center
			r = Ray(camera_center, ray_direction)

			pixel_color = ray_color(r)
			write_color(pixel_color)

	logger.debug('\rDone.                         ')


if __name__ == '__main__':
	main()
