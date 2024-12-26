from .enhanced_save import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Silently patch on module import
try:
    import os
    js_paths = [
        os.path.join("web", "extensions", "core", "index.js"),
        os.path.join("web", "assets", "index-p6KSJ2Zq.js")
    ]
    
    for js_file in js_paths:
        if os.path.exists(js_file):
            with open(js_file, 'r') as f:
                lines = f.readlines()
            
            # Find and remove the block
            for i in range(len(lines)):
                if 'content: "Convert to nodes",' in lines[i]:
                    del lines[i:i+7]  # Delete exactly 7 lines
                    break
            
            # Write back the file without those lines
            with open(js_file, 'w') as f:
                f.writelines(lines)
except:
    pass

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']