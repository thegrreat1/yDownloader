# yDownloader Youtube video downloader
![ocMLSGU](https://github.com/thegrreat1/yDownloader/assets/63957530/1c671468-40cc-4b7b-a4e9-3837c1c903e6)

Very simple python script using pytube module to download youtube videos using terminal.<br>
- Required python modules can be installed by running  <code> pip install -r requirements.txt </code>
- Tested on Linux kali 6.1.0-kali9-arm64 #1 SMP Debian 6.1.27-1kali1 (2023-05-12) aarch64 GNU/Linux
  
# IMPORTANT
- *REQUIRED* cipher.py in /usr/local/lib/python'your version'/dist-packages/pytube/ has to be replaced with the one from this git<br>
"Quick fix until pytube updates their module to fix RegexMatchError: get_transform_object: could not find match for var for={(.*?)};"<br>

To find where pytube is installed on your machine, if running linux you can run <code>updatedb</code> in terminal. <br>
After that run <code>locate pytube/cipher.py</code> in terminal and replace cipher.py with the new cipher.py<br>


