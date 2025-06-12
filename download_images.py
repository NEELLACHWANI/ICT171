import os
import requests
from pathlib import Path

# Create images directory if it doesn't exist
images_dir = Path("assets/images")
images_dir.mkdir(parents=True, exist_ok=True)

# Image URLs and their corresponding filenames
images = {
    "tech_trends_2025.jpg": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop",
    "digital_marketing_2025.jpg": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2015&auto=format&fit=crop",
    "ai_impact_2025.jpg": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=2032&auto=format&fit=crop",
    "remote_work_2025.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop",
    "sustainability_2025.jpg": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?q=80&w=2041&auto=format&fit=crop",
    "cybersecurity_2025.jpg": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop",
    "blockchain_2025.jpg": "https://images.unsplash.com/photo-1639762681057-408e52192e55?q=80&w=2022&auto=format&fit=crop",
    "healthcare_tech_2025.jpg": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=2070&auto=format&fit=crop",
    "future_education_2025.jpg": "https://images.unsplash.com/photo-1501504905252-473c47e087f8?q=80&w=1974&auto=format&fit=crop",
    "smart_cities_2025.jpg": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2044&auto=format&fit=crop"
}

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        filepath = images_dir / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

def main():
    print("Starting image downloads...")
    for filename, url in images.items():
        download_image(url, filename)
    print("Download process completed!")

if __name__ == "__main__":
    main() 