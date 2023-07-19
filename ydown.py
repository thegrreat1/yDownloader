
import pytube
import colorama
import sys

red = colorama.Fore.RED
light_green = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN

print(green, '''
 █████ █████     █████                                     ████                         █████                   
░░███ ░░███     ░░███                                     ░░███                        ░░███                    
 ░░███ ███    ███████   ██████  █████ ███ █████ ████████   ░███   ██████   ██████    ███████   ██████  ████████ 
  ░░█████    ███░░███  ███░░███░░███ ░███░░███ ░░███░░███  ░███  ███░░███ ░░░░░███  ███░░███  ███░░███░░███░░███
   ░░███    ░███ ░███ ░███ ░███ ░███ ░███ ░███  ░███ ░███  ░███ ░███ ░███  ███████ ░███ ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███ ░███ ░░███████████   ░███ ░███  ░███ ░███ ░███ ███░░███ ░███ ░███ ░███░░░   ░███     
    █████   ░░████████░░██████   ░░████░████    ████ █████ █████░░██████ ░░████████░░████████░░██████  █████    
   ░░░░░     ░░░░░░░░  ░░░░░░     ░░░░ ░░░░    ░░░░ ░░░░░ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░     
   
        ''')

try:
    if len(sys.argv) > 1:
        url = str(sys.argv[1])
        outpath = str(sys.argv[2])
    else:
        print(red, "Usage:", light_green, "python ydown.py URL DownloadPath")
        print(red, "Example:", light_green, "python ydown.py \"https://www.youtube.com/watch?v"
                                                                  "=dQw4w9WgXcQ&ab_channel=RickAstley\" "
              "\"/root/Downloads/\"")
    if "youtube." in url:
        try:
            pytube.YouTube(url).streams.get_highest_resolution().download(str(outpath))
            print(light_green, "Obtained video:", 'Name: ', str(pytube.YouTube(url).title.format()))
            print(light_green, "Downloaded:", "\"", str(pytube.YouTube(url).title), ".mp4\"", " To ", str(outpath))
        except Exception as error:
            print(red, "An error occurred: ", green, type(error).__name__, "–", error)

    else:
        print(red, "Error: " + green, "URL has to be a valid youtube url")

except:
    sys.exit(1)
