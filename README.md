

![1*LLHlj24sn3mPSgq9WtX-Vg](https://github.com/BrowserNeo/QA_guru_Allure_report/blob/master/allure-report.png)



## Написан тест на проверку названия Issue в репозитории через Web-интерфейс.

Этот тест представлен в трех вариантах:

1. Чистый Selene (без шагов)
2. Лямбда шаги через with allure.step
3. Шаги с декоратором @allure.step
4. Разметку тестов всеми аннотациями


##### Тесты лежат в папке  Allure_report/tests/
start db
docker stop tedu-db || true
docker rm tedu-db || true
docker volume rm serversetup_postgres-data || true
docker compose up -d --force-recreate tedu-database
sleep 5
