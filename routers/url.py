from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from orm import NoMatch, MultipleMatches

from db.models.url import Url
from scheme import FailedResponse

router = APIRouter()


@router.get("/{short_path}", response_class=RedirectResponse, status_code=302)
def short_link(short_path: str):
    try:
        url = await Url.objects.get(short_path=short_path)
    except (NoMatch, MultipleMatches):
        return FailedResponse(error="Url does not exist")

    pass
