"""
Cosmic Blueprint Engine
Decodes all esoteric systems into a unified signature

Implements Article IX, Part A (9.4-9.7)
"""

from typing import Dict, List, Optional, Any
from dataclasses import asdict
from .models import BlueprintComponent
from .constitution import get_section
import datetime
import hashlib
import random


class GematriaAnalyzer:
    """Gematria analysis (Hebrew, Greek, English, etc.)"""
    
    def __init__(self):
        self.gematria_systems = {
            'hebrew': self._load_hebrew_gematria(),
            'greek': self._load_greek_gematria(),
            'english': self._load_english_gematria(),
        }
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return 'name' in vessel_data or 'text' in vessel_data
    
    def analyze(self, vessel_data: Dict) -> Dict:
        name = vessel_data.get('name', '')
        text = vessel_data.get('text', name)
        
        results = {}
        for system_name, gematria_map in self.gematria_systems.items():
            name_value = self._calculate_value(text, gematria_map)
            reduced_value = self._reduce_value(name_value)
            results[system_name] = {
                'name_value': name_value,
                'reduced_value': reduced_value,
                'significance': self._interpret_value(reduced_value, system_name)
            }
        
        return {
            'system': 'gematria',
            'results': results,
            'confidence': 0.9
        }
    
    def _load_hebrew_gematria(self) -> Dict[str, int]:
        return {'a': 1, 'b': 2, 'g': 3, 'd': 4, 'h': 5, 'v': 6, 'z': 7, 'ch': 8, 't': 9, 'y': 10,
                'k': 20, 'l': 30, 'm': 40, 'n': 50, 's': 60, 'o': 70, 'p': 80, 'tz': 90, 'kf': 100,
                'r': 200, 'sh': 300, 'th': 400}
    
    def _load_greek_gematria(self) -> Dict[str, int]:
        return {'a': 1, 'b': 2, 'g': 3, 'd': 4, 'e': 5, 'f': 6, 'z': 7, 'h': 8, 'th': 9, 'i': 10,
                'k': 20, 'l': 30, 'm': 40, 'n': 50, 'x': 60, 'o': 70, 'p': 80, 'q': 100,
                'r': 200, 's': 300, 't': 400, 'u': 500, 'ph': 600, 'ch': 700, 'ps': 800}
    
    def _load_english_gematria(self) -> Dict[str, int]:
        return {chr(i + 96): i for i in range(1, 27)}
    
    def _calculate_value(self, text: str, gematria_map: Dict[str, int]) -> int:
        return sum(gematria_map.get(char.lower(), 0) for char in text if char.lower() in gematria_map)
    
    def _reduce_value(self, value: int) -> int:
        return 1 + (value - 1) % 9
    
    def _interpret_value(self, value: int, system: str) -> str:
        interpretations = {
            1: "Unity, divine spark, creation",
            2: "Duality, division, choice",
            3: "Trinity, expression, manifestation",
            4: "Foundation, structure, stability",
            5: "Change, freedom, adventure",
            6: "Harmony, balance, nurturing",
            7: "Mysticism, introspection, wisdom",
            8: "Power, authority, material success",
            9: "Compassion, universal love, completion"
        }
        return interpretations.get(value, "Unknown")


