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
    'Chat',
    'ChatPhoto',
    'ChatInviteLink',
    'ChatMemberOwner',
    'ChatMemberAdministrator',
    'ChatMemberMember',
    'ChatMemberRestricted',
    'ChatMemberLeft',
    'ChatMemberBanned',
    'ChatMemberUpdated',
    'ChatJoinRequest',
    'ChatPermissions',
    'ChatLocation',
)

class Chat:
    '''
    This object represents a chat.
    '''

    def __init__(
        self,
        *,
        id: int,
        type: str,
        **kwargs
    ):
        self.id: int = id
        self.type: str = type

        self.title: Optional[str] = kwargs.get('title', None)
        self.username: Optional[str] = kwargs.get('username', None)
        self.first_name: Optional[str] = kwargs.get('first_name', None)
        self.last_name: Optional[str] = kwargs.get('last_name', None)
        self.photo: Optional[ChatPhoto] = kwargs.get('photo', None)
        self.bio: Optional[str] = kwargs.get('bio', None)
        self.has_private_forwards: Optional[bool] = kwargs.get(
            'has_private_forwards', None)
        self.description: Optional[str] = kwargs.get('description', None)
        self.invite_link: Optional[str] = kwargs.get('invite_link', None)
        self.pinned_message: Optional[Message] = kwargs.get(
            'pinned_message', None)
        self.permissions: Optional[ChatPermissions] = kwargs.get(
            'permissions', None)
        self.slow_mode_delay: Optional[int] = kwargs.get(
            'slow_mode_delay', None)
        self.message_auto_delete_time: Optional[int] = kwargs.get(
            'message_auto_delete_time', None)
        self.has_protected_content: Optional[bool] = kwargs.get(
            'has_protected_content', None)
        self.sticker_set_name: Optional[str] = kwargs.get(
            'sticker_set_name', None)
        self.can_set_sticker_set: Optional[bool] = kwargs.get(
            'can_set_sticker_set', None)
        self.linked_chat_id: Optional[int] = kwargs.get('linked_chat_id', None)
        self.location: Optional[ChatLocation] = kwargs.get('location', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Chat object @{hex(id(self))} id={self.id} type={self.type}>"


class ChatPhoto:
    '''
    This object represents a chat photo.
    '''

    def __init__(
        self,
        *,
        small_file_id: str,
        small_file_unique_id: str,
        big_file_id: str,
        big_file_unique_id: str,
        **kwargs
    ):
        self.small_file_id: str = small_file_id
        self.small_file_unique_id: str = small_file_unique_id
        self.big_file_id: str = big_file_id
        self.big_file_unique_id: str = big_file_unique_id

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatPhoto object @{hex(id(self))} small_file_id={self.small_file_id} small_file_unique_id={self.small_file_unique_id} big_file_id={self.big_file_id} big_file_unique_id={self.big_file_unique_id}>"


class ChatInviteLink:
    '''
    Represents an invite link for a chat.
    '''

    def __init__(
        self,
        *,
        invite_link: str,
        creator: User,
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        **kwargs
    ):
        self.invite_link: str = invite_link
        self.creator: User = creator
        self.creates_join_request: bool = creates_join_request
        self.is_primary: bool = is_primary
        self.is_revoked: bool = is_revoked

        self.name: Optional[str] = kwargs.get('name', None)
        self.expire_date: Optional[int] = kwargs.get('expire_date', None)
        self.member_limit: Optional[int] = kwargs.get('member_limit', None)
        self.pending_join_request_count: Optional[int] = kwargs.get(
            'pending_join_request_count', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatInviteLink object @{hex(id(self))} invite_link={self.invite_link} creates_join_request={self.creates_join_request} is_primary={self.is_primary} is_revoked={self.is_revoked}>"


class ChatMemberOwner:
    '''
    Represents a chat member that owns the chat and has all administrator privileges.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        is_anonymous: bool,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user
        self.is_anonymous: bool = is_anonymous

        self.custom_title: Optional[str] = kwargs.get('custom_title', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberOwner object @{hex(id(self))} status={self.status} is_anonymous={self.is_anonymous}>"


class ChatMemberAdministrator:
    '''
    Represents a chat member that has some additional privileges.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        can_be_edited: bool,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_voice_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user
        self.can_be_edited: bool = can_be_edited
        self.is_anonymous: bool = is_anonymous
        self.can_manage_chat: bool = can_manage_chat
        self.can_delete_messages: bool = can_delete_messages
        self.can_manage_voice_chats: bool = can_manage_voice_chats
        self.can_restrict_members: bool = can_restrict_members
        self.can_promote_members: bool = can_promote_members
        self.can_change_info: bool = can_change_info
        self.can_invite_users: bool = can_invite_users

        self.can_post_messages: Optional[bool] = kwargs.get(
            'can_post_messages', None)
        self.can_edit_messages: Optional[bool] = kwargs.get(
            'can_edit_messages', None)
        self.can_pin_messages: Optional[bool] = kwargs.get(
            'can_pin_messages', None)
        self.custom_title: Optional[str] = kwargs.get('custom_title', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberAdministrator object @{hex(id(self))} status={self.status} can_be_edited={self.can_be_edited} is_anonymous={self.is_anonymous} can_manage_chat={self.can_manage_chat} can_delete_messages={self.can_delete_messages} can_manage_voice_chats={self.can_manage_voice_chats} can_restrict_members={self.can_restrict_members} can_promote_members={self.can_promote_members} can_change_info={self.can_change_info} can_invite_users={self.can_invite_users}>"


class ChatMemberMember:
    '''
    Represents a chat member that has no additional privileges or restrictions.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberMember object @{hex(id(self))} status={self.status}>"


class ChatMemberRestricted:
    '''
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        is_member: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_send_messages: bool,
        can_send_media_messages: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        until_date: int,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user
        self.is_member: bool = is_member
        self.can_change_info: bool = can_change_info
        self.can_invite_users: bool = can_invite_users
        self.can_pin_messages: bool = can_pin_messages
        self.can_send_messages: bool = can_send_messages
        self.can_send_media_messages: bool = can_send_media_messages
        self.can_send_polls: bool = can_send_polls
        self.can_send_other_messages: bool = can_send_other_messages
        self.can_add_web_page_previews: bool = can_add_web_page_previews
        self.until_date: int = until_date

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberRestricted object @{hex(id(self))} status={self.status} is_member={self.is_member} can_change_info={self.can_change_info} can_invite_users={self.can_invite_users} can_pin_messages={self.can_pin_messages} can_send_messages={self.can_send_messages} can_send_media_messages={self.can_send_media_messages} can_send_polls={self.can_send_polls} can_send_other_messages={self.can_send_other_messages} can_add_web_page_previews={self.can_add_web_page_previews} until_date={self.until_date}>"


class ChatMemberLeft:
    '''
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberLeft object @{hex(id(self))} status={self.status}>"


class ChatMemberBanned:
    '''
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    '''

    def __init__(
        self,
        *,
        status: str,
        user: User,
        until_date: int,
        **kwargs
    ):
        self.status: str = status
        self.user: User = user
        self.until_date: int = until_date

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberBanned object @{hex(id(self))} status={self.status} until_date={self.until_date}>"


class ChatMemberUpdated:
    '''
    This object represents changes in the status of a chat member.
    '''

    def __init__(
        self,
        *,
        chat: Chat,
        From: User,
        date: int,
        old_chat_member: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned],
        new_chat_member: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned],
        **kwargs
    ):
        self.chat: Chat = chat
        self.From: User = From
        self.date: int = date
        self.old_chat_member: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember,
                                    ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = old_chat_member
        self.new_chat_member: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember,
                                    ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = new_chat_member

        self.invite_link: Optional[ChatInviteLink] = kwargs.get(
            'invite_link', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatMemberUpdated object @{hex(id(self))} date={self.date}>"


class ChatJoinRequest:
    '''
    Represents a join request sent to a chat.
    '''

    def __init__(
        self,
        *,
        chat: Chat,
        From: User,
        date: int,
        **kwargs
    ):
        self.chat: Chat = chat
        self.From: User = From
        self.date: int = date

        self.bio: Optional[str] = kwargs.get('bio', None)
        self.invite_link: Optional[ChatInviteLink] = kwargs.get(
            'invite_link', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatJoinRequest object @{hex(id(self))} date={self.date}>"


class ChatPermissions:
    '''
    Describes actions that a non-administrator user is allowed to take in a chat.
    '''

    def __init__(
        self,
        **kwargs
    ):

        self.can_send_messages: Optional[bool] = kwargs.get(
            'can_send_messages', None)
        self.can_send_media_messages: Optional[bool] = kwargs.get(
            'can_send_media_messages', None)
        self.can_send_polls: Optional[bool] = kwargs.get(
            'can_send_polls', None)
        self.can_send_other_messages: Optional[bool] = kwargs.get(
            'can_send_other_messages', None)
        self.can_add_web_page_previews: Optional[bool] = kwargs.get(
            'can_add_web_page_previews', None)
        self.can_change_info: Optional[bool] = kwargs.get(
            'can_change_info', None)
        self.can_invite_users: Optional[bool] = kwargs.get(
            'can_invite_users', None)
        self.can_pin_messages: Optional[bool] = kwargs.get(
            'can_pin_messages', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatPermissions object @{hex(id(self))} >"


class ChatLocation:
    '''
    Represents a location to which a chat is connected.
    '''

    def __init__(
        self,
        *,
        location: Location,
        address: str,
        **kwargs
    ):
        self.location: Location = location
        self.address: str = address

    def __repr__(self):
        return f"<Telpy.extension.Objects.ChatLocation object @{hex(id(self))} address={self.address}>"
