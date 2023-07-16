# insurance_service

REST API сервис по расчёту стоимости страхования в зависимости от типа груза и объявленной стоимости (ОС).

## Установка зависимостей

```
pip install -r requirements.txt
```

## Настройка базы данных

Для работы с базой данных, необходимо настроить переменные окружения в файле `.env`. Замените `PG_USER`, `PG_PASSWORD` и `PG_DB` на свои значения.

## Запуск сервиса

```
docker-compose up -d --build
```

Сервис будет доступен по адресу `http://localhost:8000`.

## Использование API

### Расчёт стоимости страхования

`POST /calculate_insurance/`

Пример запроса:
```json
{
  "cargo_type": "Glass",
  "declared_value": 1000.0
}
```
Пример ответа:
```json
{
  "insurance_cost": 40.0
}
```
Остановка сервиса

```
docker-compose down
```
