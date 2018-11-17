.DEFAULT_GOAL := run

.PHONY: run test coverage install_dependencies install_pipenv setup ci_setup ci_pre_install_system_dependencies

run:
	pipenv run python3 -m home_greeter

test:
	pipenv run python3 -m unittest

coverage:
	NOHALT=False pipenv run coverage run -m home_greeter && pipenv run coverage report -m --skip-covered

install_system_dependencies:
	sudo apt-get -y update && \
	sudo apt-get --with-new-pkgs -y upgrade && \
	sudo apt-get -y install flac swig libpulse-dev libasound2-dev \
	python-pyaudio python3-pyaudio libportaudio2 \
	libportaudiocpp0 portaudio19-dev

install_pipenv:
	pip3 install pipenv

install_application_dependencies:
	pipenv install

ci_pipenv:
	pip install pipenv

ci_pre_install_system_dependencies:
	sudo apt-mark hold oracle-java8-installer && \
	sudo apt-mark hold postgresql-9.3 postgresql-contrib-9.3 postgresql-9.4 postgresql-contrib-9.4 postgresql-9.5 postgresql-contrib-9.5 postgresql-9.6 postgresql-contrib-9.6

docker_build:
	docker build . -t rpi

docker_run:
	docker run --rm=true -p 6080:80 -v $(CURDIR):/home/pi/work -w /home/pi/work rpi
