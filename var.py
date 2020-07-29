Downloads = '/Users/peter/Downloads/'

Image = Downloads + 'Images'
Video = Downloads + 'Videos'
Audio = Downloads + 'Audios'
Compressed = Downloads + 'Compressed Files'
Adobe = Downloads + 'Adobe'
Microsoft = Downloads + 'Microsoft'
Developer = Downloads + 'Developer'
Others = Downloads + 'Others'

img_paths = []
img_ext = ['.jpeg', '.png', ".jpg", ".gif",
           ".eps", ".bmp", ".tiff", ".tif", ".svg"]

video_paths = []
video_ext = ['.mp4', ".webm",
             ".flv", ".mov", ]

audio_paths = []
audio_ext = ['.aif', '.cda', ".mp3", ".mid",
             ".midi", ".mpa", ".ogg", ".wav", ".wma", ".wpl",
             '.m4a']

compressed_paths = []
compressed_ext = ['.zip', '.7z', '.arj', '.deb',
                  '.pkg', '.rar', '.rpm', '.tar.gz', '.z']

adobe_paths = []
adobe_ext = ['.ai', '.psd', ".indd", ".ps", ".eps", ".prn", '.pdf']

microsoft_paths = []
microsoft_ext = ['.doc', ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".xlsm"]

developer_paths = []
developer_ext = ['.py', ".java", ".cs", ".c", ".html", ".css", ".js", ".htm", ".php",
                 ".dart", ".py", ".scss", ".h", ".sh", ".pl", ".bash", ".cpp", ".class", ".swift", '.json', '.xml', '.sql',
                 '.plist', '.yaml', '.aspx', '.axd', '.asx', '.asmx', '.ashx', '.cfm', '.dws', '.atom', '.action', '.s', '.pod', '.html5', '.e', '.go', '.txt']

other_paths = []
