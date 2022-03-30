from .Functionals import *

class Update:
    '''
    This object represents an incoming update.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.update_id : int = kwargs["update_id"]

        
        self.message : Message = Message(**(kwargs.get("message",None)))
        self.edited_message : Message = Message(**(kwargs.get("edited_message",None)))
        self.channel_post : Message = Message(**(kwargs.get("channel_post",None)))
        self.edited_channel_post : Message = Message(**(kwargs.get("edited_channel_post",None)))
        self.inline_query : InlineQuery = InlineQuery(**(kwargs.get("inline_query",None)))
        self.chosen_inline_result : ChosenInlineResult = ChosenInlineResult(**(kwargs.get("chosen_inline_result",None)))
        self.callback_query : CallbackQuery = CallbackQuery(**(kwargs.get("callback_query",None)))
        self.shipping_query : ShippingQuery = ShippingQuery(**(kwargs.get("shipping_query",None)))
        self.pre_checkout_query : PreCheckoutQuery = PreCheckoutQuery(**(kwargs.get("pre_checkout_query",None)))
        self.poll : Poll = Poll(**(kwargs.get("poll",None)))
        self.poll_answer : PollAnswer = PollAnswer(**(kwargs.get("poll_answer",None)))
        self.my_chat_member : ChatMemberUpdated = ChatMemberUpdated(**(kwargs.get("my_chat_member",None)))
        self.chat_member : ChatMemberUpdated = ChatMemberUpdated(**(kwargs.get("chat_member",None)))

    def __repr__(self):
        return f"<Telpy.Update object @{hex(id(self))} update_id={self.update_id}>"

class WebhookInfo:
    '''
    Contains information about the current status of a webhook.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.url : str = kwargs["url"]
        self.has_custom_certificate : bool = kwargs["has_custom_certificate"]
        self.pending_update_count : int = kwargs["pending_update_count"]

        
        self.ip_address : str = kwargs.get("ip_address",None)
        self.last_error_date : int = kwargs.get("last_error_date",None)
        self.last_error_message : str = kwargs.get("last_error_message",None)
        self.max_connections : int = kwargs.get("max_connections",None)
        self.allowed_updates : List[str] = kwargs.get("allowed_updates",None)

    def __repr__(self):
        return f"<Telpy.WebhookInfo object @{hex(id(self))} url={self.url}>"

class User:
    '''
    This object represents a Telegram user or bot.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : int = kwargs["id"]
        self.is_bot : bool = kwargs["is_bot"]
        self.first_name : str = kwargs["first_name"]

        
        self.last_name : str = kwargs.get("last_name",None)
        self.username : str = kwargs.get("username",None)
        self.language_code : str = kwargs.get("language_code",None)
        self.can_join_groups : bool = kwargs.get("can_join_groups",None)
        self.can_read_all_group_messages : bool = kwargs.get("can_read_all_group_messages",None)
        self.supports_inline_queries : bool = kwargs.get("supports_inline_queries",None)

    def __repr__(self):
        return f"<Telpy.User object @{hex(id(self))} id={self.id} first_name={self.first_name}>"

class Chat:
    '''
    This object represents a chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : int = kwargs["id"]
        self.type : str = kwargs["type"]

        
        self.title : str = kwargs.get("title",None)
        self.username : str = kwargs.get("username",None)
        self.first_name : str = kwargs.get("first_name",None)
        self.last_name : str = kwargs.get("last_name",None)
        self.photo : ChatPhoto = ChatPhoto(**(kwargs.get("photo",None)))
        self.bio : str = kwargs.get("bio",None)
        self.description : str = kwargs.get("description",None)
        self.invite_link : str = kwargs.get("invite_link",None)
        self.pinned_message : ChatPermissions = ChatPermissions(**(kwargs.get("pinned_message",None)))
        self.permissions : int = kwargs.get("permissions",None)
        self.slow_mode_delay : int = kwargs.get("slow_mode_delay",None)
        self.message_auto_delete_time : int = kwargs.get("message_auto_delete_time",None)
        self.sticker_set_name : str = kwargs.get("sticker_set_name",None)
        self.can_set_sticker_set : bool = kwargs.get("can_set_sticker_set",None)
        self.linked_chat_id : int = kwargs.get("linked_chat_id",None)
        self.location : ChatLocation = ChatLocation(**(kwargs.get("location",None)))

    def __repr__(self):
        return f"<Telpy.Chat object @{hex(id(self))} id={self.id} type={self.type}>"

class Message:
    '''
    This object represents a message.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        self.message_id : int = kwargs["message_id"]
        self.date : int = kwargs["date"]

        
        self.From : User = User(**(kwargs.get("from",None)))
        self.sender_chat : Chat = Chat(**(kwargs.get("sender_chat",None)))
        self.chat : Chat = Chat(**(kwargs.get("chat",None)))
        self.forward_from : User = User(**(kwargs.get("forward_from",None)))
        self.forward_from_chat : Chat = Chat(**(kwargs.get("forward_from_chat",None)))
        self.forward_from_message_id : int = kwargs.get("forward_from_message_id",None)
        self.forward_signature : str = kwargs.get("forward_signature",None)
        self.forward_sender_name : str = kwargs.get("forward_sender_name",None)
        self.forward_date : int = kwargs.get("forward_date",None)
        self.reply_to_message : Message = Message(**(kwargs.get("reply_to_message",None)))
        self.via_bot : User = User(**(kwargs.get("via_bot",None)))
        self.edit_date : int = kwargs.get("edit_date",None)
        self.media_group_id : str = kwargs.get("media_group_id",None)
        self.author_signature : str = kwargs.get("author_signature",None)
        self.text : str = kwargs.get("text",None)
        self.entities : MessageEntity = [MessageEntity(**entity) for entity in (kwargs.get("entities",None))]
        self.animation : Animation = Animation(**(kwargs.get("animation",None)))
        self.audio : Audio = Audio(**(kwargs.get("audio",None)))
        self.document : Document = Document(**(kwargs.get("document",None)))
        self.photo : PhotoSize = [PhotoSize(**photo) for photo in (kwargs.get("photo",None))]
        self.sticker : Sticker = Sticker(**(kwargs.get("sticker",None)))
        self.video : Video = Video(**(kwargs.get("video",None)))
        self.video_note : VideoNote = VideoNote(**(kwargs.get("video_note",None)))
        self.voice : Voice = Voice(**(kwargs.get("voice",None)))
        self.caption : str = kwargs.get("caption",None)
        self.caption_entities: MessageEntity = [MessageEntity(**entity) for entity in (kwargs.get("caption_entities",None))]
        self.contact : Contact = Contact(**(kwargs.get("contact",None)))
        self.dice : Dice = Dice(**(kwargs.get("dice",None)))
        self.game : Game = Game(**(kwargs.get("game",None)))
        self.poll : Poll = Poll(**(kwargs.get("poll",None)))
        self.venue : Venue = Venue(**(kwargs.get("venue",None)))
        self.location : Location = Location(**(kwargs.get("location",None)))
        self.new_chat_members : User = [User(**user) for user in (kwargs.get("new_chat_members",None))]
        self.left_chat_member : User = User(**(kwargs.get("left_chat_member",None)))
        self.new_chat_title : str = kwargs.get("new_chat_title",None)
        self.new_chat_photo : PhotoSize = [PhotoSize(**photo) for photo in (kwargs.get("new_chat_photo",None))]
        self.delete_chat_photo : bool = kwargs.get("delete_chat_photo",None)
        self.group_chat_created : bool = kwargs.get("group_chat_created",None)
        self.supergroup_chat_created : bool = kwargs.get("supergroup_chat_created",None)
        self.channel_chat_created : bool = kwargs.get("channel_chat_created",None)
        self.message_auto_delete_timer_changed : MessageAutoDeleteTimerChanged = MessageAutoDeleteTimerChanged(**(kwargs.get("message_auto_delete_timer_changed",None)))
        self.migrate_to_chat_id : int = kwargs.get("migrate_to_chat_id",None)
        self.migrate_from_chat_id : int = kwargs.get("migrate_from_chat_id",None)
        self.pinned_message : Message = Message(**(kwargs.get("pinned_message",None)))
        self.invoice : Invoice = kwargs.get("invoice",None)
        self.successful_payment : SuccessfulPayment = SuccessfulPayment(**(kwargs.get("successful_payment",None)))
        self.connected_website : str = kwargs.get("connected_website",None)
        self.passport_data : PassportData = PassportData(**(kwargs.get("passport_data",None)))
        self.proximity_alert_triggered : ProximityAlertTriggered = ProximityAlertTriggered(**(kwargs.get("proximity_alert_triggered",None)))
        self.voice_chat_scheduled : VoiceChatScheduled = VoiceChatScheduled(**(kwargs.get("voice_chat_scheduled",None)))
        self.voice_chat_started : VoiceChatStarted = VoiceChatStarted(**(kwargs.get("voice_chat_started",None)))
        self.voice_chat_ended : VoiceChatEnded = VoiceChatEnded(**(kwargs.get("voice_chat_ended",None)))
        self.voice_chat_participants_invited : VoiceChatParticipantsInvited = VoiceChatParticipantsInvited(**(kwargs.get("voice_chat_participants_invited",None)))
        self.reply_markup : 	InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))

    def __repr__(self):
        return f"<Telpy.Message object @{hex(id(self))} message_id={self.message_id} date={self.date}>"

class MessageId:
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.message_id : str = kwargs["message_id"]

    def __repr__(self):
        return f"<Telpy.MessageId object @{hex(id(self))} message_id={self.message_id}>"

class MessageEntity:
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.offset : int = kwargs["offset"]
        self.length : int = kwargs["length"]

        
        self.url : str = kwargs.get("url",None)
        self.user : User = User(**(kwargs.get("user",None)))
        self.language : str = kwargs.get("language",None)

    def __repr__(self):
        return f"<Telpy.MessageEntity object @{hex(id(self))} type={self.type} offset={self.offset} length={self.length}>"

class PhotoSize:
    '''
    This object represents one size of a photo or a file / sticker thumbnail.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.width : int = kwargs["width"]
        self.height : int = kwargs["height"]

        
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.MessageEntity object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height}>"

