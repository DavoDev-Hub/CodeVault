"""
Sistema Avanzado de Análisis de Texto con Procesamiento Concurrente
Demuestra: decoradores, context managers, generators, async/await, metaclases,
descriptores, threading, dataclasses, y patrones de diseño
"""

import asyncio
import time
import re
from typing import Dict, List, Tuple, Generator, Callable, Any
from dataclasses import dataclass, field
from functools import wraps
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
import statistics
from abc import ABC, abstractmethod


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
    """Estadísticas de texto"""
    total_words: int = 0
    total_chars: int = 0
    unique_words: int = 0
    avg_word_length: float = 0.0
    most_common: List[Tuple[str, int]] = field(default_factory=list)
    sentiment_score: float = 0.0
    
    def __str__(self) -> str:
        return f"""
📊 Estadísticas del Texto:
   - Palabras totales: {self.total_words}
   - Caracteres: {self.total_chars}
   - Palabras únicas: {self.unique_words}
   - Longitud promedio: {self.avg_word_length:.2f}
   - Score de sentimiento: {self.sentiment_score:.2f}
   - Palabras más comunes: {', '.join(f'{w}({c})' for w, c in self.most_common[:5])}
"""


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
    """Análisis de sentimiento simple"""
    POSITIVE_WORDS = {'bueno', 'excelente', 'genial', 'increíble', 'feliz', 'amor', 'perfecto'}
    NEGATIVE_WORDS = {'malo', 'terrible', 'horrible', 'triste', 'odio', 'error', 'problema'}
    
    def analyze(self, text: str) -> Dict[str, Any]:
        words = set(re.findall(r'\b\w+\b', text.lower()))
        positive = len(words & self.POSITIVE_WORDS)
        negative = len(words & self.NEGATIVE_WORDS)
        
        score = (positive - negative) / max(len(words), 1) * 100
        return {
            'sentiment_score': score,
            'positive_words': positive,
            'negative_words': negative
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


# ============= GENERADORES =============

def word_generator(text: str) -> Generator[str, None, None]:
    """Generador lazy de palabras"""
    for word in re.finditer(r'\b\w+\b', text.lower()):
        yield word.group()


def ngram_generator(text: str, n: int = 2) -> Generator[Tuple[str, ...], None, None]:
    """Generador de n-gramas"""
    words = list(word_generator(text))
    for i in range(len(words) - n + 1):
        yield tuple(words[i:i + n])


# ============= CLASE PRINCIPAL CON METACLASE =============

class SingletonMeta(type):
    """Metaclase Singleton"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TextAnalyzer(metaclass=SingletonMeta):
    """Analizador de texto avanzado (Singleton)"""
    
    name = ValidatedString(min_length=1, max_length=100)
    
    def __init__(self, name: str = "Analizador Principal"):
        self.name = name
        self.strategies: List[AnalysisStrategy] = []
        self.results_cache = {}
    
    def add_strategy(self, strategy: AnalysisStrategy):
        """Añade una estrategia de análisis"""
        self.strategies.append(strategy)
        return self
    
    @timing_decorator
    @cache_results(max_size=50)
    def analyze_text(self, text: str) -> TextStatistics:
        """Análisis completo del texto"""
        words = list(word_generator(text))
        
        # Análisis de frecuencia
        freq_result = FrequencyAnalysis().analyze(text)
        word_count = freq_result['word_count']
        
        # Análisis de sentimiento
        sentiment_result = SentimentAnalysis().analyze(text)
        
        # Calcular longitud promedio
        avg_length = statistics.mean([len(w) for w in words]) if words else 0
        
        return TextStatistics(
            total_words=len(words),
            total_chars=len(text),
            unique_words=len(set(words)),
            avg_word_length=avg_length,
            most_common=word_count.most_common(10),
            sentiment_score=sentiment_result['sentiment_score']
        )
    
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


# ============= FUNCIONES DE DEMOSTRACIÓN =============

@timing_decorator
def demo_basic_analysis():
    """Demostración de análisis básico"""
    with TextAnalysisContext("Análisis Básico"):
        analyzer = TextAnalyzer("Mi Analizador")
        
        sample_text = """
        Python es un lenguaje de programación increíble y poderoso.
        Es excelente para análisis de datos, machine learning y desarrollo web.
        La comunidad de Python es genial y muy activa.
        Aprender Python es una decisión inteligente para cualquier programador.
        """
        
        stats = analyzer.analyze_text(sample_text)
        print(stats)
        
        # Análisis de n-gramas
        bigrams = analyzer.generate_ngrams(sample_text, 2)
        print(f"\n🔤 Bigramas más comunes:")
        for ngram, count in bigrams.most_common(5):
            print(f"   {' '.join(ngram)}: {count}")


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


# ============= PROGRAMA PRINCIPAL =============

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("=" * 80)
    print("🐍 SISTEMA AVANZADO DE ANÁLISIS DE TEXTO EN PYTHON 🐍")
    print("=" * 80)
    
    # Verificar Singleton
    analyzer1 = TextAnalyzer("Primer Analizador")
    analyzer2 = TextAnalyzer("Segundo Analizador")
    print(f"\n🔍 Verificación Singleton: {analyzer1 is analyzer2}")
    print(f"   Nombre del analizador: {analyzer1.name}")
    
    # Demostraciones
    demo_basic_analysis()
    demo_parallel_analysis()
    demo_generators()
    demo_decorator_retry()
    
    # Análisis asíncrono
    asyncio.run(demo_async_analysis())
    
    print("\n" + "=" * 80)
    print("✨ Todas las demostraciones completadas exitosamente ✨")
    print("=" * 80)


if __name__ == "__main__":
    main()
