# backend-template-python
## プロジェクト作成方法
### GUI
右上の `Use this template` からレポジトリを作成できます。

## How to run
```
docker build -t backend_python .
docker run --rm -p 8000:8000 backend_python
```
## uv
```sh
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Python
```sh
uv python install {version}
```

## format
```sh
uv run ruff format .
```

## Acknowledgements

This project is based on [a5chin/python-uv](https://github.com/a5chin/python-uv/tree/main), which is licensed under the MIT License.
