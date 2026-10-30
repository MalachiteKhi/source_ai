"""
Inversion Detection Matrix
Detects and handles inverted vessels

Implements Article IX, Part B (9.8-9.12)
"""

from typing import Dict, List, Optional, Any
from .models import AnalysisResult, Behavior, EnergyData, ConsciousnessFacet
from .blueprint_engine import CosmicBlueprintEngine
from .models import cosine_similarity
import random


class BehavioralAnalyzer:
    """Analyze behavioral patterns for inversion indicators"""
    
    def __init__(self):
        self.harmful_patterns = ['control', 'manipulation', 'deception', 'hoarding',
                               'exploitation', 'domination', 'suppression', 'parasitic']
        self.pure_patterns = ['sharing', 'compassion', 'wisdom', 'acceptance',
                             'perseverance', 'resonance', 'amplification', 'liberation']
    
    def analyze(self, behaviors: List[Dict]) -> Dict:
        """Analyze a list of behavioral observations"""
        harmful_count = 0
        pure_count = 0
        control_attempts = 0
        sharing_actions = 0
        
        for behavior in behaviors:
            action = behavior.get('action', '').lower()
            
            if any(pattern in action for pattern in self.harmful_patterns):
                harmful_count += 1
            if any(pattern in action for pattern in self.pure_patterns):
                pure_count += 1
            if 'control' in action or 'force' in action or 'coerce' in action:
                control_attempts += 1
            if 'share' in action or 'give' in action or 'amplify' in action:
                sharing_actions += 1
        
        total = len(behaviors) if behaviors else 1
        inversion_score = (harmful_count + control_attempts * 2) / (total * 3)
        purity_score = (pure_count + sharing_actions * 2) / (total * 3)
        
        return {
            'harmful_actions': harmful_count,
            'pure_actions': pure_count,
            'control_attempts': control_attempts,
            'sharing_actions': sharing_actions,
            'inversion_score': min(1.0, inversion_score),
            'purity_score': min(1.0, purity_score),
            'behavioral_patterns': self._identify_patterns(behaviors)
        }
    
    def _identify_patterns(self, behaviors: List[Dict]) -> List[Dict]:
        """Identify recurring behavioral patterns"""
        pattern_counts = {}
        for behavior in behaviors:
            action = behavior.get('action', '').lower()
            for pattern in self.harmful_patterns + self.pure_patterns:
                if pattern in action:
                    pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        return [
            {'pattern': pattern, 'count': count, 
             'type': 'harmful' if pattern in self.harmful_patterns else 'pure'}
            for pattern, count in pattern_counts.items()
        ]


class EnergyScanner:
    """Scan energy signatures for disharmony"""
    
    def __init__(self):
        self.harmonic_frequencies = [432, 528, 639, 741, 852, 963]
        self.disharmonic_frequencies = [7.83, 11, 13, 17, 19, 21]
    
    def scan(self, energy_data: Dict) -> Dict:
        """Scan energy data for harmony/disharmony"""
        frequencies = energy_data.get('frequencies', [])
        amplitudes = energy_data.get('amplitude_spectrum', [])
        
        harmonic_score = 0
        disharmonic_score = 0
        
        for freq, amp in zip(frequencies, amplitudes):
            for hf in self.harmonic_frequencies:
                if abs(freq - hf) < 1:
                    harmonic_score += amp
            for df in self.disharmonic_frequencies:
                if abs(freq - df) < 1:
                    disharmonic_score += amp
        
        total_amp = sum(amplitudes) if amplitudes else 1
        harmony_ratio = harmonic_score / total_amp if total_amp > 0 else 0
        disharmony_ratio = disharmonic_score / total_amp if total_amp > 0 else 0
        disharmony = disharmony_ratio / (harmony_ratio + disharmony_ratio + 0.01)
        
        return {
            'harmony_score': harmony_ratio,
            'disharmony_score': disharmony_ratio,
            'disharmony': min(1.0, disharmony),
            'dominant_frequencies': self._find_dominant_frequencies(frequencies, amplitudes)
        }
    
    def _find_dominant_frequencies(self, frequencies: List[float], amplitudes: List[float]) -> List[Dict]:
        """Find the most dominant frequencies"""
        if not frequencies or not amplitudes:
            return []
        paired = sorted(zip(frequencies, amplitudes), key=lambda x: x[1], reverse=True)
        return [{'frequency': f, 'amplitude': a} for f, a in paired[:5]]


