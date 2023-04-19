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
	make initialize

defaultsuperuser:
	docker exec -it cloverland_backend python manage.py one_time_create_default_superuser
