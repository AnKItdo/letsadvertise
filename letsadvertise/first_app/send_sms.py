from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6bbcf711c12791e6859dbb27103414d5'
auth_token = 'd1ed9391046e2712c2e969ac552c4f48'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hello ankit",
                     from_='+15017122661',
                     to='+9779860770561'
                 )

print(message.sid)
