migrate:
	docker exec -it cloverland_backend python manage.py migrate

migrations:
	docker exec -it cloverland_backend python manage.py makemigrations

run:
	python manage.py runserver 0.0.0.0:5183

initialize:
	make migrations
	make migrate
	make defaultsuperuser

install:
	docker rm -f cloverland_backend
	docker compose up -d --build
	make initialize

reinstall:
	rm -f $$(find . -type f -wholename "*migrations/0*.py")
	make install

defaultsuperuser:
	docker exec -it cloverland_backend python manage.py one_time_create_default_superuser

logs:
	docker logs -f cloverland_backend

restart:
	docker restart cloverland_backend
