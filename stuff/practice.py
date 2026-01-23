"""
Sistema Avanzado de Análisis de Texto con Procesamiento Concurrente
Demuestra: decoradores, context managers, generators, async/await, metaclases,
descriptores, threading, dataclasses, y patrones de diseño
"""

import asyncio
import time
import re
import math
import json
from typing import Dict, List, Tuple, Generator, Callable, Any, Optional, Union
from dataclasses import dataclass, field, asdict
from functools import wraps, lru_cache, cached_property, partial, reduce
from collections import Counter, defaultdict, ChainMap
from concurrent.futures import ThreadPoolExecutor, as_completed
import statistics
from abc import ABC, abstractmethod
from enum import Enum, auto
from pathlib import Path
import hashlib


# ============= ENUMERACIONES =============

class ComplexityLevel(Enum):
    """Niveles de complejidad del texto"""
    SIMPLE = auto()
    MEDIUM = auto()
    COMPLEX = auto()
    ADVANCED = auto()


class AnalysisType(Enum):
    """Tipos de análisis disponibles"""
    FREQUENCY = auto()
    SENTIMENT = auto()
    STRUCTURAL = auto()
    READABILITY = auto()
    STATISTICAL = auto()


# ============= DECORADORES AVANZADOS =============

def timing_decorator(func: Callable) -> Callable:
    """Decorador que mide el tiempo de ejecución"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  {func.__name__} ejecutado en {end - start:.4f} segundos")
        return result
    return wrapper


def cache_results(max_size: int = 100):
    """Decorador de caché con límite de tamaño"""
    def decorator(func: Callable) -> Callable:
        cache = {}
        cache_order = []
        
        @wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]
            
            result = func(*args)
            
            if len(cache) >= max_size:
                oldest = cache_order.pop(0)
                del cache[oldest]
            
            cache[args] = result
            cache_order.append(args)
            return result
        
        wrapper.cache = cache
        wrapper.clear_cache = lambda: (cache.clear(), cache_order.clear())
        return wrapper
    return decorator


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorador que reintenta la función en caso de error"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"⚠️  Intento {attempt + 1} falló: {e}. Reintentando...")
                    time.sleep(delay)
        return wrapper
    return decorator


def log_execution(func: Callable) -> Callable:
    """Decorador que registra la ejecución de funciones"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Ejecutando: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✓  {func.__name__} completado")
        return result
    return wrapper


def memoize_with_expiry(expiry_seconds: int = 60):
    """Decorador de memoization con expiración temporal"""
    def decorator(func: Callable) -> Callable:
        cache = {}
        
        @wraps(func)
        def wrapper(*args):
            current_time = time.time()
            cache_key = args
            
            if cache_key in cache:
                result, timestamp = cache[cache_key]
                if current_time - timestamp < expiry_seconds:
                    return result
            
            result = func(*args)
            cache[cache_key] = (result, current_time)
            return result
        
        wrapper.cache = cache
        return wrapper
    return decorator


# ============= DESCRIPTOR PATTERN =============

class ValidatedString:
    """Descriptor que valida strings"""
    def __init__(self, min_length: int = 0, max_length: int = 1000):
        self.min_length = min_length
        self.max_length = max_length
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, '')
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected string, got {type(value)}")
        if not self.min_length <= len(value) <= self.max_length:
            raise ValueError(f"String length must be between {self.min_length} and {self.max_length}")
        setattr(obj, self.name, value)


class PositiveNumber:
    """Descriptor que valida números positivos"""
    def __init__(self, default: float = 0.0):
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, self.default)
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number, got {type(value)}")
        if value < 0:
            raise ValueError(f"Value must be positive, got {value}")
        setattr(obj, self.name, value)


# ============= CONTEXT MANAGER =============

