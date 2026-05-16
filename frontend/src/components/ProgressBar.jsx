export default function ProgressBar({ progress }) {
  return (
    <div className="progress-wrapper fade-in">
      <div className="progress-header">
        <span>Processing</span>
        <span>{progress}%</span>
      </div>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${progress}%` }}
        />
      </div>
    </div>
  )
}