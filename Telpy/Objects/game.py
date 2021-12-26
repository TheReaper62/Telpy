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
    'Game',
    'GameHighScore',
)

class Game:
    '''
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    '''

    def __init__(
        self,
        *,
        title: str,
        description: str,
        photo: list[PhotoSize],
        **kwargs
    ):
        self.title: str = title
        self.description: str = description
        self.photo: list[PhotoSize] = photo

        self.text: Optional[str] = kwargs.get('text', None)
        self.text_entities: Optional[list[MessageEntity]] = kwargs.get(
            'text_entities', None)
        self.animation: Optional[Animation] = kwargs.get('animation', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Game object @{hex(id(self))} title={self.title} description={self.description}>"


class GameHighScore:
    '''
    This object represents one row of the high scores table for a game.
    '''

    def __init__(
        self,
        *,
        position: int,
        user: User,
        score: int,
        **kwargs
    ):
        self.position: int = position
        self.user: User = user
        self.score: int = score

    def __repr__(self):
        return f"<Telpy.extension.Objects.GameHighScore object @{hex(id(self))} position={self.position} score={self.score}>"