class TextAnalysisContext:
    """Context manager para análisis de texto con recursos"""
    def __init__(self, name: str):
        self.name = name
        self.start_time = None
        
    def __enter__(self):
        self.start_time = time.time()
        print(f"\n🔍 Iniciando análisis: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        print(f"✅ Análisis completado en {duration:.2f}s")
        if exc_type:
            print(f"❌ Error: {exc_val}")
        return False


# ============= DATACLASSES =============

@dataclass
class TextStatistics:
    """
    Estadísticas de texto.
    
    Attributes:
        total_words: Número total de palabras en el texto
        total_chars: Número total de caracteres incluyendo espacios
        unique_words: Cantidad de palabras únicas (sin repetición)
        avg_word_length: Longitud promedio de las palabras
        most_common: Lista de tuplas (palabra, frecuencia) más comunes
        sentiment_score: Puntuación de sentimiento (-100 a 100)
        readability_score: Puntuación de legibilidad (0-100, Flesch Reading Ease)
        complexity_level: Nivel de complejidad del texto
        lexical_diversity: Ratio de palabras únicas sobre palabras totales (0-1)
        sentence_count: Número de oraciones en el texto
        text_hash: Hash MD5 del texto (8 caracteres)
    """
    total_words: int = 0
    total_chars: int = 0
    unique_words: int = 0
    avg_word_length: float = 0.0
    most_common: List[Tuple[str, int]] = field(default_factory=list)
    sentiment_score: float = 0.0
    readability_score: float = 0.0
    complexity_level: ComplexityLevel = ComplexityLevel.MEDIUM
    lexical_diversity: float = 0.0
    sentence_count: int = 0
    text_hash: str = ""
    
    def __post_init__(self):
        """Valida los datos después de la inicialización"""
        if self.total_words < 0:
            raise ValueError("total_words debe ser no negativo")
        if self.lexical_diversity < 0 or self.lexical_diversity > 1:
            raise ValueError("lexical_diversity debe estar entre 0 y 1")
    
    def __str__(self) -> str:
        return f"""
📊 Estadísticas del Texto:
   - Palabras totales: {self.total_words}
   - Caracteres: {self.total_chars}
   - Palabras únicas: {self.unique_words}
   - Diversidad léxica: {self.lexical_diversity:.2%}
   - Longitud promedio: {self.avg_word_length:.2f}
   - Score de sentimiento: {self.sentiment_score:.2f}
   - Legibilidad: {self.readability_score:.2f}
   - Complejidad: {self.complexity_level.name}
   - Oraciones: {self.sentence_count}
   - Palabras más comunes: {', '.join(f'{w}({c})' for w, c in self.most_common[:5])}
"""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario"""
        data = asdict(self)
        data['complexity_level'] = self.complexity_level.name
        return data
    
    def to_json(self) -> str:
        """Convierte a JSON"""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)


# ============= STRATEGY PATTERN CON ABC =============

class AnalysisStrategy(ABC):
    """Estrategia abstracta de análisis"""
    @abstractmethod
    def analyze(self, text: str) -> Dict[str, Any]:
        pass


class FrequencyAnalysis(AnalysisStrategy):
    """Análisis de frecuencia de palabras"""
    def analyze(self, text: str) -> Dict[str, Any]:
        words = re.findall(r'\b\w+\b', text.lower())
        return {
            'word_count': Counter(words),
            'total_words': len(words),
            'unique_words': len(set(words))
        }


class SentimentAnalysis(AnalysisStrategy):
    """
    Análisis de sentimiento mejorado con categorías emocionales.
    Detecta emociones específicas más allá de positivo/negativo.
    """
    POSITIVE_WORDS = {
        'bueno', 'excelente', 'genial', 'increíble', 'feliz', 'amor', 'perfecto',
        'fantástico', 'maravilloso', 'espectacular', 'estupendo', 'brillante',
        'positivo', 'alegre', 'exitoso', 'éxito', 'victoria', 'ganar'
    }
    NEGATIVE_WORDS = {
        'malo', 'terrible', 'horrible', 'triste', 'odio', 'error', 'problema',
        'pésimo', 'deficiente', 'fracaso', 'negativo', 'desastre', 'fallo',
        'inútil', 'difícil', 'complicado', 'preocupante', 'crisis'
    }
    ENTHUSIASM_WORDS = {
        'increíble', 'asombroso', 'impresionante', 'wow', 'guau', 'genial',
        'extraordinario', 'fascinante', 'emocionante'
    }
    NEUTRAL_WORDS = {
        'normal', 'regular', 'estándar', 'común', 'típico', 'habitual'
    }
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """Analiza el sentimiento y emociones del texto"""
        words = set(re.findall(r'\b\w+\b', text.lower()))
        
        if not words:
            return {
                'sentiment_score': 0.0,
                'positive_words': 0,
                'negative_words': 0,
                'enthusiasm_level': 0,
                'neutrality': 0,
                'emotion': 'neutral'
            }
        
        positive = len(words & self.POSITIVE_WORDS)
        negative = len(words & self.NEGATIVE_WORDS)
        enthusiasm = len(words & self.ENTHUSIASM_WORDS)
        neutral = len(words & self.NEUTRAL_WORDS)
        
        # Calcular score ponderado
        score = ((positive * 1.5 + enthusiasm * 2) - (negative * 1.5)) / max(len(words), 1) * 100
        
        # Determinar emoción dominante
        if enthusiasm > 1:
            emotion = 'entusiasta'
        elif positive > negative:
            emotion = 'positivo'
        elif negative > positive:
            emotion = 'negativo'
        else:
            emotion = 'neutral'
        
        return {
            'sentiment_score': round(score, 2),
            'positive_words': positive,
            'negative_words': negative,
            'enthusiasm_level': enthusiasm,
            'neutrality': neutral,
            'emotion': emotion
        }


class StructuralAnalysis(AnalysisStrategy):
    """Análisis estructural del texto"""
    def analyze(self, text: str) -> Dict[str, Any]:
        sentences = re.split(r'[.!?]+', text)
        paragraphs = text.split('\n\n')
        
        return {
            'sentence_count': len([s for s in sentences if s.strip()]),
            'paragraph_count': len([p for p in paragraphs if p.strip()]),
            'avg_sentence_length': statistics.mean([len(s.split()) for s in sentences if s.strip()] or [0])
        }


class ReadabilityAnalysis(AnalysisStrategy):
    """Análisis de legibilidad (índice Flesch simplificado)"""
    def analyze(self, text: str) -> Dict[str, Any]:
        words = re.findall(r'\b\w+\b', text)
        sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
        syllables = sum(self._count_syllables(word) for word in words)
        
        if not sentences or not words:
            return {'readability_score': 0.0, 'complexity_level': ComplexityLevel.SIMPLE}
        
        avg_words_per_sentence = len(words) / len(sentences)
        avg_syllables_per_word = syllables / len(words)
        
        # Fórmula Flesch Reading Ease simplificada
        score = 206.835 - 1.015 * avg_words_per_sentence - 84.6 * avg_syllables_per_word
        score = max(0, min(100, score))  # Limitar entre 0-100
        
        # Determinar nivel de complejidad
        if score >= 80:
            complexity = ComplexityLevel.SIMPLE
        elif score >= 60:
            complexity = ComplexityLevel.MEDIUM
        elif score >= 40:
            complexity = ComplexityLevel.COMPLEX
        else:
            complexity = ComplexityLevel.ADVANCED
        
        return {
            'readability_score': score,
            'complexity_level': complexity,
            'avg_syllables_per_word': avg_syllables_per_word,
            'avg_words_per_sentence': avg_words_per_sentence
        }
    
    def _count_syllables(self, word: str) -> int:
        """Cuenta sílabas (aproximación simple)"""
        word = word.lower()
        vowels = 'aeiouáéíóúü'
        count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                count += 1
            previous_was_vowel = is_vowel
        
        return max(1, count)


class StatisticalAnalysis(AnalysisStrategy):
    """Análisis estadístico avanzado"""
    def analyze(self, text: str) -> Dict[str, Any]:
        words = re.findall(r'\b\w+\b', text)
        word_lengths = [len(w) for w in words]
        
        if not word_lengths:
            return {}
        
        return {
            'median_word_length': statistics.median(word_lengths),
            'mode_word_length': statistics.mode(word_lengths) if word_lengths else 0,
            'stdev_word_length': statistics.stdev(word_lengths) if len(word_lengths) > 1 else 0,
            'min_word_length': min(word_lengths),
            'max_word_length': max(word_lengths),
            'lexical_diversity': len(set(words)) / len(words) if words else 0
        }


class KeywordAnalysis(AnalysisStrategy):
    """
    Análisis de palabras clave usando TF-IDF simplificado.
    Identifica las palabras más importantes del texto.
    """
    # Palabras vacías comunes en español
    STOP_WORDS = {
        'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se', 'no', 'haber',
        'por', 'con', 'su', 'para', 'como', 'estar', 'tener', 'le', 'lo', 'todo',
        'pero', 'más', 'hacer', 'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese',
        'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él', 'muy', 'sin',
        'vez', 'mucho', 'saber', 'qué', 'sobre', 'mi', 'alguno', 'mismo', 'yo',
        'también', 'hasta', 'año', 'dos', 'querer', 'entre', 'así', 'primero',
        'desde', 'grande', 'eso', 'ni', 'nos', 'llegar', 'pasar', 'tiempo'
    }
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """Extrae palabras clave del texto"""
        words = [w.lower() for w in re.findall(r'\b\w+\b', text)]
        
        # Filtrar palabras vacías y palabras cortas
        keywords = [w for w in words if w not in self.STOP_WORDS and len(w) > 3]
        
        if not keywords:
            return {'keywords': [], 'keyword_density': 0.0}
        
        # Calcular frecuencias
        keyword_freq = Counter(keywords)
        total_keywords = len(keywords)
        
        # Palabras clave con su densidad
        top_keywords = [
            (word, count, count / total_keywords * 100) 
            for word, count in keyword_freq.most_common(10)
        ]
        
        return {
            'keywords': top_keywords,
            'keyword_density': len(keywords) / len(words) * 100 if words else 0,
            'unique_keywords': len(set(keywords))
        }


# ============= GENERADORES =============

def word_generator(text: str) -> Generator[str, None, None]:
    """
    Generador lazy de palabras optimizado.
    
    Args:
        text: Texto del cual extraer palabras
        
    Yields:
        Palabras individuales en minúsculas
        
    Example:
        >>> list(word_generator("Hola Mundo"))
        ['hola', 'mundo']
    """
    if not text:
        return
    
    for word in re.finditer(r'\b\w+\b', text.lower()):
        word_text = word.group()
        # Filtrar palabras de un solo carácter si son números
        if len(word_text) > 1 or not word_text.isdigit():
            yield word_text


def ngram_generator(text: str, n: int = 2) -> Generator[Tuple[str, ...], None, None]:
    """Generador de n-gramas"""
    words = list(word_generator(text))
    for i in range(len(words) - n + 1):
        yield tuple(words[i:i + n])


def sliding_window(iterable, window_size: int = 3) -> Generator[List, None, None]:
    """Generador de ventana deslizante"""
    from collections import deque
    window = deque(maxlen=window_size)
    
    for item in iterable:
        window.append(item)
        if len(window) == window_size:
            yield list(window)


# ============= OBSERVER PATTERN =============

class AnalysisObserver(ABC):
    """Observador abstracto para análisis"""
    @abstractmethod
    def update(self, event_type: str, data: Any):
        pass


class ConsoleObserver(AnalysisObserver):
    """Observador que imprime en consola"""
    def update(self, event_type: str, data: Any):
        print(f"🔔 Evento: {event_type} | Datos: {data}")


class StatisticsObserver(AnalysisObserver):
    """Observador que recolecta estadísticas"""
    def __init__(self):
        self.events: List[Tuple[str, Any]] = []
    
    def update(self, event_type: str, data: Any):
        self.events.append((event_type, data))
    
    def get_summary(self) -> Dict[str, int]:
        return Counter(event for event, _ in self.events)


class Observable:
    """Clase observable que notifica a observadores"""
    def __init__(self):
        self._observers: List[AnalysisObserver] = []
    
    def attach(self, observer: AnalysisObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: AnalysisObserver):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_type: str, data: Any):
        for observer in self._observers:
            observer.update(event_type, data)


# ============= CHAIN OF RESPONSIBILITY PATTERN =============

class TextHandler(ABC):
    """Handler abstracto para cadena de responsabilidad"""
    def __init__(self):
        self._next_handler: Optional[TextHandler] = None
    
    def set_next(self, handler: 'TextHandler') -> 'TextHandler':
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, text: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(text)
        return text


class CleanSpacesHandler(TextHandler):
    """Limpia espacios múltiples"""
    def handle(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text).strip()
        return super().handle(text)


class RemoveSpecialCharsHandler(TextHandler):
    """Remueve caracteres especiales"""
    def handle(self, text: str) -> str:
        text = re.sub(r'[^\w\s.!?,;-]', '', text)
        return super().handle(text)


class LowercaseHandler(TextHandler):
    """Convierte a minúsculas"""
    def handle(self, text: str) -> str:
        text = text.lower()
        return super().handle(text)


# ============= CLASE PRINCIPAL CON METACLASE =============

class SingletonMeta(type):
    """Metaclase Singleton"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TextAnalyzer(Observable, metaclass=SingletonMeta):
    """Analizador de texto avanzado (Singleton + Observable)"""
    
    name = ValidatedString(min_length=1, max_length=100)
    analysis_count = PositiveNumber(default=0)
    
    def __init__(self, name: str = "Analizador Principal"):
        Observable.__init__(self)
        self.name = name
        self.strategies: List[AnalysisStrategy] = []
        self.results_cache = {}
        self._texts_analyzed: List[str] = []
        self.analysis_count = 0
    
    def add_strategy(self, strategy: AnalysisStrategy):
        """Añade una estrategia de análisis"""
        self.strategies.append(strategy)
        return self
    
    @property
    def total_analyses(self) -> int:
        """Número total de análisis realizados"""
        return int(self.analysis_count)
    
    @cached_property
    def supported_analyses(self) -> List[str]:
        """Lista de análisis soportados"""
        return ['frequency', 'sentiment', 'structural', 'readability', 'statistical']
    
    def __len__(self) -> int:
        """Longitud = número de textos analizados"""
        return len(self._texts_analyzed)
    
    def __getitem__(self, index: int) -> str:
        """Acceso a textos analizados por índice"""
        return self._texts_analyzed[index]
    
    def __iter__(self):
        """Iterador sobre textos analizados"""
        return iter(self._texts_analyzed)
    
    def __contains__(self, text: str) -> bool:
        """Verifica si un texto ya fue analizado"""
        return text in self._texts_analyzed
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas sobre el caché de resultados.
        
        Returns:
            Diccionario con información del caché
        """
        cache = getattr(self.analyze_text, 'cache', {})
        return {
            'cache_size': len(cache),
            'texts_analyzed': len(self._texts_analyzed),
            'total_analyses': self.total_analyses,
            'cache_hit_potential': f"{len(cache) / max(self.total_analyses, 1) * 100:.1f}%"
        }
    
    @timing_decorator
    @cache_results(max_size=50)
    def analyze_text(self, text: str) -> TextStatistics:
        """
        Análisis completo del texto.
        
        Args:
            text: El texto a analizar
            
        Returns:
            TextStatistics con las estadísticas completas del texto
            
        Raises:
            ValueError: Si el texto está vacío o es None
        """
        if not text or not text.strip():
            raise ValueError("El texto no puede estar vacío")
        
        self.notify('analysis_started', {'text_length': len(text)})
        
        words = list(word_generator(text))
        
        # Análisis de frecuencia
        freq_result = FrequencyAnalysis().analyze(text)
        word_count = freq_result['word_count']
        
        # Análisis de sentimiento
        sentiment_result = SentimentAnalysis().analyze(text)
        
        # Análisis estructural
        structural_result = StructuralAnalysis().analyze(text)
        
        # Análisis de legibilidad
        readability_result = ReadabilityAnalysis().analyze(text)
        
        # Análisis estadístico
        statistical_result = StatisticalAnalysis().analyze(text)
        
        # Análisis de palabras clave
        keyword_result = KeywordAnalysis().analyze(text)
        
        # Calcular hash del texto
        text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
        
        # Calcular longitud promedio
        avg_length = statistics.mean([len(w) for w in words]) if words else 0
        
        # Registrar análisis
        self._texts_analyzed.append(text[:50] + '...' if len(text) > 50 else text)
        self.analysis_count += 1
        
        stats = TextStatistics(
            total_words=len(words),
            total_chars=len(text),
            unique_words=len(set(words)),
            avg_word_length=avg_length,
            most_common=word_count.most_common(10),
            sentiment_score=sentiment_result['sentiment_score'],
            readability_score=readability_result.get('readability_score', 0.0),
            complexity_level=readability_result.get('complexity_level', ComplexityLevel.MEDIUM),
            lexical_diversity=statistical_result.get('lexical_diversity', 0.0),
            sentence_count=structural_result.get('sentence_count', 0),
            text_hash=text_hash
        )
        
        self.notify('analysis_completed', {'stats': stats.to_dict()})
        return stats
    
    async def analyze_async(self, texts: List[str]) -> List[TextStatistics]:
        """Análisis asíncrono de múltiples textos"""
        async def analyze_one(text: str) -> TextStatistics:
            await asyncio.sleep(0.1)  # Simula operación I/O
            return self.analyze_text(text)
        
        tasks = [analyze_one(text) for text in texts]
        return await asyncio.gather(*tasks)
    
    def parallel_analysis(self, texts: List[str], max_workers: int = 4) -> List[TextStatistics]:
        """Análisis paralelo usando ThreadPool"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.analyze_text, texts))
        return results
    
    def find_patterns(self, text: str, pattern: str) -> List[str]:
        """Encuentra patrones usando regex"""
        return re.findall(pattern, text, re.IGNORECASE)
    
    def generate_ngrams(self, text: str, n: int = 2) -> Counter:
        """Genera estadísticas de n-gramas"""
        ngrams = list(ngram_generator(text, n))
        return Counter(ngrams)
    
    def preprocess_text(self, text: str, lowercase: bool = True, 
                       remove_special: bool = True) -> str:
        """Preprocesa texto usando Chain of Responsibility"""
        handler = CleanSpacesHandler()
        
        if remove_special:
            handler.set_next(RemoveSpecialCharsHandler())
        
        if lowercase:
            current = handler
            while current._next_handler:
                current = current._next_handler
            current.set_next(LowercaseHandler())
        
        return handler.handle(text)
    
    def compare_texts(self, text1: str, text2: str) -> Dict[str, Any]:
        """Compara dos textos"""
        stats1 = self.analyze_text(text1)
        stats2 = self.analyze_text(text2)
        
        return {
            'similarity_score': self._calculate_similarity(text1, text2),
            'word_diff': stats1.total_words - stats2.total_words,
            'sentiment_diff': stats1.sentiment_score - stats2.sentiment_score,
            'readability_diff': stats1.readability_score - stats2.readability_score
        }
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calcula similitud usando Jaccard"""
        words1 = set(word_generator(text1))
        words2 = set(word_generator(text2))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1 & words2)
        union = len(words1 | words2)
        
        return intersection / union if union > 0 else 0.0
    
    def export_results(self, filepath: Union[str, Path], format: str = 'json') -> None:
        """
        Exporta resultados a archivo.
        
        Args:
            filepath: Ruta del archivo de destino
            format: Formato de exportación ('json' o 'csv')
        """
        data = {
            'analyzer_name': self.name,
            'total_analyses': self.total_analyses,
            'texts_analyzed': self._texts_analyzed
        }
        
        filepath = Path(filepath)
        
        if format.lower() == 'json':
            filepath.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
        elif format.lower() == 'csv':
            import csv
            with filepath.open('w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Analizador', 'Total Análisis', 'Texto'])
                for text in self._texts_analyzed:
                    writer.writerow([self.name, self.total_analyses, text])
        else:
            raise ValueError(f"Formato no soportado: {format}. Use 'json' o 'csv'")
        
        print(f"💾 Resultados exportados a {filepath} (formato: {format.upper()})")
    
    def batch_analyze(self, texts: List[str], show_progress: bool = True) -> List[TextStatistics]:
        """Análisis en lote con barra de progreso"""
        results = []
        total = len(texts)
        
        for i, text in enumerate(texts, 1):
            if show_progress:
                print(f"\r📊 Progreso: {i}/{total} ({i/total*100:.1f}%)", end='')
            results.append(self.analyze_text(text))
        
        if show_progress:
            print()  # Nueva línea
        
        return results
    
    def clear_cache(self) -> None:
        """
        Limpia el caché de resultados de análisis.
        Útil para liberar memoria o forzar re-análisis.
        """
        if hasattr(self.analyze_text, 'clear_cache'):
            self.analyze_text.clear_cache()
            print("🧹 Caché limpiado exitosamente")
        else:
            print("⚠️  No hay caché para limpiar")
    
    def reset_statistics(self) -> None:
        """
        Resetea todas las estadísticas del analizador.
        Mantiene las estrategias pero limpia historial.
        """
        self._texts_analyzed.clear()
        self.analysis_count = 0
        self.clear_cache()
        print("🔄 Estadísticas reseteadas")


# ============= FUNCIONES DE DEMOSTRACIÓN =============

@timing_decorator
def demo_basic_analysis():
    """Demostración de análisis básico"""
    with TextAnalysisContext("Análisis Básico"):
        analyzer = TextAnalyzer("Mi Analizador")
        
        # Agregar observadores
        stats_observer = StatisticsObserver()
        analyzer.attach(stats_observer)
        
        sample_text = """
        Python es un lenguaje de programación increíble y poderoso.
        Es excelente para análisis de datos, machine learning y desarrollo web.
        La comunidad de Python es genial y muy activa.
        Aprender Python es una decisión inteligente para cualquier programador.
        """
        
        stats = analyzer.analyze_text(sample_text)
        print(stats)
        print(f"\n📈 Hash del texto: {stats.text_hash}")
        print(f"🎯 Análisis realizados: {analyzer.total_analyses}")
        
        # Análisis de n-gramas
        bigrams = analyzer.generate_ngrams(sample_text, 2)
        print(f"\n🔤 Bigramas más comunes:")
        for ngram, count in bigrams.most_common(5):
            print(f"   {' '.join(ngram)}: {count}")
        
        # Análisis de palabras clave
        keyword_analysis = KeywordAnalysis().analyze(sample_text)
        print(f"\n🔑 Palabras clave detectadas:")
        for word, count, density in keyword_analysis['keywords'][:5]:
            print(f"   {word}: {count} veces ({density:.1f}% densidad)")
        
        # Preprocesamiento
        processed = analyzer.preprocess_text(sample_text)
        print(f"\n🔧 Texto preprocesado (primeros 100 caracteres): {processed[:100]}...")
        
        # Resumen de eventos
        print(f"\n📊 Eventos capturados: {stats_observer.get_summary()}")


@timing_decorator
def demo_parallel_analysis():
    """Demostración de análisis paralelo"""
    with TextAnalysisContext("Análisis Paralelo"):
        analyzer = TextAnalyzer()
        
        texts = [
            "Python es increíble para ciencia de datos.",
            "Machine learning con Python es genial.",
            "El desarrollo web con Django es excelente.",
            "La sintaxis de Python es limpia y elegante.",
            "Programar en Python es muy productivo."
        ]
        
        results = analyzer.parallel_analysis(texts, max_workers=3)
        
        print(f"\n📚 Analizados {len(results)} textos en paralelo:")
        for i, stat in enumerate(results, 1):
            print(f"\n   Texto {i}: {stat.total_words} palabras, "
                  f"sentimiento: {stat.sentiment_score:.2f}")


async def demo_async_analysis():
    """Demostración de análisis asíncrono"""
    print("\n🚀 Iniciando análisis asíncrono...")
    
    analyzer = TextAnalyzer()
    texts = [
        "Async/await en Python es poderoso.",
        "La programación concurrente mejora el rendimiento.",
        "Python 3.11 es más rápido que nunca.",
    ]
    
    results = await analyzer.analyze_async(texts)
    print(f"✅ Análisis asíncrono completado: {len(results)} textos procesados")


def demo_generators():
    """Demostración de generadores"""
    print("\n🔄 Demostración de Generadores:")
    
    text = "Python es genial para programación funcional y orientada a objetos"
    
    # Uso de generador con comprensión
    long_words = (word for word in word_generator(text) if len(word) > 5)
    print(f"   Palabras largas: {list(long_words)}")
    
    # N-gramas
    trigrams = list(ngram_generator(text, 3))
    print(f"   Trigramas encontrados: {len(trigrams)}")
    print(f"   Primeros 3: {trigrams[:3]}")


def demo_decorator_retry():
    """Demostración del decorador retry"""
    @retry(max_attempts=3, delay=0.5)
    def unstable_function(should_fail: bool = False):
        if should_fail:
            raise ValueError("Fallo simulado")
        return "¡Éxito!"
    
    print("\n🔁 Demostración de Retry Decorator:")
    result = unstable_function(False)
    print(f"   Resultado: {result}")


def demo_text_comparison():
    """Demostración de comparación de textos"""
    print("\n🔍 Demostración de Comparación de Textos:")
    
    analyzer = TextAnalyzer()
    
    text1 = "Python es excelente para ciencia de datos y análisis."
    text2 = "Python es genial para machine learning y análisis de datos."
    
    comparison = analyzer.compare_texts(text1, text2)
    
    print(f"   Texto 1: {text1}")
    print(f"   Texto 2: {text2}")
    print(f"\n   📊 Resultados:")
    print(f"      - Similitud: {comparison['similarity_score']:.2%}")
    print(f"      - Diferencia de palabras: {comparison['word_diff']}")
    print(f"      - Diferencia de sentimiento: {comparison['sentiment_diff']:.2f}")
    print(f"      - Diferencia de legibilidad: {comparison['readability_diff']:.2f}")


def demo_advanced_features():
    """Demostración de características avanzadas"""
    print("\n🚀 Demostración de Características Avanzadas:")
    
    analyzer = TextAnalyzer()
    
    # Usando functools
    from functools import reduce
    texts = [
        "Python es increíble.",
        "Programar es divertido.",
        "La tecnología avanza rápido."
    ]
    
    # Combinar todas las palabras
    all_words = reduce(lambda a, b: a + list(word_generator(b)), texts, [])
    print(f"   Total de palabras combinadas: {len(all_words)}")
    
    # Usar métodos mágicos
    analyzer.analyze_text(texts[0])
    analyzer.analyze_text(texts[1])
    
    print(f"\n   📚 Usando métodos mágicos:")
    print(f"      - len(analyzer): {len(analyzer)}")
    print(f"      - analyzer[0]: {analyzer[0]}")
    print(f"      - 'Python' in analyzer[0]: {'Python' in analyzer[0]}")
    
    # Sliding window
    words = ['Python', 'es', 'un', 'lenguaje', 'poderoso']
    windows = list(sliding_window(words, 3))
    print(f"\n   🪟 Ventanas deslizantes (tamaño 3):")
    for window in windows:
        print(f"      {window}")


def demo_cache_management():
    """Demostración de gestión de caché"""
    print("\n🗄️  Demostración de Gestión de Caché:")
    
    analyzer = TextAnalyzer()
    
    # Analizar algunos textos
    texts = [
        "Python es un lenguaje increíble",
        "La programación es fascinante",
        "Python es un lenguaje increíble"  # Repetido para demostrar caché
    ]
    
    for text in texts:
        analyzer.analyze_text(text)
    
    # Mostrar estadísticas de caché
    cache_stats = analyzer.get_cache_stats()
    print(f"\n   📊 Estadísticas de Caché:")
    for key, value in cache_stats.items():
        print(f"      - {key}: {value}")
    
    # Exportar a CSV
    try:
        analyzer.export_results("resultados_test.csv", format='csv')
        print(f"   ✅ Exportación a CSV exitosa")
    except Exception as e:
        print(f"   ℹ️  Exportación omitida: {e}")


def demo_statistics():
    """Demostración de estadísticas avanzadas"""
    print("\n📈 Demostración de Estadísticas Avanzadas:")
    
    analyzer = TextAnalyzer()
    
    complex_text = """
    La inteligencia artificial está revolucionando múltiples industrias.
    Los algoritmos de aprendizaje automático procesan enormes cantidades de datos.
    Las redes neuronales profundas imitan el funcionamiento del cerebro humano.
    Esta tecnología está transformando fundamentalmente nuestra sociedad contemporánea.
    """
    
    stats = analyzer.analyze_text(complex_text)
    
    print(f"   📊 Estadísticas detalladas:")
    print(f"      - Diversidad léxica: {stats.lexical_diversity:.2%}")
    print(f"      - Nivel de complejidad: {stats.complexity_level.name}")
    print(f"      - Score de legibilidad: {stats.readability_score:.2f}")
    print(f"      - Total de oraciones: {stats.sentence_count}")
    
    # Exportar a JSON
    print(f"\n   📄 JSON generado:")
    print(stats.to_json())


# ============= PROGRAMA PRINCIPAL =============

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("=" * 80)
    print("🐍 SISTEMA AVANZADO DE ANÁLISIS DE TEXTO EN PYTHON 🐍")
    print("   Versión 2.2 - Análisis de Emociones + Gestión de Caché")
    print("   Nuevas características: Emociones detalladas, exportación CSV, caché stats")
    print("=" * 80)
    
    # Verificar Singleton
    analyzer1 = TextAnalyzer("Primer Analizador")
    analyzer2 = TextAnalyzer("Segundo Analizador")
    print(f"\n🔍 Verificación Singleton: {analyzer1 is analyzer2}")
    print(f"   Nombre del analizador: {analyzer1.name}")
    print(f"   Análisis soportados: {analyzer1.supported_analyses}")
    
    # Demostraciones
    demo_basic_analysis()
    demo_parallel_analysis()
    demo_generators()
    demo_decorator_retry()
    demo_text_comparison()
    demo_advanced_features()
    demo_cache_management()
    demo_statistics()
    
    # Análisis asíncrono
    asyncio.run(demo_async_analysis())
    
    # Resumen final
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL:")
    print(f"   Total de análisis realizados: {analyzer1.total_analyses}")
    print(f"   Textos en memoria: {len(analyzer1)}")
    print("✨ Todas las demostraciones completadas exitosamente ✨")
    print("=" * 80)


if __name__ == "__main__":
    main()