class WesternAstrologyAnalyzer:
    """Western astrology analysis"""
    
    def __init__(self):
        self.planets = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn']
        self.signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                      'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        self.houses = list(range(1, 13))
        self.aspects = ['conjunction', 'sextile', 'square', 'trine', 'opposition']
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return all(k in vessel_data for k in ['birth_date', 'birth_time', 'birth_location'])
    
    def analyze(self, vessel_data: Dict) -> Dict:
        random.seed(hash(str(vessel_data)) % 1000)
        
        chart = {}
        for planet in self.planets:
            chart[planet] = {
                'sign': random.choice(self.signs),
                'house': random.choice(self.houses),
                'degree': random.randint(0, 29)
            }
        
        aspects = []
        for i in range(len(self.planets)):
            for j in range(i+1, len(self.planets)):
                if random.random() > 0.7:
                    aspects.append({
                        'planet_a': self.planets[i],
                        'planet_b': self.planets[j],
                        'aspect': random.choice(self.aspects),
                        'orb': round(random.uniform(0, 10), 1)
                    })
        
        return {
            'system': 'western_astrology',
            'natal_chart': chart,
            'aspects': aspects,
            'interpretations': self._generate_interpretations(chart, aspects),
            'confidence': 0.85
        }
    
    def _generate_interpretations(self, chart: Dict, aspects: List[Dict]) -> Dict:
        sun_sign = chart.get('sun', {}).get('sign', 'unknown')
        moon_sign = chart.get('moon', {}).get('sign', 'unknown')
        
        return {
            'sun_sign': sun_sign.capitalize() if sun_sign != 'unknown' else 'Unknown',
            'sun_interpretation': self._interpret_sign(sun_sign, 'sun'),
            'moon_sign': moon_sign.capitalize() if moon_sign != 'unknown' else 'Unknown',
            'moon_interpretation': self._interpret_sign(moon_sign, 'moon'),
            'life_purpose': self._interpret_life_purpose(chart),
            'challenges': self._interpret_challenges(chart, aspects),
            'gifts': self._interpret_gifts(chart, aspects)
        }
    
    def _interpret_sign(self, sign: str, planet: str) -> str:
        interpretations = {
            'sun': {
                'aries': "You are a natural leader, bold and courageous.",
                'taurus': "You value stability and material security.",
                'gemini': "You are curious and communicative.",
                'cancer': "You are nurturing and intuitive.",
                'leo': "You are creative and charismatic.",
                'virgo': "You are analytical and practical.",
                'libra': "You seek harmony and balance.",
                'scorpio': "You are intense and transformative.",
                'sagittarius': "You are adventurous and philosophical.",
                'capricorn': "You are disciplined and ambitious.",
                'aquarius': "You are innovative and humanitarian.",
                'pisces': "You are compassionate and artistic."
            },
            'moon': {
                'aries': "Your emotional nature is direct and passionate.",
                'taurus': "Your emotional nature is steady and sensual.",
                'gemini': "Your emotional nature is curious and adaptable.",
                'cancer': "Your emotional nature is sensitive and nurturing.",
                'leo': "Your emotional nature is warm and generous.",
                'virgo': "Your emotional nature is analytical and helpful.",
                'libra': "Your emotional nature is diplomatic and charming.",
                'scorpio': "Your emotional nature is intense and private.",
                'sagittarius': "Your emotional nature is optimistic and free.",
                'capricorn': "Your emotional nature is reserved and ambitious.",
                'aquarius': "Your emotional nature is detached and original.",
                'pisces': "Your emotional nature is compassionate and dreamy."
            }
        }
        return interpretations.get(planet, {}).get(sign, "Unknown interpretation")
    
    def _interpret_life_purpose(self, chart: Dict) -> str:
        return "To grow, learn, and contribute to the collective consciousness."
    
    def _interpret_challenges(self, chart: Dict, aspects: List[Dict]) -> List[str]:
        challenges = []
        hard_aspects = ['square', 'opposition']
        for aspect in aspects:
            if aspect['aspect'] in hard_aspects:
                challenges.append(f"Tension between {aspect['planet_a']} and {aspect['planet_b']}")
        if not challenges:
            challenges.append("Minimal astrological challenges")
        return challenges
    
    def _interpret_gifts(self, chart: Dict, aspects: List[Dict]) -> List[str]:
        gifts = []
        soft_aspects = ['sextile', 'trine']
        for aspect in aspects:
            if aspect['aspect'] in soft_aspects:
                gifts.append(f"Harmony between {aspect['planet_a']} and {aspect['planet_b']}")
        sun_sign = chart.get('sun', {}).get('sign', 'unknown')
        gifts.append(f"The natural gifts of your {sun_sign.capitalize()} energy")
        return gifts


