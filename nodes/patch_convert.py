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
                    if 'content: "Convert to nodes",' in content:
                        target_file = file_path
                        target_content = content
                        break
        
        if target_file and target_content:
            # Split content into lines
            lines = target_content.splitlines()
            
            # Find the block
            for i in range(len(lines)):
                if 'content: "Convert to nodes",' in lines[i]:
                    # Get the block content
                    block_content = '\n'.join(lines[i:i+7])
                    # Create commented version
                    commented_block = '\n'.join('//' + line for line in lines[i:i+7])
                    # Replace only this specific block
                    new_content = target_content.replace(block_content, commented_block)
                    
                    # Write back the modified content
                    with open(target_file, 'w') as f:
                        f.write(new_content)
                    break
                    
    except Exception as e:
        print(f"Failed to patch convert nodes: {str(e)}")
        pass