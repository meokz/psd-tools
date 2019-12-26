from psd_tools.api import deprecated
from typing import Any, Optional, Iterator, Union


class Layer(object):
    def __init__(self, psd, record, channels, parent):
        ...

    @property
    def name(self):
        """
        Layer name. Writable.

        :return: `str`
        """
        ...

    @name.setter
    def name(self, value):
        ...

    @property
    def kind(self):
        """
        Kind of this layer, such as group, pixel, shape, type, smartobject,
        or psdimage. Class name without `layer` suffix.

        :return: `str`
        """
        ...

    @property
    def layer_id(self):
        """
        Layer ID.

        :return: int layer id. if the layer is not assigned an id, -1.
        """
        ...

    @property
    def visible(self):
        """
        Layer visibility. Doesn't take group visibility in account. Writable.

        :return: `bool`
        """
        ...

    @visible.setter
    def visible(self, value):
        ...

    def is_visible(self):
        """
        Layer visibility. Takes group visibility in account.

        :return: `bool`
        """
        ...

    @property
    def opacity(self):
        """
        Opacity of this layer in [0, 255] range. Writable.

        :return: int
        """
        ...

    @opacity.setter
    def opacity(self, value):
        ...

    @property
    def parent(self):
        """Parent of this layer."""
        ...

    def is_group(self):
        """
        Return True if the layer is a group.

        :return: `bool`
        """
        ...

    @property
    def blend_mode(self):
        """
        Blend mode of this layer. Writable.

        Example::

            from psd_tools.constants import BlendMode
            if layer.blend_mode == BlendMode.NORMAL:
                layer.blend_mode = BlendMode.SCREEN

        :return: :py:class:`~psd_tools.constants.BlendMode`.
        """
        ...

    @blend_mode.setter
    def blend_mode(self, value):
        ...

    def has_mask(self):
        """Returns True if the layer has a mask."""
        ...

    @property
    def left(self):
        """
        Left coordinate. Writable.

        :return: int
        """
        ...

    @left.setter
    def left(self, value):
        ...

    @property
    def top(self):
        """
        Top coordinate. Writable.

        :return: int
        """
        ...

    @top.setter
    def top(self, value):
        ...

    @property
    def right(self):
        """
        Right coordinate.

        :return: int
        """
        ...

    @property
    def bottom(self):
        """
        Bottom coordinate.

        :return: int
        """
        ...

    @property
    def width(self):
        """
        Width of the layer.

        :return: int
        """
        ...

    @property
    def height(self):
        """
        Height of the layer.

        :return: int
        """
        ...

    @property
    def offset(self):
        """
        (left, top) tuple. Writable.

        :return: `tuple`
        """
        ...

    @offset.setter
    def offset(self, value):
        ...

    @property
    def size(self):
        """
        (width, height) tuple.

        :return: `tuple`
        """
        ...

    @property
    def bbox(self):
        """(left, top, right, bottom) tuple."""
        ...

    def has_pixels(self):
        """
        Returns True if the layer has associated pixels. When this is True,
        `topil` method returns :py:class:`PIL.Image`.

        :return: `bool`
        """
        ...

    def has_mask(self):
        """
        Returns True if the layer has a mask.

        :return: `bool`
        """
        ...

    @property
    def mask(self):
        """
        Returns mask associated with this layer.

        :return: :py:class:`~psd_tools.api.mask.Mask` or `None`
        """
        ...

    def has_vector_mask(self):
        """
        Returns True if the layer has a vector mask.

        :return: `bool`
        """
        ...

    @property
    def vector_mask(self):
        """
        Returns vector mask associated with this layer.

        :return: :py:class:`~psd_tools.api.shape.VectorMask` or `None`
        """
        ...

    def has_origination(self):
        """
        Returns True if the layer has live shape properties.

        :return: `bool`
        """
        ...

    @property
    def origination(self):
        """
        Property for a list of live shapes or a line.

        Some of the vector masks have associated live shape properties, that
        are Photoshop feature to handle primitive shapes such as a rectangle,
        an ellipse, or a line. Vector masks without live shape properties are
        plain path objects.

        See :py:mod:`psd_tools.api.shape`.

        :return: List of :py:class:`~psd_tools.api.shape.Invalidated`,
            :py:class:`~psd_tools.api.shape.Rectangle`,
            :py:class:`~psd_tools.api.shape.RoundedRectangle`,
            :py:class:`~psd_tools.api.shape.Ellipse`, or
            :py:class:`~psd_tools.api.shape.Line`.
        """
        ...

    def has_stroke(self):
        """Returns True if the shape has a stroke."""
        ...

    @property
    def stroke(self):
        """Property for strokes."""
        ...

    def topil(self, channel: Optional[Any] = ..., **kwargs):
        """
        Get PIL Image of the layer.

        :param channel: Which channel to return; e.g., 0 for 'R' channel in RGB
            image. See :py:class:`~psd_tools.constants.ChannelID`. When `None`,
            the method returns all the channels supported by PIL modes.
        :return: :py:class:`PIL.Image`, or `None` if the layer has no pixels.

        Example::

            from psd_tools.constants import ChannelID

            image = layer.topil()
            red = layer.topil(ChannelID.CHANNEL_0)
            alpha = layer.topil(ChannelID.TRANSPARENCY_MASK)

        .. note:: Not all of the PSD image modes are supported in
            :py:class:`PIL.Image`. For example, 'CMYK' mode cannot include
            alpha channel in PIL. In this case, topil drops alpha channel.
        """
        ...

    def compose(self, bbox: Optional[Any] = ..., **kwargs):
        """
        Compose layer and masks (mask, vector mask, and clipping layers).

        Note that the resulting image size is not necessarily equal to the
        layer size due to different mask dimensions. The offset of the
        composed image is stored at `.info['offset']` attribute of `PIL.Image`.

        :param bbox: Viewport bounding box specified by (x1, y1, x2, y2) tuple.
        :return: :py:class:`PIL.Image`, or `None` if the layer has no pixel.
        """
        ...

    def has_clip_layers(self):
        """
        Returns True if the layer has associated clipping.

        :return: `bool`
        """
        ...

    @property
    def clip_layers(self):
        """
        Clip layers associated with this layer.

        To compose clipping layers::

            from psd_tools import compose
            clip_mask = compose(layer.clip_layers)

        :return: list of layers
        """
        ...

    def has_effects(self):
        """
        Returns True if the layer has effects.

        :return: `bool`
        """
        ...

    @property
    def effects(self):
        """
        Layer effects.

        :return: :py:class:`~psd_tools.api.effects.Effects`
        """
        ...

    @property
    def tagged_blocks(self):
        """
        Layer tagged blocks that is a dict-like container of settings.

        See :py:class:`psd_tools.constants.Tag` for available
        keys.

        :return: :py:class:`~psd_tools.psd.tagged_blocks.TaggedBlocks` or
            `None`.

        Example::

            from psd_tools.constants import Tag
            metadata = layer.tagged_blocks.get_data(Tag.METADATA_SETTING)
        """
        ...

    def __repr__(self):
        ...

    @deprecated
    def as_PIL(self, *args, **kwargs):
        ...

    @property
    @deprecated
    def flags(self):
        ...

    @deprecated
    def has_box(self):
        ...

    @deprecated
    def has_relevant_pixels(self):
        ...


