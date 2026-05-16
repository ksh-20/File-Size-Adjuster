# 🚀 File Size Adjuster

A modern production-ready full-stack web application that allows users to:

- Upload Images, PDFs, and DOCX files
- Increase or decrease file size
- Download processed files
- Preview uploaded files
- View processing progress
- Automatically clean temporary files

Built with:

- ⚛️ React.js + Vite
- ⚡ FastAPI
- 🎨 Modern Glassmorphism UI
- 🧠 Smart file processing logic
- 🔒 Secure upload handling

---

# ✨ Features

## 📂 Supported File Types

### Images
- JPG
- JPEG
- PNG
- WEBP

### Documents
- PDF
- DOCX

---

# ⚙️ Core Functionalities

## File Upload
- Drag and drop upload
- Click to upload
- MIME type validation
- Secure temporary storage
- Max upload size: 100MB

## File Size Adjustment

### Reduce File Size
- Image quality compression
- Intelligent resizing
- PDF optimization
- Embedded object compression

### Increase File Size
- Metadata/padding injection
- Maintains valid file structure
- Preserves visual quality

---

# 📊 Additional Features

- File preview
- Progress tracking
- Compression percentage
- Estimated processing time
- Responsive design
- Toast notifications
- Frontend processing history
- Auto cleanup after 5 minutes
- Cleanup after download

---

# 🧱 Project Structure

```txt
file-size-adjuster/
│
├── backend/
│   ├── app/
│   │   ├── config/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── temp/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── .env
│   ├── .env.example
│   └── README.md
│
└── README.md

```

# 🖥️ Frontend Setup
1. Navigate to frontend
cd frontend
2. Install dependencies
npm install
3. Create frontend .env

Inside:

frontend/.env

Add:

VITE_API_URL=http://localhost:8000
4. Start frontend
npm run dev

Frontend runs at:
http://localhost:5173

--- 

# ⚡ Backend Setup
1. Navigate to backend
cd backend
2. Create virtual environment
Windows
``` bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac
``` bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
pip install -r requirements.txt
4. Create backend .env

Inside:

backend/.env

Add:

TEMP_DIR=app/temp
MAX_FILE_SIZE=104857600
CLEANUP_MINUTES=5


## 📘 Backend Environment Variables Explained
Variable	Description
TEMP_DIR	Temporary file storage location
MAX_FILE_SIZE	Maximum upload size in bytes
CLEANUP_MINUTES	Auto delete timeout

## 📏 Upload Size Reference
Size	Bytes
10MB	10485760
50MB	52428800
100MB	104857600

## ▶️ Run Backend
``` bash
uvicorn app.main:app --reload
```

Backend runs at:

http://localhost:8000
🔌 API Documentation

FastAPI automatically provides Swagger documentation.

Open:
http://localhost:8000/docs

---

# 📡 API Endpoints
1. Upload File
Endpoint
POST /upload
Form Data
Key	Type
file	File
Example Response
{
  "file_id": "abc123.pdf",
  "filename": "sample.pdf",
  "size": 120394
}
2. Process File
Endpoint
POST /process
Request Body
{
  "file_id": "abc123.pdf",
  "target_size": 2,
  "unit": "MB",
  "operation": "decrease"
}
Parameters
Parameter	Values
operation	increase / decrease
unit	KB / MB
Example Response
{
  "processed_file_id": "newfile.pdf",
  "download_url": "/download/newfile.pdf",
  "final_size": 2019392
}
3. Download File
Endpoint
GET /download/{file_id}

Downloads processed file.

4. Cleanup File
Endpoint
DELETE /cleanup/{file_id}

Deletes temp file manually.

---

# 🧠 File Processing Logic
## 🖼️ Image Processing
Reduce Size
Compress image quality
Resize dimensions
Preserve aspect ratio
Increase Size
Add metadata/padding
Slight quality adjustment
Maintain valid image format

### Libraries used:
Pillow

## 📄 PDF Processing
Reduce Size
Compress embedded objects
Optimize PDF structure
Deflate streams
Increase Size
Add safe metadata/padding
Maintain valid PDF integrity

### Libraries used:
PyMuPDF
pikepdf

---

# 📝 DOCX Processing
Reduce Size
Optimize media
Compress internal zip structure
Increase Size
Add hidden padding
Maintain DOCX validity

---

# Libraries used:

python-docx
zipfile

--- 

# 🔒 Security Features
MIME type validation
Secure temporary storage
UUID file naming
Path traversal prevention
Max upload size restrictions
Auto cleanup scheduler

--- 

# 🧹 Cleanup System
Files are automatically deleted:

After successful download
After 5 minutes timeout
Manual cleanup endpoint

Cleanup service runs every 60 seconds.

---

# 🎨 UI/UX Features
Glassmorphism cards
Gradient backgrounds
Responsive layout
Animated transitions
Drag & drop upload
Hover effects
Progress animations
Dark premium theme
📱 Responsive Design

## Optimized for:

Desktop
Tablets
Mobile devices

---

# 🧪 Testing Checklist
## Test Uploads
JPG
PNG
WEBP
PDF
DOCX

## Test Operations
Increase file size
Decrease file size
Download output
Cleanup behavior

---

# 📦 Production Build
## Frontend
``` bash
npm run build
```

Generated files:

frontend/dist

--- 

# 🐳 Recommended Production Deployment
## Frontend
Vercel
Netlify
Nginx

## Backend
Render
Railway
VPS
Docker

---

# 🔧 Recommended Future Improvements
Queue system for heavy processing
WebSocket live progress
Redis caching
Multi-file batch processing
User authentication
Cloud storage integration
AI-based smart compression

---

# 🧑‍💻 Author

Kshitij S

---