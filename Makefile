build:
	sudo docker-compose up -d

start:
	sudo docker-compose start

stop:
	sudo docker-compose stop

rebuild:
	sudo docker-compose down
	sudo docker-compose build
	sudo docker-compose up -d

delete:
	sudo docker-compose stop
	sudo docker-compose rm
