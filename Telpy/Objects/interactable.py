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
    'Dice',
    'PollOption',
    'PollAnswer',
    'Poll',
    'KeyboardButton',
    'ReplyKeyboardMarkup',
    'KeyboardButtonPollType',
    'ReplyKeyboardRemove',
)

class Dice:
    '''
    This object represents an animated emoji that displays a random value.
    '''

    def __init__(
        self,
        *,
        emoji: str,
        value: int,
        **kwargs
    ):
        self.emoji: str = emoji
        self.value: int = value

    def __repr__(self):
        return f"<Telpy.extension.Objects.Dice object @{hex(id(self))} emoji={self.emoji} value={self.value}>"


class PollOption:
    '''
    This object contains information about one answer option in a poll.
    '''

    def __init__(
        self,
        *,
        text: str,
        voter_count: int,
        **kwargs
    ):
        self.text: str = text
        self.voter_count: int = voter_count

    def __repr__(self):
        return f"<Telpy.extension.Objects.PollOption object @{hex(id(self))} text={self.text} voter_count={self.voter_count}>"


class PollAnswer:
    '''
    This object represents an answer of a user in a non-anonymous poll.
    '''

    def __init__(
        self,
        *,
        poll_id: str,
        user: User,
        option_ids: list[int],
        **kwargs
    ):
        self.poll_id: str = poll_id
        self.user: User = user
        self.option_ids: list[int] = option_ids

    def __repr__(self):
        return f"<Telpy.extension.Objects.PollAnswer object @{hex(id(self))} poll_id={self.poll_id}>"


class Poll:
    '''
    This object contains information about a poll.
    '''

    def __init__(
        self,
        *,
        id: str,
        question: str,
        options: list[PollOption],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        **kwargs
    ):
        self.id: str = id
        self.question: str = question
        self.options: list[PollOption] = options
        self.total_voter_count: int = total_voter_count
        self.is_closed: bool = is_closed
        self.is_anonymous: bool = is_anonymous
        self.type: str = type
        self.allows_multiple_answers: bool = allows_multiple_answers

        self.correct_option_id: Optional[int] = kwargs.get(
            'correct_option_id', None)
        self.explanation: Optional[str] = kwargs.get('explanation', None)
        self.explanation_entities: Optional[list[MessageEntity]] = kwargs.get(
            'explanation_entities', None)
        self.open_period: Optional[int] = kwargs.get('open_period', None)
        self.close_date: Optional[int] = kwargs.get('close_date', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Poll object @{hex(id(self))} id={self.id} question={self.question} total_voter_count={self.total_voter_count} is_closed={self.is_closed} is_anonymous={self.is_anonymous} type={self.type} allows_multiple_answers={self.allows_multiple_answers}>"


class KeyboardButton:
    '''
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.
    '''

    def __init__(
        self,
        *,
        text: str,
        **kwargs
    ):
        self.text: str = text

        self.request_contact: Optional[bool] = kwargs.get(
            'request_contact', None)
        self.request_location: Optional[bool] = kwargs.get(
            'request_location', None)
        self.request_poll: Optional[KeyboardButtonPollType] = kwargs.get(
            'request_poll', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.KeyboardButton object @{hex(id(self))} text={self.text}>"


class ReplyKeyboardMarkup:
    '''
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
    '''

    def __init__(
        self,
        *,
        keyboard: list[list[KeyboardButton]],
        **kwargs
    ):
        self.keyboard: list[list[KeyboardButton]] = keyboard

        self.resize_keyboard: Optional[bool] = kwargs.get(
            'resize_keyboard', None)
        self.one_time_keyboard: Optional[bool] = kwargs.get(
            'one_time_keyboard', None)
        self.input_field_placeholder: Optional[str] = kwargs.get(
            'input_field_placeholder', None)
        self.selective: Optional[bool] = kwargs.get('selective', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ReplyKeyboardMarkup object @{hex(id(self))} >"


class KeyboardButtonPollType:
    '''
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
    '''

    def __init__(
        self,
        **kwargs
    ):

        self.type: Optional[str] = kwargs.get('type', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.KeyboardButtonPollType object @{hex(id(self))} >"


class ReplyKeyboardRemove:
    '''
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
    '''

    def __init__(
        self,
        *,
        remove_keyboard: bool,
        **kwargs
    ):
        self.remove_keyboard: bool = remove_keyboard

        self.selective: Optional[bool] = kwargs.get('selective', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.ReplyKeyboardRemove object @{hex(id(self))} remove_keyboard={self.remove_keyboard}>"
