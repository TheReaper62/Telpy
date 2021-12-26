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
    'VoiceChatScheduled',
    'VoiceChatStarted',
    'VoiceChatEnded',
    'VoiceChatParticipantsInvited',
)

class VoiceChatScheduled:
    '''
    This object represents a service message about a voice chat scheduled in the chat.
    '''

    def __init__(
        self,
        *,
        start_date: int,
        **kwargs
    ):
        self.start_date: int = start_date

    def __repr__(self):
        return f"<Telpy.extension.Objects.VoiceChatScheduled object @{hex(id(self))} start_date={self.start_date}>"


class VoiceChatStarted:
    '''
    This object represents a service message about a voice chat started in the chat. Currently holds no information.
    '''

    def __init__(
        self
    ):
        pass


class VoiceChatEnded:
    '''
    This object represents a service message about a voice chat ended in the chat.
    '''

    def __init__(
        self,
        *,
        duration: int,
        **kwargs
    ):
        self.duration: int = duration

    def __repr__(self):
        return f"<Telpy.extension.Objects.VoiceChatEnded object @{hex(id(self))} duration={self.duration}>"


class VoiceChatParticipantsInvited:
    '''
    This object represents a service message about new members invited to a voice chat.
    '''

    def __init__(
        self,
        **kwargs
    ):

        self.users: Optional[list[User]] = kwargs.get('users', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.VoiceChatParticipantsInvited object @{hex(id(self))} >"
