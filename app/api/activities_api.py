from flask_restful import Resource
from app.resources.apply import Apply
from app.model.models import activity, actUser
from flask import g
from app import auth


class Activity(Resource):

    def __init__(self):
        self.success_message = {
            "message": "ok",
            "code": 0
        }
        self.failed_message = {
            "message": "error",
            "code": 1
        }

    def success(self, data=None):
        message = self.success_message.copy()
        if data:
            message["data"] = data
        return message

    def failed(self):
        return self.failed_message

    @auth.login_required
    def get(self):
        user = g.user
        username = g.user.username
        a = Apply()
        data = a.first_login(user)
        if not data:
            return self.failed()
        activities = activity.query.all()
        doing_activity = actUser.query.filter_by(username=username).all()
        data = {
            u"status": 1,
            u"message": "存入用户数据成功",
            u"data": [],
            u"doing_act_id": []
        }
        for act_id in doing_activity:
            data[u"doing_act_id"].append({
                u"id": act_id.activity_id,
            })
        for act in activities:
            data[u"data"].append(
                {
                    u"message": "ok",
                    u"id": act.id,
                    u"title": act.title,
                    u"pic_url": act.pic_url,
                    u"bg_pic_url": act.bg_pic_url,
                    u"content": act.content,
                    u"time": act.time,
                    u"organizer": act.organizer,
                }
            )
        return data