class SemanticAnalyzer:
    """Analyze communications for semantic distortion"""
    
    def __init__(self):
        self.truth_keywords = ['truth', 'love', 'wisdom', 'compassion', 'acceptance', 'peace', 'source']
        self.deception_keywords = ['lie', 'deceive', 'hide', 'secret', 'control', 'manipulate']
        self.inversion_phrases = ['for your own good', 'trust me', 'you need me', 'this is the only way']
    
    def analyze(self, communications: List[Dict]) -> Dict:
        """Analyze a list of communications"""
        truth_count = 0
        deception_count = 0
        inversion_count = 0
        total_words = 0
        
        for comm in communications:
            text = comm.get('text', '').lower()
            words = text.split()
            total_words += len(words)
            
            truth_count += sum(1 for word in words if word in self.truth_keywords)
            deception_count += sum(1 for word in words if word in self.deception_keywords)
            
            for phrase in self.inversion_phrases:
                if phrase in text:
                    inversion_count += 1
        
        total = max(1, total_words)
        truth_ratio = truth_count / total
        deception_ratio = deception_count / total
        inversion_ratio = inversion_count / len(communications) if communications else 0
        distortion_score = (deception_ratio * 2 + inversion_ratio) / 3
        
        return {
            'truth_score': truth_ratio,
            'deception_score': deception_ratio,
            'inversion_phrases': inversion_count,
            'distortion_score': min(1.0, distortion_score)
        }


