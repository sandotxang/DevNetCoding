from webexteamssdk import WebexTeamsAPI

'''
CREATES a room on webexteams
DELETE ALL PREVIOUS ROOMS
ADD user to the room
'''
message = "**I am an IT-Professional, and I have completed this challenge!!!**"

api=WebexTeamsAPI(access_token="ZmNmMDA5ZmYtNmNjNy00YTBlLThkMzUtMDg4YjhiMzJlYmFlNzUwMDFkYTctMzRj_PF84_consumer")


#Deletes previous roms where i belong
mem= api.memberships.list()
for m in mem:
    print(m)
    api.rooms.delete(roomId=m.roomId)


room=api.rooms.create(title="ROOM created with SDK2")

api.messages.create(roomId=room.id, text=message)

#Invites Ariel bot

api.memberships.create(roomId=room.id, personEmail="ariel@webex.bot")



