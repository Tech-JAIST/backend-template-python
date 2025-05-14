# backend-template-python
## プロジェクト作成方法
### cookiecutter
```sh
cookiecutter https://github.com/Tech-JAIST/backend-template-python
```

### GUI
右上の `Use this template` からレポジトリを作成できます。

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
