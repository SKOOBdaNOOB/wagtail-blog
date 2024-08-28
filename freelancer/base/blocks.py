from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


class CodeLineBlock(StructBlock):
    """
    Custom 'StructBlock' that allows the user to apply lines of code to their pages
    """
    prefix = CharBlock(
        required=False,
        max_length=10,
        help_text="Optional prefix (e.g., $, >) for the code line.",
        label="Data Prefix",
    )
    content = TextBlock(
        required=True,
        help_text="The code or message to display.",
        label="Code Line",
    )
    css_class = CharBlock(
        required=False,
        max_length=100,
        help_text="Optional CSS class for styling (e.g., text-warning, text-success).",
        label="CSS Class",
    )

    class Meta:
        template = "blocks/code_line.html"
        icon = "code"
        label = "Code Line"

class CodeMockupBlock(StructBlock):
    """
    Custom 'StructBlock' that combines the different code lines into a "code mockup" component designed by daisyUI
    https://daisyui.com/components/mockup-code/
    """
    lines = ListBlock(CodeLineBlock())

    class Meta:
        template = "blocks/code_mockup.html"
        icon = "code"
        label = "Code Mockup"



# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    code_block = CodeMockupBlock()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
    )

