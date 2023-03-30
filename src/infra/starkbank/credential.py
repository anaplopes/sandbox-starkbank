import starkbank
from src.settings import settings


private_key_content = """
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIKlu/umyY0PjwWw/uATaKu1Ug2l/NUJVIHUUOV3H4glnoAcGBSuBBAAK
oUQDQgAEIy4ACjaUkq7PCsOiSRQOKrz+ZvMwULRNkyi9kMJ1R4xorNFXJ+s3Rjym
OKkh+ov8e/F13x4eBb52GmFnlHEX/Q==
-----END EC PRIVATE KEY-----
"""


project = starkbank.Project(
    environment="sandbox", id=settings.SB_PROJECT_ID, private_key=settings.PRIVATE_KEY
)
starkbank.user = project
