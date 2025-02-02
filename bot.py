import os
import asyncio
import ffmpeg
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils.executor import start_polling

TOKEN = "YOUR_BOT_TOKEN"  # Replace with your BotFather token
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

UPLOADS_DIR = "downloads/"
OUTPUT_DIR = "outputs/"

# Ensure directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@dp.message_handler(content_types=['video'])
async def process_video(message: types.Message):
    video = message.video

    # Download video
    file_path = await bot.get_file(video.file_id)
    input_path = os.path.join(UPLOADS_DIR, f"{video.file_id}.mp4")
    output_path = os.path.join(OUTPUT_DIR, f"watermarked_{video.file_id}.mp4")

    await message.reply("Downloading video... Please wait.")
    await bot.download_file(file_path.file_path, input_path)

    # Add watermark
    await message.reply("Processing video with watermark...")
    add_watermark(input_path, output_path)

    # Send watermarked video
    await message.reply("Uploading watermarked video...")
    await bot.send_video(message.chat.id, InputFile(output_path))

    # Cleanup
    os.remove(input_path)
    os.remove(output_path)

def add_watermark(input_video, output_video):
    ffmpeg.input(input_video).filter_(
        'drawtext', 
        text='My Watermark', 
        fontcolor='white', 
        fontsize=24, 
        x=10, 
        y=10
    ).output(output_video).run()

if __name__ == "__main__":
    print("Bot is running...")
    start_polling(dp, skip_updates=True)
