"""Tools package for MCP Atlassian."""

from .confluence_spaces import get_spaces, get_user_contributed_spaces

__all__ = [
    'get_spaces',
    'get_user_contributed_spaces'
]
