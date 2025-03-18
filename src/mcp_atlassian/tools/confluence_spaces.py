"""Tools for Confluence spaces operations."""

from typing import Dict, Any, Optional

from ..confluence.client import ConfluenceClient
from ..confluence.config import ConfluenceConfig


def get_spaces(
    base_url: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    start: int = 0,
    limit: int = 10
) -> Dict[str, Any]:
    """
    Tool to retrieve Confluence spaces.

    Args:
        base_url: Confluence base URL (optional, can use config)
        username: Confluence username (optional, can use config)
        password: Confluence password (optional, can use config)
        start: Starting index for pagination
        limit: Maximum number of spaces to return

    Returns:
        Dictionary of spaces
    """
    # Use config if not explicitly provided
    config = ConfluenceConfig()
    
    base_url = base_url or config.base_url
    username = username or config.username
    password = password or config.password

    if not all([base_url, username, password]):
        raise ValueError("Missing Confluence connection details. Please provide or set in config.")

    client = ConfluenceClient(base_url, username, password)
    return client.get_spaces(start=start, limit=limit)


def get_user_contributed_spaces(
    base_url: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    limit: int = 250
) -> Dict[str, Any]:
    """
    Tool to retrieve Confluence spaces the current user has contributed to.

    Args:
        base_url: Confluence base URL (optional, can use config)
        username: Confluence username (optional, can use config)
        password: Confluence password (optional, can use config)
        limit: Maximum number of results to return

    Returns:
        Dictionary of user-contributed spaces
    """
    # Use config if not explicitly provided
    config = ConfluenceConfig()
    
    base_url = base_url or config.base_url
    username = username or config.username
    password = password or config.password

    if not all([base_url, username, password]):
        raise ValueError("Missing Confluence connection details. Please provide or set in config.")

    client = ConfluenceClient(base_url, username, password)
    return client.get_user_contributed_spaces(limit=limit)