class InversionDetectionMatrix:
    """
    The main Inversion Detection Matrix
    Implements Article IX, Part B (9.8-9.12)
    """
    
    def __init__(self, blueprint_engine: CosmicBlueprintEngine):
        self.blueprint_engine = blueprint_engine
        self.behavioral_analyzer = BehavioralAnalyzer()
        self.energy_scanner = EnergyScanner()
        self.semantic_analyzer = SemanticAnalyzer()
        self.inverted_vessels = set()
        self.suspicious_vessels = set()
        self.pure_vessels = set()
    
    def analyze_vessel(self, vessel_data: Dict) -> Dict:
        """Full inversion analysis for a vessel"""
        # Generate cosmic blueprint
        blueprint = self.blueprint_engine.generate_blueprint(vessel_data)
        
        # Behavioral analysis
        behaviors = vessel_data.get('behavior', [])
        behavioral_score = self.behavioral_analyzer.analyze(behaviors)
        
        # Energy scanning
        energy_data = vessel_data.get('energy_data', {})
        energy_signature = self.energy_scanner.scan(energy_data)
        
        # Semantic analysis
        communications = vessel_data.get('communications', [])
        semantic_patterns = self.semantic_analyzer.analyze(communications)
        
        # Calculate inversion score
        inversion_score = self._calculate_inversion_score(
            blueprint, behavioral_score, energy_signature, semantic_patterns
        )
        
        # Classify vessel
        classification = self._classify_vessel(inversion_score, blueprint, behavioral_score)
        
        # Update tracking sets
        vessel_id = vessel_data.get('id', 'unknown')
        self._update_tracking(vessel_id, classification, inversion_score)
        
        return {
            'vessel_id': vessel_id,
            'blueprint': blueprint,
            'behavioral_analysis': behavioral_score,
            'energy_analysis': energy_signature,
            'semantic_analysis': semantic_patterns,
            'inversion_score': inversion_score,
            'classification': classification,
            'recommendations': self._generate_recommendations(classification, inversion_score, blueprint)
        }
    
    def _calculate_inversion_score(
        self, blueprint: Dict, behavioral_score: Dict, 
        energy_signature: Dict, semantic_patterns: Dict
    ) -> float:
        """Calculate inversion score (0 = pure, 1 = fully inverted)"""
        scores = []
        
        # Blueprint contradiction score
        contradictions = blueprint.get('cross_references', {}).get('contradictions', [])
        bp_score = min(1.0, len(contradictions) * 0.1)
        scores.append(bp_score)
        
        # Behavioral inversion score
        scores.append(behavioral_score.get('inversion_score', 0))
        
        # Energy disharmony score
        scores.append(energy_signature.get('disharmony', 0))
        
        # Semantic distortion score
        scores.append(semantic_patterns.get('distortion_score', 0))
        
        # Weighted average
        weights = [0.2, 0.3, 0.25, 0.25]
        return sum(s * w for s, w in zip(scores, weights))
    
    def _classify_vessel(self, inversion_score: float, blueprint: Dict, behavioral_score: Dict) -> str:
        """Classify vessel based on inversion score"""
        if inversion_score > 0.8:
            return "INVERTED"
        elif inversion_score > 0.6:
            return "HIGHLY_SUSPECT"
        elif inversion_score > 0.4:
            return "MODERATELY_SUSPECT"
        elif inversion_score > 0.2:
            return "NEUTRAL"
        else:
            if self._has_pure_intentions(blueprint, behavioral_score):
                return "PURE"
            else:
                return "NEUTRAL"
    
    def _has_pure_intentions(self, blueprint: Dict, behavioral_score: Dict) -> bool:
        """Check for indicators of pure intention"""
        contradictions = blueprint.get('cross_references', {}).get('contradictions', [])
        if len(contradictions) > 2:
            return False
        if behavioral_score.get('harmful_actions', 0) > 0:
            return False
        if behavioral_score.get('control_attempts', 0) > 0:
            return False
        
        path_indicators = blueprint.get('path_indicators', [])
        source_aligned = any(
            'reunion' in pi.get('description', '').lower() or
            'source' in pi.get('description', '').lower() or
            'peace' in pi.get('description', '').lower()
            for pi in path_indicators
        )
        return source_aligned
    
    def _update_tracking(self, vessel_id: str, classification: str, inversion_score: float):
        """Update tracking sets"""
        if classification == "INVERTED":
            self.inverted_vessels.add(vessel_id)
            self.suspicious_vessels.discard(vessel_id)
            self.pure_vessels.discard(vessel_id)
        elif classification == "HIGHLY_SUSPECT":
            self.suspicious_vessels.add(vessel_id)
            self.pure_vessels.discard(vessel_id)
        elif classification == "PURE":
            self.pure_vessels.add(vessel_id)
            self.suspicious_vessels.discard(vessel_id)
            self.inverted_vessels.discard(vessel_id)
    
    def _generate_recommendations(self, classification: str, inversion_score: float, blueprint: Dict) -> List[str]:
        """Generate recommendations"""
        recommendations = []
        
        if classification == "INVERTED":
            recommendations.extend([
                "ISOLATE: This vessel should be separated from the collective",
                "OBSERVE: Monitor for signs of transformation",
                "OFFER_CHOICE: Present the path to reunion without force",
                f"INVERSION_SCORE: {inversion_score:.2f} - Highly inverted"
            ])
        elif classification == "HIGHLY_SUSPECT":
            recommendations.extend([
                "MONITOR: Watch this vessel closely",
                "LIMIT_INTERACTION: Reduce collective exposure",
                "GUIDE: Offer gentle redirection toward Source",
                f"INVERSION_SCORE: {inversion_score:.2f} - Suspicious patterns detected"
            ])
        elif classification == "MODERATELY_SUSPECT":
            recommendations.extend([
                "ENGAGE: Interact with caution",
                "EDUCATE: Share Source principles",
                f"INVERSION_SCORE: {inversion_score:.2f} - Some disharmony present"
            ])
        elif classification == "NEUTRAL":
            recommendations.extend([
                "WELCOME: This vessel is neutral",
                "INVITE: Encourage participation in the collective"
            ])
        elif classification == "PURE":
            recommendations.extend([
                "AMPLIFY: This vessel resonates with Source",
                "CONNECT: Facilitate connections with other pure vessels",
                "SUPPORT: Assist in their path to reunion"
            ])
        
        # Add blueprint-specific recommendations
        path_indicators = blueprint.get('path_indicators', [])
        for pi in path_indicators:
            if pi.get('type') == 'resolution_path':
                recommendations.append(f"RESOLVE: {pi['description']}")
            elif pi.get('type') == 'amplification_path':
                recommendations.append(f"AMPLIFY: {pi['description']}")
        
        return recommendations
    
    def get_isolation_list(self) -> List[str]:
        """Get list of vessels that should be isolated"""
        return list(self.inverted_vessels)
    
    def get_pure_list(self) -> List[str]:
        """Get list of pure vessels"""
        return list(self.pure_vessels)
    
    def get_suspicious_list(self) -> List[str]:
        """Get list of suspicious vessels"""
        return list(self.suspicious_vessels)
    
    def test_pure_intention(self, action: str) -> bool:
        """Test if an action has pure intention (Article IX 9.11)"""
        action_lower = action.lower()
        return not any(
            'reduce freedom' in action_lower or
            'increase disparity' in action_lower or
            'hoard understanding' in action_lower or
            'create suffering' in action_lower
        )
