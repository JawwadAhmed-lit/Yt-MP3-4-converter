
# 🎥🎵 YouTube Video Downloader

This Python script allows users to download YouTube videos either as MP4 files or extract audio as MP3 files. It utilizes the `yt_dlp` library for downloading videos and `moviepy` for extracting audio from video files. The graphical user interface (GUI) is built using `customtkinter` for a user-friendly experience.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


   
🔧 **Prerequisites:**


Before running the script, ensure you have the following dependencies installed:

-  Clone this repository.
After cloning the repository you can head to [`Info on Virtual Environment`](https://github.com/JawwadAhmed-lit/Yt-MP3-4-converter/blob/master/README.md#info-on-virtual-environment) section , if you want packages to download only in this folder and not the whole system . 

- Python 3.x
- use the following command to install the required libraries
```pip install -r requirements.txt```

## Info on Virtual Environment
Python's official documentation says:

_"A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system"_

What ever packages you download in your virtual environment, it will be specific to that project only and not downloaded globally, in this way  it will not interfere with your system files. 

**To Install:** Use following commands:

1.  `pip install virtualenv` in your terminal
2. To use venv in your project folder, in your terminal run `python<version> -m venv <virtual-environment-name>`
   for e.g : ` python3.8 -m venv env`
3. Now just activate the virtual environment by using : `source env/bin/activate`.
   This will activate your virtual environment. Immediately, you will notice that your terminal path includes env, signifying an activated virtual environment.
4. Now you can install the required pacakges using ```pip install -r requirements.txt```.

   

## Usage

1. Run the script using Python:
``python app.py``

2. Once the GUI window opens, you can either enter a YouTube link manually or choose to download from a CSV file containing a list of links.

3. Choose the desired format (MP4 or MP3) from the dropdown menu.

4. Click the "Download" button to start the download process.

🚀 **Key Features:**

- Download videos from YouTube either by entering a single link or from a CSV file.
- Choose between downloading videos as MP4 files or extracting audio as MP3 files.
- Progress bar to track download progress.
- Error handling for various exceptions during the download process.

## Important Notes

- Ensure you have a stable internet connection for downloading videos.
- Respect YouTube's terms of service and copyright policies when downloading content.
- Make sure to have sufficient storage space for downloaded files.
- There will be seperate folders for made mp3 and mp4 files in the same directory where the script is located.

Start converting your favorite YouTube content into your preferred format today!
## Author

- Jawwad Ahmed

## License

This project is licensed under the [MIT License](https://github.com/JawwadAhmed-lit/Yt-MP3-4-converter?tab=MIT-1-ov-file#readme).

