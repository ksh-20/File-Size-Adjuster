export default function ResultCard({ result, originalSize }) {
  const finalSize = result.final_size

  const formatSize = (bytes) => {
    if (bytes < 1024) return `${bytes} B`

    if (bytes < 1024 * 1024) {
      return `${(bytes / 1024).toFixed(2)} KB`
    }

    return `${(bytes / (1024 * 1024)).toFixed(2)} MB`
  }

  const difference = (
    ((originalSize - finalSize) / originalSize) * 100
  ).toFixed(2)

  return (
    <div className="result-card glass-card fade-in">
      <h2>Processing Complete</h2>

      <div className="result-grid">
        <div>
          <p>Original Size</p>
          <h3>{formatSize(originalSize)}</h3>
        </div>

        <div>
          <p>Final Size</p>
          <h3>{formatSize(finalSize)}</h3>
        </div>

        <div>
          <p>Difference</p>
          <h3>{difference}%</h3>
        </div>
      </div>

      <a
        href={`http://localhost:8000${result.download_url}`}
        className="download-btn"
      >
        Download File
      </a>
    </div>
  )
}