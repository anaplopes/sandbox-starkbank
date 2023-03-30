import starkbank
from src.settings import settings


project = starkbank.Project(
    environment="sandbox", id=settings.SB_PROJECT_ID, private_key=settings.PRIVATE_KEY
)
starkbank.user = project
