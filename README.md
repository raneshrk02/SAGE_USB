# SAGE USB - Educational RAG System

A portable, USB-bootable educational chatbot system that provides intelligent Q&A capabilities for NCERT curriculum (Classes 1-12) using Retrieval-Augmented Generation (RAG).

## Overview

SAGE USB is a self-contained educational assistant that runs entirely from a USB drive. It combines a FastAPI backend with a React frontend to deliver an AI-powered question-answering system for students, requiring no internet connection once set up.

## Key Features

- **Portable**: Runs directly from USB drive with no installation required
- **Offline-First**: Works without internet connectivity using local LLM (Phi-2)
- **Educational Focus**: Optimized for NCERT curriculum across all grade levels (1-12)
- **Modern UI**: Beautiful React-based interface built with shadcn/ui components
- **Fast Retrieval**: ChromaDB vector database for efficient semantic search
- **Auto-Launch**: Automatic startup when USB is connected (Windows)

## Architecture

```
SAGE_USB/
├── backend/          # FastAPI + RAG Pipeline
│   ├── app/          # API endpoints and services
│   ├── src/          # Core RAG logic
│   └── models/       # Local LLM models (Phi-2)
├── frontend/         # React + TypeScript + Vite
│   ├── src/          # UI components and pages
│   └── dist/         # Production build
└── autorun/          # USB auto-start scripts
```

## Technology Stack

### Backend
- **FastAPI** - High-performance REST API
- **LangChain** - RAG orchestration
- **ChromaDB** - Vector database for embeddings
- **llama-cpp-python** - LLM inference (Phi-2 GGUF)
- **Sentence Transformers** - Text embeddings
- **gRPC** - High-performance RPC (optional)

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **shadcn/ui** - Component library
- **TanStack Query** - Data fetching
- **Tailwind CSS** - Styling

## Quick Start

### Prerequisites
- Windows 7+ or Linux
- USB drive with sufficient space (recommended 8GB+)
- Python 3.7+ (portable version included)
- Node.js 18+ (portable version included)

### Running from USB

**Windows:**
1. Insert USB drive
2. If AutoPlay is enabled, the system starts automatically
3. If not, run: `autorun\INSTALL.bat`
4. Browser opens to `http://localhost:8080`

**Linux:**
1. Mount USB drive
2. Navigate to mount point
3. Run: `bash autorun/autorun.sh`
4. Open browser to `http://localhost:8080`

### Development Setup

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /health` - Health check
- `POST /api/v1/chat` - Send chat messages
- `POST /api/v1/search` - Search educational content
- `GET /api/v1/admin/stats` - System statistics

## Configuration

Edit `backend/config.yaml` to customize:
- LLM parameters (temperature, max tokens, etc.)
- RAG settings (retrieval top-k, similarity threshold)
- ChromaDB collections
- Server ports and network settings

## Features

### Chat Interface
- Real-time responses with streaming support
- Markdown rendering for formatted answers
- Source citation with page references
- Context-aware follow-up questions

### Search
- Semantic search across all NCERT materials
- Filter by class level
- Relevance scoring
- Quick preview of results

### Admin Panel
- System health monitoring
- Performance metrics
- Database statistics
- Cache management

## Performance

- **Startup Time**: ~10 seconds
- **Query Response**: 2-5 seconds (depending on complexity)
- **Model Size**: ~1.6GB (Phi-2 quantized)
- **Memory Usage**: ~2-4GB RAM

## Ports

- **Frontend**: 8080
- **Backend API**: 8001
- **gRPC** (optional): 50051

## License

MIT License - Copyright (c) 2025 RANESH RK

See [LICENSE](LICENSE) for full details.

## Project Structure

```
backend/
├── app/
│   ├── api/v1/endpoints/  # REST endpoints
│   ├── core/              # Configuration & logging
│   ├── grpc_server/       # gRPC service
│   └── services/          # RAG manager
├── src/
│   ├── rag_pipeline.py    # RAG logic
│   ├── llm_handler.py     # LLM interface
│   └── db_handler.py      # ChromaDB wrapper
└── main.py                # FastAPI entry point

frontend/
├── src/
│   ├── components/        # React components
│   ├── pages/             # Route pages
│   ├── lib/               # Utilities & API client
│   └── hooks/             # Custom React hooks
└── dist/                  # Production build

autorun/
├── INSTALL.bat            # Windows installer
├── launcher.vbs           # Hidden launcher
└── detect_os.py           # OS detection
```

## Notes

- Designed for Python 3.7+ compatibility
- No external API dependencies once set up
- All models and data stored locally
- CORS configured for localhost access
- ChromaDB uses persistent storage on USB

## Support

For issues, check:
1. `backend/logs/` for error logs
2. Terminal output during startup
3. Browser console for frontend errors
4. `autorun/README.md` for USB setup details

## Version

**v1.0.0** - Initial Release