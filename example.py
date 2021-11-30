import Telpy, yaml
token = "token"
client = Telpy.Client(token)

@client.event
def on_message(message):
    client.render_response_template(message,yaml.safe_load(open("response.yaml")))
    
client.run()
