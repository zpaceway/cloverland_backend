migrate:
	python3.11 manage.py migrate

migrations:
	python3.11 manage.py makemigrations

run:
	python3.11 manage.py runserver 0.0.0.0:5183

initialize:
	make migrations
	make migrate
	make defaultsuperuser

reinstall:
	rm -f $$(find . -type f -wholename "*migrations/0*.py")
	rm -f db.sqlite3
	make initialize

defaultsuperuser:
	python3.11 manage.py one_time_create_default_superuser