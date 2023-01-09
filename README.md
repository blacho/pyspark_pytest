# pyspark_docker_delete
Running tests in pyspark test build


docker build -t "test_pyspark" .

docker run -it -v $(pwd):/app test_pyspark bash

cd /app/Project
pytest -s tests/
