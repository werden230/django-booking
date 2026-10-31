# Booking Service

Небольшой REST API для управления бронированиями и номерами отеля. Проект разработан на Django/DRF.

## Технологии

- Python 3.12
- Django/DRF
- PostgreSQL
- Docker & Docker Compose
- Poetry

## Запуск проекта

1. Клонировать репозиторий:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Собрать и запустить контейнеры:

```bash
docker compose up --build
```

API будет доступен по адресам в интерактивном режиме отладки DRF:

```text
http://localhost:8000/api/v1/room/
http://localhost:8000/api/v1/booking/
```
## API Endpoints

### Rooms

| Method | Endpoint | Description |
|---|---|---|
| GET | `/room/` | Получение списка номеров |
| POST | `/room/` | Создание нового номера |
| DELETE | `/room/{id}/` | Удаление номера по ID |

**Параметры GET-запроса:**

- `sort_by` — поле сортировки (`price`, `created_at`).
- `order` — направление сортировки (`asc`, `desc`).

### Bookings

| Method | Endpoint | Description |
|---|---|---|
| GET | `/booking/` | Получение списка бронирований |
| POST | `/booking/` | Создание нового бронирования |
| DELETE | `/booking/{id}/` | Удаление бронирования по ID |

Список бронирований упорядочивается по `date_from`.

**Особенности создания бронирования:**

- Проверяется пересечение дат с существующими бронированиями.
- При обнаружении пересечения возвращается HTTP 400.



## Тестирование

```bash
poetry run pytest
```