class Animation:
    '''
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.width : int = kwargs["width"]
        self.height : int = kwargs["height"]
        self.duration : int = kwargs["duration"]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))
        self.file_name : str = kwargs.get("file_name",None)
        self.mime_type : str = kwargs.get("mime_type",None)
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.Animation object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} duration={self.duration}>"

class Audio:
    '''
    This object represents an audio file to be treated as music by the Telegram clients.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.duration : int = kwargs["duration"]

        
        self.performer : str = kwargs.get("performer",None)
        self.title : str = kwargs.get("title",None)
        self.file_name : str = kwargs.get("file_name",None)
        self.mime_type : str = kwargs.get("mime_type",None)
        self.file_size : int = kwargs.get("file_size",None)
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))

    def __repr__(self):
        return f"<Telpy.Audio object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} duration={self.duration}>"

class Document:
    '''
    This object represents a general file (as opposed to photos, voice messages and audio files).
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))
        self.file_name : str = kwargs.get("file_name",None)
        self.mime_type : str = kwargs.get("mime_type",None)
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.Document object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id}>"

class Video:
    '''
    This object represents a video file.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.width : int = kwargs["width"]
        self.height : int = kwargs["height"]
        self.duration : int = kwargs["duration"]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))
        self.file_name : str = kwargs.get("file_name",None)
        self.mime_type : str = kwargs.get("mime_type",None)
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.Video object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} duration={self.duration}>"

class VideoNote:
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.length : int = kwargs["length"]
        self.duration : int = kwargs["duration"]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.VideoNote object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} length={self.length} duration={self.duration}>"

class Voice:
    '''
    This object represents a voice note.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.duration : int = kwargs["duration"]

        
        self.mime_type : str = kwargs.get("mime_type",None)
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.Voice object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} duration={self.duration}>"

class Contact:
    '''
    This object represents a phone contact.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.phone_number : str = kwargs["phone_number"]
        self.first_name : str = kwargs["first_name"]

        
        self.last_name : str = kwargs.get("last_name",None)
        self.user_id : int = kwargs.get("user_id",None)
        self.vcard : str = kwargs.get("vcard",None)

    def __repr__(self):
        return f"<Telpy.Contact object @{hex(id(self))} phone_number={self.phone_number} first_name={self.first_name}>"

class Dice:
    '''
    This object represents an animated emoji that displays a random value.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.emoji : str = kwargs["emoji"]
        self.value : int = kwargs["value"]

    def __repr__(self):
        return f"<Telpy.Dice object @{hex(id(self))} emoji={self.emoji} value={self.value}>"

class PollOption:
    '''
    This object contains information about one answer option in a poll.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.text : str = kwargs["text"]
        self.voter_count : int = kwargs["voter_count"]

    def __repr__(self):
        return f"<Telpy.PollOption object @{hex(id(self))} text={self.text} voter_count={self.voter_count}>"

class PollAnswer:
    '''
    This object represents an answer of a user in a non-anonymous poll.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.poll_id : str = kwargs["poll_id"]
        self.user : User = User(**(kwargs["user"]))
        self.option_ids : int = kwargs["option_ids"]

    def __repr__(self):
        return f"<Telpy.PollAnswer object @{hex(id(self))} poll_id={self.poll_id} user={self.user} option_ids={self.option_ids}>"

class Poll:
    '''
    This object contains information about a poll.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self.question : str = kwargs["question"]
        self.options : List[PollOption] = [PollOption(**option) for option in (kwargs.get("options",None))]
        self.total_voter_count : int = kwargs["total_voter_count"]
        self.is_closed : bool = kwargs["is_closed"]
        self.is_anonymous : bool = kwargs["is_anonymous"]
        self.type : str = kwargs["type"]
        self.allows_multiple_answers : bool = kwargs["allows_multiple_answers"]

        
        self.correct_option_id : int = kwargs.get("correct_option_id",None)
        self.explanation : str = kwargs.get("explanation",None)
        self.explanation_entities : List[MessageEntity] = [MessageEntity(**messageentity) for messageentity in (kwargs.get("explanation_entities",None))]
        self.open_period : int = kwargs.get("open_period",None)
        self.close_date : int = kwargs.get("close_date",None)

    def __repr__(self):
        return f"<Telpy.Poll object @{hex(id(self))} id={self.id} question={self.question} total_voter_count={self.total_voter_count} is_closed={self.is_closed} is_anonymous={self.is_anonymous} type={self.type} allows_multiple_answers={self.allows_multiple_answers}>"

