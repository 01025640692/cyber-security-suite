malakshokry73@penguin:~/cyber-security-suite$ import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_image_metadata(image_path):
    """
    أداة احترافية لاستخراج البيانات المخفية والسرية من الصور (EXIF Data)
    """
    try:
        if not os.path.exists(image_path):
            return "[-] Error: Image file not found!"
            
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if not exif_data:
            return "[!] No hidden metadata (EXIF) found in this image."
            
        parsed_metadata = ""
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            parsed_metadata += f"{tag_name}: {value}\n"
            
        return parsed_metadata
        
    except Exception as e:
        return f"[-] Error analyzing image: {str(e)}"
-bash: import: command not found
-bash: from: command not found
-bash: from: command not found
-bash: syntax error near unexpected token `('
-bash: $'\n    أداة احترافية لاستخراج البيانات المخفية والسرية من الصور (EXIF Data)\n    ': command not found
-bash: try:: command not found
-bash: syntax error near unexpected token `('
-bash: return: [-] Error: Image file not found!: numeric argument required
-bash: return: can only `return' from a function or sourced script
-bash: syntax error near unexpected token `('
-bash: syntax error near unexpected token `('
-bash: syntax error near unexpected token `value'
-bash: syntax error near unexpected token `('
-bash: parsed_metadata: command not found
-bash: return: parsed_metadata: numeric argument required
-bash: return: can only `return' from a function or sourced script
-bash: except: command not found
-bash: return: f[-] Error analyzing image: {str(e)}: numeric argument required
-bash: return: can only `return' from a function or sourced script
malakshokry73@penguin:~/cyber-security-suite$ 
