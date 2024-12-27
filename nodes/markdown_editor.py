class MarkdownEditor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, 
                    "default": "# Title\nYour markdown text here", 
                    "dynamicPrompts": False,
                    "markdown": True,
                    "tooltip": "Enter markdown text. Supports standard markdown syntax."
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("markdown_text",)
    FUNCTION = "process"
    CATEGORY = "utils"
    OUTPUT_NODE = True
    DESCRIPTION = "A node for editing and storing markdown formatted text."

    def process(self, text):
        # Return the markdown text as-is for other nodes to use
        return (text,)

NODE_CLASS_MAPPINGS = {
    "Markdown Editor": MarkdownEditor
}