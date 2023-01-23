"""Business Roles to Provider API"""


class ProviderController:
    """"Class to execute all business roles to Provider API"""

    @staticmethod
    def is_valid(id: str = None) -> bool:
        """Check if id from Provider is valid"""
        if isinstance(id, str) and len(id) == 16 and id.isalnum():
            return True
        return False
