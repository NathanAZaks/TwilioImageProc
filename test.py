from twilio.rest import Client

client = Client('ACcecd8dc1f34f143557d2fe713048f71f', '3024182f46dc1f3d0d37d953e9a39856')

# message = client.messages.create( \
#     body = "Nathan's test picture",
#     media_url = "https://api.twilio.com/2010-04-01/Accounts/ACcecd8dc1f34f143557d2fe713048f71f/Messages/MM7b3f108da47e0fd307a6947e2685d300/Media/ME86b285b2d7db602320bbe5029ef8ba59",
#     from_ = '+17035469420',
#     to = '+17605766819')

# print (message.sid)

# media = client.messages.list(limit=20)
# print(media)

media1 = client.messages('MM0bb7c04c857c2cd2473324fb3e3c3a23').media('ME253ef97e8d2eb5a5d31a8676a09087f0').fetch().uri

print(media1)

# print(media1.content_type)

# for msg in client.messages.list():
#     if int(msg.num_media) > 0:
#         for media in msg.media.list():
#             media_url = 'https://api.twilio.com' + media.uri[:-5] # Strip off the '.json'
#             print(media_url)
