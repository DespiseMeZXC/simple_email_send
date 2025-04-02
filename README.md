# Простой скрипт для отправки писем

## Установка uv

### Documentation

https://docs.astral.sh/uv/

### Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Установка зависимостей

```bash
uv sync
```

## Запуск скрипта

```bash
uv run main.py
``` 
