"""
SAGE RAG System - Source Package
Educational Q&A system using ChromaDB and Phi-2 model
"""

__version__ = "1.0.0"
__author__ = "SAGE RAG System"
__description__ = "Portable RAG system for educational content"

# Import main classes for easy access
from .db_handler import ChromaDBHandler
from .llm_handler import Phi2Handler
from .rag_pipeline import RAGPipeline, RAGResponse
from .gui import NCERTRAGAssistantGUI
from .config_loader import ConfigLoader, Config, load_config

__all__ = [
    'ChromaDBHandler',
    'Phi2Handler', 
    'RAGPipeline',
    'RAGResponse',
    'NCERTRAGAssistantGUI',
    'ConfigLoader',
    'Config',
    'load_config'
]