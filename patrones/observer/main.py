from subscriber import Subscriber
from youtube import YouTube

youtube_channel = YouTube()

suscriptor1 = Subscriber("Juan")
suscriptor2 = Subscriber("Maria")

youtube_channel.add_observer(suscriptor1)
youtube_channel.add_observer(suscriptor2)

for s in youtube_channel.observers:
    print (s.name)


youtube_channel.set_channel("Hola Soy German")

youtube_channel.delete_channel("Mr Beast")