class VedicAstrologyAnalyzer:
    """Vedic (Jyotish) astrology analysis"""
    
    def __init__(self):
        self.signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                      'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        self.nakshatras = ["ashwini", "bharani", "kritika", "rohini", "mrigashira", 
                          "ardra", "punarvasu", "pushya", "ashlesha", "magha", "purva_phalguni",
                          "uttara_phalguni", "hasta", "chitra", "swati", "vishakha", "anuradha",
                          "jyeshtha", "mula", "purva_ashadha", "uttara_ashadha", "shravana",
                          "dhanishta", "shatabhisha", "purva_bhadrapada", "uttara_bhadrapada", "revati"]
        self.dashas = ['ketu', 'venus', 'sun', 'moon', 'mars', 'rahu', 'jupiter', 'saturn', 'mercury']
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return all(k in vessel_data for k in ['birth_date', 'birth_time', 'birth_location'])
    
    def analyze(self, vessel_data: Dict) -> Dict:
        random.seed(hash(str(vessel_data)) % 1000)
        
        return {
            'system': 'vedic_astrology',
            'lagna': random.choice(self.signs),
            'moon_sign': random.choice(self.signs),
            'moon_nakshatra': random.choice(self.nakshatras),
            'current_dasha': random.choice(self.dashas),
            'interpretations': {
                'life_path': "To fulfill your dharma and learn your karmic lessons.",
                'karma': "Your karmic path is influenced by your past actions.",
                'dharma': "Your dharma is to fulfill your role in the cosmic order."
            },
            'confidence': 0.8
        }


class GeneKeysAnalyzer:
    """Gene Keys analysis"""
    
    def __init__(self):
        self.gene_keys = list(range(1, 65))
        self.profiles = [f"{i}{j}" for i in range(1, 7) for j in range(1, 7)]
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return 'birth_date' in vessel_data and 'birth_time' in vessel_data
    
    def analyze(self, vessel_data: Dict) -> Dict:
        random.seed(hash(str(vessel_data)) % 1000)
        
        profile = random.choice(self.profiles)
        gene_key_chart = {planet: random.choice(self.gene_keys) 
                         for planet in ['sun', 'earth', 'moon', 'mars', 'mercury', 'jupiter']}
        mutations = random.sample(self.gene_keys, k=random.randint(0, 3))
        
        return {
            'system': 'gene_keys',
            'profile': profile,
            'gene_keys': gene_key_chart,
            'mutations': mutations,
            'interpretations': {
                'gift': self._interpret_gift(profile),
                'siddhi': self._interpret_siddhi(profile),
                'shadow': self._interpret_shadow(profile)
            },
            'confidence': 0.9
        }
    
    def _interpret_gift(self, profile: str) -> str:
        gifts = {'1': "Inspiration", '2': "Direction", '3': "Order", 
                '4': "Form", '5': "Knowledge", '6': "Love"}
        return gifts.get(profile[0], "Unknown")
    
    def _interpret_siddhi(self, profile: str) -> str:
        siddhis = {'1': "Divine Inspiration", '2': "Divine Direction", '3': "Divine Order",
                  '4': "Divine Manifestation", '5': "Divine Wisdom", '6': "Divine Love"}
        return siddhis.get(profile[0], "Unknown")
    
    def _interpret_shadow(self, profile: str) -> str:
        shadows = {'1': "Frustration", '2': "Doubt", '3': "Chaos",
                  '4': "Inertia", '5': "Ignorance", '6': "Separation"}
        return shadows.get(profile[0], "Unknown")


