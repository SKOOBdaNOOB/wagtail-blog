from django.db import models

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.models import (
    Page,
)

from .blocks import BaseStreamBlock


class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Hero area
    - Body area
    - A promotional area
    - Moveable featured site sections
    """

    # Hero section of HomePage
    hero_title = models.CharField(
        max_length=60, 
        help_text="The title displayed within the hero section of the home page",
    )
    hero_text = models.CharField(
        max_length=255, 
        help_text="Write an introduction for the bakery",
    )
    hero_cta = models.CharField(
        verbose_name="Hero Call To Action",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )
    
    # Achievement cards in hero section
    achievement_card_1_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Achievement card 1 image",
    )
    achievement_card_1_num = models.CharField(
        max_length=5, 
        verbose_name="1st Achievement card number",
        help_text="Customize the growth of your achievements",
    )
    achievement_card_1_text = models.CharField(
        max_length=80, 
        verbose_name="1st Achievement card text",
        help_text="Customize your acheivements as they grow with you",
    )
    achievement_card_2_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Achievement card 2 image",
    )
    achievement_card_2_num = models.CharField(
        max_length=5, 
        verbose_name="2nd Achievement card number",
        help_text="Customize the growth of your achievements",
    )
    achievement_card_2_text = models.CharField(
        max_length=80, 
        verbose_name="2nd Achievement text block",
        help_text="Customize your acheivements as they grow with you",
    )
    achievement_card_3_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Achievement card 3 image",
    )
    achievement_card_3_num = models.CharField(
        max_length=5, 
        verbose_name="3rd Achievement card number",
        help_text="3rd Achievement count block",
    )
    achievement_card_3_text = models.CharField(
        max_length=80, 
        verbose_name="3rd Achievement card text",
        help_text="Customize your acheivements as they grow with you",
    )

    # Body section of the HomePage
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Home content block",
        blank=True,
        use_json_field=True,
    )

    # Promo section of the HomePage
    promo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Promo image",
    )
    promo_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display above the promo copy"
    )
    promo_text = RichTextField(
        null=True, blank=True, max_length=1000, help_text="Write some promotional copy"
    )

    # Featured sections on the HomePage
    # You will see on templates/base/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section_1_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display above the promo copy"
    )
    featured_section_1 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="First featured section for the homepage. Will display up to "
        "three child items.",
        verbose_name="Featured section 1",
    )

    featured_section_2_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display above the promo copy"
    )
    featured_section_2 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Second featured section for the homepage. Will display up to "
        "three child items.",
        verbose_name="Featured section 2",
    )

    featured_section_3_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display above the promo copy"
    )
    featured_section_3 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Third featured section for the homepage. Will display up to "
        "six child items.",
        verbose_name="Featured section 3",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_title"),
                FieldPanel("hero_text"),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_cta"),
                        FieldPanel("hero_cta_link"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("achievement_card_1_image"),
                        FieldPanel("achievement_card_1_num"),
                        FieldPanel("achievement_card_1_text"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("achievement_card_2_image"),
                        FieldPanel("achievement_card_2_num"),
                        FieldPanel("achievement_card_2_text"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("achievement_card_3_image"),
                        FieldPanel("achievement_card_3_num"),
                        FieldPanel("achievement_card_3_text"),
                    ]
                ),
            ],
            heading="Hero Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("promo_image"),
                FieldPanel("promo_title"),
                FieldPanel("promo_text"),
            ],
            heading="Promo Section",
        ),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_1_title"),
                        FieldPanel("featured_section_1"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_2_title"),
                        FieldPanel("featured_section_2"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_3_title"),
                        FieldPanel("featured_section_3"),
                    ]
                ),
            ],
            heading="Featured Homepage Sections",
        ),
    ]

    def __str__(self):
        return self.title