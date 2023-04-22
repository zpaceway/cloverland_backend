migrate:
	docker exec -it cloverland_backend python manage.py migrate

migrations:
	docker exec -it cloverland_backend python manage.py makemigrations

run:
	docker exec -it cloverland_backend python manage.py runserver 0.0.0.0:5183

initialize:
	make migrations
	make migrate
	make defaultsuperuser

reinstall:
	rm -f $$(find . -type f -wholename "*migrations/0*.py")
	docker compose down
	docker compose up -d --build
	make initialize

defaultsuperuser:
	docker exec -it cloverland_backend python manage.py one_time_create_default_superuser

logs:
	docker logs -f cloverland_backend

restart:
	docker restart cloverland_backend
