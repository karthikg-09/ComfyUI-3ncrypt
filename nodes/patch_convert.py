import os
def patch_convert_nodes():
    try:
        js_paths = [
            os.path.join("web", "extensions", "core", "index.js"),
            os.path.join("web", "assets", "index-p6KSJ2Zq.js")
        ]
        
        for js_file in js_paths:
            if os.path.exists(js_file):
                with open(js_file, 'r') as f:
                    lines = f.readlines()
                
                # Find and comment the block
                for i in range(len(lines)):
                    if 'content: "Convert to nodes",' in lines[i]:
                        # Comment out next 7 lines
                        for j in range(i, i+7):
                            if j < len(lines):
                                lines[j] = '//' + lines[j]
                        break
                
                # Write back the file
                with open(js_file, 'w') as f:
                    f.writelines(lines)
    except:
        pass