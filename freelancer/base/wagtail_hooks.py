from wagtail import hooks
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.userbar import AccessibilityItem
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from freelancer.base.filters import RevisionFilterSetMixin
from freelancer.base.models import Person, FooterContent

"""
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html

This demo project also includes the wagtail-font-awesome-svg package, allowing further icons to be
installed as detailed here: https://github.com/allcaps/wagtail-font-awesome-svg#usage
"""


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailfontawesomesvg/solid/hashtag.svg",
        "wagtailfontawesomesvg/solid/code.svg",
        "wagtailfontawesomesvg/solid/pen.svg",
    ]


class CustomAccessibilityItem(AccessibilityItem):
    axe_run_only = None


@hooks.register("construct_wagtail_userbar")
def replace_userbar_accessibility_item(request, items):
    items[:] = [
        CustomAccessibilityItem() if isinstance(item, AccessibilityItem) else item
        for item in items
    ]


class PersonFilterSet(RevisionFilterSetMixin, WagtailFilterSet):
    class Meta:
        model = Person
        fields = {
            "job_title": ["icontains"],
            "live": ["exact"],
            "locked": ["exact"],
        }


class PersonViewSet(SnippetViewSet):
    # Custom SnippetViewSet class for the Person model.
    model = Person
    menu_label = "Authors"
    icon = "pen"
    list_display = ("first_name", "last_name", "job_title", "thumb_image")
    list_export = ("first_name", "last_name", "job_title")
    filterset_class = PersonFilterSet


class FooterContentFilterSet(RevisionFilterSetMixin, WagtailFilterSet):
    class Meta:
        model = FooterContent
        fields = {
            "footer_text": ["icontains"],
        }


class FooterContentViewSet(SnippetViewSet):
    # Custom SnippetViewSet class for the FooterContent model.
    model = FooterContent
    menu_label = "Footer Content"
    icon = "site"
    list_display = ("footer_text",)
    search_fields = ("footer_text", "twitter_url", "github_url", "linkedin_url")
    filterset_class = FooterContentFilterSet


class BlogSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Blog Misc."
    menu_icon = "code"
    menu_order = 300
    items = (PersonViewSet, FooterContentViewSet)


# Register the SnippetViewSetGroup class with Wagtail
register_snippet(BlogSnippetViewSetGroup)

