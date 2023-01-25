# Pyspark Pytest


Testing pyspark code with pytest

/Link to blog post here/

Build docker container

    docker build -t "test_pyspark" .

Linux  

    docker run -it -v $(pwd):/app test_pyspark bash

Win  

    docker run -it -v %cd%:/app test_pyspark bash

Run tests (from inside container)

    pytest -s tests/
