# SAGE RAG System - USB Autorun Setup

## Overview

This setup enables automatic startup of the SAGE RAG system when the USB drive is connected to a computer. The system automatically:

1. ✅ Detects the operating system (Windows/Linux)
2. ✅ Starts the backend server (Python/FastAPI)
3. ✅ Starts the frontend server (Node.js/Vite)
4. ✅ Opens the application in default browser

## Files Structure

```
D:/
├── autorun.inf              # Windows autorun configuration
├── autorun/
│   ├── autorun.bat          # Windows autorun startup script
│   ├── autorun.sh           # Linux autorun startup script
│   ├── detect_os.py         # OS detection script
│   ├── start_servers.bat    # Windows servers startup
│   └── start_servers.sh     # Linux servers startup
├── backend/                 # Backend application
├── frontend/                # Frontend application
├── python/                  # Portable Python installation
└── node/                    # Portable Node.js installation
```

## Windows Setup

### How It Works

When you connect the USB to a Windows computer:

1. **autorun.inf** triggers automatically (if AutoPlay is enabled)
2. Runs `autorun\autorun.bat`
3. Script calls `D:\python\python.exe autorun\detect_os.py`
4. Calls `start_servers.bat` to launch backend and frontend
5. Opens browser to `http://172.31.16.1:8080`

### Manual Trigger (if AutoPlay is disabled)

```cmd
D:\autorun\autorun.bat
```

Or double-click on `autorun.bat` in Windows Explorer.

### Requirements

- Windows 7, 10, 11, Server 2008+
- Python installed in `D:\python\`
- Node.js installed in `D:\node\`

## Linux Setup

### How It Works

On Linux, USB autorun is not automatically triggered. You need to:

1. Connect USB and find the mount point (e.g., `/media/user/SAGE`)
2. Run the autorun script manually

### Manual Trigger

```bash
# Find USB mount point
lsblk
# Mount if needed: sudo mount /dev/sdX1 /media/sage

# Run autorun
cd /media/sage  # or your mount point
bash autorun/autorun.sh
```

Or make it executable and double-click:

```bash
chmod +x autorun/autorun.sh
./autorun/autorun.sh
```

### Udev Rule for Auto-Trigger (Optional)

To auto-trigger on Linux, create `/etc/udev/rules.d/99-sage-usb.rules`:

```
SUBSYSTEM=="usb", ATTRS{idVendor}=="YOUR_VENDOR_ID", ATTRS{idProduct}=="YOUR_PRODUCT_ID", ACTION=="add", RUN+="/path/to/mount/script.sh"
```

## What Gets Started

### Backend Server
- **URL:** `http://172.31.16.1:8001`
- **Port:** 8001
- **Technology:** FastAPI (Python)
- **Location:** `D:\backend`
- **Runs with:** venv and uvicorn

### Frontend Server
- **URL:** `http://172.31.16.1:8080`
- **Port:** 8080
- **Technology:** Vite + React + Node.js
- **Location:** `D:\frontend`
- **Runs with:** npm dev server

## Network Access

The application is configured to listen on `0.0.0.0`:

- **Local:** `http://localhost:8080`
- **Network:** `http://172.31.16.1:8080`
- **Backend API:** `http://172.31.16.1:8001/api/v1/`

Replace `172.31.16.1` with your actual computer IP if different.

## Troubleshooting

### Windows: AutoPlay Not Triggering

1. **Enable AutoPlay:**
   - Open Settings → Devices → AutoPlay
   - Turn ON "Use AutoPlay for all media and devices"

2. **Manual Trigger:**
   ```cmd
   D:\autorun\autorun.bat
   ```

3. **Check autorun.inf:**
   - Ensure it's in the root directory (`D:\`)
   - Verify path to `autorun\autorun.bat` is correct

### Linux: Script Permission Issues

```bash
chmod +x autorun/autorun.sh
chmod +x autorun/detect_os.py
```

### Servers Won't Start

1. **Check Python path:**
   ```bash
   # Windows
   D:\python\python.exe --version
   
   # Linux
   /path/to/usb/python/bin/python3 --version
   ```

2. **Check Node path:**
   ```bash
   # Windows
   D:\node\npm --version
   
   # Linux
   /path/to/usb/node/bin/npm --version
   ```

3. **Check ports are available:**
   - Port 8001 for backend
   - Port 8080 for frontend

### Browser Won't Open

The script will print the URL. Open it manually:
- `http://172.31.16.1:8080`

### Servers Running But App Not Accessible

1. Check firewall settings
2. Verify network interface has IP `172.31.16.1`
3. Check if running on corporate network with restrictions

## Configuration Files

### `autorun.inf`
Controls Windows AutoPlay behavior

### `autorun.bat` & `autorun.sh`
Main startup scripts that:
- Detect OS
- Run servers
- Open browser

### `detect_os.py`
Detects OS and validates environment

### `start_servers.bat` & `start_servers.sh`
Starts backend (Python) and frontend (Node.js) in separate terminals

## Environment Variables Set

The system sets these automatically:

- `USB_ROOT` - Root directory of USB
- `PYTHON_PATH` - Path to portable Python
- `NODE_PATH` - Path to portable Node.js
- `PORT` - Backend port (8001)
- `ALLOWED_ORIGINS` - CORS allowed origins

## Security Notes

- ✅ Application only listens to 0.0.0.0 (all interfaces)
- ✅ Backend includes CORS restrictions
- ✅ No sensitive data stored locally
- ⚠️ Use in trusted networks only

## Performance

Typical startup time:
- **Backend initialization:** 2-3 seconds
- **Frontend dev server:** 3-5 seconds
- **Browser load:** 2-3 seconds
- **Total:** ~10 seconds

## Support

For issues or questions:
1. Check the logs in `D:\backend\logs\`
2. Check terminal output for error messages
3. Review this README
4. Check backend/frontend configuration files

## Version Info

- SAGE RAG System v1.0.0
- Python 3.13.x
- Node.js 24.11.0
- Vite + React
- FastAPI
