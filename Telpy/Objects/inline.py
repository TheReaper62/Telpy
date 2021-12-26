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
    'InlineKeyboardButton',
    'InlineKeyboardMarkup',
    'InlineQuery',
    'InlineQueryResultArticle',
    'InlineQueryResultPhoto',
    'InlineQueryResultGif',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultVideo',
    'InlineQueryResultAudio',
    'InlineQueryResultVoice',
    'InlineQueryResultDocument',
    'InlineQueryResultLocation',
    'InlineQueryResultVenue',
    'InlineQueryResultContact',
    'InlineQueryResultGame',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultCachedAudio',
    'InputTextMessageContent',
    'InputLocationMessageContent',
    'InputVenueMessageContent',
    'InputContactMessageContent',
    'InputInvoiceMessageContent',
    'ChosenInlineResult',
)


class InlineKeyboardButton:
    '''
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    '''

    def __init__(
        self,
        *,
        text: str,
        **kwargs
    ):
        self.text: str = text

        self.url: Optional[str] = kwargs.get('url', None)
        self.login_url: Optional[LoginUrl] = kwargs.get('login_url', None)
        self.callback_data: Optional[str] = kwargs.get('callback_data', None)
        self.switch_inline_query: Optional[str] = kwargs.get(
            'switch_inline_query', None)
        self.switch_inline_query_current_chat: Optional[str] = kwargs.get(
            'switch_inline_query_current_chat', None)
        self.callback_game: Optional[CallbackGame] = kwargs.get(
            'callback_game', None)
        self.pay: Optional[bool] = kwargs.get('pay', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineKeyboardButton object @{hex(id(self))} text={self.text}>"


class InlineKeyboardMarkup:
    '''
    This object represents an inline keyboard that appears right next to the message it belongs to.
    '''

    def __init__(
        self,
        *,
        inline_keyboard: list[list[InlineKeyboardButton]],
        **kwargs
    ):
        self.inline_keyboard: list[list[InlineKeyboardButton]
                                   ] = inline_keyboard

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineKeyboardMarkup object @{hex(id(self))} >"


class LoginUrl:
    '''
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in. Telegram apps support these buttons as of version 5.7.
    '''

    def __init__(
        self,
        *,
        url: str,
        **kwargs
    ):
        self.url: str = url

        self.forward_text: Optional[str] = kwargs.get('forward_text', None)
        self.bot_username: Optional[str] = kwargs.get('bot_username', None)
        self.request_write_access: Optional[bool] = kwargs.get(
            'request_write_access', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.LoginUrl object @{hex(id(self))} url={self.url}>"


class CallbackQuery:
    '''
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    '''

    def __init__(
        self,
        *,
        id: str,
        From: User,
        chat_instance: str,
        **kwargs
    ):
        self.id: str = id
        self.From: User = From
        self.chat_instance: str = chat_instance

        self.message: Optional[Message] = kwargs.get('message', None)
        self.inline_message_id: Optional[str] = kwargs.get(
            'inline_message_id', None)
        self.data: Optional[str] = kwargs.get('data', None)
        self.game_short_name: Optional[str] = kwargs.get(
            'game_short_name', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.CallbackQuery object @{hex(id(self))} id={self.id} chat_instance={self.chat_instance}>"

class InlineQuery:
    '''
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
    '''

    def __init__(
        self,
        *,
        id: str,
        From: User,
        query: str,
        offset: str,
        **kwargs
    ):
        self.id: str = id
        self.From: User = From
        self.query: str = query
        self.offset: str = offset

        self.chat_type: Optional[str] = kwargs.get('chat_type', None)
        self.location: Optional[Location] = kwargs.get('location', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQuery object @{hex(id(self))} id={self.id} query={self.query} offset={self.offset}>"

InputMessageContent = Union[
    'InputTextMessageContent',
    'InputLocationMessageContent',
    'InputVenueMessageContent',
    'InputContactMessageContent',
    'InputInvoiceMessageContent',
]

class InlineQueryResultArticle:
    '''
    Represents a link to an article or web page.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        input_message_content: InputMessageContent,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.title: str = title
        self.input_message_content: InputMessageContent = input_message_content

        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.url: Optional[str] = kwargs.get('url',None)
        self.hide_url: Optional[bool] = kwargs.get('hide_url',None)
        self.description: Optional[str] = kwargs.get('description',None)
        self.thumb_url: Optional[str] = kwargs.get('thumb_url',None)
        self.thumb_width: Optional[int] = kwargs.get('thumb_width',None)
        self.thumb_height: Optional[int] = kwargs.get('thumb_height',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultArticle object @{hex(id(self))} type={self.type} id={self.id} title={self.title}>"

class InlineQueryResultPhoto:
    '''
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        photo_url: str,
        thumb_url: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.photo_url: str = photo_url
        self.thumb_url: str = thumb_url

        self.photo_width: Optional[int] = kwargs.get('photo_width',None)
        self.photo_height: Optional[int] = kwargs.get('photo_height',None)
        self.title: Optional[str] = kwargs.get('title',None)
        self.description: Optional[str] = kwargs.get('description',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultPhoto object @{hex(id(self))} type={self.type} id={self.id} photo_url={self.photo_url} thumb_url={self.thumb_url}>"

class InlineQueryResultGif:
    '''
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        gif_url: str,
        thumb_url: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.gif_url: str = gif_url
        self.thumb_url: str = thumb_url

        self.gif_width: Optional[int] = kwargs.get('gif_width',None)
        self.gif_height: Optional[int] = kwargs.get('gif_height',None)
        self.gif_duration: Optional[int] = kwargs.get('gif_duration',None)
        self.thumb_mime_type: Optional[str] = kwargs.get('thumb_mime_type',None)
        self.title: Optional[str] = kwargs.get('title',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultGif object @{hex(id(self))} type={self.type} id={self.id} gif_url={self.gif_url} thumb_url={self.thumb_url}>"

class InlineQueryResultMpeg4Gif:
    '''
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        mpeg4_url: str,
        thumb_url: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.mpeg4_url: str = mpeg4_url
        self.thumb_url: str = thumb_url

        self.mpeg4_width: Optional[int] = kwargs.get('mpeg4_width',None)
        self.mpeg4_height: Optional[int] = kwargs.get('mpeg4_height',None)
        self.mpeg4_duration: Optional[int] = kwargs.get('mpeg4_duration',None)
        self.thumb_mime_type: Optional[str] = kwargs.get('thumb_mime_type',None)
        self.title: Optional[str] = kwargs.get('title',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultMpeg4Gif object @{hex(id(self))} type={self.type} id={self.id} mpeg4_url={self.mpeg4_url} thumb_url={self.thumb_url}>"

class InlineQueryResultVideo:
    '''
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video. If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        video_url: str,
        mime_type: str,
        thumb_url: str,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.video_url: str = video_url
        self.mime_type: str = mime_type
        self.thumb_url: str = thumb_url
        self.title: str = title

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.video_width: Optional[int] = kwargs.get('video_width',None)
        self.video_height: Optional[int] = kwargs.get('video_height',None)
        self.video_duration: Optional[int] = kwargs.get('video_duration',None)
        self.description: Optional[str] = kwargs.get('description',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultVideo object @{hex(id(self))} type={self.type} id={self.id} video_url={self.video_url} mime_type={self.mime_type} thumb_url={self.thumb_url} title={self.title}>"

class InlineQueryResultAudio:
    '''
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        audio_url: str,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.audio_url: str = audio_url
        self.title: str = title

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.performer: Optional[str] = kwargs.get('performer',None)
        self.audio_duration: Optional[int] = kwargs.get('audio_duration',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultAudio object @{hex(id(self))} type={self.type} id={self.id} audio_url={self.audio_url} title={self.title}>"

class InlineQueryResultVoice:
    '''
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        voice_url: str,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.voice_url: str = voice_url
        self.title: str = title

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.voice_duration: Optional[int] = kwargs.get('voice_duration',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultVoice object @{hex(id(self))} type={self.type} id={self.id} voice_url={self.voice_url} title={self.title}>"

class InlineQueryResultDocument:
    '''
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        document_url: str,
        mime_type: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.title: str = title
        self.document_url: str = document_url
        self.mime_type: str = mime_type

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.description: Optional[str] = kwargs.get('description',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)
        self.thumb_url: Optional[str] = kwargs.get('thumb_url',None)
        self.thumb_width: Optional[int] = kwargs.get('thumb_width',None)
        self.thumb_height: Optional[int] = kwargs.get('thumb_height',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultDocument object @{hex(id(self))} type={self.type} id={self.id} title={self.title} document_url={self.document_url} mime_type={self.mime_type}>"

class InlineQueryResultLocation:
    '''
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.title: str = title

        self.horizontal_accuracy: Optional[float] = kwargs.get('horizontal_accuracy',None)
        self.live_period: Optional[int] = kwargs.get('live_period',None)
        self.heading: Optional[int] = kwargs.get('heading',None)
        self.proximity_alert_radius: Optional[int] = kwargs.get('proximity_alert_radius',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)
        self.thumb_url: Optional[str] = kwargs.get('thumb_url',None)
        self.thumb_width: Optional[int] = kwargs.get('thumb_width',None)
        self.thumb_height: Optional[int] = kwargs.get('thumb_height',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultLocation object @{hex(id(self))} type={self.type} id={self.id} title={self.title}>"

class InlineQueryResultVenue:
    '''
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.title: str = title
        self.address: str = address

        self.foursquare_id: Optional[str] = kwargs.get('foursquare_id',None)
        self.foursquare_type: Optional[str] = kwargs.get('foursquare_type',None)
        self.google_place_id: Optional[str] = kwargs.get('google_place_id',None)
        self.google_place_type: Optional[str] = kwargs.get('google_place_type',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)
        self.thumb_url: Optional[str] = kwargs.get('thumb_url',None)
        self.thumb_width: Optional[int] = kwargs.get('thumb_width',None)
        self.thumb_height: Optional[int] = kwargs.get('thumb_height',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultVenue object @{hex(id(self))} type={self.type} id={self.id} latitude={self.latitude} longitude={self.longitude} title={self.title} address={self.address}>"

class InlineQueryResultContact:
    '''
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        phone_number: str,
        first_name: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.phone_number: str = phone_number
        self.first_name: str = first_name

        self.last_name: Optional[str] = kwargs.get('last_name',None)
        self.vcard: Optional[str] = kwargs.get('vcard',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)
        self.thumb_url: Optional[str] = kwargs.get('thumb_url',None)
        self.thumb_width: Optional[int] = kwargs.get('thumb_width',None)
        self.thumb_height: Optional[int] = kwargs.get('thumb_height',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultContact object @{hex(id(self))} type={self.type} id={self.id} phone_number={self.phone_number} first_name={self.first_name}>"

class InlineQueryResultGame:
    '''
    Represents a Game.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        game_short_name: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.game_short_name: str = game_short_name

        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultGame object @{hex(id(self))} type={self.type} id={self.id} game_short_name={self.game_short_name}>"

class InlineQueryResultCachedPhoto:
    '''
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        photo_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.photo_file_id: str = photo_file_id

        self.title: Optional[str] = kwargs.get('title',None)
        self.description: Optional[str] = kwargs.get('description',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedPhoto object @{hex(id(self))} type={self.type} id={self.id} photo_file_id={self.photo_file_id}>"

class InlineQueryResultCachedGif:
    '''
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        gif_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.gif_file_id: str = gif_file_id

        self.title: Optional[str] = kwargs.get('title',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedGif object @{hex(id(self))} type={self.type} id={self.id} gif_file_id={self.gif_file_id}>"

class InlineQueryResultCachedMpeg4Gif:
    '''
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        mpeg4_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.mpeg4_file_id: str = mpeg4_file_id

        self.title: Optional[str] = kwargs.get('title',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedMpeg4Gif object @{hex(id(self))} type={self.type} id={self.id} mpeg4_file_id={self.mpeg4_file_id}>"

class InlineQueryResultCachedSticker:
    '''
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        sticker_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.sticker_file_id: str = sticker_file_id

        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedSticker object @{hex(id(self))} type={self.type} id={self.id} sticker_file_id={self.sticker_file_id}>"

class InlineQueryResultCachedDocument:
    '''
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        document_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.title: str = title
        self.document_file_id: str = document_file_id

        self.description: Optional[str] = kwargs.get('description',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedDocument object @{hex(id(self))} type={self.type} id={self.id} title={self.title} document_file_id={self.document_file_id}>"

class InlineQueryResultCachedVideo:
    '''
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        video_file_id: str,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.video_file_id: str = video_file_id
        self.title: str = title

        self.description: Optional[str] = kwargs.get('description',None)
        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedVideo object @{hex(id(self))} type={self.type} id={self.id} video_file_id={self.video_file_id} title={self.title}>"

class InlineQueryResultCachedVoice:
    '''
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        voice_file_id: str,
        title: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.voice_file_id: str = voice_file_id
        self.title: str = title

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedVoice object @{hex(id(self))} type={self.type} id={self.id} voice_file_id={self.voice_file_id} title={self.title}>"

class InlineQueryResultCachedAudio:
    '''
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(
        self,
        *,
        type: str,
        id: str,
        audio_file_id: str,
        **kwargs
    ):
        self.type: str = type
        self.id: str = id
        self.audio_file_id: str = audio_file_id

        self.caption: Optional[str] = kwargs.get('caption',None)
        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get('caption_entities',None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get('reply_markup',None)
        self.input_message_content: Optional[InputMessageContent] = kwargs.get('input_message_content',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InlineQueryResultCachedAudio object @{hex(id(self))} type={self.type} id={self.id} audio_file_id={self.audio_file_id}>"

class InputTextMessageContent:
    '''
    Represents the content of a text message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        *,
        message_text: str,
        **kwargs
    ):
        self.message_text: str = message_text

        self.parse_mode: Optional[str] = kwargs.get('parse_mode',None)
        self.entities: Optional[list[MessageEntity]] = kwargs.get('entities',None)
        self.disable_web_page_preview: Optional[bool] = kwargs.get('disable_web_page_preview',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputTextMessageContent object @{hex(id(self))} message_text={self.message_text}>"

class InputLocationMessageContent:
    '''
    Represents the content of a location message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        *,
        latitude: float,
        longitude: float,
        **kwargs
    ):
        self.latitude: float = latitude
        self.longitude: float = longitude

        self.horizontal_accuracy: Optional[float] = kwargs.get('horizontal_accuracy',None)
        self.live_period: Optional[int] = kwargs.get('live_period',None)
        self.heading: Optional[int] = kwargs.get('heading',None)
        self.proximity_alert_radius: Optional[int] = kwargs.get('proximity_alert_radius',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputLocationMessageContent object @{hex(id(self))} latitude={self.latitude} longitude={self.longitude}>"

class InputVenueMessageContent:
    '''
    Represents the content of a venue message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        *,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        **kwargs
    ):
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.title: str = title
        self.address: str = address

        self.foursquare_id: Optional[str] = kwargs.get('foursquare_id',None)
        self.foursquare_type: Optional[str] = kwargs.get('foursquare_type',None)
        self.google_place_id: Optional[str] = kwargs.get('google_place_id',None)
        self.google_place_type: Optional[str] = kwargs.get('google_place_type',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputVenueMessageContent object @{hex(id(self))} latitude={self.latitude} longitude={self.longitude} title={self.title} address={self.address}>"

class InputContactMessageContent:
    '''
    Represents the content of a contact message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        *,
        phone_number: str,
        first_name: str,
        **kwargs
    ):
        self.phone_number: str = phone_number
        self.first_name: str = first_name

        self.last_name: Optional[str] = kwargs.get('last_name',None)
        self.vcard: Optional[str] = kwargs.get('vcard',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputContactMessageContent object @{hex(id(self))} phone_number={self.phone_number} first_name={self.first_name}>"

class InputInvoiceMessageContent:
    '''
    Represents the content of an invoice message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        *,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        **kwargs
    ):
        self.title: str = title
        self.description: str = description
        self.payload: str = payload
        self.provider_token: str = provider_token
        self.currency: str = currency
        self.prices: list[LabeledPrice] = prices

        self.max_tip_amount: Optional[int] = kwargs.get('max_tip_amount',None)
        self.suggested_tip_amounts: Optional[list[int]] = kwargs.get('suggested_tip_amounts',None)
        self.provider_data: Optional[str] = kwargs.get('provider_data',None)
        self.photo_url: Optional[str] = kwargs.get('photo_url',None)
        self.photo_size: Optional[int] = kwargs.get('photo_size',None)
        self.photo_width: Optional[int] = kwargs.get('photo_width',None)
        self.photo_height: Optional[int] = kwargs.get('photo_height',None)
        self.need_name: Optional[bool] = kwargs.get('need_name',None)
        self.need_phone_number: Optional[bool] = kwargs.get('need_phone_number',None)
        self.need_email: Optional[bool] = kwargs.get('need_email',None)
        self.need_shipping_address: Optional[bool] = kwargs.get('need_shipping_address',None)
        self.send_phone_number_to_provider: Optional[bool] = kwargs.get('send_phone_number_to_provider',None)
        self.send_email_to_provider: Optional[bool] = kwargs.get('send_email_to_provider',None)
        self.is_flexible: Optional[bool] = kwargs.get('is_flexible',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.InputInvoiceMessageContent object @{hex(id(self))} title={self.title} description={self.description} payload={self.payload} provider_token={self.provider_token} currency={self.currency}>"

class ChosenInlineResult:
    '''
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    '''
    def __init__(
        self,
        *,
        result_id: str,
        From: User,
        query: str,
        **kwargs
    ):
        self.result_id: str = result_id
        self.From: User = From
        self.query: str = query

        self.location: Optional[Location] = kwargs.get('location',None)
        self.inline_message_id: Optional[str] = kwargs.get('inline_message_id',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChosenInlineResult object @{hex(id(self))} result_id={self.result_id} query={self.query}>"
