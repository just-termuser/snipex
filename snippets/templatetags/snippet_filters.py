from django import template

register = template.Library()

# Maps Language.name values to highlight.js language identifiers
_HLJS_MAP = {
    'python': 'python',
    'javascript': 'javascript',
    'typescript': 'typescript',
    'html5': 'html',
    'html': 'html',
    'css3': 'css',
    'css': 'css',
    'sql': 'sql',
    'bash / shell': 'bash',
    'bash': 'bash',
    'shell': 'bash',
    'c++': 'cpp',
    'с#': 'csharp',   # Cyrillic С as stored in DB
    'c#': 'csharp',
    'java': 'java',
    'go (golang)': 'go',
    'go': 'go',
    'rust': 'rust',
    'php': 'php',
    'ruby': 'ruby',
    'swift': 'swift',
    'kotlin': 'kotlin',
    'markdown': 'markdown',
    'json': 'json',
    'yaml': 'yaml',
    'xml': 'xml',
}


@register.filter
def hljs_lang(language):
    name = str(language).lower().strip() if language else ''
    return _HLJS_MAP.get(name, name)
