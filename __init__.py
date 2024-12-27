from .nodes.saveimageplus import NODE_CLASS_MAPPINGS as SAVE_NODE_MAPPINGS
from .nodes.markdown_editor import NODE_CLASS_MAPPINGS as MARKDOWN_NODE_MAPPINGS
from .nodes.patch_convert import patch_convert_nodes

# Merge all node mappings
NODE_CLASS_MAPPINGS = {
    **SAVE_NODE_MAPPINGS,
    **MARKDOWN_NODE_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Enhanced Save Image": "Save Image+",
    "Markdown Editor": "Markdown Editor"
}

# Apply patches
patch_convert_nodes()

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']