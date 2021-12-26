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
    'LabeledPrice',
    'Invoice',
    'ShippingAddress',
    'OrderInfo',
    'ShippingOption',
    'SuccessfulPayment',
    'ShippingQuery',
    'PreCheckoutQuery',
)

class LabeledPrice:
    '''
    This object represents a portion of the price for goods or services.
    '''

    def __init__(
        self,
        *,
        label: str,
        amount: int,
        **kwargs
    ):
        self.label: str = label
        self.amount: int = amount

    def __repr__(self):
        return f"<Telpy.extension.Objects.LabeledPrice object @{hex(id(self))} label={self.label} amount={self.amount}>"


class Invoice:
    '''
    This object contains basic information about an invoice.
    '''

    def __init__(
        self,
        *,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int,
        **kwargs
    ):
        self.title: str = title
        self.description: str = description
        self.start_parameter: str = start_parameter
        self.currency: str = currency
        self.total_amount: int = total_amount

    def __repr__(self):
        return f"<Telpy.extension.Objects.Invoice object @{hex(id(self))} title={self.title} description={self.description} start_parameter={self.start_parameter} currency={self.currency} total_amount={self.total_amount}>"


class ShippingAddress:
    '''
    This object represents a shipping address.
    '''

    def __init__(
        self,
        *,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str,
        **kwargs
    ):
        self.country_code: str = country_code
        self.state: str = state
        self.city: str = city
        self.street_line1: str = street_line1
        self.street_line2: str = street_line2
        self.post_code: str = post_code

    def __repr__(self):
        return f"<Telpy.extension.Objects.ShippingAddress object @{hex(id(self))} country_code={self.country_code} state={self.state} city={self.city} street_line1={self.street_line1} street_line2={self.street_line2} post_code={self.post_code}>"


class OrderInfo:
    '''
    This object represents information about an order.
    '''

    def __init__(
        self,
        **kwargs
    ):

        self.name: Optional[str] = kwargs.get('name', None)
        self.phone_number: Optional[str] = kwargs.get('phone_number', None)
        self.email: Optional[str] = kwargs.get('email', None)
        self.shipping_address: Optional[ShippingAddress] = kwargs.get(
            'shipping_address', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.OrderInfo object @{hex(id(self))} >"


class ShippingOption:
    '''
    This object represents one shipping option.
    '''

    def __init__(
        self,
        *,
        id: str,
        title: str,
        prices: list[LabeledPrice],
        **kwargs
    ):
        self.id: str = id
        self.title: str = title
        self.prices: list[LabeledPrice] = prices

    def __repr__(self):
        return f"<Telpy.extension.Objects.ShippingOption object @{hex(id(self))} id={self.id} title={self.title}>"


class SuccessfulPayment:
    '''
    This object contains basic information about a successful payment.
    '''

    def __init__(
        self,
        *,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str,
        **kwargs
    ):
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.telegram_payment_charge_id: str = telegram_payment_charge_id
        self.provider_payment_charge_id: str = provider_payment_charge_id

        self.shipping_option_id: Optional[str] = kwargs.get(
            'shipping_option_id', None)
        self.order_info: Optional[OrderInfo] = kwargs.get('order_info', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.SuccessfulPayment object @{hex(id(self))} currency={self.currency} total_amount={self.total_amount} invoice_payload={self.invoice_payload} telegram_payment_charge_id={self.telegram_payment_charge_id} provider_payment_charge_id={self.provider_payment_charge_id}>"


class ShippingQuery:
    '''
    This object contains information about an incoming shipping query.
    '''

    def __init__(
        self,
        *,
        id: str,
        From: User,
        invoice_payload: str,
        shipping_address: ShippingAddress,
        **kwargs
    ):
        self.id: str = id
        self.From: User = From
        self.invoice_payload: str = invoice_payload
        self.shipping_address: ShippingAddress = shipping_address

    def __repr__(self):
        return f"<Telpy.extension.Objects.ShippingQuery object @{hex(id(self))} id={self.id} invoice_payload={self.invoice_payload}>"


class PreCheckoutQuery:
    '''
    This object contains information about an incoming pre-checkout query.
    '''

    def __init__(
        self,
        *,
        id: str,
        From: User,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        **kwargs
    ):
        self.id: str = id
        self.From: User = From
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload

        self.shipping_option_id: Optional[str] = kwargs.get(
            'shipping_option_id', None)
        self.order_info: Optional[OrderInfo] = kwargs.get('order_info', None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.PreCheckoutQuery object @{hex(id(self))} id={self.id} currency={self.currency} total_amount={self.total_amount} invoice_payload={self.invoice_payload}>"
