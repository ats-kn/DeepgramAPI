
import asyncio
import pyaudio
from deepgram import Deepgram
from .local_settings import *

# Replace DEEPGRAM_API_KEY with your actual Deepgram API key


async def main():
    # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    # Create a websocket connection to Deepgram
    try:
        deepgramLive = await deepgram.transcription.live({
            'smart_format': True,
            'interim_results': False,
            'language': 'ja',
            'model': 'base',
            'diarize': True
        })
    except Exception as e:
        print(f'Could not open socket: {e}')
        return

    # Listen for the connection to close
    deepgramLive.register_handler(deepgramLive.event.CLOSE, lambda c: print(f'Connection closed with code {c}.'))

    # Listen for any transcripts received from Deepgram and write them to the console
    deepgramLive.register_handler(deepgramLive.event.TRANSCRIPT_RECEIVED, print)

    # Use PyAudio to open a stream from the microphone
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16,
                         rate = 44100,
                         channels = 1, 
                         input_device_index = 1,
                        input = True, 
                        frames_per_buffer = 1024)

    # Continuously send audio data to Deepgram
    try:
        while True:
            data = stream.read(1024)
            deepgramLive.send(data)
    except KeyboardInterrupt:
        # Stop the loop when Ctrl+C is pressed
        pass
    finally:
        # Stop and close the audio stream
        stream.stop_stream()
        stream.close()
        p.terminate()

    # Indicate that we've finished sending data by sending the customary zero-byte message to the Deepgram streaming endpoint, and wait until we get back the final summary metadata object
    await deepgramLive.finish()

# Run the main function
asyncio.run(main())