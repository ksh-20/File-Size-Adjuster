import { useDropzone } from 'react-dropzone'
import { useState } from 'react'
import API from '../services/api'
import FilePreviewCard from './FilePreviewCard'
import ProcessingControls from './ProcessingControls'
import ProgressBar from './ProgressBar'
import ResultCard from './ResultCard'
import { useToast } from '../hooks/useToast'

export default function UploadArea() {
  const [file, setFile] = useState(null)
  const [target, setTarget] = useState('')
  const [unit, setUnit] = useState('KB')
  const [operation, setOperation] = useState('decrease')
  const [result, setResult] = useState(null)
  const [progress, setProgress] = useState(0)
  const [loading, setLoading] = useState(false)

  const toast = useToast()

  const onDrop = (acceptedFiles) => {
    const selected = acceptedFiles[0]

    if (!selected) return

    setResult(null)
    setFile(selected)

    toast.success('File selected successfully')
  }

  const { getRootProps, getInputProps } = useDropzone({
    multiple: false,
    maxSize: 100 * 1024 * 1024,
    onDrop
  })

  const simulateProgress = () => {
    let current = 0

    const interval = setInterval(() => {
      current += 10

      if (current >= 90) {
        clearInterval(interval)
      }

      setProgress(current)
    }, 300)

    return interval
  }

  const uploadAndProcess = async () => {
    if (!file) {
      toast.error('Please select a file')
      return
    }

    if (!target || Number(target) <= 0) {
      toast.error('Enter valid target size')
      return
    }

    try {
      setLoading(true)
      setProgress(0)

      const interval = simulateProgress()

      const formData = new FormData()
      formData.append('file', file)

      const uploadRes = await API.post('/upload', formData)

      const processRes = await API.post('/process', {
        file_id: uploadRes.data.file_id,
        target_size: Number(target),
        unit,
        operation
      })

      clearInterval(interval)

      setProgress(100)

      setResult(processRes.data)

      toast.success('File processed successfully')
    } catch (error) {
      toast.error(
        error.response?.data?.detail ||
        'Processing failed'
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="upload-container">
      <div {...getRootProps()} className="dropzone glass-card">
        <input {...getInputProps()} />

        <h2>Drag and Drop File or Click Here to Select File</h2>

        <p>Supports JPG, PNG, WEBP, PDF and DOCX extensions</p>
      </div>

      {file && (
        <FilePreviewCard file={file} />
      )}

      {file && (
        <ProcessingControls
          target={target}
          setTarget={setTarget}
          unit={unit}
          setUnit={setUnit}
          operation={operation}
          setOperation={setOperation}
          onProcess={uploadAndProcess}
          loading={loading}
        />
      )}

      {loading && (
        <ProgressBar progress={progress} />
      )}

      {result && (
        <ResultCard
          result={result}
          originalSize={file.size}
        />
      )}
    </div>
  )
}