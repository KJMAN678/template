```sh
# MLFlow の実行
mlflow run ./src --env-manager=local

# MLFlow Traking による可視化
mlflow ui --port 5001

# MLFlow Models によるデプロイ (ファイルの URLは適宜変更)
mlflow models serve --model-uri file:///root/mlruns/0/ddf1022d86864f65be24949ed4d1f84e/artifacts/model_random_forest --host localhost --port 5001

# MLFlow 2.0+ で可能なクラシックモデルの推論
curl -X POST -H "Content-Type:application/json" -d '{
    "dataframe_split": {
        "columns": ["input1", "input2", "input3", "input4", "input5", "input6", "input7", "input8", "input9", "input10", "input11", "input12", "input13", "input14"],
        "data": [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0]]
        }
    }' http://127.0.0.1:5001/invocations

```

- [Unrecognized content type parameters: format when serving model on databricks experiement](https://stackoverflow.com/questions/75096564/unrecognized-content-type-parameters-format-when-serving-model-on-databricks-ex)