"""Tools for Confluence spaces operations."""

from typing import Any


def get_spaces(ctx, **arguments) -> dict:
    """
    Retrieve Confluence spaces.

    Args:
        ctx: Application context with Confluence client
        arguments: Arguments from the tool call
            - start: Starting index for pagination (default 0)
            - limit: Maximum number of spaces to return (default 10, max 50)

    Returns:
        Dictionary of spaces
    """
    if not ctx or not ctx.confluence:
        raise ValueError("Confluence is not configured.")

    start = min(int(arguments.get("start", 0)), 1000)
    limit = min(int(arguments.get("limit", 10)), 50)

    return ctx.confluence.get_spaces(start=start, limit=limit)


def get_user_contributed_spaces(ctx, **arguments) -> dict:
    """
    Retrieve Confluence spaces the current user has contributed to.

    Args:
        ctx: Application context with Confluence client
        arguments: Arguments from the tool call
            - limit: Maximum number of results to return (default 250, max 250)

    Returns:
        Dictionary of user-contributed spaces
    """
    if not ctx or not ctx.confluence:
        raise ValueError("Confluence is not configured.")

    limit = min(int(arguments.get("limit", 250)), 250)

    return ctx.confluence.get_user_contributed_spaces(limit=limit)