class Location:
    '''
    This object represents a point on the map.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.longitude : float = kwargs["longitude"]
        self.latitude : float = kwargs["latitude"]

        
        self.horizontal_accuracy : float = kwargs.get("horizontal_accuracy",None)
        self.live_period : int = kwargs.get("live_period",None)
        self.heading : int = kwargs.get("heading",None)
        self.proximity_alert_radius : int = kwargs.get("proximity_alert_radius",None)

    def __repr__(self):
        return f"<Telpy.Location object @{hex(id(self))} longitude={self.longitude} latitude={self.latitude}>"

class Venue:
    '''
    This object represents a venue.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.location : Location = Location(**(kwargs["location"]))
        self.title : str = kwargs["title"]
        self.address : str = kwargs["address"]

        
        self.foursquare_id : str = kwargs.get("foursquare_id",None)
        self.foursquare_type : str = kwargs.get("foursquare_type",None)
        self.google_place_id : str = kwargs.get("google_place_id",None)
        self.google_place_type : str = kwargs.get("google_place_type",None)

    def __repr__(self):
        return f"<Telpy.Venue object @{hex(id(self))} title={self.title} address={self.address}>"

class ProximityAlertTriggered:
    '''
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.traveler : User = User(**(kwargs["traveler"]))
        self.watcher : User = User(**(kwargs["watcher"]))
        self.distance : int = kwargs["distance"]

    def __repr__(self):
        return f"<Telpy.ProximityAlertTriggered object @{hex(id(self))} distance={self.distance}>"

class MessageAutoDeleteTimerChanged:
    '''
    This object represents a service message about a change in auto-delete timer settings.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.message_auto_delete_time : int = kwargs["message_auto_delete_time"]

    def __repr__(self):
        return f"<Telpy.MessageAutoDeleteTimerChanged object @{hex(id(self))} message_auto_delete_time={self.message_auto_delete_time}>"

class VoiceChatScheduled:
    '''
    This object represents a service message about a voice chat scheduled in the chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.start_date : int = kwargs["start_date"]

    def __repr__(self):
        return f"<Telpy.VoiceChatScheduled object @{hex(id(self))} start_date={self.start_date}>"

class VoiceChatStarted:
    '''
    This object represents a service message about a voice chat started in the chat. Currently holds no information.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        pass

    def __repr__(self):
        return f"<Telpy.VoiceChatStarted object @{hex(id(self))}"

class VoiceChatEnded:
    '''
    This object represents a service message about a voice chat ended in the chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.duration : int = kwargs["duration"]

    def __repr__(self):
        return f"<Telpy.VoiceChatEnded object @{hex(id(self))} duration={self.duration}>"

class VoiceChatParticipantsInvited:
    '''
    This object represents a service message about new members invited to a voice chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        
        self.users : List[User] = [User(**user) for user in (kwargs.get("users",None))]

    def __repr__(self):
        return f"<Telpy.VoiceChatParticipantsInvited object @{hex(id(self))}>"

class UserProfilePhotos:
    '''
    This object represent a user's profile pictures.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.total_count : int = kwargs["total_count"]
        self.photos : List[List[PhotoSize]] = [[PhotoSize(**(obj)) for obj in row] for row in kwargs.get("photos",None)]

    def __repr__(self):
        return f"<Telpy.UserProfilePhotos object @{hex(id(self))} total_count={self.total_count}>"

class File:
    '''
    This object represents a file ready to be downloaded. It is guaranteed that the url_link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling get_file.
    Maximum file size to download is 20 MB
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]

        
        self.file_size : int = kwargs.get("file_size",None)
        self.file_path : str = kwargs.get("file_path",None)

    # Special
    def url_link(self, client_object):
        token = getattr(client_object,"token",None)
        if token == None:
            raise InvalidArgument(f"Expected <Telpy.Client> object with attribute 'token', got {type(client_object)}")
        return f"https://api.telegram.org/file/bot{token}/{self.file_path}"

    def __repr__(self):
        return f"<Telpy.File object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id}>"

class ReplyKeyboardMarkup:
    '''
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.keyboard : List[List[KeyboardButton]] = [[KeyboardButton(**(obj)) for obj in row] for row in kwargs.get("keyboard",None)]

        
        self.resize_keyboard : bool = kwargs.get("resize_keyboard",None)
        self.one_time_keyboard : bool = kwargs.get("one_time_keyboard",None)
        self.input_field_placeholder : str = kwargs.get("input_field_placeholder",None)
        self.selective : bool = kwargs.get("selective",None)

    def __repr__(self):
        return f"<Telpy.ReplyKeyboardMarkup object @{hex(id(self))}>"

class KeyboardButton:
    '''
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.text : str = kwargs["text"]

        
        self.request_contact : bool = kwargs.get("request_contact",None)
        self.request_location : bool = kwargs.get("request_location",None)
        self.request_poll : KeyboardButtonPollType = kwargs.get("request_poll",None)

    def __repr__(self):
        return f"<Telpy.KeyboardButton object @{hex(id(self))} text={self.text}>"

class KeyboardButtonPollType:
    '''
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        
        self.type : str = kwargs.get("type",None)

    def __repr__(self):
        return f"<Telpy.KeyboardButtonPollType object @{hex(id(self))}>"

class ReplyKeyboardRemove:
    '''
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.remove_keyboard : bool = kwargs["remove_keyboard"]

        
        self.selective : bool = kwargs.get("selective",None)

    def __repr__(self):
        return f"<Telpy.ReplyKeyboardRemove object @{hex(id(self))} remove_keyboard={self.remove_keyboard}>"

class InlineKeyboardMarkup:
    '''
    This object represents an inline keyboard that appears right next to the message it belongs to.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.inline_keyboard : List[List[InlineKeyboardButton]] = [[InlineKeyboardButton(**(obj)) for obj in row] for row in kwargs.get("inline_keyboard",None)]

    def __repr__(self):
        return f"<Telpy.InlineKeyboardMarkup object @{hex(id(self))}>"

class InlineKeyboardButton:
    '''
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.text : str = kwargs["text"]

        
        self.url : str = kwargs.get("url",None)
        self.login_url : LoginUrl = kwargs.get("login_url",None)
        self.callback_data : str = kwargs.get("callback_data",None)
        self.switch_inline_query : str = kwargs.get("switch_inline_query",None)
        self.switch_inline_query_current_chat : str = kwargs.get("switch_inline_query_current_chat",None)
        self.callback_game : CallbackGame = kwargs.get("callback_game",None)
        self.pay : bool = kwargs.get("pay",None)

    def __repr__(self):
        return f"<Telpy.InlineKeyboardButton object @{hex(id(self))} text={self.text}>"
class LoginUrl:
    '''
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.url : str = kwargs["url"]

        
        self.forward_text : str = kwargs.get("forward_text",None)
        self.bot_username : str = kwargs.get("bot_username",None)
        self.request_write_access : bool = kwargs.get("request_write_access",None)

    def __repr__(self):
        return f"<Telpy.LoginUrl object @{hex(id(self))} url={self.url}>"

class CallbackQuery:
    '''
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self._from : User = User(**(kwargs["from"]))
        self.chat_instance : str = kwargs["chat_instance"]

        
        self.message : Message = Message(**(kwargs.get("message",None)))
        self.inline_message_id : str = kwargs.get("inline_message_id",None)
        self.data : str = kwargs.get("data",None)
        self.game_short_name : str = kwargs.get("game_short_name",None)

    def __repr__(self):
        return f"<Telpy.CallbackQuery object @{hex(id(self))} id={self.id} chat_instance={self.chat_instance}>"

class ForceReply:
    '''
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.force_reply : bool = kwargs["force_reply"]

        
        self.input_field_placeholder : str = kwargs.get("input_field_placeholder",None)
        self.selective : bool = kwargs.get("selective",None)

    def __repr__(self):
        return f"<Telpy.ForceReply object @{hex(id(self))} force_reply={self.force_reply}>"

class ChatPhoto:
    '''
    This object represents a chat photo.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.small_file_id : str = kwargs["small_file_id"]
        self.small_file_unique_id : str = kwargs["small_file_unique_id"]
        self.big_file_id : str = kwargs["big_file_id"]
        self.big_file_unique_id : str = kwargs["big_file_unique_id"]

    def __repr__(self):
        return f"<Telpy.ChatPhoto object @{hex(id(self))} small_file_id={self.small_file_id} small_file_unique_id={self.small_file_unique_id} big_file_id={self.big_file_id} big_file_unique_id={self.big_file_unique_id}>"

