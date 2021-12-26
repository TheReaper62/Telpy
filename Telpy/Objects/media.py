from __future__ import annotations

'''
MIT License

Copyright (c) 2021-Present Fishball_Noodles

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from typing import Optional, Union

from ..Objects import *

__all__ = (
    'PhotoSize',
    'Animation',
    'Audio',
    'Document',
    'Video',
    'VideoNote',
    'Voice',
    'File',
    'InputMediaPhoto',
    'InputFile',
    'InputMediaVideo',
    'InputMediaAnimation',
    'InputMediaAudio',
    'InputMediaDocument',
    'Sticker',
    'StickerSet',
    'MaskPosition',
)

class PhotoSize:
    '''
    This object represents one size of a photo or a file / sticker thumbnail.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height

        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.PhotoSize object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height}>"


class Animation:
    '''
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)
        self.file_name: Optional[str] = kwargs.get('file_name', None)
        self.mime_type: Optional[str] = kwargs.get('mime_type', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Animation object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} duration={self.duration}>"


class Audio:
    '''
    This object represents an audio file to be treated as music by the Telegram clients.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        duration: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.duration: int = duration

        self.performer: Optional[str] = kwargs.get('performer', None)
        self.title: Optional[str] = kwargs.get('title', None)
        self.file_name: Optional[str] = kwargs.get('file_name', None)
        self.mime_type: Optional[str] = kwargs.get('mime_type', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)
        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Audio object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} duration={self.duration}>"


class Document:
    '''
    This object represents a general file (as opposed to photos, voice messages and audio files).
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)
        self.file_name: Optional[str] = kwargs.get('file_name', None)
        self.mime_type: Optional[str] = kwargs.get('mime_type', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Document object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id}>"


class Video:
    '''
    This object represents a video file.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)
        self.file_name: Optional[str] = kwargs.get('file_name', None)
        self.mime_type: Optional[str] = kwargs.get('mime_type', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Video object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} duration={self.duration}>"


class VideoNote:
    '''
    This object represents a video message (available in Telegram apps as of v.4.0).
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.length: int = length
        self.duration: int = duration

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.VideoNote object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} length={self.length} duration={self.duration}>"


class Voice:
    '''
    This object represents a voice note.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        duration: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.duration: int = duration

        self.mime_type: Optional[str] = kwargs.get('mime_type', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Voice object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} duration={self.duration}>"


class File:
    '''
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile. Maximum file size to download is 20 MB.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id

        self.file_size: Optional[int] = kwargs.get('file_size', None)
        self.file_path: Optional[str] = kwargs.get('file_path', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.File object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id}>"


class InputMediaPhoto:
    '''
    Represents a photo to be sent.
    '''

    def __init__(
        self,
        *,
        type: str,
        media: str,
        **kwargs
    ):
        self.type: str = type
        self.media: str = media

        self.caption: Optional[str] = kwargs.get('caption', None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputMediaPhoto object @{hex(id(self))} type={self.type} media={self.media}>"


class InputFile:
    '''
    This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    '''

    def __init__(
        self,
        **kwargs
    ):
        pass


class InputMediaVideo:
    '''
    Represents a video to be sent.
    '''

    def __init__(
        self,
        *,
        type: str,
        media: str,
        **kwargs
    ):
        self.type: str = type
        self.media: str = media

        self.thumb: Optional[Union[InputFile, str]] = kwargs.get('thumb', None)
        self.caption: Optional[str] = kwargs.get('caption', None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)
        self.width: Optional[int] = kwargs.get('width', None)
        self.height: Optional[int] = kwargs.get('height', None)
        self.duration: Optional[int] = kwargs.get('duration', None)
        self.supports_streaming: Optional[bool] = kwargs.get(
            'supports_streaming', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputMediaVideo object @{hex(id(self))} type={self.type} media={self.media}>"


class InputMediaAnimation:
    '''
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    '''

    def __init__(
        self,
        *,
        type: str,
        media: str,
        **kwargs
    ):
        self.type: str = type
        self.media: str = media

        self.thumb: Optional[Union[InputFile, str]] = kwargs.get('thumb', None)
        self.caption: Optional[str] = kwargs.get('caption', None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)
        self.width: Optional[int] = kwargs.get('width', None)
        self.height: Optional[int] = kwargs.get('height', None)
        self.duration: Optional[int] = kwargs.get('duration', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputMediaAnimation object @{hex(id(self))} type={self.type} media={self.media}>"


class InputMediaAudio:
    '''
    Represents an audio file to be treated as music to be sent.
    '''

    def __init__(
        self,
        *,
        type: str,
        media: str,
        **kwargs
    ):
        self.type: str = type
        self.media: str = media

        self.thumb: Optional[Union[InputFile, str]] = kwargs.get('thumb', None)
        self.caption: Optional[str] = kwargs.get('caption', None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)
        self.duration: Optional[int] = kwargs.get('duration', None)
        self.performer: Optional[str] = kwargs.get('performer', None)
        self.title: Optional[str] = kwargs.get('title', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputMediaAudio object @{hex(id(self))} type={self.type} media={self.media}>"


class InputMediaDocument:
    '''
    Represents a general file to be sent.
    '''

    def __init__(
        self,
        *,
        type: str,
        media: str,
        **kwargs
    ):
        self.type: str = type
        self.media: str = media

        self.thumb: Optional[Union[InputFile, str]] = kwargs.get('thumb', None)
        self.caption: Optional[str] = kwargs.get('caption', None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)
        self.disable_content_type_detection: Optional[bool] = kwargs.get(
            'disable_content_type_detection', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputMediaDocument object @{hex(id(self))} type={self.type} media={self.media}>"


class Sticker:
    '''
    This object represents a sticker.
    '''

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        is_animated: bool,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.is_animated: bool = is_animated

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)
        self.emoji: Optional[str] = kwargs.get('emoji', None)
        self.set_name: Optional[str] = kwargs.get('set_name', None)
        self.mask_position: Optional[MaskPosition] = kwargs.get(
            'mask_position', None)
        self.file_size: Optional[int] = kwargs.get('file_size', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Sticker object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} is_animated={self.is_animated}>"


class StickerSet:
    '''
    This object represents a sticker set.
    '''

    def __init__(
        self,
        *,
        name: str,
        title: str,
        is_animated: bool,
        contains_masks: bool,
        stickers: list[Sticker],
        **kwargs
    ):
        self.name: str = name
        self.title: str = title
        self.is_animated: bool = is_animated
        self.contains_masks: bool = contains_masks
        self.stickers: list[Sticker] = stickers

        self.thumb: Optional[PhotoSize] = kwargs.get('thumb', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.StickerSet object @{hex(id(self))} name={self.name} title={self.title} is_animated={self.is_animated} contains_masks={self.contains_masks}>"


class MaskPosition:
    '''
    This object describes the position on faces where a mask should be placed by default.
    '''

    def __init__(
        self,
        *,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float,
        **kwargs
    ):
        self.point: str = point
        self.x_shift: float = x_shift
        self.y_shift: float = y_shift
        self.scale: float = scale

    def __repr__(self):
        return f"<Telpy.extension.Objects.MaskPosition object @{hex(id(self))} point={self.point} x_shift={self.x_shift} y_shift={self.y_shift} scale={self.scale}>"
