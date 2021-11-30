import mlflow
import os

os.environ["AWS_ACCESS_KEY_ID"] = "please_change_S3_ROOT_USER"
os.environ["AWS_SECRET_ACCESS_KEY"] = "please_change_S3_ROOT_PASSWORD"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"


mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("test-exp")

with mlflow.start_run():
    for epoch in range(0, 3):
        print("epoch:", epoch)
        mlflow.log_metric(key="acc", value=2*epoch, step=epoch)

    mlflow.log_artifact('README.md')
