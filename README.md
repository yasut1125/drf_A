
# 手順
## 1.Dockerコンテナ起動
```
$ docker compose up
```

- 下記からPOST実行可能
http://localhost:8000/items/items/

<br>

## その他
- もしサーバーが起動していない場合、コンテナ内部で下記を実行する
```
$ python manage.py runserver 0.0.0.0:8000
```

- コンテナに入って、管理者アカウントを作成する場合
```
$ docker exec -it [webのコンテナ名]  bash
$ python manage.py createsuperuser
```

