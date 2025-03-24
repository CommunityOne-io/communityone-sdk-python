import requests
import aiohttp
from typing import List, Dict, Any

__version__ = "1.1.0"

class CommunityOneSDK:
    """
    This SDK provides methods to interact with CommunityOne's API endpoints,
    offering both synchronous and asynchronous implementations for each endpoint.

    Methods:
        Synchronous Methods:
        - get_custom_quests(): Get all custom quests for the server
        - get_player_info(discord_user_id): Get information about a player
        - complete_custom_quest(custom_quest_id, discord_user_id): Mark a custom quest as completed
        - get_completed_members(custom_quest_id): Get all members who completed a quest

        Asynchronous Methods:
        - get_custom_quests_async(): Get all custom quests for the server asynchronously
        - get_player_info_async(discord_user_id): Get player information asynchronously
        - complete_custom_quest_async(custom_quest_id, discord_user_id): Complete a quest asynchronously
        - get_completed_members_async(custom_quest_id): Get completed members asynchronously
    """

    BASE_URL = "https://api.communityone.io/v1"

    def __init__(self, server_id: int, api_key: str):
        """
        Initialize the CommunityOne SDK.

        Args:
            server_id (int): The Discord server ID
            api_key (str): The API key for authentication
        """
        self.server_id = server_id
        self.api_key = api_key
        self.headers = {"Authorization": api_key}

    def _format_url(self, endpoint: str) -> str:
        """
        Format the complete URL for an API endpoint.

        Args:
            endpoint (str): The API endpoint path

        Returns:
            str: The complete URL
        """
        return f"{self.BASE_URL}{endpoint}"

    def _handle_response(self, response: requests.Response) -> Any:
        """
        Handle the API response, raising exceptions for error status codes.

        Args:
            response (requests.Response): The API response

        Returns:
            Any: The parsed JSON response

        Raises:
            HTTPError: If the request fails
        """
        response.raise_for_status()
        return response.json()

    async def _handle_async_response(self, response: aiohttp.ClientResponse) -> Any:
        """
        Handle the asynchronous API response, raising exceptions for error status codes.

        Args:
            response (aiohttp.ClientResponse): The API response

        Returns:
            Any: The parsed JSON response

        Raises:
            ClientResponseError: If the request fails
        """
        if not response.ok:
            response.raise_for_status()
        return await response.json()

    # Get custom quests endpoints
    def get_custom_quests(self) -> List[Dict[str, Any]]:
        """
        Get all custom quests for the server.

        Returns:
            List[Dict[str, Any]]: A list of custom quests, each containing:
                - custom_quest_id (int): The ID of the custom quest
                - title (str): The title of the quest
                - description (str): The description of the quest
                - external_url (str, optional): The external URL for the quest
                - reward_points (int): The points rewarded for completing the quest
                - reward_role_id (str, optional): The role ID rewarded for completing the quest
                - archived (bool): Whether the quest is archived

        Raises:
            requests.HTTPError: If the request fails
        """
        url = self._format_url(f"/servers/{self.server_id}/custom-quests")
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    async def get_custom_quests_async(self) -> List[Dict[str, Any]]:
        """
        Get all custom quests for the server asynchronously.

        Returns:
            List[Dict[str, Any]]: A list of custom quests, each containing:
                - custom_quest_id (int): The ID of the custom quest
                - title (str): The title of the quest
                - description (str): The description of the quest
                - external_url (str, optional): The external URL for the quest
                - reward_points (int): The points rewarded for completing the quest
                - reward_role_id (str, optional): The role ID rewarded for completing the quest
                - archived (bool): Whether the quest is archived

        Raises:
            aiohttp.ClientResponseError: If the request fails
        """
        url = self._format_url(f"/servers/{self.server_id}/custom-quests")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await self._handle_async_response(response)

    # Get player info endpoints
    def get_player_info(self, discord_user_id: str) -> Dict[str, Any]:
        """
        Get information about a player.

        Args:
            discord_user_id (str): The Discord user ID of the player

        Returns:
            Dict[str, Any]: Player information containing:
                - discord_user_id (str): The Discord user ID
                - discord_username (str): The Discord username
                - discord_display_name (str): The Discord display name
                - discord_avatar (str, optional): The Discord avatar URL

        Raises:
            requests.HTTPError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/players/{discord_user_id}/info"
        )
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    async def get_player_info_async(self, discord_user_id: str) -> Dict[str, Any]:
        """
        Get information about a player asynchronously.

        Args:
            discord_user_id (str): The Discord user ID of the player

        Returns:
            Dict[str, Any]: Player information containing:
                - discord_user_id (str): The Discord user ID
                - discord_username (str): The Discord username
                - discord_display_name (str): The Discord display name
                - discord_avatar (str, optional): The Discord avatar URL

        Raises:
            aiohttp.ClientResponseError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/players/{discord_user_id}/info"
        )
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await self._handle_async_response(response)

    # Complete custom quest endpoints
    def complete_custom_quest(self, custom_quest_id: int, discord_user_id: str) -> Dict[str, Any]:
        """
        Mark a custom quest as completed for a Discord member.

        Args:
            custom_quest_id (int): The ID of the custom quest
            discord_user_id (str): The Discord user ID of the player

        Returns:
            Dict[str, Any]: Completion information containing:
                - success (bool): Whether the operation was successful
                - message (str): A message describing the result
                - completed_at (str, optional): The ISO-formatted timestamp of completion

        Raises:
            requests.HTTPError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/custom-quests/{custom_quest_id}/complete"
        )
        data = {"discord_user_id": str(discord_user_id)}
        response = requests.post(url, headers=self.headers, json=data)
        return self._handle_response(response)

    async def complete_custom_quest_async(self, custom_quest_id: int, discord_user_id: str) -> Dict[str, Any]:
        """
        Mark a custom quest as completed for a Discord member asynchronously.

        Args:
            custom_quest_id (int): The ID of the custom quest
            discord_user_id (str): The Discord user ID of the player

        Returns:
            Dict[str, Any]: Completion information containing:
                - success (bool): Whether the operation was successful
                - message (str): A message describing the result
                - completed_at (str, optional): The ISO-formatted timestamp of completion

        Raises:
            aiohttp.ClientResponseError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/custom-quests/{custom_quest_id}/complete"
        )
        data = {"discord_user_id": str(discord_user_id)}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=data) as response:
                return await self._handle_async_response(response)

    # Get completed members endpoints
    def get_completed_members(self, custom_quest_id: int) -> List[Dict[str, Any]]:
        """
        Get a list of all members who have completed a given custom quest.

        Args:
            custom_quest_id (int): The ID of the custom quest

        Returns:
            List[Dict[str, Any]]: A list of completed members, each containing:
                - discord_user_id (str): The Discord user ID
                - last_completed (str): The ISO-formatted timestamp of the last completion
                - times_completed (int): The number of times the quest was completed

        Raises:
            requests.HTTPError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/custom-quests/{custom_quest_id}/completed-members"
        )
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    async def get_completed_members_async(self, custom_quest_id: int) -> List[Dict[str, Any]]:
        """
        Get a list of all members who have completed a given custom quest asynchronously.

        Args:
            custom_quest_id (int): The ID of the custom quest

        Returns:
            List[Dict[str, Any]]: A list of completed members, each containing:
                - discord_user_id (str): The Discord user ID
                - last_completed (str): The ISO-formatted timestamp of the last completion
                - times_completed (int): The number of times the quest was completed

        Raises:
            aiohttp.ClientResponseError: If the request fails
        """
        url = self._format_url(
            f"/servers/{self.server_id}/custom-quests/{custom_quest_id}/completed-members"
        )
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await self._handle_async_response(response)
