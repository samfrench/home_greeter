.DEFAULT_GOAL := run

.PHONY: run install_dependencies setup

run:
	pipenv run python3 src/home_greeter.py

install_dependencies:
	sudo apt-get install flac swig libpulse-dev libasound2-dev \
	python-pyaudio python3-pyaudio libportaudio0 libportaudio2 \
	libportaudiocpp0 portaudio19-dev

install_pipenv:
	sudo pip3 install pipenv

setup:
	pipenv install
