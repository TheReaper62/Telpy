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
    'BotCommand',
    'BotCommandScopeDefault',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
)

class BotCommand:
    '''
    This object represents a bot command.
    '''
    
    def __init__(
        self,
        *,
        command: str,
        description: str,
        **kwargs
    ):
        self.command: str = command
        self.description: str = description

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommand object @{hex(id(self))} command={self.command} description={self.description}>"


class BotCommandScopeDefault:
    '''
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
    '''

    def __init__(
        self,
        *,
        type: str,
        **kwargs
    ):
        self.type: str = type

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeDefault object @{hex(id(self))} type={self.type}>"


class BotCommandScopeAllPrivateChats:
    '''
    Represents the scope of bot commands, covering all private chats.
    '''

    def __init__(
        self,
        *,
        type: str,
        **kwargs
    ):
        self.type: str = type

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeAllPrivateChats object @{hex(id(self))} type={self.type}>"


class BotCommandScopeAllGroupChats:
    '''
    Represents the scope of bot commands, covering all group and supergroup chats.
    '''

    def __init__(
        self,
        *,
        type: str,
        **kwargs
    ):
        self.type: str = type

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeAllGroupChats object @{hex(id(self))} type={self.type}>"


class BotCommandScopeAllChatAdministrators:
    '''
    Represents the scope of bot commands, covering all group and supergroup chat administrators.
    '''

    def __init__(
        self,
        *,
        type: str,
        **kwargs
    ):
        self.type: str = type

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeAllChatAdministrators object @{hex(id(self))} type={self.type}>"


class BotCommandScopeChat:
    '''
    Represents the scope of bot commands, covering a specific chat.
    '''

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        **kwargs
    ):
        self.type: str = type
        self.chat_id: Union[int, str] = chat_id

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeChat object @{hex(id(self))} type={self.type}>"


class BotCommandScopeChatAdministrators:
    '''
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    '''

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        **kwargs
    ):
        self.type: str = type
        self.chat_id: Union[int, str] = chat_id

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeChatAdministrators object @{hex(id(self))} type={self.type}>"


class BotCommandScopeChatMember:
    '''
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    '''

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        user_id: int,
        **kwargs
    ):
        self.type: str = type
        self.chat_id: Union[int, str] = chat_id
        self.user_id: int = user_id

    def __repr__(self):
        return f"<Telpy.extension.Objects.BotCommandScopeChatMember object @{hex(id(self))} type={self.type} user_id={self.user_id}>"
