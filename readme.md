# 📱 Reel Downloader

A powerful Python script to download reels as MP4 videos along with their descriptions/captions. Perfect for content creators who want to repost their content on other platforms like YouTube, TikTok, or for personal backup purposes.

## ✨ Features

- 🎬 **High-Quality Downloads** - Downloads reels in the best available MP4 format
- 📝 **Caption Extraction** - Saves descriptions, metadata, and captions as text files
- 🛡️ **Smart Error Handling** - Robust error handling for network issues and invalid URLs
- 📁 **Organized Output** - Creates clean, filesystem-safe filenames
- 🔄 **Batch Processing** - Process multiple reels in one session
- 📊 **Metadata Preservation** - Saves uploader info, duration, view count, and more
- 🚀 **Fast & Reliable** - Uses yt-dlp for stable downloads

## 🎯 Use Cases

- **Content Creators**: Repost your reels on YouTube/TikTok
- **Social Media Managers**: Backup client content across platforms
- **Personal Archiving**: Save your favorite reels for offline viewing
- **Content Research**: Download reels for analysis and inspiration

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step 1: Install Dependencies
```bash
pip install yt-dlp
```

### Step 2: Download the Script
```bash
# Option 1: Clone repository (if available)
https://github.com/monis-codes/Reel-Download-Script.git
cd Content-Download-Script


### Step 3: Make Script Executable (Optional)
```bash
chmod +x reel_downloader.py
```

## 🎮 Usage

### Basic Usage
```bash
python reel_downloader.py
```

### Interactive Mode
1. **Run the script**
2. **Enter reel URL** when prompted
3. **Choose output directory** (or press Enter for default 'downloads' folder)
4. **Wait for download** to complete
5. **Repeat** for more reels or type 'quit' to exit

### Example Session
```
🎬 Reel Downloader
========================================
This tool will download reels as MP4 files along with their descriptions.
Perfect for reposting content on other platforms like YouTube!

📎 Enter reel URL (or 'quit' to exit): https://www.instagram.com/reel/ABC123xyz/

🎯 Processing: https://www.instagram.com/reel/ABC123xyz/
📁 Enter output directory (press Enter for 'downloads'): 

🔍 Extracting reel information...
⬇️  Downloading reel video...
✅ Video saved as: downloads/amazing_dance_reel.mp4
💾 Saving description...
✅ Description saved as: downloads/amazing_dance_reel_description.txt

🎉 Download completed successfully!

==================================================

📥 Download another reel? (y/n): n
👋 Thanks for using Reel Downloader!
```

## 📁 Output Files

For each downloaded reel, you'll get:

### Video File
- **Format**: MP4 (best available quality)
- **Naming**: Based on reel title or ID
- **Location**: Specified output directory

### Description File
- **Format**: Plain text (.txt)
- **Content**: Complete metadata including:
  - Original URL
  - Reel title
  - Uploader username
  - Duration
  - View count
  - Full caption/description

### Example Output
```
downloads/
├── my_viral_dance.mp4
├── my_viral_dance_description.txt
├── cooking_tutorial_reel.mp4
├── cooking_tutorial_reel_description.txt
└── ...
```

## 🔗 Supported URL Formats

The script supports various URL formats:

- `https://www.instagram.com/reel/ABC123/`
- `https://instagram.com/reel/ABC123/`
- `https://www.instagram.com/p/ABC123/` (regular posts)
- `https://instagram.com/p/ABC123/`

## ⚙️ Configuration

### Custom Output Directory
```python
# When prompted, enter your preferred directory
📁 Enter output directory (press Enter for 'downloads'): /path/to/my/folder
```

### Filename Handling
The script automatically:
- Sanitizes filenames (removes invalid characters)
- Limits filename length (200 characters max)
- Handles duplicate names
- Falls back to reel ID if title unavailable

## 🛠️ Advanced Usage

### Programmatic Usage
You can import and use the functions in your own Python scripts:

```python
from reel_downloader import download_reel, validate_instagram_url

# Download a single reel
url = "https://www.instagram.com/reel/ABC123/"
success = download_reel(url, output_dir="my_downloads")

# Validate URL before downloading
if validate_instagram_url(url):
    print("Valid URL")
```

### Batch Processing
Create a text file with URLs and modify the script to read from it:

```python
# Example: batch_download.py
urls = [
    "https://www.instagram.com/reel/ABC123/",
    "https://www.instagram.com/reel/DEF456/",
    # ... more URLs
]

for url in urls:
    download_reel(url, "batch_downloads")
```

## 🚨 Troubleshooting

### Common Issues

#### 1. "yt-dlp not installed" Error
```bash
pip install yt-dlp
# or
pip3 install yt-dlp
```

#### 2. "Invalid URL" Error
- Ensure URL starts with `https://`
- Check that URL contains `/reel/` or `/p/`
- Verify the reel/post ID is present

#### 3. Download Failures
- **Private Account**: Script cannot access private reels
- **Deleted Content**: Reel may have been removed
- **Network Issues**: Check internet connection
- **Rate Limiting**: Wait a few minutes between downloads


### Error Messages Guide

| Error | Cause | Solution |
|-------|-------|----------|
| `Error extracting reel info` | Invalid/private reel | Check URL, ensure reel is public |
| `Error downloading reel` | Network/permission issue | Check connection and folder permissions |
| `Invalid URL format` | Malformed URL | Use correct URL format |

## 📋 Requirements

### System Requirements
- **Operating System**: Windows, macOS, Linux
- **Python**: Version 3.6+
- **Internet**: Stable connection for downloads
- **Storage**: Sufficient space for video files

### Python Dependencies
```txt
yt-dlp>=2023.1.6
```

Install with:
```bash
pip install -r requirements.txt
```

## 🔒 Legal & Ethical Considerations

### Important Notice
- ✅ **Use for your own content**: Download your own reels for cross-platform posting
- ✅ **Respect copyright**: Only download content you have rights to use
- ✅ **Follow platform terms**: Comply with Instagram's Terms of Service
- ❌ **Don't redistribute**: Avoid sharing downloaded content without permission

### Best Practices
1. **Get Permission**: Ask creators before downloading their content
2. **Credit Sources**: Always credit original creators when reposting
3. **Respect Privacy**: Don't download private or sensitive content
4. **Fair Use**: Understand copyright and fair use guidelines

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues
1. Check existing issues first
2. Provide detailed error messages
3. Include system information (OS, Python version)
4. Share example URLs that fail (if public)

### Suggesting Features
- Bulk download from file
- GUI interface
- Additional metadata extraction
- Support for other platforms

### Code Contributions
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **yt-dlp**: Powerful media downloader that makes this tool possible
- **Instagram**: For providing a platform for creative content
- **Python Community**: For excellent libraries and documentation

## 🔄 Changelog

### Version 1.0.0
- Initial release
- Basic reel downloading functionality
- Description extraction
- Interactive command-line interface
- Error handling and validation

---

**⚠️ Disclaimer**: This tool is for educational and personal use only. Users are responsible for complying with Instagram's Terms of Service and applicable copyright laws.
