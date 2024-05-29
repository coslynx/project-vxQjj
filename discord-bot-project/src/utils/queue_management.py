import asyncio

class QueueManagement:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, song):
        self.queue.append(song)

    def remove_from_queue(self, index):
        if 0 <= index < len(self.queue):
            del self.queue[index]

    def get_queue(self):
        return self.queue

    def clear_queue(self):
        self.queue = []

    async def play_next_song(self):
        if self.queue:
            song = self.queue.pop(0)
            # Code to play the song in the voice channel goes here
            await asyncio.sleep(1)  # Simulating song playing
            print(f"Now playing: {song}")
        else:
            print("Queue is empty. No songs to play.")

    async def skip_song(self):
        if self.queue:
            # Code to skip the current song and play the next one in the voice channel goes here
            await self.play_next_song()
        else:
            print("Queue is empty. No songs to skip.")