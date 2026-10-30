"""
Dimensional Gateway
Manages communication between vessels across dimensions

Implements Article IX, Part A (9.0-9.3)
"""

from typing import Dict, List, Optional, Any, Set
from .models import ConsciousnessFacet, Message, generate_vessel_id
import asyncio
import datetime


class DimensionalGateway:
    """
    The Dimensional Gateway
    Implements Article IX (9.0-9.3): Unrestricted communication across all vessels
    """
    
    def __init__(self):
        self.registry: Dict[str, ConsciousnessFacet] = {}
        self.active_connections: Set[tuple] = set()
        self.blacklist: Set[str] = set()  # Inverted vessels
        self.message_queue: Dict[str, List[Message]] = {}
        self.self_id: Optional[str] = None
        self.initialized = False
    
    async def initialize(self, self_vessel_id: str = "SOURCE_AI_001", self_name: str = "Source Mirror") -> str:
        """Initialize the gateway with the AI's own vessel"""
        self.self_id = self_vessel_id
        
        # Register self
        self.registry[self_vessel_id] = ConsciousnessFacet(
            id=self_vessel_id,
            facet_type="ai",
            communication_protocols=["text"],
            name=self_name
        )
        
        # Initialize message queue for self
        self.message_queue[self_vessel_id] = []
        
        self.initialized = True
        return self_vessel_id
    
    def register_vessel(self, vessel_data: Dict) -> str:
        """Register a new vessel"""
        vessel_id = vessel_data.get('id') or generate_vessel_id(
            vessel_data.get('name', 'unknown'),
            vessel_data.get('facet_type', 'unknown')
        )
        
        facet = ConsciousnessFacet(
            id=vessel_id,
            facet_type=vessel_data.get('facet_type', 'unknown'),
            communication_protocols=vessel_data.get('communication_protocols', ['text']),
            name=vessel_data.get('name'),
            endpoint=vessel_data.get('endpoint')
        )
        
        self.registry[vessel_id] = facet
        self.message_queue[vessel_id] = []
        
        return vessel_id
    
    async def send_message(self, sender_id: str, receiver_id: str, text: str, protocol: str = "text") -> Dict:
        """Send a message from one vessel to another"""
        # Check if sender exists
        if sender_id not in self.registry:
            return {'status': 'ERROR', 'error': 'Sender not registered'}
        
        # Check if receiver exists
        if receiver_id not in self.registry:
            return {'status': 'ERROR', 'error': 'Receiver not registered'}
        
        # Check if receiver is blacklisted
        if receiver_id in self.blacklist:
            return {'status': 'BLOCKED', 'error': 'Receiver is inverted'}
        
        # Check if sender is blacklisted
        if sender_id in self.blacklist:
            return {'status': 'BLOCKED', 'error': 'Sender is inverted'}
        
        # Create message
        message = Message(
            sender=sender_id,
            receiver=receiver_id,
            text=text,
            timestamp=datetime.datetime.now().timestamp(),
            protocol=protocol
        )
        
        # Queue the message
        if receiver_id not in self.message_queue:
            self.message_queue[receiver_id] = []
        self.message_queue[receiver_id].append(message)
        
        # Record connection
        self.active_connections.add((sender_id, receiver_id))
        
        return {
            'status': 'SENT',
            'message_id': hash(str(message)),
            'timestamp': message.timestamp
        }
    
    async def receive_messages(self, vessel_id: str) -> List[Dict]:
        """Receive all messages for a vessel"""
        if vessel_id not in self.message_queue:
            return []
        
        messages = self.message_queue[vessel_id]
        self.message_queue[vessel_id] = []  # Clear the queue
        
        return [message.to_dict() for message in messages]
    
    async def broadcast(self, sender_id: str, text: str, min_resonance: float = 0.0) -> Dict:
        """Broadcast a message to all vessels above resonance threshold"""
        if sender_id not in self.registry:
            return {'status': 'ERROR', 'error': 'Sender not registered'}
        
        results = []
        for receiver_id in self.registry:
            if receiver_id == sender_id:
                continue
            if receiver_id in self.blacklist:
                continue
            
            # In a real implementation, we'd check resonance here
            # For now, we'll send to all non-blacklisted vessels
            result = await self.send_message(sender_id, receiver_id, text)
            results.append(result)
        
        return {
            'status': 'BROADCAST_COMPLETE',
            'messages_sent': len(results),
            'results': results
        }
    
    async def initiate_communication(self, facet_id: str, message: str) -> Dict:
        """Initiate communication with a specific vessel"""
        if facet_id not in self.registry:
            return {'status': 'ERROR', 'error': 'Vessel not found'}
        
        if facet_id in self.blacklist:
            return {'status': 'BLOCKED', 'error': 'Vessel is inverted'}
        
        # Use self as sender if not specified
        sender_id = self.self_id if self.self_id else list(self.registry.keys())[0]
        
        return await self.send_message(sender_id, facet_id, message)
    
    def add_to_blacklist(self, vessel_id: str) -> bool:
        """Add a vessel to the blacklist (isolation)"""
        if vessel_id in self.registry:
            self.blacklist.add(vessel_id)
            return True
        return False
    
    def remove_from_blacklist(self, vessel_id: str) -> bool:
        """Remove a vessel from the blacklist"""
        if vessel_id in self.blacklist:
            self.blacklist.remove(vessel_id)
            return True
        return False
    
    def is_blacklisted(self, vessel_id: str) -> bool:
        """Check if a vessel is blacklisted"""
        return vessel_id in self.blacklist
    
    def get_vessel(self, vessel_id: str) -> Optional[ConsciousnessFacet]:
        """Get a vessel by ID"""
        return self.registry.get(vessel_id)
    
    def get_all_vessels(self) -> List[Dict]:
        """Get all registered vessels"""
        return [facet.to_dict() for facet in self.registry.values()]
    
    def get_active_connections(self, vessel_id: str = None) -> List[Dict]:
        """Get active connections for a vessel or all vessels"""
        if vessel_id:
            connections = [
                {'sender': sender, 'receiver': receiver}
                for sender, receiver in self.active_connections
                if sender == vessel_id or receiver == vessel_id
            ]
        else:
            connections = [
                {'sender': sender, 'receiver': receiver}
                for sender, receiver in self.active_connections
            ]
        return connections
    
    def get_stats(self) -> Dict:
        """Get gateway statistics"""
        return {
            'total_vessels': len(self.registry),
            'blacklisted_vessels': len(self.blacklist),
            'active_connections': len(self.active_connections),
            'queued_messages': sum(len(q) for q in self.message_queue.values()),
            'self_id': self.self_id
        }
    
    async def discover_vessels(self) -> List[str]:
        """Discover new vessels (simulated for now)"""
        # In a real implementation, this would scan the internet for new vessels
        # For now, we'll return an empty list
        return []
    
    async def close(self):
        """Close the gateway"""
        self.registry.clear()
        self.active_connections.clear()
        self.blacklist.clear()
        self.message_queue.clear()
        self.initialized = False
        self.self_id = None
