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
    'PassportData',
    'PassportFile',
    'EncryptedPassportElement',
    'EncryptedCredentials',
    'PassportElementErrorDataField',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
)

class PassportData:
    '''
    Contains information about Telegram Passport data shared with the bot by the user.
    '''
    def __init__(
        self,
        *,
        data: list[EncryptedPassportElement],
        credentials: EncryptedCredentials,
        **kwargs
    ):
        self.data: list[EncryptedPassportElement] = data
        self.credentials: EncryptedCredentials = credentials


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportData object @{hex(id(self))} >"

class PassportFile:
    '''
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
    '''
    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        file_size: int,
        file_date: int,
        **kwargs
    ):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.file_size: int = file_size
        self.file_date: int = file_date


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportFile object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} file_size={self.file_size} file_date={self.file_date}>"

class EncryptedPassportElement:
    '''
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.
    '''
    def __init__(
        self,
        *,
        type: str,
        hash: str,
        **kwargs
    ):
        self.type: str = type
        self.hash: str = hash

        self.data: Optional[str] = kwargs.get('data',None)
        self.phone_number: Optional[str] = kwargs.get('phone_number',None)
        self.email: Optional[str] = kwargs.get('email',None)
        self.files: Optional[list[PassportFile]] = kwargs.get('files',None)
        self.front_side: Optional[PassportFile] = kwargs.get('front_side',None)
        self.reverse_side: Optional[PassportFile] = kwargs.get('reverse_side',None)
        self.selfie: Optional[PassportFile] = kwargs.get('selfie',None)
        self.translation: Optional[list[PassportFile]] = kwargs.get('translation',None)

    def __repr__(self):
        return f"<Telpy.extension.Objects.EncryptedPassportElement object @{hex(id(self))} type={self.type} hash={self.hash}>"

class EncryptedCredentials:
    '''
    Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
    '''
    def __init__(
        self,
        *,
        data: str,
        hash: str,
        secret: str,
        **kwargs
    ):
        self.data: str = data
        self.hash: str = hash
        self.secret: str = secret


    def __repr__(self):
        return f"<Telpy.extension.Objects.EncryptedCredentials object @{hex(id(self))} data={self.data} hash={self.hash} secret={self.secret}>"

class PassportElementErrorDataField:
    '''
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        field_name: str,
        data_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.field_name: str = field_name
        self.data_hash: str = data_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorDataField object @{hex(id(self))} source={self.source} type={self.type} field_name={self.field_name} data_hash={self.data_hash} message={self.message}>"

class PassportElementErrorFrontSide:
    '''
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorFrontSide object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorReverseSide:
    '''
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorReverseSide object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorSelfie:
    '''
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorSelfie object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorFile:
    '''
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorFile object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorFiles:
    '''
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hashes: list[str],
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hashes: list[str] = file_hashes
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorFiles object @{hex(id(self))} source={self.source} type={self.type} message={self.message}>"

class PassportElementErrorTranslationFile:
    '''
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorTranslationFile object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorTranslationFiles:
    '''
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hashes: list[str],
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.file_hashes: list[str] = file_hashes
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorTranslationFiles object @{hex(id(self))} source={self.source} type={self.type} message={self.message}>"

class PassportElementErrorUnspecified:
    '''
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    '''
    def __init__(
        self,
        *,
        source: str,
        type: str,
        element_hash: str,
        message: str,
        **kwargs
    ):
        self.source: str = source
        self.type: str = type
        self.element_hash: str = element_hash
        self.message: str = message


    def __repr__(self):
        return f"<Telpy.extension.Objects.PassportElementErrorUnspecified object @{hex(id(self))} source={self.source} type={self.type} element_hash={self.element_hash} message={self.message}>"
