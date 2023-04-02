```sh
# MLFlow の実行
mlflow run ./src --env-manager=local

# MLFlow Traking による可視化
mlflow ui --port 5001

# MLFlow Models によるデプロイ 
mlflow models serve -m src/mlruns/0/41cad246f9eb472f9520ed2a3250f293/artifacts/model_random_forest

mlflow models serve --model-uri file:///root/mlruns/0/ddf1022d86864f65be24949ed4d1f84e/artifacts/model_random_forest --host localhost --port 5001

curl -X POST \
    -H "Content-Type:application/json; format=pandas-records" \
    --data '{"0":{"0":0.0,"1":0.0,"2":1.0,"3":0.0,"4":0.0,"5":0.0,"6":0.0,"7":1.0,"8":1.0,"9":0.0,"10":1.0,"11":0.0,"12":0.0,"13":0.0}}' \
    http://127.0.0.1:5001/invocations

- エラーでる
https://stackoverflow.com/questions/75096564/unrecognized-content-type-parameters-format-when-serving-model-on-databricks-ex
```