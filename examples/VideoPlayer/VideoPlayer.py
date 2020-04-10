import asyncio

from EventScheduler import EventScheduler
from Player import Player
from Remote import Remote

async def main():
  eventScheduler = EventScheduler()

  videoPlayer = Player(eventScheduler)
  remote = Remote(eventScheduler, videoPlayer)

  eventScheduler.registerActiveObjects(remote, videoPlayer)
  await eventScheduler.start()

if __name__ == "__main__":
  asyncio.run(main())
