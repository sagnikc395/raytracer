# Variables
script := "main.py"
out_dir := "dist"
out_file := "{{out_dir}}/image.ppm"

# Generate PPM image
build:
	mkdir -p {{out_dir}}
	python {{script}} > {{out_file}}

# Run ruff linting and formatting
lint:
	pre-commit run --all-files

# Clean the build output
clean:
	rm -rf {{out_dir}}
