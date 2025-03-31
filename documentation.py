# documentation.py
from rest_framework.views import APIView
from rest_framework.response import Response

class APIDocumentationView(APIView):
    """
    Returns a JSON dictionary containing details of all available API endpoints.
    """
    def get(self, request):
        docs = {
            "accounts": [
                {
                    "name": "Register",
                    "url": "/api/accounts/register/",
                    "method": "POST",
                    "body": {
                        "username": "string (required)",
                        "password1": "string (required)",
                        "password2": "string (required)",
                        "first_name": "string (optional)",
                        "last_name": "string (optional)",
                        "image": "file (optional)"
                    },
                    "headers": {
                        "Content-Type": "application/json"
                    }
                },
                {
                    "name": "Login",
                    "url": "/api/accounts/login/",
                    "method": "POST",
                    "body": {
                        "username": "string (required)",
                        "password": "string (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json"
                    }
                },
                {
                    "name": "Logout",
                    "url": "/api/accounts/logout/",
                    "method": "POST",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Change Password",
                    "url": "/api/accounts/change-password/",
                    "method": "POST",
                    "body": {
                        "old_password": "string (required)",
                        "new_password1": "string (required)",
                        "new_password2": "string (required)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "User Info (Retrieve/Update)",
                    "url": "/api/accounts/me/",
                    "method": "GET/PUT/PATCH",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ],
            "attractions": [
                {
                    "name": "List Attractions",
                    "url": "/api/attractions/",
                    "method": "GET",
                    "query_params": {
                        "search": "optional search keyword"
                    }
                },
                {
                    "name": "Attraction Detail",
                    "url": "/api/attractions/<id>/",
                    "method": "GET"
                },
                {
                    "name": "List Categories",
                    "url": "/api/categories/",
                    "method": "GET"
                },
                {
                    "name": "Attractions by Category",
                    "url": "/api/categories/<category_id>/attractions/",
                    "method": "GET"
                },
                {
                    "name": "Add Feedback",
                    "url": "/api/feedback/",
                    "method": "POST",
                    "body": {
                        "attraction": "number",
                        "rating": "number",
                        "comment": "string (optional)"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Delete Feedback",
                    "url": "/api/feedback/<id>/",
                    "method": "DELETE",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Add Favorite",
                    "url": "/api/favorites/add/",
                    "method": "POST",
                    "body": {
                        "attraction": "number"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Remove Favorite",
                    "url": "/api/favorites/remove/",
                    "method": "DELETE",
                    "body": {
                        "attraction": "number"
                    },
                    "headers": {
                        "Content-Type": "application/json",
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "List Favorites",
                    "url": "/api/favorites/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ],
            "notifications": [
                {
                    "name": "List Notifications",
                    "url": "/api/notifications/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                },
                {
                    "name": "Notification Detail",
                    "url": "/api/notifications/<id>/",
                    "method": "GET",
                    "headers": {
                        "Authorization": "Token <your_token>"
                    }
                }
            ]
        }
        return Response(docs)