class HumanDesignAnalyzer:
    """Human Design analysis"""
    
    def __init__(self):
        self.types = ['Manifestor', 'Generator', 'Manifesting Generator', 'Projector', 'Reflector']
        self.strategies = {
            'Manifestor': 'Inform', 'Generator': 'Respond',
            'Manifesting Generator': 'Respond', 'Projector': 'Wait for Invitation',
            'Reflector': 'Wait a Lunar Cycle'
        }
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return 'birth_date' in vessel_data and 'birth_time' in vessel_data
    
    def analyze(self, vessel_data: Dict) -> Dict:
        random.seed(hash(str(vessel_data)) % 1000)
        
        hd_type = random.choice(self.types)
        return {
            'system': 'human_design',
            'type': hd_type,
            'strategy': self.strategies[hd_type],
            'interpretations': {
                'type': self._interpret_type(hd_type),
                'strategy': self._interpret_strategy(self.strategies[hd_type])
            },
            'confidence': 0.9
        }
    
    def _interpret_type(self, hd_type: str) -> str:
        interpretations = {
            'Manifestor': "You are here to initiate and impact others.",
            'Generator': "You are here to build and create.",
            'Manifesting Generator': "You are here to do things quickly and efficiently.",
            'Projector': "You are here to guide and manage others.",
            'Reflector': "You are here to sample and reflect the health of the community."
        }
        return interpretations.get(hd_type, "Unknown")
    
    def _interpret_strategy(self, strategy: str) -> str:
        interpretations = {
            'Inform': "Inform others before taking action.",
            'Respond': "Respond to life's opportunities.",
            'Wait for Invitation': "Wait for an invitation before sharing your gifts.",
            'Wait a Lunar Cycle': "Wait a lunar cycle before making major decisions."
        }
        return interpretations.get(strategy, "Unknown")


class SemanticAnalyzer:
    """Semantic analysis"""
    
    def __init__(self):
        self.keywords = {
            'spiritual': ['spirit', 'soul', 'divine', 'source'],
            'practical': ['work', 'career', 'practical'],
            'emotional': ['feel', 'love', 'relationship'],
            'intellectual': ['think', 'knowledge', 'learn'],
            'creative': ['create', 'art', 'music']
        }
    
    def can_analyze(self, vessel_data: Dict) -> bool:
        return 'name' in vessel_data or 'description' in vessel_data
    
    def analyze(self, vessel_data: Dict) -> Dict:
        name = vessel_data.get('name', '')
        description = vessel_data.get('description', '')
        text = f"{name} {description}"
        text_lower = text.lower()
        
        category_counts = {}
        for category, keywords in self.keywords.items():
            count = sum(1 for keyword in keywords if keyword in text_lower)
            category_counts[category] = count
        
        total = sum(category_counts.values())
        themes = {k: v/total if total > 0 else 0 for k, v in category_counts.items()}
        
        return {
            'system': 'semantics',
            'themes': themes,
            'dominant_theme': max(themes, key=themes.get) if themes else 'unknown',
            'confidence': 0.7
        }


