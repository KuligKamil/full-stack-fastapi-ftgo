from typing import Optional

from pydantic import Field

from ftgo_utils.schemas import uuid_field, RoleMixin, PhoneNumberMixin, UserIdMixin

class UserStateSchema(PhoneNumberMixin, RoleMixin, UserIdMixin):
    hashed_password: str = Field(..., min_length=1, max_length=512)
