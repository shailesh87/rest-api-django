from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from pydub import AudioSegment
import json
from rest_framework import status

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
    
class AudioSnippetAPIView(APIView):
    parser_classes = [MultiPartParser, JSONParser]

    def post(self, request, *args, **kwargs):
        try:
            # Retrieve audio file and JSON data from the request
            audio_file = request.FILES.get('audio_file')
            timestamps = json.loads(request.data.get('timestamps'))

            # Load audio using pydub
            audio = AudioSegment.from_file(audio_file)

            # Process timestamps to split audio
            for i, segment in enumerate(timestamps):
                start = segment['start'] * 1000  # Convert seconds to milliseconds
                end = segment['end'] * 1000
                split_audio = audio[start:end]

                # Export split audio as a new file
                split_audio.export(f"split_audio_{i}.mp3", format="mp3")

            return Response(
                {"message": "Audio snippets created successfully!"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )