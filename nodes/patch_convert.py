import os
def patch_convert_nodes():
    try:
        assets_dir = os.path.join("web", "assets")
        if not os.path.exists(assets_dir):
            return
        
        # Find the correct JS file containing the pattern
        target_file = None
        target_content = None
        
        for file in os.listdir(assets_dir):
            if file.endswith('.js'):
                file_path = os.path.join(assets_dir, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Look for the specific code pattern
                    if 'content: "Convert to nodes",' in content and 'callback: /* @__PURE__ */' in content:
                        target_file = file_path
                        target_content = content
                        break
        
        if target_file and target_content:
            # Split content into lines
            lines = target_content.splitlines()
            
            # Find and comment the block
            for i in range(len(lines)):
                if 'content: "Convert to nodes",' in lines[i]:
                    # Find the complete block
                    block_start = i
                    block_end = i
                    brace_count = 0
                    
                    # Find the complete block by matching braces
                    for j in range(i, len(lines)):
                        line = lines[j].strip()
                        if '{' in line:
                            brace_count += 1
                        if '}' in line:
                            brace_count -= 1
                            if brace_count == 0 and line.endswith(','):
                                block_end = j
                                break
                    
                    # Comment out the entire block
                    for j in range(block_start, block_end + 1):
                        lines[j] = '//' + lines[j]
                    break
            
            # Write back the modified content
            with open(target_file, 'w') as f:
                f.write('\n'.join(lines))
                
    except Exception as e:
        print(f"Failed to patch convert nodes: {str(e)}")
        pass