from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple health check used by the pipeline and the deployed app."""
    return Response({"status": "ok"})


@api_view(["GET"])
def hello(request):
    """Greets the caller. Try /api/hello/?name=Ada"""
    name = request.query_params.get("name", "World")
    return Response({"message": f"Hello, {name}!", "course": "CSC325", "version":"1.1"})
