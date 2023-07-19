import pytube
import colorama
import sys

print(colorama.Fore.GREEN, '''
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
        print(colorama.Fore.RED, "Usage:", colorama.Fore.GREEN, "python ydown.py URL DownloadPath")
        print(colorama.Fore.RED, "Example:", colorama.Fore.GREEN, "python ydown.py \"https://www.youtube.com/watch?v"
                                                                  "=dQw4w9WgXcQ&ab_channel=RickAstley\""
              "\"/root/Downloads/\"")
    if "youtube." in url:
        try:
            pytube.YouTube(url).streams.get_highest_resolution().download(str(outpath))
            print(colorama.Fore.RED, "Obtained video:", colorama.Fore.GREEN, 'Name: ',
                  str(pytube.YouTube(url).title.format()))
            print(colorama.Fore.RED, "Downloaded:", colorama.Fore.GREEN, str(pytube.YouTube(url).title), " To ",
                  str(outpath))
        except Exception as error:
            print(colorama.Fore.RED, "An error occurred: ", colorama.Fore.GREEN, type(error).__name__, "–", error)

    else:
        print(colorama.Fore.RED, "Error: " + colorama.Fore.GREEN, "URL has to be a valid youtube url")

except:
    sys.exit(1)
