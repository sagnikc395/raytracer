# Define variables
script := "main.py"
out_dir := "build"
out_file := "build/image.ppm"

# Generate PPM image
build:
	mkdir -p {{out_dir}}
	python {{script}} > {{out_file}}

# Lint and fix with ruff
lint:
	pre-commit run --all-files

# Clean build artifacts
clean:
	rm -rf {{out_dir}}
