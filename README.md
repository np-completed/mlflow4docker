# MLflow 4 Docker
This project combines MLflow with a database (PostgreSQL) and a reverse proxy (NGINX) into a multi-container Docker application (with docker-compose).

## Usage
1. Start the docker compose. For example with: `sudo docker-compose up --build --force-recreate --always-recreate-deps --remove-orphans -d`
2. Until [create bucket for mlflow at first start #9](https://github.com/PhilipMay/mlflow4docker/issues/9) is done: create a bucket called "mlflow". This can be done with `create_buchet.py`.
3. Start `mlflow_demo_client.py` to test the installation.
4. You should see the test run when you call http://localhost:5000

## Licensing

Copyright (c) 2021 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/PhilipMay/mlflow4docker/blob/main/LICENSE) in the repository.
