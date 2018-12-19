# Giving

## 安装requirements.txt依赖

    pip install -r requirements.txt

## 运行

    python manage.py runserver

## 登录

    POST /api/token
need

    {
        "username": 云家园账号,
        "password": 云家园密码
    }

成功return

    {
        "message": "ok",
        "code": 0,
        "token": token
    }

## 首页活动

    GET /api/activity

成功return

    {
        "data": [
            {
            "id": 1,
            "title": "JUST DO IT",
            "time": "2018年12月13日"，
            "organizer": "青志协"，
            "pic_url":"static/pic/item-1.png",
            "message": "ok",
            "bg_pic_url": "/static/bg-pic/act-bg1.png",
            "content": "第一个活动内容"
            }，
            {
            "id": 2,
            "title": "青年志愿者协会捐书活动",
            "time": "2018年12月14日",
            "organizer": "青志协",
            "pic_url": "/static/pic/item-2.png",
            "message": "ok",
            "bg_pic_url": "/static/bg-pic/act-bg2.png",
            "content": "第二个活动内容"
            }，
            {
            "id": 3,
            "title": "常回家看看吧",
            "time": "2018年12月14日",
            "organizer": "青志协",
            "pic_url": "/static/pic/item-3.png",
            "message": "ok",
            "bg_pic_url": "/static/bg-pic/act-bg3.png",
            "content": "第三个活动内容"
            }
        ],
        "doing_act_id": [
            {"id": 1},
            {"id": 2},
            {"id": 3},
        ]
        "status": 1，
        "message": "存入用户数据成功"
    }

## 加入活动

    POST /api/join
need

    {
        "activity_id": activity_id,
    }

成功return

    {
        "message": "用户加入活动成功",
        "status": 1
    }

已加入过或加入失败return：

    "数据库错误"

## 我的信息

    Get api/mine
成功return

    {
        "data": {
            "name": "王某",
            "app_avatar_url":"https://",
        "head_pic_url":"https://",
        }
        "message": "请求成功",
        "status": 1
    }