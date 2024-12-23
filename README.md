# Инструкция по запуску

1. Запустим контейнеры

```bash
docker-compose up -d
```

![](./readme_images/execute.png)


2. Проверим, что контейнеры запустились и отработали

```bash
docker-compose ps
```

![](./readme_images/containers.png)


3. Посмотрим логи контейнера загрузчика

```bash
docker-compose logs bucketloader
```

![](./readme_images/error.png)


4. Видим ошибку, что хранилище переполнилось