class ChatInviteLink:
    '''
    Represents an invite link for a chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.invite_link : str = kwargs["invite_link"]
        self.creator : User = User(**(kwargs["creator"]))
        self.creates_join_request : bool = kwargs["creates_join_request"]
        self.is_primary : bool = kwargs["is_primary"]
        self.is_revoked : bool = kwargs["is_revoked"]

        
        self.name : str = kwargs.get("name",None)
        self.expire_date : int = kwargs.get("expire_date",None)
        self.member_limit : int = kwargs.get("member_limit",None)
        self.pending_join_request_count : int = kwargs.get("pending_join_request_count",None)

    def __repr__(self):
        return f"<Telpy.ChatInviteLink object @{hex(id(self))} invite_link={self.invite_link} creates_join_request={self.creates_join_request} is_primary={self.is_primary} is_revoked={self.is_revoked}>"

class ChatMemberOwner:
    '''
    Represents a chat member that owns the chat and has all administrator privileges.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))
        self.is_anonymous : bool = kwargs["is_anonymous"]

        
        self.custom_title : str = kwargs.get("custom_title",None)

    def __repr__(self):
        return f"<Telpy.ChatMemberOwner object @{hex(id(self))} status={self.status} is_anonymous={self.is_anonymous}>"

class ChatMemberAdministrator:
    '''
    Represents a chat member that has some additional privileges.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))
        self.can_be_edited : bool = kwargs["can_be_edited"]
        self.is_anonymous : bool = kwargs["is_anonymous"]
        self.can_manage_chat : bool = kwargs["can_manage_chat"]
        self.can_delete_messages : bool = kwargs["can_delete_messages"]
        self.can_manage_voice_chats : bool = kwargs["can_manage_voice_chats"]
        self.can_restrict_members : bool = kwargs["can_restrict_members"]
        self.can_promote_members : bool = kwargs["can_promote_members"]
        self.can_change_info : bool = kwargs["can_change_info"]
        self.can_invite_users : bool = kwargs["can_invite_users"]

        
        self.can_post_messages : bool = kwargs.get("can_post_messages",None)
        self.can_edit_messages : bool = kwargs.get("can_edit_messages",None)
        self.can_pin_messages : bool = kwargs.get("can_pin_messages",None)
        self.custom_title : str = kwargs.get("custom_title",None)

    def __repr__(self):
        return f"<Telpy.ChatMemberAdministrator object @{hex(id(self))} status={self.status} can_be_edited={self.can_be_edited} is_anonymous={self.is_anonymous} can_manage_chat={self.can_manage_chat} can_delete_messages={self.can_delete_messages} can_manage_voice_chats={self.can_manage_voice_chats} can_restrict_members={self.can_restrict_members} can_promote_members={self.can_promote_members} can_change_info={self.can_change_info} can_invite_users={self.can_invite_users}>"

class ChatMemberMember:
    '''
    Represents a chat member that has no additional privileges or restrictions.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))

    def __repr__(self):
        return f"<Telpy.ChatMemberMember object @{hex(id(self))} status={self.status}>"

class ChatMemberRestricted:
    '''
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))
        self.is_member : bool = kwargs["is_member"]
        self.can_change_info : bool = kwargs["can_change_info"]
        self.can_invite_users : bool = kwargs["can_invite_users"]
        self.can_pin_messages : bool = kwargs["can_pin_messages"]
        self.can_send_messages : bool = kwargs["can_send_messages"]
        self.can_send_media_messages : bool = kwargs["can_send_media_messages"]
        self.can_send_polls : bool = kwargs["can_send_polls"]
        self.can_send_other_messages : bool = kwargs["can_send_other_messages"]
        self.can_add_web_page_previews : bool = kwargs["can_add_web_page_previews"]
        self.until_date : int = kwargs["until_date"]

    def __repr__(self):
        return f"<Telpy.ChatMemberRestricted object @{hex(id(self))} status={self.status} is_member={self.is_member} can_change_info={self.can_change_info} can_invite_users={self.can_invite_users} can_pin_messages={self.can_pin_messages} can_send_messages={self.can_send_messages} can_send_media_messages={self.can_send_media_messages} can_send_polls={self.can_send_polls} can_send_other_messages={self.can_send_other_messages} can_add_web_page_previews={self.can_add_web_page_previews} until_date={self.until_date}>"

class ChatMemberLeft:
    '''
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))

    def __repr__(self):
        return f"<Telpy.ChatMemberLeft object @{hex(id(self))} status={self.status}>"

class ChatMemberBanned:
    '''
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.status : str = kwargs["status"]
        self.user : User = User(**(kwargs["user"]))
        self.until_date : int = kwargs["until_date"]

    def __repr__(self):
        return f"<Telpy.ChatMemberBanned object @{hex(id(self))} status={self.status} until_date={self.until_date}>"

ChatMember = Union[ChatMemberOwner,ChatMemberAdministrator,ChatMemberMember,ChatMemberRestricted,ChatMemberLeft,ChatMemberBanned]
class ChatMemberUpdated:
    '''
    This object represents changes in the status of a chat member.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.chat : Chat = kwargs["chat"]
        self._from : User = User(**(kwargs["from"]))
        self.date : int = kwargs["date"]
        self.old_chat_member : ChatMember = kwargs["old_chat_member"]
        self.new_chat_member : ChatMember = kwargs["new_chat_member"]

        
        self.invite_link : ChatInviteLink = kwargs.get("invite_link",None)

    def __repr__(self):
        return f"<Telpy.ChatMemberUpdated object @{hex(id(self))} date={self.date}>"

class ChatJoinRequest:
    '''
    Represents a join request sent to a chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.chat : Chat = kwargs["chat"]
        self._from : User = User(**(kwargs["from"]))
        self.date : int = kwargs["date"]

        
        self.bio : str = kwargs.get("bio",None)
        self.invite_link : ChatInviteLink = kwargs.get("invite_link",None)

    def __repr__(self):
        return f"<Telpy.ChatJoinRequest object @{hex(id(self))} date={self.date}>"

class ChatPermissions:
    '''
    Describes actions that a non-administrator user is allowed to take in a chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        
        self.can_send_messages : bool = kwargs.get("can_send_messages",None)
        self.can_send_media_messages : bool = kwargs.get("can_send_media_messages",None)
        self.can_send_polls : bool = kwargs.get("can_send_polls",None)
        self.can_send_other_messages : bool = kwargs.get("can_send_other_messages",None)
        self.can_add_web_page_previews : bool = kwargs.get("can_add_web_page_previews",None)
        self.can_change_info : bool = kwargs.get("can_change_info",None)
        self.can_invite_users : bool = kwargs.get("can_invite_users",None)
        self.can_pin_messages : bool = kwargs.get("can_pin_messages",None)

    def __repr__(self):
        return f"<Telpy.ChatPermissions object @{hex(id(self))}>"

class ChatLocation:
    '''
    Represents a location to which a chat is connected.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.location : Location = kwargs["location"]
        self.address : str = kwargs["address"]

    def __repr__(self):
        return f"<Telpy.ChatLocation object @{hex(id(self))} address={self.address}>"

class BotCommand:
    '''
    This object represents a bot command.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.command : str = kwargs["command"]
        self.description : str = kwargs["description"]

    def __repr__(self):
        return f"<Telpy.BotCommand object @{hex(id(self))} command={self.command} description={self.description}>"

