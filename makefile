all:
	python manage.py loaddata ito/fixtures/gpu.json
	python manage.py loaddata ito/fixtures/processor.json
	python manage.py loaddata ito/fixtures/operatingSystem.json
	python manage.py loaddata ito/fixtures/microComputer.json
	python manage.py loaddata ito/fixtures/physicalCharacteristic.json