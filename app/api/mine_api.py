from app.util.qiniu import get_pic_url
from flask import g
from flask_restful import Resource
from app import auth
from app.model.models import actUser, activity


class Mine(Resource):
    @auth.login_required
    def get(self):
        user = g.user
        username = g.user.username
        if user is None:
            return {
                "status": 0,
                "message": u"未登录"
            }
        doing_activity = actUser.query.filter_by(username=username).all()
        dict = {u"data": []}
        dict['name'] = user.name
        dict['head_pic_url'] = get_pic_url(user.username + '.jpg')
        dict["app_avatar_url"] = get_pic_url(user.app_avatar_name)
        for act_id in doing_activity:
            act = activity.query.filter_by(id=act_id.activity_id).first()
            dict[u"data"].append(
                {
                    u"message": "ok",
                    u"id": act_id.activity_id,
                    u"title": act.title,
                    u"pic_url": act.pic_url,
                    u"bg_pic_url": act.bg_pic_url,
                    u"content": act.content,
                    u"time": act.time,
                    u"organizer": act.organizer,
                }
            )
        dict['status'] = 1
        dict['message'] = u'请求成功'
        return dict
