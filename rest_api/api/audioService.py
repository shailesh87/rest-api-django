from pydub import AudioSegment
import json
import os


class AudioService:
    @staticmethod
    def process_audio(audio_file, timestamps, output_directory="output"):
        """
        Splits audio based on the given timestamps and saves the segments.

        :param audio_file: Uploaded audio file.
        :param timestamps: JSON list of start and end times.
        :param output_directory: Directory to save split audio files.
        :return: List of saved file paths.
        """
        try:
            # Load audio
            audio = AudioSegment.from_file(audio_file)

            # Ensure output directory exists
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Process timestamps and save audio segments
            saved_files = []
            for i, segment in enumerate(timestamps):
                start = segment['start'] * 1000  # Convert to milliseconds
                end = segment['end'] * 1000
                split_audio = audio[start:end]

                output_file = os.path.join(output_directory, f"split_audio_{i}.mp3")
                split_audio.export(output_file, format="mp3")
                saved_files.append(output_file)

            return saved_files

        except Exception as e:
            raise ValueError(f"Error processing audio: {str(e)}")
