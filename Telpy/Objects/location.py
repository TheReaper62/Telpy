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
    'Location',
    'Venue',
    'ProximityAlertTriggered',
)

class Location:
    '''
    This object represents a point on the map.
    '''

    def __init__(
        self,
        *,
        longitude: float,
        latitude: float,
        **kwargs
    ):
        self.longitude: float = longitude
        self.latitude: float = latitude

        self.horizontal_accuracy: Optional[float] = kwargs.get(
            'horizontal_accuracy', None)
        self.live_period: Optional[int] = kwargs.get('live_period', None)
        self.heading: Optional[int] = kwargs.get('heading', None)
        self.proximity_alert_radius: Optional[int] = kwargs.get(
            'proximity_alert_radius', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Location object @{hex(id(self))} longitude={self.longitude} latitude={self.latitude}>"


class Venue:
    '''
    This object represents a venue.
    '''

    def __init__(
        self,
        *,
        location: Location,
        title: str,
        address: str,
        **kwargs
    ):
        self.location: Location = location
        self.title: str = title
        self.address: str = address

        self.foursquare_id: Optional[str] = kwargs.get('foursquare_id', None)
        self.foursquare_type: Optional[str] = kwargs.get(
            'foursquare_type', None)
        self.google_place_id: Optional[str] = kwargs.get(
            'google_place_id', None)
        self.google_place_type: Optional[str] = kwargs.get(
            'google_place_type', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.Venue object @{hex(id(self))} title={self.title} address={self.address}>"


class ProximityAlertTriggered:
    '''
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
    '''

    def __init__(
        self,
        *,
        traveler: User,
        watcher: User,
        distance: int,
        **kwargs
    ):
        self.traveler: User = traveler
        self.watcher: User = watcher
        self.distance: int = distance

    def __repr__(self):
        return f"<Telpy.extension.Objects.ProximityAlertTriggered object @{hex(id(self))} distance={self.distance}>"
