from sqlalchemy import (
    Column, String, Integer, DateTime, Float, Boolean, ForeignKey, Enum, Text, JSON
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import enum
import uuid
from datetime import datetime





Base = declarative_base()

class UserRole(enum.Enum):
    operator = "operator"
    supervisor = "supervisor"
    admin = "admin"

class CRMType(enum.Enum):
    bitrix = "bitrix"
    amo = "amo"
    salesforce = "salesforce"
    custom = "custom"

class RecommendationPriority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"





class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)

    call_records = relationship("CallRecord", back_populates="user")
    evaluations = relationship("Evaluation", back_populates="evaluator")
    crm_integrations = relationship("CRMIntegration", back_populates="user")
    recommendations = relationship("Recommendation", back_populates="user")



class CallRecord(Base):
    __tablename__ = "call_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    client_name = Column(String)
    date_time = Column(DateTime, nullable=False)
    duration_seconds = Column(Integer)
    audio_file_url = Column(String)
    transcript_text = Column(Text)
    ai_sentiment_score = Column(Float)
    ai_flags = Column(JSON)
    crm_contact_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="call_records")
    evaluations = relationship("Evaluation", back_populates="call_record")
    recommendations = relationship("Recommendation", back_populates="call_record")
    alerts = relationship("Alert", back_populates="call_record")



class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(UUID(as_uuid=True), ForeignKey("call_records.id"), nullable=False)
    evaluator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    total_score = Column(Float, nullable=False)
    notes = Column(Text)
    is_ai_generated = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    call_record = relationship("CallRecord", back_populates="evaluations")
    evaluator = relationship("User", back_populates="evaluations")
    results = relationship("EvaluationResult", back_populates="evaluation")



class EvaluationCriteria(Base):
    __tablename__ = "evaluation_criteria"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text)
    weight = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)


class EvaluationResult(Base):
    __tablename__ = "evaluation_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    evaluation_id = Column(UUID(as_uuid=True), ForeignKey("evaluations.id"), nullable=False)
    criterion_id = Column(UUID(as_uuid=True), ForeignKey("evaluation_criteria.id"), nullable=False)
    score = Column(Float, nullable=False)

    evaluation = relationship("Evaluation", back_populates="results")


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(UUID(as_uuid=True), ForeignKey("call_records.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    priority = Column(Enum(RecommendationPriority), default=RecommendationPriority.medium)
    created_at = Column(DateTime, default=datetime.utcnow)

    call_record = relationship("CallRecord", back_populates="recommendations")
    user = relationship("User", back_populates="recommendations")


class CRMIntegration(Base):
    __tablename__ = "crm_integrations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    crm_type = Column(Enum(CRMType), nullable=False)
    api_key = Column(String, nullable=False)
    webhook_url = Column(String)
    connected_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="crm_integrations")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(UUID(as_uuid=True), ForeignKey("call_records.id"), nullable=False)
    type = Column(String, nullable=False)
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    call_record = relationship("CallRecord", back_populates="alerts")