class GroupMixin(object):
    @property
    def left(self):
        ...

    @property
    def top(self):
        ...

    @property
    def right(self):
        ...

    @property
    def bottom(self):
        ...

    @property
    def bbox(self):
        """(left, top, right, bottom) tuple."""
        ...

    def __len__(self):
        ...

    def __iter__(self) -> Iterator[Union[Layer, GroupMixin]]:
        ...

    def __getitem__(self, key):
        ...

    def __setitem__(self, key, value):
        ...

    def __delitem__(self, key):
        ...

    def compose(self, **kwargs):
        """
        Compose layer and masks (mask, vector mask, and clipping layers).

        :return: PIL Image object, or None if the layer has no pixels.
        """
        ...

    def descendants(self, include_clip: bool = ...):
        """
        Return a generator to iterate over all descendant layers.

        Example::

            # Iterate over all layers
            for layer in psd.descendants():
                print(layer)

            # Iterate over all layers in reverse order
            for layer in reversed(list(psd.descendants())):
                print(layer)

        :param include_clip: include clipping layers.
        """
        ...


class Group(GroupMixin, Layer):
    """
    Group of layers.

    Example::

        group = psd[1]
        for layer in group:
            if layer.kind == 'pixel':
                print(layer.name)
    """
    @staticmethod
    def extract_bbox(layers, include_invisible: bool = ...):
        """
        Returns a bounding box for ``layers`` or (0, 0, 0, 0) if the layers
        have no bounding box.

        :param include_invisible: include invisible layers in calculation.
        :return: tuple of four int
        """
        ...

    def __init__(self, *args):
        ...

    @property
    def _setting(self):
        ...

    @property
    def blend_mode(self):
        ...

    @blend_mode.setter
    def blend_mode(self, value):
        ...


