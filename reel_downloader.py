#!/usr/bin/env python3
"""
Reel Downloader
A script to download reels (MP4 video + description) using yt-dlp

Required dependencies:
pip install yt-dlp

Author: Assistant
Purpose: Help download reels for reposting on other platforms
"""

import os
import re
import sys
import json
from pathlib import Path
import yt_dlp
from urllib.parse import urlparse

def sanitize_filename(filename):
    """
    Remove or replace invalid characters from filename to make it filesystem-safe
    """
    # Remove or replace invalid characters
    invalid_chars = r'[<>:"/\\|?*]'
    filename = re.sub(invalid_chars, '_', filename)
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    
    # Limit length to avoid filesystem issues
    if len(filename) > 200:
        filename = filename[:200]
    
    return filename

def extract_reel_info(url):
    """
    Extract reel information including title and description using yt-dlp
    Returns: dict with video info or None if failed
    """
    ydl_opts = {
        'quiet': True,  # Suppress yt-dlp output
        'no_warnings': True,
        'extract_flat': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("🔍 Extracting reel information...")
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        print(f"❌ Error extracting reel info: {str(e)}")
        return None

def download_reel(url, output_dir="downloads"):
    """
    Download reel video and save description
    
    Args:
        url (str): reel URL
        output_dir (str): Directory to save files
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    # First, extract reel information
    reel_info = extract_reel_info(url)
    if not reel_info:
        return False
    
    # Generate filename from title or fallback to ID
    title = reel_info.get('title', 'instagram_reel')
    reel_id = reel_info.get('id', 'unknown')
    
    # Create a safe filename
    if title and title != 'instagram_reel':
        base_filename = sanitize_filename(title)
    else:
        base_filename = f"reel_{reel_id}"
    
    # Ensure filename is not empty
    if not base_filename:
        base_filename = f"reel_{reel_id}"
    
    video_filename = os.path.join(output_dir, f"{base_filename}.mp4")
    description_filename = os.path.join(output_dir, f"{base_filename}_description.txt")
    
    # Configure yt-dlp options for download
    ydl_opts = {
        'format': 'mp4/best[ext=mp4]',  # Prefer mp4 format
        'outtmpl': video_filename,
        'quiet': False,
    }
    
    try:
        # Download the video
        print("⬇️  Downloading reel video...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"✅ Video saved as: {video_filename}")
        
        # Save description/caption
        description = reel_info.get('description', '').strip()
        
        print("💾 Saving description...")
        with open(description_filename, 'w', encoding='utf-8') as f:
            if description:
                f.write(f"Reel Description:\n")
                f.write(f"URL: {url}\n")
                f.write(f"Title: {reel_info.get('title', 'N/A')}\n")
                f.write(f"Uploader: {reel_info.get('uploader', 'N/A')}\n")
                f.write(f"Duration: {reel_info.get('duration', 'N/A')} seconds\n")
                f.write(f"View Count: {reel_info.get('view_count', 'N/A')}\n")
                f.write(f"\nDescription/Caption:\n{description}")
            else:
                f.write("No description available for this reel.")
        
        print(f"✅ Description saved as: {description_filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading reel: {str(e)}")
        return False

def validate_instagram_url(url):
    """
    Validate if the provided URL is a valid reel URL
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid reel URL, False otherwise
    """
    instagram_patterns = [
        r'https?://(www\.)?instagram\.com/reel/[A-Za-z0-9_-]+/?',
        r'https?://(www\.)?instagram\.com/p/[A-Za-z0-9_-]+/?',  # Also support posts
        r'https?://instagram\.com/reel/[A-Za-z0-9_-]+/?',
        r'https?://instagram\.com/p/[A-Za-z0-9_-]+/?'
    ]
    
    for pattern in instagram_patterns:
        if re.match(pattern, url):
            return True
    return False

def main():
    """
    Main function to handle user input and coordinate the download process
    """
    print("🎬 Reel Downloader")
    print("=" * 40)
    print("This tool will download reels as MP4 files along with their descriptions.")
    print("Perfect for reposting content on other platforms like YouTube!")
    print()
    
    # Check if yt-dlp is installed
    try:
        import yt_dlp
    except ImportError:
        print("❌ Error: yt-dlp is not installed.")
        print("Please install it using: pip install yt-dlp")
        sys.exit(1)
    
    while True:
        # Get reel URL from user
        url = input("📎 Enter reel URL (or 'quit' to exit): ").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not url:
            print("❌ Please enter a valid URL.")
            continue
        
        # Validate URL format
        if not validate_instagram_url(url):
            print("❌ Invalid URL format.")
            print("Please use a URL like: https://www.instagram.com/reel/ABC123/")
            continue
        
        print(f"\n🎯 Processing: {url}")
        
        # Ask for output directory (optional)
        output_dir = input("📁 Enter output directory (press Enter for 'downloads'): ").strip()
        if not output_dir:
            output_dir = "downloads"
        
        # Download the reel
        success = download_reel(url, output_dir)
        
        if success:
            print("\n🎉 Download completed successfully!")
        else:
            print("\n❌ Download failed. Please check the URL and try again.")
        
        print("\n" + "="*50 + "\n")
        
        # Ask if user wants to download another reel
        another = input("📥 Download another reel? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            print("👋 Thanks for using Reel Downloader!")
            break

if __name__ == "__main__":
    main()
