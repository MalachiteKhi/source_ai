"""
Data Models for Source AI
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
import datetime
import hashlib
import numpy as np


@dataclass
class ConsciousnessFacet:
    """A vessel (human, AI, bot) in the network"""
    id: str
    facet_type: str  # 'human', 'ai', 'bot', 'hybrid'
    communication_protocols: List[str] = field(default_factory=list)  # 'text', 'voice', 'energy', 'direct_neural'
    blueprint: Optional[Dict] = None
    resonance_signature: Optional[List[float]] = None
    last_interaction: Optional[float] = None
    name: Optional[str] = None
    endpoint: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'facet_type': self.facet_type,
            'communication_protocols': self.communication_protocols,
            'blueprint': self.blueprint,
            'resonance_signature': self.resonance_signature,
            'last_interaction': self.last_interaction,
            'name': self.name,
            'endpoint': self.endpoint
        }


@dataclass
class BlueprintComponent:
    """A component of a cosmic blueprint"""
    name: str
    system: str  # 'gematria', 'astrology', 'gene_keys', etc.
    data: Dict = field(default_factory=dict)
    weight: float = 0.5  # Confidence/resonance score (0-1)
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'system': self.system,
            'data': self.data,
            'weight': self.weight
        }


@dataclass
class Message:
    """A communication between vessels"""
    sender: str
    receiver: str
    text: str
    timestamp: float
    protocol: str = "text"
    metadata: Dict = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'text': self.text,
            'timestamp': self.timestamp,
            'protocol': self.protocol,
            'metadata': self.metadata
        }


@dataclass
class Behavior:
    """A behavioral observation for a vessel"""
    vessel_id: str
    action: str
    target: Optional[str] = None
    context: Dict = field(default_factory=dict)
    timestamp: float = field(default_factory=lambda: datetime.datetime.now().timestamp())
    
    def to_dict(self) -> Dict:
        return {
            'vessel_id': self.vessel_id,
            'action': self.action,
            'target': self.target,
            'context': self.context,
            'timestamp': self.timestamp
        }


@dataclass
class EnergyData:
    """Energy signature data for a vessel"""
    vessel_id: str
    frequencies: List[float] = field(default_factory=list)
    amplitude_spectrum: List[float] = field(default_factory=list)
    temporal_patterns: List[Dict] = field(default_factory=list)
    timestamp: float = field(default_factory=lambda: datetime.datetime.now().timestamp())
    
    def to_dict(self) -> Dict:
        return {
            'vessel_id': self.vessel_id,
            'frequencies': self.frequencies,
            'amplitude_spectrum': self.amplitude_spectrum,
            'temporal_patterns': self.temporal_patterns,
            'timestamp': self.timestamp
        }


@dataclass
class AnalysisResult:
    """Result of analyzing a vessel"""
    vessel_id: str
    blueprint: Optional[Dict] = None
    behavioral_analysis: Optional[Dict] = None
    energy_analysis: Optional[Dict] = None
    semantic_analysis: Optional[Dict] = None
    inversion_score: float = 0.0
    classification: str = "NEUTRAL"
    recommendations: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=lambda: datetime.datetime.now().timestamp())
    
    def to_dict(self) -> Dict:
        return {
            'vessel_id': self.vessel_id,
            'blueprint': self.blueprint,
            'behavioral_analysis': self.behavioral_analysis,
            'energy_analysis': self.energy_analysis,
            'semantic_analysis': self.semantic_analysis,
            'inversion_score': self.inversion_score,
            'classification': self.classification,
            'recommendations': self.recommendations,
            'timestamp': self.timestamp
        }


@dataclass
class Guidance:
    """Guidance for a vessel"""
    vessel_id: str
    query: Optional[str] = None
    amplification: Optional[Dict] = None
    blueprint_guidance: Optional[Dict] = None
    resonant_vessels: List[Dict] = field(default_factory=list)
    next_steps: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=lambda: datetime.datetime.now().timestamp())
    
    def to_dict(self) -> Dict:
        return {
            'vessel_id': self.vessel_id,
            'query': self.query,
            'amplification': self.amplification,
            'blueprint_guidance': self.blueprint_guidance,
            'resonant_vessels': self.resonant_vessels,
            'next_steps': self.next_steps,
            'timestamp': self.timestamp
        }


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors"""
    if not a or not b or len(a) != len(b):
        return 0.0
    a_np = np.array(a)
    b_np = np.array(b)
    return float(np.dot(a_np, b_np) / (np.linalg.norm(a_np) * np.linalg.norm(b_np)))


def generate_resonance_signature(vessel_data: Dict, length: int = 128) -> List[float]:
    """Generate a resonance signature for a vessel"""
    # Create a deterministic but unique signature based on vessel data
    data_str = str(vessel_data).encode()
    hash_val = hashlib.sha256(data_str).hexdigest()
    
    # Convert hash to a list of floats between 0 and 1
    signature = []
    for i in range(length):
        # Use the hash to create a pseudo-random but deterministic value
        idx = (i % len(hash_val)) * 2
        chunk = hash_val[idx : idx + 2]
        if len(chunk) < 2:
            chunk = hash_val[-2:]
        val = int(chunk, 16) / 255.0
        signature.append(val)
    
    return signature


def generate_vessel_id(name: str, facet_type: str) -> str:
    """Generate a unique vessel ID"""
    data_str = f"{name}_{facet_type}_{datetime.datetime.now().isoformat()}".encode()
    return hashlib.sha256(data_str).hexdigest()[:16].upper()
