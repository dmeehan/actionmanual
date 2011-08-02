"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'actionmanual.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'actionmanual.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for actionmanual.
    """
    

    def init_with_context(self, context):
        # we want a 3 columns layout
        self.columns = 3
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
         # append an app list module for "Portfolio"
        self.children.append(modules.ModelList(
            title=_('Portfolio'),
            include_list=('actionmanual.portfolio.models.Idea', 'actionmanual.portfolio.models.Image',
                          'actionmanual.portfolio.models.Precedent',
                          'actionmanual.portfolio.models.Designer', 'actionmanual.portfolio.models.Firm'),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        
        # append an model list module for "Resources"
        self.children.append(modules.ModelList(
            title=_('Resources'),
            include_list=('actionmanual.resources.models.*',),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        
        # append an model list module for "Site Content"
        self.children.append(modules.ModelList(
            title=_('Site Content'),
            include_list=('actionmanual.sections.models.*','actionmanual.posts.models.*','flatblocks.models.*','django.contrib.comments.models.*'),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        
        # append an model list module for "Content Organization"
        self.children.append(modules.ModelList(
            title=_('Content Organization'),
            include_list=('actionmanual.categories.models.*','tagging.models.*',),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5,
            css_classes=['column_2', 'collapse', 'open'],
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            title=_('Support'),
            css_classes=['column_3', 'collapse', 'open'],
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ]
        ))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for actionmanual.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models, css_classes=['column_1'],),
            modules.RecentActions(
                title=_('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5,
                css_classes=['column_2'],
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