class BotCommandScopeDefault:
    '''
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeDefault object @{hex(id(self))} type={self.type}>"

class BotCommandScopeAllPrivateChats:
    '''
    Represents the scope of bot commands, covering all private chats.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeAllPrivateChats object @{hex(id(self))} type={self.type}>"

class BotCommandScopeAllGroupChats:
    '''
    Represents the scope of bot commands, covering all group and supergroup chats.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeAllGroupChats object @{hex(id(self))} type={self.type}>"

class BotCommandScopeAllChatAdministrators:
    '''
    Represents the scope of bot commands, covering all group and supergroup chat administrators.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeAllChatAdministrators object @{hex(id(self))} type={self.type}>"

class BotCommandScopeChat:
    '''
    Represents the scope of bot commands, covering a specific chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.chat_id : Union[int,str] = kwargs["chat_id"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeChat object @{hex(id(self))} type={self.type}>"

class BotCommandScopeChatAdministrators:
    '''
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.chat_id : Union[int,str] = kwargs["chat_id"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeChatAdministrators object @{hex(id(self))} type={self.type}>"

class BotCommandScopeChatMember:
    '''
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.chat_id : Union[int,str] = kwargs["chat_id"]
        self.user_id : int = kwargs["user_id"]

    def __repr__(self):
        return f"<Telpy.BotCommandScopeChatMember object @{hex(id(self))} type={self.type} user_id={self.user_id}>"

class ResponseParameters:
    '''
    Contains information about why a request was unsuccessful.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        
        self.migrate_to_chat_id : int = kwargs.get("migrate_to_chat_id",None)
        self.retry_after : int = kwargs.get("retry_after",None)

    def __repr__(self):
        return f"<Telpy.ResponseParameters object @{hex(id(self))}>"

class InputMediaPhoto:
    '''
    Represents a photo to be sent.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.media : str = kwargs["media"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)

    def __repr__(self):
        return f"<Telpy.InputMediaPhoto object @{hex(id(self))} type={self.type} media={self.media}>"

class InputMediaVideo:
    '''
    Represents a video to be sent.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.media : str = kwargs["media"]

        
        self.thumb : InputFile or str = kwargs.get("thumb",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.width : int = kwargs.get("width",None)
        self.height : int = kwargs.get("height",None)
        self.duration : int = kwargs.get("duration",None)
        self.supports_streaming : bool = kwargs.get("supports_streaming",None)

    def __repr__(self):
        return f"<Telpy.InputMediaVideo object @{hex(id(self))} type={self.type} media={self.media}>"

class InputMediaAnimation:
    '''
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.media : str = kwargs["media"]

        
        self.thumb : InputFile or str = kwargs.get("thumb",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.width : int = kwargs.get("width",None)
        self.height : int = kwargs.get("height",None)
        self.duration : int = kwargs.get("duration",None)

    def __repr__(self):
        return f"<Telpy.InputMediaAnimation object @{hex(id(self))} type={self.type} media={self.media}>"

class InputMediaAudio:
    '''
    Represents an audio file to be treated as music to be sent.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.media : str = kwargs["media"]

        
        self.thumb : InputFile or str = kwargs.get("thumb",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.duration : int = kwargs.get("duration",None)
        self.performer : str = kwargs.get("performer",None)
        self.title : str = kwargs.get("title",None)

    def __repr__(self):
        return f"<Telpy.InputMediaAudio object @{hex(id(self))} type={self.type} media={self.media}>"

class InputMediaDocument:
    '''
    Represents a general file to be sent.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.media : str = kwargs["media"]

        
        self.thumb : InputFile or str = kwargs.get("thumb",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.disable_content_type_detection : bool = kwargs.get("disable_content_type_detection",None)

    def __repr__(self):
        return f"<Telpy.InputMediaDocument object @{hex(id(self))} type={self.type} media={self.media}>"

class InputFile:
    '''
    This object represents the contents of a file to be uploaded.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]

    def __repr__(self):
        return f"<Telpy.InputFile object @{hex(id(self))} file_id={self.file_id}>"

# Stickers
class Sticker:
    '''
    This object represents a sticker.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.width : int = kwargs["width"]
        self.height : int = kwargs["height"]
        self.is_animated : bool = kwargs["is_animated"]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))
        self.emoji : str = kwargs.get("emoji",None)
        self.set_name : str = kwargs.get("set_name",None)
        self.mask_position : MaskPosition = MaskPosition(**(kwargs.get("mask_position",None)))
        self.file_size : int = kwargs.get("file_size",None)

    def __repr__(self):
        return f"<Telpy.Sticker object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} width={self.width} height={self.height} is_animated={self.is_animated}>"

class StickerSet:
    '''
    This object represents a sticker set.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.name : str = kwargs["name"]
        self.title : str = kwargs["title"]
        self.is_animated : bool = kwargs["is_animated"]
        self.contains_masks : bool = kwargs["contains_masks"]
        self.stickers : List[Sticker] = [Sticker(**sticker) for sticker in (kwargs.get("stickers",None))]

        
        self.thumb : PhotoSize = PhotoSize(**(kwargs.get("thumb",None)))

    def __repr__(self):
        return f"<Telpy.StickerSet object @{hex(id(self))} name={self.name} title={self.title} is_animated={self.is_animated} contains_masks={self.contains_masks}>"
class MaskPosition:
    '''
    This object describes the position on faces where a mask should be placed by default.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.point : str = kwargs["point"]
        self.x_shift : float = kwargs["x_shift"]
        self.y_shift : float = kwargs["y_shift"]
        self.scale : float = kwargs["scale"]

    def __repr__(self):
        return f"<Telpy.MaskPosition object @{hex(id(self))} point={self.point}>"

# Inline Query
class InlineQuery:
    '''
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self.From : User = User(**(kwargs["from"]))
        self.query : str = kwargs["query"]
        self.offset : str = kwargs["offset"]

        
        self.chat_type : str = kwargs.get("chat_type",None)
        self.location : Location = Location(**(kwargs.get("location",None)))

    def __repr__(self):
        return f"<Telpy.InlineQuery object @{hex(id(self))} id={self.id} query={self.query} offset={self.offset}>"

class InlineQueryResultArticle:
    '''
    Represents a link to an article or web page.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.title : str = kwargs["title"]
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs["input_message_content"]))

        
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.url : str = kwargs.get("url",None)
        self.hide_url : bool = kwargs.get("hide_url",None)
        self.description : str = kwargs.get("description",None)
        self.thumb_url : str = kwargs.get("thumb_url",None)
        self.thumb_width : int = kwargs.get("thumb_width",None)
        self.thumb_height : int = kwargs.get("thumb_height",None)

    def __repr__(self):
        return f"<Telpy.InlineQueryResultArticle object @{hex(id(self))} type={self.type} id={self.id} title={self.title}>"

class InlineQueryResultPhoto:
    '''
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.photo_url : str = kwargs["photo_url"]
        self.thumb_url : str = kwargs["thumb_url"]

        
        self.photo_width : int = kwargs.get("photo_width",None)
        self.photo_height : int = kwargs.get("photo_height",None)
        self.title : str = kwargs.get("title",None)
        self.description : str = kwargs.get("description",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultPhoto object @{hex(id(self))} type={self.type} id={self.id} photo_url={self.photo_url} thumb_url={self.thumb_url}>"

class InlineQueryResultGif:
    '''
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.gif_url : str = kwargs["gif_url"]
        self.thumb_url : str = kwargs["thumb_url"]

        
        self.gif_width : int = kwargs.get("gif_width",None)
        self.gif_height : int = kwargs.get("gif_height",None)
        self.gif_duration : int = kwargs.get("gif_duration",None)
        self.thumb_mime_type : str = kwargs.get("thumb_mime_type",None)
        self.title : str = kwargs.get("title",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultGif object @{hex(id(self))} type={self.type} id={self.id} gif_url={self.gif_url} thumb_url={self.thumb_url}>"

class InlineQueryResultMpeg4Gif:
    '''
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.mpeg4_url : str = kwargs["mpeg4_url"]
        self.thumb_url : str = kwargs["thumb_url"]

        
        self.mpeg4_width : int = kwargs.get("mpeg4_width",None)
        self.mpeg4_height : int = kwargs.get("mpeg4_height",None)
        self.mpeg4_duration : int = kwargs.get("mpeg4_duration",None)
        self.thumb_mime_type : str = kwargs.get("thumb_mime_type",None)
        self.title : str = kwargs.get("title",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultMpeg4Gif object @{hex(id(self))} type={self.type} id={self.id} mpeg4_url={self.mpeg4_url} thumb_url={self.thumb_url}>"

class InlineQueryResultVideo:
    '''
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.\nIf an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.video_url : str = kwargs["video_url"]
        self.mime_type : str = kwargs["mime_type"]
        self.thumb_url : str = kwargs["thumb_url"]
        self.title : str = kwargs["title"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.video_width : int = kwargs.get("video_width",None)
        self.video_height : int = kwargs.get("video_height",None)
        self.video_duration : int = kwargs.get("video_duration",None)
        self.description : str = kwargs.get("description",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultVideo object @{hex(id(self))} type={self.type} id={self.id} video_url={self.video_url} mime_type={self.mime_type} thumb_url={self.thumb_url} title={self.title}>"

class InlineQueryResultAudio:
    '''
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.audio_url : str = kwargs["audio_url"]
        self.title : str = kwargs["title"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.performer : str = kwargs.get("performer",None)
        self.audio_duration : int = kwargs.get("audio_duration",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultAudio object @{hex(id(self))} type={self.type} id={self.id} audio_url={self.audio_url} title={self.title}>"

class InlineQueryResultVoice:
    '''
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.voice_url : str = kwargs["voice_url"]
        self.title : str = kwargs["title"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.voice_duration : int = kwargs.get("voice_duration",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultVoice object @{hex(id(self))} type={self.type} id={self.id} voice_url={self.voice_url} title={self.title}>"

class InlineQueryResultDocument:
    '''
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.title : str = kwargs["title"]
        self.document_url : str = kwargs["document_url"]
        self.mime_type : str = kwargs["mime_type"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = kwargs.get("caption_entities",None)
        self.description : str = kwargs.get("description",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))
        self.thumb_url : str = kwargs.get("thumb_url",None)
        self.thumb_width : int = kwargs.get("thumb_width",None)
        self.thumb_height : int = kwargs.get("thumb_height",None)

    def __repr__(self):
        return f"<Telpy.InlineQueryResultDocument object @{hex(id(self))} type={self.type} id={self.id} title={self.title} document_url={self.document_url} mime_type={self.mime_type}>"

class InlineQueryResultLocation:
    '''
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.latitude : float = kwargs["latitude"]
        self.longitude : float = kwargs["longitude"]
        self.title : str = kwargs["title"]

        
        self.horizontal_accuracy : float = kwargs.get("horizontal_accuracy",None)
        self.live_period : int = kwargs.get("live_period",None)
        self.heading : int = kwargs.get("heading",None)
        self.proximity_alert_radius : int = kwargs.get("proximity_alert_radius",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))
        self.thumb_url : str = kwargs.get("thumb_url",None)
        self.thumb_width : int = kwargs.get("thumb_width",None)
        self.thumb_height : int = kwargs.get("thumb_height",None)

    def __repr__(self):
        return f"<Telpy.InlineQueryResultLocation object @{hex(id(self))} type={self.type} id={self.id} title={self.title}>"

class InlineQueryResultVenue:
    '''
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.latitude : float = kwargs["latitude"]
        self.longitude : float = kwargs["longitude"]
        self.title : str = kwargs["title"]
        self.address : str = kwargs["address"]

        
        self.foursquare_id : str = kwargs.get("foursquare_id",None)
        self.foursquare_type : str = kwargs.get("foursquare_type",None)
        self.google_place_id : str = kwargs.get("google_place_id",None)
        self.google_place_type : str = kwargs.get("google_place_type",None)
        self.reply_markup : InlineKeyboardMarkup = kwargs.get("reply_markup",None)
        self.input_message_content : InputMessageContent = kwargs.get("input_message_content",None)
        self.thumb_url : str = kwargs.get("thumb_url",None)
        self.thumb_width : int = kwargs.get("thumb_width",None)
        self.thumb_height : int = kwargs.get("thumb_height",None)

    def __repr__(self):
        return f"<Telpy.InlineQueryResultVenue object @{hex(id(self))} type={self.type} id={self.id} latitude={self.latitude} longitude={self.longitude} title={self.title} address={self.address}>"

class InlineQueryResultContact:
    '''
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.phone_number : str = kwargs["phone_number"]
        self.first_name : str = kwargs["first_name"]

        
        self.last_name : str = kwargs.get("last_name",None)
        self.vcard : str = kwargs.get("vcard",None)
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))
        self.thumb_url : str = kwargs.get("thumb_url",None)
        self.thumb_width : int = kwargs.get("thumb_width",None)
        self.thumb_height : int = kwargs.get("thumb_height",None)

    def __repr__(self):
        return f"<Telpy.InlineQueryResultContact object @{hex(id(self))} type={self.type} id={self.id} phone_number={self.phone_number} first_name={self.first_name}>"

class InlineQueryResultGame:
    '''
    Represents a Game.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.game_short_name : str = kwargs["game_short_name"]

        
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultGame object @{hex(id(self))} type={self.type} id={self.id} game_short_name={self.game_short_name}>"

class InlineQueryResultCachedPhoto:
    '''
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.photo_file_id : str = kwargs["photo_file_id"]

        
        self.title : str = kwargs.get("title",None)
        self.description : str = kwargs.get("description",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedPhoto object @{hex(id(self))} type={self.type} id={self.id} photo_file_id={self.photo_file_id}>"

class InlineQueryResultCachedGif:
    '''
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.gif_file_id : str = kwargs["gif_file_id"]

        
        self.title : str = kwargs.get("title",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedGif object @{hex(id(self))} type={self.type} id={self.id} gif_file_id={self.gif_file_id}>"

class InlineQueryResultCachedMpeg4Gif:
    '''
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.mpeg4_file_id : str = kwargs["mpeg4_file_id"]

        
        self.title : str = kwargs.get("title",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedMpeg4Gif object @{hex(id(self))} type={self.type} id={self.id} mpeg4_file_id={self.mpeg4_file_id}>"

class InlineQueryResultCachedSticker:
    '''
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.sticker_file_id : str = kwargs["sticker_file_id"]

        
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedSticker object @{hex(id(self))} type={self.type} id={self.id} sticker_file_id={self.sticker_file_id}>"

class InlineQueryResultCachedDocument:
    '''
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.title : str = kwargs["title"]
        self.document_file_id : str = kwargs["document_file_id"]

        
        self.description : str = kwargs.get("description",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedDocument object @{hex(id(self))} type={self.type} id={self.id} title={self.title} document_file_id={self.document_file_id}>"

class InlineQueryResultCachedVideo:
    '''
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.video_file_id : str = kwargs["video_file_id"]
        self.title : str = kwargs["title"]

        
        self.description : str = kwargs.get("description",None)
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedVideo object @{hex(id(self))} type={self.type} id={self.id} video_file_id={self.video_file_id} title={self.title}>"

class InlineQueryResultCachedVoice:
    '''
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.voice_file_id : str = kwargs["voice_file_id"]
        self.title : str = kwargs["title"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedVoice object @{hex(id(self))} type={self.type} id={self.id} voice_file_id={self.voice_file_id} title={self.title}>"

class InlineQueryResultCachedAudio:
    '''
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.id : str = kwargs["id"]
        self.audio_file_id : str = kwargs["audio_file_id"]

        
        self.caption : str = kwargs.get("caption",None)
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.caption_entities : List[MessageEntity] = [MessageEntity(**caption_entity) for caption_entity in (kwargs.get("caption_entities",None))]
        self.reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup(**(kwargs.get("reply_markup",None)))
        self.input_message_content : InputMessageContent = InputMessageContent(**(kwargs.get("input_message_content",None)))

    def __repr__(self):
        return f"<Telpy.InlineQueryResultCachedAudio object @{hex(id(self))} type={self.type} id={self.id} audio_file_id={self.audio_file_id}>"

# Input Message Content

class InputTextMessageContent:
    '''
    Represents the content of a text message to be sent as the result of an inline query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.message_text : str = kwargs["message_text"]

        
        self.parse_mode : str = kwargs.get("parse_mode",None)
        self.entities : List[MessageEntity] = [MessageEntity(**entity) for entity in (kwargs.get("entities",None))]
        self.disable_web_page_preview : bool = kwargs.get("disable_web_page_preview",None)

    def __repr__(self):
        return f"<Telpy.InputTextMessageContent object @{hex(id(self))} message_text={self.message_text}>"

class InputLocationMessageContent:
    '''
    Represents the content of a location message to be sent as the result of an inline query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.latitude : float = kwargs["latitude"]
        self.longitude : float = kwargs["longitude"]

        
        self.horizontal_accuracy : float = kwargs.get("horizontal_accuracy",None)
        self.live_period : int = kwargs.get("live_period",None)
        self.heading : int = kwargs.get("heading",None)
        self.proximity_alert_radius : int = kwargs.get("proximity_alert_radius",None)

    def __repr__(self):
        return f"<Telpy.InputLocationMessageContent object @{hex(id(self))} latitude={self.latitude} longitude={self.longitude}>"

class InputVenueMessageContent:
    '''
    Represents the content of a venue message to be sent as the result of an inline query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.latitude : float = kwargs["latitude"]
        self.longitude : float = kwargs["longitude"]
        self.title : str = kwargs["title"]
        self.address : str = kwargs["address"]

        
        self.foursquare_id : str = kwargs.get("foursquare_id",None)
        self.foursquare_type : str = kwargs.get("foursquare_type",None)
        self.google_place_id : str = kwargs.get("google_place_id",None)
        self.google_place_type : str = kwargs.get("google_place_type",None)

    def __repr__(self):
        return f"<Telpy.InputVenueMessageContent object @{hex(id(self))} latitude={self.latitude} longitude={self.longitude} title={self.title} address={self.address}>"

class InputContactMessageContent:
    '''
    Represents the content of a contact message to be sent as the result of an inline query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.phone_number : str = kwargs["phone_number"]
        self.first_name : str = kwargs["first_name"]

        
        self.last_name : str = kwargs.get("last_name",None)
        self.vcard : str = kwargs.get("vcard",None)

    def __repr__(self):
        return f"<Telpy.InputContactMessageContent object @{hex(id(self))} phone_number={self.phone_number} first_name={self.first_name}>"

class InputInvoiceMessageContent:
    '''
    Represents the content of an invoice message to be sent as the result of an inline query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.title : str = kwargs["title"]
        self.description : str = kwargs["description"]
        self.payload : str = kwargs["payload"]
        self.provider_token : str = kwargs["provider_token"]
        self.currency : str = kwargs["currency"]
        self.prices : List[LabeledPrice] = [LabeledPrice(**kwargs["prices"]) for kwargs["prices"] in (kwargs["prices"])]

        
        self.max_tip_amount : int = kwargs.get("max_tip_amount",None)
        self.suggested_tip_amounts : List[int] = kwargs.get("suggested_tip_amounts",None)
        self.provider_data : str = kwargs.get("provider_data",None)
        self.photo_url : str = kwargs.get("photo_url",None)
        self.photo_size : int = kwargs.get("photo_size",None)
        self.photo_width : int = kwargs.get("photo_width",None)
        self.photo_height : int = kwargs.get("photo_height",None)
        self.need_name : bool = kwargs.get("need_name",None)
        self.need_phone_number : bool = kwargs.get("need_phone_number",None)
        self.need_email : bool = kwargs.get("need_email",None)
        self.need_shipping_address : bool = kwargs.get("need_shipping_address",None)
        self.send_phone_number_to_provider : bool = kwargs.get("send_phone_number_to_provider",None)
        self.send_email_to_provider : bool = kwargs.get("send_email_to_provider",None)
        self.is_flexible : bool = kwargs.get("is_flexible",None)

    def __repr__(self):
        return f"<Telpy.InputInvoiceMessageContent object @{hex(id(self))} title={self.title} description={self.description} payload={self.payload} provider_token={self.provider_token} currency={self.currency}>"

InputMessageContent = [InputTextMessageContent,InputLocationMessageContent,InputVenueMessageContent,InputContactMessageContent,InputInvoiceMessageContent]

class ChosenInlineResult:
    '''
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.result_id : str = kwargs["result_id"]
        self.From : User = User(**(kwargs["from"]))
        self.query : str = kwargs["query"]

        
        self.location : Location = Location(**(kwargs.get("location",None)))
        self.inline_message_id : str = kwargs.get("inline_message_id",None)

    def __repr__(self):
        return f"<Telpy.ChosenInlineResult object @{hex(id(self))} result_id={self.result_id} query={self.query}>"

# Payment
class LabeledPrice:
    '''
    This object represents a portion of the price for goods or services.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.label : str = kwargs["label"]
        self.amount : int = kwargs["amount"]

    def __repr__(self):
        return f"<Telpy.LabeledPrice object @{hex(id(self))} label={self.label} amount={self.amount}>"

class Invoice:
    '''
    This object contains basic information about an invoice.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.title : str = kwargs["title"]
        self.description : str = kwargs["description"]
        self.start_parameter : str = kwargs["start_parameter"]
        self.currency : str = kwargs["currency"]
        self.total_amount : int = kwargs["total_amount"]

    def __repr__(self):
        return f"<Telpy.Invoice object @{hex(id(self))} title={self.title} description={self.description} start_parameter={self.start_parameter} currency={self.currency} total_amount={self.total_amount}>"

class ShippingAddress:
    '''
    This object represents a shipping address.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.country_code : str = kwargs["country_code"]
        self.state : str = kwargs["state"]
        self.city : str = kwargs["city"]
        self.street_line1 : str = kwargs["street_line1"]
        self.street_line2 : str = kwargs["street_line2"]
        self.post_code : str = kwargs["post_code"]

    def __repr__(self):
        return f"<Telpy.ShippingAddress object @{hex(id(self))} country_code={self.country_code} state={self.state} city={self.city} street_line1={self.street_line1} street_line2={self.street_line2} post_code={self.post_code}>"

class OrderInfo:
    '''
    This object represents information about an order.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return

        
        self.name : str = kwargs.get("name",None)
        self.phone_number : str = kwargs.get("phone_number",None)
        self.email : str = kwargs.get("email",None)
        self.shipping_address : ShippingAddress = ShippingAddress(**(kwargs.get("shipping_address",None)))

    def __repr__(self):
        return f"<Telpy.OrderInfo object @{hex(id(self))}>"

class ShippingOption:
    '''
    This object represents one shipping option.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self.title : str = kwargs["title"]
        self.prices : List[LabeledPrice] = [LabeledPrice(**price) for price in (kwargs.get("prices",None))]

    def __repr__(self):
        return f"<Telpy.ShippingOption object @{hex(id(self))} id={self.id} title={self.title}>"

class SuccessfulPayment:
    '''
    This object contains basic information about a successful payment.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.currency : str = kwargs["currency"]
        self.total_amount : int = kwargs["total_amount"]
        self.invoice_payload : str = kwargs["invoice_payload"]
        self.telegram_payment_charge_id : str = kwargs["telegram_payment_charge_id"]
        self.provider_payment_charge_id : str = kwargs["provider_payment_charge_id"]

        
        self.shipping_option_id : str = kwargs.get("shipping_option_id",None)
        self.order_info : OrderInfo = OrderInfo(**(kwargs.get("order_info",None)))

    def __repr__(self):
        return f"<Telpy.SuccessfulPayment object @{hex(id(self))} currency={self.currency} total_amount={self.total_amount} invoice_payload={self.invoice_payload} telegram_payment_charge_id={self.telegram_payment_charge_id} provider_payment_charge_id={self.provider_payment_charge_id}>"

class ShippingQuery:
    '''
    This object contains information about an incoming shipping query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self.From : User = User(**(kwargs["from"]))
        self.invoice_payload : str = kwargs["invoice_payload"]
        self.shipping_address : ShippingAddress = ShippingAddress(**(kwargs["shipping_address"]))

    def __repr__(self):
        return f"<Telpy.ShippingQuery object @{hex(id(self))} id={self.id} invoice_payload={self.invoice_payload}>"

class PreCheckoutQuery:
    '''
    This object contains information about an incoming pre-checkout query.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.id : str = kwargs["id"]
        self.From : User = User(**(kwargs["from"]))
        self.currency : str = kwargs["currency"]
        self.total_amount : int = kwargs["total_amount"]
        self.invoice_payload : str = kwargs["invoice_payload"]

        
        self.shipping_option_id : str = kwargs.get("shipping_option_id",None)
        self.order_info : OrderInfo = OrderInfo(**(kwargs.get("order_info",None)))

    def __repr__(self):
        return f"<Telpy.PreCheckoutQuery object @{hex(id(self))} id={self.id} currency={self.currency} total_amount={self.total_amount} invoice_payload={self.invoice_payload}>"

# Telegram Passport
class PassportData:
    '''
    Contains information about Telegram Passport data shared with the bot by the user.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.data : List[EncryptedPassportElement] = [EncryptedPassportElement(**data) for data in (kwargs.get("data",None))]
        self.credentials : EncryptedCredentials = EncryptedCredentials(**(kwargs["credentials"]))

    def __repr__(self):
        return f"<Telpy.PassportData object @{hex(id(self))}>"

class PassportFile:
    '''
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.file_id : str = kwargs["file_id"]
        self.file_unique_id : str = kwargs["file_unique_id"]
        self.file_size : int = kwargs["file_size"]
        self.file_date : int = kwargs["file_date"]

    def __repr__(self):
        return f"<Telpy.PassportFile object @{hex(id(self))} file_id={self.file_id} file_unique_id={self.file_unique_id} file_size={self.file_size} file_date={self.file_date}>"

class EncryptedPassportElement:
    '''
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.type : str = kwargs["type"]
        self.hash : str = kwargs["hash"]

        
        self.data : str = kwargs.get("data",None)
        self.phone_number : str = kwargs.get("phone_number",None)
        self.email : str = kwargs.get("email",None)
        self.files : List[PassportFile] = [PassportFile(**file) for file in (kwargs.get("files",None))]
        self.front_side : PassportFile = PassportFile(**(kwargs.get("front_side",None)))
        self.reverse_side : PassportFile = PassportFile(**(kwargs.get("reverse_side",None)))
        self.selfie : PassportFile = PassportFile(**(kwargs.get("selfie",None)))
        self.translation : List[PassportFile] = [PassportFile(**translation) for translation in (kwargs.get("translation",None))]

    def __repr__(self):
        return f"<Telpy.EncryptedPassportElement object @{hex(id(self))} type={self.type} hash={self.hash}>"

class EncryptedCredentials:
    '''
    Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.data : str = kwargs["data"]
        self.hash : str = kwargs["hash"]
        self.secret : str = kwargs["secret"]

    def __repr__(self):
        return f"<Telpy.EncryptedCredentials object @{hex(id(self))} data={self.data} hash={self.hash} secret={self.secret}>"

# Passport Element Error
class PassportElementErrorDataField:
    '''
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.field_name : str = kwargs["field_name"]
        self.data_hash : str = kwargs["data_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorDataField object @{hex(id(self))} source={self.source} type={self.type} field_name={self.field_name} data_hash={self.data_hash} message={self.message}>"

class PassportElementErrorFrontSide:
    '''
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hash : str = kwargs["file_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorFrontSide object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorReverseSide:
    '''
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hash : str = kwargs["file_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorReverseSide object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorSelfie:
    '''
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hash : str = kwargs["file_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorSelfie object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorFile:
    '''
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hash : str = kwargs["file_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorFile object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorFiles:
    '''
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hashes : List[str] = kwargs["file_hashes"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorFiles object @{hex(id(self))} source={self.source} type={self.type} message={self.message}>"

class PassportElementErrorTranslationFile:
    '''
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hash : str = kwargs["file_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorTranslationFile object @{hex(id(self))} source={self.source} type={self.type} file_hash={self.file_hash} message={self.message}>"

class PassportElementErrorTranslationFiles:
    '''
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.file_hashes : List[str] = kwargs["file_hashes"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorTranslationFiles object @{hex(id(self))} source={self.source} type={self.type} message={self.message}>"

class PassportElementErrorUnspecified:
    '''
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.source : str = kwargs["source"]
        self.type : str = kwargs["type"]
        self.element_hash : str = kwargs["element_hash"]
        self.message : str = kwargs["message"]

    def __repr__(self):
        return f"<Telpy.PassportElementErrorUnspecified object @{hex(id(self))} source={self.source} type={self.type} element_hash={self.element_hash} message={self.message}>"

# Game
class Game:
    '''
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.title : str = kwargs["title"]
        self.description : str = kwargs["description"]
        self.photo : List[PhotoSize] = [PhotoSize(**photo) for photo in (kwargs.get("photo",None))]

        
        self.text : str = kwargs.get("text",None)
        self.text_entities : List[MessageEntity] = [MessageEntity(**text_entity) for text_entity in (kwargs.get("text_entities",None))]
        self.animation : Animation = Animation(**(kwargs.get("animation",None)))

    def __repr__(self):
        return f"<Telpy.Game object @{hex(id(self))} title={self.title} description={self.description}>"

class CallbackGame:
    '''
    A placeholder, currently holds no information. Use BotFather to set up your game.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        pass

    def __repr__(self):
        return f"<Telpy.CallbackGame object @{hex(id(self))}"

class GameHighScore:
    '''
    This object represents one row of the high scores table for a game.
    '''
    def __init__(self, **kwargs):
        if kwargs == {}:
            return
        self.position : int = kwargs["position"]
        self.user : User = User(**(kwargs["user"]))
        self.score : int = kwargs["score"]

    def __repr__(self):
        return f"<Telpy.GameHighScore object @{hex(id(self))} position={self.position} score={self.score}>"
