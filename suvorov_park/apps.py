from django.utils.translation import gettext_lazy as _
from suit.apps import DjangoSuitConfig
from suit.menu import ChildItem, ParentItem


class SuvorovParkConfig(DjangoSuitConfig):
    verbose_name = 'Администрация ТСЖ "Суворов парк"'
    layout = "vertical"
    menu_show_home = False
    menu = (
        ParentItem(
            _("Site setting"),
            children=[ChildItem(model="common.sitesetting")],
            icon="fa fa-folder",
        ),
        ParentItem(
            _("News"),
            children=[ChildItem(model="common.news")],
            icon="fa fa-hacker-news",
        ),
        ParentItem(
            _("services"),
            children=[
                ChildItem(model="services.service"),
                ChildItem(model="services.serviceorder"),
            ],
            icon="fa fa-server",
        ),
        ParentItem(
            _("forum"),
            children=[
                ChildItem(model="forum.forumtopic"),
                ChildItem(model="forum.forummessage"),
            ],
            icon="fa fa-comments",
        ),
        ParentItem(
            _("Голосвания"),
            children=[
                ChildItem(model="polls.poll"),
                ChildItem(model="polls.choice"),
                ChildItem(model="polls.vote"),
            ],
        ),
        ParentItem(
            _("users"), children=[ChildItem(model="users.user")], icon="fa fa-users"
        ),
    )
