import irc.bot
import requests
import subprocess

# Twitch IRC configuration
PULL_VOTES = 3
TWITCH_IRC_SERVER = 'irc.chat.twitch.tv'
TWITCH_IRC_PORT = 6667
TWITCH_NICK = 'twitchplayssocialrobots'
TWITCH_OAUTH_TOKEN = '2yns59z4c834zebulrlb7uch6c9syt'
TWITCH_CHANNEL = '#twitchplayssocialrobots'
INTRO_MESSAGE = "Welcome to Twitch Plays Social Robots! This robot should be displaying a emotive behavior. Please type in which emotion the robot looks like it is portraying: Sad, Happy, or Lazy."

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        self.votes_sad = 0
        self.votes_lazy = 0
        self.votes_happy = 0
        self.total_valid_votes = 0
        self.channel = channel
        self.nickname = nickname
        self.oauth_token = TWITCH_OAUTH_TOKEN
        server = server
        port = port
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + self.oauth_token)], nickname, nickname)

    def on_welcome(self, connection, event):
        connection.join(self.channel)
        print(f"Joined {self.channel}")
        self.send_message(INTRO_MESSAGE)

    ## start streaming?
    async def start_stream(self, video_path):
        # Open video file for reading
        with open(video_path, 'rb') as video_file:
            # Send video frames to Twitch chat as messages
            async for frame in video_file:
                await self.send(TWITCH_CHANNEL, frame)

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        print(f"Received message: {message}")

        # bot's logic here
        if "Sad" in message:
            self.send_message('Vote count: ' + str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_sad += 1
        if "sad" in message:
            self.send_message('Vote count: ' +str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_sad += 1
        if "Happy" in message:
            self.send_message('Vote count: ' + str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_happy += 1
        if "happy" in message:
            self.send_message('Vote count: ' + str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_happy += 1
        if "Lazy" in message:
            self.send_message('Vote count: ' + str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_lazy += 1
        if "lazy" in message:
            self.send_message('Vote count: ' + str(self.total_valid_votes))
            self.total_valid_votes += 1
            self.votes_lazy += 1
        print("sad count: " + str(self.votes_sad))
        #####################
        # start integrating interactive part her 
        #####################
        if self.total_valid_votes > 0:
            consensus = str(self.votes_sad/self.total_valid_votes * 100)
            print("consensus: " + str(self.votes_sad/self.total_valid_votes * 100) + "%")
            if self.total_valid_votes == PULL_VOTES:
                print("Vote Maximum Reached... Evolving..")
                with open('poll_chat.txt', 'w') as file:
                    file.write(consensus)
                subprocess.run(['python3', 'search.py'])
                # reset vote counters 
                self.total_valid_votes = 0
                self.votes_sad = 0
        else:
            print("No votes yet.")
        

    def send_message(self, message):
        self.connection.privmsg(self.channel, message)

if __name__ == "__main__":
    bot = TwitchBot(TWITCH_CHANNEL, TWITCH_NICK, TWITCH_IRC_SERVER, TWITCH_IRC_PORT)
    bot.start()
