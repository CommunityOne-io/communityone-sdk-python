# CommunityOne SDK

[![PyPI version](https://img.shields.io/pypi/v/communityone.svg)](https://pypi.org/project/communityone/)
[![Python versions](https://img.shields.io/pypi/pyversions/communityone.svg)](https://pypi.org/project/communityone/)

Official Python SDK for interacting with the [CommunityOne](https://communityone.io) API. This SDK provides both synchronous and asynchronous methods to interact with CommunityOne's API endpoints.

## About CommunityOne

[CommunityOne](https://communityone.io) is a platform that helps Discord communities grow and engage their members through quests, rewards, and gamification.

## Installation

You can install the package using pip:

```bash
pip install communityone
```

## Quick Start

```python
from communityone import CommunityOneSDK

# Initialize the SDK with your server ID and API key
sdk = CommunityOneSDK(server_id=YOUR_SERVER_ID, api_key="YOUR_API_KEY")

# Get all custom quests
custom_quests = sdk.get_custom_quests()

# Get player information
player_info = sdk.get_player_info(discord_user_id="DISCORD_USER_ID")

# Complete a custom quest
result = sdk.complete_custom_quest(custom_quest_id="CUSTOM_QUEST_ID", discord_user_id="DISCORD_USER_ID")

# Get completed members for a quest
completed_members = sdk.get_completed_members(custom_quest_id="CUSTOM_QUEST_ID")
```

## Async Support

The SDK also provides async methods for all operations:

```python
import asyncio
from communityone import CommunityOneSDK

async def main():
    sdk = CommunityOneSDK(server_id=YOUR_SERVER_ID, api_key="YOUR_API_KEY")
    
    # Get custom quests asynchronously
    custom_quests = await sdk.get_custom_quests_async()
    
    # Get player information asynchronously
    player_info = await sdk.get_player_info_async("DISCORD_USER_ID")
    
    # Complete a custom quest asynchronously
    result = await sdk.complete_custom_quest_async(custom_quest_id="CUSTOM_QUEST_ID", discord_user_id="DISCORD_USER_ID")
    
    # Get completed members asynchronously
    completed_members = await sdk.get_completed_members_async(custom_quest_id="CUSTOM_QUEST_ID")

# Run the async code
asyncio.run(main())
```

## Available Methods

### Synchronous Methods
- `get_custom_quests()`: Get all custom quests for the server
- `get_player_info(discord_user_id)`: Get information about a player
- `complete_custom_quest(custom_quest_id, discord_user_id)`: Mark a custom quest as completed
- `get_completed_members(custom_quest_id)`: Get all members who completed a quest

### Asynchronous Methods
- `get_custom_quests_async()`: Get all custom quests for the server asynchronously
- `get_player_info_async(discord_user_id)`: Get player information asynchronously
- `complete_custom_quest_async(custom_quest_id, discord_user_id)`: Complete a quest asynchronously
- `get_completed_members_async(custom_quest_id)`: Get completed members asynchronously

## Testing Mode

CommunityOne allows you to test the full quest completion workflow in your application without affecting production quests data, helping you verify quest functionality before releasing it to your community. When a quest is in testing mode:
- The quest won't be visible to regular Discord server members
- No code changes needed! - use the same SDK methods for testing and production quests (the API automatically routes to our internal test environment)

**How to enable:**
1. Go to your server's [CommunityOne dashboard](https://communityone.io/dashboard)
2. Navigate to Hype Engine > Custom Quests
3. Click the Edit button on your quest
4. Enable testing mode

## Rate Limiting

All API endpoints are subject to rate limiting:
- 60 requests per minute per server
- Rate limits are applied separately for each endpoint
- Exceeding the rate limit will result in a 429 Too Many Requests response

## Requirements

- Python 3.7 or higher
- requests>=2.25.0
- aiohttp>=3.8.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
