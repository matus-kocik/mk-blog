from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, StructBlock, URLBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


class ArticlePage(Page):
    date_published = models.DateField("Publication Date", auto_now_add=True)
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    summary = models.CharField(
        max_length=250, blank=True, help_text="Short introduction to the article"
    )
    is_published = models.BooleanField(default=True)

    content = StreamField(
        [
            ("text", RichTextBlock()),
            ("image", ImageChooserBlock()),
            (
                "quote",
                StructBlock(
                    [
                        ("quote", RichTextBlock()),
                        ("author", RichTextBlock()),
                    ]
                ),
            ),
            ("link", URLBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("thumbnail"),
        FieldPanel("summary"),
        FieldPanel("is_published"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
