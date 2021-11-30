import requests
from typing import List, Union

from .Functionals import *
from .Objects import *
from .Gateway import GatewayStart as GStart

import re

class Client:
    def __init__(self, token):
        self.token = token
        self.BASE = f"https://api.telegram.org/bot{token}"
        self.updates = []
        self.new_updates = []
        self.last_update = None

    def get_updates(
            self,
            offset:int = None,
            limit:int = 100,
            timeout:int = None,
            allowed_updates:list = None,
            debug : bool = False
        ) -> List[Update]:
        '''
        Use this method to receive incoming updates using long polling. An Array of Update objects is returned.
        '''
        self.updates += self.new_updates
        self.new_updates = []
        params = dict()

        params["limit"] = limit

        if type(timeout) == int:    params["timeout"] = timeout
        if type(allowed_updates) == int:    params["allowed_updates"] = timeout

        # Handle offset
        if offset == None:
            if self.last_update != None:
                params["offset"] = self.last_update + 1
        else:
            params["offset"] = offset

        r = requests.get(self.BASE+"/getUpdates",params=params)
        if debug:
            print("DEBUG:\nURL -",r.url,"\nResponse:",r.text)
        if r.ok and r.json()["ok"]:
            self.new_updates += [Update(**data) for data in r.json()["result"]]
            if self.new_updates == []:
                return
            self.last_update = max([update_obj.update_id for update_obj in self.new_updates])
        else:
            raise InvalidArgument(f"An Error Occured\nReason:\tHTTP Error Message:\n{r.reason}\n\nTelegram API Error Message:\n{r.json()['result']}")

    def set_webhook(
            self,
            url:str,
            certificate:InputFile = None,
            ip_address:str = None,
            max_connections:int = 40,
            allowed_updates:list = None,
            drop_pending_updates:bool = None
        ) -> bool:
        '''
        Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
        If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. https://www.example.com/<token>. Since nobody else knows your bot's token, you can be pretty sure it's us.
        '''

        params = dict()

        params["max_connections"] = max_connections
        params["url"] = url

        if type(certificate) == int:    params["certificate"] = certificate
        if type(ip_address) == int:    params["ip_address"] = ip_address
        if type(allowed_updates) == int:    params["allowed_updates"] = allowed_updates
        if type(drop_pending_updates) == int:    params["drop_pending_updates"] = drop_pending_updates

        return SimpleRequestHandler(self.BASE,"get","/setWebhook",bool,params=params)

    def delete_webhook(
            self,
            drop_pending_updates:bool = None
        ) -> bool:
        '''
        Use this method to remove webhook integration if you decide to switch back to get_updates. Returns True on success.
        '''
        params = dict()

        if type(drop_pending_updates) == int:    params["drop_pending_updates"] = drop_pending_updates

        return SimpleRequestHandler(self.BASE,"get","/deleteWebhook",bool,params=params)

    def get_webhook_info(
            self
        ) -> WebhookInfo:
        '''
        Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.
        '''
        return SimpleRequestHandler(self.BASE,"get","/getWebhookInfo",WebhookInfo)

    def get_me(
            self
        ) -> User:
        '''
        A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.
        '''
        return SimpleRequestHandler(self.BASE,"get","/getMe",User)

    def log_out(
            self
        ) -> bool:
        '''
        Use this method to log out from the cloud Bot API server before launching the bot locally.
        '''
        return SimpleRequestHandler(self.BASE,"get", "/logOut", bool)

    def close(
        self
        ) -> bool:
        '''
        Use this method to close the bot instance before moving it from one local server to another.
        '''
        return SimpleRequestHandler(self.BASE,'get', "/close", bool)

    def send_message(
            self,
            chat_id : Union[int,str],
            text : str,
            parse_mode : str = None,
            entities : List[MessageEntity] = None,
            disable_web_page_preview : bool = None,
            disable_notification : bool = None,
            reply_to_message_id : int = None,
            allow_sending_without_reply : bool = None,
            reply_markup : Union[InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove,ForceReply] = None
        ) -> Message:
        '''
        Use this method to send text messages. On success, the sent Message is returned.
        '''
        return SimpleRequestHandler(self.BASE,'get', "/sendMessage", Message, params=CleanObject(dict(locals())))

    # Additional Functions
    def render_response_template(self,message,response_template):
        for case in response_template:
            regex_pattern = case.get("regex",None)
            starts = case.get("starts",None)
            response_text = case.get("response",None)
            chat_id = case.get("chat_id",message.chat.id)
            if regex_pattern == None and starts == None:
                print(f"\n\nResponse Case Invalid identifier:\n{case}\nThis case has been ignored and the bot is still running\n\n")
                continue
            if response_text in [None,""]:
                print(f"\n\nResponse Case Invalid Response:\n{case}\nThis case has been ignored and the bot is still running\n\n")
                continue
            if regex_pattern != None:
                if re.search(regex_pattern,message.text):
                    self.send_message(chat_id,response_text)
                else:
                    continue
            elif starts != None:
                if message.text.startswith(starts):
                    self.send_message(chat_id,response_text)
                else:
                    continue

    # Decorator

    def event(self, function):
        events = ['on_message', 'on_edited_message', 'on_channel_post', 'on_edited_channel_post', 'on_inline_query', 'on_chosen_inline_result', 'on_callback_query', 'on_shipping_query', 'on_pre_checkout_query', 'on_poll', 'on_poll_answer', 'on_my_chat_member', 'on_chat_member', 'on_chat_join_request']
        assert(function.__name__ in events), "@client.event decorating Invalid Event Listener"
        setattr(self, function.__name__, function)
        return function

    def run(self,request_interval=2):
        GStart(self,request_interval)
