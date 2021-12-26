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
    'Message',
    'MessageId',
    'MessageEntity',
    'MessageAutoDeleteTimerChanged',
    'ForceReply',
)

class Message:
    '''
    This object represents a message.
    '''

    def __init__(
        self,
        *,
        message_id: int,
        date: int,
        chat: Chat,
        **kwargs
    ):
        self.message_id: int = message_id
        self.date: int = date
        self.chat: Chat = chat

        self.From: Optional[User] = kwargs.get('From', None)
        self.sender_chat: Optional[Chat] = kwargs.get('sender_chat', None)
        self.forward_from: Optional[User] = kwargs.get('forward_from', None)
        self.forward_from_chat: Optional[Chat] = kwargs.get(
            'forward_from_chat', None)
        self.forward_from_message_id: Optional[int] = kwargs.get(
            'forward_from_message_id', None)
        self.forward_signature: Optional[str] = kwargs.get(
            'forward_signature', None)
        self.forward_sender_name: Optional[str] = kwargs.get(
            'forward_sender_name', None)
        self.forward_date: Optional[int] = kwargs.get('forward_date', None)
        self.is_automatic_forward: Optional[bool] = kwargs.get(
            'is_automatic_forward', None)
        self.reply_to_message: Optional[Message] = kwargs.get(
            'reply_to_message', None)
        self.via_bot: Optional[User] = kwargs.get('via_bot', None)
        self.edit_date: Optional[int] = kwargs.get('edit_date', None)
        self.has_protected_content: Optional[bool] = kwargs.get(
            'has_protected_content', None)
        self.media_group_id: Optional[str] = kwargs.get('media_group_id', None)
        self.author_signature: Optional[str] = kwargs.get(
            'author_signature', None)
        self.text: Optional[str] = kwargs.get('text', None)
        self.entities: Optional[list[MessageEntity]
                                ] = kwargs.get('entities', None)
        self.animation: Optional[Animation] = kwargs.get('animation', None)
        self.audio: Optional[Audio] = kwargs.get('audio', None)
        self.document: Optional[Document] = kwargs.get('document', None)
        self.photo: Optional[list[PhotoSize]] = kwargs.get('photo', None)
        self.sticker: Optional[Sticker] = kwargs.get('sticker', None)
        self.video: Optional[Video] = kwargs.get('video', None)
        self.video_note: Optional[VideoNote] = kwargs.get('video_note', None)
        self.voice: Optional[Voice] = kwargs.get('voice', None)
        self.caption: Optional[str] = kwargs.get('caption', None)
        self.caption_entities: Optional[list[MessageEntity]] = kwargs.get(
            'caption_entities', None)
        self.contact: Optional[Contact] = kwargs.get('contact', None)
        self.dice: Optional[Dice] = kwargs.get('dice', None)
        self.game: Optional[Game] = kwargs.get('game', None)
        self.poll: Optional[Poll] = kwargs.get('poll', None)
        self.venue: Optional[Venue] = kwargs.get('venue', None)
        self.location: Optional[Location] = kwargs.get('location', None)
        self.new_chat_members: Optional[list[User]] = kwargs.get(
            'new_chat_members', None)
        self.left_chat_member: Optional[User] = kwargs.get(
            'left_chat_member', None)
        self.new_chat_title: Optional[str] = kwargs.get('new_chat_title', None)
        self.new_chat_photo: Optional[list[PhotoSize]] = kwargs.get(
            'new_chat_photo', None)
        self.delete_chat_photo: Optional[bool] = kwargs.get(
            'delete_chat_photo', None)
        self.group_chat_created: Optional[bool] = kwargs.get(
            'group_chat_created', None)
        self.supergroup_chat_created: Optional[bool] = kwargs.get(
            'supergroup_chat_created', None)
        self.channel_chat_created: Optional[bool] = kwargs.get(
            'channel_chat_created', None)
        self.message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = kwargs.get(
            'message_auto_delete_timer_changed', None)
        self.migrate_to_chat_id: Optional[int] = kwargs.get(
            'migrate_to_chat_id', None)
        self.migrate_from_chat_id: Optional[int] = kwargs.get(
            'migrate_from_chat_id', None)
        self.pinned_message: Optional[Message] = kwargs.get(
            'pinned_message', None)
        self.invoice: Optional[Invoice] = kwargs.get('invoice', None)
        self.successful_payment: Optional[SuccessfulPayment] = kwargs.get(
            'successful_payment', None)
        self.connected_website: Optional[str] = kwargs.get(
            'connected_website', None)
        self.passport_data: Optional[PassportData] = kwargs.get(
            'passport_data', None)
        self.proximity_alert_triggered: Optional[ProximityAlertTriggered] = kwargs.get(
            'proximity_alert_triggered', None)
        self.voice_chat_scheduled: Optional[VoiceChatScheduled] = kwargs.get(
            'voice_chat_scheduled', None)
        self.voice_chat_started: Optional[VoiceChatStarted] = kwargs.get(
            'voice_chat_started', None)
        self.voice_chat_ended: Optional[VoiceChatEnded] = kwargs.get(
            'voice_chat_ended', None)
        self.voice_chat_participants_invited: Optional[VoiceChatParticipantsInvited] = kwargs.get(
            'voice_chat_participants_invited', None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = kwargs.get(
            'reply_markup', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Message object @{hex(id(self))} message_id={self.message_id} date={self.date}>"


class MessageId:
    '''
    This object represents a unique message identifier.
    '''

    def __init__(
        self,
        *,
        message_id: int,
        **kwargs
    ):
        self.message_id: int = message_id

    def __repr__(self):
        return f"<Telpy.extension.Objects.MessageId object @{hex(id(self))} message_id={self.message_id}>"


class MessageEntity:
    '''
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    '''

    def __init__(
        self,
        *,
        type: str,
        offset: int,
        length: int,
        **kwargs
    ):
        self.type: str = type
        self.offset: int = offset
        self.length: int = length

        self.url: Optional[str] = kwargs.get('url', None)
        self.user: Optional[User] = kwargs.get('user', None)
        self.language: Optional[str] = kwargs.get('language', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.MessageEntity object @{hex(id(self))} type={self.type} offset={self.offset} length={self.length}>"


class MessageAutoDeleteTimerChanged:
    '''
    This object represents a service message about a change in auto-delete timer settings.
    '''

    def __init__(
        self,
        *,
        message_auto_delete_time: int,
        **kwargs
    ):
        self.message_auto_delete_time: int = message_auto_delete_time

    def __repr__(self):
        return f"<Telpy.extension.Objects.MessageAutoDeleteTimerChanged object @{hex(id(self))} message_auto_delete_time={self.message_auto_delete_time}>"


class ForceReply:
    '''
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    '''

    def __init__(
        self,
        *,
        force_reply: bool,
        **kwargs
    ):
        self.force_reply: bool = force_reply

        self.input_field_placeholder: Optional[str] = kwargs.get(
            'input_field_placeholder', None)
        self.selective: Optional[bool] = kwargs.get('selective', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ForceReply object @{hex(id(self))} force_reply={self.force_reply}>"
