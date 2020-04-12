DATE := $(shell date | sed 's/\ /_/g')

TARGET=./api-samsungtv

run:
	$(TARGET) --port 8080 --config=config.yml

