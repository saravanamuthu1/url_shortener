from typing import List
from typing import Optional
from datetime import datetime
from sqlalchemy import Column,Integer,String, DateTime,UUID,ForeignKey,Boolean
from sqlalchemy.orm import mapped_column
from datetime import datetime, UTC
import uuid

class TimestampMixin():
    created_at = mapped_column(DateTime(timezone=True),default = lambda: datetime.now(UTC),nullable=False)
    updated_at = mapped_column(DateTime(timezone=True),onupdate = lambda: datetime.now(UTC),nullable=True)\

class User(TimestampMixin,Base):
    __tablename__ = 'users'
    id = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,nullable=False)
    email= mapped_column(String, unique=True,nullable=False)
    hash_password = mapped_column(String,nullable=False)
    api_key = mapped_column(String, unique=True,nullable=True)

class Url(TimestampMixin,Base):
    __tablename__ = "urls"
    id = mapped_column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
    original_url = mapped_column(String, nullable=False)
    short_alias = mapped_column(String, nullable=True,unique=True)
    expires_at = mapped_column(DateTime(timezone=True),nullable=True)
    is_public = mapped_column(Boolean, default=True,nullable=False)
    owner_id = mapped_column(UUID(as_uuid=True),ForeignKey("users.id"), nullable=False)

class UrlPermission(TimestampMixin,Base):
    __tablename__ = "url_permission"
    id = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,nullable=False)
    url_id = mapped_column(UUID(as_uuid=True),ForeignKey("urls.id"), nullable=False)
    user_id = mapped_column(UUID(as_uuid=True),ForeignKey("users.id"), nullable=False)

class  RedirectEvent(Base):
    __tablename__ = "redirect_event"
    id = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,nullable=False)
    short_code = mapped_column(String, nullable=False)
    timestamp = mapped_column(DateTime(timezone=True),default = lambda: datetime.now(UTC),nullable=False)
    country = mapped_column(String, nullable=True)
    device = mapped_column(String, nullable=True)
    ip_address = mapped_column(String, nullable=True)
    created_at = mapped_column(DateTime(timezone=True),default = lambda: datetime.now(UTC),nullable=False)
        