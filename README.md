## Grocery Online Store

### Описание проекта

Магазин продуктов со следующим функционалом: 

Реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.

Реализована возможность добавления, изменения, удаления продуктов в админке.

Реализованы эндпоинты просмотра категорий, подкатегорий, продуктов для всех пользователей. 

Авторизованный пользователь может добавлять продукты в корзину, удалять из корзины, изменять количество.

Пользователь может просмотреть состав своей корзины с итоговым количеством продуктов и итоговой стоимостью.

Пользователь может очистить свою корзину. 

### Инструменты

- Django 3.2.5
- DjangoRestFramework 3.14.0
- Postgres
- Docker
- Gunicorn 21.2.0


### Как запустить проект

- клонировать репозиторий

```
git@github.com:ApriCotBrain/online-store.git
```

- в домашней директории проекта создать файл .env по примеру .env_sample

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d --build 
```

- выполнить команды:

```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py collectstatic --no-input
```

- загрузить тестовые данные:

```
docker-compose exec backend python manage.py loaddata data/fixtures.json
```

- создать суперпользователя:

```
docker-compose exec backend python manage.py createsuperuser
```


После сборки контейнеров проект будет доступен по адресу:

```
http://localhost/
```

Документация доступна по адресу:

```
http://localhost/api/v1/schema/swagger-ui/
```
