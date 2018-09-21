.PHONY: all

all: science

science_requests: science_requests.py
	python science_requests.py
science: science.py
	python3 science.py
