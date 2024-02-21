run:
	@poetry run uvicorn app.main:app --port 8080 --reload

run_docker:
	@docker compose up

dropdb:
	@dropdb rinha || true

createdb: dropdb
	@createdb rinha || true
	@psql rinha --file script.sql

select:
	@psql rinha --command "select * from person"
