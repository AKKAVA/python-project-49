install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

test-pack:
	poetry build
	python3 -m pip install --user dist/*.whl
	brain-games

init:
	poetry run flake8 brain_games

record:
	asciinema rec --overwrite brain-games-demo.cast
