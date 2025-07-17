import sys


IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def main():
    sys.stdout.write(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n")
    sys.stdout.flush()

    for j in range(0, IMAGE_HEIGHT):
        for i in range(0, IMAGE_WIDTH):
            r = float(i) / (IMAGE_HEIGHT - 1)
            g = float(j) / (IMAGE_HEIGHT - 1)
            b = 0.0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            sys.stdout.write(f"{ir} {ig} {ib}\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
