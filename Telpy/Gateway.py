import time
from .Functionals import *
from .Objects import *

def GatewayStart(client,request_interval):
    available_events = ['on_message', 'on_edited_message', 'on_channel_post', 'on_edited_channel_post', 'on_inline_query', 'on_chosen_inline_result', 'on_callback_query', 'on_shipping_query', 'on_pre_checkout_query', 'on_poll', 'on_poll_answer', 'on_my_chat_member', 'on_chat_member', 'on_chat_join_request']
    events = {i:vars(client)[i] for i in vars(client) if i in available_events}

    while True:
        client.get_updates(debug=False)
        if client.new_updates != []:
            for i in client.new_updates:
                print(">>>",i)
        else:
            print("No updates")

        print(f"Client Information: {vars(client)}")
        for this_update in client.new_updates:
            if hasattr(client,'on_message') and hasattr(this_update,'message'):
                client.on_message(this_update.message)
            elif hasattr(client,'on_edited_message') and hasattr(this_update,'edited_message'):
                client.on_edited_message(this_update.edited_message)
            elif hasattr(client,'on_channel_post') and hasattr(this_update,'channel_post'):
                client.on_channel_post(this_update.channel_post)
            elif hasattr(client,'on_edited_channel_post') and hasattr(this_update,'edited_channel_post'):
                client.on_edited_channel_post(this_update.edited_channel_post)
            elif hasattr(client,'on_inline_query') and hasattr(this_update,'inline_query'):
                client.on_inline_query(this_update.inline_query)
            elif hasattr(client,'on_chosen_inline_result') and hasattr(this_update,'chosen_inline_result'):
                client.on_chosen_inline_result(this_update.chosen_inline_result)
            elif hasattr(client,'on_callback_query') and hasattr(this_update,'callback_query'):
                client.on_callback_query(this_update.callback_query)
            elif hasattr(client,'on_shipping_query') and hasattr(this_update,'shipping_query'):
                client.on_shipping_query(this_update.shipping_query)
            elif hasattr(client,'on_pre_checkout_query') and hasattr(this_update,'pre_checkout_query'):
                client.on_pre_checkout_query(this_update.pre_checkout_query)
            elif hasattr(client,'on_poll') and hasattr(this_update,'poll'):
                client.on_poll(this_update.poll)
            elif hasattr(client,'on_poll_answer') and hasattr(this_update,'poll_answer'):
                client.on_poll_answer(this_update.poll_answer)
            elif hasattr(client,'on_my_chat_member') and hasattr(this_update,'my_chat_member'):
                client.on_my_chat_member(this_update.my_chat_member)
            elif hasattr(client,'on_chat_member') and hasattr(this_update,'chat_member'):
                client.on_chat_member(this_update.chat_member)
            elif hasattr(client,'on_chat_join_request') and hasattr(this_update,'chat_join_request'):
                client.on_chat_join_request(this_update.chat_join_request)

        time.sleep(request_interval)
