- python 3.10
- VSCode
- Docker
- mlflow
- black, flake8, mypy, isort
- Docker 起動時に読み込めるのは src/ 内のファイルのみ

```sh
# Docker イメージ作成
docker-compose build

# Docker イメージの確認
docker images

# コンテナ起動
docker-compose up -d
```

```sh
# 推奨 VSCode 拡張 を extensions.json から読み込む
# Extensions に下記を入力
@recommended
```
