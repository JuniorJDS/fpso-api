run:
	uvicorn app.main:app --reload

dbuild:
	docker-compose up -d --build
	sleep 5
	xdg-open http://0.0.0.0:8000/docs

ddown:
	docker-compose down

integration-tests:
	docker-compose -f docker-compose-tests.yml stop
	docker-compose -f docker-compose-tests.yml build
	docker-compose -f docker-compose-tests.yml up --exit-code-from web