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
    'User',
    'Contact',
    'UserProfilePhotos',
)

class User:
    '''
    This object represents a Telegram user or bot.
    '''

    def __init__(
        self,
        *,
        id: int,
        is_bot: bool,
        first_name: str,
        **kwargs
    ):
        self.id: int = id
        self.is_bot: bool = is_bot
        self.first_name: str = first_name

        self.last_name: Optional[str] = kwargs.get('last_name', None)
        self.username: Optional[str] = kwargs.get('username', None)
        self.language_code: Optional[str] = kwargs.get('language_code', None)
        self.can_join_groups: Optional[bool] = kwargs.get(
            'can_join_groups', None)
        self.can_read_all_group_messages: Optional[bool] = kwargs.get(
            'can_read_all_group_messages', None)
        self.supports_inline_queries: Optional[bool] = kwargs.get(
            'supports_inline_queries', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.User object @{hex(id(self))} id={self.id} is_bot={self.is_bot} first_name={self.first_name}>"


class Contact:
    '''
    This object represents a phone contact.
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

        self.last_name: Optional[str] = kwargs.get('last_name', None)
        self.user_id: Optional[int] = kwargs.get('user_id', None)
        self.vcard: Optional[str] = kwargs.get('vcard', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Contact object @{hex(id(self))} phone_number={self.phone_number} first_name={self.first_name}>"


class UserProfilePhotos:
    '''
    This object represent a user's profile pictures.
    '''

    def __init__(
        self,
        *,
        total_count: int,
        photos: list[list[PhotoSize]],
        **kwargs
    ):
        self.total_count: int = total_count
        self.photos: list[list[PhotoSize]] = photos

    def __repr__(self):
        return f"<Telpy.extension.Objects.UserProfilePhotos object @{hex(id(self))} total_count={self.total_count}>"