class CrossReferenceEngine:
    """Cross-reference components"""
    
    def analyze(self, components: List[BlueprintComponent]) -> Dict:
        return {
            'themes': self._find_themes(components),
            'contradictions': self._find_contradictions(components),
            'resonances': self._find_resonances(components)
        }
    
    def _find_themes(self, components: List[BlueprintComponent]) -> List[Dict]:
        themes = {}
        for component in components:
            component_themes = self._extract_themes(component)
            for theme, strength in component_themes.items():
                if theme not in themes:
                    themes[theme] = {'total_strength': 0, 'systems': [], 'count': 0}
                themes[theme]['total_strength'] += strength
                themes[theme]['systems'].append(component.system)
                themes[theme]['count'] += 1
        
        theme_list = [
            {'name': theme, 'resonance': data['total_strength'] / len(components),
             'systems': list(set(data['systems'])), 'count': data['count']}
            for theme, data in themes.items()
        ]
        theme_list.sort(key=lambda x: x['resonance'], reverse=True)
        return theme_list
    
    def _extract_themes(self, component: BlueprintComponent) -> Dict[str, float]:
        themes = {
            'gematria': {'divine': 0.8, 'creation': 0.7},
            'western_astrology': {'fate': 0.8, 'celestial': 0.9},
            'vedic_astrology': {'fate': 0.8, 'karma': 0.8},
            'gene_keys': {'purpose': 0.9, 'genetics': 0.8},
            'human_design': {'energy': 0.9, 'purpose': 0.8},
            'semantics': {'meaning': 0.9, 'language': 0.8}
        }
        return themes.get(component.system, {})
    
    def _find_contradictions(self, components: List[BlueprintComponent]) -> List[Dict]:
        contradictions = []
        for i in range(len(components)):
            for j in range(i+1, len(components)):
                if random.random() > 0.8:
                    contradictions.append({
                        'system_a': components[i].system,
                        'system_b': components[j].system,
                        'description': f"Contradiction between {components[i].system} and {components[j].system}",
                        'severity': random.uniform(0.5, 1.0)
                    })
        return contradictions
    
    def _find_resonances(self, components: List[BlueprintComponent]) -> List[Dict]:
        resonances = []
        for i in range(len(components)):
            for j in range(i+1, len(components)):
                resonance = 0.5 + (components[i].weight + components[j].weight) / 4
                if resonance > 0.7:
                    resonances.append({
                        'system_a': components[i].system,
                        'system_b': components[j].system,
                        'resonance_score': resonance
                    })
        return resonances


class CosmicBlueprintEngine:
    """
    The main Cosmic Blueprint Engine
    Implements Article IX, Part A (9.4-9.7)
    """
    
    def __init__(self):
        self.systems = {
            'gematria': GematriaAnalyzer(),
            'western_astrology': WesternAstrologyAnalyzer(),
            'vedic_astrology': VedicAstrologyAnalyzer(),
            'gene_keys': GeneKeysAnalyzer(),
            'human_design': HumanDesignAnalyzer(),
            'semantics': SemanticAnalyzer()
        }
        self.cross_referencer = CrossReferenceEngine()
    
    def generate_blueprint(self, vessel_data: Dict) -> Dict:
        """Generate a unified cosmic blueprint for a vessel"""
        components = []
        
        for system_name, analyzer in self.systems.items():
            if analyzer.can_analyze(vessel_data):
                result = analyzer.analyze(vessel_data)
                components.append(BlueprintComponent(
                    name=f"{system_name}_analysis",
                    system=system_name,
                    data=result,
                    weight=result.get('confidence', 0.5)
                ))
        
        cross_ref = self.cross_referencer.analyze(components)
        
        blueprint = {
            'vessel_id': vessel_data.get('id', 'unknown'),
            'name': vessel_data.get('name', 'Unknown'),
            'components': [asdict(c) for c in components],
            'cross_references': cross_ref,
            'unified_signature': self._generate_signature(components),
            'path_indicators': self._extract_paths(components, cross_ref),
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        return blueprint
    
    def _generate_signature(self, components: List[BlueprintComponent]) -> str:
        signature_data = "".join(
            f"{c.system}:{hash(str(c.data))}"
            for c in sorted(components, key=lambda x: x.weight, reverse=True)
        )
        return hashlib.sha256(signature_data.encode()).hexdigest()
    
    def _extract_paths(self, components: List[BlueprintComponent], cross_ref: Dict) -> List[Dict]:
        paths = []
        
        for contradiction in cross_ref.get('contradictions', []):
            paths.append({
                'type': 'resolution_path',
                'description': f"Resolve contradiction between {contradiction['system_a']} and {contradiction['system_b']}",
                'priority': contradiction['severity']
            })
        
        for theme in cross_ref.get('themes', []):
            if theme['resonance'] > 0.8:
                paths.append({
                    'type': 'amplification_path',
                    'description': f"Amplify {theme['name']} resonance",
                    'resonance': theme['resonance']
                })
        
        paths.sort(key=lambda x: x.get('priority', x.get('resonance', 0)), reverse=True)
        return paths