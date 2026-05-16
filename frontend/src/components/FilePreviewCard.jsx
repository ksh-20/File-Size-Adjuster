import { FaFilePdf, FaFileWord, FaFileImage } from 'react-icons/fa'

export default function FilePreviewCard({ file }) {
  const getIcon = () => {
    if (!file) return null

    if (file.type.includes('image')) {
      return <FaFileImage className="preview-icon image" />
    }

    if (file.type.includes('pdf')) {
      return <FaFilePdf className="preview-icon pdf" />
    }

    return <FaFileWord className="preview-icon word" />
  }

  const formatSize = (bytes) => {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1024 * 1024) {
      return `${(bytes / 1024).toFixed(2)} KB`
    }

    return `${(bytes / (1024 * 1024)).toFixed(2)} MB`
  }

  return (
    <div className="preview-card glass-card fade-in">
      <div className="preview-header">
        {getIcon()}

        <div>
          <h3>{file.name}</h3>
          <p>{formatSize(file.size)}</p>
        </div>
      </div>

      {file.type.includes('image') && (
        <img
          src={URL.createObjectURL(file)}
          alt="preview"
          className="image-preview"
        />
      )}
    </div>
  )
}