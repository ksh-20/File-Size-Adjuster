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


## 📝 DOCX Processing
Reduce Size
Optimize media
Compress internal zip structure
Increase Size
Add hidden padding
Maintain DOCX validity

### Libraries used:

python-docx
zipfile

--- 

# 🔒 Security Features
1. MIME type validation
2. Secure temporary storage
3. UUID file naming
4. Path traversal prevention
5. Max upload size restrictions
6.  Auto cleanup scheduler

--- 

# 🧹 Cleanup System
Files are automatically deleted:

After successful download
After 5 minutes timeout
Manual cleanup endpoint

Cleanup service runs every 60 seconds.

---

# 🎨 UI/UX Features
1. Glassmorphism cards
2. Gradient backgrounds
3. Responsive layout
4. Animated transitions
5. Drag & drop upload
6. Hover effects
7. Progress animations
8. Dark premium theme
9. 📱 Responsive Design

## Optimized for:

1. Desktop
2. Tablets
3. Mobile devices

---

# 🧪 Testing Checklist
## Test Uploads
1. JPG
2. PNG
3. WEBP
4. PDF
5. DOCX

## Test Operations
1. Increase file size
2. Decrease file size
3. Download output
4. Cleanup behavior

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
1. Vercel
2. Netlify
3. Nginx

## Backend
1. Render
2. Streamlit
3. Docker

---

# 🔧 Recommended Future Improvements
1. Queue system for heavy processing
2. WebSocket live progress
3. Redis caching
4. Multi-file batch processing
5. User authentication
6. Cloud storage integration
7. AI-based smart compression

---

# 🧑‍💻 Author

Kshitij S

---