import sys
import logging

from raytracer.vec3 import Vec3
from raytracer.color import write_color

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def main():
	sys.stdout.write(f'P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n')
	sys.stdout.flush()

	logger = logging.getLogger(__name__)
	logging.basicConfig(filename='raytracer.log', encoding='utf-8', level=logging.DEBUG)

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
			pixel_color = Vec3(float(i) / (IMAGE_WIDTH - 1), float(j) / (IMAGE_HEIGHT - 1), 0.0)
			write_color(pixel_color)

	logger.debug('\rDone.                         ')


if __name__ == '__main__':
	main()