class Artboard(Group):
    """
    Artboard is a special kind of group that has a pre-defined viewbox.

    Example::

        artboard = psd[1]
        image = artboard.compose()
    """
    @classmethod
    def _move(kls, group):
        ...

    @property
    def left(self):
        ...

    @property
    def top(self):
        ...

    @property
    def right(self):
        ...

    @property
    def bottom(self):
        ...

    @property
    def bbox(self):
        """(left, top, right, bottom) tuple."""
        ...

    def compose(self, bbox: Optional[Any] = ..., **kwargs):
        """
        Compose the artboard.

        See :py:func:`~psd_tools.compose` for available extra arguments.

        :param bbox: Viewport tuple (left, top, right, bottom).
        :return: :py:class:`PIL.Image`, or `None` if there is no pixel.
        """
        ...


class PixelLayer(Layer):
    """
    Layer that has rasterized image in pixels.

    Example::

        assert layer.kind == 'pixel':
        image = layer.topil()
        image.save('layer.png')

        composed_image = layer.compose()
        composed_image.save('composed-layer.png')
    """
    ...


class SmartObjectLayer(Layer):
    """
    Layer that inserts external data.

    Use :py:attr:`~psd_tools.api.layers.SmartObjectLayer.smart_object`
    attribute to get the external data. See
    :py:class:`~psd_tools.api.smart_object.SmartObject`.

    Example::

        import io
        if layer.smart_object.filetype == 'jpg':
            image = Image.open(io.BytesIO(layer.smart_object.data))
    """
    @property
    def smart_object(self):
        """
        Associated smart object.

        :return: :py:class:`~psd_tools.api.smart_object.SmartObject`.
        """
        ...

    @property
    @deprecated
    def unique_id(self):
        ...

    @property
    @deprecated
    def linked_data(self):
        ...


class TypeLayer(Layer):
    """
    Layer that has text and styling information for fonts or paragraphs.

    Text is accessible at :py:attr:`~psd_tools.api.layers.TypeLayer.text`
    property. Styling information for paragraphs is in
    :py:attr:`~psd_tools.api.layers.TypeLayer.engine_dict`.
    Document styling information such as font list is is
    :py:attr:`~psd_tools.api.layers.TypeLayer.resource_dict`.

    Currently, textual information is read-only.

    Example::

        if layer.kind == 'type':
            print(layer.text)
            print(layer.engine_dict['StyleRun'])

            # Extract font for each substring in the text.
            text = layer.engine_dict['Editor']['Text'].value
            fontset = layer.resource_dict['FontSet']
            runlength = layer.engine_dict['StyleRun']['RunLengthArray']
            rundata = layer.engine_dict['StyleRun']['RunArray']
            index = 0
            for length, style in zip(runlength, rundata):
                substring = text[index:index + length]
                stylesheet = style['StyleSheet']['StyleSheetData']
                font = fontset[stylesheet['Font']]
                print('%r gets %s' % (substring, font))
                index += length
    """

    def __init__(self, *args) -> None: ...

    @property
    def text(self) -> str:
        """
        Text in the layer. Read-only.

        .. note:: New-line character in Photoshop is `'\\\\r'`.
        """
        ...

    @property
    def transform(self):
        """Matrix (xx, xy, yx, yy, tx, ty) applies affine transformation."""
        ...

    @property
    def _engine_data(self):
        """Styling and resource information."""
        ...

    @property
    def engine_dict(self):
        """Styling information dict."""
        ...

    @property
    def resource_dict(self):
        """Resource set."""
        ...

    @property
    def document_resources(self):
        """Resource set relevant to the document."""
        ...

    @property
    def warp(self):
        """Warp configuration."""
        ...

    @property
    @deprecated
    def fontset(self):
        ...

    @property
    @deprecated
    def engine_data(self):
        ...

    @property
    @deprecated
    def full_text(self):
        ...

    @property
    @deprecated
    def writing_direction(self):
        ...

    @deprecated
    def style_spans(self):
        ...


class ShapeLayer(Layer):
    """
    Layer that has drawing in vector mask.
    """
    @property
    def left(self):
        ...

    @property
    def top(self):
        ...

    @property
    def right(self):
        ...

    @property
    def bottom(self):
        ...

    @property
    def bbox(self):
        """(left, top, right, bottom) tuple."""
        ...


class AdjustmentLayer(Layer):
    """Layer that applies specified image adjustment effect."""

    def __init__(self, *args):
        ...

    def compose(self, **kwargs):
        """
        Adjustment layer is never composed.

        :return: None
        """
        ...


class FillLayer(Layer):
    """Layer that fills the canvas region."""

    def __init__(self, *args):
        ...

    @property
    def left(self):
        ...

    @property
    def top(self):
        ...

    @property
    def right(self):
        ...

    @property
    def bottom(self):
        ...
